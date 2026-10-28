# Codex kullanımı: kurallar, özellikler ve puan stratejisi

Hazırlanma tarihi: 28 Ekim 2026. Bu doküman [minefield.md](minefield.md) §8'in arka planıdır. Kararlar §8'e süzülerek işlendi; ikisi çelişirse §8 geçerli.

Etiketler:
- **[kanıt]**: resmî kaynak (Devpost kuralları, SSS, güncellemeler, OpenAI dokümanı) ya da bu makinede doğrudan gözlem.
- **[zayıf kanıt]**: üçüncü taraf blog, ayna site ya da birbiriyle çelişen kaynaklar.
- **[tahmin]**: benim çıkarımım.

---

## 1. Özet

**Yapılması zorunlu olanlar:**
1. **Tek bir ana thread aç ve işin çoğunu orada yap.** Teslimde bu thread'in session ID'si istenecek. Devpost'un 26 Ekim güncellemesi bunu açıkça söylüyor: *"Try to keep your main build in one thread."* **[kanıt]** ID'yi ilk gün kaydet; CLI'da nasıl görüneceği aşağıda (madde 6).
2. **Videoda Codex görüntüsü olmalı.** Kural: *"Should include footage that shows how the project was built with Codex"*. 28 Ekim güncellemesi: *"Make Codex visible. Judges look at how well your project uses Codex. Say how you used it in your description, and show it in your video."* **[kanıt]** Bu yüzden ekran kaydı ilk günden açık olmalı.
3. **Devpost açıklamasında "Codex'i nasıl kullandım" bölümü olmalı.** Kural: *"explains the Project's features and functionality and how you used Codex"*. **[kanıt]**

**Ekstra puan getirenler** (Tech kriterinin "how well does it use Codex?" yarısı):

4. **Spec'ten çalışan kod.** Her WP tek bir komutla verilir: "do WP5". Codex önce SPEC.md'deki kabul kriterlerinden testleri yazar, testler kırmızı → yeşil olur, sonra WP önekli bir commit atılır. Sıradan bir sohbetle kod yazdırmaktan farklı ve görünür bir yöntem. **[tahmin]**
5. **Ölçüm döngüsü (asıl hikâye).** Codex harness'i çalıştırır, raporu okur, `config.py`'deki eşikleri değiştirir, `replay` ile saniyeler içinde yeniden ölçer. Rapor tablosunda önce/sonra farkı görünür. Bu, "AI kod yazdı"dan daha güçlü bir anlatı: Codex ürünün doğruluğunu ölçüp iyileştirdi. **[tahmin]**
6. **Codex code review.** Her kilometre taşının sonunda bir PR açılır ve PR'da `@codex review` çağrılır (toplam ~4–5 PR). GitHub'daki inceleme yorumu videoda 3–4 saniyelik iyi bir plan olur. **[tahmin; özelliğin varlığı kanıt]**
7. **Ürünün içinde Codex: kullanma.** Minefield'in çalışma anında Codex'e ihtiyacı yok. Zorla eklemek dürüst olmaz ve jüriye yapay görünür. **[tahmin]**
8. **Puan ölçeği:** Tech kriteri 4 kriterden biri ve "iyi yapılmış mı" ile "Codex'i iyi kullanıyor mu" arasında bölünüyor. Yani Codex'e doğrudan bağlı puan, istekte varsayılan 5/20 değil, muhtemelen **~2,5/20**. Ama Stage One'da "reasonably applies the required developer tools" bir geçti/kaldı eşiği; burada eksik kalmak daha pahalı olur. **[kanıt: kriter metni; ağırlık bölüşümü tahmin]**

---

## 2. Kurallar ne diyor

Kaynaklar: `docs/competition/*.md` (yerel kopya) ve 28 Ekim'de çekilen Devpost sayfaları.

### Kurallar (Official Rules)
- Proje tanımı: *"Entrants must build for streamers and their community on www.twitch.tv ("Twitch") with OpenAI Codex"* **[kanıt]**
- Teslim:
  - *"Include a text description that explains the Project's features and functionality and how you used Codex."*
  - *"Provide the Codex session ID for the Codex thread where the Project was built."* **[kanıt]**
- Video:
  - *"should be less than three (3) minutes. Judges are not required to watch beyond three minutes"*
  - *"should include footage that shows the Project functioning on Twitch"*
  - *"Should include footage that shows how the project was built with Codex"* **[kanıt]**
- Stage One (geçti/kaldı): *"whether the ideas meet a baseline level of viability, in that the Project reasonably fits the theme and reasonably applies the required developer tools featured in the Hackathon."* **[kanıt]**
- Stage Two kriteri: *"Technological implementation: How well is it built, and how well does it use Codex?"* Dört kriter eşit ağırlıklı. **[kanıt]**
- Değerlendirme yöntemi: *"This process may utilize expert panels, peer review, automated AI-driven analysis, or any combination thereof"* **[kanıt]**
  - Bundan çıkan sonuç: thread'in kendisi bir model tarafından okunup özetlenebilir. Thread'deki istemler net olmalı (WP kimlikleri, kabul kriterleri, test çıktıları). **[tahmin]**
- *"Judges are not required to test the Project and may choose to judge based solely on the text description, images, and video provided in the Submission."* **[kanıt]**
  - Codex kullanımı büyük olasılıkla **video ve açıklamadan** değerlendirilecek; thread ise ikincil bir kanıt. **[tahmin]**

### Genel bakış sayfası ve SSS
- *"Codex Session ID. Provide the Codex session ID for the thread where you built most of your project (type /status in Codex to see it). If you used multiple threads, include the one where most of the build happened."* **[kanıt]**
- *"I used several Codex threads. Which session ID do I submit? The one for the thread where you built most of your project."* **[kanıt]**
- *"Can I use other AI tools too? Yes. ... Your project must be built with Codex, and Codex use is part of the Technological Implementation criterion."* **[kanıt]**
- *"How much can Codex build for me? As much as helps. ... You direct the idea and the decisions. Be ready to explain how your project works."* **[kanıt]**
- *"Do I need a paid Codex plan? No. Use the free version of Codex. Free usage has limits..."* **[kanıt]**

### Devpost güncellemeleri
- **26 Ekim**, "Start building with Twitch": *"Keep your Codex thread. You'll submit the Codex session ID for the thread where you built most of your project. Type /status in that thread to find it. Try to keep your main build in one thread."* **[kanıt]**
- **28 Ekim**, "5 days left": *"Make Codex visible. Judges look at how well your project uses Codex. Say how you used it in your description, and show it in your video."* **[kanıt]**
- **Discussions**, "Codex Credits": yönetici yanıtı, *"There are no credits or promo codes available for this hackathon."* **[kanıt]**

### Belirsizlikler
- **"Built" mi, "built most" mu?** Kurallar "the Codex thread where the Project was built" diyor (tek thread ima ediyor). SSS ve güncellemeler "most of" diyor. Pratikte tek ID girilir; diğer thread'ler açıklamada anılabilir. **[kanıt: iki metin; yorum tahmin]**
- **`/status` ID gösteriyor mu?**
  - Resmî CLI dokümanı `/status`'u şöyle tanımlıyor: *"Display session configuration and token usage"*. ID'den söz etmiyor.
  - IDE uzantısı dokümanı *"the chat ID, context usage, and rate limits"* diyor.
  - Üçüncü taraf bir blog CLI'da da session ID gösterdiğini söylüyor.
  - Sonuç: 29 Ekim'de denenecek. Yedekler aşağıda (madde 6, bölüm 3). **[kanıt: dokümanlar çelişiyor]**
- **Jüri thread'i nasıl görecek?** ID ile thread'e OpenAI tarafında erişilip erişilemediği yazılı değil. Yerel CLI oturumları diskte `~/.codex/sessions/` altında tutuluyor, ama modele giden istekler OpenAI'dan geçiyor. **[tahmin]**
- **Videoda "built with Codex" yazısı şart mı?** Böyle bir metin şartı yok. Şart olan, Codex ile yapımın **görüntüsü**. **[kanıt]**
- **Son teslim saati:** Devpost başlığı *"Nov 2, 2026 @ 2:00pm PST"* diyor; bu 22:00 UTC, yani 3 Kasım 01:00 TSİ. SSS *"9:00 PM UTC"* diyor; bu da 00:00 TSİ eder (yaz saati 1 Kasım'da bittiği için SSS muhtemelen hatalı). Plandaki **23:00 TSİ** iki yoruma göre de güvenli. **[kanıt: iki metin]**

---

## 3. Codex özellikleri ve hangisini nasıl kullanmalıyız

Bu makinede gözlenenler **[kanıt]**:
- `codex-cli 0.155.1` kurulu, `~/.codex/config.toml` dosyasında `model = "gpt-5.6-sol"`.
- Oturumlar `~/.codex/sessions/YYYY/MM/DD/rollout-<zaman>-<UUID>.jsonl` dosyalarında; dosyanın ilk satırı `session_meta` ve `"id":"<UUID>"` içeriyor.
- Özellikler: `multi_agent` stable/true, `hooks`, `goals` ve `plugins` stable. `web_search_request` deprecated; yerine üst düzeyde `web_search = "live"` kullanılıyor.
- `~/.codex/config.toml`'da bu proje (`/home/furkankuscu08/projects/twitch`) henüz "trusted" değil.

| Özellik | Ne yapar | Minefield'de nasıl | Efor | Jüri değeri |
| --- | --- | --- | --- | --- |
| **Codex CLI** (WSL'de) | Terminal ajanı; yerel dosyalarda çalışır, komut çalıştırır | **Ana yüzey.** GPU, mikrofon kayıtları ve Twitch token'ları yerelde olduğu için bulut görevleri işe yaramaz. | yok (kurulu) | Temel |
| **AGENTS.md** | Her oturumda otomatik okunan kurallar; code review de en yakın AGENTS.md'yi uygular **[kanıt]** | Hazır. Code review için kısa bir `## Review guidelines` bölümü eklenebilir (gizlilik, `core` saflığı). Ekleme kararı senin. | 5 dk | Orta: "spec-driven" anlatısının parçası |
| **`/plan`** | Uygulamadan önce plan ister **[kanıt]** | Thread'in ilk mesajı: "Read AGENTS.md and SPEC.md, point out gaps, then plan WP7 and WP8". Codex'in spec'i eleştirmesi gerçek ve görünür bir katkı. | 5 dk | Yüksek (videoda ilk sahne) |
| **`/goal`** | Uzun işte kalıcı bir hedef tutar **[kanıt]** | `/goal Build Minefield per SPEC.md WP1–WP14; each WP done = acceptance + pytest + ruff clean`. Compaction sonrasında da yön kaybolmaz. **[tahmin]** | 1 dk | Düşük–orta |
| **Testler önce** | (özellik değil, istem kalıbı) | "Do WP1. First write failing tests from the §8 acceptance list, run them, then implement." Kırmızı → yeşil çıktısı kayda girer. | 0 | Yüksek |
| **Harness döngüsü** | (istem kalıbı) | WP6 sonrası: "Run harness on a.wav, read the report, propose config changes, verify with replay, commit the report." Rapor `reports/` altına commit edilir (SPEC §2). | WP6'nın içinde | **En yüksek**: ölçülebilir sonuç |
| **Alt ajanlar** (`multi_agent`) | Ana thread'den paralel alt thread'ler; CLI'da `/subagents` ile izlenir; daha çok token harcar **[kanıt]** | Sadece bağımsız işlerde, ana thread içinden: ör. WP3 (overlay) + WP4 (dock), WP11'in web kısmı. Alt ajanlar ana oturumdan doğduğu için iş ana thread'de kalır. **[tahmin]** | düşük | Orta: "orchestration" görünür |
| **`/review`** ve `codex review --uncommitted` | Çalışma ağacını yerelde inceler **[kanıt]** | Her WP'nin sonunda, commit'ten önce. Genel kullanım limitinden düşer **[kanıt]**. | 1–2 dk/WP | Orta |
| **GitHub code review** (`@codex review`) | PR'da inceleme; sadece P0/P1 bulguları; AGENTS.md'yi okur **[kanıt]** | Her kilometre taşında bir dal ve bir PR (M1–M5), sonra `@codex review`. Repo private olabilir. Kurulum: Codex cloud'da repo bağlantısı + chatgpt.com/codex/settings/code-review. | 15 dk kurulum + 2 dk/PR | Yüksek: GitHub'da görünür, videoya girer |
| **`/compact`** | Görünür sohbeti özetleyip token açar **[kanıt]** | Her WP bitiminde, commit'ten sonra. Codex'in kendi uyarısı: *"Long threads and multiple compactions can cause the model to be less accurate"* **[zayıf kanıt]**. Kalıcı hafıza AGENTS.md, SPEC.md ve git log. | 0 | Yok (risk yönetimi) |
| **`/side`** | Ana sohbeti bozmadan geçici yan sohbet **[kanıt]** | Kısa sorular için ("EventSub keepalive nedir?"). Ana thread'in bağlamını şişirmez. | 0 | Yok |
| **`/new`, `/fork`** | Yeni sohbet / dal **[kanıt]** | **Ana thread'de kullanma**: yeni bir ID üretirler. Ana thread'den çıkarsan `codex resume <UUID>` ile geri dön. **[tahmin: ID davranışı]** | — | Risk |
| **Web arama** | `web_search = "cached"` (varsayılan) ya da `"live"` **[kanıt]** | Twitch dokümanı doğrulaması için `.codex/config.toml` içinde `web_search = "live"`. AGENTS.md "verify against dev.twitch.tv" diyor. | 1 dk | Orta: "Codex verified Twitch docs" |
| **Sandbox / onay** | `workspace-write` varsayılan olarak ağı kapalı tutar; `[sandbox_workspace_write] network_access = true` açar **[kanıt]** | `uv sync` ve Helix testleri için ağ açık. `/permissions` → Auto. | 2 dk | Yok |
| **Görsel girdi** (`view_image`) | Ekran görüntüsünü bağlam olarak alır **[kanıt]** | WP3/WP13: OBS'teki overlay'in ekran görüntüsü verilir, "fix the banner overlap" denir. Videoda iyi ve dürüst bir an. | 0 | Orta |
| **Skills** (`.agents/skills/<ad>/SKILL.md`) | Tekrar eden iş akışı paketi **[kanıt]** | İsteğe bağlı: `wp-done` skill'i (pytest → ruff → `/review` → WP önekli commit). 4 gün için gerekli değil. | 15 dk | Düşük–orta |
| **Hooks** | Olaylara bağlı komut **[kanıt: özellik açık; ayrıntı doğrulanmadı]** | Gerek yok; ruff/pytest zaten WP tanımında. | — | Düşük |
| **MCP** | Dış araçlar | Gerek yok. Twitch için resmî bir MCP aramadım; doğrudan Helix + `respx` yeterli. | — | Düşük |
| **Codex cloud görevleri** | Uzak ortamda görev | Ana iş için **kullanma**: GPU, ses kayıtları ve token yok. Code review için repo bağlantısı yeterli. | — | Düşük |
| **Codex'i çalışma anında kullanmak** | (`codex exec` vb.) | **Yapma.** Ürünün buna ihtiyacı yok. | — | Negatif risk |

---

## 4. Önerilen çalışma akışı

### Kurulum (29 Ekim, ~20 dk)
1. Proje için `.codex/config.toml` ya da kullanıcı config'inde `web_search = "live"` ve `[sandbox_workspace_write] network_access = true` ayarlanır. Proje trust edilir (Codex ilk açılışta sorar).
2. Repo GitHub'a (private) itilir; `testing@devpost.com` hemen eklenir. Codex cloud'da repo bağlanır ve Code review açılır. Automatic reviews kapalı kalır, çünkü limit tüketir; inceleme elle `@codex review` ile istenir.
3. OBS'te Windows Terminal için bir kayıt sahnesi: büyük font (16–18 pt), koyu tema. 1080p'de okunur olmalı.
4. Ana thread açılır, ilk mesaj gönderilir, sonra **ID kaydedilir**:
   - `/status`; ID görünmüyorsa `/statusline` ile "session id" öğesi eklenir **[kanıt: dokümandaki seçenek]**;
   - ya da en yeni `~/.codex/sessions/.../rollout-*-<UUID>.jsonl` dosyasının ilk satırındaki `id`.
   - ID [minefield.md](minefield.md) §8'e yazılır.

### Thread düzeni

| Thread | Ne | Neden |
| --- | --- | --- |
| **A: "Minefield build"** (CLI, WSL, repo kökü) | WP7, WP8, WP1–WP6, WP9–WP11, WP13, WP14 ve bütün birleştirmeler. Paralel iş **bu thread'in içinden alt ajanlarla** yapılır. | Teslimdeki tek ID. Kural ve güncelleme "one thread" diyor. |
| `/side` sohbetleri | Kısa sorular | Ana bağlamı korur; ayrı bir thread sayılmaz **[tahmin]**. |
| **B: yedek** (sadece gerekirse) | Thread A bozulursa ya da compaction hatası olursa (bu türden hatalar raporlanmış **[zayıf kanıt]**) | Teslimde işin çoğunun yapıldığı thread verilir; B açıklamada ve README'de anılır. |
| GitHub PR'ları | `@codex review` | Thread değil; ayrı bir Codex yüzeyi olarak görünür. |

### WP sırası ve ritim (her WP için aynı döngü)
1. `Do WP<n> per SPEC.md §8. Write failing tests from the acceptance list first.`
2. Codex testleri yazar → kırmızı → kodu yazar → `uv run pytest` ve `uv run ruff check` → yeşil.
3. `/review` çalıştırılır. Önemli bir bulgu varsa düzeltilir.
4. `WP<n>: ...` commit'i atılır (AGENTS.md kuralı).
5. `/compact`. Thread uzadıysa `/status` ile bağlam doluluğu kontrol edilir.

| Gün | Thread A'da | Code review | Kayıt |
| --- | --- | --- | --- |
| 29 Ekim | `/plan` ile spec eleştirisi; WP7, WP8 | — | İlk istem ve spec eleştirisi |
| 30 Ekim | M1 (WP1 testler önce; WP3 + WP4 alt ajanlarla paralel), M2 (WP5, WP6), **harness döngüsü** | PR "M1", PR "M2" | Kırmızı → yeşil; harness raporu önce/sonra |
| 31 Ekim | M3 (WP9, WP10: web aramayla Twitch doğrulaması), M4 (WP11) | PR "M3+M4" | Codex'in dev.twitch.tv'yi kontrol ettiği an |
| 1 Kasım | M5 (WP3 tam, WP13, WP14): overlay ekran görüntüsüyle düzeltme | PR "M5" | Görsel girdiyle düzeltme |
| 2 Kasım | Devpost metni için: "Summarize what you built in this thread, per WP" (dürüst, kontrol edilmiş bir taslak) | — | `/status` ID çekimi |

### Harness döngüsünün istemi (örnek)
```
Run `uv run python -m minefield.harness run --wav data/recordings/c.wav --labels ... --save-hyps data/hyps/c.jsonl`.
Read the report. Propose at most 3 changes to minefield/core/config.py or deck variants,
verify each with `harness replay`, keep only changes that improve hits without raising
normalized false alarms, and commit the new report under reports/.
```
Önce/sonra raporları `reports/` altında commit'li durur. Videoda ve README'de aynı sayılar kullanılır.

### Görüntü kaydı
- Her oturumda OBS kaydı açık; dosya adı `codex-YYYYMMDD-HHMM`.
- İlginç anlar [minefield.md](minefield.md) §8'deki "Codex anları" tablosuna saatiyle yazılır.
- Hedef: 5–6 klip, her biri 3–8 sn kullanılabilir.

---

## 5. Videoda ve README'de Codex'i nasıl göstermeliyiz

### Video (2:10–2:40 arası, ~25–30 sn)

| Süre | Görüntü | Altyazı / anlatım |
| --- | --- | --- |
| 3 sn | SPEC.md §8 tablosu → Codex'e "Do WP1…" istemi | "I wrote a spec with 13 work packages; Codex built each one." |
| 5 sn | Testler kırmızı → yeşil (hızlandırılmış) | "Tests first, from the acceptance criteria." |
| 8 sn | Harness: Codex raporu okur, config'i değiştirir, `replay` → tablo iyileşir | "Codex tuned the detector against my real recordings: hits X% → Y%." |
| 4 sn | GitHub PR'da `@codex review` yorumu | "Every milestone got a Codex code review." |
| 3 sn | Codex'in dev.twitch.tv'yi kontrol ettiği an ya da overlay ekran görüntüsünden yapılan düzeltme | "It checked Twitch's docs before touching the API." |
| 3 sn | `/status` (ya da status line'da session ID) | "Session ID in the submission." |

Kurallar:
- Hızlandırma serbest, ama gerçek oturumun kaydı olmalı. Sahne kurgusu yapılmaz. **[tahmin; dürüstlük]**
- Terminal metni okunur olmalı; gerekirse yakınlaştırma yapılır.
- Sayılar gerçek `reports/` dosyalarından alınır.

### README bölümü taslağı (İngilizce; WP14'te README'ye girer)

```markdown
## How this was built with Codex

Minefield was built in a single main Codex CLI thread (session ID: `<UUID>`),
driven by a written spec.

- **Spec-driven work packages.** `SPEC.md` defines 13 work packages (WP1–WP14) with
  acceptance criteria; `AGENTS.md` holds the project rules (secrecy, no persistence,
  pure `core`). Each package was one Codex task: "Do WPn". Every commit is prefixed
  with its WP id, so `git log` maps the build step by step.
- **Tests first.** For each package Codex wrote failing tests from the acceptance
  list, then the implementation, and ran `pytest` and `ruff` before committing.
- **Measured, not guessed.** Codex ran the accuracy harness on real stream
  recordings, read the report, tuned thresholds in `minefield/core/config.py`, and
  verified each change with `harness replay`. Before/after reports are in `reports/`.
- **Docs-checked Twitch code.** With web search on, Codex verified EventSub and Helix
  endpoints, scopes and payloads against dev.twitch.tv before writing them.
- **Reviewed.** Each milestone was a PR reviewed by Codex code review (`@codex review`),
  plus a local `/review` before every commit.
- **Parallel where it helped.** The overlay and the dock were built by Codex subagents
  launched from the main thread.

I designed the game, wrote the spec and made the decisions; Codex wrote the code.
```
Taslağı sadece gerçekten yaptıkların kalacak şekilde kırp. Örneğin alt ajan kullanmadıysan o madde çıkar.

**Plan ve inceleme için başka bir asistan:** SSS buna izin veriyor. Spec'in yazımında başka bir AI'ın rolünü Codex'e mal etme. Yukarıdaki "I … wrote the spec" cümlesi, spec'i senin yönetiminde yazdırdığın için savunulabilir; daha açık olmak istersen "with help from another assistant for planning" eklenebilir. Karar senin. **[tahmin]**

### Devpost açıklaması
Tech başlığının altında README'deki maddelerin 3–4 cümlelik özeti ve harness önce/sonra sayıları. Galeriye bir görsel: Codex thread'i + harness tablosu.

---

## 6. Riskler ve emin olunmayan noktalar

1. **Kullanım limiti (en büyük risk).** OpenAI'ın fiyat sayfasındaki Plus tahminleri (5 saatlik pencere) **[kanıt]**:
   - GPT-6 Astra: **5–45** yerel mesaj;
   - GPT-6.1 Sol: 15–160;
   - GPT-6.1 Terra: 35–285;
   - GPT-6 Luna: 350–3.000.

   Ayrıca: *"Weekly limits may also apply"*; ek kredi satın alınabilir. Code review GitHub'da ayrı sayılır; yerel `/review` genel limitten düşer.

   Öneri:
   - Varsayılan model Sol sınıfı kalsın (şu an `gpt-5.6-sol`). Astra'yı sadece zor hata ayıklamalarda kullan.
   - Her gün `/status` ve chatgpt.com/codex/settings/usage ile kontrol et.
   - 1–2 Kasım için pay bırak (SSS de bunu öneriyor). Gerekirse kredi al ya da Pro'ya geç.
   - Alt ajanlar daha çok token yer **[kanıt]**; az kullan.
2. **Tek uzun thread ve compaction.** 4 gün × ~13 WP tek bağlama sığmaz; birkaç compaction olacak. Codex'in kendi uyarısı ve topluluk raporları uzun, çok kez sıkıştırılmış thread'lerde kalite düşüşünü anlatıyor **[zayıf kanıt]**. Önlemler:
   - Her WP'den sonra commit + `/compact`; WP ortasında compaction'a izin verme.
   - Kalıcı hafıza dosyalarda: AGENTS.md, SPEC.md, git log.
   - `/goal` ile hedef sabitlenir.
   - Paralel işi alt ajanlara ver; ana bağlam küçük kalır.
3. **Ana thread bozulursa ya da işin çoğunu yansıtmazsa.** SSS birden fazla thread'e izin veriyor; "most of the build" olan ID verilir **[kanıt]**. Açıklamada ve README'de ikinci thread'in ID'si ve hangi WP'leri kapsadığı yazılır. Bunun puanı ciddi etkilemesi beklenmez; jüri büyük olasılıkla video ve açıklamaya bakıyor **[tahmin]**. Ana thread'de kod yazılmadan Claude'da yazılmış kod olursa iddia zayıflar. Plan bunu zaten yasaklıyor (kod sadece Codex'te).
4. **Session ID'nin biçimi ve yeri.** CLI'da `/status` ID'yi göstermeyebilir (dokümanlar çelişiyor). Yedekler: `/statusline` ve rollout dosyasındaki UUID **[kanıt: yerel gözlem]**. Videoda ID'yi göstermek için status line hazırlanmalı.
5. **`/new` ya da `/fork` ile yanlışlıkla yeni thread açmak:** ID değişir. Devam için her zaman `codex resume <UUID>` ya da `codex resume --last` kullan.
6. **Code review kurulumu.** Codex cloud repo bağlantısı ve GitHub izinleri gerekiyor; "Action required" izin sorunları raporlanmış **[zayıf kanıt]**. 15 dakikada çalışmazsa bırak; yerel `/review` yeter.
7. **Web arama ve prompt injection.** OpenAI canlı aramayı güvenilmeyen içerik sayıyor **[kanıt]**. Sadece dokümantasyon doğrulaması için kullanılır.
8. **[Çözüldü, 28 Ekim: SPEC ve AGENTS.md Deepgram'a göre güncellendi.]** **İstekle repo arasındaki tutarsızlık.** İstek "Deepgram streaming STT" diyor. `SPEC.md` ve `AGENTS.md` ise faster-whisper diyor; `stt-cloud-options.md` Deepgram Flux öneriyor. Harness döngüsü iki durumda da geçerli, ama hangisi seçilirse SPEC ve AGENTS.md güncellenmeli; yoksa Codex yanlış motoru kurar.
9. **Yargılama yöntemi bilinmiyor.** Thread'in okunup okunmadığı, kimin okuduğu (insan ya da AI) yazılı değil **[kanıt: kural sadece "may utilize"]**. Bu yüzden asıl kanıtı videoya ve açıklamaya koymak daha güvenli.
10. **Geçmiş Codex hackathon'larından ders.** OpenAI Build Week (Ağustos 2026) kazananları çalışan ürünler ve belli bir kitleye hizmetle öne çıkmış. İkincil kaynaklar, Codex'in ekibin uzmanlığı dışındaki işleri hızlandırdığı ve kararların insanda kaldığı anlatısını vurguluyor **[zayıf kanıt]**. Minefield'de karşılığı: Twitch API, ki sen Twitch'te yenisin, ve STT doğruluk ayarı.

---

## 7. Kaynaklar

**Hackathon (resmî):**
- Genel bakış ve teslim: https://twitchcon-codex.devpost.com/ (yerel kopya: `docs/competition/overview.md`)
- Kurallar: https://twitchcon-codex.devpost.com/rules (yerel kopya: `docs/competition/rules.md`)
- SSS ve kaynaklar: https://twitchcon-codex.devpost.com/resources (yerel kopya: `docs/competition/resources.md`)
- Güncelleme, 26 Ekim: https://twitchcon-codex.devpost.com/updates/47297-start-building-with-twitch-a-quick-guide-to-the-developer-tools
- Güncelleme, 28 Ekim: https://twitchcon-codex.devpost.com/updates/47340-5-days-left-lock-in-your-winning-idea
- Discussions, kredi yok: https://twitchcon-codex.devpost.com/forum_topics/45700-codex-credits-resources

**Codex (resmî):**
- CLI slash komutları: https://learn.chatgpt.com/docs/cli/slash-commands/
- CLI komutları ve IDE `/status` ("chat ID"): https://learn.chatgpt.com/docs/developer-commands?surface=cli
- Fiyat ve limitler: https://learn.chatgpt.com/docs/pricing.md
- Alt ajanlar: https://learn.chatgpt.com/docs/agent-configuration/subagents
- GitHub code review: https://developers.openai.com/codex/integrations/github.md
- Skills: https://developers.openai.com/codex/skills
- Config, web arama, sandbox: https://developers.openai.com/codex/config-basic, https://developers.openai.com/codex/agent-approvals-security
- Codex app (thread modları, worktree): https://developers.openai.com/codex/app

**Yerel gözlem:** `codex --version` (0.155.1), `codex features list`, `codex resume --help` ve `~/.codex/sessions/*.jsonl` içindeki `session_meta`.

**İkincil (zayıf kanıt):**
- Oturum yönetimi: https://codex.danielvaughan.com/2026/04/13/codex-cli-session-management-resume-fork-transcripts
- Compaction: https://codex.danielvaughan.com/2026/04/14/context-compaction-deep-dive-codex-cli-claude-code-opencode/
- Build Week kazananları: https://www.remio.ai/post/openai-build-week-winners-show-what-codex-can-build-beyond-demos
- Code review izin sorunu: https://community.openai.com/t/codex-in-github-not-reviewing-prs/1358847
