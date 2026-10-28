# Karar rehberi: 4 finalist, final seçimi için

Hazırlanma tarihi 28 Ekim 2026; aynı gün finalistlere göre güncellendi. Bu doküman, 4 finalist arasından final projeyi seçmen için gereken her şeyi tek yerde topluyor.

**Senin 28 Ekim kararların:**
- **Finalistler:** Minefield, Checkpoint, VAR, Tap on the Shoulder. Hint Jar, Studio Audience ve Raid Torch finale alınmadı (bkz. [bölüm 12](#12-finale-alınmayan-ve-elenen-projeler)).
- **Kart MVP bütçesi 9,5 saatten 12 saate çıktı.** Toplam yapım süresi: ortak altyapı 3,5 + MVP 12 + tampon ≥2 = **yaklaşık 17,5 saat**. Video bu sürenin dışında.
- **Checkpoint'e SSS özelliği eklendi.** Diğer üç projeye de benim önerdiğim eklemeler kondu; her projede **"12 saatlik eklemeler"** başlığı altında.

**Önemli:** Puanlar eski kartlara göre verildi. 12 saatlik eklemeler yeniden puanlanmadı. Eklemelerin hangi kritere yarayacağı benim tahminim. Kısa kayıt: [finalistler.md](finalistler.md).

Kaynaklar:
- Kartlar: [../step6/cards.md](../step6/cards.md), revizyon 3
- Birleştirilmiş kanıt: [../step6/evidence/aggregate.md](../step6/evidence/aggregate.md)
- Puanlama sonuçları: [ranking.md](ranking.md)
- Üç puanlayıcının ham cevapları: [results-grok.md](results-grok.md), [results-astra.md](results-astra.md), [results-claude.md](results-claude.md)
- Pazar araştırması: [../research/stream-types.md](../research/stream-types.md)

Puanlayıcıların söyledikleri ile benim görüşümü ayrı tuttum. Benim görüşüm her bölümde **"Benim görüşüm"** başlığı altında.

---

## İçindekiler

1. [Tek bakışta özet](#1-tek-bakışta-özet)
2. [Yarışma: jüri neye bakıyor](#2-yarışma-jüri-neye-bakıyor)
3. [Twitch sözlüğü: terimler ne demek](#3-twitch-sözlüğü-terimler-ne-demek)
4. [Senin makinen ve telefon/hesap ihtiyacı](#4-senin-makinen-ve-telefonhesap-ihtiyacı)
5. [Ortak altyapı: her projede aynı olan 3,5 saat](#5-ortak-altyapı-her-projede-aynı-olan-35-saat)
6. Finalistler, puan sırasına göre:
   1. [Minefield](#61-minefield--163-puan-risk-yüksek)
   2. [Checkpoint](#62-checkpoint--150-puan-risk-orta)
   3. [VAR](#63-var--150-puan-risk-orta)
   4. [Tap on the Shoulder](#64-tap-on-the-shoulder--143-puan-risk-orta)
7. [Karşılaştırma matrisi](#7-karşılaştırma-matrisi)
8. [Kararsız kalırsan: ikili karşılaştırmalar](#8-kararsız-kalırsan-ikili-karşılaştırmalar)
9. [1. gün testleri ve karar ağacı](#9-1-gün-testleri-ve-karar-ağacı)
10. [Zaman çizelgesi](#10-zaman-çizelgesi)
11. [Önceki araştırmalardan önemli bulgular](#11-önceki-araştırmalardan-önemli-bulgular)
12. [Finale alınmayan ve elenen projeler](#12-finale-alınmayan-ve-elenen-projeler)
13. [Benim önerim](#13-benim-önerim)

---

## 1. Tek bakışta özet

| # | Proje | Bir cümlede | Puan (ort.) | Risk | Ana test | 12 saatlik eklemeler |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | **Minefield** | İzleyiciler gizlice "kelime mayını" eker. Yayıncı o kelimeyi söyleyince ekranda patlar ve ekleyenin adı çıkar. | **16,3** | Yüksek | T1 (konuşmada kelime yakalama) | Fitil, mayın tarama, Bomb Squad tablosu |
| 2= | **Checkpoint** | Yayıncı işe gömülüyken mesajlar biriktirilir. Molada yayıncı sesli cevap verir, cevap yazıya dökülür ve izleyiciye alıntı olarak gönderilir. | **15,0** | Orta | T1b (cevabı yazıya dökme) | **SSS**, cevabın klip linki, geri alma penceresi |
| 2= | **VAR** | Chat bir an'a itiraz edince (`!var`) futboldaki VAR gibi ağır çekim tekrar, 15 saniyelik chat jürisi, karar damgası ve klip gelir. | **15,0** | Orta | T2 (OBS tekrar) | VAR beklemede, telestrator, hakem itibarı |
| 4 | **Tap on the Shoulder** | Mikrofon kapalı ya da ses uzak gelince chat'in uyarısı masadaki telefon yüzüne yansır, chat de düzeltmeyi onaylar. | **14,3** | Orta | T2 (OBS mute/sessizlik), T4 (telefonda HTTPS) | Sakin mod, soundcheck, siyah/donmuş ekran, sorun raporu |

Puan, 4 kriterin (her biri 1–5) üç puanlayıcıya göre ortalamasının toplamıdır; en fazla 20 olabilir. Puanlar eski (8,5–9,5 saatlik) kartlara göre verildi. Her projenin MVP'si artık 12 saat.

**Kısaca durum:**
- **En yenilikçi ve en izlenesi proje Minefield.** Üç model de Innovation ve Design'a 5 verdi. Ama her şey konuşmadan kelime yakalama testine (T1) bağlı. Ayrıca "birine kelime söyletme" türü parti oyunlarından biliniyor (bkz. 6.1), bu yüzden gerçekçi Innovation beklentisi 4.
- **Checkpoint en faydalı proje** (Impact 4/4/4). SSS ile "her yayın açık kalan araç" profili güçlendi. Puanı kısmen Claude puanlayıcısına dayanıyor.
- **VAR en güvenli "izlemesi eğlenceli" seçenek.** Konuşma tanımaya ihtiyacı yok ve üç model ona birebir aynı puanları verdi. Zayıf yanı yenilik: parçaları zaten var.
- **Tap faydalı ama akılda kalıcılığı zayıf.** Eklemeler kullanım sıklığını artırıyor ama Innovation'ı (3,0) değiştirmiyor.

---

## 2. Yarışma: jüri neye bakıyor

| Konu | Detay |
| --- | --- |
| Son teslim | **2 Kasım 2026, 14:00 PT** (Türkiye saatiyle 3 Kasım 01:00; ABD 1 Kasım’da kış saatine geçiyor, yani PST = UTC−8) |
| Jüri dönemi | 5–15 Kasım 2026 |
| Ne teslim ediliyor | Kod reposu ve **3 dakikadan kısa** bir YouTube videosu. Video projenin Twitch'te çalıştığını **ve Codex'i nasıl kullandığını** göstermeli. |
| Jüri ne yapıyor | Kurallara göre jüri projeyi denemek zorunda değil. **Sadece açıklama, görseller ve videoya bakarak puan verebilir.** Yani pratikte video her şey. |
| Kriterler (eşit ağırlık) | **Innovation/Idea:** ne kadar yaratıcı ve yeni, mevcut şeylerden farkı ne?<br>**Potential Impact:** yayıncılar ve toplulukları için ne kadar faydalı ya da eğlenceli?<br>**Technological Implementation:** teknik uygulama, Codex kullanımı dahil.<br>**Design:** kullanımı kolay mı, izlemesi eğlenceli mi? |
| Finalistler | Toplam puanı en yüksek 5 proje finalist olur. |
| **Resmi eşitlik bozma** | Eşitlikte önce **Innovation** puanına bakılır, sonra sıradaki kriterlere. |
| Birden fazla başvuru | Serbest, ama her başvuru "unique and substantially different" olmalı; ayrı video, repo ve Codex session ID gerekir. 17,5 saatlik yapım süresiyle ikinci bir proje gerçekçi değil. |
| Bizim kısıtlarımız | Yaklaşık 17,5 saat geliştirme (3,5 ortak + 12 MVP + 2 tampon); 1 yayıncı + 3 test hesabı; videoda ticari oyun ya da müzik yok; Twitch içeriği en fazla 24 saat tutuluyor. |

**Bu kurallardan çıkan iki pratik sonuç:**
1. **İlk 20 saniye kritik.** Jüri videoya bakıp puanlıyor ve fikri ilk saniyelerde kavramalı. Bu yüzden "Design" kriterinde ilk 20 saniyede anlaşılırlığa baktık.
2. **Innovation hem bir kriter hem de eşitlik bozucu.** Bu, Innovation'da 5 alan Minefield'ın lehine.

---

## 3. Twitch sözlüğü: terimler ne demek

Twitch'e yeni olduğun için bu dokümanda geçen terimleri örneklerle açıklıyorum.

### Yayın ve kitle

| Terim | Ne demek | Örnek |
| --- | --- | --- |
| **Yayıncı (streamer)** | Kanalda canlı yayın yapan kişi. | Sen, demo videosunda. |
| **Chat** | Yayının yanındaki canlı sohbet. İzleyiciler buraya yazar. | "LUL", "pineapple on pizza??" |
| **Mod (moderatör)** | Yayıncının yetki verdiği kişi. Mesaj siler, ban atar; bizim projelerde ayrıca özel butonlara erişir. | Test hesaplarından biri mod olacak. |
| **Lurker** | Yayını izleyen ama hiç yazmayan kişi. | Checkpoint'in SSS cevabını sessizce okuyan kişi. |
| **Emote** | Twitch'e özel küçük resim/ifade. Chat'te kelime gibi yazılır. | `LUL` (gülme), `KEKW` (kahkaha). |
| **Just Chatting** | Oyun olmayan, sohbet ağırlıklı yayın kategorisi. Twitch'in en büyüğü, izlenmenin %14,2'si. | Yayıncı kamerada izleyicilerle konuşuyor. |
| **IRL** | "In Real Life": dışarıda, telefonla yapılan yayınlar. | Sokakta yürürken yayın. |
| **Backseating** | İzleyicinin istenmeden yol göstermesi, oyunu "arka koltuktan yönetmesi". | "SOL KAPI!!", "envantere bak". |

### Raid ve topluluk

Finalistlerin hiçbiri raid kullanmıyor, ama bunlar Twitch'in temel kavramları.

| Terim | Ne demek | Örnek |
| --- | --- | --- |
| **Raid** | Yayıncı yayınını bitirirken izleyicilerini toplu halde başka bir canlı kanala gönderir. Yayıncı `/raid kanaladı` yazar, 10–90 saniyelik bir geri sayım başlar (iptal edilebilir), sonra bütün izleyiciler otomatik olarak hedef kanala geçer. Hedef kanalda "X 23 izleyiciyle raid yapıyor!" uyarısı çıkar. | A kanalı yayını bitirirken 23 izleyicisini B'ye yollar. |
| **Raid train (raid treni)** | Birbirini tanıyan yayıncıların sırayla yayın yapıp her birinin bir sonrakine raid atması. | DJ'ler akşam 18'de, 20'de, 22'de sırayla. |
| **Hate raid** | Bot hesaplarla yapılan taciz amaçlı raid (2021'de yaygınlaştı). Küçük yayıncılar bu yüzden raid'lere temkinli yaklaşıyor. | — |

### Twitch'in teknik parçaları

| Terim | Ne demek | Bizim kullanım |
| --- | --- | --- |
| **Helix API** | Twitch'in REST API'si: mesaj gönderme, klip açma, marker ekleme vb. | `Send Chat Message`, `Create Clip`, `Create Stream Marker`. |
| **EventSub** | Twitch'in olay bildirimleri. Bir WebSocket açarsın; "chat mesajı geldi", "raid oldu", "takip edildi" gibi olaylar sana akar. | `channel.chat.message`, `channel.raid`. |
| **OAuth / scope** | Uygulamanın yayıncı ya da bot adına işlem yapma izni. Her işlem için ayrı izin (scope) gerekir. | Klip için `clips:edit`, marker için `channel:manage:broadcast`. |
| **Bot hesabı** | Chat'e yazan otomatik hesap (bizim uygulama). Mod yapılırsa 30 saniyede 20 yerine 100 mesaj gönderebilir. | Checkpoint'in alıntılı cevapları. |
| **Clip (klip)** | Yayından kesilmiş 5–60 saniyelik paylaşılabilir parça. `Create Clip` çağrıldığı andan yaklaşık 85 saniye öncesi ile 5 saniye sonrası arasındaki pencereden kesilir. Oluşturma asenkron, yani birkaç saniye sürer. | VAR, Minefield: başlıklı klip. |
| **Stream marker** | Yayının zaman çizelgesine konan işaret. Sadece kanalda geçmiş yayınları saklama (VOD) açıksa çalışır. | "Mayın patladı" işareti. |
| **VOD** | Yayının sonradan izlenebilen kaydı. | Kurulumda açılacak. |
| **Threaded reply** | Chat'te belirli bir mesaja "yanıt" olarak gönderilen mesaj. İzleyici, kendi mesajının altında görür. Teknik olarak `reply_parent_message_id` ile yapılır; sınır 500 karakter. Mesaj AutoMod'a takılırsa `drop_reason` döner. | Checkpoint'in özü. |
| **Whisper** | Twitch'in özel mesajı (DM). API ile göndermek için gönderenin telefon doğrulaması gerekir. | Sadece stretch hedeflerde. |
| **AutoMod** | Twitch'in otomatik mesaj filtresi. | Klip başlıkları ve cevaplar buna takılabilir. |
| **Stream delay (gecikme)** | İzleyicinin gördüğü görüntü gerçek zamanın 2–5+ saniye gerisinden gelir ve gecikme her izleyicide farklıdır. | VAR'ın tekrarı ve Tap'in onay döngüsü buna göre ayarlanır. |
| **Channel points / Bits** | İzleyicinin kazandığı puanlar / parayla alınan Twitch kredisi. | Rakip ürünler kullanıyor, biz değil. |

### OBS tarafı

| Terim | Ne demek | Bizim kullanım |
| --- | --- | --- |
| **OBS** | Yayını hazırlayıp Twitch'e gönderen ücretsiz yayın programı. | Bütün projeler. |
| **Browser source** | OBS'te yayının üstüne bir web sayfası koymak. "Overlay" denen grafik katmanı genelde budur. | Patlama, jüri sırası, kavanoz... |
| **Dock** | OBS içinde yayıncının gördüğü ama yayına çıkmayan panel; bir web sayfasıdır. | Mod paneli, Checkpoint kontrolü. |
| **obs-websocket** | OBS'i dışarıdan kod ile kontrol etme protokolü (OBS 28+ ile birlikte gelir). | Tekrar oynatma, mikrofon durumu. |
| **Replay buffer** | OBS'in son N saniyeyi hafızada tutması; komutla dosyaya kaydedilir. | VAR'ın tekrarı. |
| **Media Source** | OBS'te video dosyası oynatan kaynak. Hızı ayarlanabilir. | VAR'ın ağır çekimi. |

### Konuşma tanıma (ML tarafı, senin alanın)

| Terim | Ne demek |
| --- | --- |
| **STT (speech-to-text)** | Konuşmayı yazıya çevirme. |
| **faster-whisper** | OpenAI Whisper'ın hızlı (CTranslate2) sürümü. GPU'da float16 ile çok hızlı çalışır. Modeller: `base.en`, `small.en`, `medium.en`, `large-v3-turbo`. |
| **VAD** | Voice Activity Detection: sesin konuşma mı sessizlik mi olduğunu bulur (ör. Silero VAD). Whisper'ın sessizlikte uydurma yapmasını (hallucination) önler. |
| **Hotwords** | faster-whisper'a "bu kelimeler geçebilir" diye verilen ipucu listesi. Doğru tanımayı artırır, ama sessizlikte uydurma riskini de artırır; bu yüzden VAD şart. |
| **Keyword spotting** | Sürekli konuşmada belirli kelimeleri yakalama. |
| **Hit / false alarm / lag** | Doğru yakalama / söylenmemiş kelimeyi yakalamak / söyleyişten tepkiye kadar geçen süre. |

---

## 4. Senin makinen ve telefon/hesap ihtiyacı

### Makine: ne anlama geliyor?

| Parça | Değer | Etkisi |
| --- | --- | --- |
| GPU | **RTX 4070 Laptop, 8 GB VRAM** | faster-whisper `small.en` ve `medium.en` float16 ile rahat sığar. `large-v3-turbo` de büyük ihtimalle sığar. 2 saniyelik bir pencere GPU'da 1 saniyeden çok daha kısa sürede işlenir. **Hız riski büyük ölçüde ortadan kalkıyor; kalan risk doğruluk ve yanlış alarm.** |
| GPU + yayın | OBS videoyu NVENC ile kodlar; NVENC GPU'da ayrı bir donanım birimi. | Whisper ile yayın kodlama birbirini pek etkilemez. T1 yine de "kare düşmesi yok" şartını ölçecek. |
| CPU / RAM | Ryzen 7 8845HS, 32 GB | Fazlasıyla yeterli. |
| İşletim sistemi | Windows 11 + WSL2 (repo WSL içinde) | **Dikkat:** WSL2 içinden mikrofona erişmek güvenilmez. OBS de Windows'ta çalışacak. **Öneri:** ses yakalama ve STT'yi Windows'ta yerel Python süreci olarak çalıştırmak (CUDA Windows'ta sorunsuz). Diğer kısımlar WSL'de kalabilir. obs-websocket'e WSL'den bağlanmak için Windows host IP'si ya da WSL "mirrored networking" gerekir. Bunlar T1 sırasında doğrulanacak. |

**Bir de dil riski var:** Video ve jüri İngilizce, yani Minefield ve Checkpoint'te **senin aksanlı İngilizcen** tanınacak. Whisper aksanlarda genelde iyidir. T1 ve T1b testlerini mutlaka **kendi sesinle, doğal konuşarak** yapmalıyız; hazır kayıtlarla değil.

### Telefon ve hesaplar: hangi proje ne istiyor?

| Proje | Telefon gerekli mi? | Kaç tane? | Neden |
| --- | --- | --- | --- |
| **Minefield** | Şart değil ama **arkadaş şart gibi** | Senin telefonun + **1–2 arkadaş** (kendi telefonlarından) | Kart özellikle şunu istiyor: mayın kelimelerini sen değil arkadaşların eksin. Böylece kelimeyi gerçekten bilmezsin ve demo sahnelenmiş görünmez. Arkadaşlar test hesabına telefondan giriş yapıp ekme sayfasını açar. |
| **Tap on the Shoulder** | **Evet** | **1 yedek telefon** kamera kadrajında, masada ("telefon yüzü"). Mod butonları için ikinci bir cihaz (2. telefon ya da laptop tarayıcısı) iyi olur. | Ürünün kendisi masadaki telefon yüzü. |
| **Checkpoint** | Hayır | — | 3 test hesabı chat simülatörüyle mesaj atar. Arkadaş gerçek soru sorarsa daha doğal görünür; SSS sahnesi için ikinci bir kişinin aynı soruyu sorması gerekir. |
| **VAR** | Hayır | — | `!var` ve oyları simülatör ya da arkadaşlar yazar. Telestrator çizimini sen ya da mod hesabı dock'tan yaparsın. |

**Test hesapları için telefon numarası:**
- Twitch hesabı genelde e-postayla açılabiliyor; Twitch ek olarak telefon doğrulaması isteyebilir. Kaç hesabın aynı numaraya bağlanabileceği **doğrulanmadı**. Hesapları açarken göreceğiz; senin numaran ve 1–2 arkadaşın numarası büyük ihtimalle yeter.
- Kanal sahibi sensin; "chat için telefon doğrulaması iste" ayarını kapalı tutabilirsin.
- Whisper (DM) ile mesaj göndermek telefon doğrulaması istiyor ama bu hiçbir projenin MVP'sinde yok, sadece stretch hedeflerde.

**Kısa cevap:** Minefield, Checkpoint ve VAR için ekstra telefon gerekmiyor. Ama Minefield için **1–2 arkadaşın gerçekten katılması** demoyu çok güçlendirir. Tap seçilirse 1 yedek telefon gerekir; sende 1 telefon var, arkadaşlardan 2–3'e çıkabiliyorsun, yani yetiyor.

---

## 5. Ortak altyapı: her projede aynı olan 3,5 saat

Hangi projeyi seçersen seç önce bu kurulur:

| Parça | Saat | Ne yapar |
| --- | --- | --- |
| Twitch uygulaması, yayıncı ve bot için OAuth, token yenileme | 1 | Uygulama Twitch'te yayıncı ve bot adına işlem yapabilir. |
| EventSub WebSocket (chat, yeniden bağlanma) + Send Chat Message | 0,5 | Chat'i okur ve chat'e yazar. |
| Yerel sunucu (FastAPI), OBS overlay'lerine WebSocket ile veri gönderimi, OBS dock | 0,5 | Senin bildiğin Python/FastAPI tarafı. |
| obs-websocket bağlantısı | 0,5 | OBS'i koddan kontrol eder. |
| **Chat simülatörü** | 1 | 3 test hesabı, gerçek Twitch API üzerinden senaryolu mesajlar atar. Prova, test ve video çekimi için kullanılır. Twitch CLI chat mesajı taklit edemediği için gerekli. |

**Codex hikâyesi:** Videoda "Codex'i nasıl kullandık" kısmı zorunlu. Chat simülatörü her projede Codex'in ortak payı; ayrıca her projenin kendine özgü bir "Codex artifact"ı var. Bunlar aşağıda her projede ayrıca yazılı.

**Bütçe hesabı (28 Ekim'de güncellendi):** 3,5 saat ortak altyapı + 12 saat proje MVP'si + en az 2 saat tampon = **yaklaşık 17,5 saat**. Demo oyunu gerekirse yaklaşık 1 saati tampondan gider.

**12 saatlik eklemeler nasıl seçildi:** Her ekleme şu üç şarttan en az birini karşılamalı:
1. O projenin puanlayıcıların söylediği zayıflığını kapatmalı.
2. 3 dakikalık videoya yeni ve anlaşılır bir sahne eklemeli.
3. Aracı "bir kez denenen oyuncak" olmaktan çıkarıp "her yayında açık kalan araç" yapmalı (Impact).

Sadece cila olan, videoda görünmeyen ya da yeni bir dış bağımlılık getiren eklemeler alınmadı.

---

## 6.1 Minefield — 16,3 puan, risk Yüksek

### Ne?
İzleyiciler gizlice "kelime mayınları" eker. Yayıncı sıradan konuşurken o kelimeyi söylerse ekranda patlama olur ve mayını ekleyenin adı çıkar.

### Somut örnek
> Sen yayında öğle yemeğinden bahsediyorsun. Bo 6 dakika önce gizlice "PINEAPPLE" kelimesini ekmiş. Chat'te Bo soruyor: "worst pizza topping?" Sen "pineapple on pizza is—" derken **BOOM**: ekran sallanır, afiş çıkar: *"Bo's mine: PINEAPPLE (planted 6 min ago)"*. Bo chat'e "GOT HIM 😈" yazar.

### Nasıl çalışır (adım adım)
1. İzleyici `!mine` yazar. Bot ona ekme sayfasının linkini verir; sayfa Twitch girişi istiyor. İzleyici kelimeyi orada yazar ve kimse görmez.
2. Overlay'de mayın çipleri görünür: sadece sahiplerin adları var, kelimeler yok. Kurallar:
   - izleyici başına aynı anda 1 mayın;
   - en az 4 harf;
   - en yaygın 1000 kelimeden biri olamaz;
   - yasaklı kelime listesi var.
3. İzleyiciler sohbeti kendi kelimelerine doğru çekmeye çalışır; asıl oyun bu "tuzak kurma" kısmı.
4. Yerel STT yayıncının mikrofonunu dinler. faster-whisper kayan yaklaşık 2 saniyelik pencerelerle çalışır; VAD açıktır, aktif mayınlar `hotwords` olarak verilir ve normalize edilmiş metinde tam kelime eşleşmesi aranır (çoğullar da sayılır).
5. **Fitil (12 saatlik ekleme):** Eşleşmenin güveni yüksekse anında patlama, afiş ve stream marker gelir. Güven orta seviyedeyse ekranda yanan bir fitil ve 3 saniyelik tık-tık sesi çıkar, sonra patlar; mod ya da yayıncı bu sırada fitili kesebilir.
6. Patlamadan sonra mod 10 saniye içinde **DEFUSE** edebilir: geri sarma animasyonu ve "false alarm" damgası çıkar, yanlış tanıma bir şakaya dönüşür. DEFUSE edilmezse 30 saniyelik başlıklı klip açılır.
7. **Mayın tarama (12 saatlik ekleme):** Yayıncının yayın başına 3 tarama hakkı var. Bir tuzaktan şüphelenince kelimeyi **söylemeden** dock'a yazar (söylerse patlar). Kelime canlı bir mayınla eşleşirse mayın "SWEPT" olur ve ekleyenin çipi söner. Yanlışsa tarama hakkı gider.
8. Yayın sonunda patlamayan mayınlar "dud" olarak açılır: *"Cy's mine 'GIRAFFE' never went off"*. Altında **Bomb Squad tablosu (12 saatlik ekleme)** görünür: en çok patlatan izleyici, en uzun yaşayan mayın, yayıncının tarama isabeti. Tablo yayınlar arasında saklanır.

### 3 dakikalık video akışı
| Zaman | Ne oluyor |
| --- | --- |
| 0:00 | Hook: öğle yemeği sohbeti, "pineapple" BOOM, afiş, Bo'nun tuzak sorusuna geri dönüş. |
| 0:20 | Nasıl çalışır: `!mine`, ekme sayfası, çipler, kurallar. |
| 0:50 | İkinci tur: iki izleyici tuzak kurar. Yayıncı birinden şüphelenir, kelimeyi söylememek için dock'a yazar: "SWEPT". Diğeri tutar: BOOM. |
| 1:25 | Belirsiz bir tanıma: fitil yanar, tık-tık, mod keser, "false alarm". |
| 1:45 | Yayın sonunda dud'ların açılması ve Bomb Squad tablosu. |
| 2:00 | Kaputun altı: yerel STT, hiçbir şey kaydedilmiyor; doğruluk harness'inden sayılar. |
| 2:30 | Codex artifact, kapanış. |

### Teknik detay
- **Mimari:**
  - **STT süreci (Windows'ta Python):** mikrofon → VAD → faster-whisper (GPU) → metin.
  - **Eşleşme:** metin normalize edilir (küçük harf, noktalama silinir, çoğul eki atılır) ve aktif mayınlarla tam kelime olarak karşılaştırılır.
  - **Tekrar önleme:** pencereler örtüştüğü için aynı söyleyiş iki kez patlamamalı.
  - **Patlama:** FastAPI → WebSocket → OBS overlay.
- **Twitch:**
  - EventSub `channel.chat.message`, Send Chat Message;
  - Create Stream Marker (`channel:manage:broadcast`, VOD açık olmalı);
  - Create Clip (`clips:edit`);
  - ekme sayfası için Twitch girişi ve herkese açık URL (cloudflared ya da ngrok tüneli; bilgisayar uykuya geçerse tünel kapanır).
- **Saatler:**

| Parça | Saat |
| --- | --- |
| Ekme sayfası + Twitch girişi + herkese açık URL | 1,5 |
| STT kelime yakalayıcı + eşleşme kuralları | 2,5 |
| Doğruluk harness'i | 1 |
| Overlay: çipler, patlama, afiş | 2 |
| Marker, klip, DEFUSE, dud'lar | 1,5 |
| Cila | 1 |
| *Eski MVP toplamı* | *9,5* |
| **+ Fitil:** güven skoruna göre iki aşamalı patlama, eşiği harness'le ayarlama | 1 |
| **+ Mayın tarama:** dock'ta yazma alanı, 3 hak, SWEPT animasyonu | 1 |
| **+ Bomb Squad tablosu:** SQLite, yayın sonu ekranı | 0,5 |
| **Yeni MVP toplamı** | **12** |
| Bilerek alınmayanlar: whisper ile ekme 0,5 (sadece T4 başarısız olursa yedek; fısıltı için telefon doğrulaması gerekebilir, doğrulanmadı); "Call it" modu 1,5 | — |

- **Codex artifact:** Doğruluk harness'i. Kaydedilmiş konuşmaları yakalayıcıdan geçirir; hit, yanlış alarm ve gecikmeyi raporlar. Videoda bu sayıları göstermek teknik güven verir.

### Rakipler ve fark
| Rakip | Ne yapıyor | Fark |
| --- | --- | --- |
| **OK Gamers** (TwitchCon Hackathon 2019 **büyük ödülü**) | Yayıncı "Ok gamers" + soru deyince STT chat anketi başlatır. | Kelimeyi yayıncı seçiyor. |
| Streamer.bot Voice Control (yaygın) | Yayıncının ayarladığı cümleler aksiyon tetikler. | Kelimeyi yayıncı seçiyor. |
| Konuşma tanımalı küfür kavanozları (Blabla Radar, obs-popup-overlay) | Listedeki kelimeleri sayar. | Liste yayıncının, oyun yok. |
| Gizli kelime chat oyunları (AnkhbotSecretWord), Taboo tarzı oyunlar (Wordeous), yayın bingo'su | — | Hepsi yazılı chat'te oynanıyor. |

**Fark (üç araştırmacı ve link kontrolü hemfikir):** Bulunan bütün konuşma tetikleyicileri yayıncının seçtiği kelimeleri kullanıyor; izleyicinin gizli kelime seçtiği bütün oyunlar ise yazılı chat'te geçiyor. **İzleyicinin gizlice seçtiği kelimeyi yayıncının kendi konuşmasının patlatması hiçbir yerde bulunamadı.**

Önemli bir not: 2019'da aynı yarışmanın büyük ödülünü bir STT + chat projesi (OK Gamers) kazanmış. Bu, jürinin bu tür fikirlere açık olduğunu gösteriyor. Ama "OK Gamers'ın devamı" gibi algılanmamak için videoda farkı açıkça göstermek gerekir.

**Türün kendisi biliniyor (28 Ekim'de ek arama yapıldı; puanlayıcılar bunu görmedi).** "Birine bir kelimeyi söyletmek" eski bir parti oyunu fikri. [Don't Get Got](https://draughtslondon.com/ultimate-guide-to-the-dont-get-got-game/) (Big Potato) adlı oyunun gizli görevlerinden biri "bir oyuncuya 'banana' dedirt". Twitch'te en yakın örnek [Heads Up! Phones Down](https://support.aspyr.com/hc/en-us/articles/22586269678093-Heads-Up-Phones-Down-Edition-Twitch-Extension-Overview) eklentisi: kelime yayıncıdan gizleniyor, izleyiciler chat'e ipucu yazıyor. Ama burada kelimeyi oyun seçiyor ve yayıncının konuşması dinlenmiyor. Bu yüzden bir jüri "Don't Get Got'un Twitch hâli" ya da "STT ile anahtar kelime tetikleme" diyebilir. Bizim puanlayıcılar Innovation'a 5 verdi, ama yalnızca Twitch araçlarındaki kanıtı gördüler. Gerçekçi beklenti 4. Fark videoda görünmezse 3 de verilebilir.

### Talep ve karşı sinyaller
- **Doğrudan talep yok.** Üç araştırmacı da bu oyunu isteyen birini bulamadı.
- **Dolaylı talep:** yayıncılar elle küfür kavanozu ve bingo kartı yürütüyor; iki Reddit başlığında "mikrofonda kelime algılayıp efekt tetikleme" isteniyor (doğrulanmadı).
- **Karşı sinyal:** troller yayıncılara zaten bir şeyler söyletmeye çalışıyor (Dexerto 2019, doğrulandı). Bu oyun bunu ödüllendirdiği için yasaklı kelime listesi şart.
- **Teknik karşı sinyal:** faster-whisper `hotwords` sessizlikte kelime uydurabiliyor (GitHub issue 1356, doğrulandı); çözümü VAD'ı açık tutmak.

### Kitle
Yayıncının konuştuğu her yayın: Just Chatting (%14,2), IRL (%1,8) ve konuşkan oyun yayınları. Twitch'in en büyük kategorisi doğrudan hedefte. Ama oyunun gerçekten eğlenceli olup olmadığı test edilmedi.

### Riskler, test ve yedek plan
| Risk | Ne kadar ciddi | Önlem |
| --- | --- | --- |
| **STT doğal konuşmada kelimeyi kaçırır ya da olmayan kelimeyi yakalar** | **Proje bunun üzerine kurulu.** | T1: en az %80 yakalama, 10 dakikada en fazla 1 yanlış alarm, en fazla 3 saniye gecikme, kare düşmesi yok. |
| Aksanlı İngilizce | Orta | T1'i kendi sesinle yap; gerekirse `medium.en` ya da `large-v3-turbo` (4070'te sığar). |
| Gizli ekme sayfası | Düşük–orta | T4: Twitch girişi, herkese açık URL. |
| Oyun gerçekten eğlenceli mi? | Orta | 3 kişiyle 20 dakikalık deneme. |
| Trol kelimeler | Düşük | Yasaklı kelime listesi. |
| "Bir jüri bunu Don't Get Got'un Twitch hâli sayar" | Orta | Benzerliği açıklamada sahiplen; mayın tarama oyunu iki taraflı yapar; ilk 20 saniyede "izleyici seçti + sohbetle tuzak + kuranın adı" görünsün. |
| **Yedek plan** | **Yok** | Kart bunu açıkça söylüyor. Fitil ve DEFUSE yanlış alarmları yumuşatır: belirsiz tanıma yanlış patlama yerine gerilim olarak görünür. Ama çok sık hata varsa bunlar da kurtarmaz. |

### Puanlar ve modellerin söyledikleri
| | Innovation | Impact | Tech | Design | Toplam | Risk | Sıra |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Grok | 5 | 3 | 3 | 5 | 16 | Yüksek | **1** |
| Astra | 5 | 3 | 3 | 5 | 16 | Yüksek | 2 |
| Claude | 5 | 3 | 4 | 5 | 17 | Orta | **1** |
| **Ortalama** | **5,0** | **3,0** | **3,3** | **5,0** | **16,3** | | |

- **Grok:** "Aramanın gerçekten kaçırdığı döngü bu." Ama "bir kaçırma ya da sahte bir patlama, ürünün ta kendisi". Yedek yakalayıcı olmamasını en büyük risk olarak görüyor.
- **Astra:** DEFUSE'un "sık algılama hatalarını telafi etmediğini" söylüyor. İzleyiciler hatayı yakalayıcıya değil mayını ekleyene yormalı; bu güven kurulmazsa şaka çöker. Konuşma tanıma test edilmediği için onu Hint Jar'ın arkasına, 2. sıraya koydu.
- **Claude:** Tech'e 4 verdi: lokal keyword spotting teknik olarak ilginç ve harness güçlü bir Codex örneği. Riski "Orta" gördü çünkü DEFUSE ve yasaklı liste yanlış tanımaları yumuşatıyor.
- **Üçünün ortak görüşü:** Setteki en yeni fikir ve ilk 20 saniyede en izlenesi. Kartın kaderi T1'e bağlı.

### Benim görüşüm
- **Avantaj:** Yarışmayı **kazanabilecek** tek proje bu bence; diğerleri daha çok "finale kalır" profilinde. İnsan bunu bir kez görünce anlatmak ister ("chat bana kelime mayını döşedi!").
- **ML altyapın burada avantaj.** VAD, hotword, eşik ayarı, değerlendirme harness'i senin uzmanlık alanın.
- **4070 hız sorununu çözüyor.** Asıl soru, 10 dakikalık doğal konuşmada 1'den az yanlış alarm.
- **12 saatlik eklemeler neyi değiştiriyor:**
  - **Fitil**, Grok'un "sahte patlama ürünün kendisi" eleştirisine cevap. Senin ML tarafın burada parlıyor: güven skoruna göre karar vermek bir eşik ayarı problemi.
  - **Mayın tarama**, Innovation riskine cevap: yayıncıya oyunda bir rol verir. Videoda "söyleyemediği için yazıyor" anı kendi başına komik.
  - **Bomb Squad**, Impact'i destekler: her yayın yeniden oynanır.
- **Dezavantaj:** T1 kötü çıkarsa kurtaracak bir şey yok. Eklemeler hatayı yumuşatır, ama tanıma kötüyse oyun yine çöker.
- **Bunu seçersen:** 1. günün ilk işi T1. Sonuç kötüyse vakit kaybetmeden B planına geç. T1'de güven skorlarını da kaydet: fitil eşiği bu verilerle ayarlanır.

---

## 6.2 Checkpoint — 15,0 puan, risk Orta

### Ne?
Yayıncı çizim, kodlama ya da oyun gibi bir işe gömülmüşken chat'i görmezden gelmiş olmaz: mesajlar "kayıt kristali" olarak birikir. "Checkpoint" anında yayıncı mesajları **sesli** cevaplar; söylediği kelimeler karta yazılır ve her izleyici kendi mesajının altında yayıncının **gerçek sözlerini alıntılayan** bir yanıt alır.

Cevabı herkes görür: yayını izleyen herkes cevabı duyar ve kartta okur. Chat'teki alıntılı yanıt da herkese açık normal bir chat mesajıdır, fısıltı (whisper) değildir. Bu yanıtın tek farkı, soran kişiyi etiketlemesi ve onun mesajının altına bağlanmasıdır.

**SSS (12 saatlik ekleme, senin kararın):** Aynı soru aynı yayında tekrar gelirse yayıncı ikinci kez cevaplamaz; bot eski cevabı alıntılar.

### Somut örnek
> Sen mürekkeple çizim yapıyorsun, chat'e bakmıyorsun. 6 kristal birikiyor. Checkpoint'e basıyorsun. Ekranda kart: *"@ana (first time!): what pen is that?"* Elin hâlâ çiziyor ve diyorsun ki: "Ana, it's a Micron 05, it doesn't bleed." Kelimeler karta yazılıyor; 2 saniye sessizlik olunca ✓ ile kart uçuyor. 3 saniye sonra Ana'nın chat'inde, kendi mesajının altında: *"✓ answered on stream: 'It's a Micron 05, it doesn't bleed' (12:04)"*. Ana o sırada yayından çıkmış olsa bile geri döndüğünde cevabı görüyor; yanıttaki klip linkinden cevabı izleyebiliyor da.
>
> 20 dakika sonra Mehmet yayına geliyor ve "what pen is that?" yazıyor. Sen çizmeye devam ediyorsun. 1 saniye sonra bot Mehmet'in mesajına yanıt veriyor: *"📌 Answered earlier (12:04): 'It's a Micron 05, it doesn't bleed' ▶ clip · type !ask to ask anyway"*.

### Nasıl çalışır (adım adım)
1. Yayıncı bir kısayol tuşuna basar ya da mod `!focus` yazar. Köşede bir rozet çıkar: "Focus: messages saved 0".
2. Her normal izleyici mesajı, izleyicinin renginde bir kristal olarak düşer. Komutlar ve bot satırları filtrelenir. Mesajın id'si, yazarı, metni ve "ilk kez yazıyor" bilgisi saklanır.
3. Yayıncı "checkpoint"e basar. Alt kısımda bir "çağrı kartı" belirir: önce sorular, sonra ilk kez yazanlar.
4. Yayıncı işini bırakmadan sesli cevap verir. Yerel STT kelimeleri söylendikçe karta yazar.
5. Yaklaşık 2 saniyelik sessizlik ya da "next" demek kartı kapatır: ✓ damgası basılır, kart uçar. 3 saniye sonra bot izleyicinin mesajına alıntılı bir yanıt gönderir.
   - **Geri alma penceresi (12 saatlik ekleme):** Bu 3 saniye dock'ta görünür bir sayaç olur. Yayıncı alıntının yanlış olduğunu görürse "undo" tuşuna basar ve makbuz alıntısız düz makbuza döner.
   - Metin boş ya da güven skoru düşükse alıntı atlanır: "✓ answered on stream (12:04)". Böylece yanlış duyulmuş bir cümle izleyiciye "yayıncı böyle dedi" diye gitmez.
   - **Klip linki (12 saatlik ekleme):** Kart kapanınca bir klip açılır, linki makbuza eklenir. Yayından çıkmış izleyici cevabı sadece okumaz, izler de.
   - "Skip" kartı yanıt göndermeden kapatır.
6. Sonunda bir özet görünür: "Checkpoint cleared: 4 answered, 4 receipts sent, 2 auto-answered".
7. **SSS (12 saatlik ekleme):**
   - Her cevaplanan kart saklanır: soru, kesinleşmiş transkript, güven skoru, zaman, klip linki.
   - Yeni bir chat mesajı soru gibiyse (`?` içeriyor ya da soru kalıbıyla başlıyor), o yayında cevaplanmış sorularla karşılaştırılır.
   - Eşleşme varsa ve eski cevabın güveni yüksekse bot thread içinde eski cevabı alıntılar. Mesaj "yayıncı böyle dedi" diye değil, "daha önce şöyle cevaplandı" diye yazılır; `!ask` ile izleyici soruyu yine de kuyruğa sokabilir.
   - Focus modundaysa bu mesaj kristal olmaz; dock'ta "auto-answered" sayacına eklenir.

### 3 dakikalık video akışı
| Zaman | Ne oluyor |
| --- | --- |
| 0:00 | Hook: mürekkep çizimi hızlandırılmış, 6 kristal, checkpoint, Ana'nın sorusu, sesli cevap karta yazılıyor, ✓ ve split-screen'de Ana'nın chat'indeki alıntı. 0:19'da sıradaki kart. |
| 0:20 | İki kart daha: biri "skip", biri düşük güvenle düz makbuz. |
| 0:50 | **SSS:** Mehmet aynı soruyu soruyor, bot 1 saniyede eski cevabı ve klibi alıntılıyor. Yayıncı başını bile kaldırmıyor. |
| 1:15 | Yayından "ayrılmış" bir izleyici sonra chat'i açıp cevabı buluyor, klibi izliyor. |
| 1:35 | Kaputun altı: ses segmentleme, sessizlik kuralı, geri alma penceresi, reply threading, SSS eşleştirme. |
| 2:05 | Codex artifact. |
| 2:30 | Kapanış. |

### Teknik detay
- **Mimari:** mikrofon → VAD segmentleme → faster-whisper'ın büyüyen ses tamponunu yaklaşık 0,5 saniyede bir yeniden yazıya dökmesi (kısmi metin karta akar).
  - **Kapanış:** 2 saniye sessizlik olunca metin kesinleşir. "Hold" tuşuna basılıysa düşünme duraklaması kartı kapatmaz.
  - **Güven skoru:** `avg_logprob` ve `no_speech_prob` eşiklerinden hesaplanır.
  - **Gönderim:** `Send Chat Message` + `reply_parent_message_id`, metin 500 karaktere kırpılır. Cevaptaki `is_sent` ve `drop_reason` okunur.
  - **SSS eşleştirme:** Küçük bir embedding modeli (`all-MiniLM-L6-v2`, GPU'da milisaniyeler) ve kosinüs benzerliği. Başlangıç eşiği 0,85, kayıtlı soru çiftleriyle ayarlanır. Sadece aynı yayının cevapları kullanılır; MVP'de yayınlar arası hafıza yok.
  - **Klip:** Kart kapanınca `Create Clip` çağrılır (pencere yaklaşık 85 saniye geriye uzanıyor, cevap içinde kalır). Klip asenkron oluştuğu için makbuz klip hazır olana kadar birkaç saniye bekler; hazır olmazsa linksiz gider.
- **Twitch:** EventSub chat (`message_id` gerekli). Bot moderatör olmalı: 30 saniyede 100 mesaj gönderebilir.
- **Saatler:**

| Parça | Saat |
| --- | --- |
| Focus açma/kapama (kısayol, mod `!focus`) + filtre | 1 |
| Kristal rozet overlay'i | 1,5 |
| Çağrı kartı overlay'i (canlı transkript satırı, ✓ damgası) | 1,5 |
| Dock + sıralama + next/skip | 1 |
| Yerel STT: mikrofon, VAD segmentleme, faster-whisper, kısmi güncellemeler | 2 |
| Sesle kapanış: sessizlik kuralı, hold tuşu, kayıtlı seslerle ayar | 0,5 |
| Cevap makbuzu: güven eşiği, 500 karakter, threaded reply, `drop_reason` | 0,5 |
| Cila | 1 |
| *Eski MVP toplamı* | *9* |
| **+ SSS:** soru tespiti, embedding eşleştirme, eşik ayarı, auto-answered sayacı | 1,5 |
| **+ Cevabın klip linki** (eski stretch) | 1 |
| **+ Geri alma penceresi:** dock sayacı, undo tuşu | 0,5 |
| **Yeni MVP toplamı** | **12** |
| Hâlâ stretch: isimle kapatma 0,5; hatırlatıcı 0,5 | — |

- **Codex artifact:** Sesten makbuza giden pipeline; kayıtlı cevap sesleri ve simüle chat ile test edilir. SSS eşleştirmesi de simülatörün tekrar eden ve benzemeyen soru çiftleriyle test edilir.

### Pivot geçmişi (önemli)
- **Orijinal hâli** (mesajları biriktir, sonra ekrana çıkar) **Meld X AMA Question Queue** ile aynı çekirdek döngüydü. Meld yaygın bir ürün; sen de "aynı döngü" kararını verdin.
- **Kural gereği tek pivot hakkı kullanıldı ve C adayı seçildi:** sesli cevap + alıntılı makbuz.
- **Pivot sonrası fark tek kaynaktan (P) kontrol edildi.** Meld, StreamerQnA, Social Stream Ninja ve Senchabot'un hiçbiri yayıncıyı dinlemiyor ve cevaptan sonra izleyiciye bir şey göndermiyor. En yakın bulunanlar ters yönde çalışıyor: yapay zekânın chat'e sesli cevap verdiği araçlar.
- **Yedek plan, T1b başarısız olursa "pause trigger" (B adayı).** Uygulama, yayıncının işe ara verdiğini kendisi fark eder: iş ekranı durur (64×36 piksellik ekran görüntüsü farkı, saniyede 2 kez) **ve** mikrofonda konuşma başlar. Bunun üzerine "Checkpoint in 3…" geri sayımı başlar.
  - **Sorun:** Tetiklendikten sonraki çıktı yine Meld gibi bir soru kuyruğu. Yani yedek plan demoyu kurtarır ama yeniliği kurtarmaz.
  - **SSS yedek planda da çalışır mı?** Kısmen. Transkript yoksa saklanacak "cevap" da yok. Yayıncı cevabı dock'a kısaca yazarsa SSS yine çalışır, ama bu sesli cevabın sihrini kaybettirir.
  - **Astra'nın eleştirisi haklı:** Puanlayıcıların gördüğü kartta yedek plan sadece adıyla geçiyordu.

### Talep ve karşı sinyaller
- **Problem kanıtı orta düzeyde, setin en iyilerinden:**
  - Streamlabs rehberi elle yapılan versiyonu anlatıyor: odak yayınlarında chat'i okumak için planlı molalar, sorular için mod tarafından tutulan liste.
  - Art yayıncıları selamları kaçırıyor; cevap alamayan izleyiciler yazmayı bırakıyor (Reddit, doğrulanmadı).
  - Twitch de yeni gelenler eski mesajları görsün diye Chat History özelliğini geliştirdi.
- **Karşı sinyaller:**
  - Bazı izleyiciler beklemiyor; mesajı saklanan kişi yayında kalmayabilir. Makbuz bunu kısmen çözüyor.
  - Yanlış duyulan bir kelime izleyicinin alıntısına girebilir. Güven eşiği bunu azaltıyor.

### Kitle
İşe gömülü formatlar: çizim (Art kategorisi #40, kanal başına yaklaşık 17 izleyici), maker, kodlama, yemek ve odak gerektiren oyunlar. Haftalık değil, **her yayın** kullanılabilecek bir araç.

### Riskler, test ve yedek plan
| Risk | Önlem |
| --- | --- |
| STT hızı ve doğruluğu | **T1b:** 10 senaryolu cevapta alıntı en fazla 2 saniyede hazır olmalı, en az 9'u düzeltme gerekmeden okunur olmalı. 4070 hız riskini büyük ölçüde kaldırıyor. |
| Düşünme duraklaması kartı erken kapatır | 2 saniye eşiği + hold tuşu. |
| Yanlış duyulan kelime alıntıya girer | Güven eşiği: düşük güvende alıntısız makbuz. Geri alma penceresi: yayıncı 3 saniye içinde iptal eder. |
| SSS yanlış soruyu eşleştirir | Yüksek eşik; "daha önce şöyle cevaplandı" dili; `!ask` ile kuyruğa girme yolu. |
| AutoMod yanıtı düşürür | `drop_reason` okunur. |
| **Yedek plan** | Pause trigger (B). Demo yapılabilir ama yenilik düşer. |

### Puanlar ve modellerin söyledikleri
| | Innovation | Impact | Tech | Design | Toplam | Risk | Sıra |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Grok | 3 | 4 | 3 | 4 | 14 | Orta | 4 |
| Astra | 4 | 4 | 3 | 4 | 15 | **Yüksek** | 3 |
| Claude | 4 | 4 | 4 | 4 | 16 | Orta | 2 |
| **Ortalama** | **3,7** | **4,0** | **3,3** | **4,0** | **15,0** | | |

- **Grok:** Innovation'a 3 verdi. Kuyruktan soru öne çıkarmak bilinen bir döngü (Meld, StreamerQnA); farkı, karta yazılan sesli cevap ve alıntılı thread yanıtı. Impact 4: Streamlabs'in elle yapılan versiyonu haftalık bir alışkanlık olarak belgelemesi.
- **Astra:** Riski "Yüksek" gördü çünkü yedek plan yeterince tanımlanmamış. En büyük zayıflık olarak şunu söylüyor: erken kapanan ya da kendinden emin ama yanlış bir transkript, izleyiciye "yayıncının ağzından" yanlış bir cevap gönderebilir. Tasarımı faydalı ama bir patlamaya ya da tekrar görüntüsüne göre "daha az teatral" buluyor.
- **Claude:** Her kritere 4 verdi ve şunu ekledi: "Sesli makbuz olmazsa bu, Meld'in soru kuyruğu."
- **Ortak görüş:** Impact'te en güçlü proje (4/4/4). Yenilik de demo da T1b'ye bağlı.

### Benim görüşüm
- **Avantajlar:**
  - Gerçekten **faydalı**: "her yayın açılır" profilinde tek proje.
  - Minefield ile aynı STT altyapısını kullanıyor; T1 ve T1b tek oturumda test edilebilir.
  - T1b'nin çıtası T1'den düşük: okunabilir bir transkript Whisper'ın en iyi yaptığı iş.
- **Dezavantajlar:**
  - **İkinci sıra kısmen Claude puanlayıcısına dayanıyor.** Grok ve Astra'nın ortalamasında 14,5 ile 6. sıraya düşüyor.
  - Pivotu ben tasarladım, yani bir taraflılık ihtimali var. Pivot sonrası kanıt da tek kaynaklı.
  - Video sakin geçiyor: bir kart ve bir chat yanıtı, patlama yok. SSS sahnesi buna ikinci bir "vay" anı ekliyor ama yine de sakin.
- **12 saatlik eklemeler neyi değiştiriyor:**
  - **SSS**, Impact'i ve Innovation'ı birlikte güçlendiriyor. Art yayınlarında aynı soru sürekli tekrar sorulur. Rakiplerin hiçbiri cevabı saklayıp yeniden kullanmıyor (bunu ayrıca aramadık; kanıt adımındaki rakip tablosuna göre).
  - **Geri alma penceresi**, Astra'nın "yayıncının ağzından yanlış cevap" eleştirisine doğrudan cevap.
  - **Klip linki**, makbuzu "metin" olmaktan çıkarıp "izlenebilir an" yapıyor.
- **İlginç bir detay:** Yarışmanın resmi eşitlik kuralı önce Innovation'a bakıyor. Checkpoint (3,7) bu kurala göre VAR'ın (3,0) önüne geçerdi. Bu sadece bilgi; bizim kayıtlı kurallarımız bu eşitliği bozamadı.
- **Bunu seçersen:** Yedek planı (B) karta düzgünce yazmak gerekir. Ayrıca videoda "Meld'den farkı ne?" sorusunun ilk 20 saniyede cevaplanması şart.

---

## 6.3 VAR — 15,0 puan, risk Orta

### Ne?
Futboldaki VAR'ın Twitch versiyonu. Chat yayıncının bir iddiasına itiraz edince iki izleyicinin `!var` yazması yeterli: "VAR CHECK" sireni çalar, ağır çekim tekrar oynar, chat 15 saniye oy verir (jüri), "NO BASKET" gibi bir karar damgası basılır ve başlıklı bir klip oluşur.

### Somut örnek
> Kâğıt topu çöp kutusuna atıyorsun ve "IN!" diyorsun. Chat'te iki kişi `!var` yazıyor. Siren çalıyor, ekran "VAR CHECK" oluyor. Son 10 saniye tekrar oynuyor, son 4 saniyesi yarı hızda: top çemberden sekip dışarı düşüyor. Chat 15 saniye `!yes`/`!no` oyluyor, oy verenlerin isimleri jüri sırasında görünüyor. **"NO BASKET"** damgası iniyor. Chat'e "VAR: NO BASKET" başlıklı klibin linki düşüyor.

### Nasıl çalışır (adım adım)
1. Yayıncı bir iddiada bulunur ("IN!").
2. 30 saniye içinde 2 farklı izleyici `!var` yazar. Eşik aktif izleyici sayısına göre büyür; mod ya da yayıncı da VAR çağırabilir.
3. **VAR beklemede (12 saatlik ekleme):** Eşik dolunca replay buffer hemen dosyaya kaydedilir, ama tekrar hemen oynamaz. Ekranın köşesinde "🟨 VAR PENDING (2 calls)" çıkar. Yayıncı uygun bir anda tuşa basar ve inceleme başlar. "Auto" modunda eskisi gibi hemen başlar.
4. "VAR CHECK" geçiş animasyonu oynar. Bir OBS Media Source kaydedilen dosyadan son yaklaşık 10 saniyeyi, gecikme payı kadar geri kaydırarak oynatır; son 4 saniye yarı hızdadır.
5. **Telestrator (12 saatlik ekleme):** Ağır çekimin sonunda kare donar. Mod ya da yayıncı dock'ta fareyle çizgi ya da daire çizer ("top çizginin dışında"). Çizim yayında, donmuş karenin üstünde görünür.
6. Chat 15 saniye `!yes`/`!no` oylar; isimler jüri sırasına dizilir.
7. Karar damgası donmuş karenin üstüne basılır. Uygulama 60 saniyelik "VAR: NO BASKET" klibini ve bir marker oluşturur. Klip incelemeyi, inceleme de tekrar görüntüsünü içerir.
8. **Hakem itibarı (12 saatlik ekleme):** Çağrısı haklı çıkan (karar değişen) ve jüride çoğunlukla oy veren izleyiciler puan kazanır. Yayın sonunda "Referee of the night" anılır. Puanlar yayınlar arasında saklanır.

**Self-VAR:** Yayıncı kendi iddiasına VAR çağırır ("mükemmel bir daire çizebilirim"), chat de iddiayı reddedebilir. Her yayında tekrarlanabilecek bir şaka.

### 3 dakikalık video akışı
| Zaman | Ne oluyor |
| --- | --- |
| 0:00 | Hook: kâğıt top, "IN!", iki `!var`, siren, ağır çekim, donmuş karede çizilen daire, jüri, "NO BASKET". |
| 0:25 | Klip linki chat'e düşer, klipten 5 saniye. |
| 0:40 | VAR beklemede: yayıncı bir işin ortasında, "🟨 VAR PENDING" köşede bekliyor; yayıncı işi bitirip tuşa basıyor. |
| 1:00 | Self-VAR: "mükemmel daire çizerim", chat reddeder. |
| 1:35 | Gecikme payının tekrarı doğru ana nasıl oturttuğu; geri itme kısayolu. Yayın sonu: "Referee of the night". |
| 2:10 | Codex artifact, kapanış. |

### Teknik detay
- **Mimari:**
  - **Kayıt:** `SaveReplayBuffer` gönderilir, `ReplayBufferSaved` olayı dosya yolunu verir.
  - **Oynatma:** Media Source'un dosyası `SetInputSettings` ile değiştirilir, `SetMediaInputCursor` ile "son 10 saniye + gecikme payı" noktasına gidilir.
  - **Ağır çekim:** Media Source'un `speed_percent` ayarıyla yapılır. Oynatma sırasında hız değişimi sorun çıkarırsa B yolu: ffmpeg ile son 4 saniyeyi önceden yarı hıza çevirmek (NVENC ile yaklaşık 1 saniye). Bu da T2'de doğrulanacak.
  - **Gecikme payı:** İzleyici yayını 2–5 saniye geriden görür ve `!var` yazması biraz zaman alır. Kayıt ise yerel, gerçek zamanlı. Bu yüzden tekrar, "şu an eksi gecikme" noktasından başlamalı; tutturamazsa "geri it" kısayolu var.
  - **Oylama:** 15 saniyelik pencerede her izleyicinin yalnızca bir oyu sayılır.
  - **Klip:** Karardan hemen sonra `Create Clip` çağrılır. Klip penceresi yaklaşık 85 saniye geriye uzandığı için inceleme klibin içinde kalır.
  - **VAR beklemede:** Eşik dolunca `SaveReplayBuffer` hemen gönderilir, yani bekleme süresi replay buffer'ın 60 saniyesiyle sınırlı değil; dosya diskte durur. Bekleme 2 dakikayı geçerse uyarı çıkar, 5 dakikada çağrı düşer.
  - **Telestrator:** Dock'taki canvas'ta çizilen noktalar WebSocket ile overlay'deki bir canvas'a gider; overlay, Media Source'un üstünde durur. Kare dondurmak için `TriggerMediaInputAction` ile pause.
  - **Hakem itibarı:** SQLite; çağıran, oy veren, karar ve karar değişip değişmediği saklanır.
- **Twitch:** EventSub chat, Create Clip, Create Stream Marker, Send Chat Message; OBS replay buffer ve Media Source.
- **Saatler:**

| Parça | Saat |
| --- | --- |
| Replay kaydetme + Media Source oynatma | 2 |
| Gecikme payı + kısayol | 1 |
| Çağrı ve oylama mantığı | 1 |
| Overlay: geçiş, jüri sırası, damga | 2,5 |
| Klip + marker | 0,5 |
| Cila | 1,5 |
| *Eski MVP toplamı* | *8,5* |
| **+ VAR beklemede:** pending rozeti, "review now" tuşu, auto modu | 1 |
| **+ Telestrator:** dock canvas, overlay canvas, kare dondurma | 1,5 |
| **+ Hakem itibarı:** puan mantığı, SQLite, yayın sonu kartı | 1 |
| **Yeni MVP toplamı** | **12** |
| Bilerek alınmayanlar: ikinci kamera açısı (replay buffer sadece program çıktısını kaydediyor; ayrı kayıt ve telefon kamerası kurulumu gerekir, 1 saat iyimser); yayın sonu VAR derlemesi (bütçe kalırsa ilk aday); karar geçmişi şeridi 0,5 | — |

- **Codex artifact:** Tekrar pipeline'ı (buffer → Media Source → ağır çekim) ve simülatörle yapılan eşik ve oylama zamanlaması testleri.
- **Demo oyunu (isteğe bağlı):** Codex ile "çizgiye değdi mi?" türünden kıl payı anlar üreten küçük bir oyun (yaklaşık 1 saat, tampondan). Kâğıt top gibi masa düelloları için gerekmez.

### Rakipler ve fark
| Rakip | Ne yapıyor | Yaygın mı |
| --- | --- | --- |
| tomaae OBS instant replay | Chat komutuyla tekrar | Evet (12,6 bin indirme; son güncelleme 2019) |
| Streamer.bot replay buffer aksiyonları | Her tetikleyiciyle tekrar | Evet |
| Twitch'in kendi anketleri | Süreli oylama | Evet |
| Glitch Studios Instant Replay | Mod tetikli, markalı, 0,5× ağır çekim; oylama yok | Hayır |
| BarRaider OBS Tools, Fyre Instant Replay | `!replay` + klip | Hayır |
| Streamer's Court (Steam oyunu) | Chat suçlu/suçsuz oyluyor; tekrar yok | Hayır |

**Fark:** Tekrar ve oylama ayrı ayrı mevcut. Bulunamayan şey: eşik → tekrar → süreli jüri → karar → başlıklı klip zincirinin **tek bir ritüel** olması. Astra ve Grok farkın "kısmen" var olduğunu, Claude "var" olduğunu söylüyor.

### Talep ve karşı sinyaller
- **Dolaylı talep:** chat ile tetiklenen bir tekrar script'inin 12,6 bin indirmesi var (2019'dan kalma). Bir yayıncı, anları kaydedip raundlar arasında tekrar göstermenin yolunu soruyor (doğrulanmadı).
- **Chat jürisi ya da VAR incelemesi için doğrudan talep bulunamadı.**
- **Karşı sinyal:** Tekrar isteyen yayıncı, tekrarın **ne zaman** oynayacağını kendisi belirlemek istiyordu. Otomatik bir durdurma bunun tersi.

### Kitle
İtiraz edilebilir, gözle görülür sonuçlar: rekabetçi oyunlar (izlenmenin büyük kısmı), spor tarzı IRL meydan okumalar, masa düelloları. Konuşma tanıma gerektirmediği için aksan riski yok.

### Riskler ve test
| Risk | Önlem |
| --- | --- |
| Replay buffer ve Media Source ağır çekimi | **T2:** komuttan sonra en fazla 5 saniyede tekrar ekranda. |
| Tekrar yanlış ana denk gelir | Gecikme payı + geri itme kısayolu. |
| 60 saniyelik klip asıl anı dışarıda bırakabilir | İnceleme içindeki tekrar yine de anı gösteriyor. T5: klibin içeriği doğrulanacak. |
| Yayını kesintiye uğratır | VAR beklemede: tekrarın ne zaman oynayacağına yayıncı karar veriyor. Self-VAR ve eşik de kontrolü yayıncıda tutuyor. |
| **Yedek plan** | Gerekmiyor; en kötü durumda tekrar ağır çekimsiz oynar. |

### Puanlar ve modellerin söyledikleri
| | Innovation | Impact | Tech | Design | Toplam | Risk | Sıra |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Grok | 3 | 3 | 4 | 5 | 15 | Orta | 3 |
| Astra | 3 | 3 | 4 | 5 | 15 | Orta | 4 |
| Claude | 3 | 3 | 4 | 5 | 15 | Orta | 3 |
| **Ortalama** | **3,0** | **3,0** | **4,0** | **5,0** | **15,0** | | |

- **Tamamen oybirliğiyle puanlanan tek proje.**
- **Grok:** "Setteki en yayın-gibi (broadcast-like) video." Zayıflık olarak otomatik durdurmayı görüyor: tekrarın ne zaman oynayacağını kontrol etmek isteyen yayıncıya ters düşüyor.
- **Astra:** T5'te klibin incelemeyi gerçekten içerdiği gösterilmeli; klip penceresi belgelenmemiş. "Teknik demo başarılı olsa bile yayıncıların chat'in oyunu kesmesini istediği kanıtlanmış olmuyor."
- **Claude:** "Jüri bunu yeni bir fikir yerine cila olarak okuyabilir."

### Benim görüşüm
- **Avantajlar:**
  - **En sağlam yedek.** Konuşma tanıma yok, aksan riski yok, setin en esnek bütçesi.
  - Herkes VAR'ı bildiği için açıklamaya gerek kalmıyor; ilk 10 saniyede anlaşılıyor.
- **Dezavantajlar:**
  - Innovation tavanı 3. Jüri "tekrar + anket, güzel paketlenmiş" diyebilir.
  - OBS ve Twitch tarafında senin daha az deneyimli olduğun işler var (Media Source, gecikme payı). Ama bunlar iyi belgelenmiş API'ler.
- **12 saatlik eklemeler neyi değiştiriyor:**
  - **VAR beklemede**, Grok'un ve kanıt dosyasının en büyük karşı sinyaline cevap: tekrar isteyen yayıncı, tekrarın ne zaman oynayacağını kendisi seçmek istiyordu.
  - **Telestrator**, Design'ı güçlendirir: spor yayınlarından tanıdık "çizgiyi çizen hakem" karesi, videonun en akılda kalan anı olabilir.
  - **Hakem itibarı**, Impact'e katkı: jüriye katılmanın bir anlamı olur, haftalık kullanım artar.
  - Innovation tavanı büyük ihtimalle yine 3. Eklemeler ritüeli zenginleştiriyor ama "tekrar + oylama" çekirdeğini değiştirmiyor.
- **Bunu seçersen:** Ritüeli olabildiğince teatral yap; stinger, ses efekti ve damga animasyonu Design puanını taşır. Self-VAR da "sadece spor için" algısını kırar.

---

## 6.4 Tap on the Shoulder — 14,3 puan, risk Orta

### Ne?
Yayıncı işe ya da tam ekran bir oyuna gömülmüşken chat ona dokunamaz. Bu araçla dokunabilir: izleyici şikâyetleri ("ses uzak geliyor") ve mod uyarıları masadaki bir telefonda **alarm veren bir yüze** dönüşür. Yayıncı sorunu düzeltince chat de "düzeldi" diye onaylar.

### Somut örnek
> Mikrofonun kapalı kaldı. OBS bunu görüyor; masadaki telefon yüzü panikliyor: **"MIC MUTED"**. Açıyorsun. Ama sonra mikrofonu yanlışlıkla çevirdin; OBS bunu göremez. Chat'te 2 kişi "you sound far away" yazıyor ve telefon yüzü **"FAR AWAY"** gösteriyor. Düzeltip kısayola basıyorsun. Bot soruyor: "Fix #2: sound right now? 👍/👎". İki 👍 geliyor; ilk bildiren kişi ekranda anılıyor.

### Nasıl çalışır (adım adım)
1. **Girdiler:**
   - 60 saniye içinde en az 2 farklı izleyici mic, audio, "far away", black screen ya da frozen gibi bir şey yazar, ya da biri `!mic` yazar;
   - mod özel telefon sayfasından hazır bir uyarıya dokunur ("game too loud" vb.);
   - obs-websocket mikrofonun kapalı olduğunu ya da N saniyedir sessiz olduğunu bildirir. Bunlar iki ayrı sinyal.
2. Kadrajdaki telefon yüzü alarm verir ve sorunu büyük harflerle yazar. Sadece yayıncının kulaklığında bir ses çalar. Chat ve OBS aynı şeyi söylüyorsa yüz bunu belirtir: "chat + OBS: mic muted".
3. Yayıncı sorunu düzeltip "fixed" tuşuna basar.
4. Bot 👍/👎 sorar. Düzeltme anı artı tahmini yayın gecikmesinden önce gelen cevaplar sayılmaz. Gecikme her izleyicide farklı olduğu için sonuç "herkes duydu" değil, "chat onayladı" diye yazılır.
5. Sorun kapanır ve ilk bildiren kişi anılır.
6. **Sakin mod (12 saatlik ekleme, eskiden stretch):** Sorun yokken yüz chat durumunu gösterir: ilk kez yazan biri el sallar, bekleyen bir soru varsa yüz el kaldırır, chat sessizken uyuklar.
7. **Soundcheck (12 saatlik ekleme):** Yayıncı yayın başında "soundcheck" tuşuna basar. Telefon yüzü "SOUNDCHECK A" gösterir, yayıncı konuşur. Bot chat'e sorar: *"Test A: mic vs game? !heard good / quiet / loud"*. Aynı anda mikrofon ve oyun seviyeleri ölçülür. Yüz ikisini birlikte gösterir: "chat: quiet · meter: −28 dB → raise mic".
8. **Siyah ya da donmuş ekran (12 saatlik ekleme):** Yayın görüntüsü kararırsa "BLACK SCREEN", 10 saniye hiç değişmezse "FROZEN?" uyarısı çıkar. Chat'te de aynı şikâyet varsa "chat + OBS" olarak gösterilir.
9. **Sorun raporu (12 saatlik ekleme):** Yayın sonunda dock'ta ve chat'te: "3 issues · avg fix 42 s · first reporter: @ana".

### Teknik detay
- **Telefon yüzü:** HTTPS üzerinde bir web sayfası. Ekranın kapanmaması için Wake Lock API kullanılıyor ve bu API HTTPS istiyor; bu yüzden tünel ya da yerel sertifika (mkcert) gerekiyor. Eşleştirme QR kodla yapılır.
- **Kulaklık sesi:** Sadece yayıncı duymalı, yayına çıkmamalı. OBS'te "monitor only" ses ya da ayrı bir çıkış cihazıyla yapılır.
- **Sessizlik algılama:** obs-websocket `InputMuteStateChanged` olayı ve `InputVolumeMeters` (50 ms'de bir gelir) ile eşik.
- **Soundcheck:** Aynı `InputVolumeMeters` verisinden mikrofon ve oyun kaynağının birkaç saniyelik ortalama seviyesi; chat cevapları 30 saniyelik pencerede sayılır.
- **Siyah/donmuş ekran:** `GetSourceScreenshot` saniyede 1 kez küçük bir kare (ör. 64×36) alır. Ortalama parlaklık eşiğin altındaysa siyah; 10 saniye boyunca kareler arası fark sıfıra yakınsa donmuş. Statik bir "BRB" sahnesi yanlış alarm vermesin diye sadece oyun/kamera sahnelerinde çalışır.
- **Video sahnesi (3 dk):** 0:00 hook: OBS mute → telefon yüzü panik; 0:20 "far away" chat şikâyeti → yüz; 0:45 düzeltme ve chat onayı; 1:05 yayın başı soundcheck; 1:30 donmuş ekran "chat + OBS"; 1:50 sakin mod ve yayın sonu raporu; 2:15 Codex artifact.
- **Saatler:**

| Parça | Saat |
| --- | --- |
| Şikâyet dedektörü | 1 |
| Mod uyarı sayfası + Twitch girişi | 1,5 |
| Telefon yüzü sayfası + HTTPS eşleştirme | 2,5 |
| obs-websocket mute/sessizlik kontrolü | 1 |
| Onay döngüsü + dock | 1,5 |
| Anma overlay'i | 0,5 |
| Cila | 1 |
| *Eski MVP toplamı* | *9* |
| **+ Sakin mod** (eski stretch) | 1 |
| **+ Soundcheck:** seviye ölçümü, chat sorusu, yüz ekranı | 1 |
| **+ Siyah/donmuş ekran algılama** | 0,5 |
| **+ Yayın sonu sorun raporu** | 0,5 |
| **Yeni MVP toplamı** | **12** |

- **Codex artifact:** Telefon yüzü sayfası ve chat simülatörüyle gürültülü chat senaryoları üzerinde çalışan dedektör test seti.

### Rakipler ve fark
- **Yaygın OBS eklentileri:** Muted Notification (12,4 bin indirme: kapalı mikrofona konuşunca uyarı), Remember to Talk (2,4 bin: mikrofon uzun süre sessiz kalınca uyarı).
- **Diğerleri:** Twitch Guardian (chat'te anahtar kelime çıkınca masaüstü uyarısı), Elgato Prompter chat modu, Mochi ve WooferBot maskotları.
- **Fark:** İnsan yargısı (izleyici şikâyeti, mod uyarısı) OBS'in sinyaliyle karşılaştırılıyor, odadaki fiziksel bir sinyale dönüşüyor ve chat'in onayıyla kapanıyor. "Ses uzak geliyor" gibi durumları hiçbir OBS eklentisi göremez.

### Talep ve karşı sinyaller
- **Problem güçlü kanıtlı:**
  - Snoop Dogg bir saatten uzun süre sessiz yayın yaptı; chat sadece emote moduna alındığı için ona söyleyemedi (Kotaku 2021, doğrulandı).
  - OBS forumunda bir istek: "yayıncılar mikrofonu kapattıklarını sık sık unutuyor" (2018, doğrulandı).
- **Karşı sinyaller:**
  - "Kendi mikrofonunu OBS'te izle" tavsiyesi.
  - DrDisrespect yaklaşık 10 dakika sessiz kaldı ve izleyiciler ona söyleyebildi (doğrulandı).
  - Gerçek arızalar seyrek, yani araç çoğu zaman boşta bekler.

### Puanlar ve modellerin söyledikleri
| | Innovation | Impact | Tech | Design | Toplam | Risk | Sıra |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Grok | 3 | 4 | 4 | 4 | 15 | Orta | **2** |
| Astra | 3 | 4 | 4 | 4 | 15 | Orta | 5 |
| Claude | 3 | 3 | 3 | 4 | 13 | Düşük | 5 |
| **Ortalama** | **3,0** | **3,7** | **3,7** | **4,0** | **14,3** | | |

- **Grok onu 2. sıraya koydu:** Problem belgelenmiş, demo için bir mikrofon, yedek bir telefon ve 3 hesap yetiyor.
- **Astra:** Puanları Grok ile aynı ama sırası 5: "Daha az ayırt edici ve teatral." Günlük kullanım için en güçlü argüman olan sakin mod MVP'nin dışında.
- **Claude:** Impact 3: arızalar seyrek ve yaygın eklentiler mute durumunu zaten kapsıyor. Tech 3: daha çok entegrasyon işi.

### Benim görüşüm
- **Avantajlar:** Faydalı ve somut bir problem. Telefon yüzü kadrajda hoş bir fiziksel öğe.
- **Dezavantajlar:**
  - Kriterlere tek tek bakınca sağlam görünüyor ama iki model onu 5. sıraya koydu. Bunu "akılda kalmaz" diye okuyorum.
  - Demo, yapay bir arızayı sahnelemeyi gerektiriyor.
  - Telefon ve HTTPS kurulumu ayrıca uğraştırıyor.
- **12 saatlik eklemeler neyi değiştiriyor:**
  - **Sakin mod**, Astra'nın "günlük kullanım argümanı MVP dışında" eleştirisini kapatıyor.
  - **Soundcheck**, aracın arıza beklemeden her yayının ilk dakikasında çalışmasını sağlıyor. Bu, "gerçek arızalar seyrek" karşı sinyaline en iyi cevap.
  - **Siyah/donmuş ekran**, "OBS sinyali" tarafını sesten görüntüye genişletiyor.
  - **Dürüst not:** Bunlar Impact'i güçlendiriyor ama Innovation'ı (3,0) pek değiştirmiyor. "Akılda kalmaz" sorunu sürüyor.
- **Bunu seçersen:** Telefon yüzünün tasarımına (ifadeler, animasyonlar) ekstra özen göster; videoda akılda kalan tek görsel o.

---

## 7. Karşılaştırma matrisi

| | Minefield | Checkpoint | VAR | Tap |
| --- | --- | --- | --- | --- |
| **Toplam (ort., eski kartlara göre)** | **16,3** | 15,0 | 15,0 | 14,3 |
| Innovation | **5,0** (gerçekçi: 4) | 3,7 | 3,0 | 3,0 |
| Impact | 3,0 | **4,0** | 3,0 | 3,7 |
| Tech | 3,3 | 3,3 | **4,0** | 3,7 |
| Design | **5,0** | 4,0 | **5,0** | 4,0 |
| Risk (medyan) | Yüksek | Orta | Orta | Orta |
| Eklemelerin büyük ihtimalle yaradığı kriter | Innovation (tarama), Tech/Design (fitil), Impact (tablo) | Impact + Innovation (SSS), risk (geri alma) | Design (telestrator), Impact (beklemede, itibar) | Impact (sakin mod, soundcheck) |
| Konuşma tanıma gerekli mi | Evet (kelime) | Evet (cümle) | Hayır | Hayır |
| Aksan riski | Var | Var (daha az) | Yok | Yok |
| Yedek planı var mı | **Yok** (fitil yumuşatır) | Var (yeniliği düşürür) | Gerek yok | Gerek yok |
| İlk 20 saniyedeki "vay" etkisi | **Patlama** | Kelimeler karta yazılıyor + alıntı | **Siren + ağır çekim + çizim + damga** | Telefon yüzü paniği |
| 3 hesapla gerçekçi demo | Evet (arkadaşla daha iyi) | Evet | Evet | Evet |
| MVP saati | 12 | 12 | 12 | 12 (+ telefon kurulumu) |
| Senin ML uzmanlığına uyum | **Yüksek** | **Yüksek** | Düşük | Düşük (sinyal eşikleri biraz) |
| Ekstra telefon | 1–2 arkadaş | — | — | **1 telefon** |
| Kitle | Konuşan her yayın (Just Chatting %14,2) | Odak yayınları (art, maker, kod) | Rekabetçi oyun, meydan okuma | Mikrofonlu her yayın |
| Kullanım sıklığı | Her yayın (arka planda) | Her yayın | Tartışmalı anlarda | Her yayın başı (soundcheck) + arıza olunca |
| 1. gün testleri | T1, T4 | T1b | T2 | T2, T4 |

---

## 8. Kararsız kalırsan: ikili karşılaştırmalar

### Minefield mi VAR mı?
Bu, "yüksek tavan" ile "sağlam taban" arasındaki seçim.

| | Minefield | VAR |
| --- | --- | --- |
| En iyi senaryo | Jüri "bunu hiç görmemiştim" der; Innovation 4–5 ve eşitlik bozmada da avantaj. | Jüri "çok eğlenceli, çok iyi paketlenmiş" der; telestrator karesi akılda kalır. |
| En kötü senaryo | T1 başarısız, proje çöker; ya da jüri "Don't Get Got'un Twitch hâli" der. | Jüri "tekrar + anket" deyip Innovation'a 2–3 verir. |
| Belirsizlik | Yüksek, ama **1. gün testiyle 2 saatte büyük kısmı çözülür.** | Düşük. |

**Karar kuralım:** T1'i koş. Geçerse Minefield, geçmezse VAR. Bu ikisini yarıştırmak yerine test sonucunun seçmesine izin vermek mantıklı.

### Minefield mi Checkpoint mi?
- İkisi de STT kullanıyor ve aynı testte (T1 + T1b) ölçülüyor.
- **Minefield** daha eğlenceli ve daha yeni. **Checkpoint** daha faydalı (Impact 4), SSS ile daha da faydalı.
- Jüri videoya baktığı için ilk 20 saniyede patlama, alt yazının karta yazılmasını büyük ihtimalle yener.
- **İkisi de geçerse ben Minefield derim.** Sadece T1b geçerse Checkpoint masaya gelir.

### Checkpoint mi VAR mı? (puan eşitliği)
- Bizim kayıtlı kurallarımız bu eşitliği bozamadı.
- Yarışmanın resmi kuralı uygulansaydı (önce Innovation) Checkpoint öne geçerdi (3,7'ye karşı 3,0).
- Ama Checkpoint'in puanı kısmen Claude puanlayıcısına dayanıyor; Grok ve Astra'nın ortalamasında Checkpoint 14,5, VAR 15.
- **Eklemelerden sonra:** SSS, Checkpoint'in Impact ve Innovation tarafını güçlendiriyor; telestrator VAR'ın Design tarafını güçlendiriyor. Yani ikisi de kendi güçlü yanını büyüttü, eşitlik büyük ihtimalle sürüyor.
- **Faydayı mı, izlenebilirliği mi daha çok önemsiyorsun?** Fayda için Checkpoint, izlenebilirlik için VAR.
- Ben hâlâ VAR'a yatkınım: riski daha düşük, videosu daha teatral ve puanı tartışmasız. Ama SSS ile fark eskisinden küçük.

### VAR mı Tap mı? (STT gerektirmeyen iki seçenek)
- **VAR:** Daha izlenesi (Design 5) ve teknik olarak daha ilginç (Tech 4). Ekstra cihaz yok.
- **Tap:** Daha faydalı (Impact 3,7) ve soundcheck ile her yayında kullanılır. Ama iki puanlayıcı onu 5. sıraya koydu; yedek telefon ve HTTPS kurulumu ek iş.
- Bence VAR, çünkü jüri videoya bakıyor ve "Design + Tech" toplamı daha yüksek. Tap'i ancak T2'de VAR'ın replay tarafı çalışmazsa öne alırdım.

---

## 9. 1. gün testleri ve karar ağacı

### Hangi test, ne kadar sürer, neyi ölçer
| Test | Proje | Ne ölçer | Geçme şartı | Tahmini süre |
| --- | --- | --- | --- | --- |
| **T1** | Minefield | Doğal İngilizce konuşmada kelime yakalama | ≥%80 yakalama, 10 dakikada ≤1 yanlış alarm, ≤3 saniye gecikme, kare düşmesi yok | ~1–1,5 saat |
| **T1b** | Checkpoint | Sesli cevabın yazıya dökülmesi | 10 cevabın en az 9'u okunur, alıntı ≤2 saniyede hazır | T1 ile aynı oturumda ~30 dk |
| **T2** | VAR, Tap | obs-websocket ile replay kaydı ve Media Source ağır çekimi; Tap için mute/sessizlik olayı ve `GetSourceScreenshot` | Tekrar ≤5 saniyede ekranda, mute olayı geliyor, ekran görüntüsü alınabiliyor | ~1–1,5 saat |
| **T4** | Minefield, Tap | Herkese açık URL arkasında Twitch girişli sayfa; Tap için telefonda HTTPS + Wake Lock (ekran kapanmıyor) | Tek yol uçtan uca çalışıyor | ~1 saat |
| **T5** | Hepsi | API kontrolleri: başlıklı klip, marker, threaded reply | Yeni kanalımızda hepsi başarılı | ~30 dk |

T2 ve T4, VAR ile Tap'i aynı oturumda test ettiği için 4. finalist 1. güne çok az ek iş getiriyor. Toplam yaklaşık 4–5 saat.

### T1 nasıl yapılmalı (somut)
1. Windows'ta Python + CUDA ile faster-whisper kur (`small.en` ile başla, sonra `medium.en` dene).
2. 10 kelimelik bir mayın listesi hazırla. Kelimeleri **bir arkadaşın** seçsin ki sen bilmeyesin.
3. **10 dakika doğal İngilizce konuş:** OBS açık, yayın test modunda. Arkadaş kelimeleri sohbete sokmaya çalışsın.
4. Ölç:
   - Kaç kelime yakalandı (hit)?
   - Kaç tanesi söylenmediği halde yakalandı (yanlış alarm)?
   - Söyleyişten tetiklenmeye kaç saniye geçti (gecikme)?
   - OBS kare düşürdü mü?
   - **Her yakalamanın güven skoru** (fitil eşiği bununla ayarlanacak): yanlış alarmların skorları doğru yakalamalarınkinden ayrışıyor mu?
5. Aynı oturumda T1b: 10 senaryolu cevabı oku. Her biri için alıntının hazır olma süresini ve düzeltmesiz okunur olup olmadığını ölç.

### Karar ağacı (önerim)
```
T1 geçti mi? ──Evet──► MINEFIELD
     │
    Hayır
     │
T1b geçti mi? ──Evet──► CHECKPOINT ya da VAR (sen seçersin; ben VAR'a hafif yatkınım)
     │
    Hayır
     │
T2 (replay) geçti mi? ──Evet──► VAR
     │
    Hayır
     │
     ▼
    TAP  (T2'nin mute/sessizlik kısmı ve T4'ün telefon kısmı geçtiyse)
```
T1 "sınırda" çıkarsa (ör. %75 yakalama ama yanlış alarmların güven skoru düşük): fitil yanlış alarmları gerilime çevirebilir. Bu durumda Minefield'ı elemeden önce birlikte bakalım.

---

## 10. Zaman çizelgesi

| Tarih | Ne |
| --- | --- |
| **28 Ekim (bugün)** | Finalistler seçildi (4 proje), MVP bütçesi 12 saat. |
| **29 Ekim** | 1. gün testleri: T1 + T1b, T2, T4, T5 (~4–5 saat). Akşam final seçimi. Twitch hesapları ve ayarları (VOD açık, bot mod). |
| **30 Ekim – 1 Kasım** | Yaklaşık 17,5 saat geliştirme: önce 3,5 saat ortak altyapı, sonra 12 saatlik MVP, en az 2 saat tampon. Günde yaklaşık 6 saat. |
| **1–2 Kasım** | Video çekimi (arkadaşlarla), montaj (<3 dk), YouTube'a yükleme, repo README, Devpost açıklaması. |
| **2 Kasım 14:00 PT** | **Son teslim** (Türkiye saatiyle 3 Kasım 01:00; ABD 1 Kasım’da kış saatine geçiyor, yani PST = UTC−8). |

**Dikkat:** Video çekimi ve montaj 17,5 saatin içinde değil. Toplam bütçen 20–25 saatse video için 2,5–7,5 saat kalıyor; alt uçta bu dar. Tampon saatleri video için de kullanılabilir.

---

## 11. Önceki araştırmalardan önemli bulgular

### Pazar (stream-types araştırması, Ekim 2026)
- **Just Chatting açık ara en büyük kategori:** ortalama izleyicinin %14,19'u (303 bin), 30 günde 201 milyon saat. Konuşan yayıncıyı hedefleyen Minefield bu yüzden geniş kitleli.
- **IRL** 2025'te +%186 büyüdü, 2026'da dalgalı.
- **Büyüyen formatlar:** indie oyunlar +%51, Drops +%46, korku +%6. Bunlar VAR'ın oyun tarafı için iyi.
- **Twitch küçülüyor** (2026 Q2'de saatler -%8,3), Kick büyüyor (+%36,7).
- **Küçük yayıncılar:** kanalların yaklaşık %61'i ortalama 10 izleyicinin altında (snippet, doğrulanmadı). Art kategorisinde kanal başına yaklaşık 17 izleyici var; Checkpoint'in hedefi tam bu.

### Daha önce kazanmış ya da benzer hackathon projeleri
| Proje | Yarışma | Bize anlamı |
| --- | --- | --- |
| **OK Gamers** | TwitchCon Hackathon 2019, **büyük ödül** | STT + chat, jüriyi daha önce etkilemiş. Minefield'ın atası sayılabilir; fark mutlaka gösterilmeli. |

### Kanıt yöntemi hakkında
- Üç bağımsız araştırmacı (Astra, Grok, Claude) kullanıldı; bir Sonnet ajanı da linkleri tek tek açıp kontrol etti.
- Devpost sayfaları bot korumasıyla açılmadı. PROVE IT (VAR'a benzer), Raid Train ve Twitch Sense kurala göre kanıttan düşürüldü. Bu, onların var olmadığı anlamına gelmiyor. **PROVE IT linkini elle açıp bakmanı öneririm**, çünkü VAR seçilirse önemli.
- Checkpoint'in pivot sonrası kanıtı tek kaynaklı (P).

### Puanlama yöntemi hakkında
- Üç model (Grok, Astra, Claude Opus) kartları ve kanıtları gördü. Kartların kendini savunduğu "Strengthening" bölümlerini görmediler.
- Her model kartları farklı sırayla gördü ve web araması yapmadı.
- **Hiçbir kriterde modeller arasında 2 puanlık fark çıkmadı;** görüş birliği çok yüksek.
- Toplam senin kararınla ortalama ile hesaplandı; medyan ile tek fark, Hint Jar ve Tap'in yer değiştirmesi.
- **12 saatlik eklemeler puanlanmadı.** Puanlar eski kartlara göre.

### Fikirler nereden çıktı
Wave 2'de beş kaynak aynı brief'le toplam 101 fikir üretti: L1 (Claude Opus, ihtiyaç odaklı), L2 (Claude Opus, gösteri odaklı), L3 (Claude Opus, yetenek odaklı), G (GPT 6 Astra, serbest), X (Grok, X'e dayalı).

| Finalist | Ana kaynak | Bağımsız benzerini bulan |
| --- | --- | --- |
| Minefield | L2-1 | Yok, tek kaynak |
| Checkpoint | L1-1; bugünkü sesli cevap hâli step 6'daki pivot (Claude yazdı, sen onayladın) | G-18 (Astra), varyant |
| VAR | L2-11 | Yok, tek kaynak |
| Tap on the Shoulder | L1-4 | G-2 Soundcheck Relay (Astra), o da tam kart; soundcheck eklemesi buradan geliyor |

Dört finalistin de ana kaynağı Claude. Claude puanlayıcısı bu yüzden kendi fikirlerini puanlamış oldu; Grok ve Astra'nın ortalamasına bakınca sıralama büyük ölçüde aynı kalıyor, en çok etkilenen Checkpoint.

---

## 12. Finale alınmayan ve elenen projeler

**Finale alınmayanlar (28 Ekim, senin kararın; puanlandılar ama finale girmediler):**

| Proje | Ne idi | Puan, risk | Neden geride kaldı |
| --- | --- | --- | --- |
| Hint Jar | İlk kez oynanan oyunlarda izleyiciler ipucunu chat'e yazmak yerine kademeli bir kavanoza mühürler; yayıncı istediği seviyeyi açar. | 14,7, Düşük | En düşük riskli proje, ama kitlesi dar ve teknik olarak sıradan. Kanıt dosyası, backseating'in kurallar ve banlarla zaten çözüldüğünü söylüyor. |
| Studio Audience | Chat tepkileri isimli kahkahalara dönüşür; tepki veren kişi sayısı arttıkça kalabalık büyür. | 13,0, Düşük | Kalabalığın büyümesi 3 test hesabıyla gösterilemiyor; videoda sadece etiketli simülasyon olurdu. |
| Raid Torch | Raid ile kanaldan kanala taşınan meşale; her chat iz bırakır, izi taşıyanlar yeni kanalda parlar. | 12,3, Yüksek | Topluluk zinciri tek kişiyle gösterilemiyor; ikinci canlı kanal ve gerçek raid gerekiyor; talep bulunamadı. |

Ayrıntıları için: [ranking.md](ranking.md) ve bu dokümanın git geçmişindeki 7 projelik sürüm.

**Kanıt adımında elenenler (senin kararın):**

| Proje | Ne idi | Neden elendi |
| --- | --- | --- |
| Previously On | Raid gelince 10 saniyelik TV tarzı "önceki bölümlerde..." özeti | Twitch 2026'da yayın içi yapay zekâ özetlerini ve Recaps'i çıkardı. |
| Photo Booth | `!snap` ile izleyicinin avatarı yayıncıyla aynı polaroide giriyor | StreamUP Polaroid Picture (yaygın) neredeyse aynı şeyi yapıyor. |
| Foley Pit | Chat ses efekti senaryosu yazıyor, yayıncı masadaki objelerle sesi yapıyor, model puanlıyor | Talep bulunamadı; CLAP skorları insan yargısıyla zayıf örtüşüyor. |

---

## 13. Benim önerim

**Karar şekli:** Sezgiyle değil, 29 Ekim'deki test sonuçlarıyla ([karar ağacı](#karar-ağacı-önerim)).

**Finalistlerin rolleri:**
- **Minefield** kazanma şansı en yüksek proje. ML becerin ve GPU'n burada avantaj; fitil de bu avantajı doğrudan ürüne çeviriyor. Risk bir günde ölçülebiliyor.
- **Checkpoint** aynı testle ölçüldüğü için ek maliyeti çok düşük bir B planı. SSS ile fayda tarafı setin en güçlüsü.
- **VAR** konuşma tanımadan bağımsız, sağlam bir C planı. Telestrator ile videosu daha da yayın gibi.
- **Tap** STT'siz ikinci güvenli seçenek. Ama bence en düşük kazanma şansı onda; ancak VAR'ın replay tarafı T2'de çalışmazsa öne alırdım.

**Final seçilince yapılacaklar:**
- **Minefield:** Yasaklı kelime listesini hazırlamak; arkadaşlarla ekme provası; T1 verisiyle fitil eşiğini ayarlamak; açıklamaya Don't Get Got benzerliğini sahiplenen bir cümle yazmak.
- **Checkpoint:** Yedek planı (B) karta düzgünce yazmak; SSS eşiğini kayıtlı soru çiftleriyle ayarlamak; videonun ilk 20 saniyesinde "Meld'den farkı ne?" sorusunu cevaplamak.
- **VAR:** PROVE IT linkini elle kontrol etmek; stinger, siren ve damga animasyonuna özen göstermek.
- **Tap:** Yedek telefonu ayarlamak (HTTPS, Wake Lock); telefon yüzünün ifadelerine özen göstermek.

**Son not:** Bu dokümanda puanlar ve modellerin söyledikleri ölçülmüş bilgiler. "Benim görüşüm" bölümleri ve 12 saatlik eklemelerin etkisi ise yorum. Karar senin.
