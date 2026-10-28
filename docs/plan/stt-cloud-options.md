# Bulut STT seçenekleri: Minefield için gerçek zamanlı konuşmadan yazıya

> Tarih: 28 Ekim 2026. Kapsam: `SPEC.md` §1, §5, §7 ve `docs/plan/stt-research.md` (yerel turbo araştırması). Bu dosya öneridir; SPEC, AGENTS.md, minefield.md ve stt-research.md değiştirilmedi.
>
> **Karar (28 Ekim, D3):** Flux birincil, Nova-3 yedek kabul edildi. Bölüm 1'deki 29 Ekim karşılaştırma testi **yapılmayacak**: ses beğenilmezse aynı anahtarla model değiştirilir. Mikrofon için relay yerine Chrome `/mic` sayfası seçildi.
>
> **Doğrulama (28 Ekim, EU uç noktası, Deepgram'ın örnek kaydının ilk 20 sn'si):** anahtar ve `wss://api.eu.deepgram.com/v2/listen` çalışıyor. `Update` aralığı medyan 0,248 sn (p90 0,283). `Update` mesajlarındaki kelimelerde `word`, `confidence`, `start`, `end` var. Kelimeler noktalama içeriyor (`"Yeah."`); normalizer temizliyor. Kelime bitişinden ilk görünmeye kadar geçen süre kabaca medyan ~0,1 sn, p90 ~0,4 sn (hızlı ölçüm, kendi sesimizle değil). 20 sn'lik kesintisiz konuşma tek bir turn olarak kaldı.
>
> İşaretler: **[kanıt]** resmî doküman, fiyat sayfası, SDK ya da bağımsız benchmark. **[zayıf kanıt]** ikincil kaynak, forum ya da üreticinin kendi iddiası. **[tahmin]** benim çıkarımım; 29 Ekim testinde doğrulanmalı.

---

## 1. Özet ve öneri

**Öneri: Birincil motor Deepgram Flux (`flux-general-en`, EU uç noktası). Yedek, aynı anahtar ve aynı adaptörle Deepgram Nova-3. Yerel faster-whisper turbo, ancak 29 Ekim testi Flux'ı eler ya da sonradan vakit kalırsa ikinci backend olarak yapılır.**

1. **Ara sonuç sıklığı bizim matcher'a en iyi uyan servis Flux.** Flux, her ~0,25 sn'lik ses için bir `Update` mesajı gönderiyor; transkript değişmese de gönderiyor **[kanıt: Flux state doc]**. Her `Update`'te kelime bazında `word`, `confidence`, `start` ve `end` var **[kanıt: Temmuz 2026 changelog]**. "İki ardışık hipotez" kuralı Flux'ta 0,5 sn değil ~0,25 sn bekleme demek. Kelime sonundan patlamaya tahminim **~0,5–0,8 sn [tahmin]**. Yerel turbo için tahmin ~0,9–1,3 sn idi.
2. **GPU, CUDA ve OBS çekişmesi tamamen ortadan kalkıyor.** D3'teki 45 dakikalık CUDA kontrolü, VAD, tampon yönetimi ve Whisper halüsinasyon süzgeçleri gerekmez. STT motoru için ayrılan 1–2 saate sığan tek seçenek bu: Codex için ~1–1,5 saat **[tahmin]**. Yerel motor tek başına bu bütçeyi aşıyordu.
3. **Maliyet sıfır sayılır.** Flux 0,0065 $/dk (promosyon fiyatı). 8 saat ses ≈ 3,1 $; MIP'ten çıkınca (aşağıda) en fazla ~6,2 $. Yeni hesaba 200 $ kredi veriliyor ve süresi dolmuyor **[kanıt: fiyat sayfası]**.
4. **Doğruluk konusunda tek çekince var.** Artificial Analysis'in akış benchmark'ında Flux'ın WER'i %7,36. Bu, ölçülen grubun en kötüsü; Nova-3 %6,7 **[kanıt]**. Pipecat benchmark'ında Nova-3 %1,62 ile iyi **[kanıt]** (Flux orada ölçülmemiş). Ama bizim işimiz tam transkript değil, 120 somut ismin tanınması. Aksanlı İngilizce için hiçbir sağlayıcıda sağlam bağımsız veri yok. **Bu yüzden karar 29 Ekim'deki 45 dakikalık teste bağlı** (aşağıda).
5. **Yanlış alarm riski muhtemelen Whisper'dan düşük.** Deepgram'ın modelleri Whisper gibi üretici (generative) bir kod çözücü değil. Sessizlik ve gürültüde "thank you for watching" türü uydurma çıktısı beklemiyorum **[tahmin; test (b) ile ölçülecek]**. Keyterm/prompt kullanmıyoruz; bu karar aynen kalıyor.
6. **Yedek: Nova-3** (`/v1/listen`, `interim_results=true`). Aynı hesap ve SDK kullanılır, adaptörün ~%70'i ortak **[tahmin]**. Ara sonuçlar daha seyrek, yaklaşık 1 sn'de bir **[zayıf kanıt: doküman örneğinde interim'ler 1,1 → 9,1 sn arasında ~1 sn adımlarla geliyor]**. Ama `is_final` kelimeleri değişmez. Bunun yerine Soniox (`stt-rt-v5`) ikinci en güçlü aday: Pipecat'te WER %1,27, TTFS 260 ms. Ancak ücretsiz kredisi belirsiz, EU uç noktası yok ve token'ları birleştirmek ek iş gerektiriyor.
7. **Demo günü güvenceleri:**
   - Dock'taki typed mode (zaten SPEC'te var).
   - Otomatik yeniden bağlanma.
   - `--backend nova3` bayrağı.
   - Yerel motora otomatik geçiş **yapılmaz**: 2 saatlik bütçeye sığmaz, canlı yayın sırasında GPU'da model ısıtmak da ayrıca risk.
8. **Pitch:** "Yerel, ses makineden çıkmıyor" iddiası kaybolur. Yerine daha güçlü bir Impact cümlesi gelir: **"GPU gerekmez; yayıncının GPU'su zaten oyun ve NVENC ile meşgul."** Ses zaten Twitch'te herkese açık yayınlanıyor; `mip_opt_out=true` ve EU uç noktasıyla gizlilik cevabı kısa olur. Tech puanı için: harness ölçüm tablosu, ve vakit kalırsa aynı WAV'lar üzerinde "Flux vs yerel turbo" karşılaştırması.

### 29 Ekim'de 45 dakikalık karşılaştırma testi

**Yer:** `minefield.md`'deki 29 Ekim planında 3. sıradaki CUDA kontrolünün 45 dakikası bu teste verilir. Kayıtlar (b) ve (c) gerektiği için 7. sıradan **sonra** yapılır.

**Hazırlık** (Codex ana thread'inde, WP7/WP8 ile paralel, ~20 dk Codex işi): `scripts/stt_probe.py`.
- Bir WAV'ı 80 ms parçalar halinde gerçek zaman hızında Deepgram'a gönderir: `--model flux` ya da `--model nova3`.
- Gelen her mesajı JSONL'e yazar: `recv_offset_s`, yani motor saatine göre sesin başından itibaren geçen süre, artı ham mesaj.
- İkinci küçük betik `probe_report.py`: deste kelimeleri için ilk görülme zamanını, ikinci ardışık görülme zamanını ve kelimenin `end` zamanını çıkarır. `end` olarak son (final/EndOfTurn) mesajdaki değer kullanılır. Bu, etiket olmadan kullanılabilecek bir vekil (proxy).

**Kayıtlar:**
- (c) deste kelimeleri kısa cümlelerde, ilk ~3 dk;
- (a)'dan 2 dk, kesintisiz sohbet;
- (b)'den 3 dk, sessizlik ve gürültü;
- yeni, 1 dk: içinde 10 deste kelimesi geçen, **duraklamasız** uzun bir konuşma.

**Ölçülecekler:**

| Ölçüt | Nasıl | Geçme şartı |
| --- | --- | --- |
| Recall | (c)'de söylenen deste kelimelerinin kaçı iki ardışık hipotezde görüldü | **≥ %90** |
| Onay gecikmesi | ikinci ardışık görülme − kelime `end` | **p50 ≤ 0,8 sn, p95 ≤ 1,3 sn** |
| Duraklamasız konuşma | aynı gecikme, 1 dk'lık kayıtta | p95 ≤ 1,5 sn; turn içinde takılma yok |
| Yanlış onay (konuşma) | söylenmeyen deste kelimesinin iki ardışık hipotezde görülmesi; 120 kelimenin hepsi kurulu sayılır | 6 dk'da **≤ 1** |
| Yanlış onay (sessizlik/gürültü) | (b)'de herhangi bir deste kelimesi | **0** |
| Bağlantı | 10 dk boyunca kopma, hata ve 10 sn timeout | 0 |

**Karar kuralı:**
1. **Flux bütün şartları geçerse** birincil motor Flux olur. CUDA kontrolü atlanır; yerel turbo "vakit kalırsa" listesine iner. Test toplam 10 dk'yı geçmez.
2. **Flux sadece recall'da kalırsa ve Nova-3 geçerse** birincil motor Nova-3 olur. Gecikme şartı Nova-3 için p95 ≤ 1,8 sn'ye gevşetilir, çünkü yerel tahmin de bu civardı.
3. **İkisi de recall'da kalırsa** iki yol var:
   - Kalan sürede Soniox denenir: aynı probe, `--model soniox`, ~15 dk.
   - Ya da 30 Ekim'de eski plana (yerel turbo, D3) dönülür. Bu durumda CUDA kontrolü o gün yapılır.
4. **Yanlış onay şartında kalan bir model hiçbir koşulda seçilmez.** Bir izleyicinin adını haksız yere vermek, kaçan bir kelimeden daha pahalı.
5. **Eşitlikte** sırayla gecikme, sonra entegrasyon kolaylığı belirler (Flux > Nova-3 > Soniox).

---

## 2. Karşılaştırma tablosu

Gecikme sütunu: "kelime bittikten sonra ara sonuçta görünmesi" ve "iki ardışık hipotezle onay". Bağımsız benchmark'lar (Pipecat TTFS, AA) **konuşma bittikten sonraki** final süresini ölçüyor; cümle ortasındaki kelime gecikmesini değil. Bu yüzden cümle içi değerlerin çoğu [tahmin].

| Seçenek | Ara sonuç sıklığı ve gecikme | Kelime zaman damgası ve güven skoru | Aksan ve isim doğruluğu | Yanlış alarm riski | Entegrasyon (saat) | Maliyet ve ücretsiz kredi (8 sa) | Demo günü riski | Pitch etkisi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Deepgram Flux** ✅ | ~0,25 sn'de bir `Update` **[kanıt]**; onay ~0,5–0,8 sn [tahmin]. AA'da en hızlı model (kısmi sonuç 0,019 sn) **[kanıt]** | Ara sonuçta da var (`word`, `confidence`, `start`, `end`) **[kanıt]** | AA WER %7,36, grubun en kötüsü **[kanıt]**. "Nova-3 kalitesi" iddiası **[zayıf kanıt]**. Aksan verisi yok | Düşük [tahmin]; üretici değil | ~1–1,5 | 3,1 $ (opt-out ile ≤6,2 $); **200 $ kredi** | Düşük-orta: yeni model; EU uç noktası var **[kanıt]** | No-GPU Impact; "ölçülmüş 0,x sn" |
| **Deepgram Nova-3** (yedek) | interim ~1 sn'de bir **[zayıf kanıt]**; `is_final` değişmez. Onay ~1–2 sn [tahmin] | Ara sonuçta da var **[kanıt]** | Pipecat WER %1,62, TTFS 247 ms **[kanıt]**; AA %6,7 | Düşük [tahmin] | ~1–1,5 (Flux'la ortak +0,3) | 2,3 $; 200 $ kredi | Düşük; olgun ürün | aynı |
| **Soniox stt-rt-v5** | Her yanıtta final olmayan token'lar; final ≥360 ms ile ayarlanabilir **[kanıt]**. ~0,5–0,9 sn [tahmin] | Token bazında `start_ms`, `end_ms`, `confidence` **[kanıt]**. Token'lar alt-kelime olabilir; birleştirme gerekir | Pipecat WER %1,27 **[kanıt]**; AA'da "en düşük doğruluk" %11,9 **[kanıt, çelişkili]** | Düşük-orta [tahmin] | ~1,5–2 | ~1 $; **kredi belirsiz** (Ekim 2025'te 200 $ kaldırıldı) **[zayıf kanıt]** | Orta: EU uç noktası dokümanda yok, ABD RTT'si | aynı |
| **AssemblyAI Universal-3.6 Pro RT** | "Continuous partials" ~1 sn'de bir; her mesaj tüm turn'ü baştan yazar **[kanıt]**. Onay ~1,5–2,5 sn [tahmin] | var (`start`, `end`, `confidence`) **[kanıt]** | **En iyi doğruluk**: Pipecat WER %0,96 **[kanıt]** | Düşük [tahmin] | ~1,5 | 3,6 $ (oturum süresine göre faturalanıyor, boşta geçen süre de dahil); **50 $ kredi** | Düşük; EU uç noktası var **[kanıt]** | aynı |
| AssemblyAI universal-streaming-english | `word_is_final` ile değişmez kelimeler **[kanıt]**; sıklık belgelenmemiş | var | Pipecat WER %3,02 | düşük | ~1,5 | 1,2 $; 50 $ kredi | Düşük | aynı |
| **Speechmatics** (Enhanced / linden-1) | Partial "<500 ms", final `max_delay` ≥ 0,7 sn **[kanıt]** | partial'larda var [hafıza, doğrulanmadı] | Pipecat WER %1,05 (linden-1) **[kanıt]**; aksan iddiası pazarlama | Düşük | ~1,5–2 | ~1,2–3,5 $; ayda 4 sa realtime ücretsiz **[kanıt, çelişkili]** | Düşük-orta | aynı |
| **ElevenLabs Scribe v2 Realtime** | Partial'lar hızlı (AA 0,13 sn) **[kanıt]** | **Partial'da zaman damgası yok**; sadece commit edilen sonuçta **[kanıt]**. Güven skoru yok | AA'da en iyi partial WER %3,65 **[kanıt]** | Düşük-orta | ~1,5 | ~3 $ | Orta | aynı |
| **OpenAI gpt-live-transcribe** (Realtime, transkripsiyon modu) | Delta'lar konuşma sürerken gelir; `delay` ayarı minimal…xhigh **[kanıt]**. Pipecat TTFS 740 ms (gpt-realtime-whisper) | **Kelime zaman damgası ve güven skoru yok** **[kanıt]** | AA'da kısmi WER %7,5 → final %5,1 (gpt-realtime-whisper) | Orta: üretici model, uydurma riski [tahmin] | ~2 (istemci VAD + commit, 24 kHz) | 8,2 $ (0,017 $/dk) | Orta; gpt-4o-transcribe delta'larının toplu geldiğine dair forum raporları var **[zayıf kanıt]** | "OpenAI" etiketi, ama Codex puanını etkilemez |
| Google Gemini 3.5 Transcribe Live | artımlı metin | **Kelime zaman damgası yok**, oturum ≤10 dk, Preview **[kanıt]** | Pipecat WER %2,24, TTFS 458 ms | Orta | ~2 | belirsiz | Yüksek (preview, 10 dk) | — |
| Google Chirp 3 streaming | interim var | **Akışta kelime zaman damgası yok** **[kanıt]** | AA'da VoxPopuli partial lideri | düşük | ~2,5 (GCP kurulumu) | düşük | Orta | — |
| Azure Speech | `Recognizing` olayları | ara sonuçta kelime yok [hafıza] | Pipecat WER %1,18, ama TTFS ~1 sn **[kanıt]** | düşük | ~2 | ayda 5 sa ücretsiz [hafıza] | Düşük | — |
| Gladia | partial var [zayıf] | belirsiz | bağımsız veri yok | ? | ~2 | ~6 $; 50 € tek seferlik kredi **[zayıf kanıt]** | Orta | — |
| **Yerel faster-whisper turbo** (önceki rapor) | 0,5 sn adım; onay ~0,9–1,3 sn [tahmin] | var (Whisper `word.probability`) | Kullanıcının aksanında GCP'de çok iyiydi **[kendi deneyimi]** | Whisper sessizlik ve gürültüde uydurabilir; süzgeç gerekiyor | ~3–4 + CUDA kontrolü [tahmin] | 0 $ | Orta: CUDA, OBS GPU çekişmesi | "Yerel, ses makineden çıkmıyor"; özel motor |

---

## 3. Açılara göre tartışma

### 3.1 Gecikme
- **Asıl ölçüt cümle içi gecikme.** Benchmark'lar konuşma bittikten sonraki final süresini ölçüyor. Bizim mayınlar çoğunlukla cümle ortasında. Burada belirleyici olan ara sonuç sıklığı ve onay kuralı.
- **Flux:** 0,25 sn'lik ritim belgelenmiş. İki ardışık `Update` ≈ kelime ilk göründükten 0,25 sn sonra onay. Ağ: Türkiye → AB bölgesi RTT'si ~40–70 ms [tahmin], ABD'ye ~150 ms [tahmin]. Flux için `wss://api.eu.deepgram.com/v2/listen` mevcut, ve AB uç noktası istekleri AB dışına yönlendirmiyor **[kanıt]**.
- **Nova-3:** interim'ler yaklaşık 1 sn'lik ses adımlarıyla geliyor **[zayıf kanıt: doküman örneği]**. İki interim beklemek 1–2 sn eder. Daha iyi yol: `is_final:true` olan kelimeleri tek başına onay saymak (bu kelimeler bir daha değişmez **[kanıt]**). Ancak final'ler ne sıklıkla geliyor, ölçülmeli.
- **AssemblyAI U3.6:** kesintisiz konuşmada partial ~1 sn'de bir geliyor ve her biri tüm turn'ü yeniden yazıyor **[kanıt]**. Bu tam bizim yerel tasarımımızın bulut hali, ama 2 kat yavaş ritimde.
- **Soniox:** final olmayan token'lar sürekli akıyor. `max_non_final_tokens_duration_ms` 360–6000 ms (varsayılan 4000) **[kanıt]**. Not: WebSocket referansı bu alanı yapılandırma alanı olarak listelemiyor, sadece hata mesajlarında geçiyor; doğrulanmalı. 360 ms'e çekilirse "final token = onay" mantığıyla ~0,5–0,9 sn [tahmin].
- **OpenAI:** `gpt-live-transcribe` delta'ları konuşma sürerken veriyor, ama zaman damgası yok ve istemci VAD'ı gerekiyor. Pipecat'te OpenAI modelleri en yavaş gruptan (TTFS 637–740 ms).

### 3.2 Ara sonuç anlamı
- **Flux:** turn içinde birikimli (cumulative), değişebilir transkript **[kanıt]**. Turn sınırları: `StartOfTurn`, `EndOfTurn` (`eot_threshold` 0,7 varsayılan, `eot_timeout_ms` 5000 varsayılan) **[kanıt]**. Uzun ve duraklamasız konuşmada turn'ün bir üst sınırı olup olmadığı belgelenmemiş **[belirsiz]**. Bizim için önemli değil: turn = utterance, ve occurrence kimliği (kelime, n).
- **Boş `Update`'ler var** (örnek kodda boş transkript atlanıyor) **[zayıf kanıt]**. Bunlar matcher'a gönderilmemeli; yoksa "sonraki hipotez" boş gelir ve gereksiz fizzle olur.
- **Nova-3:** her mesaj sadece son `is_final`'den beri olan bölümü taşır. Hipotez = o utterance'ın final kelimeleri + güncel interim. Final bölümler değişmez **[kanıt]**.
- **AssemblyAI:** "her Turn bir öncekinin yerine geçer" **[kanıt]**. Oturum 3 saatte kapanıyor; 5 dk'dan fazla işlenmemiş ses birikirse 3007 hatasıyla kapanıyor **[kanıt]**.
- **Soniox:** final token'lar bir kez gönderilir ve tekrarlanmaz; final olmayanlar her yanıtta yeniden gelir **[kanıt]**. Akış başına 300 dk sınırı var **[kanıt]**.
- **Bağlantı canlılığı:** Deepgram ses gelmezse bağlantıyı kapatır (yaklaşık 10 sn, NET-0001) [hafıza]. Relay sessizlikte de PCM gönderdiği için sorun olmaz. Ama motor relay'den ses alamazsa KeepAlive gönderilmeli ya da yeniden bağlanılmalı.

### 3.3 Aksan ve isim doğruluğu, yanlış alarm
- **Aksanlı İngilizce için bağımsız ve güncel bir karşılaştırma yok.** L2-ARCTIC çalışması (2025) okuma konuşmasında Whisper ve AssemblyAI'ı en iyi bulmuş. Deepgram ve Speechmatics için doğruluk vermemiş **[kanıt]**. Türkçe ana dilli konuşmacı bu korpusta yok.
- **Sonuç:** kendi kaydımız tek güvenilir veri. Bu yüzden 29 Ekim testi şart.
- **Somut isimler** (giraffe, spaghetti) Deepgram/Soniox tipi modellerde genelde sorun olmaz [tahmin]. Riskli olanlar:
  - kısa ya da başka kelimeye benzeyen isimler (ör. "bear" ↔ "bare");
  - çoğul ve bitişik yazım (deste varyantları zaten çözüyor).
- **Yanlış alarm, iki kaynaktan gelir:**
  1. Sessizlik ve gürültüde uydurma. Whisper/gpt-4o tipi üretici modellerde bilinen bir sorun. Deepgram'da daha az beklenir [tahmin].
  2. Benzer sesli kelimenin mayın kelimesi olarak yazılması. Bu her modelde olur; iki hipotez şartı ve `MIN_WORD_PROB` ile azalır.
- **Biasing yok:** keyterm/prompt kapalı kalır. Bonus: Flux'ta keyterm `Configure` ile akış ortasında güncellenebiliyor **[kanıt]**. Bu, "mayınlar değişince modeli güncelle" fikrini mümkün kılar; ama bilerek **kullanmıyoruz**.

### 3.4 Python entegrasyonu
- **Deepgram:** `deepgram-sdk` (PyPI 7.x) `AsyncDeepgramClient` → `client.listen.v2.connect(model="flux-general-en", encoding="linear16", sample_rate=16000)` **[kanıt: PyPI ve quickstart]**. SDK yerine doğrudan `websockets` ile bağlanmak da ~60 satır. SDK sürümleri arasında API çok değişti (v5 → v6 → v7), bu yüzden **ham WebSocket öneriyorum** [tahmin: Codex için daha az sürpriz].
- **Ses yolu değişmiyor.** Windows relay 16 kHz int16 PCM'i 20 ms'lik çerçevelerle WSL'deki motora gönderir. Motor 4 çerçeveyi birleştirip 80 ms'lik parça (2560 bayt) olarak Deepgram'a yollar. Önerilen parça boyu bu **[kanıt]**.
  - Relay'i doğrudan Deepgram'a bağlamak mümkün, ama harness'ın `--wav` yolu ve saat modeli için motor ortada kalmalı.
- **Soniox:** token birleştirme (boşluk token'ları, alt-kelime parçaları) ve final/final olmayan listelerin yönetimi gerekiyor: +30 dk.
- **OpenAI:** 24 kHz'e yeniden örnekleme, base64, istemci VAD'ı + `commit`. Kelime damgası olmadığı için bizim protokole ancak tahmini zamanlarla uyar: +1 sa.
- **Saat tahmini (Codex):**
  - Flux adaptörü + yeniden bağlanma + kaydedilmiş mesajlarla birim testi: ~1–1,5 sa.
  - Nova-3 modu: +0,3–0,5 sa.
  - Yerel turbo: ~3–4 sa (önceki rapor).

### 3.5 Maliyet
| Servis | Fiyat | 8 sa | Ücretsiz |
| --- | --- | --- | --- |
| Deepgram Flux | 0,0065 $/dk (promosyon) | 3,12 $ | 200 $, süresiz **[kanıt]** |
| Deepgram Nova-3 | 0,0048 $/dk | 2,30 $ | aynı |
| AssemblyAI U3.6 Pro / U-S English | 0,45 / 0,15 $/sa | 3,6 / 1,2 $ | 50 $ **[kanıt]** |
| Soniox | ~0,12 $/sa | ~1 $ | belirsiz |
| Speechmatics linden-1 | ~0,15 $/sa [zayıf] | ~1,2 $ | ayda 4 sa [çelişkili] |
| OpenAI gpt-live-transcribe | 0,017 $/dk | 8,2 $ | yok |
| ElevenLabs Scribe v2 RT | ~6,5 $/1000 dk [AA] | ~3,1 $ | plana bağlı |

- **Deepgram MIP:** opt-out edenler PAYG'deki "%50 indirimi" kaybediyor **[kanıt: Deepgram dokümanı/topluluk]**. Yani liste fiyatı veri paylaşımını varsayıyor olabilir **[belirsiz]**. 200 $ kredi her iki durumda da fazlasıyla yeter. `mip_opt_out=true` kullan.
- **Jüri çalıştırabilir mi?** Evet:
  - README'de `DEEPGRAM_API_KEY` ortam değişkeni ve "yeni hesap 200 $ kredi" notu.
  - Anahtar asla repoya girmez.
  - Anahtarsız yol 1: typed mode.
  - Anahtarsız yol 2: `harness replay` ile kaydedilmiş hipotez dosyaları. Öneri: birkaç küçük JSONL dosyası `reports/` altında commit'lenir ki ölçüm tablosu anahtarsız yeniden üretilebilsin.

### 3.6 Demo günü riski
- **Kesinti:** Deepgram ya da ağ giderse oyun durur. Önlemler:
  - dock'ta kırmızı ışık (SPEC'te zaten var: heartbeat);
  - typed mode;
  - `--backend nova3` ile yeniden başlatma (Flux'a özgü bir sorun varsa).
  - Deepgram durum sayfası demo öncesi kontrol edilir.
- **AB uç noktası:** bölge çökerse ABD'ye geçmiyor **[kanıt]**. Gerekirse `--region us` bayrağı (tek satır).
- **Hız limitleri:** PAYG WSS eşzamanlılığı 150 **[kanıt]**. Bize 1–2 bağlantı yeter.
- **Ağ:** 16 kHz PCM yukarı yönde 256 kbps; 6 Mbps'lik yayın yanında önemsiz. Jitter, gecikme p95'ini büyütür. Harness ve test bunu ölçer.
- **Yeniden bağlanma:** üstel geri çekilme (0,5 → 8 sn). Bağlantı kopunca açık utterance `final` sayılmaz, atılır. Açık spark'lar fizzle olur.
- **Anahtar:** `.env` dosyasında; `scripts/run_all.sh` yoksa açık bir hata verir.

### 3.7 Pitch ve jüri
- **Innovation:** etkilenmez. Yenilik oyunun kendisinde, STT motorunda değil.
- **Impact:** bulut daha güçlü.
  - Twitch yayıncılarının çoğu oyun oynarken GPU'yu tam kullanıyor. Yerel large-v3-turbo onlarda pratik değil.
  - "Herhangi bir PC'de, GPU'suz, ~0,5 $/yayın-saati altı maliyetle" (Flux ~0,39 $/sa) yayılabilir bir ürün cümlesi.
- **Tech:** Özel yerel motor daha etkileyici görünür; ama ölçülmüş gecikme/doğruluk tablosu, iki hipotezli eşleştirici ve replay harness'ı zaten güçlü. Bunlara bir de "değiştirilebilir backend + aynı WAV'larda karşılaştırma" eklenirse Tech kaybı küçük olur [tahmin].
- **Gizlilik ve ToS:** Yayıncının sesi zaten herkese açık yayında. Yine de:
  - sadece yayıncının mikrofonu gönderilir (Discord sesi gönderilmez, kayıt kuralı aynı);
  - `mip_opt_out=true` ile eğitimden çıkılır;
  - AB'de işlenir;
  - README'de bir cümleyle açıklanır.
  - Konuk ya da arkadaş sesi mikrofona girerse onların sesi de gider. Demo'da kulaklık kullanılmalı (zaten plan bu).

### 3.8 Hibrit seçenekler
| Seçenek | Değer | Maliyet | Karar |
| --- | --- | --- | --- |
| Tek arayüz (`Backend` protokolü), `--backend flux|nova3|whisper` | Yüksek: yedek ve karşılaştırma tablosu aynı koddan çıkar | +15 dk | **Yap** |
| Flux birincil + Nova-3 elle yedek | Orta | +0,3–0,5 sa | **Yap** (test sonucuna göre biri birincil olur) |
| Bulut birincil + yerel turbo otomatik yedek | Düşük-orta: canlı yayında GPU'da model sıcak tutulur, CUDA riski geri gelir | +3–4 sa | **Yapma** (teslim sonrası) |
| Yerel turbo, sadece harness karşılaştırması için | Pitch'e "neden bulut" kanıtı | +3–4 sa | Ancak 1 Kasım 17:00'den önce vakit kalırsa |
| İki bulut paralel ve oylama (Flux + Soniox) | Yanlış alarmı düşürebilir | +1,5 sa, iki anahtar | Yapma |

---

## 4. Seçilen sağlayıcı için entegrasyon taslağı (Deepgram Flux)

**Bağlantı:**
```
wss://api.eu.deepgram.com/v2/listen
  ?model=flux-general-en
  &encoding=linear16
  &sample_rate=16000
  &eot_threshold=0.7          # varsayılan; turn sonu sadece "final" zamanlamasını etkiler
  &eot_timeout_ms=3000        # 5000 yerine; uzun sessizlikte turn daha erken kapanır [tahmin, harness'ta dene]
  &mip_opt_out=true
Header: Authorization: Token $DEEPGRAM_API_KEY
```
- **Kapalı / verilmeyecek:** `keyterm`, `eager_eot_threshold` (EagerEndOfTurn/TurnResumed gereksiz). Flux'ta `smart_format`/`punctuate` gibi bayraklar yok; normalizer noktalama ve büyük harfi zaten temizliyor.
- **Dil:** `flux-general-en` sadece İngilizce; `language_hint` gerekmez.
- **Ses:** motor, relay'den gelen 20 ms'lik çerçeveleri 80 ms'lik (2560 bayt) ikili mesajlara birleştirir. `--wav` modunda aynı parçalar gerçek zaman hızında gönderilir.
- **Kapanış:** `{"type":"CloseStream"}`. Utterance zorla kapatılacaksa `ForceEndTurn` (örneğin tur sonunda).

**Saat modeli** (SPEC §4 ile uyumlu):
- `stream_start_wall` = ilk ses parçasının gönderildiği andaki motor saati. Mevcut saat modelinde karşılığı: `hello` zamanı + (o ana kadar alınan örnek sayısı) ÷ 16000.
- Deepgram'ın zamanları akış başına göre saniye [tahmin: `audio_window_start` ve kelime `start` akışa göre; ilk gün mesaj kaydından doğrulanacak].

**Mesaj → hipotez eşlemesi:**
| Flux olayı | Bizim hipotezimiz |
| --- | --- |
| `StartOfTurn` (turn_index = i) | yeni utterance: `utt_id = f"{session}-t{i}"`, `seq = 0`, `utt_start_wall = stream_start_wall + audio_window_start` |
| `Update` (words boş değilse) | `final: false`, `seq += 1`. Her kelime: `text = word`, `start = word.start − audio_window_start`, `end = word.end − audio_window_start`, `prob = confidence` |
| `Update` (words boş) | **gönderilmez** (matcher için "sonraki hipotez" sayılmaz) |
| `EndOfTurn` | aynı kelimelerle `final: true` |
| bağlantı koptu | açık utterance atılır; `session += 1` |

- **`compute_ms`:** bu alan "gecikme" anlamında kullanılır: `emitted_wall − (stream_start_wall + audio_window_end)`. Ağ ve sunucu gecikmesini gösterir. Heartbeat'te `rtf` yerine `lag_ms_p95`.
- **Süzgeçler:**
  - Bilinen halüsinasyon listesi kalır (ucuz).
  - "Konuşma oranı" ve `no_speech_prob` süzgeçleri bu backend'de yok.
  - Kendi Silero VAD'ımız da gerekmez.

**Matcher parametreleri** (hepsi `config.py`'de; `replay` ile ayarlanır):
| Parametre | Flux için başlangıç | Not |
| --- | --- | --- |
| Onay kuralı | 2 ardışık hipotez (değişmez) | Flux'ta 0,25 sn arayla. Replay'de yanlış onay çok çıkarsa `CONFIRM_N=3` (≈0,5 sn) eklenir: 5 satırlık bir değişiklik |
| `MIN_WORD_PROB` | 0,6 [tahmin] | Deepgram güven skorları Whisper olasılıklarıyla aynı ölçekte değil; (c) ve (b) üzerinde replay ile seçilir |
| `AGREE_TOL_S` | 1,0 → 0,5 | Flux'ta zamanlar daha kararlı olmalı [tahmin] |
| `FINAL_SOLO_MIN_PROB` | 0,7 | aynı |
| Boom'u `final`'de de kabul et | evet | turn sonundaki kelime için |

**Nova-3 yedeği (aynı adaptör, farklı birleştirici):**
- Uç nokta: `wss://api.eu.deepgram.com/v1/listen?model=nova-3&language=en&encoding=linear16&sample_rate=16000&interim_results=true&smart_format=false&punctuate=false&endpointing=300&utterance_end_ms=1000&vad_events=true&mip_opt_out=true` (keyterm yok).
- Hipotez = utterance'ın `is_final` kelimeleri + son interim kelimeleri.
- Utterance `speech_final:true` ya da `UtteranceEnd` ile biter.
- `is_final` bölümündeki bir mayın kelimesi, bir sonraki hipotezde zaten tekrar göründüğü için matcher değişmeden çalışır.

---

## 5. Emin olunmayan noktalar

- **Flux'ın aksanlı İngilizcedeki doğruluğu.** AA'da genel WER %7,4; Türkçe aksanı için hiç veri yok. Bütün öneri 29 Ekim testine bağlı.
- **Flux kelime zamanlarının referansı:** akış başı mı, turn başı mı? Ve `Update`'lerdeki son kelimenin ne kadar kararsız olduğu. İlk 5 dakikalık kayıtla görülür.
- **Nova-3 interim sıklığı.** Doküman örneğinden ~1 sn çıkarımı yaptım; resmî bir sayı yok.
- **Flux'ta duraklamasız çok uzun turn'lerin davranışı** (üst sınır, takılma). Belgelenmemiş.
- **Deepgram PAYG'de MIP'in varsayılan durumu** ve opt-out'un fiyata etkisi. Kaynaklar çelişkili; kredi zaten yetiyor.
- **Promosyon fiyatları** (Flux/Nova-3 "limited-time"). Demo ölçeğinde önemsiz.
- **Soniox:** ücretsiz kredi (200 $, 300 dk ya da hiç), `max_non_final_tokens_duration_ms` alanının adı/geçerliliği, ve AA ile Pipecat sonuçları arasındaki büyük çelişki (%11,9 vs %1,27).
- **Speechmatics:** ücretsiz kota (4 sa/ay mı, 20 sa/ay mı) ve partial'larda kelime güven skoru. Hafızamdan yazdım, doğrulanmadı.
- **Benchmark'ların neyi ölçtüğü.** Pipecat TTFS ve AA "latency" konuşma bittikten sonrasını ölçüyor; cümle içi gecikmeyi ölçen bağımsız bir benchmark bulamadım. Tablodaki cümle içi gecikmelerin hepsi [tahmin].
- **Ağ gecikmesi** (Türkiye → AB, ev bağlantısı, OBS yayın yaparken). Test ölçecek.
- **Deepgram'ın sessizlikte bağlantıyı kapatma süresi** (~10 sn). Hafızadan; relay sessizliği de gönderdiği için önemsiz olmalı.

---

## 6. Kaynaklar

**Deepgram**
- Flux genel bakış: https://developers.deepgram.com/docs/flux
- Flux quickstart (uç nokta, parametreler, 80 ms parça, ~260 ms EoT): https://developers.deepgram.com/docs/flux/quickstart.mdx
- Flux durum makinesi (`Update` ~0,25 sn): https://developers.deepgram.com/docs/flux/state
- Flux kelime zaman damgaları (changelog): https://developers.deepgram.com/changelog/2026/7/2
- Nova-3 → Flux geçişi: https://developers.deepgram.com/docs/flux/nova-3-migration
- Interim results: https://developers.deepgram.com/docs/using-interim-results , https://developers.deepgram.com/docs/interim-results
- Bölgesel uç noktalar (EU, `/v2/listen`): https://developers.deepgram.com/reference/regional-endpoints
- EU uç noktası GA: https://deepgram.com/learn/deepgram-eu-endpoint-now-generally-available
- Fiyatlar ve 200 $ kredi: https://deepgram.com/pricing
- Model Improvement Program: https://developers.deepgram.com/docs/the-deepgram-model-improvement-partnership-program
- Python SDK: https://github.com/deepgram/deepgram-python-sdk , https://pypi.org/project/deepgram-sdk/7.6.0/

**AssemblyAI**
- Streaming: https://assemblyai.com/docs/streaming
- Turn detection ve partial'lar: https://www.assemblyai.com/docs/streaming/universal-3-pro/turn-detection-and-partials
- Mesaj sırası: https://www.assemblyai.com/docs/streaming/universal-streaming/message-sequence.md
- Fiyatlar: https://www.assemblyai.com/pricing

**OpenAI**
- Realtime transkripsiyon rehberi: https://developers.openai.com/api/docs/guides/realtime-transcription.md
- gpt-realtime-whisper: https://developers.openai.com/api/docs/models/gpt-realtime-whisper.md
- gpt-live-transcribe: https://developers.openai.com/api/docs/models/gpt-live-transcribe
- Forum, toplu gelen delta'lar: https://community.openai.com/t/gpt-4o-transcribe-realtime-the-delta-updates-not-received-during-the-transcription/1357039

**Soniox**
- WebSocket API: https://soniox.com/docs/api-reference/stt/websocket-api.mdx
- Final ve final olmayan token'lar: https://soniox.com/docs/speech-to-text/core-concepts/final-vs-non-final-tokens
- Gecikme: https://soniox.com/docs/speech-to-text/core-concepts/real-time-latency
- Fiyatlar: https://soniox.com/pricing
- Kredi değişikliği: https://soniox.com/blog/2025-10-27-free-credits-update-for-soniox-api

**Diğerleri**
- ElevenLabs realtime: https://elevenlabs.io/docs/developers/guides/cookbooks/speech-to-text/streaming
- Speechmatics: https://docs.speechmatics.com/speech-to-text/realtime/quickstart , https://docs.speechmatics.com/features/realtime-latency , https://docs.speechmatics.com/speech-to-text/realtime/limits
- Gemini Live transkripsiyon: https://ai.google.dev/gemini-api/docs/live-api/live-transcribe , https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-5-transcribe
- Chirp 3: https://docs.cloud.google.com/speech-to-text/docs/models/chirp-3
- Gladia fiyatlar: https://www.gladia.io/pricing

**Bağımsız benchmark'lar ve çalışmalar**
- Pipecat STT benchmark (Ağustos 2026): https://www.pipecat.ai/benchmarks/speech-to-text
- Artificial Analysis, AA-WER Streaming (Haziran 2026): https://artificialanalysis.ai/articles/new-streaming-speech-to-text-benchmark-aa-wer-streaming
- Coval: https://www.coval.ai/blog/best-speech-to-text-providers-in-2026-independent-benchmarks-and-how-to-choose/
- Speko: https://benchmarks.speko.ai/
- Ana dili İngilizce olmayan konuşmacılarda ASR (L2-ARCTIC): https://arxiv.org/pdf/2503.06924

**Önceki rapor:** `docs/plan/stt-research.md` (yerel turbo, gecikme bütçesi, mikrofon relay).
