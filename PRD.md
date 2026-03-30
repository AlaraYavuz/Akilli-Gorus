# 📄 Kapsamlı PRD: Akıllı Görüş (Smart Vision) v2.0

**Proje Sahibi:** Alara Yavuz  
**Konsept:** Görme Engelliler İçin Bağımsız Yaşam ve Akademik Başarı Asistanı  
**Durum:** Taslak / Geliştirme Aşamasında

---

## 1. Ürün Özeti & Hedef
**Akıllı Görüş**, görme engelli bireylerin günlük hayatta bağımsız hareket etmelerini desteklerken, eğitim hayatındaki görsel bariyerleri (grafikler, formüller, tahta notları) yapay zeka ile ortadan kaldıran düşük maliyetli bir **web tabanlı MVP prototipidir** (ileride mobil arayüz genişletilecektir).

## 2. Kullanıcı Hikayeleri (User Stories)
* **Günlük Yaşam:** "Bir kullanıcı olarak, önümdeki engelleri ve yaklaşan araçları duymak istiyorum ki güvenle yürüyebileyim."
* **Eğitim/Akademi:** "Bir öğrenci olarak, ders kitabındaki bir grafik veya matematik formülünün ne anlama geldiğini duymak istiyorum ki derslerimde geri kalmayayım."
* **Sosyal/Kişisel:** "Bir kullanıcı olarak, karşımdaki arkadaşımı tanımak ve bir ürünün son kullanma tarihini kimseye sormadan öğrenmek istiyorum."

---

## 3. Fonksiyonel Gereksinimler (Teknik Yetenekler)

### A. Bilgisayarlı Görü ve Analiz (AI Core)
* **Nesne & Engel Tespiti:** Canlı video akışında nesneleri (basamak, kapı, araç) tanımlama ve mesafe tahmini.
* **Akademik Analiz Modülü:** Karmaşık grafikleri, tabloları ve matematiksel formülleri (LaTeX tabanlı) sese dönüştürme.
* **OCR (Optik Karakter Tanıma):** Türkçe karakter desteğiyle tabelaları, menüleri ve ders notlarını okuma.
* **Yüz Tanıma:** Rehberdeki kişileri %95 doğrulukla tanıma ve kullanıcıya bildirme.

### B. Akıllı Seslendirme ve Etkileşim
* **Öncelikli Uyarı Sistemi:** Güvenlik kritik nesneleri (örn: yaklaşan araba) diğer betimlemelerin önüne alma.
* **Sesli Komut Desteği:** "Önümde ne var?", "Grafiği açıkla" gibi komutlarla eller serbest kullanım.
* **Doğal Dil İşleme (NLP):** Bilgiyi robotik bir sesle değil, bağlama uygun (uyarıcı veya açıklayıcı) bir tonla aktarma.

---

## 4. Ekran Tasarımları & Arayüz (UI/UX)

| Ekran Adı | Görsel Özellik | Fonksiyon |
| :--- | :--- | :--- |
| **1. Ana Görüş (Navigasyon)** | Tam ekran kamera vizörü | Günlük hareket ve engel tanıma. |
| **2. Akademi & Okuma Modu** | Odak çerçevesi & Tarama çizgisi | Kitap sayfası, grafik ve formül analizi. |
| **3. Kişi Rehberi** | Büyük, dokunsal geri bildirimli butonlar | Tanıdık yüzleri kaydetme ve yönetme. |
| **4. Ayarlar & Ses** | Yüksek kontrast (Siyah/Sarı) | Ses hızı, Offline mod ve yerel dil ayarları. |

---

## 5. Farklılaştırıcı Unsurlar (Pazar Avantajı)

1.  **Ekonomik Erişilebilirlik:** 2000-3000 dolarlık donanımlar yerine, akıllı telefon + düşük maliyetli (3D yazıcı üretimi) aparat çözümü.
2.  **Akademik Odak:** Rakipler sadece nesne tanırken, Akıllı Görüş bir "eğitim asistanı" gibi grafikleri ve ders materyallerini yorumlar.
3.  **Yerelleştirme:** Türkiye'deki sokak yapısı, yerel market ürünleri ve Türkçe akademik müfredat ile tam uyum.
4.  **Hız ve Gizlilik (Edge AI):** Veriyi buluta göndermeden cihaz üzerinde işleyebilme yeteneği (İnternetsiz çalışma). Not: MVP’de Gemini API (bulut) kullanılacak; Edge AI tarafı sonraki iterasyonda güçlendirilecektir.

---

## 6. Teknik Teknoloji Yığını (Tech Stack)
* **Frontend:** Python + Streamlit (web arayüz MVP).
* **AI / Vizyon Analizi:** Google Gemini 1.5 Flash (API üzerinden multimodal analiz).
* **API:** Google Generative Language API (görüntü + Türkçe talimat -> çıktı).
* **Seslendirme (MVP opsiyonel):** Tarayıcı `SpeechSynthesis` ile Türkçe metni seslendirme.

---

## 7. Başarı Metrikleri (KPI)
* **Tepki Süresi:** Algılama ile sesli geri bildirim arası < 1.5 saniye.
* **Akademik Doğruluk:** Grafik ve formül yorumlamada %90 başarı oranı.
* **Erişilebilirlik:** WCAG 2.1 standartlarına tam uyum.