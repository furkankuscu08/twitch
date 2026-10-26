# Kalan 20 aday (adım 4 sonrası)

> **Güncel değil (2026-10-26):** adım 5a sonrası 10 aday kaldı, bkz. [shortlist-10.md](shortlist-10.md). Bu dosya kayıt için duruyor.

Kaynaklar: [step4/aggregate.md](step4/aggregate.md) (oylar), [step4/candidates.md](step4/candidates.md) (sade açıklamalar), [filter.md](filter.md) (sert filtre), [inventory.md](inventory.md) (kümeler). Tam kartlar fikir dosyalarında: [L1-need.md](L1-need.md), [L2-spectacle.md](L2-spectacle.md), [L3-capability.md](L3-capability.md), [G-gpt-open.md](G-gpt-open.md), [X-grok-open.md](X-grok-open.md). ★ = tam kart var.

Okuma rehberi:
- **FATAL:** adım 4'te O (Opus), A (Astra) veya G (Grok) hangi soruda FATAL dedi. Q1 yenilik, Q2 tasarım, Q3 etki, Q4 teknik.
- **İlk 5:** kaç değerlendiricinin ilk 5 listesinde.
- **Filtre:** adım 3 sonucu. Test (high) = 1. gün testine bağlı.

## Özet tablo

Adım 5'te "Senin işaretin" sütununa ★ (favori, 3–5 tane) veya ✗ (veto) koyabilirsin.

| # | K | Ad | FATAL | İlk 5 | Filtre | Senin işaretin |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | K24 | VAR: chat'in çağırdığı tekrar inceleme | — | 3 | Pass (büyük iş) | |
| 2 | K19 | Minefield: gizli kelime mayınları | — | 3 | Test (high): STT | |
| 3 | K17 | Hint Jar: kademeli ipuçları | — | 2 | Pass | |
| 4 | K09 | Lore dipnotları | — | 1 | Pass | |
| 5 | K06 | Prodüksiyon sorunu yayıncıya ulaşır | — | 1 | Pass (orta iş) | |
| 6 | K20 | Chat tepkileri büyütülür (Studio Audience) | — | 1 | Pass | |
| 7 | K18b | Spoiler bekletme çekmecesi | — | 0 | Pass | |
| 8 | K30 | Sesli mesaj hattı | — | 0 | Pass (orta iş) | |
| 9 | K11 | Yeni gelene karşılama | — | 0 | Pass | |
| 10 | K23 | Hatıra Polaroid'i (Photo Booth) | — | 0 | Pass (orta iş) | |
| 11 | K14 | Raid'le taşınan şey (Raid Torch / not) | O: Q3 | 2 | Test (high): 2. kanal | |
| 12 | K21 | İzleyici senaryo yazar, yayıncı canlandırır (Foley Pit) | O: Q3 | 1 | Pass | |
| 13 | K10 | "Previously On": raid'e özet kartı | A: Q1 | 1 | Pass (raid için 2. kanal) | |
| 14 | K01b | Odak modu, molada çağrı kartları (Checkpoint) | A: Q1 | 0 | Pass | |
| 15 | K26 | Mühürlü tahminler | O: Q1 | 0 | Test (low) | |
| 16 | K03 | Masadaki chat yüzü (Desk Buddy) | G: Q1 | 0 | Pass | |
| 17 | K28 | Lurker fenerleri | A: Q1 | 0 | Pass | |
| 18 | K02 | Yer imi / encore listesi | O: Q2, Q4 | 0 | Pass | |
| 19 | K29 | Maker süreklilik kontrolü | O: Q2, Q3 | 0 | Pass | |
| 20 | K15 | Kötü anda gelen raid | O: Q1, Q3, Q4 | 0 | Test (high): 2. kanal | |

## Adaylar

### 1. K24 VAR: chat'in çağırdığı tekrar inceleme

- **Ne:** İzleyiciler bir anı tartışınca ikisi `!var` yazar. "VAR CHECK" geçişi, yerel replay buffer'dan son ~20 sn, sonu ağır çekim. Chat 20 sn evet/hayır oylar, isimler jüri sırasında. Karar damgası iner, başlıklı klip oluşur.
- **İlk 10 sn:** Yayıncı kâğıt topu atar, "GİRDİ!" der. İki izleyici VAR çağırır. Ağır çekimde top çemberden seker. Jüri oylar: "SAYI YOK".
- **En yakın mevcut:** Chat tetiklemeli OBS instant-replay scripti, native anketler.
- **FATAL:** yok. **İlk 5:** Opus #2, Astra #1, Grok #4.
- **Filtre / risk:** Pass, ama iş büyük (replay buffer yakalama, ağır çekim, gecikme ofseti, jüri, damga). Spike gerekli.
- **Kart:** L2-11 VAR!★ ([L2-spectacle.md](L2-spectacle.md))

### 2. K19 Minefield: izleyici gömer, yayıncı patlatır

- **Ne:** İzleyiciler gizlice kelime mayını gömer (`!mine ananas`). Overlay mayınları sahibinin adıyla gösterir, kelimeyi asla. İzleyiciler sohbeti kendi kelimelerine yönlendirir. Yayıncı kelimeyi söyleyince yerel STT yakalar: patlama, gömenin adı, otomatik klip. Varyantlar: yayıncının klişe lafına ses efekti bağlama; "gülme" turu (webcam).
- **İlk 10 sn:** Üç mayın aktif. Yayıncı "dürüst olmak gerekirse pizzada ananas—" der, BUM. Gömenin adı çıkar, dakikalar önceki tuzak sorusuna kesilir.
- **En yakın mevcut:** STT'li küfür kavanozları, Taboo oyunu.
- **FATAL:** yok. **İlk 5:** Opus #1, Astra #2, Grok #2.
- **Filtre / risk:** Test (high). Gündelik konuşmada STT doğruluğu, 1 saatlik spike.
- **Not:** Mesajı silerek mühürlemek gizli değil (kısa süre görünür, mod loglarında kalır). Kelime whisper veya web formu ile alınmalı.
- **Kart:** L2-1 Minefield★ ([L2-spectacle.md](L2-spectacle.md)); varyantlar L2-2, L2-3, L2-18.

### 3. K17 Hint Jar: kademeli ipuçları

- **Ne:** Kör oynanışta cevabı bilen izleyiciler backseat yapmak yerine bir güçte ipucu bırakır (dürtme / yöntem / cevap). İpuçları mühürlüdür: chat'ten silinir ya da mod onaylı özel kuyruğa gider. Overlay'de kavanoz zarflarla dolar. Yayıncı takılınca yalnızca istediği seviyeyi açar, ipucu sahibi kredi alır.
- **İlk 10 sn:** Yayıncı bir bulmacada takılmış. Zarflar kavanoza düşer. Yayıncı iç çeker, tuşa basar, dürtme açılır; cevap mühürlü kalır.
- **En yakın mevcut:** "Backseat yok" kuralları, backseat kuyrukları (LeagueBackseat).
- **FATAL:** yok. **İlk 5:** Opus #5, Astra #3.
- **Filtre / risk:** Pass (Hint Airlock: silme yok). Demo kendi bulmacamızla (kâğıt bilmece, kutu).
- **Not:** Silerek mühürleme yerine özel kuyruk (G-1) daha güvenli.
- **Kart:** L1-5 Hint Jar★ ([L1-need.md](L1-need.md)), G-1 Hint Airlock★ ([G-gpt-open.md](G-gpt-open.md))

### 4. K09 Lore dipnotları

- **Ne:** Modlar kanalın iç şakalarını küçük bir sözlükte tutar. Terim chat'te geçince yayının köşesine numaralı dipnot kartı kayar, açıklama ve yazarın adı ile. Varyant: yalnızca `!why <terim>` ile, soranı göstermeden.
- **İlk 10 sn:** Bir müdavim "yine fasulye anı" yazar. Dipnot çıkar ("1 fasulye: yayında çiğ kahve çekirdeği yiyip ağladı"). Yeni hesap "ahh lol" yazar.
- **En yakın mevcut:** Bot özel komutları (`!bean`, sadece bilen sorar), kanal About panelleri.
- **FATAL:** yok. **İlk 5:** Opus #3.
- **Filtre / risk:** Pass. Sözlük kendi panelimizde yazılır (24 saat kuralı).
- **Karşı sinyal:** Grok X'te "iç şakalarda kaybolan yeni izleyici" şikâyeti bulamadı.
- **Kart:** L1-2★, L3-3★, G-3★ (üç kaynak bağımsız buldu)

### 5. K06 Prodüksiyon sorunu yayıncıya ulaşır (Tap on the Shoulder)

- **Ne:** Yayıncının fark edemeyeceği sorunlar (mikrofon kapalı, oyun çok yüksek, el kamerayı kapatıyor) özel bir kanaldan yayıncıya ulaşır: masa lambası kırmızı olur, kulaklıkta sesli uyarı, dock'ta büyük yazı. Tetik: 60 sn içinde 2+ izleyici "mic/ses" der, ya da mod hazır butona basar. Yardım edene yayında teşekkür. Varyant: "Test B" deyip izleyicilerden `!heard B good` almak.
- **İlk 10 sn:** Kapalı mikrofon yakın çekim. Chat "MİK??" ile dolar. Arkada lamba kırmızı yanar. Yayıncı yüzünü buruşturur, açar, teşekkür kartı çıkar.
- **En yakın mevcut:** Twitch olaylarına akıllı ışık (Streamer.bot), OBS mute göstergesi, chat'i aktaran arkadaş.
- **FATAL:** yok. **İlk 5:** Opus #4.
- **Filtre / risk:** Pass, orta iş (dört girdi + lamba). Lamba opsiyonel, telefon flaşı yedek.
- **Kart:** L1-4 Tap on the Shoulder★ ([L1-need.md](L1-need.md)), G-2 Soundcheck Relay★ ([G-gpt-open.md](G-gpt-open.md))

### 6. K20 Chat tepkileri büyütülür (Studio Audience)

- **Ne:** Chat emote ve kelimeleri canlı tiyatro seyircisi sesine dönüşür (kahkaha, şaşkınlık, yuhalama, alkış). Yoğunluk tepki veren farklı izleyici sayısıyla ölçeklenir; üç izleyici dolu salon gibi duyulur. Her izleyicinin tanınır bir kahkahası ve adıyla zıplayan koltuk silüeti var. Kulaklık modu: yayıncı chat'i okumadan duyar.
- **İlk 10 sn:** Yayıncı kâğıt topu kaçırır. Bir izleyici "L", ikisi "LUL" yazar. Dolu salon yuhalar, sonra güler, üç isimli silüet zıplar.
- **En yakın mevcut:** Sound Alerts (ücretli soundboard), kişisel giriş sesleri, emote duvarları.
- **FATAL:** yok. **İlk 5:** Astra #4.
- **Filtre / risk:** Pass. Yalnızca CC0 sesler. Kalabalık listesinde "ses efektleri" var, fark "ölçeklenen seyirci" olmalı.
- **Kart:** L2-4 Studio Audience★ ([L2-spectacle.md](L2-spectacle.md)); L2-5 Leitmotif, G-12 Quiet Applause

### 7. K18b Spoiler bekletme çekmecesi

- **Ne:** Hikâye bölümü açıkken spoiler veya yönlendirme gibi görünen chat satırları yayıncının görüşünden (ya da açık chat'ten) bir çekmeceye alınır. Yayıncı bölüm bitince açar.
- **İlk 10 sn:** İzleyici "anahtar tablonun arkasında" yazar, satır "bekletilen" çekmecesine kayar. Bölüm sonunda yayıncı açar.
- **En yakın mevcut:** AutoMod ve yasaklı kelimeler, spoiler yasağı kuralları.
- **FATAL:** yok. **İlk 5:** yok.
- **Filtre / risk:** Pass (yayıncı görüşünden saklama versiyonu). Açık chat'ten saklamak silme testine bağlı. "Spoiler mi?" tespiti zor olabilir.
- **Kart:** L1-14 Spoiler Airlock, X-16 Spoiler drawer (tam kart yok)

### 8. K30 Sesli mesaj hattı

- **Ne:** İzleyiciler bir web sayfasından 15 saniyelik sesli mesaj bırakır. Mod onaylar. Yayıncı molada retro telefon overlay'iyle yayına verir ve cevaplar.
- **İlk 10 sn:** Çalan telefon overlay'i. İzleyicinin kayıtlı sesi çalar, yayıncı canlı cevaplar.
- **En yakın mevcut:** Ücretli TTS mesajları, Discord üzerinden call-in.
- **FATAL:** yok. **İlk 5:** yok.
- **Filtre / risk:** Pass, orta iş. Kayıt izni, yayından önce mod onayı ve yayın sonrası silme şart.
- **Kart:** L2-14 Call-in Line (tam kart yok)

### 9. K11 Yeni gelene karşılama

- **Ne:** Biri bu yayında ilk kez yazınca kanal onu spot ışığına koymadan yönlendirir: "karşılama nöbetindeki" müdavime ping gider, ya da sadece o an küçük bir menü kartı çıkar, ya da müdavimlerin kendi yazdığı tek satırlık biyografileri ilk konuştuklarında görünür. Varyant: termal yazıcı ilk kez yazanın adını basar, yayıncı gerçek duvara asar.
- **İlk 10 sn:** Yeni hesap "selam" der. Küçük kart cevap veren müdavimi tanıtır ("@kay: mod, kötü espriler yapar"). Yeni gelen cevap yazar.
- **En yakın mevcut:** Streamlabs/Streamer.bot ilk-mesaj uyarıları, Twitch'in "ilk kez yazan" vurgusu.
- **FATAL:** yok. **İlk 5:** yok.
- **Filtre / risk:** Pass. Biyografiler bizim uygulamada yazılır; termal yazıcı donanım ister.
- **Kart:** L1-9 Welcome Mat, L1-10 Name Card, G-8, L1-18, L2-9 Wall of Firsts (tam kart yok)

### 10. K23 Hatıra Polaroid'i (Photo Booth)

- **Ne:** İzleyici `!snap <başlık>` yazar. Yayıncı bir sinyal duyup poz verir, overlay geri sayar, flaş patlar, köşede izleyicinin adı ve başlığıyla bir Polaroid belirir. İzleyici kaydetmek için 24 saatlik link alır. Yayın sonunda tüm fotoğraflar "bugün kim buradaydı" kolajı olur. Varyantlar: numaralı bilet koçanı, yayın sonu "müze".
- **İlk 10 sn:** İzleyici `!snap ilk galibiyet` yazar. Yayıncı kupayı kaldırır, flaş, Polaroid belirir.
- **En yakın mevcut:** Genel chat-overlay komutları, fiziksel abone fişi yazıcıları.
- **FATAL:** yok. **İlk 5:** yok.
- **Filtre / risk:** Pass, orta iş (obs-websocket ekran görüntüsü + herkese açık link için hosting/tünel).
- **Kart:** L2-10 Photo Booth★ ([L2-spectacle.md](L2-spectacle.md)); L2-19, G-14

### 11. K14 Raid'le taşınan şey (Raid Torch / not)

- **Ne:** Bir kanal başka bir kanala raid atınca yanında bir şey götürür ve hedef yayında görünür: giden yayıncının ya da chat'in birlikte yazdığı tek satır not ("az önce bir turta bitirdik"), ya da elinde tutan her chat'ten emote izi toplayan dijital meşale. İki kanal da aracı çalıştırır.
- **İlk 10 sn:** A kanalının meşalesi emote halkalarıyla parlar. Raid. B kanalında meşale halkalarıyla uçarak gelir, raider'lar "bunu biz getirdik!" yazar.
- **En yakın mevcut:** Raid uyarıları, raid trenleri (kanallar arası durum taşımaz).
- **FATAL:** Opus Q3: yalnızca hedef de aracı kullanıyorsa çalışır, küçük yayıncı nadiren görür. **İlk 5:** Astra #5, Grok #5.
- **Filtre / risk:** Test (high). İkinci canlı kanal gerekir. Yalnızca aynı gün (24 saat kuralı). En ağır kurulum.
- **Not:** Beş kaynağın beşi de bu temaya ulaştı, ama brief "raid = devir teslim" diye tohumlamıştı.
- **Kart:** L3-5 Raid Torch★ ([L3-capability.md](L3-capability.md)); L1-15, L2-17, G-7, X-6, L3-20

### 12. K21 İzleyici senaryo yazar, yayıncı canlandırır (Foley Pit)

- **Ne:** Yayıncı kısa bir sahne açar ("minik bir dedektif fırtınaya girer"). Üç izleyici birer rol alır (hava, ayak sesleri, sürpriz) ve bir ipucu seçer; partisyon ekranda dolar. Yayıncı sesleri masadaki eşyalarla (kâğıt, bardak, kaşık) canlı yapar, overlay ilerler. Varyantlar: üç gerçek objeye kurgusal kimlik verme; izleyicilerin önerdiği mini deneyler.
- **İlk 10 sn:** Senaryo ve üç izleyici ipucu görünür. Yayıncı yağmur için kâğıt buruşturur, bardakla saçma bir gök gürültüsü yapar.
- **En yakın mevcut:** İzleyici tetiklemeli ses efektleri (oynatma, performans değil), doğaçlama oyunları.
- **FATAL:** Opus Q3: yayıncı bir kez dener, tekrar eden bir araç değil. **İlk 5:** Grok #1.
- **Filtre / risk:** Pass. Demo için en telif-güvenli fikirlerden.
- **Kart:** G-4 Foley Pit★ ([G-gpt-open.md](G-gpt-open.md)); G-13, G-17, G-9, L2-22

### 13. K10 "Previously On": raid'e özet kartı

- **Ne:** Yayın sırasında yayıncı ya da modlar kısa olaylar veya bölüm başlıkları girer ("kurbağa kralı 9. denemede yendik"). Raid gelince ya da istek üzerine yayında 10 saniyelik TV tarzı "Önceki bölümlerde…" kartı son üç olayla çıkar. Varyant (Story So Far): her yeni bölüm Twitch chat'inin üstüne sabitlenir, stream marker oluşturur, başlığı günceller, son 90 sn'yi klipler.
- **İlk 10 sn:** Raid gelir. Ekran kararır, "PREVIOUSLY ON" kartı üç olayla süzülür. Bir raider "ahh tamam, kurbağa kral" yazar.
- **En yakın mevcut:** Raid uyarıları ve otomatik shoutout (raider'ı karşılar, bilgilendirmez), elle sabitlenmiş "bugünün planı".
- **FATAL:** Astra Q1: elle yazılsa da hâlâ "ne kaçırdım" deneyimi. **İlk 5:** Grok #3.
- **Filtre / risk:** Pass (Previously On). Gerçek raid için ikinci kanal; provada CLI mock. Pin varyantı Test (high).
- **Kart:** L1-3 Previously On★ ([L1-need.md](L1-need.md)), L3-2 Story So Far★ ([L3-capability.md](L3-capability.md)); X-12, L3-6, L3-11

### 14. K01b Odak modu, molada çağrı kartları (Checkpoint)

- **Ne:** Zor bir bölümden önce yayıncı kısayola basar. Normal chat mesajlarının hepsi bekletilir (komutlar ve bot satırları hariç), köşede renkli "kayıt kristali" yığını olarak görünür. Molada "checkpoint" basar, bekleyen mesajları yayında call-in kartları olarak tek tek açıp sesli cevaplar; ilk kez yazanlar önce. Özet yok, her mesaj sahibiyle kalır. Varyant: mod, dönüş için bir soru, bir katkı, bir duyuru toplar.
- **İlk 10 sn:** Yayıncı meşgulken kristaller birikir. "CHECKPOINT" yanıp söner, ilk izleyicinin mesajı TV tarzı kartla çıkar.
- **En yakın mevcut:** Soru kuyrukları, chat vurgulama araçları, AI "ne kaçırdım" özetleri.
- **FATAL:** Astra Q1: mesajları sonra göstermek yine bir kuyruk. **İlk 5:** yok.
- **Filtre / risk:** Pass. Demo için IRL odak görevi (çizim, yapım).
- **Kart:** L1-1 Checkpoint★ ([L1-need.md](L1-need.md)); G-18, L1-11

### 15. K26 Mühürlü tahminler

- **Ne:** Bir sonuçtan önce izleyiciler `!seal <tahmin>` yazar. Bot mesajı hemen siler, kimse kopyalayamaz. Overlay isimli mühürlü zarfları gösterir; açılışta hepsi birlikte açılır.
- **İlk 10 sn:** Ekranda üç isimli zarf. Sonuç gelir, zarflar açılır, kimin bildiği görünür.
- **En yakın mevcut:** Twitch Predictions (kanal puanı), chat tahmin oyunları.
- **FATAL:** Opus Q1: zarflar olmasa bir tahmin oyunu. **İlk 5:** yok.
- **Filtre / risk:** Test (low): silme testi.
- **Not:** Silmek gizlilik sağlamaz; whisper veya web formu gerekir.
- **Kart:** L3-9 Sealed Envelope (tam kart yok)

### 16. K03 Masadaki chat yüzü (Desk Buddy)

- **Ne:** Masaya dayalı yedek telefon chat'i temsil eden çizgi bir yüz gösterir: yeni yazanın adını büyük harfle gösterip el sallar, soru bekliyorsa sayaçla el kaldırır, emote havasına göre ifade değiştirir, chat sessizken uyuklar. Tek dokunuşla bekleyen soru açılır. Kamera kadrajında durur, izleyici mesajının odadaki bir nesneyi oynattığını görür. Varyantlar: chat rengini alan akıllı ampul; mesaj türüne göre kulaklık sesleri.
- **İlk 10 sn:** Yayıncı çizim yapıyor. Test hesabı "selam, ilk kez buradayım" yazar. Telefon el sallar, adı gösterir; yayıncı kalemi bırakmadan selamlar.
- **En yakın mevcut:** Ekran üstü chat pet'leri (Elgato Mochi), Elgato Prompter chat modu, Lumia Stream ışıkları.
- **FATAL:** Grok Q1: odadaki yüz bir chat pet'i. **İlk 5:** yok.
- **Filtre / risk:** Pass. Sadece telefon gerekir. "Müdavim" sadece bu yayın içinde.
- **Kart:** L2-7 Desk Buddy★ ([L2-spectacle.md](L2-spectacle.md)); L2-8, X-11, L1-7

### 17. K28 Lurker fenerleri

- **Ne:** Sessiz izleyiciler küçük bir şehir silüeti overlay'inde soluk fenerler ya da yıldızlar olarak görünür; chatter listesinden, isimsiz, konuşmaya davet etmeden. İlk mesajlarında ışıkları parlar. `!lurk` "buradayım, beni bekleme" der.
- **İlk 10 sn:** Silüette beş soluk ışık. Bir izleyici yazar, bir ışık parlar.
- **En yakın mevcut:** Lurk komutları, izleyici sayaçları.
- **FATAL:** Astra Q1: varlık sayacı ve ilk mesaj uyarısını manzaraya çeviriyor, etkileşim değişmiyor. **İlk 5:** yok.
- **Filtre / risk:** Pass.
- **Not:** Get Chatters yalnızca chat'e bağlı hesapları verir; giriş yapmamış izleyiciler hiç görünmez. İddia "giriş yapmış lurker'lar" diye daraltılmalı.
- **Kart:** L1-12, L2-6, L3-14, X-13 (dört kaynak buldu, hiçbiri tam kart yapmadı)

### 18. K02 Yer imi / encore listesi

- **Ne:** İzleyici tekrar dönülecek bir şeyi işaretler: "o fırçayı tekrar göster", komik anda `!rewind`, ya da yayıncının verdiği bir söz ("sonra göstereceğim"). Yayıncı molada ya da sonda kısa bir liste alır, birini seçip izleyiciye kredi vererek tekrar yapar.
- **İlk 10 sn:** Çizim sırasında izleyici `!encore fırça` yazar. Sonda yayıncı listeyi açar, darbeyi yavaşça tekrar eder, izleyicinin adı görünür.
- **En yakın mevcut:** Stream marker'ları, chat'te klip istekleri, mod notları.
- **FATAL:** Opus Q2: değer dakikalar içinde ortaya çıkıyor, 10 saniyede anlatımsız anlaşılmaz. Opus Q4: komut kaydedici + liste, ince. **İlk 5:** yok.
- **Filtre / risk:** Pass.
- **Kart:** G-5 Loose Ends, G-11 Encore Ledger, L1-16 Rewind Request (tam kart yok)

### 19. K29 Maker süreklilik kontrolü

- **Ne:** Bir maker yayıncı kontrol edilebilir bir adım ilan eder ("Aşama C: iki kanatta da iki mavi nokta"). İzleyiciler o aşamaya etiketli gözlem gönderir (`!mark C sol kanatta bir tane var`). Mod onaylar. Planlı kontrol noktasında yayıncı küçük listeyi açar, düzeltir ya da reddeder, aşamayı tamamlandı diye damgalar.
- **İlk 10 sn:** Kanatları uyumsuz kâğıt yaratık. Kontrol noktasında bir izleyici gözlemi çıkar. Yayıncı eksik noktayı ekler, "Aşama C tamam" damgası.
- **En yakın mevcut:** Kontrol listeleri, chat'te backseat, mod aktarımı.
- **FATAL:** Opus Q2: "Aşama C tamam" anlatımsız anlaşılmaz. Opus Q3: yalnızca kontrol edilebilir aşaması olan maker'lar, nadir. **İlk 5:** yok.
- **Filtre / risk:** Pass.
- **Kart:** G-6 Continuity Crew★ ([G-gpt-open.md](G-gpt-open.md))

### 20. K15 Kötü anda gelen raid

- **Ne:** Raid, yayıncı BRB ya da "birazdan başlıyoruz" ekranındayken gelirse raider'ın adı ekranda kalır ve yayıncı "teşekkürler"e basana kadar hatırlatma alır; bu tuş resmi shoutout'u da gönderir. Varyant: sahne otomatik olarak canlı karşılamaya geçer.
- **İlk 10 sn:** BRB ekranı. Raid gelir. Kalıcı "X'ten raid: teşekkür et!" kartı. Yayıncı döner, dokunur, shoutout çıkar.
- **En yakın mevcut:** Raid uyarıları, otomatik shoutout botları.
- **FATAL:** Opus Q1: yapışkan raid uyarısı + otomatik shoutout zaten yaygın. Q3: küçük yayıncı nadiren raid alır, BRB'deyken daha da nadir. Q4: tek EventSub dinleyici + tek shoutout çağrısı. **İlk 5:** yok.
- **Filtre / risk:** Test (high). İnandırıcı video için gerçek raid (ikinci kanal).
- **Kart:** X-7 BRB receipt, X-17 (tam kart yok; X-17'yi kaynağı "net bir dert değil" diye işaretlemişti)

## Elenen 17 (kayıt için)

| K | Ad | Ortak FATAL |
| --- | --- | --- |
| K04 | One Line (oyunun üstünde tek satır) | Q1 ×2, **sınırda** |
| K22b | Kolektif oyuncaklar (Ouija) | Q1 ×2, **sınırda** |
| K33 | Guest Star bekleme odası | Q1 ×3 |
| K16 | Raid halkası | Q1 ×3 |
| K25 | Chat uzlaşısıyla klip | Q1 ×3 |
| K12b | Yerel canlı altyazı | Q1 ×3 |
| K34 | Diğer platformdan kaçan selamlar | Q1 ×3 |
| K31 | Shared Chat köprüsü | Q1 ×3 |
| K22a | İzleyiciler kamerayı yönetir | Q1 ×3 |
| K32 | GIF jukebox | Q1 ×3 |
| K18a | Süreli chat modu | Q1 ×3 |
| K12a | Chat çevirisi | Q1 ×3 |
| K01a | Soru kuyruğu | Q1 ×3 |
| K05 | Özel filtreli chat görünümü | Q1 ×3 |
| K07 | Mod prodüksiyon paneli | Q1 ×3 |
| K08 | Mobil moderasyon + geri al | Q4 ×3 |
| K13 | Raid ön kontrolü (Raid Gate) | Q4 ×3 |

Sınırda olanları ya da herhangi birini geri almak istersen savunman yeterli.
