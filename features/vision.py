import base64
import json
import re
import urllib.error
import urllib.request


def _clean_api_key(raw: str) -> str:
    if not raw:
        return ""
    raw = str(raw).strip()
    m = re.search(r"(AIza[0-9A-Za-z\-_]+)", raw)
    return m.group(1) if m else raw


def _normalize_model_id(model_value: str) -> str:
    if not model_value:
        return ""
    model_value = str(model_value).strip()
    if model_value.startswith("models/"):
        return model_value[len("models/") :]
    return model_value


def gemini_analyze_image(
    *,
    image_bytes: bytes,
    mime_type: str,
    prompt: str,
    api_key: str,
    preferred_model: str,
) -> tuple[str, dict]:
    api_key = _clean_api_key(api_key)
    if not api_key:
        raise RuntimeError("Gemini API anahtarı boş/eksik görünüyor.")

    preferred_model = _normalize_model_id(preferred_model) or "gemini-1.5-flash"

    model_candidates = []
    for m in [
        preferred_model,
        "gemini-1.5-flash",
        "gemini-1.5-flash-latest",
        "gemini-1.5-flash-002",
        "gemini-1.5-flash-001",
        "gemini-2.5-flash",
        "gemini-2.0-flash",
    ]:
        n = _normalize_model_id(m)
        if n and n not in model_candidates:
            model_candidates.append(n)

    b64 = base64.b64encode(image_bytes).decode("utf-8")

    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {"text": prompt},
                    {
                        "inline_data": {
                            "mime_type": mime_type,
                            "data": b64,
                        }
                    },
                ],
            }
        ],
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 2048,
        },
    }

    last_http_error: Exception | None = None
    for api_version in ["v1beta", "v1"]:
        for model_id in model_candidates:
            endpoint = (
                "https://generativelanguage.googleapis.com/"
                f"{api_version}/models/{model_id}:generateContent?key={api_key}"
            )

            req = urllib.request.Request(
                endpoint,
                data=json.dumps(payload).encode("utf-8"),
                headers={"Content-Type": "application/json"},
                method="POST",
            )

            try:
                with urllib.request.urlopen(req, timeout=90) as resp:
                    raw = resp.read().decode("utf-8")
                data = json.loads(raw)

                text_parts = []
                for cand in data.get("candidates", []) or []:
                    content = cand.get("content", {}) or {}
                    for part in content.get("parts", []) or []:
                        if isinstance(part, dict) and "text" in part:
                            text_parts.append(part["text"])

                if text_parts:
                    complete_response = "\n\n".join([t for t in text_parts if t]).strip()
                    return (
                        complete_response,
                        {"model_id": model_id, "api_version": api_version},
                    )

                return (
                    (data.get("error", {}).get("message") or raw)[:2000],
                    {"model_id": model_id, "api_version": api_version},
                )

            except urllib.error.HTTPError as e:
                last_http_error = e
                continue
            except urllib.error.URLError as e:
                raise RuntimeError(
                    f"Gemini API'ye erişilemiyor (URL/bağlantı hatası). Detay: {e.reason}"
                ) from e

    if last_http_error:
        raise RuntimeError(
            "Gemini model(leri) bulunamadı veya generateContent desteklenmiyor. "
            "API anahtarını ve modele ait izinlerini kontrol edin."
        ) from last_http_error
    raise RuntimeError("Gemini analizi başarısız oldu.")

