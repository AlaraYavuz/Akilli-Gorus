## Uygulama Geliştirme Görev Listesi (Smart Vision v2.0)

### 1) MVP kapsamı ve teknik kararlar
- [x] Python + Streamlit seçildi (başlangıç seviyesi için hızlı prototip ve tek dosyada çalışan MVP)
- [x] Uygulama mimarisi belirlendi: `Streamlit UI` (kamera yakalama + çıktı) + `Gemini Analysis` (görüntü -> Türkçe analiz metni)
- [x] MVP minimum özellikleri: web tarayıcıdan kamera ile kare yakalama (`st.camera_input`), Gemini 1.5 Flash ile görüntü analizi, sonucu Türkçe ekrana yazma
- [x] Edge AI yaklaşımı: MVP’de internetli Gemini API kullanılır; offline/cihaz üstü yaklaşım v2.1/v2.2’de ele alınır
- [x] Model/servis gereksinimleri: Gemini 1.5 Flash (vision + Türkçe), OCR/yüz tanıma gibi ek modüller sonraki görevlerde (buna uygun kod yapısı eklenecek)

### 2) Proje iskeleti ve altyapı
- [x] Streamlit proje iskeletini oluştur (tema/kontrast, erişilebilirlik başlangıç ayarı)
- [x] Kamera altyapısını kur (web tabanlı: `st.camera_input` ile kare yakalama)
- [x] Ses altyapısını opsiyonel kur (tarayıcı `SpeechSynthesis` ile Türkçe metin seslendirme)
- [x] Offline/online durum yönetimini kur (API anahtarı yok / ağ yok gibi durumlarda anlaşılır hata mesajı)
- [x] Loglama ve metrik toplama iskeletini kur (analiz süresi ölçümü + basit log dosyası)

### 3) Navigasyon (Günlük Yaşam) Modülü
- [ ] Nesne/engel tespiti için ilk çalışan prototipi kur (kamera akışından tespit + sınıf listesi)
- [ ] Mesafe tahmini yaklaşımını seç (heuristic, model tabanlı veya cihaz özellikleri)
- [ ] Öncelikli uyarı sistemi uygula (güvenlik kritik nesneler diğerlerinden önce duyurulsun)
- [ ] Seslendirme tonunu/formatını belirle (uyarıcı vs açıklayıcı)
- [ ] “Önümde ne var?” gibi temel sesli komutları bağla
- [ ] Tepki süresi KPI ölçümünü entegre et (algılama -> sesli geri bildirim < 1.5 sn hedefi)

### 4) Akademi & Okuma Modu
- [ ] Okuma modu arayüzünü oluştur (odak çerçevesi, tarama çizgisi, analiz sonucu alanı)
- [ ] OCR altyapısını kur (Türkçe karakter desteği)
- [ ] OCR çıktısını doğal dile çevir (robotik olmayan, bağlama uygun özet)
- [ ] Grafik/tablo analiz akışını kur (OCR + Gemini/MM modellere yönlendirme veya edge yaklaşımı)
- [ ] Matematik formül analizi yaklaşımını kur (LaTeX tabanlı yorum hedefi)
- [ ] “Grafiği açıkla” komutunu sesli kullanım için ekle
- [ ] Akademik doğruluk için değerlendirme yöntemi tanımla (hedef %90)

### 5) Kişi Rehberi (Yüz Tanıma)
- [ ] Rehber ekranını tasarla/uygula (büyük dokunsal butonlar, geri bildirim)
- [ ] Yüz verisini toplama akışı oluştur (kaydet, yeniden dene, sil)
- [ ] Yüz tanıma prototipini entegre et (>= %95 hedef doğruluk için iterasyon planı)
- [ ] Tanıma sonucunu kullanıcılara güvenli biçimde bildir (sesli uyarı + ekrana görsel geri bildirim)
- [ ] Gizlilik yaklaşımını uygula (mümkünse cihaz üzerinde, istenirse şifreli saklama)

### 6) Ayarlar & Ses / Erişilebilirlik
- [ ] Yüksek kontrast (Siyah/Sarı) temayı uygula
- [ ] Ses hızı, ses yüksekliği ve okuma modu tercihlerini ekle
- [ ] Yerel dil ayarlarını (TR) ve temel metin erişilebilirliğini ekle
- [ ] WCAG 2.1’e uyum kontrol listesi oluştur ve UI üzerinde düzeltmeler yap

### 7) Arayüz bütünleştirme ve kullanıcı akışları
- [ ] 4 ana ekranın navigasyon akışını kur (Ana Görüş, Akademi, Kişi Rehberi, Ayarlar)
- [ ] Modlar arası geçişi eller serbest olacak şekilde iyileştir (sesli komut/duyuru mantığı)
- [ ] Hata durumları için kullanıcıya anlaşılır geri bildirim ver (mikrofon/izin/kamera yok vb.)
- [ ] Performans optimizasyonları yap (FPS düşüşleri, gecikme azaltma, bellek yönetimi)

### 8) Başarı metrikleri ve doğrulama
- [ ] Tepki süresi test senaryolarını yaz ve ölç (tepki süresi KPI)
- [ ] Grafik/formül değerlendirme setiyle doğrulama yap (akademik doğruluk KPI)
- [ ] Kullanıcı testleriyle erişilebilirlik bulgularını topla (WCAG hedefi)
- [ ] İnternetsiz kullanım senaryolarını doğrula (Edge AI beklentisi)

### 9) Yayına hazırlık (v2.0 için)
- [ ] Güvenlik risklerini gözden geçir (kritik uyarıların önceliği, yanlış pozitif/negatif)
- [ ] Model/ayar parametrelerini ince ayar yap (zaman içinde doğruluk iyileştirme)
- [ ] Uygulama içi dokümantasyon ve kullanım kılavuzunu hazırlayarak teslim et
