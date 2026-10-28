# Finalistler ve 12 saatlik MVP paketleri

Ayrıntılı hâli [karar-rehberi.md](karar-rehberi.md) içinde, her projenin "12 saatlik eklemeler" kısımlarında.

28 Ekim 2026. Kullanıcının kararları ve benim önerilerim. Öneriler kullanıcı onaylayana kadar taslaktır.

## Kullanıcının kararları

- **Finalistler:** Minefield, Checkpoint, VAR, Tap on the Shoulder.
- **Checkpoint'e SSS özelliği eklenecek.**
- **Kart MVP bütçesi 9,5 saatten 12 saate çıktı.** Toplam yapım: ortak altyapı 3,5 + MVP 12 + tampon ≥2 = **yaklaşık 17,5 saat** (önceden 15). Video bu sürenin dışında.

**Not:** Puanlar ([ranking.md](ranking.md)) eski kartlara göre verildi. Aşağıdaki eklemeler yeniden puanlanmadı. Hangi kritere yarayacakları benim tahminim.

## Seçim ilkesi

Her ekleme şu üç şarttan en az birini karşılamalı:
1. O kartın puanlayıcıların söylediği zayıflığını kapatmalı.
2. 3 dakikalık videoya yeni ve anlaşılır bir sahne eklemeli.
3. Aracı "bir kez denenen oyuncak" olmaktan çıkarıp "her yayında açık kalan araç" yapmalı (Impact).

Sadece cila olan, videoda görünmeyen ya da yeni bir dış bağımlılık getiren eklemeler alınmadı.

---

## Checkpoint: 9 → 12 saat

| Ekleme | Saat | Neyi çözüyor |
| --- | --- | --- |
| **SSS: aynı soru tekrar gelince eski cevap** (kullanıcının kararı) | 1,5 | Impact ve Innovation; videoda ikinci bir "vay" anı |
| **Makbuzda cevabın klip linki** (eski stretch) | 1 | Yayından çıkmış izleyici cevabı izleyebilir; makbuzun değeri artar |
| **Gönderimden önce geri alma penceresi** | 0,5 | Astra'nın "yayıncının ağzından yanlış cevap" eleştirisi |
| **Toplam** | **12** | |

**SSS nasıl çalışır:**
1. Her cevaplanan kart saklanır: soru, kesinleşmiş transkript, güven skoru, zaman, klip linki.
2. Yeni bir chat mesajı soru gibiyse (`?` içeriyor ya da soru kalıbıyla başlıyor), saklanan sorularla karşılaştırılır. Benzerlik küçük bir embedding modeliyle (`all-MiniLM-L6-v2`, GPU'da milisaniyeler) ve kosinüs eşiğiyle (başlangıç 0,85, kayıtlı örneklerle ayarlanır) ölçülür.
3. Eşleşme varsa ve eski cevabın güveni yüksekse bot, thread içinde yanıt verir:
   *"📌 Answered earlier (12:04): 'It's a Micron 05, it doesn't bleed' ▶ clip · type !ask to ask anyway"*
4. Focus modundaysa bu mesaj kristal olmaz; dock'ta "auto-answered" sayacına eklenir.
5. Riskler:
   - **Yanlış eşleşme:** Eşik yüksek tutulur. Yanıtın sözü "yayıncı böyle dedi" değil "daha önce şöyle cevaplandı" olur. `!ask` ile izleyici soruyu yine kuyruğa sokabilir.
   - **Doğru eşleşme, eski cevap:** SSS sadece aynı yayın içinde çalışır; MVP'de yayınlar arası hafıza yok.
6. **Video sahnesi:** 20 dakika sonra Mehmet "what pen is that?" yazar, 1 saniyede bot Ana'ya verilen cevabı alıntılar. Yayıncı çizmeye devam eder.

**Geri alma penceresi:** Kart kapanınca alıntı 3 saniye sonra gönderiliyordu. Bu 3 saniye dock'ta görünür bir sayaç olur, "undo" tuşu makbuzu alıntısız düz makbuza çevirir. Kodu zaten var olan gecikmenin üstüne biniyor.

**Hâlâ açık:** B yedek planı (pause trigger) karta düzgünce yazılmalı. Bu dokümantasyon işi; saat bütçesinden yemiyor.

---

## Minefield: 9,5 → 12 saat

| Ekleme | Saat | Neyi çözüyor |
| --- | --- | --- |
| **Fitil: iki aşamalı patlama** | 1 | Grok'un "sahte bir patlama ürünün ta kendisi" eleştirisi; T1 riskini yumuşatır |
| **Mayın tarama (Sweep): yayıncının karşı hamlesi** | 1 | Innovation: "Don't Get Got'un Twitch hâli" algısının ötesine geçer; oyun iki taraflı olur |
| **Bomb Squad tablosu (yayınlar arası)** | 0,5 | Impact: her yayın yeniden oynanır, sadakat |
| **Toplam** | **12** | |

**Fitil:** STT eşleşmesinin güveni yüksekse anında BOOM. Orta güvendeyse ekranda yanan bir fitil ve 3 saniyelik tık-tık sesi çıkar, sonra patlar. Mod ya da yayıncı bu sırada fitili keserse "false alarm" damgası basılır. Faydası: emin olmadığımız tanımalar, yanlış patlama yerine **gerilim** olarak görünür. Eşik ayarı doğruluk harness'iyle yapılır; bu, senin ML tarafın. Var olan DEFUSE'u değiştirmez, öne alır.

**Mayın tarama:** Yayıncının yayın başına 3 tarama hakkı olur. Bir tuzaktan şüphelenince kelimeyi **söylemeden** dock'a yazar (söylerse patlar; videoda bunun kendisi komik). Kelime canlı bir mayınla eşleşirse mayın "SWEPT" olur ve ekleyenin çipi söner. Yanlışsa tarama hakkı gider. Bu, yayıncıya oyunda bir rol verir ve Don't Get Got'taki suçlama kuralının canlı yayındaki karşılığıdır.

**Bomb Squad tablosu:** SQLite ile yayınlar arası: en çok patlatan, en uzun yaşayan mayın, yayıncının tarama isabeti. Yayın sonu dud ekranına eklenir.

**Bilerek alınmayanlar:**
- **Whisper ile mayın ekleme** (eski stretch): T4'ü (herkese açık sayfa) atlatabilirdi, ama Twitch'te fısıltı göndermek için hesapta telefon doğrulaması gerekebilir (doğrulanmadı). Sadece T4 başarısız olursa yedek olarak düşünülmeli.
- **"Call it" modu** (1,5 saat): bütçeye sığıyor ama Sweep + Fitil videoya daha çok katkı veriyor.

---

## VAR: 8,5 → 12 saat

| Ekleme | Saat | Neyi çözüyor |
| --- | --- | --- |
| **Yayıncı kontrolü: VAR beklemede** | 1 | Grok'un ve kanıt dosyasının en büyük karşı sinyali: yayıncı tekrarın ne zaman oynayacağını seçmek istiyor |
| **Donmuş karede çizim (telestrator)** | 1,5 | Design: spor yayını hissi; videoda en akılda kalan kare |
| **Hakem itibarı** | 1 | Impact: haftalık kullanım; jüriye katılmanın bir anlamı olur |
| **Toplam** | **12** | |

**VAR beklemede:** Çağrı eşiği dolunca tekrar hemen oynamaz. Ekranın köşesinde "🟨 VAR PENDING (2 calls)" çıkar. Yayıncı uygun bir anda tuşa basar ve inceleme başlar. Ya da "auto" modunda eskisi gibi hemen başlar. Eşik dolunca replay buffer hemen dosyaya kaydedilir, yani bekleme buffer'ın 60 saniyesiyle sınırlı değil. Bekleme 2 dakikayı geçerse uyarı çıkar, 5 dakikada çağrı düşer.

**Telestrator:** Ağır çekimin sonunda kare donar. Mod ya da yayıncı dock'ta fareyle çizgi ya da daire çizer ("top çizginin dışında"). Çizim WebSocket ile overlay'deki bir canvas'a gider. Karar damgası bu karenin üstüne iner.

**Hakem itibarı:** VAR çağıranın çağrısı haklı çıktıysa ("call overturned") ve jüride çoğunlukla oy verdiyse puan kazanır. Yayın sonunda "Referee of the night" anılır. Puanlar SQLite ile yayınlar arasında saklanır.

**Bilerek alınmayanlar:**
- **İkinci kamera açısı** (eski stretch, 1 saat): replay buffer sadece program çıktısını kaydediyor. İkinci açı için ayrı bir kayıt (Source Record eklentisi) ve telefon kamerası kurulumu gerekir; 1 saat iyimser.
- **Yayın sonu VAR derlemesi** (ffmpeg ile klipleri birleştirme): güzel ama Twitch klipleri zaten var. Bütçe kalırsa ilk aday bu.

---

## Tap on the Shoulder: 9 → 12 saat

| Ekleme | Saat | Neyi çözüyor |
| --- | --- | --- |
| **Sakin mod MVP'ye** (eski stretch) | 1 | Astra'nın "günlük kullanım için en güçlü argüman MVP dışında" eleştirisi |
| **Soundcheck: yayın başında ses kontrolü** | 1 | Arızaları beklemeden her yayında kullanılır (G-2 Soundcheck Relay'den) |
| **Siyah veya donmuş ekran algılama** | 0,5 | "OBS sinyali" tarafını sesten görüntüye genişletir |
| **Yayın sonu sorun raporu** | 0,5 | Impact: kayıt, yardım edenlere teşekkür |
| **Toplam** | **12** | |

**Soundcheck:** Yayıncı yayın başında "soundcheck" tuşuna basar. Telefon yüzü "SOUNDCHECK A" gösterir, yayıncı konuşur. Bot chat'e sorar: *"Test A: mic vs game? !heard good / quiet / loud"*. Aynı sırada `InputVolumeMeters` ile mikrofon ve oyun seviyeleri ölçülür. Chat'in cevabı ve ölçüm birlikte yüzde gösterilir: "chat: quiet · meter: −28 dB → raise mic". Böylece araç sadece arıza anında değil, her yayının ilk dakikasında da çalışır.

**Siyah veya donmuş ekran:** `GetSourceScreenshot` saniyede 1 kez küçük bir kare alır. Ortalama parlaklık çok düşükse "BLACK SCREEN", 10 saniye boyunca hiç değişmiyorsa "FROZEN?" uyarısı çıkar. Chat'teki "black screen" ya da "frozen" şikâyetiyle aynı anda gelirse "chat + OBS" olarak gösterilir.

**Sorun raporu:** Yayın sonunda dock'ta ve chat'te: "3 issues · avg fix 42 s · first reporter: @ana".

**Not:** Bu kart puanlarda 5. sırada (14,3) ve iki puanlayıcı "akılda kalmaz" dedi. Eklemeler Impact'i güçlendirir, ama Innovation'ı (3,0) pek değiştirmez.

---

## 1. gün testleri (29 Ekim), dört finaliste göre

| Test | Kartlar | Ne kontrol edilir |
| --- | --- | --- |
| **T1 + T1b** (tek oturum) | Minefield, Checkpoint | Senin sesinle STT: hit, yanlış alarm, gecikme; cevap okunabilirliği |
| **T2** | VAR, Tap | OBS: replay buffer + Media Source (+ ağır çekim); mute olayı ve sessizlik eşiği |
| **T4** | Minefield, Tap | Twitch girişli sayfa herkese açık URL'de; Tap için telefonda HTTPS + Wake Lock |
| **T5** | Hepsi | API kontrolleri: marker, klip, threaded reply |

T2 ve T4 VAR ile Tap'i aynı anda test ettiği için 4. finalist 1. güne çok az ek iş getiriyor.
