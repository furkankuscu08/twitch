# Minefield planı: bağımsız inceleme (Opus)

İnceleme tarihi 28 Ekim 2026. İncelenenler: `docs/plan/minefield.md`, `SPEC.md`, `AGENTS.md`, yarışma dokümanları (`docs/competition/`), karar rehberi §6.1.
Twitch ve kütüphane bilgileri resmî dokümanlardan doğrulandı (bölüm 6). Hatalar dosyalarda düzeltildi; görüş gerektiren her şey aşağıda **öneri** olarak duruyor, dosyalara işlenmedi.

---

## 1. Özet

1. **Plan genel olarak sağlam; ama 3 Twitch bilgisi yanlış ya da eksikti, düzelttim.** Klip için 15 sn değil **60 sn** beklenmeli (Twitch dokümanı). EventSub `session_reconnect` sonrasında yeniden abone **olunmaz**; abonelikler yeni bağlantıya taşınır. Tünel arkasında "IP başına rate limit" bütün izleyicileri tek IP olarak görür; gerçek IP `CF-Connecting-IP` başlığında.
2. **Gizlilikte bir açık var: "elde sadece canlı olmayan kelimeler" kuralı canlı mayınları sızdırıyor.** `/api/hand` birkaç yüz kez çağrılırsa hiç çıkmayan 4 kelime, canlı mayınlardır. Bunu yapabilecek kişilerden biri yayıncının kendisi. Ucuz bir çözümü var (öneri 1).
3. **DEFUSE akışında oyun hatası var.** Patlama afişi kelimeyi herkese gösteriyor. DEFUSE sonrasında mayın yine `armed` oluyor, ama artık herkes kelimeyi biliyor; yayıncı da o kelimeden kaçar. DEFUSE edilen mayın kaldırılmalı ve sahibine yeniden ekme hakkı verilmeli (öneri 2).
4. **Harness'te görünmeyen insan saati var.** Kayıt (a) doğal konuşma; içinde geçen her deste kelimesi için elle etiket ve kelime **bitiş** zamanı gerekiyor. Kayıt (c) için de "etiketler betikten çıkar" deniyor, ama betik zaman vermiyor. Bu iş planda hiç yok: ~0,5–1 saat. Çözüm: bir etiket yardımcısı ve hipotez kaydının tekrar oynatılması (öneri 4).
5. **D3'ü kabul ediyorum, iki şartla:** saatler tek bir saat alanından ölçülsün (WSL saati kayabilir) ve 29 Ekim'deki CUDA kontrolüne 15 dk değil 45 dk ayrılsın; cuDNN 9 / cuBLAS 12 kurulumu ve `LD_LIBRARY_PATH` zaman alıyor. **D4'ü de kabul ediyorum.** Twitch OAuth'u telefonda, uygulama içi tarayıcıda baştan şifre ve 2FA ister; kod akışı bundan daha az sürtünmeli. Sayfada `!mine K7QF` için bir kopyala düğmesi olmalı; büyük/küçük harf ve boşluklar toleranslı ayrıştırılmalı.
6. **Bütçe gerçekçi değil: 27,5 saat, artı görünmeyen işler.** Etiketleme, Twitch hesap ve 2FA kurulumu, OBS ses yönlendirmesi ve README'deki jüri kurulumu ~2–3 saat daha ekliyor. Kesilmesi önerilenler: WP12 simülatörü yarıya indirilsin, "mayın tarama" ve Türkçe tamamen çıksın, DEFUSE'un geri sarma animasyonu basit bir damgaya insin (öneri 9).
7. **Video jüri için Twitch'te geçmeli.** Kural "projeyi Twitch'te çalışırken gösteren görüntü" istiyor. Soğuk açılışın ve en az bir patlamanın **twitch.tv oynatıcısı + chat** ekranından da kaydedilmesi gerekiyor; sadece OBS önizlemesi yetmeyebilir. Kelime → BOOM anı kesintisiz bırakılmalı (öneri 12).
8. **Jüri kurulabilirliği ve "Potential Impact" zayıf.** NVIDIA GPU + WSL + CUDA şartı, kodu deneyecek jürinin önünde büyük engel. CPU modu (`small.en`, int8) ve GPU'suz bir demo yolu (typed + debug plant + `/overlay?demo=1`) README'de olmalı (öneri 13).

---

## 2. Düzeltilen hatalar

| Dosya | Önce | Sonra | Kaynak |
| --- | --- | --- | --- |
| `SPEC.md` §6 Clip | "poll `GET /helix/clips?id=` for up to 15 s" | 60 sn'ye kadar bekle (dokümandan alıntıyla). Klip penceresinin notu eklendi: ~90 sn'lik pencere çağrıdan ~5 sn sonra biter; patlamadan 10 sn sonra yapılan çağrı ≈ patlama −15 sn … +15 sn aralığını kapsar. | Twitch API Reference, Create Clip: *"If after 60 seconds Get Clips hasn't returned the clip, assume it failed."* |
| `SPEC.md` §6 EventSub | "Handle `session_welcome`, keepalive timeout and `session_reconnect`, then resubscribe." | Welcome'dan sonra 10 sn içinde abone ol. `session_reconnect` gelince `reconnect_url`'e bağlan; eski soketi yeni welcome gelince kapat; **yeniden abone olma**. Keepalive zaman aşımında ya da kopmada yeni bağlantı aç ve abone ol; kaçan olaylar tekrar gönderilmez. | EventSub "Handling WebSocket events": *"The connection will include the same subscriptions that the old connection had"*, *"you have 10 seconds…"*, *"There is no replay of events that are lost."* |
| `SPEC.md` §4 Plant app | "Rate-limit per IP." | IP `CF-Connecting-IP` başlığından okunur, çünkü tünelden gelen her istek localhost'taki cloudflared'den geliyor. | Cloudflare: proxy'lenen isteklerde istemci IP'si `CF-Connecting-IP` ile iletilir. Tünel mimarisinin doğal sonucu. |
| `SPEC.md` §6 App | "refreshed on 401." | Ek: public client refresh token'ları tek kullanımlık ve 30 günlük; her yenilemede yeni refresh token saklanmalı. | Twitch "Getting OAuth Access Tokens" (DCF): *"one time use only"*; "Refreshing Access Tokens": public client token'ları 30 günde sona erer. |
| `SPEC.md` §7 Labels | `t` tanımsızdı | `t` = söylenen kelimenin **bitiş** zamanı (dosya başından saniye). Gecikme buradan ölçülür. | İç tutarlılık: plan T1 ve SPEC §5 kural 7 gecikmeyi "kelime bitişinden" tanımlıyor; etiketin tek zamanı başka bir şey olursa gecikme ölçülemez. |
| `minefield.md` §5 (WP tablosu altı) | "…o 0,5 saat düştü." (ama toplam 3,5 + 10,5 = 14 olarak kalıyor) | "…düştü; toplam yine 14, çünkü parçalar yeniden bölündü (örneğin çekirdek ve eşleştirici ayrı paket WP1 oldu)." | İç tutarlılık: 0,5 saat düşüp toplamın aynı kalması açıklanmamıştı. |
| `minefield.md` §6 (29 Ekim, sıra 1) | "bot hesabı + 2 test hesabı" | "bot hesabı + 3 test hesabı (WP12 simülatörü 3 hesap kullanıyor)" | İç tutarlılık: WP12 ve karar rehberi 3 test hesabı diyor. |
| `minefield.md` §2 MVP | "yayın sonunda dud'lar ve yayın içi sayaçlar" | "tur sonunda dud'lar ve tur içi sayaçlar" | İç tutarlılık: SPEC §3 dud'ları ve istatistikleri **tur** (round) sonuna bağlıyor. |
| `minefield.md` §9 çekim listesi | "1:25 Yayın sonu: dud'lar" | "1:25 Tur sonu: dud'lar" | Aynı nedenle. |

`AGENTS.md`'de nesnel bir hata bulmadım. Linkler (`../../AGENTS.md`, `../../SPEC.md`, karar rehberi, `#10-karar-günlüğü`) doğru. WP saatleri toplanınca 14 ediyor; insan saati toplamı 27,5 tutuyor.

Doğrulanan ve doğru bulunanlar:
- Marker: `POST /helix/streams/markers`, `channel:manage:broadcast`, canlı yayın + VOD şart.
- Clip: `clips:edit`, `title` ve `duration` (5–60 sn, varsayılan 30) parametreleri.
- Chat: `POST /helix/chat/messages` için `user:write:chat`; `channel.chat.message` v1 için kullanıcı token'ı ve `user:read:chat`.
- DCF: public client ile ve client secret olmadan çalışıyor.
- faster-whisper: `transcribe` parametrelerinin hepsi mevcut. `vad_filter` varsayılanı True, SPEC bunu doğru şekilde kapatıyor.
- Silero VAD: 512 örnek, yani 32 ms pencere.
- deepdml modelinin `config.json`'unda `alignment_heads` var, yani kelime zaman damgaları desteklenir.

---

## 3. Öneriler

Her biri için: ne, neden, maliyet, güven, öncelik.

**1. Eli tam desteden çek; çakışmayı seçim anında çöz.**
- **Ne:** `/api/hand` 6 kartı tüm desteden çeksin. `/api/pick` sırasında kelime canlıysa "taken, pick another" dönsün; bu durum zaten SPEC'te var.
- **Neden:** Şu anki kural ("not currently live") gizlilik değişmezini çiğniyor. Rate limit bunu sadece yavaşlatır. Yayıncı kendi makinesinde `curl` ile canlı kelimeleri bulabiliyorsa "kelimeyi bilmiyorum" dürüstlüğü teknik olarak kırılgan. Yeni hâlde sızıntı, sadece seçim yapan kişiye ve sadece tek kelimeye olur.
- **Maliyet:** 0,1 sa · **Güven:** yüksek · **Öncelik:** şart

**2. DEFUSE = mayın kaldırılır, sahibine yeniden ekme hakkı.**
- **Ne:** `defused` olan mayın `armed`'a dönmesin; kaldırılsın ve sahibi yeniden ekebilsin. Overlay'de "FALSE ALARM — @owner gets a free re-plant" yazsın.
- **Neden:** Kelime afişte zaten açıklandı; aynı mayının tekrar `armed` olması anlamsız. Ayrıca yayıncının kendi patlamasını dock'tan iptal etmesi oyunda hile gibi görünür. DEFUSE'u açıkça "yanlış alarm" düğmesi olarak çerçevele; videoda da öyle göster.
- **Maliyet:** 0,1 sa · **Güven:** yüksek · **Öncelik:** şart

**3. "Canlı" mayını tanımla.**
- **Ne:** SPEC §3'e tek satır: canlı = `arming | armed | sparking`, artı DEFUSE penceresindeki `exploded`.
- **Neden:** `MAX_MINES` ve "kişi başına 1 canlı mayın" kuralları buna bağlı. Patlayan mayının sahibinin yeniden ekip ekleyemeyeceği tanımsız. Codex bunu WP1'de kendi tahminiyle doldurur.
- **Maliyet:** 0,05 sa · **Güven:** yüksek · **Öncelik:** şart

**4. Harness'i hipotez kaydı + tekrar oynatma ile kur; etiket yardımcısı ekle.**
- **Ne:**
  - (a) Motor, her WAV için hipotez akışını bir kez JSONL'e yazsın. Eşik ayarı (`AGREE_TOL_S`, `FINAL_SOLO_MIN_PROB`, deste) saniyeler içinde bu kayıttan tekrar oynatılsın.
  - (b) `harness label-assist`: dosyanın tamamını offline yazıya döker (beam 5, kelime zaman damgalı), deste kelimelerini aday etiket olarak çıkarır; sen 10 dakikada düzeltirsin.
  - (c) Kayıt (c) için 20 satırlık bir "prompter": cümleleri sırayla gösterir, her birinin zamanını yazar. Ya da (c)'yi de (b) ile etiketle.
  - (d) Rapor yanlış alarmı iki biçimde versin: "300 kelime kurulu" ve "4 canlı mayına normalize". 300 kelimeyle ölçülen yanlış alarm, gerçek oyundakinin ~75 katı. T1'deki "≤1/10 dk" hedefi 4 mayına göre tanımlanmalı, yoksa haksız yere başarısız görünür.
- **Neden:** Planda etiketleme işi yok. Her ayar denemesi için gerçek zamanlı yeniden yazıya dökme saatler yer.
- **Maliyet:** +0,5 sa Codex, −1 sa senin zamanın · **Güven:** yüksek · **Öncelik:** şart

**5. "İki ardışık tahmin" eşleştiricisini zaman damgası toleransına bağlama.**
- **Ne:** Onayı "aynı kelime, aynı utterance'ta, aynı sıradaki geçiş (n'inci geçiş)" ile yap. `start` farkı sadece ikincil kontrol olsun; `AGREE_TOL_S` 1,0 sn olsun.
- **Neden:** Tamponun sonundaki kelimenin zaman damgası (DTW hizalaması), tampon büyüdükçe 0,3–0,8 sn oynayabilir. Bu yüzden gerçek söylemler "fıss" olur; kaçırmaların en olası nedeni bu. Bu kayma belgelenmiş bir değer değil, benim tahminim; T1'de fizzle oranını kelime bazında gör.
- **Ek:** Hipotez filtrelenip atılırsa "k+1" bir sonraki **gelen** hipotez sayılmalı. Bunu kural 4'e yaz.
- **Maliyet:** 0,1 sa · **Güven:** orta · **Öncelik:** iyi olur

**6. Gecikmeyi tek bir saat alanında ölç.**
- **Ne:** Motor `utt_start_wall`'u relay'in `start_wall`'undan değil, kendi saatinden hesaplasın: hello'nun geldiği an + örnek sayısı / 16000. Relay saati sadece log için kalsın.
- **Neden:** Relay Windows saatini, sunucu WSL saatini kullanıyor. WSL2 saati, uyku ya da hibernate sonrasında saniyelerce kayabiliyor; o zaman gecikme raporu ve videodaki rakam yanlış çıkar.
- **Maliyet:** 0 sa (spec cümlesi) · **Güven:** orta · **Öncelik:** şart

**7. Simülatöre `plant` eylemi ekle.**
- **Ne:** WP12'nin YAML'ı sadece `(t, account, message)` destekliyor. Ama `!mine KOD` için kod önceden bilinemez. `plant` adımı ekle: simülatör `/api/hand` → `/api/pick` çağırır, sonra `!mine KOD` gönderir.
- **Neden:** Bu adım olmadan simülatör ekme akışını hiç sınayamaz. WP13'ün kabulü ("3 tur kesintisiz simülatörle") de karşılanamaz.
- **Maliyet:** 0,1 sa · **Güven:** yüksek · **Öncelik:** şart

**8. Relay ayrıntıları.**
- **Ne:**
  - Mikrofonu cihazın yerel hızında (genelde 48 kHz) aç ve 16 kHz'e indir. Ya da WASAPI'de `auto_convert=True` kullan.
  - Relay, motor yeniden başlayınca otomatik yeniden bağlansın.
  - `numpy` bağımlılığına izin ver.
- **Neden:** WASAPI paylaşımlı modda 16 kHz ile açmak "Invalid sample rate" hatası verebilir. Demo sırasında motoru yeniden başlatınca relay'i de yeniden başlatmak gerekmesin.
- **Maliyet:** 0,1 sa · **Güven:** orta · **Öncelik:** iyi olur

**9. Bütçeyi 24 saate indir.** Kesme ve küçültme sırası:
- "Zaman kalırsa" listesinin üçünü de baştan sil (Türkçe, mayın tarama, `!dud`): −0 sa ama dikkat dağıtmaz.
- WP12'yi 0,5 saate indir: sadece `plant` + `say` adımları, YAML yerine Python listesi.
- WP3'te DEFUSE'u geri sarma efekti yerine statik "FALSE ALARM" damgası yap: −0,5 sa.
- 1 Kasım öğlen provasını 3 turdan 2 tura indir.
- Tamponu 3,5'tan 2,5'a indir, ama görünmeyen işleri açıkça yaz (öneri 4, 15, 16). Etiket ~0,5, Twitch hesap/2FA ~0,5, OBS ses ~0,5, README/jüri kurulumu ~0,5 sa.
- **Maliyet:** −1,5…2 sa · **Güven:** orta · **Öncelik:** şart

**10. Takvimde Twitch'i öne al.**
- **Ne:** 30 Ekim sabahı: WP1, WP2, WP4 (M1) + WP8 (auth). Öğleden sonra: WP5 + T1 için WP6. 31 Ekim: WP9–WP11.
- **Neden:** Senin için en bilinmeyen kısım STT değil, Twitch: hesap doğrulama, sadece canlıda çalışan API'ler, token'lar. WP8'i T5'te zaten elle deniyorsun; kodunu erkene almak 31 Ekim'deki riski azaltır.
- **Ek:** T5'i Twitch CLI ile yapacaksan `twitch token -u --dcf -s "clips:edit channel:manage:broadcast"` kullan. Bayrak var; Public client uygulamada secret olmadan ilerler (bölüm 5'e bak).
- **Maliyet:** 0 · **Güven:** orta · **Öncelik:** iyi olur

**11. Codex stratejisi: bir ana thread + paralel yan thread'ler (worktree).**
- **Ne:**
  - Ana thread'de çekirdek, sunucu, STT, eşleştirici, harness ve Twitch yapılsın; yani "most of the build". Kurallar bunu istiyor; SSS çoklu thread'e açıkça izin veriyor.
  - Overlay görselleri (WP3) ve ekme sayfası (WP11) ayrı thread'lerde, ayrı git worktree'lerde paralel ilerlesin; birleştirme ana thread'de olsun.
  - Ana thread'in bağlamı 4 gün sürer; WP aralarında `/compact` kullan. Kalıcı hafıza `AGENTS.md` ve `SPEC.md`'dir.
- **Neden:** Hafızandaki "paralel ajanlar" kısıtı tek thread ile çelişiyor. Paralellik insan saatini değil, takvim süresini kısaltır; bu da 1 Kasım'ın dondurma saatini korur.
- **Maliyet:** 0 · **Güven:** orta · **Öncelik:** iyi olur

**12. Video, Twitch'te geçtiğini kanıtlasın.**
- **Ne:**
  - Kayıt gecesi OBS yerel kaydına ek olarak ikinci bir cihazdan ya da ikinci bir tarayıcı penceresinden **twitch.tv/kanalın + chat**'i kaydet.
  - Soğuk açılışta kelime → BOOM arasını kesme; köşede `latency_ms` göster (debug rozeti).
  - Chat'teki klip linkine tıklayıp klibi oynat (2 sn).
  - Codex bölümünde `/status` ile session ID'yi göster.
  - Video 2:50'yi geçmesin.
- **Neden:** Kural: *"footage that shows the Project functioning on Twitch"*. Kesintisiz an ve görünen gecikme, Tech puanı için en güçlü kanıt.
- **Maliyet:** 0,5 sa · **Güven:** yüksek · **Öncelik:** şart

**13. Jüri kurulumu ve CPU modu.**
- **Ne:**
  - Motora `--device cpu --model small.en --compute int8` seçeneği ekle.
  - README'de "GPU'suz 2 dakikalık deneme" bölümü olsun: `MINEFIELD_DEBUG=1`, `/overlay?demo=1`, typed mod, debug plant.
  - Twitch adımları: kendi Public uygulamanı kaydet, `TWITCH_CLIENT_ID`'yi gir, DCF.
- **Neden:** Kural "successfully installed and running consistently" diyor. Potential Impact de "başka yayıncı bunu kurabilir mi" sorusuna bakar; NVIDIA + WSL şartı bu soruya kötü cevap.
- **Maliyet:** 0,5 sa · **Güven:** orta · **Öncelik:** iyi olur

**14. Klip mesajını ikiye böl.**
- **Ne:** Patlama mesajı hemen gitsin (`💥 @owner's mine WORD went off!`). Klip linki hazır olunca ikinci mesaj olarak gelsin.
- **Neden:** Patlama + 10 sn DEFUSE + 60 sn'ye kadar bekleme, chat'teki tepkiyi ~1 dakika geciktirebilir. İlk mesajı DEFUSE penceresi bitince gönder.
- **Opsiyonel:** Daha isabetli klip için yeni "Create Clip From VOD" (`vod_offset`) kullanılabilir; scope'u `editor:manage:clips` ya da `channel:manage:clips`. MVP için gerekmez.
- **Maliyet:** 0,1 sa · **Güven:** yüksek · **Öncelik:** iyi olur

**15. Demo günü kontrol listesi (WP13'e ya da plana ekle).**
- **OBS:**
  - Overlay kaynağında "Control audio via OBS" açık; ses izleme "Monitor and Output".
  - "Shutdown source when not visible" kapalı.
  - Dock: Docks → Custom Browser Docks.
  - Kayıt kodlayıcısı "Same as stream" (NVENC'i iki kez kullanmamak için).
- **Ses:**
  - Kulaklık şart. Discord'daki arkadaş sesi ve BOOM efekti mikrofona sızmamalı; yoksa arkadaşın söylediği kelime de patlatır, bu da dürüstlük sorunu.
  - Mikrofonu hiçbir uygulama "exclusive mode"da tutmasın.
- **Laptop:**
  - Prize takılı, Windows "En iyi performans" modunda.
  - Uyku kapalı (cloudflared tüneli de düşer).
  - Bildirimler kapalı, Discord overlay'i kapalı.
- **WSL:** Uykudan sonra localhost yönlendirmesi ya da saat bozulursa `wsl --shutdown` yap ve her şeyi yeniden başlat.
- **Twitch kanal ayarları:**
  - Chat'te e-posta/telefon doğrulama şartı test hesaplarını engellemesin.
  - Klipler açık; "Store past broadcasts" açık.
  - Bot moderatör (hem link engelinden hem AutoMod'dan muaf olur).
- **Tek komutla başlatma:** WSL'de sunucu + motor + cloudflared için `scripts/run_all.sh`, Windows'ta relay için bir `.bat`. Dock'taki durum ışıkları bu süreçleri göstersin.
- **Maliyet:** 0,5 sa · **Güven:** yüksek · **Öncelik:** şart

**16. 29 Ekim kurulumu için gizli adımlar.**
- **Ne:**
  - Geliştirici konsolunda uygulama kaydı için yayıncı hesabında **2FA** gerekiyor (resmî doküman değil, birden çok kılavuz böyle diyor). Bu genelde telefon ister.
  - Form, Public client için de bir OAuth Redirect URL alanı istiyor; `http://localhost:3000` gir.
  - 4–5 hesabın e-posta doğrulaması.
- 45 dk sıkı; 60–75 dk ayır.
- **Maliyet:** +0,5 sa · **Güven:** orta · **Öncelik:** şart

**17. AGENTS.md'ye Codex için çalışma ortamı kuralları.**
- **Ne:**
  - "GPU, mikrofon ya da ağ gerektiren testler `@pytest.mark.gpu` / `live` ile işaretlenir ve varsayılan `pytest`'te atlanır."
  - "Twitch'i birim testlerinde `respx`/fake ile taklit et."
  - Codex'in web araması ve ağ izni açık olsun. Aksi hâlde hem "dev.twitch.tv'den doğrula" kuralını uygulayamaz, hem `uv sync` çalışmaz.
  - Sürümleri sabitle: `faster-whisper` güncel, `ctranslate2>=4.5` (CUDA 12 + cuDNN 9).
  - VAD için faster-whisper'ın içindeki Silero ONNX'u (`faster_whisper.vad`) kullan; `silero-vad` pip paketi torch çeker.
- **Maliyet:** 0,1 sa · **Güven:** yüksek · **Öncelik:** iyi olur

**18. Plant app 127.0.0.1'e bağlansın.**
- **Ne:** cloudflared WSL'de çalışırsa 8001'in `0.0.0.0`'a açılmasına gerek yok.
- **Neden:** WSL "mirrored" moda geçilirse `0.0.0.0` portu LAN'a açar.
- **Maliyet:** 0 · **Güven:** orta · **Öncelik:** iyi olur

**19. T0 protokolünü yaz.**
- **Ne:**
  - Kodsuz oyunu kim hakemliyor? Öneri: deste v0'dan her arkadaşa 6 kelimelik bir el gönderilir; arkadaşlar seçtikleri kelimeyi bir hakeme (üçüncü arkadaş ya da arkadaşlardan biri) DM'ler; hakem "BOOM" der.
  - İzleyicilerin tuzağı **yazılı** kurması gerektiğini simüle etmek için arkadaşlar Discord'da sesli değil, yazılı chat'ten tuzak kursun. Sesle "pineapple de" demek oyunu bozar.
  - Not al: yayıncının chat'i sesli okuması en kolay tuzak; bu eğlenceli mi, yoksa ucuz mu?
- **Opsiyonel kural:** Kendi kelimesini chat'e yazan, mayınını kaybeder. Sunucu kelimeyi bildiği için 0,25 saatlik bir iş; tuzağı yaratıcı hâle getirir. T0 sonucuna göre karar ver.
- **Maliyet:** 0,1 sa (+0,25 opsiyonel) · **Güven:** orta · **Öncelik:** iyi olur

**20. Dil ve dürüstlük notu.**
- Kayıt gecesi yayıncı konuşması İngilizce olmalı. `language="en"` sabitken Türkçe konuşma "çevrilip" uydurma bir İngilizce kelime üretebilir; bu yanlış alarm riski demek.
- Arkadaşlar Türkçe konuşacaksa bu sadece Discord'da kalsın; mikrofona girmesin.
- Devpost metninde "friends picked the words; I did not know them" cümlesi ve typed fallback'in videoda kullanılmadığı açıkça yazılsın.
- **Maliyet:** 0 · **Güven:** yüksek · **Öncelik:** şart

**21. Kalan şüphecilik: 6 kartlık el.**
- 6 kart mobilde biraz kalabalık. Ama "seçme" hissi oyunun bir parçası ve maliyeti yok, o yüzden değiştirmeyi önermiyorum.
- Daha önemlisi destenin **dengesi**: "en sık 1000 kelime yasak" kuralı, sohbette kendiliğinden hiç geçmeyecek kelimeler seçtirebilir (oyun sıkıcı olur).
- T0'da patlama süresini not et. Ortalama >5 dk ise desteye biraz daha yaygın kelimeler ekle.
- **Maliyet:** 0 · **Güven:** düşük · **Öncelik:** opsiyonel

**22. Süreç bölünmesi (relay / motor / sunucu) doğru; birleştirme önermiyorum.**
- Motorun ayrı süreç olması GPU'yu sunucudan ayırıyor, harness'i aynı kodla çalıştırıyor ve motoru tek başına yeniden başlatmaya izin veriyor.
- Tek ekleme: sunucu, motor heartbeat'i 5 sn gelmezse dock'ta kırmızı ışık yaksın ve overlay'de hiçbir şey göstermesin; sessizce typed moda geçmesin.
- **Maliyet:** 0 · **Güven:** yüksek · **Öncelik:** iyi olur

---

## 4. D3 ve D4 hakkında görüşüm

### D3: STT motoru WSL'de, Windows'ta mic relay → **Kabul (şartlı)**

**Neden doğru:**
- Harness ve canlı sistem aynı kodu, aynı ortamı kullanır; iki ayrı Python ortamı ve `\\wsl$` üzerinden uv kurulumu derdi olmaz.
- WSL2'de CUDA, Windows sürücüsüyle resmî olarak destekleniyor.
- Relay 50 satır ve tek bir WebSocket; localhost üzerinden ses aktarımı gecikmeye ~1 ms ekler.
- Mikrofonun WSLg/PulseAudio üzerinden alınması güvenilmez; relay doğru çözüm.

**Şartlar:**
1. **29 Ekim CUDA kontrolüne 45 dk ayır.** Sadece `nvidia-smi` yetmez. Şu çalışmalı:
   - `pip install nvidia-cublas-cu12 nvidia-cudnn-cu12==9.*` ve `LD_LIBRARY_PATH` ayarı (faster-whisper README'si);
   - ardından 30 sn'lik bir WAV'ın turbo + float16 ile **kelime zaman damgalı** yazıya dökülmesi;
   - ve bunun OBS açık ve yayın sürerken süresinin ölçülmesi.
2. **Geri dönüş kriteri net olsun:** 45 dk içinde WSL'de GPU'da çalışmazsa motor Windows'a taşınır. Modeli daha önce nerede denediğine bak: Windows'ta çalışan bir ortamın varsa geri dönüş 15 dakikalık bir iş.
3. **Saat alanı:** öneri 6.
4. **Ağ:** Windows → WSL `localhost` yönlendirmesi NAT modunda çalışıyor (Microsoft dokümanı). Ama uyku sonrasında bozulabiliyor. OBS browser source'u `http://localhost:8000/overlay` ile ve relay'i `ws://localhost:8765` ile 29 Ekim'de dene.

### D4: Ekme sayfasında Twitch girişi yerine chat kodu → **Kabul, küçük değişikliklerle**

**Neden doğru:**
- Quick tunnel adresi her açılışta değişiyor; OAuth redirect URI'nin her seferinde konsolda güncellenmesi gerekirdi. Bu demo günü bir arıza noktası.
- Daha önemlisi: Twitch mobil uygulamasından açılan link uygulama içi tarayıcıda açılır ve oturum paylaşılmaz. İzleyici twitch.tv'ye **şifre + 2FA ile yeniden** girmek zorunda kalır. Kod akışında giriş yok.
- Kimliği chat'in kendisi (EventSub `chatter_user_id`) doğruluyor. Kod tek kullanımlık ve 120 sn'lik; 32⁴ ≈ 1 milyon olasılıkla tahmin edilemez.

**Değişiklikler:**
- Sayfada tam komut görünsün: `!mine K7QF` ve bir **Copy** düğmesi (clipboard API HTTPS ister; trycloudflare HTTPS veriyor).
- Ayrıştırıcı büyük/küçük harfe ve boşluklara toleranslı olsun. Mobil klavye otomatik büyük harf yapar: `!Mine k7qf`.
- `CODE_TTL_S`'i 300'e çıkar; telefonda uygulama değiştirmek zaman alıyor.
- Ekme linkini sadece bot cevabında değil, overlay'in köşesinde kısa bir URL + QR olarak da göster. Videoda "telefonla QR → kart → chat'e kod → çipte isim" akışı daha net görünür.

**Alternatif (D4b, düşük öncelik):**
- `!mine` sonrasında bot, kullanıcıya özel tek kullanımlık bir link verir (`…/?n=ab12`); sayfada kartı seçince iş biter, chat'e dönmek gerekmez.
- Bir adım daha kısa. Ama link chat'te herkese açık; başkası tıklayıp o kişi adına ekleyebilir. Zarar küçük (sadece desteden kelime seçilebiliyor).
- Küçük demo için daha akıcı, gerçek kanal için daha zayıf. Ben D4'te kalırdım.

---

## 5. Doğrulayamadığım ya da emin olmadığım noktalar

- **Son teslim saati:** Kurallar "2 Kasım 14:00 PT" diyor. ABD'de yaz saati 1 Kasım 2026'da bitiyor; bu durumda son saat **3 Kasım 01:00 TSİ** (22:00 UTC). Ama SSS "9:00 PM UTC" diyor, bu da 00:00 TSİ eder; SSS kendi içinde çelişiyor ("10 PM London" = 22:00 UTC). Senin 23:00 TSİ hedefin iki durumda da güvenli. Devpost sayacına bir kez bak.
- **2FA şartı:** Geliştirici konsolunda uygulama kaydı için 2FA'yı birden çok kılavuz söylüyor; resmî bir Twitch sayfası bulamadım. Bir telefon numarasına kaç hesap bağlanabileceğini ve bir e-postayla kaç hesap açılabileceğini de doğrulayamadım.
- **Clip `duration`:** Doküman varsayılan durum için "90 sn'lik pencerenin son 30 sn'si yayımlanır" diyor. `duration` verilince son *N* saniyenin alındığını varsayıyorum. T5'te klibi oynatıp kontrol et.
- **WSL localhost yönlendirmesi:** Microsoft dokümanı Windows'tan `localhost` ile WSL uygulamalarına erişilebildiğini söylüyor. 127.0.0.1'e bağlı servisler için açık bir ifade yok; pratikte çalışır diye biliyorum. 29 Ekim'de dene.
- **Twitch CLI ve Public client:** `twitch token -u --dcf` var. Ama `twitch configure` client secret isteyebilir; Public uygulamada secret alanı boş geçilebiliyor mu, denemedim. Geçilemezse T5 için curl ile DCF yap (iki istek).
- **Twitch kanal varsayılanları:** Yeni bir kanalda chat için e-posta/telefon doğrulama şartının varsayılan durumu ve trycloudflare linklerinin Twitch link filtresine takılıp takılmadığı doğrulanmadı. Bot mod olduğu için büyük ihtimalle sorun yok.
- **Kelime zaman damgası kayması:** Akan tanımada tampon sonundaki kelimenin zaman damgasının ne kadar oynadığı (öneri 5) ölçülmüş bir değer değil, deneyimime dayalı bir tahmin.
- **Codex kullanım limitleri:** SSS ücretsiz Codex'in sınırlı olduğunu söylüyor. Planın hangi Codex/ChatGPT planıyla yürüyeceği bilinmiyor; 1–2 Kasım'daki düzeltmeler için pay bırak.
- **Twitch CLI mock EventSub sunucusu:** `channel.chat.message` olayını taklit edip edemediğini doğrulamadım. Edebiliyorsa WP9 testleri için kullanılabilir.
- **Model performansı:** Turbo'nun RTX 4070 Laptop'ta, OBS açıkken adım başına süresi (~150–300 ms tahmini) ölçülmedi. Encoder her adımda 30 sn'lik dolgulu girişi işlediği için süre tampon uzunluğundan pek etkilenmez.

---

## 6. Kaynaklar

- Twitch API Reference, Create Clip / Create Clip From VOD / Create Stream Marker / Send Chat Message: https://dev.twitch.tv/docs/api/reference/
- Twitch EventSub WebSocket olayları: https://dev.twitch.tv/docs/eventsub/handling-websocket-events/
- Twitch EventSub `channel.chat.message`: https://dev.twitch.tv/docs/eventsub/eventsub-subscription-types/#channelchatmessage
- Twitch Device Code Flow: https://dev.twitch.tv/docs/authentication/getting-tokens-oauth/
- Twitch Refresh Tokens: https://dev.twitch.tv/docs/authentication/refresh-tokens/
- Twitch CLI `token` (`--dcf`): https://github.com/twitchdev/twitch-cli/blob/main/docs/token.md
- 2FA şartı (üçüncü taraf): https://github.com/alsi-lawr/BlokeBot/wiki/Twitch-Developer-Application , https://clerk.com/docs/authentication/social-connections/twitch , https://ngrok.com/docs/integrations/oauth/twitch-oauth
- faster-whisper README (CUDA 12 / cuDNN 9, `LD_LIBRARY_PATH`, VAD): https://github.com/SYSTRAN/faster-whisper
- faster-whisper kaynak: `transcribe.py`, `vad.py` (Silero v6 ONNX, 512 örnek): https://github.com/SYSTRAN/faster-whisper/tree/master/faster_whisper
- deepdml turbo modeli (`alignment_heads`): https://huggingface.co/deepdml/faster-whisper-large-v3-turbo-ct2
- WSL ağ yapısı: https://learn.microsoft.com/en-us/windows/wsl/networking
- Cloudflare Quick Tunnel sınırları: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/trycloudflare/
- Yarışma kuralları ve SSS: `docs/competition/rules.md`, `docs/competition/resources.md`
