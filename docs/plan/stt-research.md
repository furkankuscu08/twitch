# STT araştırması: Minefield için konuşmadan yazıya katmanı

> **Arşiv (28 Ekim, D3):** STT için yerel turbo yerine Deepgram Flux seçildi; bkz. [stt-cloud-options.md](stt-cloud-options.md) ve [minefield.md](minefield.md) bölüm 3. Bu rapor sadece arka plan için duruyor.

> Tarih: 28 Ekim 2026. Kapsam: `SPEC.md` §1 ve §5, `docs/plan/minefield.md` §3 ve D3. Bu dosya öneridir; SPEC ve plan değiştirilmedi.
> İşaretler: **[kanıt]** doküman, kod, makale ya da issue'ya dayanıyor. **[tahmin]** benim çıkarımım; 29 Ekim testleriyle doğrulanmalı.

---

## 1. Özet ve öneri

**Optimal çözüm: mevcut tasarım kalıyor, birkaç somut düzeltmeyle.** Topluluktaki olgun projeler (whisper_streaming, WhisperLive, WhisperLiveKit) de aynı iskeleti kullanıyor: büyüyen tamponu tekrar tekrar yazıya dökmek ve iki ardışık tahminin uyuşmasını beklemek. Hazır bir çerçeveye geçmek 2 saatlik bütçeye bir şey katmıyor, aksine riski artırıyor.

1. **Mikrofon: Windows'ta küçük Python relay kalsın.** En az kırılgan yol bu. İki ekleme öneriyorum:
   - Önce `sd.WasapiSettings(auto_convert=True)` ile mikrofonu doğrudan 16 kHz açmayı dene; Windows kendisi örnekleme dönüştürür. Olmazsa 48 kHz açılır ve numpy ile basit bir FIR alçak geçiren süzgeçten geçirilip 3'te 1 seyreltilir.
   - Yedek olarak, oyun sunucusunun servis ettiği bir `/mic` sayfası olsun. Windows'taki Chrome sekmesi `getUserMedia` ile mikrofonu alır ve aynı WebSocket protokolüyle gönderir. Bu sayfa Windows'ta Python gerektirmez.
   - OBS dock'u içinden mikrofon almaya güvenme: kanıtlar anekdot düzeyinde ve çelişkili. WSLg/PulseAudio yolunu da kullanma.
2. **Motor: faster-whisper large-v3-turbo, WSL'de, 0,5 sn adım, iki tahmin uyuşması (kelime düzeyinde LocalAgreement-2).** Bu doğru seçim. Eklenmesi gerekenler:
   - `temperature=0.0` (sıcaklık geri dönüşü kapalı; aksi halde kısa ve gürültülü tamponlarda tek bir adım birkaç kez yeniden çözülür, gecikme sıçrar);
   - VAD kısa bir duraklama gördüğünde (≥200 ms) bir sonraki adımı beklemeden hemen transkripsiyon;
   - açılışta ısınma çağrısı;
   - tampon sınırına gelindiğinde ses rastgele bir yerden değil, kelime sınırından kesilmeli;
   - `compression_ratio` süzgeci.
3. **Gecikme beklentisi: ~0,9–1,3 sn [tahmin].** Hesap: ortalama 0,25 sn adım beklemesi + 0,5 sn ikinci tahmin + 2 × ~0,15–0,25 sn hesaplama. Hedefe (1–1,5 sn) sığıyor, ama sınırda. Asıl belirleyici adım başına hesaplama süresi; 29 Ekim'de OBS yayın yaparken ölçülmeli.
4. **Whisper'ın adım başı maliyeti tampon uzunluğuyla pek azalmaz.** faster-whisper sesi her zaman 30 sn'ye doldurarak kodlayıcıdan geçirir, ve turbo'da hızlanan kısım yalnızca kod çözücü (4 katman; kodlayıcı large-v3 ile aynı). Bu yüzden hız gerekirse distil-large-v3 işe yaramaz (kodlayıcı aynı). Gerçek kaçış yolları: `STEP_S=0.75` ya da `small.en`/`medium.en`.
5. **Hotword, initial_prompt ya da keyterm biasing kullanma** (SPEC'teki karar doğru). Mayın kelimesini modele "öğütlemek" söylenmediği halde o kelimenin yazılma ihtimalini artırır. Bu oyunda yanlış alarm, kaçan kelimeden daha pahalı.
6. **Pipecat'i yeniden kullanma.** `WhisperSTTService` bir `SegmentedSTTService`: VAD konuşmanın bittiğini söyleyince segment başına tek bir final metin üretir; ara sonuç (partial) ve kelime zaman damgası yok **[kanıt]**. Cümle ortasındaki bir mayın kelimesi ancak cümle bitince patlar. Ara sonuç istersen özel bir servis yazman gerekir; bu da aynı motoru WebRTC katmanıyla birlikte yazmak demek.
7. **Yedek (D3 dışında, model tarafı):** turbo, OBS yükü altında adım başına p95 > 0,35 sn çıkarsa sırasıyla şunlar denenir:
   1. `compute_type="int8_float16"`;
   2. `STEP_S=0.75`;
   3. `medium.en` ya da `small.en`.
   
   CUDA tamamen çökerse plan zaten var: motor Windows'ta çalışır (D3). Bulut, yalnızca karşılaştırma için: Deepgram Nova-3 + keyterm ile 5 saat yaklaşık 2–3 $ tutar, gecikmesi daha düşük olabilir. Ama "ses makineden çıkmıyor" iddiası kaybolur ve keyterm biasing yanlış alarmı artırır. Önermiyorum.
8. **Keyword spotting (sherpa-onnx KWS) ilginç ama 2 saate sığmaz.** Çalışma anında akış başına anahtar kelime verilebiliyor **[kanıt]**. Ancak İngilizce modeli küçük (3,3M) ve aksanlı, spontane konuşmada yanlış alarm oranı bilinmiyor. Teslimden sonrası için "ikinci doğrulayıcı" fikri olarak kalsın.

---

## 2. Seçenekler karşılaştırması

### 2a. Mikrofon yakalama

| Seçenek | Gecikme | Kurulum | Demo günü riski | 2 saatte? | Not |
| --- | --- | --- | --- | --- | --- |
| **Windows Python relay (sounddevice → WS → WSL)** ✅ | ~20–40 ms | Windows'ta Python + 3 paket | Düşük. Tek risk cihaz adı değişmesi; cihazı isimle seç. | Evet (~30 dk) | WASAPI shared modda OBS ile aynı mikrofonu paylaşabilir. `auto_convert=True` ile 16 kHz açılabilir **[kanıt: sounddevice API'si]**. |
| **Chrome sekmesi `/mic` (getUserMedia + AudioWorklet → WS)** yedek | ~30–60 ms | Python yok; ~40 satır JS | Düşük-orta: sekme açık kalmalı, Chrome izni bir kez verilir. | Evet (~20 dk) | `localhost` güvenli bağlam sayılır. `echoCancellation/noiseSuppression/autoGainControl:false` verilmeli. `AudioContext({sampleRate:16000})` örneklemeyi tarayıcıya bırakır. |
| OBS custom dock'ta getUserMedia | aynı | OBS başlatma bayrakları | **Yüksek**: forumda bazıları dock'ta çalıştığını, bazıları izin hatası aldığını yazıyor **[kanıt: OBS forumu, anekdot]** | Belirsiz | Denemesi 2 dk sürer, ama buna bağlanma. |
| OBS'ten doğrudan ses (eklenti/obs-websocket) | — | Eklenti, UDP | Orta-yüksek | Hayır | obs-websocket ham ses vermiyor **[kanıt]**. VBAN eklentisi/Lua betiği UDP ile PCM gönderebilir, ama ekstra eklenti demek. |
| WSLg PulseAudio | değişken | Kolay görünür | **Yüksek**: WSLg mikrofonu RDP üzerinden geliyor; takılma ve kopma raporları var **[tahmin + genel PulseAudio raporları]** | Riskli | Görev tanımı da "güvenilir değil" diyor. |
| Motor tamamen Windows'ta | 0 | CUDA DLL'leri (Purfview arşivi) | Orta | D3 yedeği | Zaten planlı. |

### 2b. STT yaklaşımı

| Seçenek | Mic yakalama | Gecikme (kelime sonu → boom) | Doğruluk / yanlış alarm | Kurulum zorluğu | Demo günü riski | 2 saatte? |
| --- | --- | --- | --- | --- | --- | --- |
| **Özel motor: Silero VAD + turbo, 0,5 sn yeniden yazım + kelime uyuşması** ✅ | relay | ~0,9–1,3 sn [tahmin] | Yüksek tanıma (kullanıcı GCP'de denedi). Yanlış alarm iki tahmin şartıyla düşük; harness ölçecek. | Orta (CUDA/cuDNN) | Düşük-orta | Evet (SPEC zaten bu) |
| whisper_streaming (ufal, LocalAgreement-2) | kendi | Makalede ortalama 3,3 sn (0,5 sn chunk, large-v2, A40) **[kanıt]** | WER ~%8,5 | Kolay | Orta | Evet, ama bizden yavaş: kesinleşmiş önek, tüm metin için en uzun ortak önek. Biz sadece mayın kelimesine bakıyoruz. |
| SimulStreaming / WhisperLiveKit (AlignAtt) | tarayıcı/WS | whisper_streaming'den "~5× hızlı" iddiası **[kanıt: README, mutlak sayı yok]** | iyi | Orta-yüksek: torch Whisper, çok sayıda ekstra | Orta | Riskli; kelime zaman damgası ve özel eşleştirici için kodu kurcalamak gerekir. |
| WhisperLive (collabora) | kendi istemcisi | ~1 sn tampon bekleme + tekrar | iyi | Orta (Docker) | Orta | Gereksiz; "tamamlanmış segment" mantığı 10 tekrar ister (`same_output_threshold=10`) **[kanıt]**. |
| RealtimeSTT | kendi (PyAudio) | partial var (küçük model) | partial'lar küçük modelle → yanlış alarm riski | Orta | Orta | Hayır |
| Pipecat + WhisperSTTService | SmallWebRTC (tarayıcı) | **Cümle/duraklama bitince** (VAD `stop_secs=0.2` varsayılan) **[kanıt]** | iyi, ama kelime zaman damgası yok | Orta | Orta | Partial olmadan hedefi tutmaz. |
| obs-localvocal (whisper.cpp, OBS içinde) | OBS kaynağı (tam yayın mikrofonu) | partial var | whisper.cpp modelleri | Kolay kurulum | Yüksek: çıktı metin kaynağı/dosya; oyuna akıtmak hack | Hayır |
| whisper.cpp `stream` | SDL | `--step 500 --length 5000` kayan pencere | tekrarlı/dağınık çıktı bilinen sorun [tahmin] | Orta (derleme) | Orta | Hayır |
| sherpa-onnx open-vocab KWS | relay | düşük (100 ms parçalar) [tahmin: <0,5 sn] | Bilinmiyor; eşik ve boost ayarı gerekir | Orta (token dönüştürme) | Orta | Hayır (yan proje) |
| NVIDIA Nemotron streaming 0.6B (cache-aware RNNT) | relay | 80 ms–1,12 sn chunk **[kanıt]** | WER %6,9 (1,12 sn) – %8,4 (80 ms) **[kanıt]** | **Yüksek** (NeMo veya yeni transformers / nemo-speech.cpp) | Yüksek | Hayır; ama gerçek akışlı en iyi yerel aday. |
| Vosk + grammar | relay | düşük | Grammar her sesi listeye zorlar; `[unk]` olmadan yanlış alarm çok [tahmin] | Kolay | Orta | Mümkün ama doğruluk zayıf |
| Moonshine v2 (akışlı kodlayıcı) | relay | düşük TTFT iddiası **[kanıt: makale, kendi beyanı]** | turbo'dan zayıf olabilir [tahmin] | Orta | Orta | Hayır |
| Bulut: Deepgram / AssemblyAI / OpenAI | relay → internet | ~0,3–0,8 sn partial [tahmin] | iyi; keyterm yanlış alarmı artırabilir | Kolay | İnternet ve anahtar bağımlılığı | Evet, ama pitch'i bozar |

---

## 3. Mevcut tasarıma göre önerilen değişiklikler

SPEC'e işlemek senin kararın; aşağıdakiler somut öneriler.

### §1 Components: mic relay

- **Örnekleme:**
  - Önce `sd.InputStream(samplerate=16000, channels=1, dtype="int16", blocksize=320, extra_settings=sd.WasapiSettings(auto_convert=True))` denenir.
  - Hata verirse cihazın kendi hızında (genelde 48 kHz) açılır. Ardından 63 dokunuşlu pencereli-sinc FIR (kesim ~7,5 kHz) uygulanır ve 3'te 1 seyreltilir. Bu `np.convolve` ile yapılır; scipy gerekmez.
  - Sadece 3 örneği ortalamak yetersiz alçak geçiren süzgeçtir, örtüşmeye (aliasing) yol açar.
- **Cihaz seçimi:** sırayla indekse değil, ad parçasına göre (`--device "Shure"`). `--list-devices` bayrağı olmalı.
- **Kopma sırasında:** motor yokken gelen ses atılır, kuyruğa alınmaz. Yeniden bağlanınca yeni `hello` gönderilir. Mevcut saat modeli bunu zaten gerektiriyor.
- **Yeni (opsiyonel, ~20 dk):** `web/mic/` sayfası, aynı `ws://localhost:8765/audio` protokolü.
  - AudioWorklet 20 ms'lik Int16 çerçeveler gönderir.
  - `getUserMedia({audio:{echoCancellation:false,noiseSuppression:false,autoGainControl:false}})`.
  - Relay çalışmazsa Chrome sekmesinde açılır. README'de "Plan B" olarak geçer.
- **OBS ile paylaşım:** Windows shared modda aynı mikrofonu hem OBS hem relay açabilir. Relay OBS filtrelerinden (gürültü bastırma vb.) **önceki** sesi alır. Bu Whisper için genelde iyi bir şey [tahmin], ama kayıt (a)/(b)/(c) da aynı yolla alınmalı ki harness canlıyla aynı sesi görsün.

### §5 Engine

| Ayar | SPEC'teki | Öneri | Neden |
| --- | --- | --- | --- |
| `temperature` | belirtilmemiş (faster-whisper varsayılanı 0,0→1,0 geri dönüş listesi) | **`0.0`** (tek değer) | Geri dönüş, sıkıştırma oranı ya da logprob kötü olunca aynı tamponu 5 kereye kadar yeniden çözer. Gecikme sıçrar ve halüsinasyon riski artar. |
| `beam_size` | 1 | 1 | Gecikme. (label-assist'te 5 kalabilir.) |
| `condition_on_previous_text`, `hotwords`, `initial_prompt` | kapalı | kapalı | Biasing yanlış alarm üretir. İstersen harness'ta A/B yapılabilir, ama varsayılan kapalı kalsın. |
| `compute_type` | float16 | float16; yedek `int8_float16` | VRAM ve hız. |
| Pre-roll | 200 ms | **300 ms** | İlk kelimenin başı kırpılmasın (Silero başlangıcı geç yakalayabilir). |
| VAD eşikleri | belirtilmemiş | başlangıç 0,5, bitiş 0,35 (histerezis); min konuşma 250 ms | Silero'nun önerdiği yapı. |
| `MIN_SILENCE_MS` | 500 | 500 (harness'ta 400 da denenmeli) | |
| **Duraklama adımı** | yok | **Yeni:** utterance içinde ≥200 ms sessizlik görülünce, iş yoksa zamanlayıcıyı beklemeden hemen bir adım çalıştır. Zamanlayıcı bu adımdan itibaren yeniden başlar. | Duraklamadan önceki kelime stabil olur. Cümle sonundaki mayınlar ~0,3–0,5 sn erken patlar [tahmin]. |
| `MAX_BUFFER_S` | 15 (zorunlu final + yeni utterance) | **12**. Son hipotezde sondan ikinci kelimenin `end` zamanından kes, artan ses yeni utterance'ın başına taşınsın. | Rastgele kesimde kelime ikiye bölünür (whisper_streaming da cümle/kelime sınırından kırpıyor **[kanıt]**). 12 sn kod çözücü token sayısını da sınırlar. |
| Isınma | yok | Açılışta 1 sn sessizlik + 1 sn gürültüyle 2 çağrı | İlk CUDA/cuDNN çağrısı saniyeler sürebilir; ilk patlama gecikmesin. |
| Halüsinasyon süzgeci | konuşma oranı < 0,3; tüm segmentler `no_speech_prob > 0.6`; liste | **ek:** herhangi bir segmentte `compression_ratio > 2.4` → at; ayrıca kelime `prob < MIN_WORD_PROB` (yeni, varsayılan 0,4, `replay` ile ayarlanır) olan mayın eşleşmeleri sayılmaz | Tekrar döngüleri ve düşük güvenli kelimeler. |
| Silero VAD | onnxruntime, durum korunur | faster-whisper'ın **`silero_vad_v6.onnx`** dosyası kullanılır, ama **`SileroVADModel.__call__` kullanılmaz**: o fonksiyon her çağrıda `h`,`c` durumlarını sıfırlıyor **[kanıt: kod]**. Kendi 20 satırlık sarmalayıcımız olmalı: girdi `(1, 576)` = önceki 64 örnek + 512 yeni örnek; `h`,`c` her pencereden sonra saklanır. | Durum korunmazsa VAD titrer. 64 örneklik bağlam olmazsa doğruluk düşer. |
| İş parçacığı | — | Transkripsiyon tek bir worker thread'de, ses alımı asyncio'da | CTranslate2 GIL'i bırakır. Ses alımı hiç bloklanmaz. |
| Heartbeat | `gpu_mem_mb`, `rtf` | + `step_ms_p95` (son 60 adım) | Demo günü yavaşlamayı dock'ta görmek için. |

**Eşleştirici (§5 Matcher):** spark→boom kuralı aslında kelime düzeyinde LocalAgreement-2. Bu, whisper_streaming'in tüm metin için en uzun ortak önek koşulundan daha hızlı ve bu iş için yeterli. Değiştirme. Tek ekleme `MIN_WORD_PROB`. Hem spark hem boom hipotezinde kelime prob'u bu eşiğin üstünde olmalı.

**Gecikme bütçesi [tahmin, 29 Ekim'de ölçülecek]:**

| Kalem | Süre |
| --- | --- |
| Kelime sonu → sonraki adımın başlaması | 0–0,5 sn (ort. 0,25) |
| Adım hesaplama (turbo, fp16, 30 sn dolgu, kelime damgalı) | ~0,15–0,25 sn |
| Tampon sonundaki kelime ilk tahminde eksik/yanlış çıkarsa | +0,5 sn (bazen) |
| İkinci (onay) tahmin | +0,5 sn + hesaplama |
| Sunucu + WS + overlay animasyonu | ~0,05 sn |
| **Toplam** | **~0,9–1,3 sn tipik; kötü durumda ~1,8 sn** |

Bulgu: adım hesaplaması 0,25 sn'yi aşarsa "atlanan adımlar" kuralı devreye girer ve gecikme hızla büyür. Hesaplama p95 < 0,3 sn şart.

**Neden tam LocalAgreement + prompt + tampon kırpma yok:**
- Bizim utterance'lar VAD ile sınırlı ve kısa (≤12 sn). 30 sn sınırına hiç gelmiyoruz.
- Önceki metni prompt olarak vermek tutarlılık sağlıyor **[kanıt: makale]**, ama halüsinasyonun bir utterance'tan diğerine taşınması riski var.
- Bizim ihtiyacımız tam transkript değil, 4 kelimenin tespiti.

### §7 Harness: küçük eklemeler

- `run` simüle gerçek zamanda çalışırken hesaplama süresini de saymalı ("computationally aware"; whisper_streaming makalesi de böyle ölçüyor **[kanıt]**). SPEC'teki "adım zamanı + `compute_ms`" bunu karşılıyor. Ek olarak bir koşu **OBS yayın yaparken** yapılmalı. Raporda "OBS açık/kapalı" sütunu olmalı.
- Raporda adım hesaplama p50/p95 ve atlanan adım sayısı da olsun.

---

## 4. Başkaları ne yapmış

- **whisper_streaming (ÚFAL, Macháček vd. 2023):**
  - LocalAgreement-2: iki ardışık çıktının en uzun ortak öneki kesinleşir.
  - Önceki 200 kesinleşmiş kelime prompt olarak verilir. Tampon cümle sonundan kırpılır.
  - English, A40, large-v2: MinChunkSize 0,5 sn → WER %8,5, ortalama gecikme 3,27 sn; 1,0 sn → %8,1, 3,62 sn.
  - VAD akıcı konuşmada gecikmeyi ~0,23 sn düşürüyor. Öneri: sistemi konuşmadan biraz önce başlat, ilk kelime kaçmasın.
  - Bizim gecikmemiz daha düşük olmalı, çünkü (a) turbo, large-v2'den çok daha hızlı çözüyor; (b) önek değil tek kelime onaylıyoruz; (c) utterance'lar kısa. [tahmin]
- **SimulStreaming (ÚFAL, 2025):**
  - AlignAtt politikası: cross-attention ile sesin sonuna yakın token'larda durur (`frame_threshold`).
  - "WhisperStreaming'den ~5× hızlı" iddiası var. torch tabanlı (openai-whisper), faster-whisper değil. MIT lisanslı.
- **WhisperLiveKit:**
  - Varsayılan AlignAtt (SimulStreaming), alternatif LocalAgreement. faster-whisper dahil birçok backend.
  - `--pcm-input` ile ham s16le PCM kabul ediyor, tarayıcıda AudioWorklet kullanıyor.
  - Anahtar kelime tespiti yok; `context` parametresi sadece tanıma ipucu.
- **WhisperLive (Collabora):**
  - Tamponu `timestamp_offset`'ten itibaren tekrar yazıya döküyor; 1 sn'den kısa sesi beklemeye alıyor.
  - Son segment dışındakileri tamamlanmış sayıyor; son segment 10 kez aynı çıkarsa onu da tamamlıyor.
  - `no_speech_thresh=0.45`; 45 sn'yi aşınca tamponun ilk 30 sn'sini atıyor.
- **RealtimeSTT:** Ara metin için hızlı bir model, final için ayrı bir model kullanıyor. WebRTC + Silero VAD; wake word (Porcupine/OpenWakeWord) desteği var. Ara metni küçük modelle üretmek bizde yanlış alarm riski olurdu.
- **Pipecat:**
  - `WhisperSTTService` bir `SegmentedSTTService`. `run_stt` bir segmenti tek seferde yazıya döker ve tek bir final `TranscriptionFrame` üretir.
  - `word_timestamps` kullanılmıyor. Model enum'unda `LARGE_V3_TURBO = "deepdml/faster-whisper-large-v3-turbo-ct2"` var. `no_speech_prob` eşiği 0,4. VAD varsayılanı `stop_secs=0.2`.
  - Bizdeki karşılığı şöyle bir hat olurdu: `SmallWebRTCTransport(input) → SileroVADAnalyzer → WhisperSTTService → özel FrameProcessor (POST /stt/hypothesis)`. Mayın kelimesi ancak duraklamadan sonra çıkar, ve ara sonuç için kendi `STTService` alt sınıfını yazmak gerekir. Sonuç: daha zor, daha yavaş.
- **obs-localvocal:** OBS içinde whisper.cpp. Ara transkripsiyon var. Çıktı metin kaynağı, .txt/.srt ya da RTMP altyazı. WebSocket veya HTTP çıktısı yok. Windows'ta CUDA dahil.
- **sherpa-onnx KWS:**
  - Açık kelime dağarcıklı anahtar kelime tespiti: "sadece verilen kelimeleri çözen küçük bir ASR".
  - Satır formatı: `▁PINE APP LE :2.0 #0.3` (boost ve eşik). Python'da `create_stream(keywords=...)` ile akış başına ek anahtar kelime verilebiliyor; mayın değişince yeni stream açılır. Tespitten sonra `reset_stream` gerekir.
  - İngilizce model: `sherpa-onnx-kws-zipformer-gigaspeech-3.3M-2024-01-01`.
- **NVIDIA Nemotron Speech Streaming EN 0.6B:** Cache-aware FastConformer-RNNT. Chunk boyutu çalışma anında 80/160/560/1120 ms seçilebiliyor; WER %8,43 → %6,93. NVIDIA Open Model License. NeMo, transformers ≥5.13 ya da nemo-speech.cpp (GGUF) ile çalışıyor. Teslimden sonra denemeye değer.
- **Moonshine v2 (2026):** Kayan pencereli akışlı kodlayıcı, düşük TTFT iddiası. Bağımsız ölçüm bulamadım.
- **faster-whisper:** CTranslate2'nin son sürümleri CUDA 12 + cuDNN 9 istiyor. Linux'ta `pip install nvidia-cublas-cu12 nvidia-cudnn-cu12==9.*` ve `LD_LIBRARY_PATH` yeterli; plan zaten böyle. Windows için Purfview arşivi önerilir.

---

## 5. Emin olmadığım noktalar ve 29 Ekim'de hızlı testler

**Belirsizlikler:**
- Turbo'nun 4070 Laptop'ta adım başına süresi (30 sn dolgu + word_timestamps). Tahminim 150–250 ms, ama ölçüm bulamadım.
- OBS NVENC yayını sürerken GPU çekişmesi. NVENC ayrı bir donanım bloğu, ama OBS'in sahne birleştirmesi ve tarayıcı kaynakları GPU kullanıyor. Etkinin küçük olmasını bekliyorum [tahmin].
- WSL2'nin GPU sanallaştırma ek yükü (genelde küçük) [tahmin].
- Tampon sonundaki kelimenin ilk tahminde ne sıklıkla eksik çıktığı (gecikmeye +0,5 sn ekler).
- Deste kelimelerinde turbo'nun karıştırma oranı (ör. "giraffe" ↔ "a graph"). Harness gösterecek.
- OBS dock'ta getUserMedia: forumda çelişkili raporlar var.

**29 Ekim testleri** (CUDA kontrolünün 45 dakikası içine sığar):
1. **Adım süresi:** Turbo fp16, `beam_size=1`, `temperature=0`, `word_timestamps=True`. 2, 6 ve 12 sn'lik tamponlar, her biri 20 kez (ısınmadan sonra). p50/p95 not edilir. Aynısı OBS 1080p60 NVENC ile test yayını yaparken tekrarlanır. **Kabul: p95 < 300 ms.** Değilse önce `int8_float16`, sonra `STEP_S=0.75` denenir.
2. **word_timestamps maliyeti:** Aynı test `word_timestamps=False` ile. Fark büyükse (>80 ms) hipotezde kelime zamanı yalnızca spark/boom adaylarında gerekecek şekilde tasarım düşünülebilir [tahmin: gerekmeyecek].
3. **Relay:** `auto_convert=True` + 16 kHz açılıyor mu? OBS mikrofonu açıkken relay de açabiliyor mu? Windows → `ws://localhost:8765` WSL'ye ulaşıyor mu?
4. **2 dk deneme (opsiyonel):** OBS'te custom dock olarak `/mic` test sayfası mikrofon izni alıyor mu? Sonuç ne olursa olsun karar değişmez; sadece not edilir.
5. **Sessizlik:** Kayıt (b) (10 dk sessizlik ve gürültü) motorla çalıştırılır. Süzgeçlerden sonra kaç hipotez kalıyor, içinde deste kelimesi var mı?
6. **İlk kelime:** "Pineapple is great" gibi mayın kelimesiyle başlayan 10 cümle. İlk kelime kırpılıyor mu? (Pre-roll 300 ms'nin yeterli olup olmadığı.)

---

## 6. Bulut seçenekleri (sadece karşılaştırma)

| Servis | Gerçek zamanlı | Kelime ipucu | Fiyat (kaynaklar çelişkili, resmi sayfada doğrulanmalı) | 5 saat |
| --- | --- | --- | --- | --- |
| Deepgram Nova-3 streaming | evet, interim sonuçlar | keyterm prompting (+~0,0013 $/dk) | ~0,0048–0,0077 $/dk | ~1,8–2,7 $ |
| AssemblyAI Universal-Streaming | evet | keyterms (+~0,04–0,05 $/sa) | 0,15 $/sa (Universal-3.5 Pro Realtime 0,45 $/sa) | ~0,8–2,3 $ |
| OpenAI realtime transkripsiyon | evet (delta olayları) | prompt | gpt-4o-mini-transcribe ~0,003 $/dk, gpt-4o-transcribe ~0,006 $/dk, gpt-realtime-whisper 0,017 $/dk | ~0,9–5,1 $ |

**Değerlendirme:** Para önemsiz, ama pitch'in "yerel STT, ses kaydedilmiyor, makineden çıkmıyor" iddiası kaybolur. API anahtarı, internet ve kota da demo günü riskine eklenir. Keyterm biasing de bizim için yanlış alarm riski demek [tahmin, harness ile ölçülebilir]. Yerel turbo zaten iyi çalıştığı için bulut "açıkça daha iyi" değil. Yalnızca CUDA hem WSL'de hem Windows'ta çökerse acil durum B planı olarak düşünülebilir.

---

## 7. Kaynaklar

- Macháček, Dabre, Bojar. *Turning Whisper into Real-Time Transcription System* (whisper_streaming): https://arxiv.org/html/2307.14743
- SimulStreaming: https://github.com/ufal/SimulStreaming
- WhisperLiveKit: https://github.com/QuentinFuxa/WhisperLiveKit
- WhisperLive backend (`same_output_threshold`, tampon kırpma): https://github.com/collabora/WhisperLive/blob/main/whisper_live/backend/base.py
- RealtimeSTT: https://github.com/KoljaB/RealtimeSTT
- Pipecat Whisper STT kaynak kodu: https://reference-server.pipecat.ai/en/latest/_modules/pipecat/services/whisper/stt.html
- Pipecat Whisper dokümanı: https://docs.pipecat.ai/api-reference/server/services/stt/whisper.md
- Pipecat VAD varsayılanları: https://github.com/pipecat-ai/pipecat/blob/main/src/pipecat/audio/vad/vad_analyzer.py
- faster-whisper README (CUDA 12 / cuDNN 9, pip ile kurulum): https://github.com/SYSTRAN/faster-whisper
- faster-whisper Silero sarmalayıcısı (durum her çağrıda sıfırlanıyor): https://github.com/SYSTRAN/faster-whisper/blob/master/faster_whisper/vad.py
- python-sounddevice `WasapiSettings(auto_convert=...)`: https://github.com/spatialaudio/python-sounddevice
- sherpa-onnx KWS dokümanı: https://k2-fsa.github.io/sherpa/onnx/kws/index.html
- sherpa-onnx `create_stream(keywords)`: https://github.com/k2-fsa/sherpa-onnx/blob/master/sherpa-onnx/python/sherpa_onnx/keyword_spotter.py
- sherpa-onnx mikrofon KWS örneği: https://github.com/k2-fsa/sherpa-onnx/blob/master/python-api-examples/keyword-spotter-from-microphone.py
- NVIDIA Nemotron Speech Streaming EN 0.6B: https://huggingface.co/nvidia/nemotron-speech-streaming-en-0.6b
- Moonshine v2 makalesi: https://arxiv.org/abs/2602.12241
- obs-localvocal: https://github.com/royshil/obs-localvocal
- OBS forumu, browser source'ta getUserMedia: https://obsproject.com/forum/threads/cant-get-mediastream-permissions-in-browser-source.143858/
- OBS forumu, OBS 27.2 getUserMedia: https://obsproject.com/forum/threads/obs-27-2-0-cannot-read-properties-of-undefined-reading-getusermedia.153470
- OBS VBAN Audio eklentisi: https://obsproject.com/forum/resources/vban-audio.1623/
- Deepgram fiyat özeti (ikincil): https://www.activepieces.com/blog/deepgram-pricing-2026-per-minute-rates-and-add-ons.md
- AssemblyAI fiyatları: https://www.assemblyai.com/pricing
- OpenAI gpt-realtime-whisper: https://developers.openai.com/api/docs/models/gpt-realtime-whisper.md
- OpenAI transkripsiyon fiyat takibi (ikincil): https://costgoat.com/pricing/openai-transcription
