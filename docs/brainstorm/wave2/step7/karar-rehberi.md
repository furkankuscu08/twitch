# Karar rehberi: 3 finalist, final seçimi için

Hazırlanma tarihi 28 Ekim 2026; aynı gün iki kez güncellendi: önce 4 finaliste, sonra final analize göre 3 finaliste. Bu doküman, 3 finalist arasından final projeyi seçmen için gereken her şeyi tek yerde topluyor.

**Senin 28 Ekim kararların:**
- **Finalistler:** Minefield, VAR, Checkpoint. Tap on the Shoulder final analizden sonra çıkarıldı; Hint Jar, Studio Audience ve Raid Torch finale alınmamıştı (bkz. [bölüm 12](#12-finale-alınmayan-ve-elenen-projeler)).
- **Kart MVP bütçesi en fazla 12 saat.** Final analizden sonra her projenin MVP'si yaklaşık 11 saate indi; artan süre tampona kaldı. Toplam yapım süresi yaklaşık **17,5 saat**; video bu sürenin dışında.
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
6. Finalistler, önerilen sırayla:
   1. [Minefield: önerilen seçim](#61-minefield-önerilen-seçim)
   2. [VAR: yedek](#62-var-yedek)
   3. [Checkpoint: ikinci yedek](#63-checkpoint-ikinci-yedek)
7. [Karşılaştırma matrisi](#7-karşılaştırma-matrisi)
8. [Kararsız kalırsan: ikili karşılaştırmalar](#8-kararsız-kalırsan-ikili-karşılaştırmalar)
9. [1. gün testleri ve karar ağacı](#9-1-gün-testleri-ve-karar-ağacı)
10. [Zaman çizelgesi](#10-zaman-çizelgesi)
11. [Önceki araştırmalardan önemli bulgular](#11-önceki-araştırmalardan-önemli-bulgular)
12. [Finale alınmayan ve elenen projeler](#12-finale-alınmayan-ve-elenen-projeler)
13. [Benim önerim](#13-benim-önerim)

---

## 1. Tek bakışta özet

| Rol | Proje | Bir cümlede | Step 7 puanı | Step 8 tercihi (Opus / Grok / Astra) | Risk | Ana test | MVP |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Önerilen** | **Minefield** | İzleyiciler gizlice bir desteden "kelime mayını" seçer. Yayıncı o kelimeyi söyleyince ekranda patlar ve ekleyenin adı çıkar. | **16,3** | **1 / 1 / 1** | Yüksek | T0 (eğlence) + T1 (konuşmada kelime yakalama) | ~11,25 sa |
| Yedek | **VAR** | Chat bir an'a itiraz edince (`!var`) futboldaki VAR gibi ağır çekim tekrar, 15 saniyelik chat jürisi, karar damgası ve klip gelir. | **15,0** | 3 / 2 / 2 | Orta | T2 (OBS tekrar) | ~11 sa |
| İkinci yedek | **Checkpoint** | Yayıncı işe gömülüyken mesajlar biriktirilir. Molada yayıncı sesli cevap verir, cevap izleyiciye alıntı olarak gider; tekrar eden sorulara bot eski cevabı verir. | **15,0** | 2 / 3 / 3 | Orta | T1b (cevabı yazıya dökme) | ~11 sa |

Step 7 puanı, 4 kriterin (her biri 1–5) üç puanlayıcıya göre ortalamasının toplamıdır; en fazla 20 olabilir. Puanlar eski kartlara göre verildi; son hâller yeniden puanlanmadı.

**Kısaca durum:**
- **Minefield en yenilikçi ve en izlenesi proje.** Step 7'de üç model Innovation ve Design'a 5 verdi; step 8'de üçü de "bunu yapardım" dedi. Şartları: T1 senin sesinle geçmeli ve T0'da arkadaşlarla oyun eğlenceli çıkmalı. "Birine kelime söyletme" türü parti oyunlarından biliniyor, bu yüzden gerçekçi Innovation beklentisi 4.
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
| Bizim kısıtlarımız | Yaklaşık 17,5 saat geliştirme (3,5 ortak + ~11 MVP + kalan tampon); 1 yayıncı + 3 test hesabı; videoda ticari oyun ya da müzik yok; Twitch içeriği en fazla 24 saat tutuluyor. |

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
| **Checkpoint** | Hayır | — | 3 test hesabı chat simülatörüyle mesaj atar. Arkadaş gerçek soru sorarsa daha doğal görünür; SSS sahnesi için ikinci bir kişinin aynı soruyu sorması gerekir. |
| **VAR** | Hayır | — | `!var` ve oyları simülatör ya da arkadaşlar yazar. Telestrator çizimini sen ya da mod hesabı dock'tan yaparsın. |

**Test hesapları için telefon numarası:**
- Twitch hesabı genelde e-postayla açılabiliyor; Twitch ek olarak telefon doğrulaması isteyebilir. Kaç hesabın aynı numaraya bağlanabileceği **doğrulanmadı**. Hesapları açarken göreceğiz; senin numaran ve 1–2 arkadaşın numarası büyük ihtimalle yeter.
- Kanal sahibi sensin; "chat için telefon doğrulaması iste" ayarını kapalı tutabilirsin.
- Whisper (DM) ile mesaj göndermek telefon doğrulaması istiyor ama bu hiçbir projenin MVP'sinde yok, sadece stretch hedeflerde.

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

**Bütçe hesabı (final analizden sonra):** 3,5 saat ortak altyapı + ~11 saat proje MVP'si + kalan tampon (~3 saat) = **yaklaşık 17,5 saat**. Astra'nın uyarısı: 3,5 saatlik ortak altyapı Twitch'e yeni biri için iyimser. Seçilen projenin ihtiyacı olmayan parçaları baştan kurma; örneğin Minefield'ın ilk patlaması için obs-websocket gerekmiyor.

**MVP'ler nasıl son hâline geldi:** Önce her projeye 12 saate kadar eklemeler önerdim. Sonra üç model bu eklemeleri serbestçe inceledi. Astra'nın genel uyarısı belirleyici oldu: *"12 saatlik MVP alanını doldurma hedefi... son eklenen özellikler tamamlanmış ürün hissinden çok yeni hata yüzeyleri getiriyor."* Bu yüzden eklemelerin bir kısmı kesildi, MVP'ler ~11 saate indi ve artan süre tampona kaldı. Ayrıntılar her projenin "Önceki plandan ne değişti" tablosunda.

---

## 6.1 Minefield: önerilen seçim

Puan (step 7): **16,3**, risk Yüksek. Step 8'de üç modelin de birinci tercihi.

### Ne?
İzleyiciler gizlice "kelime mayınları" eker. Yayıncı sıradan konuşurken o kelimeyi söylerse ekranda patlama olur ve mayını ekleyenin adı çıkar.

### Somut örnek
> Sen yayında öğle yemeğinden bahsediyorsun. Bo 6 dakika önce gizlice "PINEAPPLE" kelimesini ekmiş. Chat'te Bo soruyor: "worst pizza topping?" Sen "pineapple on pizza is—" derken **BOOM**: ekran sallanır, afiş çıkar: *"Bo's mine: PINEAPPLE (planted 6 min ago)"*. Bo chat'e "GOT HIM 😈" yazar.

### Nasıl çalışır (son hâli)
1. İzleyici `!mine` yazar. Bot ona ekme sayfasının linkini verir. Sayfa Twitch girişi ister (hiçbir izin istemeyen, sadece kimlik doğrulayan bir giriş; sayfada "We only see your Twitch name" yazar).
2. İzleyici kelimesini **yaklaşık 150 kelimelik bir desteden** seçer: pineapple, giraffe, spaghetti, keyboard gibi somut, komik isimler. Kimse seçimi görmez. Kurallar:
   - izleyici başına aynı anda 1 mayın, toplamda en fazla **4 canlı mayın**;
   - aynı kelime iki kişiye verilmez;
   - mayın eklendikten **30 saniye sonra** aktif olur ("kurulma" süresi).
3. Overlay'de mayın çipleri görünür: sadece sahiplerin adları, kelimeler yok.
4. İzleyiciler sohbeti kendi kelimelerine doğru çekmeye çalışır. Asıl oyun bu "tuzak kurma" kısmı.
5. Yerel STT yayıncının mikrofonunu dinler:
   - VAD bir konuşma parçası (sözce) bitince onu keser, faster-whisper `small.en` o parçayı **bir kez** yazıya döker.
   - Metinde canlı bir mayın kelimesi varsa, aynı ses parçası **hotword'süz ikinci bir geçişle** doğrulanır.
   - Transkript sadece mayın kelimelerinden ibaretse ya da sesin enerjisi düşükse patlama olmaz (hayalet kelime koruması).
6. **Güvene göre iki aşama:**
   - **Yüksek güven** (iki geçiş de kelimeyi buldu): anında patlama, afiş, stream marker.
   - **Orta güven** (sadece hotword'lü geçiş buldu): ekranda en fazla 2 saniyelik bir **fitil** yanar, sonra patlar. Mod ya da yayıncı bu sırada fitili kesebilir.
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
| 1:00 | Belirsiz bir tanıma: fitil yanar, mod keser, "false alarm". Aksilik gag'e döner. |
| 1:25 | Yayın sonu: dud'lar açılır ("Cy'ın 'giraffe'ı hiç patlamadı"). |
| 1:45 | Kaputun altı: yerel STT, ses kaydedilmiyor; harness tablosu ~10 sn ekranda (isabet, yanlış alarm, gecikme). |
| 2:10 | Codex bölümü (20–30 sn): harness'in yakaladığı somut bir hata ve düzeltmesi. |
| 2:40 | Kapanış. |

**Not:** Birkaç tur kaydet, en temiz patlamayı başa koy. Kelimeleri gerçekten arkadaşların seçsin; sen bilme.

### Teknik detay
- **Mimari:**
  - **STT süreci (Windows'ta yerel Python):** mikrofon → VAD (sözce sınırı) → faster-whisper `small.en` (GPU) → aday eşleşmede ikinci geçiş → eşleşme olayı.
  - **Köprü:** Windows süreci eşleşmeyi WSL'deki FastAPI'ye HTTP POST ile gönderir.
  - **Eşleşme:** metin normalize edilir (küçük harf, noktalama silinir, çoğul eki atılır) ve canlı mayınlarla tam kelime olarak karşılaştırılır. Aynı sözce iki kez patlamaz.
  - **Patlama:** FastAPI → WebSocket → OBS overlay. Minefield'ın ilk patlaması için obs-websocket gerekmez.
- **Twitch:**
  - EventSub `channel.chat.message`, Send Chat Message;
  - Create Stream Marker (`channel:manage:broadcast`, VOD açık olmalı);
  - Create Clip (`clips:edit`, `title`, `duration=30`). Klip asenkron ve hazır olması bir dakikayı bulabilir; T5'te klibi oynatıp patlamanın içinde olduğunu doğrula.
  - Ekme sayfası için Twitch girişi ve herkese açık URL (`cloudflared` quick tunnel; bilgisayar uykuya geçerse tünel kapanır).
- **Gecikme hedefi:** medyan ≤1,5 sn, en kötü durumda ≤3 sn. Overlay yayına yerelde eklendiği için yayın gecikmesi kelimeyi ve patlamayı aynı miktarda kaydırır; yalnızca STT gecikmesi önemli.
- **Saatler:**

| Parça | Saat |
| --- | --- |
| Ekme sayfası: scope'suz Twitch girişi + cloudflared + desteden seçim | 1,5 |
| STT: sözce bazlı VAD + `small.en` + ikinci geçiş + Windows → WSL köprüsü | 2,5 |
| Kelime destesi (~150 isim, harness'te test edilmiş) + kurallar | 0,5 |
| "Konuşmayı yaz" dock modu | 0,25 |
| Doğruluk harness'i (Codex artifact) | 1 |
| Overlay: çipler, patlama, afiş | 2 |
| Marker, klip, DEFUSE, dud'lar + yayın içi sayaçlar | 1,5 |
| Fitil (sadece orta güven, ≤2 sn) | 1 |
| Cila | 1 |
| **MVP toplamı** | **~11,25** |
| Zaman kalırsa sırayla: `!dud` chat jürisi (fitil yanarken chat 10 sn oy verir) 0,5; mayın tarama 1 | — |
| **Çıkarıldı:** serbest kelime girişi, yayınlar arası Bomb Squad tablosu, whisper ile ekme, "Call it" modu | — |

- **Codex artifact:** Doğruluk harness'i. Senin sesinle kaydedilmiş konuşmaları (deste kelimeleri cümle içinde, benzer sesli kelimeler, sessizlik, doğal duraksamalar, OBS açıkken normal konuşma) yakalayıcıdan geçirir; isabet, yanlış alarm ve gecikmeyi raporlar. Fitil eşiği de bu verilerle ayarlanır.

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
- **Teknik karşı sinyal:** faster-whisper `hotwords` sessizlikte kelime uydurabiliyor (issue 1356, PR 731). Sözce bazlı tanıma, ikinci geçiş ve ≤4 mayın bunun için.

### Kitle
Yayıncının konuştuğu her yayın: Just Chatting (%14,2), IRL (%1,8) ve konuşkan oyun yayınları. Oyun gerekmediği için demo oyunu da gerekmiyor.

### Riskler, test ve yedek plan
| Risk | Ne kadar ciddi | Önlem |
| --- | --- | --- |
| **STT kelimeyi kaçırır ya da olmayan kelimeyi yakalar** | **Proje bunun üzerine kurulu.** | T1 (yenilenmiş): senin sesin, deste kelimeleri cümle içinde; ≥%80 isabet, 10 dakikada ≤1 yanlış alarm, medyan gecikme ≤1,5 sn. Sözce bazlı tanıma + ikinci geçiş + fitil + DEFUSE. |
| **Oyun eğlenceli değil** | Yüksek, henüz ölçülmedi | **T0:** Discord'da kodsuz 20 dakika. Ölçüt: arkadaşlar ikinci tur istiyor mu? |
| Aksanlı İngilizce | Orta | T1'i kendi sesinle yap; deste kelimeleri harness'te senin sesinle test edilir. Gerekirse `medium.en`. |
| Ekme sayfası | Düşük–orta | T4. Kalırsa: arkadaşlar kelimelerini Discord'dan mod rolündeki üçüncü kişiye iletir, o da dock'a girer. Sen yine bilmezsin. |
| "Don't Get Got'un Twitch hâli" algısı | Orta | Benzerliği sahiplen; ilk 20 saniyede "izleyici gizlice seçti + sohbetle tuzak + kuranın adı" görünsün. |
| Arkadaşların zamanı | Orta | Darboğaz koddan çok insanlar. Arkadaşları şimdiden bağla: 29 Ekim T0, 1 Kasım akşamı kayıt. |
| **Yedek plan** | — | Proje içinde yedek yok. Testler kötü çıkarsa **VAR**'a geç (bkz. karar ağacı). |

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
- **Yarışmayı kazanabilecek tek proje bu.** Altı değerlendirmenin altısında da birinci ya da ikinci; step 8'de üç model de "bunu yapardım" dedi.
- **Sentezle risk azaldı ama gitmedi.** Deste ve sözce bazlı tanıma, tanıma işini çok kolaylaştırıyor: rastgele bir kelimeyi değil, önceden test edilmiş 150 kelimeden birini arıyoruz. Yine de T1 senin sesinle geçmeli.
- **En büyük açık soru artık eğlence.** T0 bunu 20 dakikada, kod yazmadan ölçüyor. Arkadaşlar ikinci tur istemiyorsa Minefield'ı zorlama.
- **Destenin bedeli:** "İzleyici her şeyi seçebilir" hissi biraz azalıyor. Ama gizlilik ve tuzak kurma, yani oyunun özü aynı kalıyor.

---

## 6.2 VAR: yedek

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

## 6.3 Checkpoint: ikinci yedek

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

| | Minefield | VAR | Checkpoint |
| --- | --- | --- | --- |
| **Step 7 toplam (ort.)** | **16,3** | 15,0 | 15,0 |
| Innovation | **5,0** (gerçekçi: 4) | 3,0 | 3,7 |
| Impact | 3,0 | 3,0 | **4,0** |
| Tech | 3,3 | **4,0** | 3,3 |
| Design | **5,0** | **5,0** | 4,0 |
| Risk (medyan) | Yüksek | Orta | Orta |
| **Step 8 tercihi (Opus / Grok / Astra)** | **1 / 1 / 1** | 3 / 2 / 2 | 2 / 3 / 3 |
| Konuşma tanıma gerekli mi | Evet (kelime) | Hayır | Evet (cümle) |
| Aksan riski | Var (deste ile azaldı) | Yok | Var (daha az) |
| Ana açık soru | T1 ve T0 (eğlence) | T2 (OBS tesisatı) | Farkın ince olması |
| İlk 20 saniyedeki "vay" etkisi | **Patlama + kuranın adı** | **Siren + ağır çekim + halka + damga** | Kelimeler karta yazılıyor + alıntı |
| 3 hesapla gerçekçi demo | Evet (arkadaşla daha iyi) | Evet | Evet |
| MVP saati (son hâli) | ~11,25 | ~11 | ~11 |
| Senin ML uzmanlığına uyum | **Yüksek** | Düşük | **Yüksek** |
| "With AI" çerçevesine uyum (Opus) | Var (yerel Whisper) | Yok | Var |
| Ekstra kişi | 1–2 arkadaş (şart gibi) | — | — |
| Kitle | Konuşan her yayın (Just Chatting %14,2) | Rekabetçi oyun, meydan okuma | Odak yayınları (kod, çizim, maker) |
| Kullanım sıklığı | Her yayın (arka planda) | Tartışmalı anlarda, self-VAR | Her yayın |
| 1. gün testleri | T0, T1, T4, T5 | T2, T5 | T1b, T5 |

---

## 8. Kararsız kalırsan: ikili karşılaştırmalar

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

## 9. 1. gün testleri ve karar ağacı

### Hangi test, ne kadar sürer, neyi ölçer
| Sıra | Test | Proje | Ne ölçer | Geçme şartı | Süre |
| --- | --- | --- | --- | --- | --- |
| 1 | **T0 (yeni)** | Minefield | Kodsuz oyun: Discord'da 2 arkadaş kelimelerini üçüncü arkadaşa DM'ler; o, kelimeyi duyunca "BOOM" der. Sen kelimeleri bilmezsin. | Gülüş var, ilk patlama makul sürede geliyor, **arkadaşlar ikinci tur istiyor**. | 20–30 dk |
| 2 | **T1 (yenilenmiş)** | Minefield | Senin sesin, deste kelimeleri cümle içinde, OBS açık; sözce bazlı tanıma + ikinci geçiş; negatif örnekler (benzer sesli kelimeler, sessizlik, doğal konuşma) | ≥%80 isabet; 10 dakikada ≤1 yanlış alarm; **medyan gecikme ≤1,5 sn**, en kötü ≤3 sn; kare düşmesi yok. Güven skorları kaydedilir. | 1–1,5 sa |
| 3 | T1b | Checkpoint | Aynı oturumda 10 senaryolu cevap | 10 cevabın en az 9'unda **anlam ve kritik kelimeler doğru**; alıntı ≤2 sn'de hazır | 30 dk |
| 4 | T4 | Minefield | Ekme sayfası: arkadaşın telefonundan cloudflared + Twitch girişi | Uçtan uca bir mayın ekleniyor | ~1 sa |
| 5 | T5 | Hepsi | Create Clip (`title`, `duration`) ve marker; **klibi oynatıp** doğru anı içerdiğini görmek; threaded reply | Klip doğru anı içeriyor | ~30 dk |
| 6 | T2 | VAR | Replay buffer kaydı → ffmpeg → Media Source | Komuttan sonra ≤5 sn'de tekrar ekranda | ~1 sa |

Toplam yaklaşık 4,5–5 saat. T0 için arkadaşlarla saati şimdiden ayarla.

### T1 nasıl yapılmalı (somut)
1. Windows'ta Python + CUDA ile faster-whisper kur; `small.en` ile başla, gerekirse `medium.en` dene.
2. İlk ~150 kelimelik desteyi hazırla (somut, komik isimler). Arkadaşın içinden 10 kelime seçsin; sen bilme.
3. **10 dakika doğal İngilizce konuş:** OBS açık, yayın test modunda. Arkadaş kelimeleri sohbete sokmaya çalışsın.
4. Ölç:
   - Kaç kelime yakalandı (isabet)?
   - Kaç tanesi söylenmediği halde yakalandı (yanlış alarm)? İkinci geçiş bunları eledi mi?
   - Söyleyişten tetiklenmeye kaç saniye geçti? Medyan ve en kötü değer.
   - OBS kare düşürdü mü?
   - Her yakalamanın güven skoru: yanlış alarmların skorları doğru yakalamalarınkinden ayrışıyor mu? (Fitil eşiği bununla ayarlanır.)
5. Aynı oturumda T1b: 10 senaryolu cevabı oku; her birinde anlam ve kritik kelimeler doğru mu, alıntı kaç saniyede hazır?
6. Kayıtları sakla: harness'in ilk veri seti bunlar olacak.

### Karar ağacı
```
T0 eğlenceli VE T1 geçti ─────────────────► MINEFIELD
        │
  T1 sınırda (isabet iyi, yanlış alarmların güveni düşük)
        │  → fitil bunu gerilime çevirebilir; birlikte bakalım
        │
  T0 eğlenceli değil YA DA T1 kaldı
        │
  T2 geçti ────────────────────────────────► VAR
        │
  T2 kaldı, T1b geçti ─────────────────────► CHECKPOINT
        │
  Hepsi kaldı ─────────────────────────────► VAR (replay'siz: çağrı, jüri, damga, klip)
```

---

## 10. Zaman çizelgesi

| Tarih | Ne |
| --- | --- |
| **28 Ekim (bugün)** | Finalistler 3 projeye indi; final analiz yapıldı. Arkadaşlarla T0 ve kayıt saatlerini ayarla. |
| **29 Ekim** | 1. gün testleri: T0, T1 + T1b, T4, T5, T2 (~4,5–5 saat). Akşam final seçimi. Twitch hesapları ve ayarları (VOD açık, bot mod). |
| **30 Ekim – 1 Kasım** | Yaklaşık 17,5 saat geliştirme: ortak altyapı (seçilen projenin ihtiyacı kadar) 3,5 saat, MVP ~11 saat, kalan tampon. Günde yaklaşık 6 saat. |
| **1 Kasım akşamı** | Arkadaşlarla kayıt (Minefield seçilirse). |
| **1–2 Kasım** | Video montajı (<3 dk), YouTube'a yükleme, repo README, Devpost açıklaması (dört kriterle eşleşen başlıklar: Innovation / Potential Impact / Technological implementation + Codex / Design). |
| **2 Kasım 23:00 TSİ** | **Hedef: Submit'e bas.** Taslak olarak kaydetmek teslim sayılmıyor. |
| **2 Kasım 14:00 PT** | Resmi son teslim. Kuralların çoğuna göre Türkiye saatiyle **3 Kasım 01:00**; ama `resources.md` kendi içinde çelişiyor ("10 PM London" ve "9 PM UTC" kasımda aynı an değil). Bu yüzden 23:00 hedefi. |

**Dikkat:** Video çekimi ve montaj 17,5 saatin içinde değil. Toplam bütçen 20–25 saatse video için 2,5–7,5 saat kalıyor. MVP'ler 12 yerine ~11 saat olduğu için tampon biraz büyüdü; bu süre video için de kullanılabilir. Astra'nın uyarısı: 3,5 saatlik ortak altyapı Twitch'e yeni biri için iyimser.

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

## 13. Benim önerim

**Seçim: Minefield. Yedek: VAR. İkinci yedek: Checkpoint.** Karar şekli: sezgiyle değil, 29 Ekim testleriyle ([karar ağacı](#karar-ağacı)).

**Neden Minefield:**
1. Step 7'de en yüksek toplam (16,3); step 8'de üç modelin de birinci tercihi. Altı değerlendirmenin altısında birinci ya da ikinci.
2. Innovation hem bir kriter hem de eşitlik bozucu; üç finalist içinde en yüksek Innovation onda.
3. ML becerin projenin merkezinde; accuracy harness Tech kriterine sayılarla cevap veriyor.
4. Riski pahalı değil: T0 ve T1, 29 Ekim'de birkaç saatte ölçülüyor.
5. Sentezle risk azaldı: deste ve sözce bazlı tanıma, tanıma işini rastgele kelimeden test edilmiş 150 kelimeye indiriyor.

**Neden yedek VAR:** Minefield'la aynı riski (STT) taşımayan tek seçenek; videosu en kolay anlaşılanı; Grok ve Astra'nın ikinci tercihi.

**Final seçilince yapılacaklar:**
- **Minefield:** ~150 kelimelik desteyi hazırlamak ve harness'te senin sesinle test etmek; T1 verisiyle fitil eşiğini ayarlamak; arkadaşlarla 1 Kasım kaydını kesinleştirmek; açıklamaya Don't Get Got benzerliğini sahiplenen bir cümle yazmak.
- **VAR:** ffmpeg ön-render hattını T2'de doğrulamak; stinger, siren ve damga animasyonuna özen göstermek; PROVE IT Devpost linkini elle kontrol etmek.
- **Checkpoint:** Pause trigger yedeğini karta yazmak; SSS eşiklerini 20–30 soru çiftiyle ayarlamak; kodlama yayınıyla çekmek.

**Her durumda:**
- Devpost açıklamasını dört kriterle birebir eşleşen başlıklarla yaz (Opus: değerlendirmede otomatik AI analizi de kullanılabiliyor).
- Videoda Codex'e 20–30 saniye ayır; kod ekranını gezmek yerine harness'in ya da testlerin yakaladığı somut bir hatayı ve düzeltmesini göster.
- 2 Kasım 23:00 TSİ'den önce Submit.

**Son not:** Bu dokümanda puanlar ve modellerin söyledikleri ölçülmüş bilgiler. "Benim görüşüm" bölümleri ve son hâllerin etkisi ise yorum. Final analizin tamamı: [../step8/final-analiz.md](../step8/final-analiz.md). Karar senin.
