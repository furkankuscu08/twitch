# Minefield: yapım planı

Hazırlanma tarihi 28 Ekim 2026; aynı gün bağımsız incelemeye göre güncellendi, sadeleştirildi ([bölüm 13](#13-sadeleştirmeler-28-ekim)) ve STT kararı (D3: Deepgram) işlendi. Bu doküman **senin** için: kapsam, takvim, kararlar, testler, video ve teslim.

Codex'in okuyacağı teknik kısımlar İngilizce olarak repo kökünde:
- [`AGENTS.md`](../../AGENTS.md): Codex'in her oturumda kendiliğinden okuduğu kurallar.
- [`SPEC.md`](../../SPEC.md): mimari, olay şemaları, oyun kuralları, iş paketleri ve kabul kriterleri.

Diğer kaynaklar:
- Bağımsız inceleme: [review-opus.md](review-opus.md). Ondan neleri aldığım: [bölüm 12](#12-bağımsız-inceleme-ne-alındı-ne-alınmadı).
- Kararın arka planı: [karar-rehberi.md](../brainstorm/wave2/step7/karar-rehberi.md) (bölüm 6.1).
- STT araştırmaları: [stt-cloud-options.md](stt-cloud-options.md) (bulut seçenekleri; D3 buna dayanıyor) ve [stt-research.md](stt-research.md) (yerel turbo; artık kullanılmıyor, arşiv).

---

## 1. Tek cümle ve kesilemezler

**"Chat plants secret words. Say one on stream, it explodes."**

Zaman biterse her şey kesilebilir, ama bu üçü kesilemez (Grok):
1. Overlay'de **kelimesiz** mayın çipi; sadece sahibinin adı görünür.
2. Gerçekten söylenmiş bir kelimede **gerçek** bir patlama.
3. Patlamada mayını **ekleyenin adı**.

---

## 2. Kapsam

**MVP:**
- **Ekme:**
  - Ekme sayfası: bütün desteden rastgele 6 kart; seçilen kart için `!mine KOD` komutu ve kopyala düğmesi.
  - Overlay'de ekme adresi ve QR kodu.
  - 30 sn kurulma; en fazla 4 canlı mayın.
- **Tanıma ve oyun:**
  - Akan STT (Deepgram Flux) + iki ardışık tahmin onayı.
  - Kıvılcım / BOOM / "fıss" ve afiş.
  - Afişte **patlama makbuzu**: yayıncının son ~8 kelimesi, tuzak kelime vurgulu; diğer deste kelimeleri `•••` ile maskeli.
  - Patlamadan sonraki 10 sn içinde "False alarm" (`!defuse` ya da dock): patlama sayılmaz.
  - Patlama mesajı hemen.
  - Tur sonunda overlay'de dud'lar ve patlama sayısı; chat'te tek bir **tur özeti** mesajı.
- **Araçlar:**
  - "Konuşmayı yaz" modu.
  - Doğruluk harness'i (tekrar oynatma ve etiket yardımcısıyla).
  - Tek komutla başlatma.
  - README'de anahtarsız demo yolu ("konuşmayı yaz" + kayıtlı tahminlerle `replay`).

**Zaman kalırsa:** Yok. Özellik dondurmadan sonra artan zaman videoya gider.

**Yapılmayacak:**
- serbest kelime girişi;
- yayınlar arası skor tablosu;
- whisper (DM);
- "Call it" modu;
- `!dud` chat itirazı, Türkçe deste, mayın tarama (inceleme sonrası kesildi);
- chat simülatörü, `!mines` komutu, ekme sayfasında hız sınırı, "en hızlı patlama" istatistiği (sadeleştirmede kesildi);
- veritabanı (her şey bellekte; 24 saat kuralı);
- yerel STT motoru (faster-whisper) ve yerel yedek; STT sağlayıcıları arasında ayrı bir karşılaştırma testi (D3);
- Twitch Extension;
- stream marker, otomatik klip ve klip linki (D15; yayıncı Twitch'in kendi Clip düğmesini kullanabilir).

---

## 3. Mimari (özet)

Ayrıntılar `SPEC.md`'de. Kısaca:

```
[Windows] mikrofon ─► mic sayfası (Chrome sekmesi, localhost:8000/mic) ─PCM/WebSocket─►
[WSL]     STT motoru ─ses─► Deepgram Flux (AB uç noktası) ─~0,25 sn'de bir ara sonuç─► motor ─tahminler─►
[WSL]     oyun sunucusu (FastAPI): mayınlar, eşleştirme, Twitch
              ├─► overlay  (OBS browser source)
              ├─► dock     (OBS içi kontrol paneli)
              ├─► Twitch   (EventSub chat, chat mesajı)
              └─► ekme sayfası (ayrı port; cloudflared ile sadece bu port dışarı açılır)
```

**İki karar ([bölüm 10](#10-karar-günlüğü)):**
1. **D3: STT bulutta, Deepgram Flux; mikrofon Chrome'daki bir sayfadan.**
   - Chrome'da açık duran `/mic` sayfası sesi WSL'deki motora yollar; motor Deepgram'a akıtır ve gelen ara sonuçları tahmine çevirir. Harness ve canlı oyun aynı motoru kullanır.
   - Neden: GPU'yu oyun ve NVENC ile paylaşmak yok, CUDA kurulumu yok, ~2–3 saat daha az iş. Flux ~0,25 sn'de bir kelime zamanlı ve güven skorlu ara sonuç veriyor; iki tahmin onayına çok uygun. Pitch'te "GPU gerekmez, her yayıncı kullanabilir" (Impact).
   - Ayrı karşılaştırma testi yapılmaz. Ses beğenilmezse aynı anahtarla Nova-3'e (`--backend nova3`) ya da başka bir Deepgram modeline geçilir. Yerel motor yazılmaz.
   - Gecikme tek bir saatle ölçülür: motorun kendi saati, çünkü Windows ve WSL saatleri uykudan sonra kayabiliyor.
   - Ayrıntılar ve kaynaklar: [stt-cloud-options.md](stt-cloud-options.md).
2. **D4: Ekme sayfasında Twitch girişi yerine chat kodu** (onaylandı, 28 Ekim).
   - İzleyici kartını seçer, sayfa `!mine K7QF` komutunu kopyala düğmesiyle gösterir; izleyici bunu chat'e yapıştırır.
   - Kazanç:
     - OAuth yönlendirme adresi gerekmez (quick tunnel adresi her açılışta değişiyor).
     - Telefonda Twitch uygulamasından açılan link uygulama içi tarayıcıda açılır. Orada Twitch girişi baştan şifre ve 2FA isterdi; kodla buna gerek yok.
     - Kod kelimeyi ele vermez.
   - İnceleme sonrası eklenenler: komut büyük/küçük harfe ve boşluklara toleranslı; kod 5 dakika geçerli; overlay'de QR.

---

## 4. Kilometre taşları

Önce uçtan uca çalışan bir iskelet yapılır, sonra parçalar gerçekleriyle değiştirilir. Böylece her kilometre taşının sonunda gösterilebilir bir demo olur.

| Kilometre taşı | Sonunda ne çalışıyor | İş paketleri |
| --- | --- | --- |
| **M0: Hazırlık** (29 Ekim) | Deste v0; Twitch token'ları alınabiliyor (T5 bu araçla yapılır). | WP7, WP8 |
| **M1: İskelet** | Dock'a yazılan cümle → overlay'de BOOM. Mayınlar dock'tan debug olarak eklenir. Twitch ve STT yok. | WP1, WP2, WP3 (temel), WP4 |
| **M2: Ses** | Konuşunca BOOM; kıvılcım ve "fıss" çalışıyor; harness raporu çıkıyor (**T1**). | WP5, WP6 |
| **M3: Twitch** | Chat komutları, bot cevapları, patlama ve tur özeti mesajları. | WP9, WP10 |
| **M4: İzleyici** | Telefondan (mobil veriyle) mayın ekleniyor (**T4**). | WP11 |
| **M5: Cila ve teslim hazırlığı** | Animasyonlar, sesler, dud gösterimi, başlatma betikleri, README. **Özellik dondurma.** | WP3 (tam), WP13, WP14 |

Twitch yetkilendirmesi (WP8) inceleme önerisiyle öne alındı. Senin için en bilinmeyen kısım STT değil, Twitch: hesap doğrulama, sadece canlı yayında çalışan API'ler ve token'lar.

---

## 5. İş paketleri ve saatler

Kabul kriterleri `SPEC.md` §8'de. Codex'e görevler bu kimliklerle verilir ("WP5'i yap").

| WP | İş | Saat | Kilometre taşı |
| --- | --- | --- | --- |
| WP7 | Deste: ~120 isim, yazım biçimleri, sesteş eleme | 0,5 | M0 |
| WP8 | Twitch kimlik: device code flow, bot (+ 1 test hesabı) token'ları, yenileme | 1 | M0 |
| WP1 | Çekirdek: normalizasyon, deste, oyun durumu, eşleştirici + birim testleri | 1 | M1 |
| WP2 | Sunucu: FastAPI, WebSocket yayını, dock/overlay uç noktaları, "konuşmayı yaz", motor nabzı | 0,5 | M1 |
| WP3 | Overlay: çipler, kurulma halkası, kıvılcım/fıss, BOOM, afiş ve makbuz, sabit "FALSE ALARM" damgası, dud'lar, QR, gecikme rozeti | 2,25 | M1 → M5 |
| WP4 | Dock: tur başlat/bitir, durum ışıkları, mayın listesi (kelimesiz), "False alarm", yazı kutusu | 0,5 | M1 |
| WP5 | STT: mic sayfası (Chrome, 16 kHz, yeniden bağlanma) + Deepgram motoru (Flux, Nova-3 yedeği, yeniden bağlanma, kayıtlı mesajlarla testler) | 1,5 | M2 |
| WP6 | Harness: `run`, `replay` (kayıtlı tahminlerden saniyeler içinde), `label-assist`, rapor | 1,5 | M2 |
| WP9 | EventSub chat + komutlar + chat mesajı | 0,5 | M3 |
| WP10 | Patlama mesajı, False alarm mesajı, tur özeti mesajı | 0,25 | M3 |
| WP11 | Ekme sayfası (ayrı port) + kod akışı + kopyala düğmesi + cloudflared | 1,5 | M4 |
| WP13 | Cila ve prova | 1 | M5 |
| WP14 | Başlatma betiği, İngilizce README (Deepgram anahtarı, anahtarsız demo yolu), demo günü listesi | 0,75 | M5 |
| | **Toplam** | **12,75** | |
| | Tampon | 2,5 | |
| | **Yapım toplamı** | **~15,25** | |

İnceleme sonrası değişen saatler:
- WP3: 2,5 → 2 (geri sarma animasyonu yerine sabit damga).
- WP6: 1 → 1,5 (tekrar oynatma ve etiket yardımcısı). Etiketleme için harcayacağın zamanı ~1 saat azaltır.
- WP12 (simülatör): 1 → 0,5, sadeleştirmede tamamen çıktı.
- Yeni WP14: 1.
- Tampon: 3,5 → 2,5. Önceki planda görünmeyen işler artık iş paketlerinde ya da 29 Ekim'de.
- Sadeleştirmede: WP7 0,75 → 0,5 (120 kelime), WP10 0,75 → 0,5 (pencere durumu yok), WP14 1 → 0,75 (CPU modu test edilmiyor).
- Marker ve klip çıkınca (D15): WP10 0,5 → 0,25; WP3 2 → 2,25 (makbuz). Toplam değişmedi; kazanç senin zamanında: T5 kısaldı, canlı yayında hata ayıklama yok.
- STT kararında (D3): WP5 2 → 1,5 (yerel model, VAD ve uydurma süzgeçleri yok; Windows relay yerine Chrome sayfası). CPU modu tamamen çıktı.

---

## 6. Takvim

| Gün | Saat (insan) | Ne |
| --- | --- | --- |
| **28 Ekim (bugün)** | — | Plan, `AGENTS.md`, `SPEC.md`, bağımsız inceleme, Twitch/Deepgram/OBS hazırlığı. 1–2 arkadaşla 1 Kasım 20:00 kaydını ayarla. |
| **29 Ekim** | ~2,25 | **Kurulum ve veri günü** (aşağıda). Codex ana thread'i açılır: WP7 + WP8. |
| **30 Ekim** | ~6 | M1 + M2. Akşam **T1**. |
| **31 Ekim** | ~4,5 | M3 + M4. Kendi telefonunla **T4**. |
| **1 Kasım** | ~4 + akşam 2 | M5. Öğlen prova (2 tur). **17:00 özellik dondurma.** 20:00 arkadaşlarla kayıt ([bölüm 9](#arkadaşlar-sadece-kayıt-gecesi)). |
| **2 Kasım** | ~4 | Video montajı, Devpost metni, repo paylaşımı. **23:00 TSİ Submit.** |

### 29 Ekim ayrıntısı

T1 ve T4 kod gerektirdiği için 30 ve 31 Ekim'e kaydı. 29 Ekim'de bunlar yapılır:

| Sıra | İş | Süre |
| --- | --- | --- |
| 1 | ✅ Twitch hesapları ve uygulama kaydı (28 Ekim'de yapıldı; ayrıntı aşağıda) | — |
| 2 | Codex ana thread'i ([bölüm 8](#8-codex-kullanımı); OBS "Codex" sahnesi 28 Ekim'de hazırlandı). Thread'i aç; **kayda bas**, ilk mesaj (`/plan`), sonuç gelince kaydı durdur (an 1), session ID'yi bölüm 8'e yaz. Sonra WP7 (deste) ve WP8 (auth). WP8 bitince **bot ve test hesabı** için device code girişini yap: bundan sonra Twitch testlerini Codex kendisi koşar. | 45 dk (senin zamanın) |
| 3 | ✅ Deepgram hesabı, API anahtarı `.env`'de, AB uç noktasında Flux denendi (28 Ekim'de yapıldı) | — |
| 4 | **T5:** WP8 aracıyla bot token'ını al, curl ile kanala bir chat mesajı gönder (canlı yayın gerekmez). WSL'de `python -m http.server 8000` çalıştır; OBS browser source'ta ve Windows Chrome'da `http://localhost:8000` açılıyor mu bak (Windows → WSL). | 20 dk |
| 5 | Deste v0'ı gözden geçir | 20 dk |
| 6 | Kayıt (a): 15 dk İngilizce serbest konuşma, yayındaymış gibi (chat'i okur gibi, bir konu anlatarak). Deste kelimelerini bilerek söyleme. | 15 dk |
| 7 | Kayıt (b): 10 dk sessizlik ve arka plan (klavye, nefes, sandalye). Kayıt (c): deste kelimeleri kısa cümlelerde; etiketleri sonra `label-assist` çıkarır. | 30 dk |

**Twitch hesapları ve uygulama kaydı:**
- Bot hesabı + 1 test hesabı açılır, e-postaları doğrulanır. Arkadaşlar kendi hesaplarını kullanır.
- Yayıncı hesabında 2FA açılır: geliştirici konsolunda uygulama kaydı için gerekiyor (birden çok kılavuz böyle diyor; resmî sayfa bulunamadı).
- Uygulama Public client olarak kaydedilir. Form bir Redirect URL isterse `http://localhost:3000` girilir.
- Bot'a mod yetkisi verilir.
- Kanal ayarları: VOD saklama açık (kayıt gecesi yedeği); chat'te e-posta/telefon doğrulama şartı test hesaplarını engellemeyecek şekilde.

**Kayıt formatı:** WAV, mono, sadece senin mikrofonun. Dosyalar `data/recordings/` altına (git'e girmez).

### İnsan saati
28 Ekim'de yapılan hazırlık ~1,5 + 29 Ekim 2,25 + 30 Ekim–1 Kasım 14,5 (6 + 4,5 + 4) + kayıt 2 + montaj ve teslim 4 ≈ **24,25 saat**. 29 Ekim sabahından itibaren kalan ≈ **22,75 saat**; tampon (2,5) kullanılmazsa ~20,25. T0 çıkınca 15 dk (kayıt (a) tek başına 15 dk), marker ve klip çıkınca ~1 saat kazanıldı (T5 45 → 20 dk, 31 Ekim'de canlı yayın denemesi yok).

**Aktif emek ve bekleme (D16).** Codex'in kendi doğrulayabildiği işler ona bırakılır; sende sadece onun yapamadıkları kalır. Bu açıdan kalan ~22,75 saatin ~15,5'i aktif emek, ~7'si Codex çalışırken bekleme. Bekleme, Codex'in hatalarının düzeltildiği yer (fiilî tampon); iş yolunda giderse kayıtlara, OBS'e ve montaj hazırlığına kayar.

| Gün | Plandaki | Aktif | Bekleme | Senin işin |
| --- | --- | --- | --- | --- |
| 29 Ekim | 2,25 | ~2,25 | — | `/plan`, device code girişleri, T5, deste, kayıtlar |
| 30 Ekim | 6 | ~3 | ~3 | Mic sayfasında konuşmak, etiket düzeltme, overlay'e ilk bakış, T1 kararları |
| 31 Ekim | 4,5 | ~1,75 | ~2,75 | OBS kaynakları ve dock, telefonla T4 |
| 1 Kasım | 6 | ~4,75 | ~1,25 | Overlay cilası (zevk), prova, kayıt gecesi |
| 2 Kasım | 4 | ~3,75 | — | Montajda zaman damgalarını seçmek, Devpost'u düzeltmek, Submit |

**Codex'e tamamen bırakılanlar:** WP1, WP2, WP6 ve T1 ayar döngüsü (`run` ve `replay`'i kendisi koşar), WP7, WP9 ve WP10'un canlı testleri (test hesabıyla komut gönderir), WP14; overlay, dock ve ekme sayfasının ekran görüntülerini Playwright ile kendisi alıp kontrol eder; sesleri WebAudio ile sentezler (ses dosyası ve lisans işi yok); montajın mekanik kısmı (`ffmpeg` betiği) ve Devpost taslağı.

Sıkışırsan kesilecekler, sırasıyla:
1. dud gösteriminin animasyonu (düz liste);
2. overlay'deki QR (bot cevabındaki link yeter);
3. tur özeti chat mesajı (overlay'deki dud gösterimi yeter).

---

## 7. Testler ve ölçütler

| Test | Ne zaman | Hedef | Kötüyse |
| --- | --- | --- | --- |
| **T5** bot token'ı ve erişim | 29 Ekim | Bot'un chat mesajı kanalda görünüyor; OBS'ten ve Chrome'dan WSL'deki sunucuya erişiliyor | Scope'lar ve bot'un mod yetkisi kontrol edilir; erişim yoksa `wsl --shutdown` ve tekrar |
| **T1** harness ilk koşusu | 30 Ekim akşam | ≥%80 isabet · **4 canlı mayına göre** 10 dk'da ≤1 yanlış alarm (kayıt b'de 0) · kelime bitişinden medyan ≤1,5 sn, en kötü ≤3 sn · OBS açıkken kare düşmesi yok · kelime bazında "fıss" oranı | Önce `replay` ile eşleştirici ayarı (`CONFIRM_N` 2 → 3, `MIN_WORD_PROB`); tanıma kötüyse `--backend nova3` ile aynı kayıtlar tekrar; sorunlu kelimeler desteden çıkar |
| **T4** ekme sayfası | 31 Ekim | Kendi telefonundan, Wi-Fi kapalı (mobil veri), `minefield_test` hesabıyla uçtan uca bir mayın | Kayıt gecesine kadar düzelt; olmazsa kayıtta Discord + mod yolu: arkadaş kelimeyi mod rolündeki kişiye iletir, o da dock'a girer |
| Prova | 1 Kasım öğlen | "Konuşmayı yaz" + debug ekleme: 2 tur kesintisiz. Kurallar (D8) burada kesinleşir. | Dondurmadan önce düzelt, yoksa kes. İlk patlama 5 dk'dan uzun sürecek gibiyse desteye yaygın kelimeler eklenir. |

**Yanlış alarm notu:** Harness bütün desteyi (~120 kelime) kurulu sayar. Gerçek oyunda en fazla 4 mayın var, yani harness'in ham yanlış alarm sayısı oyundakinin ~30 katı. Hedef bu yüzden 4 mayına göre normalize edilmiş sayıya uygulanır.

Harness raporu (`reports/`) videoda ~10 saniye görünecek. Bu yüzden rapor okunaklı bir tablo olmalı.

---

## 8. Codex kullanımı

Ayrıntılı araştırma: [codex-usage.md](codex-usage.md). Bu bölüm ondan süzülmüş karardır; ikisi çelişirse bu bölüm geçerli.

**Kurallar ne istiyor** (`docs/competition/` ile doğrulandı):
- işin çoğunun yapıldığı **Codex thread'inin session ID'si**;
- Devpost açıklamasında **Codex'i nasıl kullandığın**;
- videoda **Codex ile nasıl yapıldığının görüntüsü**.

Puan:
- Codex, Tech kriterinin yarısı ("how well is it built, and how well does it use Codex?"). Yani doğrudan ~2,5/20.
- Ama Stage One'da "required developer tools" geçti/kaldı eşiği de var.
- Jüri büyük olasılıkla video ve açıklamaya bakıyor; asıl kanıt oraya konur.

### Kurulum (29 Ekim, ~20 dk)
- **Codex masaüstü uygulaması** (Windows), ajan WSL'de çalışıyor (`runCodexInWindowsSubsystemForLinux = true`). Bu repo uygulamada zaten "trusted". Config ve oturumlar Windows tarafında: `C:\Users\furkan\.codex` (WSL'den `/mnt/c/Users/furkan/.codex`). WSL'deki `~/.codex` CLI'a ait, uygulama onu kullanmıyor.
- **Ağ ve web:** `uv sync` ve dokümanlar için ağ ve canlı web araması açık olmalı. Uygulamanın config'ine (`C:\Users\furkan\.codex\config.toml`) eklenir, sonra uygulama yeniden başlatılır:

  ```toml
  web_search = "live"

  [sandbox_workspace_write]
  network_access = true
  ```
- **Model:** uygulamada `gpt-6.1-sol`, reasoning şu an `xhigh`. Rutin WP'lerde `medium`, zor işlerde `high`; `xhigh` limiti çok hızlı yer. Astra sadece takıldığında.
- **Session ID:**
  - Uygulamada thread'in ID'sini göster ya da `/status` dene.
  - Görünmezse: thread'in oturum dosyası `C:\Users\furkan\.codex\sessions\YYYY\MM\DD\rollout-<zaman>-<UUID>.jsonl`; UUID dosya adının sonundaki kısım. İlk mesajdan sonra en yeni dosya ana thread'indir.
  - **SESSION ID: `01a188b5-edca-79f3-9ee7-1b1d7198d173`** (ana thread "Minefield build", 29 Ekim).
- **GitHub code review:** chatgpt.com/codex/settings/code-review'da repo bağlanır, otomatik inceleme kapalı. 15 dk'da çalışmazsa bırakılır.

### Ana thread: "Minefield build"
- Bütün WP'ler ve birleştirmeler burada. Kod sadece Codex'te yazılır; Claude plan, spec ve inceleme için kullanılır.
- Ana thread'de **`/new` ve `/fork` kullanılmaz**, ID değişir. Her gün aynı thread'e uygulamanın kenar çubuğundan dönülür; yeni chat açılmaz.
- Kısa sorular için `/side`, ana bağlam şişmesin.
- Yan thread ya da alt ajan: varsayılan olarak yok. Sadece ana thread bir şey beklerken. Darboğaz senin dikkatin, alt ajanlar da limiti hızlı yiyor.
- Ana thread bozulursa yeni bir thread açılır. Teslimde işin çoğunun olduğu ID verilir, diğeri README'de anılır.

### İlk mesaj (29 Ekim)
```
/plan Read AGENTS.md and SPEC.md. Summarize the architecture in 10 lines, then list
anything unclear, contradictory or risky to implement. Then plan WP7 and WP8.
Do not write code yet.
```
Codex'in spec'i eleştirmesi gerçek bir katkı ve videonun ilk Codex sahnesi. Haklı bulduğun düzeltmeleri SPEC'e işlet.

### Her WP için aynı döngü
Kilometre taşı içindeki WP'ler **zincirlenir** (D16); Codex her birini bitirip commit'ler, düzeltemediği ilk hatada durur. Senin başında beklemen gerekmez.
```
Do M1: WP1, WP2, WP4, then WP3 (basic), per SPEC.md §8, following the Workflow in AGENTS.md
(tests first, verify it yourself, commit each WP, stop at the first failure you cannot fix).
End with one report and a short checklist of anything only I can do.
```
Zincir bitince her WP için `/review` (2–3 dk) ve sonda bir `/compact`. Tek WP isteniyorsa:
1. `Do WP<n> per SPEC.md §8. Write failing tests from the acceptance list first, run them, then implement.`
2. Testler kırmızı → kod → `uv run pytest` + `uv run ruff check` → yeşil.
3. `/review`. Önemli bulgu varsa düzelttir.
4. `WP<n>: ...` commit'i.
5. `/compact`. WP ortasında compaction'a izin verme. Kalıcı hafıza AGENTS.md, SPEC.md ve git log.

### Görünür Codex anları (videonun Codex bölümü bunlardan kurulur)
| # | An | Ne zaman | Nasıl |
| --- | --- | --- | --- |
| 1 | Spec eleştirisi ve "Do WP1" | 29–30 Ekim | Yukarıdaki ilk mesaj; WP1 istemi |
| 2 | Testler kırmızı → yeşil | 30 Ekim (WP1) | Döngünün 2. adımı |
| 3 | **Harness döngüsü (asıl hikâye)** | 30 Ekim akşam, T1 | Aşağıdaki istem; önce/sonra raporları `reports/` altında |
| 4 | Codex'in dev.twitch.tv'yi kontrol etmesi | 31 Ekim (WP9/WP10) | Web araması açık; AGENTS.md zaten istiyor |
| 5 | Codex'in overlay'i kendi ekran görüntüsüyle düzeltmesi | 30 Ekim–1 Kasım (WP3) | `scripts/shoot.py overlay` → Codex PNG'ye bakar → düzeltir; gerekirse OBS'teki görüntü de verilir |
| 6 | PR'da `@codex review` | M1 ve M3 sonunda (2 PR) | Kilometre taşı dalı → PR → yorum |
| 7 | Session ID | 2 Kasım | `/status` ya da status line |

Harness döngüsü istemi:
```
Run `uv run python -m minefield.harness run --wav data/recordings/c.wav --labels data/recordings/c.labels.json --deck deck/en.json --save-hyps data/hyps/c.jsonl`.
Read the report. Propose at most 3 changes to minefield/core/config.py or deck variants,
verify each with `harness replay`, keep only changes that improve hits without raising
normalized false alarms, and commit the new report under reports/.
```

Canlı testler (`pytest -m live`) ve harness koşuları Codex'in kendi işi; sana sadece cihaz ve zevk gerektirenler kalır (AGENTS.md, Workflow).

Kullanılmayacaklar: Codex'i ürünün içinde çalıştırmak (yapay görünür), Codex cloud görevleri (kayıtlar ve token'lar yerelde), skills, hooks, MCP.

### Ekran kaydı
**Ne:**
- Sadece Codex uygulamasının penceresi.
- Masaüstünün tamamı değil: e-posta, bildirim ya da başka bir pencere görünmesin.

**OBS kurulumu (bir kez, ~10 dk):**
- Ayrı bir **"Codex" sahnesi** oluştur; içinde Codex uygulaması için tek bir **Window Capture** kaynağı olsun.
- Uygulama: koyu tema, kod fontu 16 pt (şu an 14), pencere büyük. 1080p'de satırlar okunmalı.
- Kayıt ayarları: mp4, 1080p, 30 fps, NVENC. Kayıtlar kısa olduğu için çökmeye dayanıklı format gerekmiyor.
- Audio Mixer'da mikrofon ve masaüstü sesi Codex kayıtlarında kapalı. **Yayından önce tekrar aç.**
- Yayın yaparken Codex kaydı alınmaz. Yayın ve oyun kayıtları ayrı bir iş (bölüm 9).

**Ne zaman:** Sadece yukarıdaki 7 an kaydedilir; sürekli kayıt yok.
- O anın mesajını göndermeden hemen önce kayda bas, sonuç gelince durdur. Her kayıt ~5–20 dk; montajda 3–8 sn'si kullanılır.
- Kayıt bitince dosya adını ve ne olduğunu aşağıdaki tabloya bir satırla yaz.
- Beklenmedik iyi bir an olursa (ör. Codex ciddi bir hatayı yakaladı) kaydı yoksa saatini tabloya yaz; yedek yoldan alınır.

**Yedek: thread geçmişi.** Codex uygulaması ana thread'in tüm geçmişini saklıyor. 2 Kasım'da thread'i baştan sona kaydırırken 1–2 dk'lık bir kayıt alınır. Kaçırılan anların görüntüsü buradan çıkar; bu da gerçek oturumun görüntüsü.

**Gizlilik:**
- `.env` ve `data/tokens.json` ekranda açılmaz; Codex'ten bunları göstermesini isteme.
- Bir anahtar ya da token ekrana gelirse saatini not et; montajda bulanıklaştırılır ya da kesilir. Gerekirse anahtar yenilenir.

**Tarayıcıda olanlar:**
- PR'daki `@codex review` yorumu ve harness raporu tablosu için tarayıcı penceresi ayrı bir kaynakla kaydedilir.
- Kısa bir ekran kaydı (5–10 sn) yeter.

**Montajda:**
- Codex bölümü 25–30 sn.
- Her an 3–8 sn, 4–8× hızlandırılmış, ilgili satıra yakınlaştırılmış.
- Altyazı bölüm 9'daki çekim listesinde.
- Sahne kurgusu yok: gösterilen her şey gerçek oturumdan.

**"Codex anları" kaydı:**

| Zaman | Ne oldu | Kayıt dosyası |
| --- | --- | --- |
| | | |

### Açıklama ve README
- README'de "How this was built with Codex" bölümü (WP14). Taslak: [codex-usage.md](codex-usage.md) bölüm 5. Sadece gerçekten yapılanlar kalır.
- **Dürüstlük cümlesi:** "Planning and spec review with another AI assistant; all code was written in Codex." SSS başka araçlara izin veriyor; açık olmak güven verir.
- Devpost'ta Tech başlığının altında aynı maddelerin 3–4 cümlelik özeti ve harness önce/sonra sayıları.

---

## 9. Video ve teslim

### Çekim listesi (taslak; 1 Kasım akşamı)
| Zaman | Sahne | Gerekenler |
| --- | --- | --- |
| 0:00 | Soğuk açılış: sohbet, "pineapple" BOOM, afiş ve makbuz (yayıncının cümlesi, kelime vurgulu), çipte isim. **Kelime → BOOM arası kesilmez**, köşede gecikme rozeti. | Arkadaşların gerçekten seçtiği kelimeler; birkaç tur çek, en iyisini koy |
| 0:08 | Başlık kartı | — |
| 0:12 | Telefonda QR → kart → kopyala → chat'te `!mine K7QF` → çipte isim | Arkadaşın telefonunun ekran kaydı |
| 0:35 | İki tuzak: biri tutar, biri tutmaz | — |
| 1:00 | "Fıss" ya da False alarm gag'i | — |
| 1:20 | Tur sonu: overlay'de dud'lar, chat'te tur özeti mesajı (izleyici adlarıyla) | twitch.tv kaydı |
| 1:45 | Kaputun altı: akan STT (Deepgram Flux), iki tahmin onayı, GPU gerekmez; harness tablosu | `reports/` |
| 2:10 | Codex bölümü (20–30 sn), `/status`'ta session ID | Bölüm 8'deki kayıtlar |
| 2:40 | Kapanış: repo linki. Video en fazla 2:50. | — |

### Arkadaşlar (sadece kayıt gecesi)
Arkadaşlar sadece 1 Kasım 20:00 kaydında var (D14); T0 yapılmaz, T4 tek başına yapılır.
- 1–2 arkadaş, ~1 saat. Her biri kendi Twitch hesabıyla izler, telefondan ekme sayfasıyla mayın ekler, kelimeyi kendisi seçer. Sen kelimeleri bilmezsin.
- Discord'dan konuşulur, sen kulaklıkla dinlersin (aşağıdaki kontrol listesi).
- Biri 0:12 sahnesi için telefonunun ekran kaydını alır.
- **Yedek, karar 1 Kasım öğlen:** arkadaş bulunamazsa ~0,5 saatlik bir **kör ekleme** betiği yazılır (önce `SPEC.md`'ye eklenir): desteden rastgele kelimeleri test hesaplarıyla ekler, kelimeleri ekrana yazmaz. Afişte farklı isimler için 2–3 test hesabı daha açılır (~10 dk/hesap). Bu durumda dürüstlük cümlesi değişir (aşağıda).

**Twitch'te geçtiğinin kanıtı:** Kural "footage that shows the Project functioning on Twitch" istiyor. Kayıt gecesi OBS kaydına ek olarak ikinci bir cihazdan ya da tarayıcı penceresinden **twitch.tv/kanalın + chat** de kaydedilir. Soğuk açılış ve en az bir patlama bu görüntüden de gösterilir.

**Dürüstlük:**
- "Konuşmayı yaz" modu videoda gerçek STT gibi gösterilmez; gösterilirse "typed fallback" diye etiketlenir.
- Devpost metninde şu cümleler olur: "Friends picked the words; I did not know them." ve "Typed fallback was not used in the video."
- Kör ekleme kullanılırsa ilk cümle şu olur: "Words were planted at random by a script that hid them from me; the viewer names are test accounts."
- Kayıtta yayıncı konuşması İngilizce. Model sadece İngilizce (`flux-general-en`); Türkçe konuşma uydurma bir İngilizce kelimeye "çevrilip" yanlış alarm üretebilir. Arkadaşların Türkçe konuşması Discord'da kalır, mikrofona girmez.

### Demo günü kontrol listesi
- **OBS:**
  - Overlay kaynağında "Control audio via OBS" açık; ses izleme "Monitor and Output".
  - "Shutdown source when not visible" kapalı.
  - Dock: Docks → Custom Browser Docks.
  - Kayıt kodlayıcısı "Same as stream".
- **Ses:**
  - Kulaklık şart. Arkadaşların sesi ve BOOM efekti mikrofona sızmamalı; yoksa arkadaşın söylediği kelime de patlatır.
  - Mikrofonu hiçbir uygulama "exclusive mode"da tutmasın.
- **Laptop:**
  - Prize takılı, "En iyi performans" modunda.
  - Uyku kapalı; uykuda tünel de düşer.
  - Bildirimler ve Discord overlay'i kapalı.
- **WSL:** Uykudan sonra localhost erişimi ya da saat bozulursa `wsl --shutdown` yap ve her şeyi yeniden başlat.
- **Deepgram:** kayıttan önce status.deepgram.com'a bak. Dock'ta Deepgram ışığı kırmızıysa "konuşmayı yaz" moduna geç, kayda devam etme.
- **OBS sesi:** Mic/Aux ve Desktop Audio açık (Codex kayıtlarında kapatılmıştı).
- **Twitch:** Bot mod (link engelinden ve AutoMod'dan muaf); test hesaplarının chat'e yazabildiğini kontrol et.
- **Başlatma:** WSL'de `scripts/run_all.sh`, Windows Chrome'da `http://localhost:8000/mic` (sekme kayıt boyunca açık kalır; OBS ile aynı mikrofon seçili). Dock'taki ışıklar yeşil olmadan kayda başlama.

### Montaj (2 Kasım, yarı otomatik)
- Sen ham kayıtları izleyip her sahne için başlangıç–bitiş zamanını ve altyazıyı bir listeye yazarsın (`video/cuts.json`, git'e girmez; ham görüntüler `C:\Users\furkan\Videos\minefield`'da kalır).
- Codex bu listeden `ffmpeg` ile kesen, hızlandıran, birleştiren ve altyazıyı yakan bir betik yazar ve çalıştırır.
- Son kontrol ve zevk kararı sende. Devpost metninin taslağını da Codex repo'dan çıkarır; sen düzeltirsin.

### Teslim listesi
- [ ] YouTube'a **public** video: 2:50'nin altında, altyazılı; telifli müzik ya da marka yok. Ses efektleri CC0 ya da kendi üretimin.
- [ ] Repo private kalabilir, GitHub'da **testing@devpost.com** ile paylaşılır. Ya da public yapılır.
- [ ] İngilizce `README.md` (WP14):
  - ne yapar;
  - kurulum (Windows + WSL), Deepgram anahtarı ve Twitch uygulama kaydı;
  - anahtarsız demo yolu;
  - test talimatları.
  - Kurallara göre bütün teslim materyalleri İngilizce olmalı. `docs/brainstorm` Türkçe; teslimden önce silmek ya da bırakmak senin kararın.
- [ ] Devpost açıklaması:
  - dört kriterle eşleşen başlıklar (Innovation / Potential Impact / Technological Implementation + Codex / Design);
  - Don't Get Got benzerliğini sahiplenen bir cümle;
  - Impact için: kurulumu bir browser source ve bir Chrome sekmesi, GPU yok; 3 izleyicili küçük bir yayında bile her izleyicinin adı ekrana çıkıyor; makbuz ve tur özeti anı chat'e taşıyor; otomatik klip "future work" diye tek cümle (Twitch'in kendi Clip düğmesi zaten var);
  - dürüstlük cümleleri (yukarıda).
- [ ] Codex session ID.
- [ ] Galeri görselleri: patlama anı, ekme sayfası, harness tablosu.
- [ ] 2 Kasım 23:00 TSİ'den önce **Submit**. Taslak olarak kaydetmek teslim sayılmıyor. Devpost sayacına bir kez bak: SSS'deki saatler kendi içinde çelişiyor.

---

## 10. Karar günlüğü

| # | Karar | Durum | Tarih |
| --- | --- | --- | --- |
| D1 | Kod bu repoda; repo şimdilik private | Verildi | 28 Ekim |
| D2 | Plan Türkçe; `AGENTS.md`, `SPEC.md`, kod, README İngilizce | Verildi | 28 Ekim |
| D3 | STT: Deepgram Flux (AB uç noktası, `mip_opt_out`, keyterm yok), yedek Nova-3 aynı anahtarla; mikrofon Chrome'daki `/mic` sayfasından; yerel motor ve ayrı karşılaştırma testi yok; tek saat | Verildi | 28 Ekim |
| D4 | Ekme sayfasında Twitch girişi yerine chat kodu (`!mine KOD`), kopyala düğmesi, QR, 5 dk geçerlilik | Verildi | 28 Ekim |
| D5 | Teknoloji: Python 3.12 + uv + FastAPI; overlay, dock ve sayfa framework'süz HTML/JS | Verildi | 28 Ekim |
| D6 | Herkese açık adres: cloudflared quick tunnel (WSL'de), sadece ekme sayfası portu | Verildi | 28 Ekim |
| D7 | Ana yapım tek Codex thread'inde; yan thread sadece ana thread beklerken | Güncellendi (sadeleştirme) | 28 Ekim |
| D8 | Kurallar (mayın sayısı, kurulma süresi, "kendi kelimesini yazan kaybeder") | 1 Kasım provasında (T0 çıktı) | — |
| D9 | False alarm: patlamadan sonraki 10 sn içinde; patlama sayılmaz, sahibi yeniden ekebilir. Patlama mesajı beklemeden gider. | Verildi (inceleme + sadeleştirme) | 28 Ekim |
| D10 | "Zaman kalırsa" listesi kaldırıldı; dondurmadan sonraki zaman videoya | Verildi | 28 Ekim |
| D11 | Sadeleştirmeler ([bölüm 13](#13-sadeleştirmeler-28-ekim)) | Verildi | 28 Ekim |
| D12 | Eşleştiricide onay sayısı ayarlanabilir (`CONFIRM_N`, varsayılan 2); Deepgram'ın ham mesajları ve tahminler kaydedilir; rapordaki tahmin dosyaları commit'lenir ki `replay` anahtarsız çalışsın | Verildi | 28 Ekim |
| D13 | Codex: masaüstü uygulamasında (ajan WSL'de) tek ana thread; her WP'de önce testler, `/review`, commit, `/compact`; harness döngüsü ana hikâye; M1 ve M3'te `@codex review`; sadece 7 hedef an kaydedilir, yedek olarak 2 Kasım'da thread geçmişi | Verildi | 28 Ekim |
| D14 | Arkadaşlar sadece 1 Kasım kayıt gecesinde; T0 yok, T4 tek başına (kendi telefonun, mobil veri); arkadaş yoksa kör ekleme betiği (~0,5 sa), karar 1 Kasım öğlen | Verildi | 28 Ekim |
| D15 | Marker, otomatik klip ve klip linki çıktı (sadece canlı yayında test edilebiliyor, videoda ~10 sn). Yerine patlama makbuzu (afişte yayıncının son ~8 kelimesi, diğer deste kelimeleri maskeli) ve tur sonu chat özeti. Yayıncı token'ı gerekmiyor. | Verildi | 28 Ekim |
| D16 | Otomasyon: Codex kendi işini doğrular (Playwright ekran görüntüleri, `pytest -m live` ile test hesabından Twitch testleri, harness'i kendisi koşar); sesler WebAudio ile sentezlenir; kilometre taşı içinde WP'ler zincirlenir; montajın mekanik kısmı `ffmpeg` betiğiyle. Sen sadece cihaz, giriş ve zevk işlerini yaparsın. | Verildi | 28 Ekim |

---

## 11. Değişiklik geçmişi

- **28 Ekim, ilk sürüm.**
- **28 Ekim, bağımsız incelemeden sonra:**
  - Twitch bilgileri düzeltildi: klip 60 sn beklenir; EventSub yeniden bağlanmada yeniden abone olunmaz; rate limit `CF-Connecting-IP` ile yapılır; refresh token tek kullanımlık.
  - Gizlilik açığı kapatıldı: el, bütün desteden çekiliyor.
  - DEFUSE düzeltildi (D9).
  - "Canlı mayın" tanımlandı.
  - Eşleştirici zaman damgası yerine kelime geçişine (occurrence) bakıyor.
  - Gecikme tek saatle ölçülüyor.
  - Harness'e `replay` ve `label-assist` eklendi.
  - Simülatöre `plant` adımı eklendi.
  - WP14 eklendi; WP8 öne alındı.
  - Video ve demo günü listeleri eklendi.
- **28 Ekim, STT kararı (D3, D12):**
  - Yerel faster-whisper turbo yerine Deepgram Flux (yedek Nova-3). Gerekçe: GPU çekişmesi ve CUDA kurulumu yok, ~0,25 sn'lik ara sonuç ritmi, daha az iş.
  - Windows'taki Python relay yerine Chrome'daki `/mic` sayfası.
  - 29 Ekim'deki 45 dk'lık CUDA kontrolü yerine 15 dk'lık Deepgram hesap ve anahtar kontrolü.
  - WP5 1,5 saate indi; CPU modu çıktı; insan saati ~24,5.
  - Eşleştirici: `CONFIRM_N`, `MIN_WORD_PROB`; `AGREE_TOL_S` 0,5.
- **28 Ekim, arkadaşlar (D14):** T0 çıktı; arkadaşlar sadece 1 Kasım kayıt gecesinde. T4 tek başına (kendi telefonun, mobil veri). Kayıt (a) tek başına 15 dk. Kurallar (D8) provada kesinleşir. Arkadaş yoksa kör ekleme betiği yedek. 28 Ekim'de yapılan hazırlıklar 29 Ekim tablosunda işaretlendi; 29 Ekim ~2,5 saat.
- **28 Ekim, marker ve klip (D15):** marker, otomatik klip ve klip linki çıktı; yerine patlama makbuzu ve tur sonu chat özeti. Yayıncı token'ı ve `channel:manage:broadcast` / `clips:edit` scope'ları gitti. T5 bot token'ı ve erişim kontrolüne indi (20 dk). Video çekim listesinde klip sahnesi yerine tur özeti.
- **28 Ekim, otomasyon (D16) ve D4 onayı:** AGENTS.md'ye "önce kendin doğrula", zincirleme ve Playwright kuralları; SPEC'te `scripts/shoot.py`, `?step=N`, WebAudio sesleri, WP9/WP10/WP11 canlı testleri; plana aktif emek/bekleme tablosu, zincir istemi, yarı otomatik montaj. D4 (chat kodu) onaylandı.
- **28 Ekim, Codex kullanımı:** bölüm 8, [codex-usage.md](codex-usage.md) araştırmasına göre yeniden yazıldı: kurulum, ilk mesaj, WP döngüsü (önce testler, `/review`, `/compact`), 7 görünür an, ekran kaydı, dürüstlük cümlesi. Alt ajanlar varsayılan değil; PR incelemesi sadece M1 ve M3'te.

---

## 12. Bağımsız inceleme: ne alındı, ne alınmadı

Rapor: [review-opus.md](review-opus.md). İncelemeci 9 nesnel hatayı doğrudan düzeltti (raporun 2. bölümü); hepsini kontrol ettim ve doğru buldum. 22 önerinin durumu:

| # | Öneri | Durum |
| --- | --- | --- |
| 1 | El bütün desteden; çakışma seçimde | ✅ Alındı |
| 2 | DEFUSE mayını kaldırır + yeniden ekme; "False alarm" diye çerçevele | ✅ Alındı (D9) |
| 3 | "Canlı mayın" tanımı | ✅ Alındı |
| 4 | Harness: tahmin kaydı + tekrar oynatma, etiket yardımcısı, yanlış alarmı 4 mayına normalize | ✅ Alındı. "Prompter" ayrı araç olarak alınmadı; kayıt (c) da `label-assist` ile etiketleniyor. |
| 5 | Eşleştiricide kelime geçişi, tolerans 1,0 sn, "sonraki gelen tahmin" | ✅ Alındı |
| 6 | Tek saat alanı | ✅ Alındı |
| 7 | Simülatöre `plant` | ✅ Alındı; sonra simülatör sadeleştirmede tamamen çıktı |
| 8 | Relay: 48 kHz → 16 kHz, yeniden bağlanma, numpy | ✅ Alındı; STT kararında relay yerine Chrome sayfası geldi (yeniden örnekleme ve yeniden bağlanma orada) |
| 9 | Bütçe kesintileri | ✅ Çoğu alındı. O an "24 saate iner" iddiası alınmadı (hesap ~28 saatti); sadeleştirmeden sonra ~25,5. |
| 10 | Twitch'i öne al | ✅ Alındı, daha da öne: WP8 29 Ekim'de. T5 Twitch CLI yerine bu araçla yapılır, CLI'ın client secret sorunu da ortadan kalkar. |
| 11 | Ana thread + yan thread'ler, `/compact` | ✅ Alındı (SSS ile doğrulandı); sadeleştirmede yan thread'ler varsayılan olmaktan çıktı |
| 12 | Video Twitch'te geçsin, kesintisiz an, klip linki, `/status` | ✅ Alındı; klip linki sonra çıktı (D15) |
| 13 | CPU modu + GPU'suz demo yolu | ✅ Alındı (WP14); STT bulut olunca CPU modu gereksizleşti, anahtarsız demo yolu kaldı |
| 14 | Klip mesajını ikiye böl | ✅ Alındı, sonra klip tamamen çıktı (D15). Create Clip From VOD **alınmadı**: beta sırasında `vod_offset` kayması bildirilmişti. |
| 15 | Demo günü kontrol listesi | ✅ Alındı |
| 16 | 29 Ekim gizli adımları (2FA, e-posta, redirect alanı) | ✅ Alındı |
| 17 | AGENTS.md test ve bağımlılık kuralları | ✅ Alındı, bir farkla: `silero-vad` pip paketi de torch çekiyor. Bu yüzden VAD doğrudan onnxruntime ile çalıştırılacaktı; STT bulut olunca VAD de çıktı. |
| 18 | Ekme uygulaması 127.0.0.1'de | ✅ Alındı |
| 19 | T0 protokolü | ✅ Alındı, sonra çıkarıldı (D14). "Kendi kelimesini yazan kaybeder" kuralı 1 Kasım provasına kaldı (D8). |
| 20 | Dil ve dürüstlük notu | ✅ Alındı |
| 21 | Deste dengesi (6 kart kalsın) | ⏸ Kısmen: kural değişmedi; provada ilk patlama 5 dk'yı geçecek gibiyse desteye yaygın kelimeler eklenir. |
| 22 | Süreç bölünmesi doğru; nabız kesilince kırmızı ışık | ✅ Alındı |

---

## 13. Sadeleştirmeler (28 Ekim)

Ölçüt: **Jüri bunu videoda görüyor mu, ya da dört kriterden birine katkısı var mı?**

| Ne | Önce | Şimdi | Neden |
| --- | --- | --- | --- |
| Chat simülatörü (WP12) | 3 test hesabıyla senaryolu chat | Çıkarıldı; 1 test hesabı | Videoda gerçek arkadaşlar var; test için "konuşmayı yaz" + debug ekleme yetiyor. 3 hesabın kurulumu ve token'ları gitti. |
| `!mines` komutu | Mayın sayısı ve sahipleri | Çıkarıldı | Çipler aynı bilgiyi gösteriyor. |
| Ekme sayfasında hız sınırı | `CF-Connecting-IP` ile IP başına | Yok | Demoda saldırı riski yok. |
| İstatistik | Patlama sayısı + en hızlı patlama | Sadece patlama sayısı | Videoda fark yaratmıyor. |
| CPU modu | Test edilen bir yol | Sadece bayraklar ve README notu; STT kararında tamamen çıktı | Jürinin kurması beklenmiyor; anahtarsız demo yolu kalıyor. |
| Deste | ~300 kelime | ~120 kelime | 4 mayın ve 6 kart için yeterli; kayıt (c) ve eleme işi yarıdan aza indi; yanlış alarm yüzeyi küçüldü. |
| DEFUSE | 10 sn'lik pencere boyunca mayın "hâlâ canlı"; patlama mesajı ve klip pencereyi bekliyor | Patlama mesajı hemen gider; "False alarm" bu süre içinde basit bir geri alma (klip sonra D15'te tamamen çıktı) | Durum makinesinden bir durum ve bir mesaj türü çıktı; chat'teki tepki hızlandı. |
| Codex yan thread'leri | Overlay ve ekme sayfası paralel | Varsayılan tek thread | Darboğaz senin dikkatin. |

**Bilerek kalanlar** (karmaşık görünse de puan getiriyor):
- **Akan tanıma, iki tahmin onayı, kıvılcım ve "fıss":** ürünün kendisi; zamanlama Design puanını taşıyor.
- **Harness:** Tech kriterinin kanıtı ve videodaki Codex hikâyesi.
- **Ekme sayfası ve chat kodu:** "izleyici gizlice seçti" fikrinin videodaki kanıtı.
- **Gecikme rozeti:** "hızlı" kanıtı. "Twitch'te çalışıyor" kanıtı twitch.tv kaydından ve chat mesajlarından gelir.
- Klip linki ve marker sonradan çıktı (D15); yerlerine makbuz ve tur özeti.

STT kararı (D3) ayrı araştırmalarla verildi: [stt-cloud-options.md](stt-cloud-options.md), [stt-research.md](stt-research.md).
