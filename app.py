import logging
import os
import re
import time
from datetime import datetime, timezone
from pathlib import Path

import streamlit as st
from features.audio import (
    autoplay_audio_mp3,
    clean_text_for_gtts,
    gtts_to_mp3_bytes,
    speak_tr_text,
    stop_browser_speech,
)
from features.vision import gemini_analyze_image


APP_DIR = Path(__file__).resolve().parent
LOG_PATH = APP_DIR / "app.log"


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.FileHandler(LOG_PATH, encoding="utf-8"), logging.StreamHandler()],
)
logger = logging.getLogger("smart-vision")


def _redact_secrets(text: str) -> str:
    # Query string içindeki `key=` değerlerini maskele.
    return re.sub(r"(\bkey=)[^&\s]+", r"\1***", text or "")


st.set_page_config(page_title="Akıllı Görüş (Smart Vision) - Gemini", layout="centered")

st.title("Akıllı Görüş (Smart Vision) - Gemini Görüntü Analizi")

st.caption("Kameradan bir kare yakala → Gemini ile görüntüyü analiz et → sonucu Türkçe gör.")


st.sidebar.header("Ayarlar")
api_key_default = os.environ.get("GEMINI_API_KEY", "") or ""
secrets_key = ""
try:
    # Bazı kurulumlarda st.secrets farklı davranabilir, o yüzden try/except ile güvenli alıyoruz.
    secrets_key = st.secrets.get("GEMINI_API_KEY", "")  # type: ignore[attr-defined]
except Exception:
    secrets_key = ""
api_key = st.sidebar.text_input(
    "Gemini API Anahtarı",
    type="password",
    value=secrets_key or api_key_default,
    help="API anahtarını burada girebilir ya da bilgisayarda `GEMINI_API_KEY` olarak tanımlayabilirsiniz.",
)

preferred_model = st.sidebar.text_input(
    "Gemini Model (id veya models/id)",
    value="gemini-1.5-flash",
    help="Örn: `gemini-1.5-flash`, `gemini-1.5-flash-002`. Değilse diğer 1.5 flash varyantları otomatik denenir.",
)

high_contrast = st.sidebar.checkbox("Yüksek Kontrast (Siyah/Sarı)", value=True)
tts_enabled = st.sidebar.checkbox("Seslendir (tarayıcı)", value=False)
tts_rate = st.sidebar.slider("Ses Hızı", min_value=0.6, max_value=1.4, value=0.95, step=0.05)
tts_volume = st.sidebar.slider("Ses Şiddeti", min_value=0.0, max_value=1.0, value=1.0, step=0.05)
gtts_autoplay = st.sidebar.checkbox("gTTS ile otomatik oku (MP3)", value=True)

if high_contrast:
    st.markdown(
        """
        <style>
          body { background: #000000; color: #FFEB3B; }
          .stTextInput, .stTextArea, .stButton > button { color: #FFEB3B; }
          .stMarkdown, .stSubheader, .stCaption { color: #FFEB3B; }
        </style>
        """,
        unsafe_allow_html=True,
    )


prompt_default = (
    "Sen görme engelliler için ileri seviye bir görsel asistansın. "
    "Nesneleri sadece şekil olarak değil, işlevleriyle birlikte tanımla (Örn: Bu bir hesap makinesi). "
    "Eğer üzerinde yazı veya rakam varsa onları oku. "
    "Kullanıcının elinde ne tuttuğunu ve nesnenin özelliklerini detaylıca Türkçe anlat."
)

prompt = st.text_area("Analiz talimatı (Türkçe)", value=prompt_default, height=120)


image_file = st.camera_input("Kamerayı aç ve bir kare yakala")

if image_file is not None:
    # Streamlit UploadedFile: bytes olarak okunur
    image_bytes = image_file.read()
    mime_type = getattr(image_file, "type", None) or "image/jpeg"

    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(image_bytes, caption="Yakalanan kare", use_column_width=True)
    with col2:
        st.info("Analiz için `Analiz Et` butonuna basın. Bu işlem Gemini API ile yapılır.")

    if "last_result" not in st.session_state:
        st.session_state.last_result = ""
    if "last_latency_ms" not in st.session_state:
        st.session_state.last_latency_ms = None
    if "last_spoken_text_gtts" not in st.session_state:
        st.session_state.last_spoken_text_gtts = ""

    analyze_btn = st.button("Analiz Et", type="primary")
    if analyze_btn:
        if not api_key:
            st.error("Gemini API anahtarı gerekli. Sol taraftan anahtarı girin.")
        else:
            start = time.perf_counter()
            try:
                with st.spinner("Analiz Ediliyor... Lütfen bekleyin."):
                    result_text, model_meta = gemini_analyze_image(
                        image_bytes=image_bytes,
                        mime_type=mime_type,
                        prompt=prompt,
                        api_key=api_key,
                        preferred_model=preferred_model,
                    )
                # Streaming kapalı: cevabı tek parça alıp işlemeye devam ediyoruz.
                full_text = (result_text or "").strip()
                elapsed_ms = int((time.perf_counter() - start) * 1000)

                st.session_state.last_result = full_text
                st.session_state.last_latency_ms = elapsed_ms
                st.session_state.last_model_meta = model_meta

                # Analiz biter bitmez otomatik seslendirme (gTTS)
                if (
                    gtts_autoplay
                    and full_text
                    and full_text != st.session_state.last_spoken_text_gtts
                ):
                    try:
                        clean_for_tts = clean_text_for_gtts(full_text)
                        mp3 = gtts_to_mp3_bytes(clean_for_tts, lang="tr")
                        autoplay_audio_mp3(mp3)
                        st.session_state.last_spoken_text_gtts = full_text
                    except Exception as tts_err:
                        logger.exception("gtts_failed error_type=%s", type(tts_err).__name__)
                        st.warning("gTTS ile seslendirme başarısız oldu. (İnternet/erişim kısıtı olabilir.)")

                ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
                logger.info("analysis_success latency_ms=%s ts=%s", elapsed_ms, ts)
            except Exception as e:
                elapsed_ms = int((time.perf_counter() - start) * 1000)
                logger.exception(
                    "analysis_failed latency_ms=%s error_type=%s",
                    elapsed_ms,
                    type(e).__name__,
                )
                st.error(f"Analiz başarısız: {_redact_secrets(str(e))}")
else:
    st.session_state.setdefault("last_result", "")
    st.session_state.setdefault("last_latency_ms", None)
    st.session_state.setdefault("last_model_meta", {})
    st.session_state.setdefault("last_spoken_text_gtts", "")


if st.session_state.get("last_result"):
    st.subheader("Gemini Sonucu (Türkçe)")
    st.write(st.session_state.last_result)

    if st.session_state.get("last_latency_ms") is not None:
        st.caption(f"Analiz süresi (yaklaşık): {st.session_state.last_latency_ms} ms")
    if st.session_state.get("last_model_meta"):
        meta = st.session_state.last_model_meta
        st.caption(f"Kullanılan model: {meta.get('model_id')} (API: {meta.get('api_version')})")

    speak_btn = st.button("Duy (tarayıcı)", disabled=not tts_enabled)
    stop_btn = st.button("Durdur", disabled=not tts_enabled)

    if speak_btn and tts_enabled:
        speak_tr_text(
            st.session_state.last_result,
            rate=tts_rate,
            volume=tts_volume,
        )

    if stop_btn and tts_enabled:
        stop_browser_speech()

