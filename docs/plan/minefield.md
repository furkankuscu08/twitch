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
  - Tek komutla başlatma.
  - README'de anahtarsız demo yolu ("konuşmayı yaz" + debug ekleme + `/overlay?demo=1`).

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
[Windows] mikrofon ─► mic sayfası (Chrome sekmesi, localhost:8100/mic) ─PCM/WebSocket─►
[WSL]     STT motoru ─ses─► Deepgram Flux (AB uç noktası) ─~0,25 sn'de bir ara sonuç─► motor ─tahminler─►
[WSL]     oyun sunucusu (FastAPI): mayınlar, eşleştirme, Twitch
              ├─► overlay  (OBS browser source)
              ├─► dock     (OBS içi kontrol paneli)
              ├─► Twitch   (EventSub chat, chat mesajı)
              └─► ekme sayfası (ayrı port; cloudflared ile sadece bu port dışarı açılır)
```

**İki karar ([bölüm 10](#10-karar-günlüğü)):**
1. **D3: STT bulutta, Deepgram Flux; mikrofon Chrome'daki bir sayfadan.**
   - Chrome'da açık duran `/mic` sayfası sesi WSL'deki motora yollar; motor Deepgram'a akıtır ve gelen ara sonuçları tahmine çevirir. `--save-hyps` ile duyduklarını dosyaya yazar (prova analizi, D17).
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
| **M2: Ses** | Konuşunca BOOM; kıvılcım ve "fıss" çalışıyor; motor tahminleri `--save-hyps` ile kaydediyor. | WP5 |
| **M3: Twitch** | Chat komutları, bot cevapları, patlama ve tur özeti mesajları. | WP9, WP10 |
| **M4: İzleyici** | Telefondan (mobil veriyle) mayın ekleniyor (**T4**). | WP11 |
| **M5: Cila ve teslim hazırlığı** | Animasyonlar, sesler, dud gösterimi, başlatma betikleri, README. **Özellik dondurma.** | WP3 (tam), WP13, WP14 |

Twitch yetkilendirmesi (WP8) inceleme önerisiyle öne alındı. Senin için en bilinmeyen kısım STT değil, Twitch: hesap doğrulama, sadece canlı yayında çalışan API'ler ve token'lar.

---

## 5. İş paketleri ve saatler

Kabul kriterleri `SPEC.md` §7'de. Codex'e görevler bu kimliklerle verilir ("WP5'i yap").

| WP | İş | Saat | Kilometre taşı |
| --- | --- | --- | --- |
| WP7 | Deste: ~120 isim, yazım biçimleri, sesteş eleme | 0,5 | M0 |
| WP8 | Twitch kimlik: device code flow, bot (+ 1 test hesabı) token'ları, yenileme | 1 | M0 |
| WP1 | Çekirdek: normalizasyon, deste, oyun durumu, eşleştirici + birim testleri | 1 | M1 |
| WP2 | Sunucu: FastAPI, WebSocket yayını, dock/overlay uç noktaları, "konuşmayı yaz", motor nabzı | 0,5 | M1 |
| WP3 | Overlay: çipler, kurulma halkası, kıvılcım/fıss, BOOM, afiş ve makbuz, sabit "FALSE ALARM" damgası, dud'lar, QR, gecikme rozeti | 2,25 | M1 → M5 |
| WP4 | Dock: tur başlat/bitir, durum ışıkları, mayın listesi (kelimesiz), "False alarm", yazı kutusu | 0,5 | M1 |
| WP5 | STT: mic sayfası (Chrome, 16 kHz, yeniden bağlanma) + Deepgram motoru (Flux, Nova-3 yedeği, yeniden bağlanma, kayıtlı mesajlarla testler) | 1,5 | M2 |
| WP9 | EventSub chat + komutlar + chat mesajı | 0,5 | M3 |
| WP10 | Patlama mesajı, False alarm mesajı, tur özeti mesajı | 0,25 | M3 |
| WP11 | Ekme sayfası (ayrı port) + kod akışı + kopyala düğmesi + cloudflared | 1,5 | M4 |
| WP13 | Cila ve prova | 1 | M5 |
| WP14 | Başlatma betiği, İngilizce README (Deepgram anahtarı, anahtarsız demo yolu), demo günü listesi | 0,75 | M5 |
| | **Toplam** | **11,25** | |
| | Tampon | 2,5 | |
| | **Yapım toplamı** | **~13,75** | |

İnceleme sonrası değişen saatler:
- WP3: 2,5 → 2 (geri sarma animasyonu yerine sabit damga).
- WP6: 1 → 1,5 (tekrar oynatma ve etiket yardımcısı). Etiketleme için harcayacağın zamanı ~1 saat azaltır.
- WP12 (simülatör): 1 → 0,5, sadeleştirmede tamamen çıktı.
- Yeni WP14: 1.
- Tampon: 3,5 → 2,5. Önceki planda görünmeyen işler artık iş paketlerinde ya da 29 Ekim'de.
- Sadeleştirmede: WP7 0,75 → 0,5 (120 kelime), WP10 0,75 → 0,5 (pencere durumu yok), WP14 1 → 0,75 (CPU modu test edilmiyor).
- Marker ve klip çıkınca (D15): WP10 0,5 → 0,25; WP3 2 → 2,25 (makbuz). Toplam değişmedi; kazanç senin zamanında: T5 kısaldı, canlı yayında hata ayıklama yok.
- Test ve harness iptal (D17, 29 Ekim): WP6 (1,5) tamamen çıktı.
- STT kararında (D3): WP5 2 → 1,5 (yerel model, VAD ve uydurma süzgeçleri yok; Windows relay yerine Chrome sayfası). CPU modu tamamen çıktı.

---

## 6. Takvim

| Gün | Saat (insan) | Ne |
| --- | --- | --- |
| **28 Ekim (bugün)** | — | Plan, `AGENTS.md`, `SPEC.md`, bağımsız inceleme, Twitch/Deepgram/OBS hazırlığı. 1–2 arkadaşla 1 Kasım 20:00 kaydını ayarla. |
| **29 Ekim** | ~1,5 | **Kurulum günü** (aşağıda). Codex ana thread'i açılır: WP7 + WP8. |
| **30 Ekim** | ~5 | ✅ M1–M5 bitti (planın bir gün önünde), T4, OBS kurulumu, kör ekleme (D18), video senaryosu v4 (D20). |
| **31 Ekim** | ~4 | Prova (2 tur) ve Codex log döngüsü (an 3), **özellik dondurma**, kayıt turları ([çekim listesi](#çekim-listesi)). |
| **1 Kasım** | ~4 | Montaj (`cuts.json` taslağı, canlı transkript altyazısı, TTS, `ffmpeg`), ham kurgu jüri testi, Devpost, YouTube, **Submit**. |
| **2 Kasım** | — | Tampon. Son teslim **3 Kasım 01:00 TSİ** (2 Kasım 14:00 PST). |

### 29 Ekim ayrıntısı

T4 kod gerektirdiği için 31 Ekim'e kaydı. 29 Ekim'de bunlar yapılır:

| Sıra | İş | Süre |
| --- | --- | --- |
| 1 | ✅ Twitch hesapları ve uygulama kaydı (28 Ekim'de yapıldı; ayrıntı aşağıda) | — |
| 2 | Codex ana thread'i ([bölüm 8](#8-codex-kullanımı); OBS "Codex" sahnesi 28 Ekim'de hazırlandı). Thread'i aç; **kayda bas**, ilk mesaj (`/plan`), sonuç gelince kaydı durdur (an 1), session ID'yi bölüm 8'e yaz. Sonra WP7 (deste) ve WP8 (auth). WP8 bitince **bot ve test hesabı** için device code girişini yap: bundan sonra Twitch testlerini Codex kendisi koşar. | 45 dk (senin zamanın) |
| 3 | ✅ Deepgram hesabı, API anahtarı `.env`'de, AB uç noktasında Flux denendi (28 Ekim'de yapıldı) | — |
| 4 | ✅ **T5** (29 Ekim): bot'un chat mesajı gitti (`is_sent: true`); Windows'tan WSL'deki `127.0.0.1:8100`'e erişim PowerShell `Invoke-WebRequest` ile doğrulandı (200). Port 8000'i başka bir projenin Docker container'ı kullandığı için Minefield 8100 (sunucu) / 8101 (ekme) portlarına taşındı. | — |
| 5 | Deste v0'ı gözden geçir | 20 dk |

**Twitch hesapları ve uygulama kaydı:**
- Bot hesabı + 1 test hesabı açılır, e-postaları doğrulanır. Arkadaşlar kendi hesaplarını kullanır.
- Yayıncı hesabında 2FA açılır: geliştirici konsolunda uygulama kaydı için gerekiyor (birden çok kılavuz böyle diyor; resmî sayfa bulunamadı).
- Uygulama Public client olarak kaydedilir. Form bir Redirect URL isterse `http://localhost:3000` girilir.
- Bot'a mod yetkisi verilir.
- Kanal ayarları: VOD saklama açık (kayıt gecesi yedeği); chat'te e-posta/telefon doğrulama şartı test hesaplarını engellemeyecek şekilde.

### İnsan saati
(28–29 Ekim'deki tahmin; 30 Ekim sonrası için yukarıdaki takvim ve aşağıdaki tablo geçerli.) 28 Ekim'de yapılan hazırlık ~1,5 + 29 Ekim 1,5 + 30 Ekim–1 Kasım 13,5 (5 + 4,5 + 4) + kayıt 2 + montaj ve teslim 4 ≈ **22,5 saat**. 29 Ekim sabahından itibaren kalan ≈ **21 saat**; tampon (2,5) kullanılmazsa ~18,5. T0 çıkınca 15 dk, ses kayıtları ve T1 çıkınca ~1,25 saat (D17), marker ve klip çıkınca ~1 saat kazanıldı (T5 45 → 20 dk, 31 Ekim'de canlı yayın denemesi yok).

**Aktif emek ve bekleme (D16).** Codex'in kendi doğrulayabildiği işler ona bırakılır; sende sadece onun yapamadıkları kalır. Bu açıdan kalan ~21 saatin ~14,25'i aktif emek, ~6,75'i Codex çalışırken bekleme. Bekleme, Codex'in hatalarının düzeltildiği yer (fiilî tampon); iş yolunda giderse kayıtlara, OBS'e ve montaj hazırlığına kayar.

| Gün | Plandaki | Aktif | Bekleme | Senin işin |
| --- | --- | --- | --- | --- |
| 29 Ekim | 1,5 | ~1,5 | — | `/plan`, device code girişleri, T5, deste |
| 30 Ekim | 5 | ~2,25 | ~2,75 | Mic sayfasında konuşmak, overlay'e ilk bakış |
| 31 Ekim | ~4 | ~3,5 | ~0,5 | Prova, log döngüsü, kayıt turları, telefon demosu (30 Ekim'de güncellendi) |
| 1 Kasım | ~4 | ~3 | ~1 | `cuts.json` seçimi, ham kurguya bakmak, Devpost'u düzeltmek, YouTube, Submit |
| 2 Kasım | — | — | — | Tampon |

**Codex'e tamamen bırakılanlar:** WP1, WP2, prova log'unun analizi ve ayar (T1), WP7, WP9 ve WP10'un canlı testleri (test hesabıyla komut gönderir), WP14; overlay, dock ve ekme sayfasının ekran görüntülerini Playwright ile kendisi alıp kontrol eder; sesleri WebAudio ile sentezler (ses dosyası ve lisans işi yok); montajın mekanik kısmı (`ffmpeg` betiği) ve Devpost taslağı.

Sıkışırsan kesilecekler, sırasıyla:
1. dud gösteriminin animasyonu (düz liste);
2. overlay'deki QR (bot cevabındaki link yeter);
3. tur özeti chat mesajı (overlay'deki dud gösterimi yeter).

---

## 7. Testler ve ölçütler

| Test | Ne zaman | Hedef | Kötüyse |
| --- | --- | --- | --- |
| **T5** bot token'ı ve erişim | 29 Ekim | Bot'un chat mesajı kanalda görünüyor; OBS'ten ve Chrome'dan WSL'deki sunucuya erişiliyor | Scope'lar ve bot'un mod yetkisi kontrol edilir; erişim yoksa `wsl --shutdown` ve tekrar |
| **T1** prova log'u | 31 Ekim, provadan sonra | Provada kaçan ya da yanlış patlayan kelimenin nedeni bulunmuş ve düzeltilmiş; gecikme rozeti medyan ≤1,5 sn, en kötü ≤3 sn; OBS açıkken kare düşmesi yok | Codex `--save-hyps` log'unu inceler: `CONFIRM_N` 2 → 3, `MIN_WORD_PROB`; tanıma kötüyse `--backend nova3`; sorunlu kelimeler desteden çıkar ya da videoya konmaz |
| **T4** ekme sayfası | 31 Ekim | Kendi telefonundan, Wi-Fi kapalı (mobil veri), `minefield_test` hesabıyla uçtan uca bir mayın | ✅ 30 Ekim'de geçti. (Eski yedek, D18 ile geçersiz: Discord + mod yolu: arkadaş kelimeyi mod rolündeki kişiye iletir, o da dock'a girer.) |
| Prova | 31 Ekim sabah | Kör ekleme ve gerçek sesle 2 tur kesintisiz ([çekim listesi](#çekim-listesi)). Kurallar (D8) burada kesinleşir. | Dondurmadan önce düzelt, yoksa kes. İlk patlama 5 dk'dan uzun sürecek gibiyse desteye yaygın kelimeler eklenir. |

Ölçüm için ayrı ses kaydı ve harness yok (D17). Yanlış duyulan kelimeler videoya konmaz; normal sohbetteki yanlış alarm provada izlenir.

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
- **Model:** uygulamada `gpt-6.1-sol`, reasoning `high` (29 Ekim kararı). `xhigh` limiti çok hızlı yer. Astra sadece takıldığında.
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
Do M1: WP1, WP2, WP4, then WP3 (basic), per SPEC.md §7, following the Workflow in AGENTS.md
(tests first, verify it yourself, commit each WP, stop at the first failure you cannot fix).
End with one report and a short checklist of anything only I can do.
```
Zincir bitince her WP için `/review` (2–3 dk) ve sonda bir `/compact`. Tek WP isteniyorsa:
1. `Do WP<n> per SPEC.md §7. Write failing tests from the acceptance list first, run them, then implement.`
2. Testler kırmızı → kod → `uv run pytest` + `uv run ruff check` → yeşil.
3. `/review`. Önemli bulgu varsa düzelttir.
4. `WP<n>: ...` commit'i.
5. `/compact`. WP ortasında compaction'a izin verme. Kalıcı hafıza AGENTS.md, SPEC.md ve git log.

### Görünür Codex anları (videonun Codex bölümü bunlardan kurulur)
| # | An | Ne zaman | Nasıl |
| --- | --- | --- | --- |
| 1 | Spec eleştirisi ve "Do WP1" | 29–30 Ekim | Yukarıdaki ilk mesaj; WP1 istemi |
| 2 | Testler kırmızı → yeşil | 30 Ekim (WP1) | Döngünün 2. adımı |
| 3 | **Prova log'u döngüsü (asıl hikâye)** | 31 Ekim, provadan sonra (T1) | Aşağıdaki istem; Codex gerçek bir provadaki hatayı log'dan bulup düzeltir |
| 4 | Codex'in dev.twitch.tv'yi kontrol etmesi | 31 Ekim (WP9/WP10) | Web araması açık; AGENTS.md zaten istiyor |
| 5 | Codex'in overlay'i kendi ekran görüntüsüyle düzeltmesi | 30 Ekim–1 Kasım (WP3) | `scripts/shoot.py overlay` → Codex PNG'ye bakar → düzeltir; gerekirse OBS'teki görüntü de verilir |
| 6 | PR'da `@codex review` | M1 ve M3 sonunda (2 PR) | Kilometre taşı dalı → PR → yorum |
| 7 | Session ID | 1 Kasım | `/status` ya da status line |

Prova log'u istemi (provada motor `--save-hyps data/hyps/rehearsal.jsonl` ile çalışır; kaçan ve yanlış patlayan anlar not edilir):
```
Read data/hyps/rehearsal.jsonl. In the rehearsal, <word> was said but didn't go off, and
<word> went off by mistake. Find out why from the hypotheses, propose at most 3 changes to
minefield/core/config.py or deck variants, show which logged moments each one fixes, apply
the ones I approve and commit.
```

Canlı testler (`pytest -m live`) ve log analizi Codex'in kendi işi; sana sadece cihaz ve zevk gerektirenler kalır (AGENTS.md, Workflow).

Kullanılmayacaklar: Codex'i ürünün içinde çalıştırmak (yapay görünür), Codex cloud görevleri (kayıtlar ve token'lar yerelde), skills, hooks, MCP.

### Ekran kaydı
**Ne:**
- Sadece Codex uygulamasının penceresi.
- Masaüstünün tamamı değil: e-posta, bildirim ya da başka bir pencere görünmesin.

**OBS kurulumu (bir kez, ~10 dk):**
- Ayrı bir **"Codex" sahnesi** oluştur; içinde Codex uygulaması için tek bir **Window Capture** kaynağı olsun.
- Uygulama: koyu tema, kod fontu 14 pt, pencere büyük. 1080p'de satırlar okunmalı.
- Kayıt ayarları: mp4, 1080p, 30 fps, NVENC. Kayıtlar kısa olduğu için çökmeye dayanıklı format gerekmiyor.
- Audio Mixer'da mikrofon ve masaüstü sesi Codex kayıtlarında kapalı. **Yayından önce tekrar aç.**
- Yayın yaparken Codex kaydı alınmaz. Yayın ve oyun kayıtları ayrı bir iş (bölüm 9).

**Ne zaman:** Sadece yukarıdaki 7 an kaydedilir; sürekli kayıt yok.
- O anın mesajını göndermeden hemen önce kayda bas, sonuç gelince durdur. Her kayıt ~5–20 dk; montajda 3–8 sn'si kullanılır.
- Kayıt bitince dosya adını ve ne olduğunu aşağıdaki tabloya bir satırla yaz.
- Beklenmedik iyi bir an olursa (ör. Codex ciddi bir hatayı yakaladı) kaydı yoksa saatini tabloya yaz; yedek yoldan alınır.

**Yedek: thread geçmişi.** Codex uygulaması ana thread'in tüm geçmişini saklıyor. 1 Kasım'da thread'i baştan sona kaydırırken 1–2 dk'lık bir kayıt alınır. Kaçırılan anların görüntüsü buradan çıkar; bu da gerçek oturumun görüntüsü.

**Gizlilik:**
- `.env` ve `data/tokens.json` ekranda açılmaz; Codex'ten bunları göstermesini isteme.
- Bir anahtar ya da token ekrana gelirse saatini not et; montajda bulanıklaştırılır ya da kesilir. Gerekirse anahtar yenilenir.

**Tarayıcıda olanlar:**
- PR'daki `@codex review` yorumu için tarayıcı penceresi ayrı bir kaynakla kaydedilir.
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
- Devpost'ta Tech başlığının altında aynı maddelerin 3–4 cümlelik özeti ve provadaki hatanın Codex'le bulunup düzeltilmesi.

---

## 9. Video ve teslim

### Video senaryosu v4 (donduruldu, D20)
TTS anlatım üçüncü şahıs konuşur ("the streamer"). Oyun sahnelerinde ses yayıncının gerçek sesi. Hedef süre ~2:30, en fazla 2:50.

| Zaman | Görüntü | Anlatım (TTS) | Ekran yazısı |
| --- | --- | --- | --- |
| 0:00–0:07 | twitch.tv çerçevesinde yayın, kurulu çipler | "Three test viewers have hidden secret words on this stream. A script picked them at random; the streamer doesn't know which ones." | "3 test accounts · real Twitch chat · words hidden from the streamer" |
| 0:07–0:17 | **Kesintisiz:** kıvılcımdan ~2 sn önce başlar → BOOM → gerçek tepki | *(gerçek ses)* | Altyazıda kelime vurgulu · "Real voice (Turkish accent) · live recognition · uncut" |
| 0:17–0:28 | Afişte dondurma, isim ve kelimeye ok | "That's Minefield. Say a hidden word, and it explodes, naming who planted it. Viewers win when their word goes off. The streamer can't dodge words they don't know." | **MINEFIELD** |
| 0:28–0:45 | Telefon: kartlarda kısa bekleme → kod → chat'te `!mine` → çip kuruluyor | "How did that word get there? A viewer scans the QR code, picks one of six cards, and types a one-time code in chat. Chat is public, so the word stays on the phone." | — |
| 0:45–1:05 | Başka bir izleyicinin patlaması, altında hipotez log'undan canlı transkript; varsa gerçek fizzle | "How does it know? It listens live. Heard once, a mine sparks. Still there a moment later, it explodes." (Fizzle cümlesi sadece görüntüsü varsa: "If the recognizer changes its mind, it fizzles.") | "SPARK → BOOM" · transkript üzerinde: "Recognizer log (post-production, not shown on stream)" |
| 1:05–1:20 | twitch.tv: chat'te `!mine` mesajları, tur sonu açıklaması, bot özeti | "At round end, surviving mines are revealed and the bot posts a recap. Even with three viewers, every plant puts a name on screen and gives chat a reason to listen." | "Built for small streams · one browser source + one Chrome tab" |
| 1:20–1:30 | Mimari şeması: A (tamamı) → B (izleyici yolu) → C (ses yolu ve iki kural), ~3'er sn | "Two rules keep it fair. Nothing on stream, in chat or in logs sees a word until it explodes or the round ends. And the recognizer is never told the words." | "No word hints to speech recognition" |
| 1:30–1:58 | **Codex**, etiketli 3 kare: etiketin öncesi/sonrası → prova log satırı ve config değişikliği → kırmızıdan yeşile test | "Built solo in four days with Codex. The spec was the contract; every feature started with a failing test. Codex screenshotted its own overlay and fixed a label it couldn't read. After a rehearsal, it read the speech log, found what went wrong, and tuned the game." | Kısa etiketler (sorun → Codex → sonuç) · session ID köşede küçük |
| 1:58–2:25 | **Final:** son turun mayınlarını Codex ekledi (kör ekleme betiğini o çalıştırdı); yayıncı Codex'i anlatırken bir mayın patlar ya da gerçek tur sonunda "survived" + twitch.tv özeti | "For the last round, Codex planted the mines." … "Your chat chooses the trap. Your voice pulls the pin." | "Codex ran the planting script" |
| 2:25–2:30 | Başlık ve repo | — | **MINEFIELD** · repo linki |

**Kurallar:**
- Hiçbir tanıma anı sahnelenmez ya da uydurulmaz. Fizzle ve false alarm sadece doğal olarak yaşandıysa gösterilir; yoksa anlatımdan da çıkar.
- "Konuşmayı yaz" modu videoda yok.
- Prova log'unda aksan kaynaklı bir hata çıkarsa Codex cümlesi "...found the words it misheard in the streamer's accent, and tuned the game." olur; sadece gerçekten öyleyse.
- Final turunda mayın patlamazsa bu kayıp değil, oyunun geçerli sonucu: gerçek tur sonu gösterilir.
- Ham kurgu çıkınca bir tur daha bağımsız jüri değerlendirmesi yapılır (kareler ve transkriptle).

### Çekim listesi
**Hazırlık (her oturumdan önce):**
- [ ] [Demo günü kontrol listesi](#demo-günü-kontrol-listesi) tamam: kulaklık, Deepgram durumu, `/mic` sekmesi, bildirimler kapalı.
- [ ] Twitch kanal ayarında "Store past broadcasts" açık (yedek).
- [ ] Telefonda Twitch uygulamasında `minefield_test` ile oturum açık.

**Prova (31 Ekim sabah):**
- [ ] Codex üç test hesabının token'ını yeniler, `scripts/run_all.sh`'ı başlatır. Dock'taki ışıklar yeşil.
- [ ] OBS'te Minefield sahnesi, Mic/Aux açık: **Start Streaming** ve **Start Recording**.
- [ ] İki ayrı Chrome penceresi: biri `/mic` (arka planda açık kalır), diğeri twitch.tv kanal sayfası (sessiz, küçültülmez) ve Game Bar (`Win+Alt+R`) ile kayıtta.
- [ ] 2 tur. Her tur: dock'ta turu başlat, sonra Codex `scripts/blind_plant.py`'ı çalıştırır. Motor `--save-hyps` ile. Kaçan ya da yanlış patlayan anların saatini not et.
- [ ] Provadan sonra: OBS'te Stop Streaming ve Stop Recording, Game Bar kaydını durdur.

**Log döngüsü (Codex anı 3):**
- [ ] OBS'te "Codex" sahnesine geç, Mic/Aux ve Desktop Audio'yu sessize al, Start Recording; bölüm 8'deki prova log'u istemi. Bitince Stop Recording.
- [ ] Net bir öncesi ve sonrası: hangi kelime kaçtı ya da yanlış patladı, ne değişti, sonra çalıştı mı. Ardından **özellik dondurma**.

**Kayıt turları:**
- [ ] OBS'te Minefield sahnesine dön, **Mic/Aux'u yeniden aç** (Desktop Audio sessiz kalır), Codex token'ları yeniler; Start Streaming, Start Recording, Game Bar kaydı.
- [ ] **Telefon demosu, ayrı turda:** `minefield_test` ile QR → kartlar (2–3 sn bekle) → kod → `!mine`. Telefon ekran kaydı, OBS ve twitch.tv kaydı aynı anda açık. Bu turda kör ekleme çalıştırılmaz; tur bitmeden sonraki tur başlamaz (bir izleyiciye bir canlı mayın kuralı). Bu turun patlaması videoya girmez (kelimeyi biliyorsun).
- [ ] **En az 3 doğal konuşma turu,** her biri 5–10 dk, konuşma kartıyla. Her tur: dock'ta başlat, Codex kör eklemeyi çalıştırır. Hedef: farklı izleyicilerle en az 2 temiz patlama, en az biri 10 sn kesintisiz kullanılabilir ve tepki gerçek.
- [ ] Fizzle ya da false alarm: sadece doğal olursa.
- [ ] Her tur sonunda overlay açıklaması ve twitch.tv'deki bot özeti kayıtta.
- [ ] **Final turu:** turu başlat; kör ekleme betiğini **Codex** çalıştırır (betik hesap seçemez, üç hesap da birer mayın ekler). Yaklaşık 10 dk doğaçlama Codex anlatımı; yanında 3–4 maddelik hatırlatma.

**Saklanacaklar:**
- OBS ve Game Bar dosyaları, telefon kaydı. Yayın gecikmesi 3–8 sn olduğu için twitch.tv kaydı OBS'e dosya adındaki saatle kabaca, BOOM sesiyle tam hizalanır.
- Her turun `data/hyps/*.jsonl` log'u (canlı transkript altyazısı bundan üretilir), turların başlangıç ve bitiş saatleri.

**Gizlilik:** `.env`, token'lar ve stream key ekranda açılmaz. Tur sonu açıklaması ve chat özeti o turun kelimelerini gösterir; sonraki turun kelimeleri yine rastgele olduğu için sorun değil.

### Kör ekleme ve dürüstlük
Arkadaş kaydı yok (D18). Mayınları `scripts/blind_plant.py` üç test hesabıyla (`minefield_test`, `pixelmoth01`, `mossy_otter`) gerçek chat yolundan ekler; kelimeler hiçbir yerde gösterilmez.

**Twitch'te geçtiğinin kanıtı:** Kural "footage that shows the Project functioning on Twitch" istiyor. OBS kaydına ek olarak twitch.tv kanal sayfası ve chat de kaydedilir. Açılış ve en az bir patlama bu görüntüden de gösterilir.

**Dürüstlük:**
- Devpost'ta: "Words were planted at random by a script that hid them from me; the viewer names are test accounts." ve "Typed fallback was not used in the video."
- Anlatım TTS; oyun sahnelerindeki ses gerçek.
- Kayıtta yayıncı konuşması İngilizce. Model sadece İngilizce (`flux-general-en`); Türkçe konuşma uydurma bir İngilizce kelimeye "çevrilip" yanlış alarm üretebilir.

### Demo günü kontrol listesi
- **OBS:**
  - Overlay kaynağında "Control audio via OBS" açık; ses izleme "Monitor and Output".
  - "Shutdown source when not visible" kapalı.
  - Dock: Docks → Custom Browser Docks.
  - Kayıt kodlayıcısı "Same as stream".
- **Ses:**
  - Kulaklık şart. BOOM efekti ve bilgisayardan gelen sesler mikrofona sızmamalı; yoksa sızan ses de kelime patlatabilir.
  - Mikrofonu hiçbir uygulama "exclusive mode"da tutmasın.
- **Laptop:**
  - Prize takılı, "En iyi performans" modunda.
  - Uyku kapalı; uykuda tünel de düşer.
  - Bildirimler ve Discord overlay'i kapalı.
- **WSL:** Uykudan sonra localhost erişimi ya da saat bozulursa `wsl --shutdown` yap ve her şeyi yeniden başlat.
- **Deepgram:** kayıttan önce status.deepgram.com'a bak. Dock'ta Deepgram ışığı kırmızıysa "konuşmayı yaz" moduna geç, kayda devam etme.
- **OBS sesi:** Mic/Aux açık; Desktop Audio sessiz (açık kalırsa izlenen overlay sesi kayda iki kez girer); Overlay'de monitoring açık. Minefield sahnesi ve dock 30 Ekim'de kuruldu.
- **Twitch:** Bot mod (link engelinden ve AutoMod'dan muaf); test hesaplarının chat'e yazabildiğini kontrol et.
- **Yayın ve kayıt:** OBS'te Start Streaming ve Start Recording; twitch.tv sekmesi sessiz ve Game Bar ile kayıtta. Codex kayıttan hemen önce test hesaplarının token'larını yeniler.
- **Başlatma:** WSL'de `scripts/run_all.sh`, Windows Chrome'da `http://localhost:8100/mic` (sekme kayıt boyunca açık kalır; OBS ile aynı mikrofon seçili). Dock'taki ışıklar yeşil olmadan kayda başlama.

### Montaj (1 Kasım, yarı otomatik)
- Claude patlama saatlerinden ve OBS dosya adından `video/cuts.json` taslağını ve kare önizlemelerini hazırlar; sen seçer ve düzeltirsin (git'e girmez; ham görüntüler `C:\Users\furkan\Videos\minefield`'da kalır). Altyazıyı Codex son videodan Deepgram ile üretir; 0:45 sahnesinin canlı transkriptini `--save-hyps` log'undan üretir (D19, D20).
- Codex bu listeden `ffmpeg` ile kesen, hızlandıran, birleştiren ve altyazıyı yakan bir betik yazar ve çalıştırır.
- Anlatım TTS ile seslendirilir: Codex Deepgram Aura ile üretir; istersen Gemini TTS'i AI Studio'dan alıp karşılaştırırsın.
- Son kontrol ve zevk kararı sende. Devpost metninin taslağını Claude yazar (D19); sen düzeltirsin.

### Teslim listesi
- [ ] YouTube'a **public** video: 2:50'nin altında, altyazılı; telifli müzik ya da marka yok. Ses efektleri CC0 ya da kendi üretimin.
- [ ] Repo private kalabilir, GitHub'da **testing@devpost.com** ile paylaşılır. Ya da public yapılır; ama o zaman eski commit'lerdeki kişisel e-posta görünür (72 commit), bu yüzden paylaşım öneriliyor.
- [ ] İngilizce `README.md` (WP14):
  - ne yapar;
  - kurulum (Windows + WSL), Deepgram anahtarı ve Twitch uygulama kaydı;
  - anahtarsız demo yolu;
  - test talimatları.
  - Kurallara göre bütün teslim materyalleri İngilizce olmalı. `docs/brainstorm` Türkçe; teslimden önce silmek ya da bırakmak senin kararın.
- [ ] Devpost açıklaması: taslak Claude Docs'ta, [Minefield — Devpost submission draft](https://claude.ai/artifact/HuZUJaVRJ2R8jMzdjV81pX). 30 Ekim: iskelet kuruldu ve review'dan geçti. İsim, slogan, Built with ve dürüstlük satırları yazıldı; diğer bölümler yer tutucu. Rakamlar ve Codex hikâyesi provadan sonra, kalan metin 1 Kasım'da yazılacak.
  - sıra: TL;DR ve video linki → What it does (Design) → What's new (Innovation) → Why streamers want it (Impact) → How it works (Tech) → How Codex built it → Demo transparency. Beraberlikte önce Innovation sayıldığı için o bölüm öne alındı;
  - Don't Get Got benzerliğini sahiplenen bir cümle;
  - Impact için: yayında bir browser source ve bir dock, mikrofon bir Chrome sekmesinde; GPU ve Extension incelemesi yok, ama Deepgram anahtarı ve bot hesabı gerekiyor (abartmadan); 3 izleyicili küçük bir yayında bile her izleyicinin adı ekrana çıkıyor; makbuz ve tur özeti anı chat'e taşıyor; otomatik klip "future work" diye tek cümle (Twitch'in kendi Clip düğmesi zaten var);
  - dürüstlük cümleleri ([yukarıda](#kör-ekleme-ve-dürüstlük)).
- [ ] Codex session ID.
- [ ] Galeri görselleri: patlama anı, ekme sayfası, mimari şeması.
- [ ] **Submit**, hedef 1 Kasım akşamı. Son teslim 2 Kasım 14:00 PST = **3 Kasım 01:00 TSİ** (kurallar ve overview aynı ana denk geliyor). Taslak olarak kaydetmek teslim sayılmıyor.

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
| D12 | Eşleştiricide onay sayısı ayarlanabilir (`CONFIRM_N`, varsayılan 2); Deepgram'ın ham mesajları ve tahminler kaydedilir; rapordaki tahmin dosyaları commit'lenir ki `replay` anahtarsız çalışsın | Verildi; replay ve rapor D17'de çıktı | 28 Ekim |
| D13 | Codex: masaüstü uygulamasında (ajan WSL'de) tek ana thread; her WP'de önce testler, `/review`, commit, `/compact`; harness döngüsü ana hikâye (D17'de prova log'u döngüsüne döndü); M1 ve M3'te `@codex review`; sadece 7 hedef an kaydedilir, yedek olarak 2 Kasım'da thread geçmişi | Verildi | 28 Ekim |
| D14 | Arkadaşlar sadece 1 Kasım kayıt gecesinde; T0 yok, T4 tek başına (kendi telefonun, mobil veri); arkadaş yoksa kör ekleme betiği (~0,5 sa), karar 1 Kasım öğlen | D18 ile değişti | 28 Ekim |
| D15 | Marker, otomatik klip ve klip linki çıktı (sadece canlı yayında test edilebiliyor, videoda ~10 sn). Yerine patlama makbuzu (afişte yayıncının son ~8 kelimesi, diğer deste kelimeleri maskeli) ve tur sonu chat özeti. Yayıncı token'ı gerekmiyor. | Verildi | 28 Ekim |
| D16 | Otomasyon: Codex kendi işini doğrular (Playwright ekran görüntüleri, `pytest -m live` ile test hesabından Twitch testleri, harness'i kendisi koşar); sesler WebAudio ile sentezlenir; kilometre taşı içinde WP'ler zincirlenir; montajın mekanik kısmı `ffmpeg` betiğiyle. Sen sadece cihaz, giriş ve zevk işlerini yaparsın. | Verildi | 28 Ekim |
| D17 | Ses kayıtları, T1 doğruluk testi ve WP6 harness iptal. Yanlış duyulan kelimeler videoya konmaz. Motorun `--save-hyps` kaydı kalır; 1 Kasım provasından sonra Codex log'u inceleyip ayarı düzeltir (yeni T1 ve Codex anı 3). Tanıma beğenilmezse Deepgram modeli değiştirilir. | Verildi | 29 Ekim |
| D18 | Arkadaş kaydı yok: mayınları kör ekleme betiği test hesaplarıyla, gerçek chat yolundan (`!mine KOD`) ekler; kelimeler hiçbir yerde gösterilmez. Oyunda yayıncı sesi kendi sesin (TTS değil). Video anlatımı TTS (Deepgram Aura, mevcut anahtar). Kayıt 1 Kasım 20:00'a bağlı değil; teslim hedefi 1 Kasım, 2 Kasım tampon. | Verildi | 30 Ekim |
| D19 | İş bölümü (teslime kadar). **Codex** (kod ve repo işi, Codex kanıtı): kör ekleme betiği; provayı yönetir (`run_all.sh`, tur, kör ekleme, log analizi) ve built-in browser'da twitch.tv kanalında `!mine` mesajlarını ve tur özetini kontrol eder, galeri için görüntü alır; `ffmpeg` montaj betiği; altyazı (son videodan Deepgram ile SRT, videoya yakılır); teslim öncesi repo denetimi (sır, e-posta, Türkçe dosya, temiz klonda README). **Claude** (metin ve analiz): patlama saatleri ile OBS dosya adından `cuts.json` taslağı ve kare önizlemeleri; anlatım metni; Devpost taslağı; mimari şeması; Devpost kuralları ve sayaç kontrolü. **Sen:** konuşma, telefon, device-code girişleri (kendi Chrome'unda gizli pencere; Codex browser'ı yayıncı hesabıyla açık), zevk kararları, YouTube ve Submit. Codex computer use kullanmaz. | Verildi | 30 Ekim |
| D20 | Video senaryosu v4 donduruldu ([bölüm 9](#video-senaryosu-v4-donduruldu-d20)). Opus, Astra ve Grok önce bağımsız senaryo yazdı; birleşik senaryo 3 tur soğuk okuma jüri testinden geçti (ortalama 7,5–8/10, Codex mühendisi gözüyle ilk 5'e yakın). Sonuçlar: kesintisiz gerçek patlamayla açılış en güçlü an, olduğu gibi kalır; kural ilk saniyede söylenir; her bölüm bir soruya cevap verir; kör ekleme açıklaması başta ve "tepki bu yüzden gerçek" diye sunulur; aksan güç olarak gösterilir; patlama montajı yerine canlı transkriptli tek patlama; şema ve OBS ekranı kısalır; Codex bölümü tek bir "sorun → Codex → sonuç" hikâyesi; final "Codex'in mayını". Sonraki değerlendirme ham kurgu üzerinde. | Verildi | 30 Ekim |

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
- **29 Ekim, T5 ve kayıtlar (D17):** T5 tamam (bot mesajı `is_sent: true`; Windows → WSL `127.0.0.1:8100` erişimi PowerShell ile doğrulandı). Portlar 8100/8101 (8000'de başka bir projenin Docker container'ı var). Ses kayıtları, T1 testi ve WP6 harness iptal (D17); yerine prova log'u analizi. Codex: reasoning `high`, font 14. Kalan iş ~21 saat.
- **28 Ekim, otomasyon (D16) ve D4 onayı:** AGENTS.md'ye "önce kendin doğrula", zincirleme ve Playwright kuralları; SPEC'te `scripts/shoot.py`, `?step=N`, WebAudio sesleri, WP9/WP10/WP11 canlı testleri; plana aktif emek/bekleme tablosu, zincir istemi, yarı otomatik montaj. D4 (chat kodu) onaylandı.
- **30 Ekim, video senaryosu (D20):** bölüm 9'daki eski (arkadaşlı) çekim listesi yerine v4 senaryosu ve yeni çekim listesi; takvim gerçekleşene göre güncellendi (M5 30 Ekim'de bitti; prova ve kayıt 31 Ekim; teslim hedefi 1 Kasım); son teslim saati düzeltildi (3 Kasım 01:00 TSİ).
- **30 Ekim, kör ekleme ve TTS (D18):** arkadaş kaydı iptal, yerine kör ekleme betiği (önce SPEC'e eklenir) ve 2–3 ek test hesabı. Oyunda kendi sesin; video anlatımı TTS. Dürüstlük cümlesi kör ekleme sürümüne döndü. Teslim hedefi 1 Kasım.
- **28 Ekim, Codex kullanımı:** bölüm 8, [codex-usage.md](codex-usage.md) araştırmasına göre yeniden yazıldı: kurulum, ilk mesaj, WP döngüsü (önce testler, `/review`, `/compact`), 7 görünür an, ekran kaydı, dürüstlük cümlesi. Alt ajanlar varsayılan değil; PR incelemesi sadece M1 ve M3'te.

---

## 12. Bağımsız inceleme: ne alındı, ne alınmadı

Rapor: [review-opus.md](review-opus.md). İncelemeci 9 nesnel hatayı doğrudan düzeltti (raporun 2. bölümü); hepsini kontrol ettim ve doğru buldum. 22 önerinin durumu:

| # | Öneri | Durum |
| --- | --- | --- |
| 1 | El bütün desteden; çakışma seçimde | ✅ Alındı |
| 2 | DEFUSE mayını kaldırır + yeniden ekme; "False alarm" diye çerçevele | ✅ Alındı (D9) |
| 3 | "Canlı mayın" tanımı | ✅ Alındı |
| 4 | Harness: tahmin kaydı + tekrar oynatma, etiket yardımcısı, yanlış alarmı 4 mayına normalize | ✅ Alındı, 29 Ekim'de harness tamamen çıktı (D17). |
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
| Chat simülatörü (WP12) | 3 test hesabıyla senaryolu chat | Çıkarıldı; 1 test hesabı | (D18 ile geçersiz: arkadaş yok, kör ekleme 3 test hesabı kullanıyor.) Videoda gerçek arkadaşlar var; test için "konuşmayı yaz" + debug ekleme yetiyor. 3 hesabın kurulumu ve token'ları gitti. |
| `!mines` komutu | Mayın sayısı ve sahipleri | Çıkarıldı | Çipler aynı bilgiyi gösteriyor. |
| Ekme sayfasında hız sınırı | `CF-Connecting-IP` ile IP başına | Yok | Demoda saldırı riski yok. |
| İstatistik | Patlama sayısı + en hızlı patlama | Sadece patlama sayısı | Videoda fark yaratmıyor. |
| CPU modu | Test edilen bir yol | Sadece bayraklar ve README notu; STT kararında tamamen çıktı | Jürinin kurması beklenmiyor; anahtarsız demo yolu kalıyor. |
| Deste | ~300 kelime | ~120 kelime | 4 mayın ve 6 kart için yeterli; kayıt (c) ve eleme işi yarıdan aza indi; yanlış alarm yüzeyi küçüldü. |
| DEFUSE | 10 sn'lik pencere boyunca mayın "hâlâ canlı"; patlama mesajı ve klip pencereyi bekliyor | Patlama mesajı hemen gider; "False alarm" bu süre içinde basit bir geri alma (klip sonra D15'te tamamen çıktı) | Durum makinesinden bir durum ve bir mesaj türü çıktı; chat'teki tepki hızlandı. |
| Codex yan thread'leri | Overlay ve ekme sayfası paralel | Varsayılan tek thread | Darboğaz senin dikkatin. |

**Bilerek kalanlar** (karmaşık görünse de puan getiriyor):
- **Akan tanıma, iki tahmin onayı, kıvılcım ve "fıss":** ürünün kendisi; zamanlama Design puanını taşıyor.
- **Harness:** sonradan çıktı (D17); Codex hikâyesini prova log'u analizi taşıyor.
- **Ekme sayfası ve chat kodu:** "izleyici gizlice seçti" fikrinin videodaki kanıtı.
- **Gecikme rozeti:** "hızlı" kanıtı. "Twitch'te çalışıyor" kanıtı twitch.tv kaydından ve chat mesajlarından gelir.
- Klip linki ve marker sonradan çıktı (D15); yerlerine makbuz ve tur özeti.

STT kararı (D3) ayrı araştırmalarla verildi: [stt-cloud-options.md](stt-cloud-options.md), [stt-research.md](stt-research.md).
