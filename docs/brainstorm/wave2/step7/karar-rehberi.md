# Karar rehberi: 3 finalist ve final seçim

Hazırlanma tarihi 28 Ekim 2026. Aynı gün üç kez güncellendi: önce 4 finaliste, sonra final analize göre 3 finaliste, en son da final karara göre.

> **Final karar (28 Ekim): Minefield.** STT modeli `deepdml/faster-whisper-large-v3-turbo-ct2`. Bu modeli daha önce test ettin, Türkçe ve İngilizcede iyi çalıştı; bu yüzden STT doğruluğu çözülmüş kabul edildi. Bu karara göre yapılan değişiklikler: [6.1, "Karardan sonra değişenler"](#karardan-sonra-değişenler-28-ekim-stt-modeli). VAR ve Checkpoint bölümleri kayıt için duruyor. Yapım ayrıntıları ayrı bir plan dosyasında olacak (`docs/plan/minefield.md`).

**Senin 28 Ekim kararların:**
- **Finalistler:** Minefield, VAR, Checkpoint. Tap on the Shoulder final analizden sonra çıkarıldı; Hint Jar, Studio Audience ve Raid Torch finale alınmamıştı (bkz. [bölüm 12](#12-finale-alınmayan-ve-elenen-projeler)).
- **Kart MVP bütçesi en fazla 12 saat.** Final analizden sonra her projenin MVP'si yaklaşık 11 saate indi. Minefield'ın MVP'si karardan sonra yaklaşık 10,5 saate indi; artan süre tampona ve videoya kaldı. Toplam yapım süresi yaklaşık **17,5 saat**; video bu sürenin dışında.
- **Checkpoint'te SSS** senin kararın; final analizde katmanlı (iki eşikli) hâline getirildi.

**Bu sürümde ne var:** Projeler, step 7 puanlarına ek olarak step 8'deki üç serbest incelemenin (Opus, Grok, Astra) [sentezine](../step8/final-analiz.md) göre son hâllerine getirildi. Her projede **"Önceki plandan ne değişti"** tablosu ve **"Step 8: serbest incelemeler"** bölümü var. Son hâller yeniden puanlanmadı.

Kaynaklar:
- Kartlar: [../step6/cards.md](../step6/cards.md), revizyon 3
- Birleştirilmiş kanıt: [../step6/evidence/aggregate.md](../step6/evidence/aggregate.md)
- Puanlama sonuçları: [ranking.md](ranking.md)
- Üç puanlayıcının ham cevapları: [results-grok.md](results-grok.md), [results-astra.md](results-astra.md), [results-claude.md](results-claude.md)
- Pazar araştırması: [../research/stream-types.md](../research/stream-types.md)
- Serbest incelemeler (step 8): [../step8/review-opus.md](../step8/review-opus.md), [../step8/review-grok.md](../step8/review-grok.md), [../step8/review-astra.md](../step8/review-astra.md)
- Final analiz (sentez): [../step8/final-analiz.md](../step8/final-analiz.md)

Puanlayıcıların söyledikleri ile benim görüşümü ayrı tuttum. Benim görüşüm her bölümde **"Benim görüşüm"** başlığı altında.

---

## İçindekiler

1. [Tek bakışta özet](#1-tek-bakışta-özet)
2. [Yarışma: jüri neye bakıyor](#2-yarışma-jüri-neye-bakıyor)
3. [Twitch sözlüğü: terimler ne demek](#3-twitch-sözlüğü-terimler-ne-demek)
4. [Senin makinen ve telefon/hesap ihtiyacı](#4-senin-makinen-ve-telefonhesap-ihtiyacı)
5. [Ortak altyapı: her projede aynı olan 3,5 saat](#5-ortak-altyapı-her-projede-aynı-olan-35-saat)
6. Finalistler:
   1. [Minefield: seçilen proje](#61-minefield-seçilen-proje)
   2. [VAR: seçilmedi](#62-var-seçilmedi)
   3. [Checkpoint: seçilmedi](#63-checkpoint-seçilmedi)
7. [Karşılaştırma matrisi](#7-karşılaştırma-matrisi)
8. [Kararsız kalırsan: ikili karşılaştırmalar](#8-kararsız-kalırsan-ikili-karşılaştırmalar)
9. [29 Ekim testleri](#9-29-ekim-testleri)
10. [Zaman çizelgesi](#10-zaman-çizelgesi)
11. [Önceki araştırmalardan önemli bulgular](#11-önceki-araştırmalardan-önemli-bulgular)
12. [Finale alınmayan ve elenen projeler](#12-finale-alınmayan-ve-elenen-projeler)
13. [Karar ve sonraki adımlar](#13-karar-ve-sonraki-adımlar)

---

## 1. Tek bakışta özet

| Rol | Proje | Bir cümlede | Step 7 puanı | Step 8 tercihi (Opus / Grok / Astra) | Risk | Ana test | MVP |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Seçildi** | **Minefield** | İzleyiciler gizlice bir desteden "kelime mayını" seçer. Yayıncı o kelimeyi söyleyince ekranda patlar ve ekleyenin adı çıkar. | **16,3** | **1 / 1 / 1** | Orta (karardan sonra) | T0 (eğlence ayarı) + harness ilk koşusu | ~10,5 sa |
| Seçilmedi | **VAR** | Chat bir an'a itiraz edince (`!var`) futboldaki VAR gibi ağır çekim tekrar, 15 saniyelik chat jürisi, karar damgası ve klip gelir. | **15,0** | 3 / 2 / 2 | Orta | T2 (OBS tekrar) | ~11 sa |
| Seçilmedi | **Checkpoint** | Yayıncı işe gömülüyken mesajlar biriktirilir. Molada yayıncı sesli cevap verir, cevap izleyiciye alıntı olarak gider; tekrar eden sorulara bot eski cevabı verir. | **15,0** | 2 / 3 / 3 | Orta | T1b (cevabı yazıya dökme) | ~11 sa |

Step 7 puanı, 4 kriterin (her biri 1–5) üç puanlayıcıya göre ortalamasının toplamıdır; en fazla 20 olabilir. Puanlar eski kartlara göre verildi; son hâller yeniden puanlanmadı.

**Kısaca durum:**
- **Minefield seçildi: en yenilikçi ve en izlenesi proje.** Step 7'de üç model Innovation ve Design'a 5 verdi; step 8'de üçü de "bunu yapardım" dedi. STT modeli senin testinden geçtiği için risk yüksekten ortaya indi. Kalan açık soru eğlence (T0). "Birine kelime söyletme" türü parti oyunlarından biliniyor, bu yüzden gerçekçi Innovation beklentisi 4.
- **VAR en güvenli "izlemesi eğlenceli" seçenek** ve Minefield'la aynı riski (STT) taşımayan tek yedek. Zayıf yanı yenilik: parçaları zaten var.
- **Checkpoint en faydalı proje** (Impact 4/4/4), ama videosu sakin ve farkı ince. Üç model de onu Minefield'ın arkasına koydu.

---

## 2. Yarışma: jüri neye bakıyor

| Konu | Detay |
| --- | --- |
| Son teslim | **2 Kasım 2026, 14:00 PT** (Türkiye saatiyle 3 Kasım 01:00; ABD 1 Kasım’da kış saatine geçiyor, yani PST = UTC−8). `resources.md` kendi içinde çelişiyor, bu yüzden **hedef 2 Kasım 23:00 TSİ**. |
| Jüri dönemi | 5–15 Kasım 2026 |
| Ne teslim ediliyor | Kod reposu ve **3 dakikadan kısa** bir YouTube videosu. Video projenin Twitch'te çalıştığını **ve Codex'i nasıl kullandığını** göstermeli. |
| Jüri ne yapıyor | Kurallara göre jüri projeyi denemek zorunda değil. **Sadece açıklama, görseller ve videoya bakarak puan verebilir.** Yani pratikte video her şey. Değerlendirmede otomatik AI analizi de kullanılabilir (rules §6). |
| Kriterler (eşit ağırlık) | **Innovation/Idea:** ne kadar yaratıcı ve yeni, mevcut şeylerden farkı ne?<br>**Potential Impact:** yayıncılar ve toplulukları için ne kadar faydalı ya da eğlenceli?<br>**Technological Implementation:** teknik uygulama, Codex kullanımı dahil.<br>**Design:** kullanımı kolay mı, izlemesi eğlenceli mi? |
| Finalistler | Toplam puanı en yüksek 5 proje finalist olur. |
| **Resmi eşitlik bozma** | Eşitlikte önce **Innovation** puanına bakılır, sonra sıradaki kriterlere. |
| Birden fazla başvuru | Serbest, ama her başvuru "unique and substantially different" olmalı; ayrı video, repo ve Codex session ID gerekir. 17,5 saatlik yapım süresiyle ikinci bir proje gerçekçi değil. |
| Bizim kısıtlarımız | Yaklaşık 17,5 saat geliştirme (3,5 ortak + ~10,5 Minefield MVP'si + ~3,5 tampon); 1 yayıncı + 3 test hesabı; videoda ticari oyun ya da müzik yok; Twitch içeriği en fazla 24 saat tutuluyor. |

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
| **Whisper** | Twitch'in özel mesajı (DM). API ile göndermek için gönderenin telefon doğrulaması gerekir. | Hiçbir finalistte kullanılmıyor (Minefield'da whisper ile ekme çıkarıldı). |
| **AutoMod** | Twitch'in otomatik mesaj filtresi. | Klip başlıkları ve cevaplar buna takılabilir. |
| **Stream delay (gecikme)** | İzleyicinin gördüğü görüntü gerçek zamanın 2–5+ saniye gerisinden gelir ve gecikme her izleyicide farklıdır. | VAR'ın tekrarı buna göre ayarlanır. Minefield'da önemsiz: overlay yerelde eklendiği için kelime ve patlama aynı miktarda gecikir. |
| **Channel points / Bits** | İzleyicinin kazandığı puanlar / parayla alınan Twitch kredisi. | Rakip ürünler kullanıyor, biz değil. |

### OBS tarafı

| Terim | Ne demek | Bizim kullanım |
| --- | --- | --- |
| **OBS** | Yayını hazırlayıp Twitch'e gönderen ücretsiz yayın programı. | Bütün projeler. |
| **Browser source** | OBS'te yayının üstüne bir web sayfası koymak. "Overlay" denen grafik katmanı genelde budur. | Patlama, jüri sırası, çağrı kartı... |
| **Dock** | OBS içinde yayıncının gördüğü ama yayına çıkmayan panel; bir web sayfasıdır. | Mod paneli, Checkpoint kontrolü. |
| **obs-websocket** | OBS'i dışarıdan kod ile kontrol etme protokolü (OBS 28+ ile birlikte gelir). | Tekrar oynatma, mikrofon durumu. |
| **Replay buffer** | OBS'in son N saniyeyi hafızada tutması; komutla dosyaya kaydedilir. | VAR'ın tekrarı. |
| **Media Source** | OBS'te video dosyası oynatan kaynak. Hızı ayarlanabilir. | VAR'ın ağır çekimi. |

### Konuşma tanıma (ML tarafı, senin alanın)

| Terim | Ne demek |
| --- | --- |
| **STT (speech-to-text)** | Konuşmayı yazıya çevirme. |
| **faster-whisper** | OpenAI Whisper'ın hızlı (CTranslate2) sürümü. GPU'da float16 ile çok hızlı çalışır. Modeller: `base.en`, `small.en`, `medium.en`, `large-v3-turbo`. **Minefield `large-v3-turbo` kullanıyor** (`deepdml/faster-whisper-large-v3-turbo-ct2`, çok dilli). |
| **VAD** | Voice Activity Detection: sesin konuşma mı sessizlik mi olduğunu bulur (ör. Silero VAD). Whisper'ın sessizlikte uydurma yapmasını (hallucination) önler. |
| **Hotwords** | faster-whisper'a "bu kelimeler geçebilir" diye verilen ipucu listesi. Doğru tanımayı artırır, ama sessizlikte uydurma riskini de artırır; bu yüzden VAD şart. Minefield'da kullanılmıyor. |
| **Keyword spotting** | Sürekli konuşmada belirli kelimeleri yakalama. |
| **Akan tanıma + LocalAgreement** | Konuşma sürerken biriken ses kısa aralıklarla (ör. 0,5 sn) yeniden yazıya dökülür. Bir kelime iki ardışık tahminde de görünürse kesinleşmiş sayılır (whisper_streaming'deki yöntem). Minefield'da patlama bu onayla gelir. |
| **Hit / false alarm / lag** | Doğru yakalama / söylenmemiş kelimeyi yakalamak / söyleyişten tepkiye kadar geçen süre. |

---

## 4. Senin makinen ve telefon/hesap ihtiyacı

### Makine: ne anlama geliyor?

| Parça | Değer | Etkisi |
| --- | --- | --- |
| GPU | **RTX 4070 Laptop, 8 GB VRAM** | faster-whisper `large-v3-turbo` float16 ile rahat sığar. Minefield'da konuşma sürerken yaklaşık 0,5 saniyede bir çalışacak. OBS açıkken GPU yükü, VRAM ve gecikme harness'in ilk koşusunda ölçülecek. |
| GPU + yayın | OBS videoyu NVENC ile kodlar; NVENC GPU'da ayrı bir donanım birimi. | Whisper ile yayın kodlama birbirini pek etkilemez. T1 yine de "kare düşmesi yok" şartını ölçecek. |
| CPU / RAM | Ryzen 7 8845HS, 32 GB | Fazlasıyla yeterli. |
| İşletim sistemi | Windows 11 + WSL2 (repo WSL içinde) | **Dikkat:** WSL2 içinden mikrofona erişmek güvenilmez. OBS de Windows'ta çalışacak. **Öneri:** ses yakalama ve STT'yi Windows'ta yerel Python süreci olarak çalıştırmak (CUDA Windows'ta sorunsuz). Diğer kısımlar WSL'de kalabilir. obs-websocket'e WSL'den bağlanmak için Windows host IP'si ya da WSL "mirrored networking" gerekir. Bunlar T1 sırasında doğrulanacak. |

**Dil:** Video ve jüri İngilizce, yani **senin aksanlı İngilizcen** tanınacak. `large-v3-turbo`'yu kendi sesinle denedin ve iyi buldun; bu riski büyük ölçüde kapatıyor. Model çok dilli olduğu için `language="en"` sabitlenmeli. Aksi hâlde kısa ve aksanlı cümlelerde dili yanlış tespit edebilir.

### Telefon ve hesaplar: hangi proje ne istiyor?

| Proje | Telefon gerekli mi? | Kaç tane? | Neden |
| --- | --- | --- | --- |
| **Minefield** | Şart değil ama **arkadaş şart gibi** | Senin telefonun + **1–2 arkadaş** (kendi telefonlarından) | Kart özellikle şunu istiyor: mayın kelimelerini sen değil arkadaşların eksin. Böylece kelimeyi gerçekten bilmezsin ve demo sahnelenmiş görünmez. Arkadaşlar test hesabına telefondan giriş yapıp ekme sayfasını açar. |
| **Checkpoint** | Hayır | — | 3 test hesabı chat simülatörüyle mesaj atar. Arkadaş gerçek soru sorarsa daha doğal görünür; SSS sahnesi için ikinci bir kişinin aynı soruyu sorması gerekir. |
| **VAR** | Hayır | — | `!var` ve oyları simülatör ya da arkadaşlar yazar. Telestrator çizimini sen ya da mod hesabı dock'tan yaparsın. |

**Test hesapları için telefon numarası:**
- Twitch hesabı genelde e-postayla açılabiliyor; Twitch ek olarak telefon doğrulaması isteyebilir. Kaç hesabın aynı numaraya bağlanabileceği **doğrulanmadı**. Hesapları açarken göreceğiz; senin numaran ve 1–2 arkadaşın numarası büyük ihtimalle yeter.
- Kanal sahibi sensin; "chat için telefon doğrulaması iste" ayarını kapalı tutabilirsin.
- Whisper (DM) ile mesaj göndermek telefon doğrulaması istiyor, ama Minefield bunu kullanmıyor.

**Kısa cevap:** Üç finalistin hiçbiri için ekstra telefon gerekmiyor. Ama Minefield için **1–2 arkadaşın gerçekten katılması** neredeyse şart: T0'da (29 Ekim) ve kayıtta (1 Kasım akşamı). Arkadaşlar ekme sayfasını kendi telefonlarından açar.

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

**Bütçe hesabı (karardan sonra):** 3,5 saat ortak altyapı + ~10,5 saat Minefield MVP'si + ~3,5 saat tampon = **yaklaşık 17,5 saat**. Astra'nın uyarısı: 3,5 saatlik ortak altyapı Twitch'e yeni biri için iyimser. Seçilen projenin ihtiyacı olmayan parçaları baştan kurma; örneğin Minefield'ın ilk patlaması için obs-websocket gerekmiyor.

**MVP'ler nasıl son hâline geldi:** Önce her projeye 12 saate kadar eklemeler önerdim. Sonra üç model bu eklemeleri serbestçe inceledi. Astra'nın genel uyarısı belirleyici oldu: *"12 saatlik MVP alanını doldurma hedefi... son eklenen özellikler tamamlanmış ürün hissinden çok yeni hata yüzeyleri getiriyor."* Bu yüzden eklemelerin bir kısmı kesildi, MVP'ler ~11 saate indi ve artan süre tampona kaldı. Ayrıntılar her projenin "Önceki plandan ne değişti" tablosunda.

---

## 6.1 Minefield: seçilen proje

Puan (step 7): **16,3**, risk Yüksek (karardan sonra Orta). Step 8'de üç modelin de birinci tercihi. **28 Ekim'de seçildi.**

### Ne?
İzleyiciler gizlice "kelime mayınları" eker. Yayıncı sıradan konuşurken o kelimeyi söylerse ekranda patlama olur ve mayını ekleyenin adı çıkar.

### Somut örnek
> Sen yayında öğle yemeğinden bahsediyorsun. Bo 6 dakika önce gizlice "PINEAPPLE" kelimesini ekmiş. Chat'te Bo soruyor: "worst pizza topping?" Sen "pineapple on pizza is—" derken **BOOM**: ekran sallanır, afiş çıkar: *"Bo's mine: PINEAPPLE (planted 6 min ago)"*. Bo chat'e "GOT HIM 😈" yazar.

### Nasıl çalışır (son hâli)
1. İzleyici `!mine` yazar. Bot ona ekme sayfasının linkini verir. Sayfa Twitch girişi ister (hiçbir izin istemeyen, sadece kimlik doğrulayan bir giriş; sayfada "We only see your Twitch name" yazar).
2. İzleyiciye **yaklaşık 300 kelimelik bir desteden rastgele 6 kart** gösterilir; kelimesini bunlardan seçer: pineapple, giraffe, spaghetti, keyboard gibi somut, komik isimler. Kimse seçimi görmez. Kurallar:
   - izleyici başına aynı anda 1 mayın, toplamda en fazla **4 canlı mayın** (ekran okunabilsin diye; T0'da 5–6 denenir);
   - aynı kelime iki kişiye verilmez (seçilen kelime destede kalan kartlardan çıkar);
   - mayın eklendikten **30 saniye sonra** aktif olur ("kurulma" süresi).
3. Overlay'de mayın çipleri görünür: sadece sahiplerin adları, kelimeler yok.
4. İzleyiciler sohbeti kendi kelimelerine doğru çekmeye çalışır. Asıl oyun bu "tuzak kurma" kısmı.
5. Yerel STT yayıncının mikrofonunu dinler: `large-v3-turbo`, dil `en` olarak sabit, hotword yok.
   - VAD konuşma başlayınca bir ses tamponu açar. Konuşma sürerken tampon yaklaşık **0,5 saniyede bir** yeniden yazıya dökülür (akan tanıma).
   - Bir mayın kelimesi **iki ardışık tahminde** de görünürse onaylanır (LocalAgreement). Böylece patlama cümlenin bitmesini beklemez, kelimeden yaklaşık 1 saniye sonra gelir.
   - VAD konuşma görmediğinde model çalışmaz; Whisper'ın bilinen uydurma kalıpları ("thank you for watching" gibi) filtrelenir.
6. **Fitil = onay penceresi:**
   - Kelime ilk tahminde görününce sahibinin çipinde bir **kıvılcım** çakar (~0,5 sn).
   - İkinci tahminde de varsa **BOOM**: patlama, afiş, stream marker.
   - Kaybolursa fitil **"fıss"** diye söner. Ayrı bir güven eşiği yok.
7. Patlamadan sonra mod 10 saniye içinde **DEFUSE** edebilir: geri sarma animasyonu ve "false alarm" damgası çıkar. DEFUSE edilmezse 30 saniyelik başlıklı klip açılır.
8. Yayın sonunda patlamayan mayınlar "dud" olarak açılır: *"Cy's mine 'GIRAFFE' never went off"*. Altında sadece **o yayına ait** birkaç sayaç görünür (kaç patlama, en hızlı patlayan mayın). Yayınlar arası hiçbir şey saklanmaz.
9. **"Konuşmayı yaz" modu:** Dock'ta bir metin kutusu; yazılan cümle STT'den geliyormuş gibi işlenir. STT'siz test için ve kayıt sırasında STT tökezlerse sigorta olarak.

### 3 dakikalık video akışı
| Zaman | Ne oluyor |
| --- | --- |
| 0:00 | Soğuk açılış: öğle yemeği sohbeti, "pineapple" BOOM, afiş, chip'te Bo'nun adı. |
| 0:08 | Başlık kartı: "Chat plants secret words. Say one on stream, it explodes." |
| 0:12 | Arkadaşın telefonundan ekme sayfası: desteden kelime seçimi; kelimenin gizli kaldığı görünüyor. |
| 0:35 | İkinci tur: iki arkadaş tuzak kurar; biri tutar (BOOM), biri tutmaz. |
| 1:00 | Bir kelime ilk tahminde görünür, kıvılcım çakar, ikinci tahminde kaybolur: fitil "fıss" diye söner. Ya da yanlış bir patlamayı mod DEFUSE eder. Aksilik gag'e döner. |
| 1:25 | Yayın sonu: dud'lar açılır ("Cy'ın 'giraffe'ı hiç patlamadı"). |
| 1:45 | Kaputun altı: yerel STT, ses kaydedilmiyor; harness tablosu ~10 sn ekranda (isabet, yanlış alarm, gecikme). |
| 2:10 | Codex bölümü (20–30 sn): harness'in yakaladığı somut bir hata ve düzeltmesi. |
| 2:40 | Kapanış. |

**Not:** Birkaç tur kaydet, en temiz patlamayı başa koy. Kelimeleri gerçekten arkadaşların seçsin; sen bilme.

### Teknik detay
- **Mimari:**
  - **STT süreci (Windows'ta yerel Python):** mikrofon → Silero VAD → büyüyen ses tamponu → her ~0,5 sn'de `large-v3-turbo` → iki ardışık tahminin ortak kelimeleri → eşleşme olayı.
    - Tampon konuşma boyunca büyür; sözce bitince ya da ~15 saniyede sıfırlanır.
    - Başlangıç ayarları: float16, `language="en"`, `beam_size=1`, `condition_on_previous_text=False`, hotword yok. Harness'te ayarlanacak.
  - **Köprü:** Windows süreci eşleşmeyi WSL'deki FastAPI'ye HTTP POST ile gönderir.
  - **Eşleşme:** metin normalize edilir (küçük harf, noktalama silinir, çoğul eki atılır) ve canlı mayınlarla tam kelime olarak karşılaştırılır. Birleşik yazımlar için destede kelimenin birkaç biçimi tutulur (pineapple, pine apple). Aynı konuşmada bir mayın bir kez patlar.
  - **Patlama:** FastAPI → WebSocket → OBS overlay. Minefield'ın ilk patlaması için obs-websocket gerekmez.
- **Twitch:**
  - EventSub `channel.chat.message`, Send Chat Message;
  - Create Stream Marker (`channel:manage:broadcast`, VOD açık olmalı);
  - Create Clip (`clips:edit`, `title`, `duration=30`). Klip asenkron ve hazır olması bir dakikayı bulabilir; T5'te klibi oynatıp patlamanın içinde olduğunu doğrula.
  - Ekme sayfası için Twitch girişi ve herkese açık URL (`cloudflared` quick tunnel; bilgisayar uykuya geçerse tünel kapanır).
- **Gecikme hedefi:** kelimenin bitişinden patlamaya medyan ≤1,5 sn, en kötü durumda ≤3 sn. Overlay yayına yerelde eklendiği için yayın gecikmesi kelimeyi ve patlamayı aynı miktarda kaydırır; yalnızca STT gecikmesi önemli.
- **Saatler:**

| Parça | Saat |
| --- | --- |
| Ekme sayfası: scope'suz Twitch girişi + cloudflared + rastgele 6 karttan seçim | 1,5 |
| STT: VAD + akan tanıma (`large-v3-turbo`) + iki ardışık tahmin onayı + Windows → WSL köprüsü | 2 |
| Kelime destesi (~300 isim; sesteşler harness'le elenmiş) + kurallar | 0,75 |
| "Konuşmayı yaz" dock modu | 0,25 |
| Doğruluk harness'i (Codex artifact) | 1 |
| Overlay: çipler, patlama, afiş | 2 |
| Marker, klip, DEFUSE, dud'lar + yayın içi sayaçlar | 1,5 |
| Fitil: kıvılcım ve "fıss" (onay penceresine bağlı) | 0,5 |
| Cila | 1 |
| **MVP toplamı** | **~10,5** |
| Zaman kalırsa sırayla: `!dud` chat itirazı (patlamadan sonra 10 sn içinde chat çoğunluğu `!dud` derse DEFUSE) 0,5; Türkçe deste + ekleri tanıyan eşleşme ~1 (videoda 5 sn "also works in Turkish"); mayın tarama 1 | — |
| **Çıkarıldı:** serbest kelime girişi, yayınlar arası Bomb Squad tablosu, whisper ile ekme, "Call it" modu | — |

- **Codex artifact:** Doğruluk harness'i. Senin sesinle kaydedilmiş konuşmaları (deste kelimeleri cümle içinde, benzer sesli kelimeler, sessizlik, doğal duraksamalar, OBS açıkken normal konuşma) yakalayıcıdan geçirir; isabet, yanlış alarm ve gecikmeyi (kelimenin bitişinden) raporlar. Tahmin aralığı, tampon sınırı ve deste bu verilerle ayarlanır.

### Önceki plandan ne değişti (ve neden)
| Önceki | Son hâli | Kim önerdi |
| --- | --- | --- |
| Serbest kelime + "ilk 1000 kelime yasak" + blocklist | ~150 isimlik deste | Grok, Astra. Grok: "İlk 1000 kelime yasak, tam da Whisper'ın kaçırdığı kelimeleri seçtiriyor." Deste trol kelime sorununu da kapatıyor. |
| ~2 sn'lik kayan pencere + hotwords | Sözce bazlı tek yazım + hotword'süz ikinci geçiş + ≤4 canlı mayın | Grok (sözce, ≤4 mayın), Opus (ikinci geçiş). Üçü de `hotwords`'ün hayalet kelime riskini vurguladı. |
| Fitil 3 sn | Sadece orta güvende, ≤2 sn | Opus ve Grok fitili istedi; Astra gecikme eklediği için karşıydı. Kısa ve sadece belirsiz durumlarda olunca ikisi de karşılanıyor. |
| Mayın tarama MVP'de | Zaman kalırsa | Grok: koyma. Astra: ikinci sürüm. Opus: zaman kalırsa. |
| Bomb Squad (yayınlar arası) | Sadece yayın içi sayaçlar | Üçü de. Yayınlar arası kayıt "24 saatten uzun veri tutma" kuralımıza aykırı ve 3 dakikalık videoda görünmüyor. |
| Gecikme ≤3 sn | Medyan ≤1,5 sn | Opus, Astra: "Espri, kelimeden hemen sonra gelen patlamada." |
| — | "Konuşmayı yaz" modu | Opus. STT'siz test ve kayıt sigortası. |
| — | Kurulma süresi, aynı kelime iki kişiye verilmez | Opus, Astra. |

### Karardan sonra değişenler (28 Ekim: STT modeli)
`deepdml/faster-whisper-large-v3-turbo-ct2` senin testinden geçtiği için, zayıf bir model için koyduğumuz önlemlerin bir kısmı gereksiz kaldı:

| Önceki | Şimdi | Neden |
| --- | --- | --- |
| `small.en` + hotwords | `large-v3-turbo`, hotword yok, `language="en"` sabit | Turbo hotword olmadan da yeterince doğru; hotword ise uydurma riski getiriyordu. Dil sabit, çünkü çok dilli model kısa ve aksanlı cümlelerde dili yanlış tespit edebilir. |
| Sözce bazlı tek yazım + ikinci geçiş | Akan tanıma + iki ardışık tahmin onayı | Patlama cümle sonunu beklemiyor. "Pineapple on pizza is honestly the worst thing ever" cümlesinde sözce bazlı tanımada BOOM kelimeden ~3 sn sonra, akan tanımada ~1 sn sonra gelir. Espri bu zamanlamada. |
| Fitil: sadece orta güvende, ≤2 sn | Fitil = onay penceresi: kıvılcım → BOOM ya da "fıss" | Ayrı eşik yok. ~0,5 sn zaten var olan bekleme, yani Astra'nın "fitil gecikme ekliyor" itirazı da karşılanıyor. |
| ~150 kelimelik deste (STT için) | ~300 kelime, izleyiciye rastgele 6 kart | Desteyi artık STT için değil, trol kelimeleri engellemek ve oyun dengesi için tutuyoruz. Rastgele kart, herkesin aynı kolay kelimeyi seçmesini önlüyor ve kart çekme hissi veriyor. |
| ≤4 mayın (STT yükü) | ≤4 mayın (ekran okunabilirliği) | T0'da 5–6 denenebilir. |
| T1: geçme şartı | T1: harness'in ilk koşusu | Doğruluk çözüldü; gecikme ve yanlış alarm yine ölçülüyor, çünkü videoda rakamlar gerekiyor. |
| Yedek proje: VAR | Proje içi sigortalar | "Konuşmayı yaz" modu ve Discord + mod yolu. |
| MVP ~11,25 sa | ~10,5 sa | Artan süre video ve tampona. |
| Türkçe yok | Zaman kalırsa | Model çok dilli, Impact için koz. Ama Türkçe ekler ("ananası", "ananasa") eşleşmeyi zorlaştırıyor; test etmeden iddia edilmeyecek. |

### Rakipler ve fark
| Rakip | Ne yapıyor | Fark |
| --- | --- | --- |
| **OK Gamers** (TwitchCon Hackathon 2019 **büyük ödülü**) | Yayıncı "Ok gamers" + soru deyince STT chat anketi başlatır. | Kelimeyi yayıncı seçiyor. |
| Streamer.bot Voice Control (yaygın), Stream Voice Triggers | Yayıncının ayarladığı cümleler aksiyon tetikler. | Kelimeyi yayıncı seçiyor. |
| Konuşma tanımalı küfür kavanozları (Blabla Radar, obs-popup-overlay) | Listedeki kelimeleri sayar. | Liste yayıncının, oyun yok. |
| Gizli kelime chat oyunları (AnkhbotSecretWord, RobinSystem Word Guess, Chatexto), Taboo tarzı oyunlar (Wordeous), yayın bingo'su | — | Hepsi yazılı chat'te oynanıyor. |
| [Heads Up! Phones Down](https://support.aspyr.com/hc/en-us/articles/22586269678093-Heads-Up-Phones-Down-Edition-Twitch-Extension-Overview) (Twitch eklentisi) | Kelime yayıncıdan gizleniyor, izleyiciler chat'e ipucu yazıyor. | Kelimeyi oyun seçiyor, yayıncının konuşması dinlenmiyor. |
| [Don't Get Got](https://draughtslondon.com/ultimate-guide-to-the-dont-get-got-game/) (parti oyunu) | Gizli görev: "bir oyuncuya 'banana' dedirt". | Yüz yüze; Twitch yok, otomatik hakem yok. |

**Fark:** Bulunan bütün konuşma tetikleyicilerinde kelimeyi yayıncı seçiyor; izleyicinin gizli kelime seçtiği bütün oyunlar ise yazılı chat'te geçiyor. Step 8'de üç model de web'de aradı, daha yakın bir şey bulamadı.

**Ama tür biliniyor.** "Birine kelime söyletmek" bir parti oyunu fikri. Bunu saklama, sahiplen: *"Inspired by party games like Don't Get Got: a whole chat against one live streamer, refereed automatically by local speech recognition."* Astra: "Yeni bir oyun türü diye sunmazdım. Farkı **tetikleyiciyi gizlice izleyicinin seçmesi** üzerinden anlatın." Gerçekçi Innovation beklentisi 4; fark videoda görünmezse 3.

OK Gamers'ın 2019'da aynı yarışmanın büyük ödülünü kazanması, jürinin STT + chat fikirlerine açık olduğunu gösteriyor. Ama "OK Gamers'ın devamı" gibi algılanmamak için fark videoda açık olmalı.

### Talep ve karşı sinyaller
- **Doğrudan talep yok.** Üç araştırmacı da bu oyunu isteyen birini bulamadı. Astra: "Eğlence ürünlerinde doğrudan talep bulunamaması tek başına olumsuz değil; birkaç kişinin gerçekten oynamak istemesi bir forum talebinden daha iyi gösterir."
- **Dolaylı talep:** yayıncılar elle küfür kavanozu ve bingo kartı yürütüyor; iki Reddit başlığında "mikrofonda kelime algılayıp efekt tetikleme" isteniyor (doğrulanmadı).
- **Karşı sinyal:** troller yayıncılara zaten bir şeyler söyletmeye çalışıyor (Dexerto 2019, doğrulandı). Deste bunu büyük ölçüde kapatıyor.
- **Teknik karşı sinyal:** faster-whisper `hotwords` sessizlikte kelime uydurabiliyor (issue 1356, PR 731). Bu yüzden hotword kullanılmıyor; VAD ve iki ardışık tahmin onayı uydurmalara karşı koruyor.

### Kitle
Yayıncının konuştuğu her yayın: Just Chatting (%14,2), IRL (%1,8) ve konuşkan oyun yayınları. Oyun gerekmediği için demo oyunu da gerekmiyor.

### Riskler, test ve yedek plan
| Risk | Ne kadar ciddi | Önlem |
| --- | --- | --- |
| STT kelimeyi kaçırır ya da olmayan kelimeyi yakalar | Düşük–orta (turbo senin sesinle test edildi) | Harness'in ilk koşusu: OBS açık ve yayın sürerken gecikme ve VRAM, 10 dk sessizlik ve arka plan sesi, deste kelimeleri. Hedefler: ≥%80 isabet, 10 dakikada ≤1 yanlış alarm, medyan gecikme ≤1,5 sn. Onay kuralı + "fıss" + DEFUSE. |
| **Oyun eğlenceli değil** | **Orta–yüksek, henüz ölçülmedi** | **T0:** Discord'da kodsuz 20 dakika. Ölçüt: arkadaşlar ikinci tur istiyor mu? Sonuç kötüyse proje değil kurallar değişir: mayın sayısı, kurulma süresi, deste zorluğu. |
| Aksanlı İngilizce | Düşük | Turbo kendi sesinle denendi; `language="en"`. |
| GPU paylaşımı (OBS + 0,5 sn'de bir turbo) | Düşük | NVENC ayrı bir birim. Harness ilk koşusunda kare düşmesi ölçülür; gerekirse tahmin aralığı 0,75–1 sn'ye çıkar. |
| Ekme sayfası | Düşük–orta | T4. Kalırsa: arkadaşlar kelimelerini Discord'dan mod rolündeki üçüncü kişiye iletir, o da dock'a girer. Sen yine bilmezsin. |
| "Don't Get Got'un Twitch hâli" algısı | Orta | Benzerliği sahiplen; ilk 20 saniyede "izleyici gizlice seçti + sohbetle tuzak + kuranın adı" görünsün. |
| Arkadaşların zamanı | Orta | Darboğaz koddan çok insanlar. Arkadaşları şimdiden bağla: 29 Ekim T0, 1 Kasım akşamı kayıt. |
| **Sigortalar** | — | Proje değişmiyor. STT tökezlerse "konuşmayı yaz" modu; ekme sayfası tökezlerse Discord + mod yolu. |

### Step 7: puanlar ve modellerin söyledikleri
| | Innovation | Impact | Tech | Design | Toplam | Risk | Sıra |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Grok | 5 | 3 | 3 | 5 | 16 | Yüksek | **1** |
| Astra | 5 | 3 | 3 | 5 | 16 | Yüksek | 2 |
| Claude | 5 | 3 | 4 | 5 | 17 | Orta | **1** |
| **Ortalama** | **5,0** | **3,0** | **3,3** | **5,0** | **16,3** | | |

- **Grok:** "Aramanın gerçekten kaçırdığı döngü bu." Ama "bir kaçırma ya da sahte bir patlama, ürünün ta kendisi".
- **Astra:** DEFUSE'un "sık algılama hatalarını telafi etmediğini" söyledi. Konuşma tanıma test edilmediği için 2. sıraya koydu.
- **Claude:** Tech'e 4 verdi: lokal keyword spotting teknik olarak ilginç ve harness güçlü bir Codex örneği.

### Step 8: serbest incelemeler
- **Opus: "Seçimim: Minefield."** Şartları T1 ve T0. Dördün en yenisi; ML gücün projenin kalbinde; ölçülmüş bir doğruluk tablosu "how well is it built" sorusuna "kimsenin itiraz edemeyeceği bir cevap". Fitil "en iyi ek".
- **Grok: "En iyi yarışma fikri bu."** Tek cümlede anlatılıyor, patlama üç saniyede izleniyor. "Kesilemez üç şey: kelimesiz chip, gerçekten söylenmiş bir kelimede gerçek patlama, eken kişinin adı. Gerisi ikinci dakika."
- **Astra: "Minefield'i seçerdim."** "İzleyici yayındaki olayın gerçek sebebi oluyor... İki arkadaşla bile çekişme, sürpriz ve sahiplenme oluşabilir." Ama: "On dakikada bir yanlış patlama bile saatte altı tartışmalı sonuç demek."

### Benim görüşüm
- **Doğru seçim.** Altı değerlendirmenin altısında da birinci ya da ikinci; step 8'de üç model de "bunu yapardım" dedi.
- **STT artık ana risk değil.** Turbo'yu kendi sesinle denemiş olman en büyük belirsizliği kapattı. Kalan iş mühendislik: akan tanımada gecikmeyi ve yanlış alarmı ölçüp ayarlamak.
- **En büyük açık soru eğlence.** T0 artık "yapalım mı?" testi değil, "nasıl ayarlayalım?" testi.
- **Artan süreyi özellik eklemeye harcama.** Minefield'da video işin yarısı; zaman kalırsa listesi sıralı ve kısa.
- **Destenin bedeli:** "İzleyici her şeyi seçebilir" hissi biraz azalıyor. Ama gizlilik ve tuzak kurma, yani oyunun özü aynı kalıyor.

---

## 6.2 VAR: seçilmedi

Puan (step 7): **15,0**, risk Orta. Step 8'de Grok ve Astra'nın ikinci tercihi; Opus'un üçüncüsü.

### Ne?
Futboldaki VAR'ın Twitch versiyonu. Chat yayıncının bir iddiasına itiraz edince iki izleyicinin `!var` yazması yeterli: "VAR CHECK" sireni çalar, ağır çekim tekrar oynar, chat 15 saniye oy verir (jüri), "NO BASKET" gibi bir karar damgası basılır ve başlıklı bir klip oluşur.

### Somut örnek
> Kâğıt topu çöp kutusuna atıyorsun ve "IN!" diyorsun. Chat'te iki kişi `!var` yazıyor. Siren çalıyor, ekran "VAR CHECK" oluyor. Son 10 saniye ağır çekimde oynuyor: top çemberden sekip dışarı düşüyor. Kare donuyor, topun düştüğü yerde bir halka beliriyor. Chat 15 saniye `!yes`/`!no` oyluyor, oy verenlerin isimleri jüri sırasında görünüyor. **"NO BASKET"** damgası iniyor. Chat'e "VAR: NO BASKET" başlıklı klibin linki düşüyor.

### Nasıl çalışır (son hâli)
1. Yayıncı bir iddiada bulunur ("IN!").
2. İlk `!var` geldiği anda replay buffer dosyaya kaydedilir ve **o an sabitlenir**. 30 saniye içinde ikinci bir farklı izleyici `!var` yazarsa çağrı onaylanır. Eşik aktif izleyici sayısına göre büyür; mod ya da yayıncı da VAR çağırabilir. İncelemeler arasında bir bekleme süresi (cooldown) var.
3. **VAR beklemede (varsayılan):** Tekrar hemen oynamaz. Ekranın köşesinde "🟨 VAR PENDING (2 calls)" çıkar; yayıncı uygun anda tuşa basar. "Auto" modunda hemen başlar (videonun hook'u bu modla çekilir).
4. "VAR CHECK" geçişi oynar. Arka planda ffmpeg, sabitlenen andan geriye ~10 saniyeyi keser, **önceden yarı hıza çevirir** ve sona donmuş bir kare ekler. Geçişin 2–3 saniyesi bu işlemi gizler. Media Source hazır dosyayı oynatır.
5. Donmuş karede yayıncı dock'ta bir noktaya tıklar; o noktada **bir halka** belirir.
6. Chat 15 saniye `!yes`/`!no` oylar; kişi başına tek oy; isimler jüri sırasına dizilir. Oy eşitse ya da kimse oy vermezse karar **"INCONCLUSIVE"**.
7. Karar damgası donmuş karenin üstüne basılır. Uygulama 60 saniyelik "VAR: NO BASKET" klibini ve bir marker oluşturur.

**Self-VAR:** Yayıncı kendi iddiasına VAR çağırır ("mükemmel bir daire çizebilirim"), chat iddiayı reddedebilir. Her yayında tekrarlanabilecek bir şaka.

### 3 dakikalık video akışı
| Zaman | Ne oluyor |
| --- | --- |
| 0:00 | Hook (auto mod): kâğıt top, "IN!", iki `!var`, siren, ağır çekim, halka, jüri, "NO BASKET". |
| 0:25 | Klip linki chat'e düşer, klipten 5 saniye. |
| 0:40 | VAR beklemede: yayıncı bir işin ortasında, "🟨 VAR PENDING" köşede bekliyor; yayıncı işi bitirip tuşa basıyor. |
| 1:00 | Self-VAR: "mükemmel daire çizerim", chat reddeder. |
| 1:35 | İlk çağrının anı nasıl sabitlediği; gecikme payı ve geri itme kısayolu. |
| 2:10 | Codex artifact, kapanış. |

### Teknik detay
- **Mimari:**
  - **Kayıt:** İlk `!var`'da `SaveReplayBuffer`; `ReplayBufferSaved` olayı dosya yolunu verir.
  - **Ağır çekim:** OBS Media Source'ta `speed_percent` değişince kaynak baştan başlıyor (Opus, OBS kaynak kodu). Bu yüzden ağır çekim **önceden ffmpeg ile** hazırlanır: kes → `setpts` ile yarı hız → `tpad` ile donmuş kare → `h264_nvenc` (10 saniyelik klip ~1 sn). Astra'nın notu: tüm replay'i tek hızda oynatmak yeterli; son 4 saniyede hız değiştirmek şart değil.
  - **Yol dönüşümü:** OBS Windows'ta, sunucu WSL'de. Ya `C:\…` ↔ `/mnt/c/…` dönüşümü ya da ffmpeg'i Windows tarafında çalıştırmak.
  - **Gecikme payı:** İzleyici yayını 2–5 saniye geriden görür. Tekrar, ilk çağrı anı eksi gecikme noktasından başlar; tutturamazsa "geri it" kısayolu var.
  - **Oylama:** Astra'nın notu: oy penceresi sunucu saatinden sayılırsa bazı izleyicilerin süresi kısalır; gerçek Twitch oynatıcısıyla dene. Native Polls sadece Affiliate/Partner kanallarda olduğu için `!yes`/`!no` doğru seçim.
  - **Klip:** Karardan hemen sonra Create Clip, `duration=60`. Ritüel 25 saniyenin altında kalırsa klip anı ve incelemeyi birlikte tutar (Grok). T5'te klibi oynatıp doğrula. Create Clip From VOD'u canlı demonun yoluna koyma: beta'da `vod_offset` klibi birkaç saniye kaydırıyordu, düzeldiği belli değil (Grok).
  - **Markalar:** "VAR CHECK" tasarımı senin olsun; FIFA ya da lig görseli yok (kurallar üçüncü taraf markalarını yasaklıyor).
- **Twitch:** EventSub chat, Create Clip, Create Stream Marker, Send Chat Message; OBS replay buffer ve Media Source.
- **Saatler:**

| Parça | Saat |
| --- | --- |
| Replay kaydı + ffmpeg ön-render + Media Source oynatma | 2,5 |
| Gecikme payı + kısayol | 1 |
| Çağrı ve oylama: ilk çağrıya sabitleme, tek oy, inconclusive, cooldown | 1,5 |
| VAR beklemede (varsayılan) + auto modu | 1 |
| Overlay: geçiş, jüri sırası, damga | 2,5 |
| Donmuş karede halka (basit işaretçi) | 0,5 |
| Klip + marker | 0,5 |
| Cila | 1,5 |
| **MVP toplamı** | **~11** |
| Zaman kalırsa: serbest çizimli telestrator 1; yayın sonu VAR derlemesi | — |
| **Çıkarıldı:** hakem itibarı (yayınlar arası), ikinci kamera açısı, karar geçmişi şeridi | — |

- **Codex artifact:** Tekrar pipeline'ı (buffer → ffmpeg → Media Source) ve simülatörle yapılan eşik ve oylama zamanlaması testleri.

### Önceki plandan ne değişti (ve neden)
| Önceki | Son hâli | Kim önerdi |
| --- | --- | --- |
| Media Source `speed_percent` (A), ffmpeg (B) | ffmpeg ön-render A planı | Opus (OBS kaynak kodu bulgusu), Astra (tek hız yeter) |
| Son 10 sn, ikinci çağrıdan geriye | İlk çağrının anı sabitlenir | Astra: "İkinci çağrıdan sonra son on saniyeyi oynatmak olayın kendisini kaçırabilir." |
| VAR beklemede bir ek | Varsayılan mod | Üç model de tuttu; Astra varsayılan yapılmasını istedi. |
| Telestrator (1,5 sa) | Basit halka (0,5 sa); serbest çizim zaman kalırsa | Opus: sadece yayıncı çizsin. Astra: "1,5 saat iyimser." Grok: "Çizim senkronu kolayca kötü görünür." |
| Hakem itibarı | Çıkarıldı | Üç model de. Astra: "Çoğunluğa katılmayı ödüllendiriyor, doğruluğu ölçmüyor." |
| — | Inconclusive, tek oy, cooldown | Astra |

### Rakipler ve fark
| Rakip | Ne yapıyor | Yaygın mı |
| --- | --- | --- |
| tomaae OBS instant replay | Chat komutuyla tekrar | Evet (12,6 bin indirme; son güncelleme 2019) |
| Streamer.bot replay buffer aksiyonları | Her tetikleyiciyle tekrar | Evet |
| Twitch'in kendi anketleri | Süreli oylama | Evet |
| Glitch Studios Instant Replay | Mod tetikli, markalı, 0,5× ağır çekim; oylama yok | Hayır |
| BarRaider OBS Tools, Fyre Instant Replay | `!replay` + klip | Hayır |
| Streamer's Court (Steam oyunu) | Chat suçlu/suçsuz oyluyor; tekrar yok | Hayır |

**Fark:** Tekrar ve oylama ayrı ayrı mevcut. Bulunamayan şey: eşik → tekrar → süreli jüri → karar → başlıklı klip zincirinin **tek bir ritüel** olması. Step 8'de Opus da replay ile chat jürisini birleştiren bir overlay bulamadı. Astra: "Sizin farkınız, replay'i topluluğun rol aldığı bir karar ritüeline dönüştürmeniz. Sunumun bütün ağırlığı buna binmeli."

### Talep ve karşı sinyaller
- **Dolaylı talep:** chat ile tetiklenen bir tekrar script'inin 12,6 bin indirmesi var (2019'dan kalma).
- **Chat jürisi ya da VAR incelemesi için doğrudan talep bulunamadı.**
- **Karşı sinyal:** Tekrar isteyen yayıncı, tekrarın ne zaman oynayacağını kendisi belirlemek istiyordu. VAR beklemede bunun için varsayılan.
- **Kullanım sıklığı:** Opus: "Çoğu oyunda sonucu oyunun kendisi belirliyor; etkinin büyük kısmı self-VAR gibi bir içerik formatına dayanıyor."

### Kitle
İtiraz edilebilir, gözle görülür sonuçlar: rekabetçi oyunlar (izlenmenin büyük kısmı), spor tarzı IRL meydan okumalar, masa düelloları. Konuşma tanıma gerektirmediği için aksan riski yok. Kâğıt topu demosu ticari oyun gerektirmiyor.

### Riskler ve test
| Risk | Önlem |
| --- | --- |
| Replay hattı (kayıt, ffmpeg, Media Source) | **T2:** komuttan sonra en fazla 5 saniyede tekrar ekranda. |
| Tekrar yanlış ana denk gelir | İlk çağrıya sabitleme + gecikme payı + geri itme kısayolu. |
| Klip asıl anı dışarıda bırakır | Ritüel 25 sn'nin altında; `duration=60`; T5'te oynatıp doğrula. |
| Yayını kesintiye uğratır | VAR beklemede varsayılan. |
| **Yedek plan** | T2 kalırsa bile replay'siz hâli (çağrı, jüri, damga, klip) hâlâ gösterilebilir (Grok). |

### Step 7: puanlar ve modellerin söyledikleri
| | Innovation | Impact | Tech | Design | Toplam | Risk | Sıra |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Grok | 3 | 3 | 4 | 5 | 15 | Orta | 3 |
| Astra | 3 | 3 | 4 | 5 | 15 | Orta | 4 |
| Claude | 3 | 3 | 4 | 5 | 15 | Orta | 3 |
| **Ortalama** | **3,0** | **3,0** | **4,0** | **5,0** | **15,0** | | |

- **Tamamen oybirliğiyle puanlanan tek proje.**
- **Grok:** "Setteki en yayın-gibi (broadcast-like) video."
- **Claude:** "Jüri bunu yeni bir fikir yerine cila olarak okuyabilir."

### Step 8: serbest incelemeler
- **Grok:** "En güvenli gösteri." T1 kalırsa "aynı repoda VAR'a dönerim". Ama: "Innovation en zayıf halka ve beraberlikte ilk kriter bu."
- **Astra:** "Dört fikir içinde en kolay izlenen gösteriyi üretebilir." İkinci tercihi; "fikrin zayıflığı yüzünden değil, Minefield'deki izleyicinin gizli planı daha kişisel ve ayırt edici olduğu için".
- **Opus:** "En güvenli 'iyi video' bu. Ama Innovation ve Tech'teki tavanı sınırlı; ilk 5'e girmesi için cilasının kusursuz olması gerekir." AI içermediğini, yarışmanın "with AI" çerçevesine oturmadığını not etti.

### Benim görüşüm
- **En sağlam yedek.** Minefield'la aynı riski (STT) taşımayan tek seçenek; konuşma tanıma yok, aksan riski yok.
- Herkes VAR'ı bildiği için ilk 10 saniyede anlaşılıyor.
- **Dezavantaj:** Innovation tavanı 3. Jüri "tekrar + anket, güzel paketlenmiş" diyebilir. Ritüeli olabildiğince teatral yap; stinger, ses efekti ve damga animasyonu Design puanını taşır.
- **Bunu seçersen:** OBS tarafı senin daha az deneyimli olduğun alan; T2'yi 29 Ekim'de mutlaka çalıştır.

---

## 6.3 Checkpoint: seçilmedi

Puan (step 7): **15,0**, risk Orta. Step 8'de Opus'un ikinci, Grok ve Astra'nın üçüncü tercihi.

### Ne?
Yayıncı çizim, kodlama ya da oyun gibi bir işe gömülmüşken chat'i görmezden gelmiş olmaz: mesajlar "kayıt kristali" olarak birikir. "Checkpoint" anında yayıncı mesajları **sesli** cevaplar; söylediği kelimeler karta yazılır ve her izleyici kendi mesajının altında yayıncının **gerçek sözlerini alıntılayan** bir yanıt alır.

Cevabı herkes görür: yayını izleyen herkes cevabı duyar ve kartta okur. Chat'teki alıntılı yanıt da herkese açık normal bir chat mesajıdır, fısıltı (whisper) değildir. Bu yanıtın tek farkı, soran kişiyi etiketlemesi ve onun mesajının altına bağlanmasıdır.

**SSS (senin kararın):** Aynı soru aynı yayında tekrar gelirse yayıncı ikinci kez cevaplamaz; bot eski cevabı alıntılar.

### Somut örnek
> Sen kod yazıyorsun, chat'e bakmıyorsun. 6 kristal birikiyor. Checkpoint'e basıyorsun. Ekranda kart: *"@ana (first time!): what editor is that?"* Elin hâlâ klavyede ve diyorsun ki: "Ana, it's VS Code with a dark theme." Kelimeler karta yazılıyor; ✓ ile kart uçuyor. 3 saniye sonra Ana'nın mesajının altında: *"✓ answered on stream: 'It's VS Code with a dark theme' (12:04)"*.
>
> 20 dakika sonra Mehmet "which editor do you use?" yazıyor. Bot hemen yanıt veriyor: *"📌 Answered earlier (12:04): 'It's VS Code with a dark theme' · type !ask to ask anyway"*.

Notlar: Opus, kodlama yayınının senin için en doğal demo ortamı olduğunu söyledi; çizim yapman gerekmez. Grok, "Micron 05" gibi marka + rakam karışımlarının Whisper'ın en çok yanıldığı yer olduğunu hatırlattı; demoda düz kelimeli cevaplar kullan.

### Nasıl çalışır (son hâli)
1. Yayıncı bir kısayol tuşuna basar ya da mod `!focus` yazar. Köşede bir rozet çıkar: "Focus: messages saved 0".
2. Her normal izleyici mesajı, izleyicinin renginde bir kristal olarak düşer. Komutlar ve bot satırları filtrelenir. **Kişi başına bekleyen mesaj sınırı ve toplam kuyruk sınırı** var (Astra: "Selam, emote ve devam mesajları kuyruğu hızla şişirir").
3. Yayıncı "checkpoint"e basar. Alt kısımda bir "çağrı kartı" belirir: önce sorular, sonra ilk kez yazanlar.
4. Yayıncı işini bırakmadan sesli cevap verir. Yerel STT kelimeleri söylendikçe karta yazar.
5. Kart, **tek tuşla** ya da yaklaşık 2 saniyelik sessizlikle kapanır. Otomatik kapanma, doğal konuşma denemesinde güvenilir çıkarsa öne alınır (Astra). ✓ damgası basılır, kart uçar.
6. 3 saniye sonra bot alıntılı yanıtı gönderir:
   - **Geri alma:** Bu 3 saniye dock'ta görünür; bir hotkey alıntıyı iptal edip düz makbuza çevirir.
   - Metin boş ya da güven skoru düşükse alıntı atlanır: "✓ answered on stream (12:04)".
   - Alıntı göndermeden önce bir blocklist'ten geçer (Opus: "Yanlış duyulmuş bir küfür bot hesabının başını yakar").
   - "Skip" kartı yanıt göndermeden kapatır.
7. **SSS (katmanlı, Opus'un önerisi):**
   - Her cevaplanan kart saklanır (o yayın boyunca).
   - Soru gibi görünen yeni bir mesaj, cevaplanmış sorularla karşılaştırılır.
   - Benzerlik **≥0,85**: bot eski cevabı "daha önce şöyle cevaplandı" diye alıntılar; `!ask` ile izleyici yine de kuyruğa girebilir.
   - **0,70–0,85:** Dock'ta tek tıkla onaylanan bir "bunu mu soruyor?" önerisi çıkar.
   - Daha düşük: mesaj normal bir kristal olur.
8. Sonunda bir özet görünür: "Checkpoint cleared: 4 answered, 4 receipts sent, 1 auto-answered".

### 3 dakikalık video akışı
| Zaman | Ne oluyor |
| --- | --- |
| 0:00 | Hook: kodlama yayını hızlandırılmış, 6 kristal, checkpoint, Ana'nın sorusu, sesli cevap karta yazılıyor, ✓ ve split-screen'de Ana'nın mesajının altındaki alıntı. |
| 0:20 | İki kart daha: biri "skip", biri düşük güvenle düz makbuz. |
| 0:50 | **SSS:** Mehmet benzer soruyu soruyor, bot eski cevabı alıntılıyor. Yayıncı başını kaldırmıyor. |
| 1:20 | Kaputun altı: ses segmentleme, güven kapısı, geri alma, reply threading, SSS eşikleri. |
| 2:05 | Codex artifact. |
| 2:30 | Kapanış. |

**Çıkarılan sahne:** "Yayından ayrılan izleyici sonra dönüp cevabı buluyor." Opus: Twitch Chat History yeni gelen birine sadece son 50 mesajı ya da son 1 saati gösteriyor; yoğun chat'te cevap pencerenin dışına kayar. Grok ve Astra: threaded reply çevrimdışı bildirim değil. Bu sahne kalırsa "in quiet chats" diye dürüstçe çerçevelenmeli ve "Twitch ona haber verdi" denmemeli.

### Teknik detay
- **Mimari:** mikrofon → VAD segmentleme → faster-whisper'ın büyüyen ses tamponunu yaklaşık 0,5 saniyede bir yeniden yazıya dökmesi (kısmi metin karta akar).
  - **Güven skoru:** `avg_logprob` ve `no_speech_prob` eşiklerinden. Astra'nın uyarısı: güven skoru doğru alıntı garantisi değil; T1b'de "okunabilir" değil, "anlamı ve kritik kelimeleri doğru" ölçülmeli.
  - **Gönderim:** `Send Chat Message` + `reply_parent_message_id`, 500 karakter; `is_sent` ve `drop_reason` okunur.
  - **SSS eşleştirme:** `all-MiniLM-L6-v2` + kosinüs benzerliği; eşikler 20–30 soru çiftiyle harness'te ayarlanır.
- **Twitch:** EventSub chat (`message_id` gerekli). Bot moderatör olmalı: 30 saniyede 100 mesaj.
- **Saatler:**

| Parça | Saat |
| --- | --- |
| Focus açma/kapama + filtre + kuyruk sınırları | 1,25 |
| Kristal rozet overlay'i | 1,5 |
| Çağrı kartı overlay'i (canlı transkript satırı, ✓ damgası) | 1,5 |
| Dock + sıralama + next/skip | 1 |
| Yerel STT: mikrofon, VAD segmentleme, faster-whisper, kısmi güncellemeler | 2 |
| Kapanış: tek tuş + sessizlik kuralı | 0,5 |
| Cevap makbuzu: güven eşiği, blocklist, 500 karakter, threaded reply, `drop_reason` | 0,5 |
| Geri alma hotkey'i | 0,25 |
| SSS (katmanlı): soru tespiti, embedding, iki eşik, dock önerisi | 1,5 |
| Cila | 1 |
| **MVP toplamı** | **~11** |
| Zaman kalırsa: soruyu yayıncının kulaklığına okuyan yerel TTS 1 (Opus; "Monitor Only" ile yayından ayrılmalı); cevabın klip linki 1 (Grok ve Astra şüpheli: klip asenkron, VOD zaman eşlemesi doğrulanmalı) | — |

- **Codex artifact:** Sesten makbuza giden pipeline; kayıtlı cevap sesleri ve simüle chat ile test edilir. SSS eşikleri de simülatörün tekrar eden ve benzemeyen soru çiftleriyle test edilir.

### Önceki plandan ne değişti (ve neden)
| Önceki | Son hâli | Kim önerdi |
| --- | --- | --- |
| SSS tek eşik (0,85) | İki eşik + dock önerisi | Opus. Grok ve Astra SSS'ye karşıydı ("dört cevaplık bir yayında ya hiç tutmaz ya yanlış tutar"; "benzer soru, aynı soru olmayabilir"). Senin kararın olduğu için kaldı, ama yanlış eşleşmeye karşı daha temkinli. |
| Klip linki MVP'de | Zaman kalırsa | Grok, Astra |
| Görsel geri alma sayacı | Hotkey | Opus (Astra ve Grok geri almayı tutmak istedi) |
| Sadece sessizlikle kapanma | Tek tuş + sessizlik | Astra |
| — | Kuyruk sınırları, alıntı blocklist'i | Astra, Opus |
| "Ayrılan izleyici dönüyor" sahnesi | Çıkarıldı ya da "quiet chats" diye çerçevelendi | Opus, Grok, Astra |

### Pivot geçmişi
- **Orijinal hâli** (mesajları biriktir, sonra ekrana çıkar) **Meld X AMA Question Queue** ile aynı çekirdek döngüydü; sen "aynı döngü" kararını verdin.
- **Tek pivot hakkı kullanıldı:** sesli cevap + alıntılı makbuz.
- **Pivot sonrası fark** tek kaynaktan (P) kontrol edildi; step 8'de Grok da "baktığım araçlarda yok" dedi. Opus en yakın rakip olarak StreamChat A.I.'ı buldu: bir knowledge base'den LLM ile cevap üretiyor. Checkpoint ise yayıncının gerçekten söylediği sözü aktarıyor.
- **Yedek plan, T1b başarısız olursa "pause trigger":** iş ekranı durur ve mikrofonda konuşma başlarsa "Checkpoint in 3…" geri sayımı. Demoyu kurtarır ama yeniliği kurtarmaz; bu plan seçilirse karta düzgünce yazılmalı.

### Talep ve karşı sinyaller
- **Problem kanıtı setin en iyilerinden:** Streamlabs rehberi elle yapılan versiyonu anlatıyor (odak yayınlarında planlı chat molaları, mod tarafından tutulan soru listesi).
- **Karşı sinyaller:** Bazı izleyiciler beklemiyor; yanlış duyulan bir kelime alıntıya girebilir; ayrılan izleyiciye ulaşma vaadi sınırlı (yukarıda).

### Kitle
İşe gömülü formatlar: kodlama, çizim (Art kategorisi #40, kanal başına yaklaşık 17 izleyici), maker, yemek ve odak gerektiren oyunlar. Her yayında kullanılabilecek bir araç.

### Riskler, test ve yedek plan
| Risk | Önlem |
| --- | --- |
| STT doğruluğu | **T1b:** 10 cevabın en az 9'unda anlam ve kritik kelimeler doğru, alıntı ≤2 sn'de hazır. |
| Düşünme duraklaması kartı erken kapatır | Tek tuş kapanma; sessizlik eşiği ikincil. |
| Yanlış duyulan kelime alıntıya girer | Güven eşiği, blocklist, geri alma hotkey'i. |
| SSS yanlış soruyu eşleştirir | İki eşik; arada dock'ta onay; "daha önce şöyle cevaplandı" dili; `!ask`. |
| "Yine bir soru kuyruğu" algısı | İlk 15 saniyede kartın üstünde beliren kelimeler ve yanındaki thread net görünmeli. |
| **Yedek plan** | Pause trigger. Demo yapılabilir ama yenilik düşer. |

### Step 7: puanlar ve modellerin söyledikleri
| | Innovation | Impact | Tech | Design | Toplam | Risk | Sıra |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Grok | 3 | 4 | 3 | 4 | 14 | Orta | 4 |
| Astra | 4 | 4 | 3 | 4 | 15 | **Yüksek** | 3 |
| Claude | 4 | 4 | 4 | 4 | 16 | Orta | 2 |
| **Ortalama** | **3,7** | **4,0** | **3,3** | **4,0** | **15,0** | | |

- **Grok:** Kuyruktan soru öne çıkarmak bilinen bir döngü; fark, karta yazılan sesli cevap ve alıntılı yanıt.
- **Astra:** Kendinden emin ama yanlış bir transkript, izleyiciye "yayıncının ağzından" yanlış bir cevap gönderebilir.
- **Claude:** "Sesli makbuz olmazsa bu, Meld'in soru kuyruğu."
- Impact'te en güçlü proje (4/4/4). Puanı kısmen Claude puanlayıcısına dayanıyor (Grok + Astra ortalaması 14,5).

### Step 8: serbest incelemeler
- **Opus:** "Dört kart içinde en faydalı ve riski en düşük ML kartı." SSS'yi merkeze almayı önerdi: *"Answer once, out loud. Every later asker gets your own words."* T1 kalır ama T1b geçerse Checkpoint'i seçerdi.
- **Grok:** "Pivot işe yaramış." Ama SSS'yi ve klip linkini koymazdı. Checkpoint'i ancak T1 düşer, T1b geçer ve VAR'ın replay'i T2'de çalışmazsa açardı.
- **Astra:** "Uzun vadeli ürün potansiyelini daha yüksek görüyorum, fakat bu hafta içinde onu farklılaştıran kısmı güvenilir biçimde teslim etmek zor." Odak: "Bir soruya verilen gerçek cevabın doğru alıntıyla geri gitmesi."

### Benim görüşüm
- **En faydalı proje** ve aksan riskinin en az zarar verdiği ML kartı.
- **Ama yarışma için zayıf yanları belirgin:** video sakin, fark ince ve "soru kuyruğu" algısı riski yüksek. Üç model de onu Minefield'ın arkasına koydu.
- **SSS konusunda dürüst not:** İki model karşı. Katmanlı eşik yanlış eşleşme riskini azaltıyor, ama videoda aynı soruyu ikinci kez yazdırmak sahnelenmiş görünebilir (Grok).
- **Bunu seçersen:** Kodlama yayınıyla çek; pause trigger yedeğini karta yaz; ilk 15 saniyede "Meld'den farkı ne?" sorusunu cevapla.

---

## 7. Karşılaştırma matrisi

Karar verildi; bu tablo kayıt için. Minefield sütunu karardan sonraki hâli gösteriyor.

| | Minefield | VAR | Checkpoint |
| --- | --- | --- | --- |
| **Step 7 toplam (ort.)** | **16,3** | 15,0 | 15,0 |
| Innovation | **5,0** (gerçekçi: 4) | 3,0 | 3,7 |
| Impact | 3,0 | 3,0 | **4,0** |
| Tech | 3,3 | **4,0** | 3,3 |
| Design | **5,0** | **5,0** | 4,0 |
| Risk (step 7 medyanı) | Yüksek (karardan sonra Orta) | Orta | Orta |
| **Step 8 tercihi (Opus / Grok / Astra)** | **1 / 1 / 1** | 3 / 2 / 2 | 2 / 3 / 3 |
| Konuşma tanıma gerekli mi | Evet (kelime, akan tanıma) | Hayır | Evet (cümle) |
| Aksan riski | Düşük (turbo test edildi) | Yok | Var (daha az) |
| Ana açık soru | T0 (eğlence) | T2 (OBS tesisatı) | Farkın ince olması |
| İlk 20 saniyedeki "vay" etkisi | **Patlama + kuranın adı** | **Siren + ağır çekim + halka + damga** | Kelimeler karta yazılıyor + alıntı |
| 3 hesapla gerçekçi demo | Evet (arkadaşla daha iyi) | Evet | Evet |
| MVP saati (son hâli) | ~10,5 | ~11 | ~11 |
| Senin ML uzmanlığına uyum | **Yüksek** | Düşük | **Yüksek** |
| "With AI" çerçevesine uyum (Opus) | Var (yerel Whisper) | Yok | Var |
| Ekstra kişi | 1–2 arkadaş (şart gibi) | — | — |
| Kitle | Konuşan her yayın (Just Chatting %14,2) | Rekabetçi oyun, meydan okuma | Odak yayınları (kod, çizim, maker) |
| Kullanım sıklığı | Her yayın (arka planda) | Tartışmalı anlarda, self-VAR | Her yayın |
| 1. gün testleri | T0, T1 (harness ilk koşusu), T4, T5 | T2, T5 | T1b, T5 |

---

## 8. Kararsız kalırsan: ikili karşılaştırmalar

Karar verildi (Minefield); bu bölüm kayıt için.

### Minefield mi VAR mı?
Bu, "yüksek tavan" ile "sağlam taban" arasındaki seçim.

| | Minefield | VAR |
| --- | --- | --- |
| En iyi senaryo | Jüri "bunu hiç görmemiştim" der; Innovation 4–5 ve eşitlik bozmada avantaj. | Jüri "çok eğlenceli, çok iyi paketlenmiş" der. |
| En kötü senaryo | T1 ya da T0 başarısız; ya da jüri "Don't Get Got'un Twitch hâli" der. | Jüri "tekrar + anket" deyip Innovation'a 2–3 verir. |
| Belirsizlik | Yüksek, ama **29 Ekim'de birkaç saatte büyük kısmı çözülür.** | Düşük. |
| Step 8 | Üç modelin birinci tercihi | Grok ve Astra'nın ikinci tercihi |

**Karar kuralı:** T0 ve T1'i koş. İkisi de geçerse Minefield, geçmezse VAR. İkisini yarıştırmak yerine test sonucunun seçmesine izin vermek mantıklı.

### VAR mı Checkpoint mi? (Minefield olmazsa)
- Step 7'de eşitler (15,0). Resmi eşitlik kuralına göre (önce Innovation) Checkpoint öne geçerdi (3,7'ye karşı 3,0). Ama Checkpoint'in puanı kısmen Claude puanlayıcısına dayanıyor; Grok ve Astra'nın ortalamasında Checkpoint 14,5, VAR 15.
- Step 8'de Grok ve Astra VAR'ı, Opus Checkpoint'i öne koydu.
- **VAR'ın lehine:** Minefield'la aynı riski taşımıyor. T1 kaldıysa sorun büyük ihtimalle senin sesinle STT'de; Checkpoint de aynı STT'ye dayanıyor.
- **Checkpoint'in lehine:** Daha faydalı (Impact 4), ML becerine uygun, T1b T1'den kolay.
- **Benim önerim VAR.** Checkpoint'i ancak T1b temiz geçer ve T2 kalırsa açarım (Grok'un kuralı).

---

## 9. 29 Ekim testleri

Minefield seçildiği için T1b (Checkpoint) ve T2 (VAR) kalktı. T1 artık bir geçme şartı değil; harness'in ilk koşusu. **Hiçbir test projeyi değiştirmiyor; sonuçlar kuralları ve ayarları belirliyor.**

| Sıra | Test | Ne ölçer | Hedef | Sonuç kötüyse | Süre |
| --- | --- | --- | --- | --- | --- |
| 1 | **T0: kodsuz oyun** | Discord'da 2 arkadaş kelimelerini (desteden rastgele 6 karttan) üçüncü arkadaşa DM'ler; o, kelimeyi duyunca "BOOM" der. Sen kelimeleri bilmezsin. | Gülüş var; ilk patlama makul sürede geliyor (kaç dakika, not al); **arkadaşlar ikinci tur istiyor**. | Kuralları değiştir: mayın sayısı, kurulma süresi, deste zorluğu. | 20–30 dk |
| 2 | **T1: harness ilk koşusu** | Akan tanıma (turbo, 0,5 sn aralık, iki tahmin onayı); OBS açık ve test yayını sürerken | ≥%80 isabet; 10 dk'da ≤1 yanlış alarm; kelimenin bitişinden medyan ≤1,5 sn, en kötü ≤3 sn; kare düşmesi yok; VRAM kaydı | Tahmin aralığını büyüt (0,75–1 sn), tampon sınırını küçült, sorunlu kelimeleri desteden çıkar. | ~1 sa |
| 3 | T4 | Ekme sayfası: arkadaşın telefonundan cloudflared + Twitch girişi | Uçtan uca bir mayın ekleniyor | Discord + mod yolu | ~1 sa |
| 4 | T5 | Create Clip (`duration=30`) ve marker; **klibi oynatıp** patlamanın içinde olduğunu görmek | Klip doğru anı içeriyor | `duration`'ı ve çağrı zamanını ayarla | ~30 dk |

Toplam yaklaşık 3 saat (önceki planda 4,5–5 saatti). T0 için arkadaşlarla saati şimdiden ayarla.

### T1 nasıl yapılmalı (somut)
1. Windows'ta Python + CUDA ile faster-whisper; model `deepdml/faster-whisper-large-v3-turbo-ct2`. Ayarlar: `language="en"`, hotword yok, `condition_on_previous_text=False`.
2. İlk ~300 kelimelik desteyi hazırla. Arkadaşın içinden 10 kelime seçsin; sen bilme.
3. Üç kayıt al. Bunlar harness'in ilk veri seti olacak:
   - **a.** 10 dk doğal İngilizce; OBS açık ve test yayını sürerken. Arkadaş kelimeleri sohbete sokmaya çalışsın.
   - **b.** 10 dk sessizlik ve arka plan sesi (klavye, nefes, sandalye).
   - **c.** Deste kelimeleri kısa cümleler içinde (300 kelime ~15 dk; zaman yoksa ilk 100).
4. Ölç:
   - Kaç kelime yakalandı (isabet)?
   - Kaç tanesi söylenmediği hâlde yakalandı (yanlış alarm)? Kayıt b'de sıfır olmalı.
   - Kelimenin bitişinden patlamaya kaç saniye geçti (`word_timestamps` ile)? Medyan ve en kötü değer.
   - OBS kare düşürdü mü? VRAM ne kadar?
   - Kayıt c'de kaçırılan ve birbirine karışan kelimeleri desteden çıkar.
5. Kayıtları sakla.

---

## 10. Zaman çizelgesi

| Tarih | Ne |
| --- | --- |
| **28 Ekim (bugün)** | Minefield seçildi, STT modeli belirlendi. Arkadaşlarla T0 ve kayıt saatlerini ayarla. Yapım planı: `docs/plan/minefield.md`. |
| **29 Ekim** | Testler: T0, T1 (harness ilk koşusu), T4, T5 (~3 saat). Twitch hesapları ve ayarları (VOD açık, bot mod). Akşam sonuçlara göre kurallar ve ayarlar. |
| **30 Ekim – 1 Kasım** | Yaklaşık 17,5 saat geliştirme: ortak altyapı (Minefield'ın ihtiyacı kadar) 3,5 saat, MVP ~10,5 saat, ~3,5 saat tampon. Günde yaklaşık 6 saat. |
| **1 Kasım akşamı** | Arkadaşlarla kayıt. |
| **1–2 Kasım** | Video montajı (<3 dk), YouTube'a yükleme, repo README, Devpost açıklaması (dört kriterle eşleşen başlıklar: Innovation / Potential Impact / Technological implementation + Codex / Design). |
| **2 Kasım 23:00 TSİ** | **Hedef: Submit'e bas.** Taslak olarak kaydetmek teslim sayılmıyor. |
| **2 Kasım 14:00 PT** | Resmi son teslim. Kuralların çoğuna göre Türkiye saatiyle **3 Kasım 01:00**; ama `resources.md` kendi içinde çelişiyor ("10 PM London" ve "9 PM UTC" kasımda aynı an değil). Bu yüzden 23:00 hedefi. |

**Dikkat:** Video çekimi ve montaj 17,5 saatin içinde değil. Toplam bütçen 20–25 saatse video için 2,5–7,5 saat kalıyor. MVP ~10,5 saate indiği ve 29 Ekim testleri yaklaşık 2 saat kısaldığı için video için daha çok zaman var. Astra'nın uyarısı: 3,5 saatlik ortak altyapı Twitch'e yeni biri için iyimser.

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
- **Son hâller puanlanmadı.** Step 7 puanları eski kartlara göre.
- **Step 8 (serbest inceleme):** Aynı üç model (Opus ajan, Grok, Astra) finalistleri puan vermeden, web aramasıyla inceledi. Paket yalnızca resmi kuralları, senin koşullarını ve fikirleri içeriyordu; puanlar, sıralama ve benim görüşlerim yoktu. Opus benimle aynı model ailesinden; Grok ve Astra'nın Minefield'da hemfikir olması bu yüzden daha anlamlı.

### Fikirler nereden çıktı
Wave 2'de beş kaynak aynı brief'le toplam 101 fikir üretti: L1 (Claude Opus, ihtiyaç odaklı), L2 (Claude Opus, gösteri odaklı), L3 (Claude Opus, yetenek odaklı), G (GPT 6 Astra, serbest), X (Grok, X'e dayalı).

| Finalist | Ana kaynak | Bağımsız benzerini bulan |
| --- | --- | --- |
| Minefield | L2-1 | Yok, tek kaynak |
| Checkpoint | L1-1; bugünkü sesli cevap hâli step 6'daki pivot (Claude yazdı, sen onayladın) | G-18 (Astra), varyant |
| VAR | L2-11 | Yok, tek kaynak |

Üç finalistin de ana kaynağı Claude. Claude puanlayıcısı bu yüzden kendi fikirlerini puanlamış oldu; Grok ve Astra'nın ortalamasına bakınca sıralama büyük ölçüde aynı kalıyor, en çok etkilenen Checkpoint.

---

## 12. Finale alınmayan ve elenen projeler

**Finalden çıkarılan (28 Ekim, senin kararın, final analizden sonra):**

| Proje | Ne idi | Puan, risk | Neden çıktı |
| --- | --- | --- | --- |
| Tap on the Shoulder | Mikrofon kapalı ya da ses uzak gelince chat'in uyarısı masadaki telefon yüzüne yansır, chat de düzeltmeyi onaylar. | 14,3, Orta | Step 8'de üç model de yapmazdı: "Bunu OBS plugin'leri zaten yapıyor" algısı (Muted Notification 12 bin+ indirme), videoda eğlencenin az olması, yedek telefon ve HTTPS kurulumu. |

**Finale alınmayanlar (28 Ekim, senin kararın; puanlandılar ama finale girmediler):**

| Proje | Ne idi | Puan, risk | Neden geride kaldı |
| --- | --- | --- | --- |
| Hint Jar | İlk kez oynanan oyunlarda izleyiciler ipucunu chat'e yazmak yerine kademeli bir kavanoza mühürler; yayıncı istediği seviyeyi açar. | 14,7, Düşük | En düşük riskli proje, ama kitlesi dar ve teknik olarak sıradan. Kanıt dosyası, backseating'in kurallar ve banlarla zaten çözüldüğünü söylüyor. |
| Studio Audience | Chat tepkileri isimli kahkahalara dönüşür; tepki veren kişi sayısı arttıkça kalabalık büyür. | 13,0, Düşük | Kalabalığın büyümesi 3 test hesabıyla gösterilemiyor; videoda sadece etiketli simülasyon olurdu. |
| Raid Torch | Raid ile kanaldan kanala taşınan meşale; her chat iz bırakır, izi taşıyanlar yeni kanalda parlar. | 12,3, Yüksek | Topluluk zinciri tek kişiyle gösterilemiyor; ikinci canlı kanal ve gerçek raid gerekiyor; talep bulunamadı. |

Ayrıntıları için: [ranking.md](ranking.md) ve bu dokümanın git geçmişindeki önceki sürümler.

**Kanıt adımında elenenler (senin kararın):**

| Proje | Ne idi | Neden elendi |
| --- | --- | --- |
| Previously On | Raid gelince 10 saniyelik TV tarzı "önceki bölümlerde..." özeti | Twitch 2026'da yayın içi yapay zekâ özetlerini ve Recaps'i çıkardı. |
| Photo Booth | `!snap` ile izleyicinin avatarı yayıncıyla aynı polaroide giriyor | StreamUP Polaroid Picture (yaygın) neredeyse aynı şeyi yapıyor. |
| Foley Pit | Chat ses efekti senaryosu yazıyor, yayıncı masadaki objelerle sesi yapıyor, model puanlıyor | Talep bulunamadı; CLAP skorları insan yargısıyla zayıf örtüşüyor. |

---

## 13. Karar ve sonraki adımlar

**Karar (28 Ekim): Minefield.** VAR ve Checkpoint seçilmedi; bölümleri kayıt için duruyor.

**Neden Minefield:**
1. Step 7'de en yüksek toplam (16,3); step 8'de üç modelin de birinci tercihi. Altı değerlendirmenin altısında birinci ya da ikinci.
2. Innovation hem bir kriter hem de eşitlik bozucu; üç finalist içinde en yüksek Innovation onda.
3. ML becerin projenin merkezinde; accuracy harness Tech kriterine sayılarla cevap veriyor.
4. STT riski senin testinle büyük ölçüde kapandı (`large-v3-turbo`, Türkçe ve İngilizce).

**Sonraki adımlar:**
- Yapım planı: `docs/plan/minefield.md`. Sıradaki iş bu.
- ~300 kelimelik desteyi hazırlamak; sesteşleri harness'le elemek.
- 29 Ekim testleri ([bölüm 9](#9-29-ekim-testleri)).
- Arkadaşlarla 29 Ekim T0 ve 1 Kasım kayıt saatlerini kesinleştirmek.
- Açıklamaya Don't Get Got benzerliğini sahiplenen bir cümle yazmak.

**Her durumda:**
- Devpost açıklamasını dört kriterle birebir eşleşen başlıklarla yaz (Opus: değerlendirmede otomatik AI analizi de kullanılabiliyor).
- Videoda Codex'e 20–30 saniye ayır; kod ekranını gezmek yerine harness'in ya da testlerin yakaladığı somut bir hatayı ve düzeltmesini göster.
- 2 Kasım 23:00 TSİ'den önce Submit.

**Son not:** Bu dokümanda puanlar ve modellerin söyledikleri ölçülmüş bilgiler. "Benim görüşüm" bölümleri ve son hâllerin etkisi ise yorum. Final analizin tamamı: [../step8/final-analiz.md](../step8/final-analiz.md). Karar verildi; bu doküman artık kayıt. Yapım ayrıntıları plan dosyasında olacak.
