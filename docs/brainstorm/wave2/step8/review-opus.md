# Serbest değerlendirme: 4 Twitch hackathon fikri

Değerlendiren: Opus (bağımsız) · 28 Ekim 2026
Okunan dosyalar: `docs/competition/rules.md`, `overview.md`, `resources.md` ve `paste-free-review.md`. Web aramasından gelen her iddianın linki metinde köşeli parantezle belirtildi; tam liste en sonda.

---

## Kısa cevap

- **Seçimim: Minefield.** İki şartım var: 29 Ekim'de T1'i geçmesi ve aynı gün yapılacak 20 dakikalık, kodsuz bir oyun testinde (aşağıda T0) gerçekten eğlenceli olması.
- **T1 kalır ama T1b geçerse: Checkpoint.** STT altyapısı aynı olduğu için geçişte kayıp olmaz. FAQ'yi ek özellik olarak değil, ürünün merkezi olarak kurgulayın.
- **İki ses testi de kalırsa: VAR.** ML riski taşımaz ve dört fikir içinde videosu en kolay anlaşılanıdır.
- **Tap on the Shoulder'ı yapmazdım.** Mühendisliği sağlam, ama jürinin ilk 10 saniyede "bunu OBS plugin'leri zaten yapıyor" deme riski dördü içinde en yüksek olan bu.

---

## Önce genel gözlemler (dört fikir için de geçerli)

1. **Jüri büyük ihtimalle videoya bakarak puanlayacak.** Kurallarda "Judges are not required to test the Project and may choose to judge based solely on the text description, images, and video" yazıyor, FAQ'de ise "Make your video count." Bu durumda "Design: fun to watch" kriteri pratikte videonun ilk 20 saniyesine bağlı.
2. **Değerlendirmede otomatik AI analizi kullanılabilir** (rules §6: "automated AI-driven analysis"). Proje açıklamasını dört kriterle birebir eşleşen başlıklarla yazın: Innovation / Potential Impact / Technological implementation + Codex / Design. Hem insan hem makine okuyucu aradığını kolayca bulur.
3. **Eşitlikte ilk bakılan kriter Innovation** (rules, Tie Breaking). Birbirine yakın iki projeden daha yenilikçi olanı öne geçer.
4. **Hackathon "with AI" diye çerçevelenmiş.** Overview'da "OpenAI and Twitch are teaming up to see what developers can build for the Twitch community with AI" yazıyor, etiketler arasında da "Machine Learning/AI" var. AI kullanmak zorunlu değil. Yine de yerelde Whisper (bir OpenAI modeli) çalıştıran bir proje bu çerçeveye kendiliğinden oturur. Minefield ile Checkpoint'te bu var, VAR ile Tap'te yok. Üstelik sizin en güçlü olduğunuz alan bu.
5. **Kalabalık fikir alanları.** Overview sayfası 473 katılımcı gösteriyor. "Streamer meşgulken chat'i özetleyen veya sıraya koyan AI" ile "AI chatbot" fikirlerinin en kalabalık kümeler olacağını tahmin ediyorum (bu bir tahmin, veri değil). Checkpoint ilk bakışta bu kümeye benziyor. Minefield'e benzeyen bir başvuru gelmesi ise düşük ihtimal.
6. **İki ek, kendi kuralınızla çelişiyor.** "No Twitch content kept beyond 24 h" kuralı koymuşsunuz. Oysa VAR'daki *Referee reputation* ile Minefield'daki *Bomb Squad table*, kullanıcı adlarını ve skorları yayınlar arasında SQLite'ta tutuyor. Ya kuralı netleştirin (örneğin yalnızca user_id ve sayaç tutulsun, 24 saat sonra silinsin) ya da bu iki eki kesin. Zaten ikisinin de demo değerini düşük buluyorum: yayınlar arası kalıcılık 3 dakikalık bir videoda gösterilemez.
7. **Sesin yayına sızma riski.** Tap'teki "sadece kulaklıkta" çalan chime ve benim Checkpoint için önerdiğim kulaklık TTS'i, OBS'in Desktop Audio yakalamasına düşerse yayına çıkar. En basit çözüm: sesi OBS içinde Audio Monitoring ayarı "Monitor Only (mute output)" olan bir Media Source ile çaldırmak.
8. **Son teslim saatindeki belirsizlik.** Son teslim 2 Kasım 14:00 PT. ABD'de yaz saati 1 Kasım 2026 Pazar günü bitiyor, yani o gün PT = PST (UTC−8). Bu da 22:00 UTC, yani **3 Kasım 01:00 TSİ** eder. Devpost başlığındaki "5:00pm EST" de bununla uyumlu. Ancak resources.md "9:00 PM UTC" diyor (bu yaz saatiyle yapılmış bir hesap ve 3 Kasım 00:00 TSİ'ye denk geliyor). Kaynaklar birbiriyle çelişiyor. Güvenli olan: **2 Kasım 23:00 TSİ'den önce Submit'e basın.** FAQ'ye göre taslak olarak kaydetmek teslim sayılmıyor.

---

## Fikir: Tap on the Shoulder

### İyi olan
- Herkesin tanıdığı gerçek bir sorunu ele alıyor. Snoop Dogg hikâyesi videonun anlatımı için çok iyi (görüntüsünü kullanmadan, sadece sözle veya metinle anlatarak).
- Asıl farkı gerçek: "you sound far away" ya da "game too loud" gibi durumları hiçbir OBS plugin'i göremez, bunları ancak insan yargısı fark eder.
- Chat'i OBS ile çapraz kontrol etmek zarif bir fikir ("chat + OBS: mic muted"): aynı soruna iki bağımsız tanık.
- Onay döngüsü iyi düşünülmüş. Fix zamanı artı tahmini stream delay'den önce gelen cevapları yok saymak ve sonuca "everyone heard it" yerine "chat confirmed" demek dürüst bir dil.
- Teknik risk düşük. obs-websocket'te `InputMuteStateChanged`, `InputVolumeMeters` (her 50 ms'de bir gelen yüksek hacimli olay) ve `GetSourceScreenshot` hazır duruyor [obs-websocket protocol].

### Kötü olan
- **Jüri algısı.** Video, OBS'in zaten görebildiği durumla açılıyor. Muted Notification 12 bini aşkın indirmeye sahip. Jüri ilk 5 saniyede "bunu biliyorum" diyebilir. Innovation açısından en zayıf kart bu.
- **Ölçek paradoksu.** "60 saniye içinde ≥2 farklı izleyici" kuralı, sorunun en sık yaşandığı yerde, yani 0–5 izleyicili yeni yayıncılarda, neredeyse hiç tetiklenmez. Büyük yayınlarda ise modlar ve ikinci monitör zaten var. Aracın asıl işe yarayacağı aralık (20–200 izleyici, kafası işe gömülü yayıncı) dar.
- **Olay seyrek.** Gerçek sorunlar haftada birkaç kez bile yaşanmayabilir. Calm mode bunu çözmüyor, ürünü bir "chat pet"e (Mochi, WooferBot) doğru kaydırıp odağı dağıtıyor.
- **Kurulum sürtünmesi.** QR eşleme, HTTPS, Wake Lock ve ikinci bir telefon gerekiyor. Bu hem sizin 2.5 saatinizi yiyor hem de kurulumu deneyecek biri için yük oluyor.
- **Anahtar kelime tespiti kırılgan.** "mic" kelimesi normal sohbette de geçer ("nice mic"), "far away" ise bağlama bağlı.

### Değiştirir, ekler, çıkarırdım
- **Kancayı tersine çevirin.** İlk 10 saniyede OBS'in göremediği "far away" vakası gösterilsin. Mute vakası ikinci ve destekleyici örnek olsun, en fazla 5 saniye sürsün.
- **Eşiği küçük yayınlara uydurun.** Tek bir rapor artı aynı yönde bir OBS sinyali alarm için yeterli olsun. Rapor mod, VIP veya düzenli bir izleyiciden geliyorsa tek rapor da yetsin.
- **Kelime listesi yerine küçük bir embedding sınıflandırıcı kullanın.** Birkaç örnek cümleyle "ses sorunu / görüntü sorunu / sorun değil" ayrımı yapsın. ML altyapınız zaten var, 30–45 dakika sürer ve yanlış pozitifleri ciddi oranda düşürür.
- **Yeni ek: sabitlenmiş onay mesajı.** Twitch, 15 Mayıs 2026'da Send Chat Message'a `pin` parametresini ekledi. Pinned Chat uç noktaları da Mayıs sonunda genel kullanıma açıldı [Twitch changelog]. Streamer alarmı gördüğü anda bot "✅ Streamer biliyor: mic kapalı, düzeltiliyor (ilk bildiren @ana)" mesajını sabitlesin, fix gelince sabitlemeyi kaldırsın. Bu "MIC MIC MIC" spam'ini keser, izleyiciye görünür bir döngü sunar ve Twitch'in yeni bir API'sini kullanmış olursunuz. Yaklaşık 0.5 saat sürer. Gerekli scope'u T5'te kontrol edin.
- **Wake Lock için HTTPS ile uğraşmayın.** Demoda telefonun otomatik kilidini kapatmak yeterli. Telefon yüzü aynı ağda düz HTTP/WS ile çalışabilir. HTTPS'i (tünel üzerinden) yalnızca uzaktaki modun kullanacağı sayfa için tutun.
- **Çıkarın:** End-of-stream issue report.

### Önerilen eklemeler hakkında
- **Soundcheck:** Bence en iyi ek. Aracı "nadir olay" ürünü olmaktan çıkarıp "her yayının başında kullanılan" bir ürüne çeviriyor. "chat: quiet · meter: −28 dB → raise mic" birleşimini başka bir yerde görmedim. Tutun.
- **Black or frozen screen:** Ucuz ve faydalı, ama yanlış pozitif riski var (koyu oyun sahneleri, duraklatma menüleri). Tek başına tetiklendiğinde sessizce "OBS şüpheleniyor" diye göstersin, alarm ancak chat de aynı şeyi söylediğinde çalsın.
- **Calm mode:** Bu 1 saati Soundcheck'e ve sabitlenmiş mesaja vermeyi tercih ederim. Tutacaksanız tek durumla sınırlayın: ilk kez yazan izleyiciye el sallamak.
- **End-of-stream report:** Kesin.

**Özet:** Mühendisliği en sağlam, "vay" etkisi en zayıf kart. Farkı gerçek ama ince, videoda anlatması da zaman alıyor.

---

## Fikir: VAR

### İyi olan
- **Dördü içinde en kolay anlaşılan konsept.** VAR'ı herkes tanıyor; 2026 Dünya Kupası ABD, Kanada ve Meksika'da oynandığı için ABD'li jüri için de taze bir referans. "`!var` → siren → slow-mo → jüri → damga" akışı 3 saniyede kavranıyor. "Fun to watch" açısından dördün en iyisi.
- Chat'e gerçek bir güç veriyor (incelemeyi çağırmak ve jüri olmak). "Audience participation" temasına tam oturuyor.
- **Çıktısı paylaşılabilir:** başlıklı bir klip. Klipler Twitch'in büyüme motoru, dolayısıyla "community impact" hikâyesini anlatmak kolay.
- ML riski yok. Riskler OBS tesisatında ve gecikmede, ikisi de 29 Ekim'de ölçülebilir.
- **Self-VAR kartın en iyi buluşu.** Streamer'ın kendi iddiasını yargıya açması, kullanım alanını "tartışmalı an"dan "her türlü iddia ve böbürlenme"ye genişletiyor.

### Kötü olan
- **Yenilik orta düzeyde.** Parçaların hepsi zaten var: chat'le çağrılan replay, slow-mo'lu markalı replay, chat anketleri. Jüri projeyi "replay + poll" diye özetleyebilir. Ritüelin bütünü yeni olsa da Innovation'da orta sırada kalır.
- **Kullanım sıklığı düşük.** Çoğu oyunda sonucu oyunun kendisi belirliyor, gerçekten tartışmalı an az. Etkinin büyük kısmı self-VAR gibi bir içerik formatına dayanıyor.
- AI içermiyor. Ne "with AI" çerçevesinde ne de sizin ML gücünüzde puan topluyor.
- **Kartta olmayan bir teknik tuzak var.** OBS Media Source'ta `speed_percent` değiştiğinde kaynak baştan başlıyor. OBS kaynak kodunda bu ayar, değiştiğinde medyayı yeniden başlatan özellikler arasında sayılıyor ("Restart media source if these properties are changed") [obs-ffmpeg-source.c]. Yani "son 4 saniye yarı hızda" efekti, oynatma sürerken `SetInputSettings` ile yapılamaz. Ya iki ayrı dosya kullanmak ya da videoyu önceden render etmek gerekir.
- **Gecikme ofseti tahmine dayanıyor.** Twitch izleyici başına gecikmeyi vermiyor. Ofset ve nudge-back doğru çözüm, ama demoda replay ilk denemede doğru ana düşmezse sahne bozulur.

### Değiştirir, ekler, çıkarırdım
- **Replay hattını önceden render'a çevirin.** `ReplayBufferSaved` olayı kaydedilen dosyanın yolunu veriyor [obs-websocket protocol]. Akış şöyle olsun:
  1. ffmpeg ile dosyayı kesin.
  2. Son 4 saniyeye `setpts=2*PTS` uygulayın.
  3. Sona `tpad` ile donmuş bir kare ekleyin (telestrator için de hazır olur).
  4. `h264_nvenc` ile kodlayın; 10 saniyelik bir klip yaklaşık 1 saniye sürer.
  5. Sonucu Media Source'ta oynatın.

  2–3 saniyelik stinger bu işlem süresini gizler. Dikkat: OBS Windows'ta, sunucu ise WSL'de çalışıyor. Ya `C:\…` yolunu `/mnt/c/…` biçimine çevirin ya da ffmpeg'i Windows tarafında çalıştırın.
- **VAR pending'i varsayılan yapın ve orijinal anı VOD'dan kırpın.** İnceleme ertelendiğinde orijinal an, 60 saniyelik Create Clip penceresinin dışında kalır. Bunun çözümü **Create Clip From VOD**. Bu uç nokta Şubat 2026'dan beri genel kullanımda; klibin bittiği saniyeyi `vod_offset` ile siz seçiyorsunuz ve canlı yayın sırasında da çalışıyor [Twitch API reference, changelog]. Böylece iki klip çıkarırsınız: "an" ve "inceleme". Gereken scope `channel:manage:clips`; VOD storage marker için zaten açık olacak. Bunu T5'e ekleyin.
- Replay buffer'ın kayıt formatını (mkv veya mp4) T2'de sabitleyin. ffmpeg ikisini de işler.
- Videoda FIFA'nın ya da başka bir ligin görsel kimliğini kullanmayın (kurallar üçüncü taraf markalarını yasaklıyor). "VAR CHECK" sizin kendi tasarımınız olsun.

### Önerilen eklemeler hakkında
- **VAR pending:** Tutun. Kartın tek karşı sinyalini, yani streamer'ın replay'in ne zaman olacağını kontrol etme isteğini karşılıyor.
- **Telestrator:** Videoda çok iyi görünür, tutun. Ancak çizimi yalnızca streamer dock'tan yapsın; uzaktaki bir modun çizmesi ek bir sayfa ve login demek. Daha ucuz bir alternatif: tıklanan noktaya otomatik zoom ve halka (0.5 saat).
- **Referee reputation:** Kesin. Hem 24 saat kuralınızla çelişiyor hem de etkisi videoda gösterilemiyor. En fazla yayın içinde bir "Referee of the night" bırakın.

**Özet:** En güvenli "iyi video" bu. Ama Innovation ve Tech'teki tavanı sınırlı; ilk 5'e girmesi için cilasının kusursuz olması gerekir.

---

## Fikir: Checkpoint

### İyi olan
- **Gerçek ve belgelenmiş bir acıya dokunuyor:** kafası işe gömülü yayıncı, cevapsız kalan mesajlar, bu yüzden ayrılan izleyiciler. Streamlabs rehberi bu sorunun manuel çözümünü anlatıyor.
- **Döngüyü streamer'ın gerçek sözleriyle kapatıyor.** Bu duygusal olarak güçlü: izleyici duyulduğunu hissediyor, chat'teki diğer kişiler de soru-cevap çiftini görüyor.
- Ek donanım gerekmiyor ve izleyicinin hiçbir şey öğrenmesi gerekmiyor. "Easy to use" kriteri için ideal.
- **ML'e birebir uyuyor:** VAD, STT, güven kapısı ve embedding'li FAQ.
- **Doğal demo ortamı sizde hazır: kodlama yayını.** Software and Game Development kategorisinde siz zaten kafası işe gömülü kişisiniz; "what language is that?" sorusu kendiliğinden otantik olur. Çizim yapmanız gerekmez.
- **T1b, T1'den daha kolay bir test.** Gerçek zamanlı yanlış alarm şartı yok. Aksan riskinin en az zarar verdiği kart bu.

### Kötü olan
- **Fark ince ve yalnızca tek kaynakla (P) kontrol edildi.** Jüri ilk bakışta "soru kuyruğu + bot" görebilir (Meld, StreamerQnA). Sesin threaded reply'a dönüşmesi videonun ilk 15 saniyesinde net görünmezse kart sıradanlaşır.
- **Alıntının değeri sınırlı.** Yayını canlı izleyen kişi cevabı zaten duydu; alıntının asıl değeri yayından ayrılan ya da sonradan gelen izleyici için. Ancak Twitch Chat History, chat'e katılan birine yalnızca **son 50 mesajı ya da son 1 saati (hangisi daha azsa)** gösteriyor [Tubefilter]. Yoğun bir chat'te cevap bu pencerenin dışına kayar. Videodaki 1:00 sahnesi ("ayrılan izleyici sonradan dönüp cevabı buluyor") yalnızca sakin bir chat'te doğru. Ya bunu dürüstçe "in quiet chats" diye çerçeveleyin ya da o sahnenin yerine FAQ sahnesini koyun.
- **Bot, STT çıktısını herkese açık yazıyor.** Yanlış duyulmuş bir küfür bot hesabının başını yakar. Güven kapısı iyi bir önlem; ek olarak alıntıyı göndermeden önce bir blocklist'ten geçirin. `drop_reason` olay gerçekleştikten sonra gelir, önleyici değildir.
- **"Fun to watch" orta düzeyde.** Akış sakin ve sıcak, ama güldürmüyor.
- **"Heads-down" vaadinde bir delik var.** Streamer soruyu okumak için yine ekrana bakmak zorunda.

### Değiştirir, ekler, çıkarırdım
- **FAQ'yi ek özellik olarak değil, ürünün merkezi olarak kurgulayın.** Ürün cümlesi bence şu olmalı: *"Answer once, out loud. Every later asker gets your own words."* Tekrar eden sorular yayıncıların en bilinen yorgunluğu. Rakip LLM botları, örneğin StreamChat A.I., streamer'ın tanımladığı ya da chat'ten öğrenilen bir knowledge base'den cevap üretiyor [streamchatai.com]. Sizin sisteminiz ise streamer'ın gerçekten söylediği sözü, zaman damgası ve klibiyle, hiçbir şey uydurmadan aktarıyor. Bu yaklaşım Innovation ile Impact'i birlikte yükseltir.
- **FAQ eşleşmesine güven katmanları ekleyin:**
  - Benzerlik ≥0.85: otomatik cevap.
  - 0.70–0.85 arası: dock'ta tek tıkla onaylanan bir "bunu mu soruyor?" önerisi.
  - Daha düşük: mesaj normal bir kristal olarak kalır.

  MiniLM ile "what pen is that?" ve "which pen do you use?" gibi parafrazlar 0.85'in altında kalabilir. Eşiği 20–30 çiftlik küçük bir setle harness içinde ayarlayın.
- **Soruyu streamer'ın sadece kulaklığına okuyun.** Yerel bir TTS (örneğin Windows SAPI ya da Piper) kullanın ve sesi genel gözlem 7'deki gibi "Monitor Only" ile yayından ayırın. Böylece streamer gerçekten başını kaldırmadan cevap verebilir ve kartın vaadi tamamlanır. Yaklaşık 1 saat sürer ve Undo window'dan daha değerli.
- **Klip:** Create Clip From VOD ile `vod_offset`'i cevabın bittiği saniyeye ayarlayın; böylece pencere tam doğru olur [Twitch API reference]. Planınız zaten bunu yapıyor, iyi.

### Önerilen eklemeler hakkında
- **FAQ:** Tutun ve merkeze alın (yukarıda anlatıldığı gibi).
- **Clip link in the receipt:** Tutun. Videodaki "▶ watch it" anı iyi görünür.
- **Undo window:** Güvenlik açısından mantıklı, ama 0.5 saatlik görsel geri sayım yerine "son receipt'i geri çek" hotkey'i yeterli. Kazanılan süreyi kulaklık TTS'ine verin.

**Özet:** Dört kart içinde en faydalı ve riski en düşük ML kartı. FAQ merkeze alınırsa Innovation orta-yükseğe çıkar, ama Minefield kadar "vay" dedirtmez.

---

## Fikir: Minefield

### İyi olan
- **Dördün en yenisi.** Üç araştırmacının da farkın geçerli olduğunda hemfikir olduğu tek kart bu. Benim aramalarımda da (konuşma tanıma + izleyicinin gizlice seçtiği kelime) daha yakın bir ürün çıkmadı.
- **Oyun döngüsü kanıtlanmış (Don't Get Got), ortam yeni.** Gizli bilgi gerilim yaratıyor; patlayan bannerda mayını dikenin adının görünmesi izleyiciye tanınma veriyor; dud reveal da güzel bir kapanış.
- **Yayını ele geçirmiyor.** Konuşan her yayının arka planında çalışıyor; anket ya da oyun gibi içeriği durdurmuyor. Doğal yuvası izlenmenin %14.2'sini alan Just Chatting. Oyun gerekmediği için 1 saatlik Codex oyununa da ihtiyaç yok.
- Overview'daki "streamer distractions" yönüne oturuyor ama örneği kopyalamıyor.
- **Teknik hikâyesi dördün en güçlüsü:** gerçek zamanlı yerel Whisper (OpenAI modeli olduğu için "with AI" çerçevesine uyuyor), ölçülmüş doğruluk ve bir accuracy harness. Codex artifact'i olan harness, "Codex'i iyi kullandı mı?" sorusuna sayılarla cevap veriyor.
- **Demo otantik olur.** Kelimeleri arkadaşlarınız dikecek ve siz gerçekten bilmeyeceksiniz. Gerçek bir şaşkınlık, sahnelenmiş bir tepkiden çok daha iyi bir video çıkarır.

### Kötü olan
- **T1 eşiği zor.** Aksanlı ve gündelik konuşmada ≥%80 isabet ile 10 dakikada en fazla 1 yanlış alarm isteniyor. Üstelik yanlış alarm herkesin önünde patlıyor.
- **3 saniyelik gecikme komedi için fazla.** Espri, kelimeden hemen sonra gelen patlamada. 3 saniye sonra cümle çoktan bitmiş olur; hedef medyan ≤1.5 saniye olmalı (≤3 saniye en fazla p95 sınırı olarak kalsın). İyi haber şu: overlay yayına yerelde eklendiği için stream delay, kelimeyi ve patlamayı aynı miktarda kaydırıyor. Yani yalnızca STT gecikmesi önemli.
- **`hotwords` uydurma isabeti artırabilir.** faster-whisper'da `hotwords`, metne prompt öneki olarak ekleniyor [faster-whisper transcribe.py]; yani modeli o kelimeleri "duymaya" itiyor. Gerçek isabeti artırırken uydurma isabeti de artırır ve VAD tek başına bunu çözmez.
- **Oyun dengesi belirsiz.** Kelime çok zorsa hiçbir şey olmaz ve yayın sıkıcılaşır; çok kolaysa sürekli patlar. "Top-1000 kelimeden biri olmasın" kuralı kaba kalıyor. Streamer'ın zaten sık söylediği kelimeler (oyunun adı, kendi kalıp sözleri) de bedava patlama demek.
- Eğlencesi henüz doğrulanmadı ve bu oyun için doğrudan bir talep bulunamadı.
- **Kurulum sürtünmesi var.** Plant sayfası public bir URL ve Twitch login gerektiriyor. Gerçek izleyiciler üçüncü taraf bir login sayfasından çekinebilir.
- **Whisper intake (stretch) zayıf.** Whisper gönderen hesabın doğrulanmış bir telefon numarası olmalı; günde en fazla 40 farklı alıcı sınırı var ve mesajlar sessizce düşebiliyor [Streamer.bot docs, Twitch forum]. Test hesaplarınızda doğrulanmış telefon büyük ihtimalle yok. Kesin.

### Değiştirir, ekler, çıkarırdım
- **Day-1'e bir T0 testi ekleyin: 20 dakikalık, kodsuz bir Wizard-of-Oz oturumu.** Discord'da konuşurken iki arkadaşınız kelimelerini üçüncü bir arkadaşa DM ile göndersin. "Hakem" olan bu arkadaş kelimeyi duyunca bir tuşa bassın ya da sadece "BOOM" yazsın. Şunları ölçün: kaç kez gülündü, arkadaşlar ikinci bir tur istedi mi, ilk patlama kaçıncı dakikada geldi. Bu 20 dakika, kartın en büyük riskini (eğlence) hiç kod yazmadan test eder.
- **Güveni iki geçişle hesaplayın:**
  - (a) Hotword'süz geçişte kelime çıkıyor ve kelime olasılığı (`word_timestamps=True` ile gelir) eşiğin üstündeyse → anında patlama.
  - (b) Kelime yalnızca hotword'lü geçişte ya da fonetik bir yakın eşleşmede çıkıyorsa → Fuse.
  - (c) Diğer durumlar → yok sayılır.

  Eşikleri harness'taki ROC eğrisinden seçin ve videoda tablo olarak gösterin. 4070'te `small.en` ile iki geçiş rahatça sığar. Dropped frame görülürse STT'yi CPU'ya taşıyın (`base.en`, int8).
- **Kelime kuralları:**
  - Bir sıklık bandı uygulayın (örneğin `wordfreq` paketinin zipf değeri). Çok yaygın kelimeleri dışarıda bırakın; çok nadir olanları da, çünkü kimsenin yemleyemeyeceği nadir kelimeler hep dud kalır.
  - Streamer'ın son 30 dakikada söylediği kelimeleri yasaklayın. Bunun için yalnızca bellekte kelime sayımı tutun; ses kaydedilmez.
  - Yayın başlığındaki ve kategorideki kelimeleri yasaklayın.
  - Dikilen mayın 30–60 saniyelik bir "arming" süresinden sonra aktif olsun.
  - Blocklist'e ek olarak, modun gizlice veto edebileceği bir liste tutun. Bu, gerçek kişi adları gibi taciz amaçlı kelimelere karşı korur.
- **Plant sayfası:** Hiç scope istemeyen, yalnızca kimlik doğrulayan bir Twitch OAuth kullanın ve sayfayı `cloudflared` quick tunnel ile HTTPS üzerinden sunun. Sunucu token'ı `/oauth2/validate` ile doğrulasın. Sayfaya tek bir cümle yazın: "We only see your Twitch name."
- **Dock'a bir "konuşmayı yaz" modu ekleyin.** STT olmadan test etmeye yarar (jüri mikrofonsuz deneyebilir) ve kayıt sırasında STT tökezlerse sigorta olur. Bunu ilk gün yapın.
- **Klip:** DEFUSE penceresi bittiğinde (patlamadan 10 saniye sonra) Create Clip'i yaklaşık 25–30 saniyelik `duration` ile çağırın. Twitch'in varsayılan olarak pencerenin son 30 saniyesini yayınlaması [Twitch API reference], `duration`'ın da pencerenin sonundan sayıldığını düşündürüyor. Ama bu belgelenmemiş, T5'te ölçün. Sigorta olarak Create Clip From VOD ile kesin bir `vod_offset` kullanabilirsiniz.

### Önerilen eklemeler hakkında
- **Fuse:** En iyi ek. ML'deki belirsizliği oyun gerilimine çeviriyor ve yanlış alarm riskine karşı sigorta görevi görüyor. Tutun ve yukarıdaki iki geçişli güven hesabına bağlayın. Fuse'u yalnızca modun kesmesi yerine chat'in de kesebilmesini öneriyorum (aşağıda, kombinasyon 1).
- **Sweep:** İyi bir fikir. Streamer'ı kurban olmaktan çıkarıp oyuncu yapıyor; streamer'ın paranoyası içeriğin ta kendisi. Yine de Fuse ve chat jürisinden sonra, zaman kalırsa yapın.
- **Bomb Squad table:** Kesin. 24 saat kuralınızla çelişiyor ve videoda gösterilemiyor. Dud reveal ekranına yayın içi birkaç istatistik eklemek (0.25 saat) yeterli.
- **"Call it" (stretch):** Bunu da kesin; kartta ne olduğu bile net tanımlanmamış.

**Özet:** Tavanı en yüksek kart bu (Innovation, Design ve Tech'te), ama tek noktaya bağlı riski de en yüksek olan (T1). Bu risk 29 Ekim'de ucuza ölçülebiliyor ve yedeği olan Checkpoint aynı STT altyapısını kullanıyor.

---

## Yan yana (puan değil, kaba bir karşılaştırma)

| | Tap | VAR | Checkpoint | Minefield |
| --- | --- | --- | --- | --- |
| Innovation | düşük-orta | orta | orta-yüksek (FAQ merkezde olursa) | yüksek |
| Potential Impact | orta (olay seyrek) | orta (eğlence) | yüksek (fayda) | orta-yüksek (eğlence, konuşan her yayında çalışır) |
| Tech + Codex | orta | orta | yüksek | yüksek |
| Design / fun to watch | orta | çok yüksek | orta | yüksek |
| Ana risk | algı ("zaten var") | OBS tesisatı, gecikme | farkın ince olması | T1, eğlence |
| AI / ML | yok | yok | var | var |
| Gereken demo ortamı | masa (oyun isteğe bağlı) | masa malzemesi veya oyun | kodlama yayını | sohbet (oyun gerekmez) |

---

## Hangisini yapardım ve neden

**Minefield.** Gerekçelerim:

1. Dört kriterin üçünde (Innovation, Tech, Design) birinci ya da ikinci sırada. Eşitlikte ilk bakılan kriter de Innovation.
2. Sizin güçlü olduğunuz alan (ML ve Python) projenin tam kalbinde. Ölçülmüş bir doğruluk tablosu, "how well is it built" sorusuna kimsenin itiraz edemeyeceği bir cevap.
3. Videosu kendiliğinden komik ve otantik olur, 3 dakikada anlatması da kolay.
4. Benzer bir başvuru gelme ihtimali düşük.
5. Riski pahalı değil. 29 Ekim'de T0 ve T1 ile ölçülür; sonuç kötü çıkarsa aynı STT servisiyle Checkpoint'e geçersiniz.

**Karar ağacı (29 Ekim akşamı):**
- T1 geçti ve T0'da gülündü → **Minefield**.
- T1 geçti ama T0'da eğlence çıkmadı → **Checkpoint**. Bence en dürüst sinyal T0.
- T1 kaldı (örneğin yanlış alarm fazla) ama T1b geçti → **Checkpoint**, FAQ merkezde.
- T1 de T1b de kaldı → **VAR**.
- Hiçbir durumda Tap.

**Minefield için önerdiğim 12 saatlik paket:**

| Parça | Saat |
| --- | --- |
| Plant sayfası + login + tünel | 1.5 |
| STT spotter + iki geçişli güven + "konuşmayı yaz" modu | 2.5 |
| Kelime kuralları (sıklık bandı, son söylenen kelimeler, arming, blocklist) | 0.5 |
| Accuracy harness (Codex artifact) | 1 |
| Overlay: chips, explosion, banner | 2 |
| Marker, klip, DEFUSE, duds (+ yayın içi istatistik) | 1.5 |
| Fuse + chat itirazı (kombinasyon 1) | 1.5 |
| Polish | 1 |
| **Toplam** | **11.5** |
| Zaman kalırsa: Sweep | 1 |

**Takvim notu:** Arkadaşlarınızı şimdiden belirli bir saate bağlayın (örneğin 1 Kasım akşamı 1.5 saat). Minefield'ın videosu arkadaşların canlı katılımına bağlı; darboğaz koddan çok insanlar.

**Video akışında küçük değişiklikler (sizin storyboard'unuz üzerinden):**
- 0:00 Soğuk açılış, patlama. Olduğu gibi kalsın.
- 0:08 Tek cümlelik başlık kartı: "Chat plants secret words. Say one on stream, it explodes."
- 0:12 Arkadaşın telefonundan alınmış plant sayfası ekran kaydı. Kelimenin gizli kaldığını göstermek için gerekli.
- 0:50'deki ikinci turda yanlış alarmı Fuse ve chat itirazıyla gösterin; aksilik gag'e dönsün.
- 1:50 civarında harness tablosu (isabet, yanlış alarm, gecikme) 10 saniye ekranda kalsın.
- Codex thread'i için en az 20–30 saniye ayırın; kurallar bunu açıkça istiyor.

---

## Kombinasyon ve farklı fikir

1. **Minefield + "VAR-lite" itiraz.** Fuse yanarken ya da patlamadan hemen sonra 2 izleyici `!dud` yazarsa 10 saniyelik bir chat jürisi başlasın. Ekranda STT'nin yakaladığı cümle parçası, kelime vurgulanmış olarak görünsün ("…pineapple on pizza is…"); chat `!boom` / `!dud` diye oy versin. Bu, VAR'ın en iyi parçasını (jüri ritüelini) slow-mo tesisatına girmeden alır. Ayrıca modu olmayan küçük yayınlarda da çalışır ve "audience participation" temasını güçlendirir. Fuse'la birleşik maliyeti yaklaşık +0.5 saat. Sweep'ten önce bunu yapardım.
2. **Ortak STT servisi.** Bu bir kombinasyon değil, bir yatırım. Windows-native STT süreci (mic → VAD → faster-whisper → WebSocket) hem Minefield'da hem Checkpoint'te aynı. Bu yüzden 29 Ekim'de T1 ve T1b ile birlikte, base'in bir parçası gibi kurun. Hangi kararı verirseniz verin boşa gitmez (VAR seçilirse hariç).
3. **Farklı fikir (yalnızca bir not):** Minefield'ın ortak yayın sürümü. İki yayıncının toplulukları birbirlerinin yayıncısına mayın diker; bu "Streamer collaboration" temasına da girer. Bu hackathon için uygun değil (ikinci bir yayıncı gerektirir), ama videonun sonunda "next" olarak tek cümleyle anılabilir.

Bunun ötesinde fikir birleştirmeyin. 3 dakikalık bir videoda tek ürün, tek hikâye olmalı.

---

## Kaynaklar (web aramasından gelen iddialar)

- Twitch API reference: Create Clip (`title`, `duration` 5–60 s; varsayılan olarak pencerenin son 30 saniyesi yayınlanıyor) ve Create Clip From VOD (`vod_offset`, `channel:manage:clips` / `editor:manage:clips`, canlı yayın sırasında da çalışıyor): https://dev.twitch.tv/docs/api/reference/#create-clip
- Twitch changelog: Create Clip'e `title`/`duration` eklenmesi ve Create Clip From VOD'un open beta'ya çıkması (19 Aralık 2025), Create Clip From VOD'un genel kullanıma açılması (5 Şubat 2026), Send Chat Message'a `pin` parametresinin eklenmesi (15 Mayıs 2026) ve Pinned Chat'in genel kullanıma açılması (Mayıs 2026): https://dev.twitch.tv/docs/change-log/
- Twitch Chat History: katılımda son 50 mesaj ya da son 1 saat, hangisi daha azsa (Tubefilter, 2023): https://www.tubefilter.com/2023/02/07/twitch-chat-history-replay-conversation-streaming-platform/
- OBS Media Source'ta `speed_percent` değişince medyanın yeniden başlaması: https://github.com/obsproject/obs-studio/blob/master/plugins/obs-ffmpeg/obs-ffmpeg-source.c
- obs-websocket protokolü (`ReplayBufferSaved.savedReplayPath`, `GetLastReplayBufferReplay`, `InputVolumeMeters` her 50 ms'de bir, `InputMuteStateChanged`, `GetSourceScreenshot`): https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md
- faster-whisper'da `hotwords`'ün prompt öneki olarak kodlanması: https://github.com/SYSTRAN/faster-whisper/blob/master/faster_whisper/transcribe.py
- Whisper sınırları (gönderende doğrulanmış telefon, günde 40 farklı alıcı): https://docs.streamer.bot/api/csharp/methods/twitch/chat/send-whisper
- Whisper API'nin mesajları sessizce düşürmesi (geliştirici forumu): https://discuss.dev.twitch.tv/t/twitch-whispers-api-silently-drops-messages/56357
- StreamChat A.I. (otomatik soru-cevap ve "knowledge base about your stream"): https://www.streamchatai.com
- Aramada bulunamayanlar: izleyicinin gizlice seçtiği kelimeyi streamer'ın konuşmasında yakalayan bir Twitch aracı ve VAR tarzı, replay ile chat jürisini birleştiren bir overlay. İkisi için de birkaç farklı sorgu denendi; araştırmacıların bulgularından daha yakın bir şey çıkmadı.
