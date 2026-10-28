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
  - Stream marker.
  - Patlamadan sonraki 10 sn içinde "False alarm" (`!defuse` ya da dock): patlama sayılmaz, klip açılmaz.
  - Patlama mesajı hemen; 10 sn sonra 30 sn'lik klip ve linki.
  - Tur sonunda dud'lar ve patlama sayısı.
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
- Create Clip From VOD.

---

## 3. Mimari (özet)

Ayrıntılar `SPEC.md`'de. Kısaca:

```
[Windows] mikrofon ─► mic sayfası (Chrome sekmesi, localhost:8000/mic) ─PCM/WebSocket─►
[WSL]     STT motoru ─ses─► Deepgram Flux (AB uç noktası) ─~0,25 sn'de bir ara sonuç─► motor ─tahminler─►
[WSL]     oyun sunucusu (FastAPI): mayınlar, eşleştirme, Twitch
              ├─► overlay  (OBS browser source)
              ├─► dock     (OBS içi kontrol paneli)
              ├─► Twitch   (EventSub chat, chat mesajı, marker, klip)
              └─► ekme sayfası (ayrı port; cloudflared ile sadece bu port dışarı açılır)
```

**İki karar ([bölüm 10](#10-karar-günlüğü)):**
1. **D3: STT bulutta, Deepgram Flux; mikrofon Chrome'daki bir sayfadan.**
   - Chrome'da açık duran `/mic` sayfası sesi WSL'deki motora yollar; motor Deepgram'a akıtır ve gelen ara sonuçları tahmine çevirir. Harness ve canlı oyun aynı motoru kullanır.
   - Neden: GPU'yu oyun ve NVENC ile paylaşmak yok, CUDA kurulumu yok, ~2–3 saat daha az iş. Flux ~0,25 sn'de bir kelime zamanlı ve güven skorlu ara sonuç veriyor; iki tahmin onayına çok uygun. Pitch'te "GPU gerekmez, her yayıncı kullanabilir" (Impact).
   - Ayrı karşılaştırma testi yapılmaz. Ses beğenilmezse aynı anahtarla Nova-3'e (`--backend nova3`) ya da başka bir Deepgram modeline geçilir. Yerel motor yazılmaz.
   - Gecikme tek bir saatle ölçülür: motorun kendi saati, çünkü Windows ve WSL saatleri uykudan sonra kayabiliyor.
   - Ayrıntılar ve kaynaklar: [stt-cloud-options.md](stt-cloud-options.md).
2. **D4: Ekme sayfasında Twitch girişi yerine chat kodu.**
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
| **M3: Twitch** | Chat komutları, bot cevapları, marker, klip ve link. | WP9, WP10 |
| **M4: İzleyici** | Arkadaşın telefonundan mayın ekleniyor (**T4**). | WP11 |
| **M5: Cila ve teslim hazırlığı** | Animasyonlar, sesler, dud gösterimi, başlatma betikleri, README. **Özellik dondurma.** | WP3 (tam), WP13, WP14 |

Twitch yetkilendirmesi (WP8) inceleme önerisiyle öne alındı. Senin için en bilinmeyen kısım STT değil, Twitch: hesap doğrulama, sadece canlı yayında çalışan API'ler ve token'lar.

---

## 5. İş paketleri ve saatler

Kabul kriterleri `SPEC.md` §8'de. Codex'e görevler bu kimliklerle verilir ("WP5'i yap").

| WP | İş | Saat | Kilometre taşı |
| --- | --- | --- | --- |
| WP7 | Deste: ~120 isim, yazım biçimleri, sesteş eleme | 0,5 | M0 |
| WP8 | Twitch kimlik: device code flow, yayıncı + bot (+ 1 test hesabı) token'ları, yenileme | 1 | M0 |
| WP1 | Çekirdek: normalizasyon, deste, oyun durumu, eşleştirici + birim testleri | 1 | M1 |
| WP2 | Sunucu: FastAPI, WebSocket yayını, dock/overlay uç noktaları, "konuşmayı yaz", motor nabzı | 0,5 | M1 |
| WP3 | Overlay: çipler, kurulma halkası, kıvılcım/fıss, BOOM, afiş, sabit "FALSE ALARM" damgası, dud'lar, QR, gecikme rozeti | 2 | M1 → M5 |
| WP4 | Dock: tur başlat/bitir, durum ışıkları, mayın listesi (kelimesiz), "False alarm", yazı kutusu | 0,5 | M1 |
| WP5 | STT: mic sayfası (Chrome, 16 kHz, yeniden bağlanma) + Deepgram motoru (Flux, Nova-3 yedeği, yeniden bağlanma, kayıtlı mesajlarla testler) | 1,5 | M2 |
| WP6 | Harness: `run`, `replay` (kayıtlı tahminlerden saniyeler içinde), `label-assist`, rapor | 1,5 | M2 |
| WP9 | EventSub chat + komutlar + chat mesajı | 0,5 | M3 |
| WP10 | Marker, patlama mesajı, klip zamanlayıcısı + link mesajı, False alarm | 0,5 | M3 |
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
- STT kararında (D3): WP5 2 → 1,5 (yerel model, VAD ve uydurma süzgeçleri yok; Windows relay yerine Chrome sayfası). CPU modu tamamen çıktı.

---

## 6. Takvim

| Gün | Saat (insan) | Ne |
| --- | --- | --- |
| **28 Ekim (bugün)** | — | Plan, `AGENTS.md`, `SPEC.md`, bağımsız inceleme. Arkadaşlarla T0 ve kayıt saatlerini ayarla. |
| **29 Ekim** | ~4 | **Kurulum ve veri günü** (aşağıda). Codex ana thread'i açılır: WP7 + WP8. |
| **30 Ekim** | ~6 | M1 + M2. Akşam **T1**. |
| **31 Ekim** | ~5 | M3 + M4. Bir arkadaşla **T4**. |
| **1 Kasım** | ~4 + akşam 2 | M5. Öğlen prova (2 tur). **17:00 özellik dondurma.** 20:00 arkadaşlarla kayıt. |
| **2 Kasım** | ~4 | Video montajı, Devpost metni, repo paylaşımı. **23:00 TSİ Submit.** |

### 29 Ekim ayrıntısı

T1 ve T4 kod gerektirdiği için 30 ve 31 Ekim'e kaydı. 29 Ekim'de bunlar yapılır:

| Sıra | İş | Süre |
| --- | --- | --- |
| 1 | Twitch hesapları ve uygulama kaydı (ayrıntı aşağıda) | 60–75 dk |
| 2 | Codex kurulumu ve OBS'te "Codex" sahnesi ([bölüm 8](#8-codex-kullanımı)). **Kayıt açık**, ana thread'i aç, ilk mesaj (`/plan`), session ID'yi bölüm 8'e yaz. Sonra WP7 (deste) ve WP8 (auth). | 45 dk (senin zamanın) |
| 3 | Deepgram hesabı (200 $ ücretsiz kredi), API anahtarı `.env`'e. Kısa bir WAV'ı `curl` ile AB uç noktasındaki pre-recorded API'ye gönder: anahtar çalışıyor mu, kelimeler doğru mu? | 15 dk |
| 4 | **T5:** WP8 aracıyla yayıncı token'ı al. Kısa bir test yayını aç, curl ile marker ve klip oluştur; **klibi oynat**, doğru anı içeriyor mu bak. Aynı yayında OBS'te ve Chrome'da `http://localhost:8000` erişimini dene (Windows → WSL). | 45 dk |
| 5 | Deste v0'ı gözden geçir | 20 dk |
| 6 | **T0** arkadaşlarla Discord'da ([protokol](#t0-protokolü)). Bu sırada kendi mikrofonunu kaydet: kayıt (a) | 30 dk |
| 7 | Kayıt (b): 10 dk sessizlik ve arka plan (klavye, nefes, sandalye). Kayıt (c): deste kelimeleri kısa cümlelerde; etiketleri sonra `label-assist` çıkarır. | 30 dk |

**Twitch hesapları ve uygulama kaydı:**
- Bot hesabı + 1 test hesabı açılır, e-postaları doğrulanır. Arkadaşlar kendi hesaplarını kullanır.
- Yayıncı hesabında 2FA açılır: geliştirici konsolunda uygulama kaydı için gerekiyor (birden çok kılavuz böyle diyor; resmî sayfa bulunamadı).
- Uygulama Public client olarak kaydedilir. Form bir Redirect URL isterse `http://localhost:3000` girilir.
- Bot'a mod yetkisi verilir.
- Kanal ayarları: VOD saklama açık; klipler açık; chat'te e-posta/telefon doğrulama şartı test hesaplarını engellemeyecek şekilde.

**Kayıt formatı:** WAV, mono, sadece senin mikrofonun. Arkadaşların sesi kayda girmemeli; Discord'u kulaklıkla dinle. Dosyalar `data/recordings/` altına (git'e girmez).

### T0 protokolü
1. Deste v0'dan her arkadaşa 6 kelimelik bir el gönder.
2. Arkadaşlar seçtikleri kelimeyi hakeme DM'ler. Hakem, üçüncü bir arkadaş ya da oynayan arkadaşlardan biri olabilir.
3. Arkadaşlar tuzağı Discord'un **yazılı** chat'inden kurar, çünkü gerçek izleyiciler de yazarak tuzak kuruyor. Sesle "pineapple de" demek oyunu bozar.
4. Sen yazılanları sesli okuyup sohbet edersin. Hakem kelimeyi duyunca "BOOM" der.
5. Not al:
   - ilk patlamaya kadar geçen süre;
   - chat'i sesli okumak en kolay tuzak mı, eğlenceli mi yoksa ucuz mu;
   - arkadaşlar ikinci tur istiyor mu?
6. Ortalama patlama süresi 5 dakikayı geçiyorsa desteye biraz daha yaygın kelimeler eklenir.
7. Opsiyonel kural, T0'a göre karar verilecek (D8): kendi kelimesini chat'e yazan mayınını kaybeder.

### İnsan saati
29 Ekim 4 + 30 Ekim–1 Kasım 14,5 + kayıt 2 + montaj ve teslim 4 ≈ **24,5 saat**. Bu, 20–25 saatlik bütçenin içinde ama üst sınırında. Tampon (2,5) kullanılmazsa ~22'ye iner.

Sıkışırsan kesilecekler, sırasıyla:
1. dud gösteriminin animasyonu (düz liste);
2. overlay'deki QR (bot cevabındaki link yeter);
3. marker (videoda görünmüyor).

---

## 7. Testler ve ölçütler

| Test | Ne zaman | Hedef | Kötüyse |
| --- | --- | --- | --- |
| **T0** kodsuz oyun | 29 Ekim akşam | Gülüş; ilk patlama makul sürede; arkadaşlar ikinci tur istiyor | Kurallar değişir: mayın sayısı, kurulma süresi, deste zorluğu |
| **T5** klip ve marker | 29 Ekim | Klip doğru anı içeriyor; OBS'ten WSL'deki sunucuya erişiliyor | `duration` ya da çağrı zamanı ayarlanır |
| **T1** harness ilk koşusu | 30 Ekim akşam | ≥%80 isabet · **4 canlı mayına göre** 10 dk'da ≤1 yanlış alarm (kayıt b'de 0) · kelime bitişinden medyan ≤1,5 sn, en kötü ≤3 sn · OBS açıkken kare düşmesi yok · kelime bazında "fıss" oranı | Önce `replay` ile eşleştirici ayarı (`CONFIRM_N` 2 → 3, `MIN_WORD_PROB`); tanıma kötüyse `--backend nova3` ile aynı kayıtlar tekrar; sorunlu kelimeler desteden çıkar |
| **T4** ekme sayfası | 31 Ekim | Arkadaşın telefonundan uçtan uca bir mayın | Discord + mod yolu: arkadaş kelimeyi mod rolündeki kişiye iletir, o da dock'a girer |
| Prova | 1 Kasım öğlen | "Konuşmayı yaz" + debug ekleme ya da bir arkadaşla: 2 tur kesintisiz | Dondurmadan önce düzelt, yoksa kes |

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
  - Buraya yaz: `SESSION ID: ____`.
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
| 5 | Overlay ekran görüntüsüyle düzeltme | 1 Kasım (WP3 tam / WP13) | OBS'teki overlay'in ekran görüntüsü Codex'e verilir |
| 6 | PR'da `@codex review` | M1 ve M3 sonunda (2 PR) | Kilometre taşı dalı → PR → yorum |
| 7 | Session ID | 2 Kasım | `/status` ya da status line |

Harness döngüsü istemi:
```
Run `uv run python -m minefield.harness run --wav data/recordings/c.wav --labels data/recordings/c.labels.json --deck deck/en.json --save-hyps data/hyps/c.jsonl`.
Read the report. Propose at most 3 changes to minefield/core/config.py or deck variants,
verify each with `harness replay`, keep only changes that improve hits without raising
normalized false alarms, and commit the new report under reports/.
```

Kullanılmayacaklar: Codex'i ürünün içinde çalıştırmak (yapay görünür), Codex cloud görevleri (kayıtlar ve token'lar yerelde), skills, hooks, MCP.

### Ekran kaydı
**Ne:**
- Sadece Codex uygulamasının penceresi.
- Masaüstünün tamamı değil: e-posta, bildirim ya da başka bir pencere görünmesin.

**OBS kurulumu (bir kez, ~10 dk):**
- Ayrı bir **"Codex" sahnesi** oluştur; içinde Codex uygulaması için tek bir **Window Capture** kaynağı olsun.
- Uygulama: koyu tema, kod fontu 16 pt (şu an 14), pencere büyük. 1080p'de satırlar okunmalı.
- Kayıt ayarları:
  - **kayıt formatı:** `mkv` (çökmede dosya bozulmaz; montajdan önce Dosya → Remux ile mp4'e çevrilir);
  - **çözünürlük:** 1080p;
  - **kare hızı:** 30 fps;
  - **kodlayıcı:** NVENC.
  - Terminal görüntüsü az değiştiği için dosyalar küçük kalır.
- Yayın yaparken Codex kaydı alınmaz. Yayın ve oyun kayıtları ayrı bir iş (bölüm 9).

**Ne zaman:** Codex'le çalışmaya oturduğun an kayda bas, kalktığında durdur. Seçmeye çalışma; hepsini kaydet, montajda kırp. 4 günde ~15 saatlik kayıt birikir. "Codex anları" tablosu sayesinde montajda sadece işaretli dakikalara bakarsın.

**İlginç bir an olduğunda:** Saati ve ne olduğunu aşağıdaki tabloya bir satırla yaz. Bunun için 10 saniye yeter. Yukarıdaki 7 an, hedeflenen anlar.

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
| 0:00 | Soğuk açılış: sohbet, "pineapple" BOOM, afiş, çipte isim. **Kelime → BOOM arası kesilmez**, köşede gecikme rozeti. | Arkadaşların gerçekten seçtiği kelimeler; birkaç tur çek, en iyisini koy |
| 0:08 | Başlık kartı | — |
| 0:12 | Telefonda QR → kart → kopyala → chat'te `!mine K7QF` → çipte isim | Arkadaşın telefonunun ekran kaydı |
| 0:35 | İki tuzak: biri tutar, biri tutmaz | — |
| 1:00 | "Fıss" ya da False alarm gag'i | — |
| 1:20 | Chat'teki klip linkine tıklanır, klip 2 sn oynar | twitch.tv kaydı |
| 1:30 | Tur sonu: dud'lar | — |
| 1:45 | Kaputun altı: akan STT (Deepgram Flux), iki tahmin onayı, GPU gerekmez; harness tablosu | `reports/` |
| 2:10 | Codex bölümü (20–30 sn), `/status`'ta session ID | Bölüm 8'deki kayıtlar |
| 2:40 | Kapanış: repo linki. Video en fazla 2:50. | — |

**Twitch'te geçtiğinin kanıtı:** Kural "footage that shows the Project functioning on Twitch" istiyor. Kayıt gecesi OBS kaydına ek olarak ikinci bir cihazdan ya da tarayıcı penceresinden **twitch.tv/kanalın + chat** de kaydedilir. Soğuk açılış ve en az bir patlama bu görüntüden de gösterilir.

**Dürüstlük:**
- "Konuşmayı yaz" modu videoda gerçek STT gibi gösterilmez; gösterilirse "typed fallback" diye etiketlenir.
- Devpost metninde şu cümleler olur: "Friends picked the words; I did not know them." ve "Typed fallback was not used in the video."
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
- **Twitch:** Bot mod (link engelinden ve AutoMod'dan muaf); test hesaplarının chat'e yazabildiğini kontrol et.
- **Başlatma:** WSL'de `scripts/run_all.sh`, Windows Chrome'da `http://localhost:8000/mic` (sekme kayıt boyunca açık kalır; OBS ile aynı mikrofon seçili). Dock'taki ışıklar yeşil olmadan kayda başlama.

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
| D4 | Ekme sayfasında Twitch girişi yerine chat kodu (`!mine KOD`), kopyala düğmesi, QR, 5 dk geçerlilik | **Öneri.** İnceleme kabul etti; senin onayını bekliyor. | — |
| D5 | Teknoloji: Python 3.12 + uv + FastAPI; overlay, dock ve sayfa framework'süz HTML/JS | Verildi | 28 Ekim |
| D6 | Herkese açık adres: cloudflared quick tunnel (WSL'de), sadece ekme sayfası portu | Verildi | 28 Ekim |
| D7 | Ana yapım tek Codex thread'inde; yan thread sadece ana thread beklerken | Güncellendi (sadeleştirme) | 28 Ekim |
| D8 | Kurallar (mayın sayısı, kurulma süresi, "kendi kelimesini yazan kaybeder") | T0'dan sonra | — |
| D9 | False alarm: patlamadan sonraki 10 sn içinde; patlama sayılmaz, klip açılmaz, sahibi yeniden ekebilir. Patlama mesajı beklemeden gider. | Verildi (inceleme + sadeleştirme) | 28 Ekim |
| D10 | "Zaman kalırsa" listesi kaldırıldı; dondurmadan sonraki zaman videoya | Verildi | 28 Ekim |
| D11 | Sadeleştirmeler ([bölüm 13](#13-sadeleştirmeler-28-ekim)) | Verildi | 28 Ekim |
| D12 | Eşleştiricide onay sayısı ayarlanabilir (`CONFIRM_N`, varsayılan 2); Deepgram'ın ham mesajları ve tahminler kaydedilir; rapordaki tahmin dosyaları commit'lenir ki `replay` anahtarsız çalışsın | Verildi | 28 Ekim |
| D13 | Codex: masaüstü uygulamasında (ajan WSL'de) tek ana thread; her WP'de önce testler, `/review`, commit, `/compact`; harness döngüsü ana hikâye; M1 ve M3'te `@codex review`; çalışırken sürekli ekran kaydı | Verildi | 28 Ekim |

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
| 12 | Video Twitch'te geçsin, kesintisiz an, klip linki, `/status` | ✅ Alındı |
| 13 | CPU modu + GPU'suz demo yolu | ✅ Alındı (WP14); STT bulut olunca CPU modu gereksizleşti, anahtarsız demo yolu kaldı |
| 14 | Klip mesajını ikiye böl | ✅ Alındı. Create Clip From VOD **alınmadı**: beta sırasında `vod_offset` kayması bildirilmişti. |
| 15 | Demo günü kontrol listesi | ✅ Alındı |
| 16 | 29 Ekim gizli adımları (2FA, e-posta, redirect alanı) | ✅ Alındı |
| 17 | AGENTS.md test ve bağımlılık kuralları | ✅ Alındı, bir farkla: `silero-vad` pip paketi de torch çekiyor. Bu yüzden VAD doğrudan onnxruntime ile çalıştırılacaktı; STT bulut olunca VAD de çıktı. |
| 18 | Ekme uygulaması 127.0.0.1'de | ✅ Alındı |
| 19 | T0 protokolü | ✅ Alındı. "Kendi kelimesini yazan kaybeder" kuralı T0'a bırakıldı (D8). |
| 20 | Dil ve dürüstlük notu | ✅ Alındı |
| 21 | Deste dengesi (6 kart kalsın) | ⏸ Kısmen: kural değişmedi; T0'da patlama süresi 5 dk'yı geçerse desteye yaygın kelimeler eklenir. |
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
| DEFUSE | 10 sn'lik pencere boyunca mayın "hâlâ canlı"; patlama mesajı ve klip pencereyi bekliyor | Patlama mesajı hemen gider; klip 10 sn'lik bir zamanlayıcıyla açılır; "False alarm" bu süre içinde basit bir geri alma | Durum makinesinden bir durum ve bir mesaj türü çıktı; chat'teki tepki hızlandı. |
| Codex yan thread'leri | Overlay ve ekme sayfası paralel | Varsayılan tek thread | Darboğaz senin dikkatin. |

**Bilerek kalanlar** (karmaşık görünse de puan getiriyor):
- **Akan tanıma, iki tahmin onayı, kıvılcım ve "fıss":** ürünün kendisi; zamanlama Design puanını taşıyor.
- **Harness:** Tech kriterinin kanıtı ve videodaki Codex hikâyesi.
- **Ekme sayfası ve chat kodu:** "izleyici gizlice seçti" fikrinin videodaki kanıtı.
- **Klip linki ve gecikme rozeti:** "Twitch'te çalışıyor" ve "hızlı" kanıtları.
- **Marker:** ucuz ve yayıncıya gerçekten faydalı; sıkışırsa ilk kesilecek.

STT kararı (D3) ayrı araştırmalarla verildi: [stt-cloud-options.md](stt-cloud-options.md), [stt-research.md](stt-research.md).
