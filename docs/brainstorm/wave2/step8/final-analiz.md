# Final analiz: 4 finalist, 6 değerlendirme

Hazırlanma tarihi 28 Ekim 2026. Bu doküman iki aşamayı birleştiriyor:

1. **Step 7, puanlı değerlendirme:** Grok, Astra ve Claude (Opus) 7 kartı resmi kriterlere göre 1–5 arası puanladı ([../step7/ranking.md](../step7/ranking.md), [../step7/karar-rehberi.md](../step7/karar-rehberi.md)).
2. **Step 8, serbest inceleme:** Aynı üç model, 4 finalisti ve 12 saatlik eklemeleri serbest formatta, web aramasıyla inceledi ([review-opus.md](review-opus.md), [review-grok.md](review-grok.md), [review-astra.md](review-astra.md)).

Modellerin ne dediği ile benim yorumum ayrı tutuldu. Benim yorumum **"Benim sentezim"** başlıkları altında.

---

## 1. Kısa sonuç

| | Step 7 sırası (G / A / C) | Step 8 tercihi (Opus / Grok / Astra) |
| --- | --- | --- |
| **Minefield** | 1 / 2 / 1 | **1 / 1 / 1** |
| **VAR** | 3 / 4 / 3 | 3 / **2** / **2** |
| **Checkpoint** | 4 / 3 / 2 | **2** / 3 / 3 |
| **Tap on the Shoulder** | 2 / 5 / 5 | Yapma / Yapma / Son sıra |

- **Minefield, altı değerlendirmenin altısında da ilk sıraya ya da ikinci sıraya çıktı. Step 8'de üç model de "bunu yapardım" dedi.** Üçü de aynı iki şartı koydu: konuşma tanıma testi (T1) senin sesinle geçmeli ve arkadaşlarla kısa bir oyun denemesi eğlenceli çıkmalı.
- **Yedek: VAR.** Grok ve Astra ikinci sıraya VAR'ı koydu. Opus Checkpoint'i koydu, çünkü aynı STT altyapısını kullanıyor. Benim önceki eğilimim de VAR'dı.
- **Tap on the Shoulder'ı üç model de yapmazdı.** Gerekçeleri: "Bunu OBS plugin'leri zaten yapıyor" algısı ve videoda eğlencesinin az olması.
- **12 saatlik eklemelerin çoğu kesildi.** Astra'nın genel uyarısı: "12 saati doldurmaya çalışmayın; son eklenen özellikler yeni hata yüzeyleri getiriyor." Grok ve Opus da Minefield paketini sadeleştirdi.

**Bağımsızlık notu:** Üç model step 8'de aynı paketi okudu. Opus benimle aynı model ailesinden ve dört fikrin dördü de Claude kaynaklı. Grok ve Astra'nın Minefield'da hemfikir olması bu yüzden daha anlamlı bir sinyal.

---

## 2. Üç modelin ortak gördükleri (step 8)

| Konu | Opus | Grok | Astra |
| --- | --- | --- | --- |
| Minefield'ı yap | Evet (T0 + T1 şartıyla) | Evet (T1 şartıyla) | Evet (T1 + oynanış denemesi şartıyla) |
| Tap'i yapma | Hiçbir durumda | Her durumda dışarıda | Son sıra, en çok açıklama isteyen |
| `hotwords` yanlış patlama riski | "Prompt öneki; modeli kelimeyi duymaya itiyor" | "Hayalet metin çoğu zaman hotword listesinin kendisi" (PR 731, issue 1356) | "Güvenilir bir keyword detector yerine geçmez" |
| 3 saniyelik gecikme | Komedi için fazla; medyan ≤1,5 sn | Kabul edilebilir (sözce başına tanıma bunun altında kalır) | "Şakanın zamanlamasını bozabilir" |
| Eğlence henüz doğrulanmadı | T0: Discord'da kodsuz 20 dk deneme | Birkaç tur kaydet, en temizini başa koy | "Arkadaşlar 20 dakika sonunda yeni tur istiyor mu?" |
| Bomb Squad (yayınlar arası tablo) | Kes | Kes | Yayın içi sayaçlara indir |
| Hakem itibarı (VAR) | Kes | Kes | Kes ("çoğunluğa katılmayı ödüllendiriyor") |
| VAR beklemede | Tut | Tut (tek alınacak ek) | Tut ve varsayılan yap |
| Son teslim saati | 2 Kasım 23:00 TSİ'den önce gönder | — | "2 Kasım akşamı tamamla" |

**24 saat kuralı:** Opus ve Grok, Bomb Squad ile hakem itibarının kendi koyduğumuz "24 saatten uzun Twitch verisi tutma" kuralıyla çeliştiğini fark etti. Haklılar.

**Son teslim:** `resources.md` hem "10:00 PM London" hem "9:00 PM UTC" diyor; bu ikisi kasımda birbiriyle çelişiyor. Kuralların geri kalanı 22:00 UTC'yi, yani 3 Kasım 01:00 TSİ'yi gösteriyor. Güvenli hedef: **2 Kasım 23:00 TSİ'den önce Submit.**

---

## 3. Modellerin ayrıştığı yerler ve benim kararım

| Konu | Opus | Grok | Astra | Benim sentezim |
| --- | --- | --- | --- | --- |
| **Mayın kelimesi** | Serbest kelime + sıklık bandı + kurallar | **~150 isimlik deste** (pineapple, giraffe...) | **Küçük, test edilmiş kelime havuzu** | **Deste.** İkisi önerdi; üç sorunu birden çözüyor: tanınabilirlik, trol kelimeler, blocklist. Kelime hâlâ gizli, izleyici hâlâ seçiyor. Desteyi harness'te senin sesinle test ederiz. |
| **Tanıma yöntemi** | İki geçiş: hotword'süz geçiş doğrularsa patlama | Kayan pencereyi bırak; VAD sözceyi kessin, bir kez yaz; transkript sadece hotword listesiyse patlatma; en fazla 4 canlı mayın | Benzer sesli kelimeler, sessizlik, OBS açıkken normal konuşma testte olsun | **Grok'un sözce yöntemi + Opus'un ikinci geçişi.** Sözce bitince bir kez yaz; aday eşleşme varsa hotword'süz ikinci geçişle doğrula. Canlı mayın ≤4. Astra'nın negatif örnekleri harness'e girsin. |
| **Fitil** | En iyi ek | Al, "Design kriterinin kendisi" | Ertele: gecikme ekler, moda iş çıkarır | **Al, ama sadece orta güvende ve kısa (≤2 sn).** Yüksek güvende patlama anında olur; Astra'nın gecikme endişesi sadece belirsiz durumlara uygulanır. |
| **Mayın tarama (Sweep)** | Zaman kalırsa | Koyma | İkinci sürüm | **MVP dışı.** |
| **Plant sayfası** | Scope'suz Twitch OAuth + cloudflared | Önce localhost form, T4 geçince OAuth | Sade sayfa | **T4 karar verir.** Arkadaşlar uzaktaysa public URL şart; T4 kalırsa yedek: arkadaşlar kelimelerini Discord'dan mod rolündeki üçüncü kişiye iletir, o da kelimeleri dock'a girer. Sen yine bilmezsin. |
| **Yedek proje** | Checkpoint (aynı STT) | VAR; Checkpoint ancak T2 de kalırsa | VAR | **VAR.** 2'ye 1, ve VAR'ın riski STT'den bağımsız. Bu, Minefield ile aynı riski taşımayan tek seçenek. |
| **Checkpoint'te SSS** (senin kararın) | Merkeze al: "Answer once, out loud" | Koyma: dört cevaplı yayında ya tutmaz ya yanlış tutar | Çıkar: benzer soru aynı soru değil | **Checkpoint seçilmezse önemsiz.** Seçilirse: Opus'un katmanlı hâli (≥0,85 otomatik, 0,70–0,85 dock'ta öneri). 2 model karşı, bunu bil. |
| **VAR telestrator** | Tut, ama sadece yayıncı çizsin | Koyma: senkron kötü görünür | Zaman kalırsa; 1,5 sa iyimser | **Zaman kalırsa.** Önce basit işaretçi (tıklanan yere halka). |
| **`!dud` chat jürisi** (Minefield + VAR-lite) | Önerdi (+0,5 sa) | Fikir birleştirme | İkinci sistem ekleme | **MVP dışı, zaman kalırsa ilk aday.** |
| **12 saati doldur** | 11,5 sa paket | Sade paket | **Doldurma** | **~11 sa paket, artan süre tampona.** |

---

## 4. Modellerin yeni bulguları (kendileri web'den buldu; ben ayrıca doğrulamadım)

| Bulgu | Kim | Ne değişir |
| --- | --- | --- |
| OBS Media Source'ta `speed_percent` değişince kaynak baştan başlıyor | Opus | VAR'da ağır çekim önceden ffmpeg ile hazırlanmalı. Astra: "Tüm replay'i aynı hızda oynatmak da yeter." |
| Create Clip From VOD beta'da `vod_offset` klibi birkaç saniye kaydırıyordu; düzeldiği belli değil | Grok | Canlı demoda normal Create Clip (`duration=30`) kullan; T5'te klibi oynatıp patlamanın içinde olduğunu doğrula. |
| Create Clip varsayılan olarak pencerenin son 30 saniyesini yayınlıyor | Opus, Grok | Klibi patlamadan sonra çok geç çağırma. |
| Twitch Chat History, yeni gelen birine son 50 mesajı ya da son 1 saati gösteriyor | Opus | Checkpoint'in "izleyici dönüp cevabı buluyor" sahnesi sadece sakin chat'te doğru. |
| Threaded reply çevrimdışı bildirim değil | Grok, Astra | Aynı sahne; "Twitch ona haber verdi" denmemeli. |
| "Micron 05" gibi marka + rakam Whisper'ın düştüğü yer | Grok | Checkpoint demosunda düz kelimeli cevaplar. |
| Whisper göndermek doğrulanmış telefon istiyor, günde 40 alıcı sınırı, mesajlar sessizce düşebiliyor | Opus | Minefield'da whisper ile ekme kesin çıktı. |
| Send Chat Message'a `pin` parametresi geldi (Mayıs 2026) | Opus | Sadece Tap için; Tap çıktığı için önemsiz. |
| Yakın rakip olarak Stream Voice Triggers, RobinSystem Word Guess, Chatexto | Grok | Hepsi ya yayıncının kelimesi ya yazılı chat. Minefield'ın farkı duruyor. |

---

## 5. Final öneri

### Seçim: Minefield, yedek VAR

**Neden:**
1. Puanlı değerlendirmede en yüksek toplam (16,3), serbest incelemede üç modelin de birinci tercihi.
2. Innovation hem bir kriter hem de eşitlik bozucu; dört finalist içinde en yüksek Innovation'a sahip.
3. Senin ML becerin projenin tam merkezinde; accuracy harness Tech kriterine sayılarla cevap veriyor.
4. Riski pahalı değil: 29 Ekim'de birkaç saatte ölçülüyor.

**Benzerliği sahiplen (hâlâ geçerli):** Açıklamada ve videoda "Don't Get Got gibi parti oyunlarından ilham aldık; yeni olan, bütün chat'in canlı bir yayıncıya karşı oynaması ve hakemin yerel konuşma tanıma olması" de. Astra da aynı şeyi söylüyor: "Yeni bir oyun türü diye sunmayın; farkı, tetikleyiciyi gizlice izleyicinin seçmesi üzerinden anlatın."

### Minefield MVP'si (son hâli)

| Parça | Saat | Kaynak |
| --- | --- | --- |
| Plant sayfası: Twitch login (scope'suz) + cloudflared, desteden seçim | 1,5 | Kart + Opus + Grok/Astra (deste) |
| STT: sözce bazlı VAD + `small.en`, aday eşleşmede hotword'süz ikinci geçiş, Windows → WSL köprüsü | 2,5 | Grok + Opus |
| Kelime destesi (~150 isim, harness'te test edilmiş) + kurallar (≤4 canlı mayın, aynı kelime iki kişiye verilmez, 30 sn kurulma süresi) | 0,5 | Grok + Astra + Opus |
| "Konuşmayı yaz" dock modu (STT'siz test ve kayıt sigortası) | 0,25 | Opus |
| Accuracy harness (Codex artifact): senin sesin, cümle içi deste kelimeleri, negatif örnekler | 1 | Kart + üç model |
| Overlay: chip'ler, patlama, afiş | 2 | Kart |
| Marker, klip (`duration=30`), DEFUSE, dud'lar + yayın içi sayaçlar | 1,5 | Kart + üç model |
| Fitil (sadece orta güven, ≤2 sn) | 1 | Opus + Grok |
| Cila | 1 | Kart |
| **Toplam** | **~11,25** | |
| Zaman kalırsa sırayla: `!dud` chat jürisi 0,5; Mayın tarama 1 | | |
| **Çıktı:** whisper ile ekme, "Call it", yayınlar arası Bomb Squad, serbest kelime | | |

Toplam yapım: 3,5 ortak altyapı + ~11,25 MVP + ~2,75 tampon ≈ 17,5 saat.

Astra'nın uyarısı: **3,5 saatlik ortak altyapı Twitch'e yeni biri için iyimser.** Minefield'ın ilk patlaması için obs-websocket gerekmiyor; ortak altyapıyı Minefield'ın ihtiyacı kadar kur.

### VAR (yedek) MVP'si

| Değişiklik | Kaynak |
| --- | --- |
| VAR beklemede: tut ve varsayılan yap; videoda hook için auto modu | Üç model |
| Ağır çekim: ffmpeg ile önceden hazırla, ya da tüm replay'i tek hızda oynat | Opus + Astra |
| Replay'i ilk `!var` çağrısının anına sabitle; ikinci çağrı inceleme izni olsun | Astra |
| Oy eşitse ya da oy yoksa "inconclusive"; kişi başına tek oy; incelemeler arası cooldown | Astra |
| Ritüel 25 saniyenin altında, klip `duration=60`; T5'te oynatıp doğrula | Grok |
| Telestrator: zaman kalırsa, önce basit halka | Opus + Astra |
| Hakem itibarı: çıktı | Üç model |
| Kendi "VAR CHECK" tasarımın; FIFA ya da lig görseli yok (kurallar üçüncü taraf markalarını yasaklıyor) | Opus + Grok |

---

## 6. 29 Ekim planı (yenilenmiş)

| Sıra | Test | Ne | Geçme şartı | Süre |
| --- | --- | --- | --- | --- |
| 1 | **T0 (yeni)** | Discord'da kodsuz oyun: 2 arkadaş kelimelerini 3. arkadaşa DM'ler, o kelimeyi duyunca "BOOM" der | Gülüş var, ilk patlama makul sürede geliyor, **arkadaşlar ikinci tur istiyor** | 20–30 dk |
| 2 | **T1 (yenilenmiş)** | Senin sesin, deste kelimeleri cümle içinde, OBS açık; sözce bazlı tanıma + ikinci geçiş; negatif örnekler (benzer sesli kelimeler, sessizlik) | ≥%80 isabet; 10 dakikada ≤1 yanlış alarm; **medyan gecikme ≤1,5 sn**, en kötü durumda ≤3 sn; kare düşmesi yok. Güven skorları kaydedilir (fitil eşiği). | 1–1,5 sa |
| 3 | T4 | Plant sayfası: arkadaşın telefonundan cloudflared + Twitch login | Uçtan uca bir mayın ekleniyor | ~1 sa |
| 4 | T5 | Create Clip (`title`, `duration=30`) ve marker; **klibi oynatıp** patlamanın içinde olduğunu gör | Klip doğru anı içeriyor | ~30 dk |
| 5 | T2 (yedek için) | Replay buffer kaydı → ffmpeg → Media Source ≤5 sn | Replay ekranda | ~1 sa |
| — | T1b | İsteğe bağlı, sadece Checkpoint'e dönme ihtimali için; T1 oturumunda 30 dk | 10 cevabın 9'unda anlam ve kritik kelimeler doğru (Astra'nın ölçütü) | 30 dk |

**Karar ağacı (29 Ekim akşamı):**

```
T0 eğlenceli VE T1 geçti ───────────────► MINEFIELD
        │
  T1 sınırda (isabet iyi, yanlış alarmların güveni düşük)
        │  → fitil bunu gerilime çevirebilir; birlikte bakalım
        │
  T0 eğlenceli değil YA DA T1 kaldı
        │
  T2 geçti ──────────────────────────────► VAR
        │
  T2 kaldı, T1b geçti ───────────────────► CHECKPOINT
        │
  Hepsi kaldı ───────────────────────────► VAR (replay'siz: çağrı, jüri, damga, klip)
```

Tap hiçbir dalda yok.

---

## 7. Video için toplu notlar (üç modelden)

- **0:00 soğuk açılış:** öğle yemeği sohbeti, patlama, chip'te isim. İlk 20 saniye puanın kendisi (Grok).
- **0:08 başlık kartı:** "Chat plants secret words. Say one on stream, it explodes." (Opus)
- **Plant sayfası arkadaşın telefonundan**, kelimenin gizli kaldığını göstermek için (Opus).
- **Yanlış alarm sahnesi:** fitil + DEFUSE, aksilik gag'e dönsün (Opus, Grok).
- **Harness sayıları ekranda ~10 sn:** isabet, yanlış alarm, gecikme (Opus, Grok).
- **Codex bölümü 20–30 sn:** kod ekranını gezmek yerine harness'in yakaladığı somut bir hatayı ve düzeltmeyi göster (Astra, Opus).
- **Gerçek arkadaş seçimleri kullan.** Simülatörü prova için kullan; test hesaplarını gerçek bir kitle gibi sunma (Astra).
- **Birkaç tur kaydet,** en temiz patlamayı başa koy (Grok).
- **Kısa cümleler ve okunaklı altyazı** (Astra).
- **Arkadaşları şimdiden belli saatlere bağla:** 29 Ekim T0 için, 1 Kasım akşamı kayıt için. Darboğaz koddan çok insanlar (Opus).

---

## 8. Açık kalan ve senin karar vereceğin şeyler

1. **Final seçim:** Bu analize göre önerim Minefield (yedek VAR), ama karar 29 Ekim testlerinden sonra senin.
2. **Mayın destesi:** Serbest kelime yerine deste, Minefield'ın "izleyici her şeyi seçebilir" hissini biraz azaltıyor. İki model öneriyor, ben de katılıyorum. Onaylıyor musun?
3. **Checkpoint'te SSS:** Senin kararındı; iki model karşı. Checkpoint seçilmezse konu kapanır.
4. **Karar rehberinin güncellenmesi:** İstersen [../step7/karar-rehberi.md](../step7/karar-rehberi.md) içindeki eklemeleri ve karar ağacını bu analize göre güncellerim.
