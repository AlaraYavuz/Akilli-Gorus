# Akıllı Görüş (Smart Vision) v2.0

Akıllı Görüş, görme engelli bireylerin çevresindeki nesneleri ve metinleri daha erişilebilir hale getirmeyi amaçlayan, yapay zeka destekli bir görüntü analiz uygulamasıdır.  
Bu MVP sürümünde kullanıcı kameradan görüntü alır, Gemini API ile analiz eder ve sonucu Türkçe metin/ses olarak alır.

## Projenin Amacı

- Kameradan alınan görüntüyü yapay zeka ile analiz etmek
- Nesne ve yazıları Türkçe, anlaşılır bir dille açıklamak
- Sonucu hem ekranda göstermek hem de sesli geri bildirim sağlamak
- Erişilebilirlik odaklı, hızlı prototip geliştirme altyapısı sunmak

## Kullanılan Teknolojiler

- **Python**: Uygulama geliştirme dili
- **Streamlit**: Web arayüzü ve hızlı prototipleme
- **Gemini API**: Görüntü analizi ve metin üretimi
- **gTTS (Google Text-to-Speech)**: Türkçe metni sese dönüştürme

## Proje Yapısı

```text
.
├── app.py
├── features
│   ├── vision.py
│   └── audio.py
├── PRD.md
├── tasks.md
└── README.md
```

- `app.py`: Ana Streamlit uygulaması
- `features/vision.py`: Gemini analiz fonksiyonları
- `features/audio.py`: gTTS ve tarayıcı TTS fonksiyonları

## Kurulum

### 1) Gereksinimler

- Python 3.10+
- İnternet bağlantısı (Gemini API ve gTTS için)
- Geçerli bir Gemini API anahtarı

### 2) Bağımlılıkların yüklenmesi

Proje klasöründe aşağıdaki komutu çalıştırın:

```bash
pip install streamlit gTTS
```

> Not: Uygulama Gemini API çağrılarını standart Python HTTP kütüphanesi ile yapar; ek Gemini SDK kurulumu zorunlu değildir.

### 3) API anahtarının ayarlanması

Gemini anahtarınızı ortam değişkeni olarak tanımlayın:

- **Windows (PowerShell)**:

```powershell
$env:GEMINI_API_KEY="BURAYA_API_ANAHTARINIZ"
```

Alternatif olarak uygulama açıldığında sol paneldeki **Gemini API Anahtarı** alanına da manuel girebilirsiniz.

## Çalıştırma

Proje klasöründe:

```bash
streamlit run app.py
```

Ardından tarayıcıda açılan uygulamada:

1. Kameradan bir kare yakalayın  
2. **Analiz Et** butonuna basın  
3. Sonucu Türkçe metin olarak görüntüleyin ve isterseniz seslendirin

## Temel Özellikler

- Kamera üzerinden görüntü alma (`st.camera_input`)
- Gemini ile detaylı Türkçe görsel analiz
- Model fallback stratejisi (uygun model/sürüm denemesi)
- gTTS ile otomatik seslendirme (MP3 autoplay)
- Tarayıcı tabanlı manuel seslendirme seçenekleri

## Notlar

- gTTS ve Gemini API internet gerektirir.
- API anahtarınızı paylaşmayın ve doğrudan kaynak kod içine yazmayın.
- `app.log` dosyasında uygulama çalışma günlükleri tutulur.

