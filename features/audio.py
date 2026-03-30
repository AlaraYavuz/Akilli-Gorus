import base64
import json
from io import BytesIO

import streamlit as st
import streamlit.components.v1 as components
from gtts import gTTS


def speak_tr_text(text: str, *, rate: float, volume: float) -> None:
    js_text = json.dumps(text, ensure_ascii=False)
    js_rate = float(rate)
    js_volume = float(volume)

    components.html(
        f"""
<script>
  try {{
    const text = {js_text};
    const utter = new SpeechSynthesisUtterance(text);
    utter.lang = 'tr-TR';
    utter.rate = {js_rate};
    utter.volume = {js_volume};

    window.speechSynthesis && window.speechSynthesis.cancel();
    window.speechSynthesis && window.speechSynthesis.speak(utter);
  }} catch (e) {{
    console.error(e);
  }}
</script>
""",
        height=0,
    )


def stop_browser_speech() -> None:
    components.html(
        """
        <script>
          try {
            window.speechSynthesis && window.speechSynthesis.cancel();
          } catch (e) {}
        </script>
        """,
        height=0,
    )


@st.cache_data(show_spinner=False, ttl=60 * 60)
def gtts_to_mp3_bytes(text: str, lang: str = "tr") -> bytes:
    buf = BytesIO()
    tts = gTTS(text=text, lang=lang)
    tts.write_to_fp(buf)
    return buf.getvalue()


def autoplay_audio_mp3(mp3_bytes: bytes) -> None:
    b64 = base64.b64encode(mp3_bytes).decode("utf-8")
    components.html(
        f"""
<audio autoplay>
  <source src="data:audio/mpeg;base64,{b64}" type="audio/mpeg" />
</audio>
""",
        height=0,
    )


def clean_text_for_gtts(text: str) -> str:
    return (text or "").replace("**", "")

