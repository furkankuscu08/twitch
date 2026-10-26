# Sentez

## Dalga 1 (2026-10-25)

Kaynaklar: [A](wave1/A-capabilities.md), [B](wave1/B-culture-needs.md), [C](wave1/C-mechanisms.md), [D](wave1/D-landscape.md). Etiketler agent dosyalarındaki gibi: [V] doğrulanmış, [S] yalnızca snippet veya ikincil kaynak, [I] çıkarım, [U] bilinmiyor. Bu bölüm fikir önermez, sadece kısıtları ve sinyalleri özetler.

### 1. Teknik kısıtlar (kesinleşenler)

| Konu | Bulgu | Bizim için anlamı |
| --- | --- | --- |
| Chat, overlay, EventSub | Hiçbiri Affiliate şartına bağlı değil. EventSub'da 79 olay türü var, hiçbirinde Affiliate ifadesi geçmiyor [V, A] | Güvenli temel: chat komutları + OBS overlay + EventSub WebSocket |
| Affiliate olmak | Haziran 2026 şartları: 25 takipçi, 4 saat yayın, 4 farklı gün, ortalama 3 eşzamanlı izleyici [V-ish, A]. B'deki 50/500 dk rakamları eski. | 3 izleyici ortalaması gerçekçi değil. Test hesaplarıyla izleyici şişirmek kural ihlali riski taşıyor. **Affiliate'e güvenme.** |
| Hâlâ kapalı olanlar | Reklamlar, charity, abonelik sorguları, stream delay, Power-ups [V, A/C/D] | Bunlara dayalı mekanikleri baştan ele |
| Twitch CLI | Chat mesajı, follow ve channel.update olaylarını taklit edemiyor [V, A] | Chat testleri gerçek hesaplarla yapılmalı. Demo kurgusu planlanmalı. |
| Gecikme | İzleyici, yayındaki etkiyi 2–30 sn sonra görür [S, A] | Anlık geri bildirim yayıncı tarafında olmalı. Tasarım gecikmeye dayanıklı olmalı. |
| Veri saklama | Developer Agreement, Twitch içeriğini izinsiz saklamayı yasaklıyor. Sadece 24 saatlik önbelleğe izin var [V, A] | Uzun süreli chat geçmişi veya izleyici hafızası tasarımları kısıtlı. Chat'i LLM'e göndermek belirsiz [U]. |
| Kurulum | Developer console için 2FA ve doğrulanmış e-posta gerekiyor. Bot moderatör yapılırsa limiti 100 mesaj/30 sn'ye çıkar [V, A] | 1. gün yapılacak işler |

### 2. Çelişkili kaynaklar: 1. gün test edilecek

| Soru | Çelişki | Test |
| --- | --- | --- |
| Kanal puanları (Custom Reward) yeni bir kanalda açık mı? | 2026-05-13 tarihli Twitch blogu kanal puanlarını herkese açtığını söylüyor [V]. API referansında ise "not a partner or affiliate" 403 hatası hâlâ listeleniyor [V]. | Creator Dashboard'da kanal puanlarını aç, `Create Custom Reward` çağır |
| Anket ve tahmin (Polls/Predictions) | API referansında Affiliate şartı yok [V]. 2021 blogu ve 2022 tarihli bir forum yanıtı Affiliate gerekli diyor [S]. | `Create Poll` ve `Create Prediction` çağır |

**Tasarım ilkesi:** Test sonucu ne çıkarsa çıksın, ana deneyim bu API'lere bağımlı olmamalı. En fazla, çalışıyorlarsa kullanılan bir bonus olabilirler.

### 3. Kullanıcı ve kültür sinyalleri

- **Küçük kanal gerçeği.** Kanalların büyük çoğunluğu çok küçük [S/I, B]. Bizim demo kanalı (1 yayıncı + birkaç hesap) tipik bir kanala benziyor. Bu ölçekte sorun "chat'in çok kalabalık olması" değil, "katılımın az olması". Kalabalık chat varsayan araçlar videoda inandırıcı görünmez. [B]
- **En güçlü kanıtlı ihtiyaç moderasyon** (hakemli çalışmalar). Ama Twitch'in burada güçlü yerleşik araçları var ve gerçek saldırgan olmadan demosu zor. [B]
- **Orta düzey kanıtlı ihtiyaçlar:**
  - sessiz chat'in yayıncıyı yıldırması (tek ama bilinen bir yayıncı, Eylül 2026)
  - oyun/performans sırasında yayıncının chat'i okuyamaması
  - yeni izleyicinin kanalın iç şakalarına ve bağlamına yabancı kalması
  - yazmak veya ödeme yapmak istemeyen izleyicilerin (lurker) katılımı [B]
- **Twitch'in değiştirmesi gereken, bizim çözemeyeceğimiz şeyler:** keşfedilme, sahte izleyici, müzik telifi. [B]
- **Kanıt boşluğu.** Reddit ve UserVoice agent'lara kapalıydı. İhtiyaç kanıtı bu yüzden zayıf. Senin saha gözlemin ve Reddit'e elle göz atman burada değer katar.

### 4. Diğer platformlardaki mekanizmalar

- **Kalabalık ve paralı hediye gerektirenler:** TikTok Match tarzı düellolar, danmaku grup savaşları. Bize uymuyorlar. Kaynaklar ayrıca hızlı yükselip düşme ve doygunluk örüntüsü bildiriyor (HQ Trivia, Fan Controlled Football, Çin danmaku oyunları). [C]
- **Hediye/eylemle oyun etkisi tetikleme** Twitch'te zaten var (Crowd Control, TikFinity). Yenilik düşük. [C]
- **Kalabalık veya para gerektirmeyenler** (hepsinde başarı kanıtı zayıf veya eski):
  - izleyicinin kontrol kurallarına oy vermesi
  - kilitlenmiş tahminler ve "diğerleri ne seçti" karşılaştırması
  - chat'in video üstünde akması (danmaku). Twitch'te izleyici tarafında eklentiler zaten var, yenilik zayıf. [C]
- **Yön sinyali.** YouTube, 2027 için canlı düello ve yayıncı eşleştirme kuyruğu duyurdu. Başarı verisi yok. [C]
- **Boşluklar:** canlı satış (live commerce), Kick, Discord ve Instagram için mekanizma düzeyinde kanıt bulunamadı. [C]

### 5. Rekabet ve mevcut araçlar

- **Yaygın işlerin hepsinin ücretsiz bir sahibi var:** alert/overlay, izleyicinin para verip tetiklediği etkiler, otomasyon, chat botu. [D]
- **AI co-host alanı aktif ve ticari rakipli:** ai_licia, Streamlabs Intelligent Streaming Agent, Neuro-sama. "AI chatbot/co-host" fikirleri için farklılaşma yükü yüksek. [D]
- **Geçmiş Twitch hackathon kazananları** (2018–2024):
  - Niş ve küçük projelerdi. Solo geliştiriciler de kazanmış.
  - Birkaçı fiziksel ya da chat dışı çıktı üretiyordu (su pompası, LED, ışık kapatma oyunu).
  - Bazıları prototip seviyesindeydi.
  - Videolar çoğunlukla 2–3 dakikaydı.
  - Bu bir tasvir. Neden kazandıklarını göstermez. [D]
- **Katılım tahmini:** Bugün 549 katılımcı var. Geçmiş oranlarla (%6–12) 30–70 civarı proje bekleniyor, ilk 5 de bunların ~%7–15'i [I, düşük güven]. Tahmin doğruysa, rekabet katılımcı sayısının düşündürdüğünden küçük.
- **"Katılımcılar örneklerin etrafında toplanacak" varsayımı:** Bu yarışma için bilinmiyor (galeri kapalı). 2024 galerisinde zar, anket, bingo, trivia ve AI chat projeleri çoktu, kazananlar ise nişti. Kısmi destek. [D]

### 5b. Reddit ve GitHub eki ([B2](wave1/B2-reddit-github-needs.md))

Kaynak: 583 Reddit postu (Arctic Shift, son 12 ay) ve 4 aracın GitHub issue'ları. Yorum araması büyük ölçüde zaman aşımına uğradı. r/streaming ve r/obs çok az örneklendi.

- **"Sessiz chat" tezi zayıfladı.** Yayıncılar gerçekten yalnızlık hissediyor (~8 gerçek soru) [V]. Ama izleyicilere doğrudan soran tek başlıkta en çok oy alan cevaplar ilgisizlik ("chat için izlemiyorum"). Asıl şikâyet, yeni geleni dışlayan "klik" chat'ler (169 puan) [V]. Bazı izleyiciler küçük yayınların samimiyetini özellikle seviyor [V].
- **"Chat'i uyandıran" overlay'lere şüpheyle bakılıyor.** Örnek: "Kimse oynamıyor, 30–40 izleyicili chat'lerde bile." Tek başlık, ama güçlü bir sinyal [V]. Ayrıca postların ~%14'ü (82/583) kendi aracını tanıtan geliştiricilerden. Aynı fikirler tekrar tekrar geliyor, arz kalabalık [V/I].
- **En iyi kanıtlı, dışarıdan çözülebilir ihtiyaçlar dar ve somut:**
  - N2: Oyuna odaklanmış yayıncının chat'in uyandığını fark etmesi. Yayıncılar bunu Streamer.bot veya Mix It Up ile kendileri kuruyor, ama ilkel.
  - N3: Moderatörler yayının yönetimine yalnızca herkese açık `!komut` ile katılabiliyor.
  - N4: Yeni izleyicinin iç şakalardan dışlanması.
  - N5: Otomatik bot mesajlarının yeni izleyiciyi rahatsız etmesi.
  - N7: Yayıncının kendi chat görünümünü filtreleyememesi.
  - N8: Çoklu platform chat'i (kalabalık alan) [V].
- **Prodüksiyon kalitesi.** En çok oy alan "küçük yayıncı" postu (3.552 puan) sorunu chat'te değil, kötü ses, uzun başlangıç ekranı ve ekranın %40'ını kaplayan overlay'de buluyor [V]. Tasarım için ders: overlay ekranı kaplamamalı.
- **Kanal puanları.** Twitch Support'un 2026-05 tarihli ifadesine göre herkese açık, sadece para çekmek Affiliate istiyor [V, Reddit]. API dokümanı ise hâlâ 403 diyor. 1. gün testi geçerliliğini koruyor.
- **GitHub sinyali zayıf.** Çok tepki alan konular, Twitch veya tarayıcı değişikliklerinden sonra bozulan şeyler. Gerçek özellik isteklerinin tepkisi 1–2. [V]

### 5c. X (Grok) eki ([E](wave1/E-x-grok.md))

**Kaynak ve doğrulama.** Grok ~190 post taradı, ~40'ı konuyla ilgiliydi. 7 linki X'in herkese açık syndication uç noktasından kontrol ettim. **7/7 post gerçek; tarih, hesap adı ve alıntı doğru.** Tek nüans: @JCbackfire'ın postu "birleşik chat"ten çok "Twitch ve YT için animasyonlu, büyük emote'lu chat overlay'i" istiyor. Bulgular [V-örneklem] kabul edildi.

**Kaynaklar arası üçgenleme:**

| İhtiyaç | B | B2 (Reddit) | E (X) | Sonuç |
| --- | --- | --- | --- | --- |
| Oyun ekranı doluyken chat'i görememek/yanıtlayamamak (tek monitör, overlay kabul etmeyen oyunlar, VR) | B5 | N2 (~17 post) | ~8 post | **En tutarlı, üç kaynakta da var.** Mevcut çözümler: ikinci ekran, arkadaşın chat'i sesli okuması, DIY alarm. |
| Sessiz chat'in yayıncıyı yıldırması | B1 | N1 + güçlü karşı kanıt | En büyük küme (~25), ama karşı norm da güçlü ("lurker'ları utandırma") | Duygu gerçek. Ama "izleyiciyi konuşturmaya" yönelik çözümler topluluk normlarıyla çatışıyor. |
| Çoklu platform chat'i (birleşik, stillendirilebilir, yanıtlanabilir) | — | N8 | ~8 post | Talep gerçek, ama araç arzı da kalabalık. Bulunamayan şey kalite: animasyon, emote, yanıtlama. |
| Klip iş akışı (marker'dan klip, TTS boşlukları) | B12 | — | ~4 post | Zayıf–orta |
| Yeni izleyicinin dışlanması | B7 | N4 | — | İki kaynak |

**X'e özgü sinyaller:**
- **Kick'in "Level Up" rozetleri:** tüm kanallardaki izleme süresiyle artan bir seviye. Mixer'da da vardı, Twitch kullanıcıları istiyor [V]. Platform genelinde olanını sadece Twitch yapabilir.
- **Shared Chat'te mesajın hangi kanaldan geldiği görünmüyor** (tek post) [V].
- **Overlay yapmak bazı yayıncılar için başlı başına keyif.** Örnek: "Kimse konuşmuyor ama chat overlay'i yapmaya 5 saat harcadım, çok eğlenceli" [V]. Yani özelleştirilebilirlik bir değer.
- **TikTok kıskançlığı neredeyse yok.** Tersine, YouTube kullanıcıları Twitch'in kanal puanlarını kıskanıyor [V].

### 5d. Asya ve Kick eki ([C2](wave1/C2-asia-mechanisms.md))

- **Kanala özel sadakat seviyesi** (izleyicinin adının yanında görünür):
  - Bilibili fan medal: doğrulandı [V]. Ama ücretsiz kazanım 2025'te sert kısıldı (günlük ~30 sınırı). Eleştirmenler bunun kullanıcıları ödemeye ittiğini söylüyor.
  - TikTok Fan Club: seviyeler ve görevler var [V]. Katılmak için hediye gerekiyor.
  - Twitch'te ücretsiz ve birikimli bir seviye yok. Watch Streaks (seri katılım) [S] ve ücretli abonelik rozetleri var [V].
- **Soru-cevap modu:** YouTube Live'da doğrulandı [V]. TikTok'ta kısmen. Twitch'te yerleşik bir karşılığı yok.
- **Anketler:** YouTube'da Temmuz 2021'den beri herkese açık [V]. Kick'te de Affiliate şartı yok [V]. Twitch anket API sayfası hâlâ "partners and affiliates only" diyor [V]. 1. gün testi geçerli.
- **CHZZK (Kore):**
  - İzleme süresiyle ücretsiz puan kazanılıyor (통나무 파워), bu puanlar tahminlerde kullanılıyor. Puanları otomatik toplayan resmi olmayan bir eklentinin ~10 bin kullanıcısı var. Bu hem ilgi göstergesi, hem de insanların "boşta izlemeyi" otomatikleştirdiğini gösteriyor [V].
  - Her kanalda izleme süresinde ilk 5'e giren izleyicilere rozet veriliyor [V, wiki, başarısı doğrulanmadı].
- **Kick:**
  - Level Up: tüm kanallarda geçerli izleme süresi rozeti, varsayılan olarak kapalı [V].
  - Daily Rewards: günde 1 saat izleyene emote ve rozet açılıyor [V].
  - Bunlara kullanıcı tepkisi verisi yok.
- **Monetization for All** (Twitch, 2026-05-13): Kanal puanları, Bits ve rozetler herkese açık, sadece para çekmek Affiliate istiyor [V]. Custom Reward API'sinin buna uyup uymadığı hâlâ 1. gün testinde.
- **Genel tablo:** Ücretsiz mekanizmaların neredeyse hiçbirinde güçlü "seviliyor" kanıtı yok. Tekrarlanan örüntü şu: izleme süresi veya katılımla biriken, kanala özel kimlik ve statü (Kick, Bilibili, CHZZK, TikTok). Twitch'te ise bu sadece ücretli abonelikle var.

### 5e. Sponsorların bakış açısı ([F](wave1/F-sponsor-lens.md))

**Codex:**
- **Yüzeyler:** CLI, IDE eklentisi, masaüstü uygulaması, cloud, SDK, App Server, GitHub, MCP, AGENTS.md, skills, subagent'lar (Mart 2026'da genel kullanıma açıldı), `/review` [V].
- **OpenAI'ın iyi kullanım tavsiyeleri** [V]:
  - hedef, bağlam ve "bitti" tanımı vermek
  - Plan modu
  - kısa bir AGENTS.md
  - testler ve kendi diff'ini `/review` ile incelemek
  - skills
  - "her tutarlı iş birimi için ayrı chat"
  
  Son madde, hackathon'un "ana thread" session ID şartıyla hafifçe çelişiyor.
- **Session ID:** Kurallar `/status` komutunu gösteriyor, ama CLI dokümanında `/status`'ta session ID listelenmiyor. **Şimdi kendi kurulumumuzda test etmeliyiz.** Ana thread fork'lanmamalı.
- **Ücretsiz plan:** Görünüşe göre sadece masaüstü uygulamasında ve kullanım hakkı belirsiz. Plus aylık $20.
- **Çalışma zamanında Codex:**
  - SDK ve `codex exec` ile mümkün.
  - App Server'ın auth'u barındırılan servislerde kullanılamaz.
  - API anahtarıyla kullanımda API fiyatı ödenir. [V]
- **OpenAI Build Week 2026 (en yakın emsal):** OpenAI'ın kendi yazısı, 8 kazananın sadece 2'sinde Codex kullanımını ayrıntılı anlatıyor:
  - uzmanlık alanı dışında bir şey inşa etmek
  - alan bilgisini çalışan bir iş akışına dönüştürmek
  
  Diğerlerinde model özellikleri öne çıkıyor. [S/V-kısmi]

**Twitch:**
- **2026 öncelikleri** (Rotterdam, 2026-05-30) [V]:
  - para kazanma (Power-Ups, sponsorluk)
  - dikey ve çift formatlı yayın
  - **yapay zekâ destekli klip ve özetler**
  - keşfedilme
  - moderasyon
- **API'ler:** Rotterdam'da API, bot veya Extension duyurusu yoktu. Geliştirici changelog'u ise aktif (Ekim 2026'ya kadar): **Pinned Chat API, Custom Power-Up EventSub, chat'te GIF**, app access token [V]. Yeni API'lerin az kullanılmış olması muhtemel [I].
- **Yapay zekâ tutumu:** CEO Clancy'ye göre "şimdilik" yapay zekâ beyanı kuralı yok. Ancak yayıncılar kendilerinin yerine yapay zekâ koymaya başlarsa müdahale edecekler [V, GamesBeat 2026-09-20]. Yapay zekâ chatbot veya co-host'larına özel bir kural bulunamadı.

**Bulunamayanlar:** Bu hackathon hakkında Devpost metni dışında Twitch veya OpenAI açıklaması. TwitchCon San Diego planı.

### 5f. X: Kore ve rakipler ([E2](wave1/E2-x-grok-kore.md), [E3](wave1/E3-x-competitors.md))

**Doğrulama.** 5 linki syndication uç noktasından kontrol ettim (3 Kore postu, @devpost duyurusu, @Xemdo yanıtı). **5/5 gerçek; tarih, hesap adı ve metin doğru.**

**Kore (CHZZK/SOOP):**
- **Sevilen ücretsiz özelliklerin hepsi oynatıcı seviyesinde:** kameraya zoom, sadece ses (radyo) modu, hemen yayınlanan VOD, kısa klip (SOOP Catch) [V].
  - Bunları yalnızca platform yapabilir. Chat, overlay veya API ile aktarılamazlar [I].
  - Radyo modu ve geri sarma sonradan paralı hale gelince şikâyet aldı [V].
- **Göç edenlerin Twitch'te özledikleri:**
  - raid'ler ("raid gelince izlerdim, şimdi sadece izleyeceğimi izleyip çıkıyorum")
  - whisper
  - klipler
  - kanal puanları ve tahminler
  - follow teşekkürleri
  
  [V] Yani Twitch'in mevcut sosyal mekanizmaları gerçekten değer görüyor. Özellikle **raid, bir sosyal keşif ve "devir teslim" aracı** olarak.
- CHZZK'nın puan sisteminin adı ("통나무 파워", kütük gücü) bile kullanıcıları soğuttu. İsim ve sunum önemli [V, tek post].

**Rakipler:**
- **"Build in public" paylaşımı yok.** Yalnızca duyuru ve tanıtım postları var [V]. Katılımcı sayısı 565, galeri hâlâ kapalı.
- **Twitch DevRel (@Xemdo)**, "uygulama Codex'i çalışma zamanında kullanmak zorunda mı?" sorusuna doğrudan cevap vermeyip kurallara yönlendirdi [V]. Kurallar sadece "built with Codex" diyor. **Çalışma zamanında Codex kullanma şartı yok** [V, rules.md].

### 6. Dalga 2'ye etkisi

**F'den sonra güncelleme:**
- **Codex kullanımı baştan planlanmalı ve kayıt altına alınmalı.** Ana thread'de: Plan modu, AGENTS.md, testler ve `/review`, subagent'lar. Bunların hepsi videoda ve proje açıklamasında gösterilebilir. Paralel agent'lar ana thread'e bağlanmalı.
- **Twitch'in yönü:** yapay zekâ destekli klip ve özetler, moderasyon, dikey yayın. Twitch'in yeni API'leri ise az kullanılmış yüzeyler. İkisi de "teknik imkândan" merceği için girdi.
- **Twitch'in yapay zekâ kırmızı çizgisi:** yayıncının yerini alan yapay zekâ. Yayıncıyı güçlendiren yapay zekâ daha uyumlu.

**B2'den sonra güncelleme:**
- "Chat'i canlandırma" tek başına zayıf bir gerekçe. Hem kanıtı tartışmalı, hem topluluk şüpheci, hem de arz kalabalık. Bu alandaki bir fikir, lurker'ı rahatsız etmediğini ve neden gerçekten oynanacağını açıklamak zorunda.
- Dar ve somut ihtiyaçlar (N2–N5, N7) daha güvenilir başlangıç noktaları. Ama tek başlarına "izlemesi eğlenceli" olmayabilirler. Gösteri kriteri ayrıca düşünülmeli.
- Overlay tasarımı küçük ve rahatsız etmeyen bir şey olmalı.

**Güncellenmiş sert filtreler** (process.md'dekilere ek):
- Ana deneyim yalnızca chat + overlay + EventSub ile çalışıyor. Kapalı olabilecek API'ler sadece bonus.
- 2–30 sn gecikmeyle bozulmuyor.
- Twitch içeriğini 24 saatten uzun saklamayı gerektirmiyor.
- Demosu, gerçek hesaplarla yazılmış kurgu chat'le inandırıcı.

**Benzerlik kontrolü gerektiren kalabalık alanlar** (yasak değil, ama anlamlı fark şart):
- alert/overlay araçları
- izleyicinin para verip tetiklediği oyun etkileri
- AI chatbot/co-host
- zar, anket, bingo, trivia
- klasik "Twitch Plays"

**Önerilen fikir mercekleri** (kesinleşmedi):
1. **İhtiyaçtan:** küçük kanal ölçeğinde B'deki orta kanıtlı ihtiyaçlar.
2. **Deneyim ve gösteriden:** "izlemesi eğlenceli" kriteri. Chat dışı veya fiziksel çıktı gibi alışılmadık çıktılar.
3. **Teknik imkândan:** az kullanılan yüzeyler (Shared Chat, raid/shoutout, clip ve stream marker, Guest Star) ve ML becerisi. Ama başlangıç noktası LLM olmamalı.

**Açık konular:**
- İnsan girdisi: `human-notes.md` dosyasındaki gözlemler fikir agent'larına girdi olarak verilsin mi?
- Chat metnini bir LLM'e göndermenin Developer Agreement açısından durumu belirsiz. Gerekirse TwitchDev Discord'da sorulacak.

## Dalga 2 (2026-10-25)

Kaynaklar: [L1](wave2/L1-need.md), [L2](wave2/L2-spectacle.md), [L3](wave2/L3-capability.md), [G](wave2/G-gpt-open.md), [X](wave2/X-grok-open.md). Envanter ve kümeler: [inventory.md](wave2/inventory.md).

**Eleme hunisi** (2026-10-25'te kabul edildi): envanter → kümeleme → sert filtre (+ video telif kontrolü) → kalite eşiği (jüri hatırlar mı? 10 saniyelik an var mı?) → Grok X kontrolü + kullanıcının işaretlemesi → dalga 3 kör değerlendirme (Opus ×3 rol + GPT 6 Astra, normalleştirilmiş kartlar, önceden tanımlı puan ölçekleri) → kısa liste → teknik deneme → karar. Her eleme gerekçesiyle kaydedilir.

### 1–2. Envanter ve kümeleme

- 101 ham fikir, 25 tam kart → **38 küme**. Bağımsız bir Sonnet incelemesinden sonra revize edildi ([inventory-review.md](wave2/inventory-review.md)). 19 bulgunun hepsi kabul edildi.
- **Kalabalık haritaları büyük ölçüde aynı.** AI co-host, AI özetleyici, Twitch Plays, anket, trivia, zar, dikkat dağıtıcılar, otomatik klip ve collab beşinde de var. Soru kuyruğu ise sadece 2 haritada.
- **Yakınsama kısmen prompt kaynaklı.** Brief ve L1/L3 mercekleri birçok temayı (raid devri, ihtiyaç #1/#3, Soru-Cevap) zaten adıyla veriyordu. Yakınsama bu yüzden "fikrin kalitesi" değil, "brief'ten bakınca bariz olan" sinyali.
- **Yakınsayan kümeler:**
  - K14 "raid'le bir şey taşı": 5/5
  - K10 "şu an buradayız" bağlamı: 4/5
  - K28 "lurker'ı görünür kılma": 4/5, kartı yok
  - K01a "soru kuyruğu": 3/5
  - K09 "iç şaka dipnotları": 3/5, 3 kart
- **Karşı sinyal:** X'te, yeni gelenin iç şakalarda kaybolduğuna dair post bulunamadı.
- **Video telif kuralı** (rules.md §4): ticari oyun görüntüsü izinsiz kullanılamaz. Bu yüzden oyun odaklı fikirlerin demosu masa başı ya da IRL içerikle planlanmalı.

### 3. Sert filtre ([filter.md](wave2/filter.md))

- 8 kriter: F1–F7 brief'ten ve kurallardan geliyor, F8 ise ~10 saatte yapılabilirlik. Bağımsız bir incelemeden sonra revize edildi ([filter-review.md](wave2/filter-review.md)). 12 bulgunun hepsi kabul edildi.
- **Sonuç: 22 geçti, 5 düşük riskli test, 10 yüksek riskli test, 1 kaldı (K27 kazanılmış statü, 24 saat kuralı).** 4. adıma 37 küme geçiyor.
- **Ortak kural:** Kontrolümüzdeki ikinci bir canlı kanal "?" sayılır. Sağlayamayacağımız gerçek üçüncü taraflar ise ✗.
- **25 tam kart:** 15 geçti, 4 düşük riskli test, 5 yüksek riskli test, 1 kaldı (Lit Medals).
- **1. gün test listesi** aynı dosyada: 9 düşük riskli, 10 yüksek riskli madde. En kritik üçü:
  - yeni kanalda Pin Chat Message (Floor, Story So Far)
  - yerel konuşma tanıma (Minefield)
  - ikinci canlı kanal ve gerçek raid

### 4. Kalite eşiği ([aggregate.md](wave2/step4/aggregate.md))

- Üç kör değerlendirici (Opus 5.5, GPT 6 Astra, Grok), 37 aday, dört soru (Q1 yenilik, Q2 tasarım, Q3 etki, Q4 teknik).
- **Kural (kullanıcı, 2026-10-26):** en az 2 değerlendirici en az bir FATAL verdiyse aday elenir. Önceden yazılan kural ("2 değerlendirici Eliminate derse") yalnızca 4 aday elerdi. Bu yüzden değiştirildi; değişiklik key.md'de kayıtlı.
- **Sonuç:** 17 aday elendi, 20 aday kaldı. Elenen her adayda en az iki değerlendirici aynı soruda FATAL vermişti: 15'inde Q1 (yenilik), 2'sinde Q4 (çok ince).
- **Kalanlar:**
  - 0 FATAL alan 10 aday: K24 VAR, K20, K19 Minefield, K09 Footnotes, K18b, K06 Tap, K30, K11, K17 Hint Jar, K23.
  - 1 değerlendiricinin işaretlediği 10 aday: K28, K15, K02, K03, K21, K01b, K26, K14, K10, K29.
- **Sınırda elenenler:** K04 One Line ve K22b. İkisi de 2/3 FATAL aldı. Kullanıcı isterse geri alınabilir.
- **İlk 5 listeleri:** VAR (K24) ve Minefield (K19) üç listede de var.
- **Taşınan tasarım notu:** mesajı silerek mühürlemek gizli değil. Gizli girdi whisper veya web formu ile alınmalı.

### 5a. Puanlama ile 20 → 10 ([step5/aggregate.md](wave2/step5/aggregate.md), [shortlist-10.md](wave2/shortlist-10.md))

- Üç kör değerlendirici (Opus, Astra, Grok) her adaya dört jüri kriterinde 0–5 puan verdi. Toplam puan 0–60. Kural puanlar gelmeden yazıldı: ilk 10 aday geçer; 11–14. sıradakiler bir modelin ilk 5'indeyse kurtulur.
- **Kalan 10:** Minefield (54), Prodüksiyon sorunları (49), VAR (49), Raid Torch (46), Previously On (45), Studio Audience (45), Foley Pit (44), Hint Jar (43), Photo Booth (40), Checkpoint (39).
- Modeller benzer ölçekte puanladı (ortalamalar 12,4–12,6). Hiçbir kriterde 3 puanlık ayrışma yok. İlk üç aday (Minefield, Prodüksiyon sorunları, VAR) üç modelin de ilk 5'inde. Kesim noktası (39 / 39 / 38) gürültü bandında.
- **Elenenlerden kalan adaylara taşınan özellikler:**
  - Desk Buddy → Prodüksiyon sorunları
  - Lore dipnotları ve Yeni gelene karşılama → Previously On
  - Mühürlü tahminler → Minefield
  - Lurker → Studio Audience
- **Yeni risk:** gizli giriş (whisper için telefon doğrulaması ve günlük 40 alıcı sınırı). Bu risk Minefield ve Hint Jar'ı etkiliyor. 1. gün test listesine eklendi.
