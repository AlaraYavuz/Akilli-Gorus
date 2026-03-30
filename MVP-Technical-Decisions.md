# MVP Teknik Karar Özeti (Smart Vision v2.0)

Bu doküman, `tasks.md` içindeki **1. görev** kapsamında alınan teknik kararları tek yerde toplar.

## 1) Teknoloji seçimi
- **React Native (Expo)**: Hızlı geliştirme/iterasyon için seçildi.
- Amaç: MVP’de “uçtan uca akış” (kamera -> tespit/okuma -> sesli geri bildirim) mümkün olduğunca çabuk çalışsın; ileride native modül veya farklı framework’e geçiş ihtiyacı doğarsa mimari izin versin.

## 2) Modüler mimari
- `Navigation` (Ana Görüş, Akademi, Kişi Rehberi, Ayarlar)
- `Akademi`
  - OCR (Türkçe karakter desteği)
  - OCR çıktısını bağlama uygun özetleme/yorumlama (API opsiyonlu)
- `Kişi Rehberi`
  - Yüz kaydet/yeniden dene/sil prototipi
  - Tanıma sonucu güvenli ve anlaşılır bildirim
- `Ayarlar`
  - Yüksek kontrast (Siyah/Sarı)
  - Ses hızı/şiddeti
  - Dil/erişilebilirlik tercihleri

## 3) MVP minimum özellik seti
- Ana ekran: tam ekran kamera vizörü
- Güvenlik uyarısı: sınıf/öncelik bazlı temel seslendirme (ör. yaklaşan araç gibi kritik sınıflar daha önce)
- Komut: “Önümde ne var?” sesi/duyurusu
- Akademi: okuma modu + OCR sonucu ekran + sesli özet

## 4) Edge AI + API stratejisi
- **Cihazda (Edge)**
  - Kamera akışından hafif işleme (ön-işleme, tespit için uygun kare seçimi)
  - Temel OCR ve yüz tanıma prototipi (offline hedefi için)
- **API ile (Online opsiyon)**
  - Grafik/tablo ve formül açıklama (multimodal yorum)
  - OCR + bağlamlı doğal dil dönüşümü (robotik olmayan ton)
- **Offline davranış**
  - Tam multimodal açıklama yerine “kısmi sonuçlar”: nesne sınıfı + temel OCR çıktısı + sınırlı sesli geri bildirim

## 5) Model/servis gereksinimleri
- Nesne/engel tespiti: hafif TFLite modeli (öncelik: hızlı tepki)
- OCR: Türkçe karakterli OCR pipeline (cihazda mümkünse)
- Yüz tanıma: cihazda embedding çıkarımı + yakınlık tabanlı eşleştirme prototipi
- Grafik/tablo ve formül açıklama: Gemini benzeri multimodal model (API opsiyonlu)

