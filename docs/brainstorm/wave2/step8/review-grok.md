Varsayımım şu: amaç, bu yarışmada üst sıra. Dört kriter eşit ağırlıkta; beraberlikte önce Innovation bakılıyor. Hakemler kodu çalıştırmak zorunda değil, üç dakikayı da sonuna kadar izlemek zorunda değil. Video, ürünün kendisi. Sizin kısıtınız da net: seyirci yok, İngilizce aksanlı, konuşma tanıma WSL içinde değil Windows sürecinde, inşa bütçesi yaklaşık 17,5 saat.

Bu çerçevede kuracağım şey **Minefield**. 29 Ekim akşamı T1 kalırsa aynı repoda **VAR**'a dönerim. Checkpoint üçüncü sırada. Tap'i bu yarışma için kurmam.

## Minefield

En iyi yarışma fikri bu. Tek cümlede anlatılıyor, chat gerçekten bir şey biliyor ve yayıncı bilmiyor, patlama üç saniyede izleniyor. Overview'un "audience participation / streamer distractions" çağrısına da oturuyor. Innovation burada en temiz: baktığım yerlerde konuşmayla tetiklenen araçlar kelimeyi yayıncının seçtiği sistemler ([Stream Voice Triggers](https://github.com/Chenzo/stream-voice-triggers) mikrofonu dinleyip yayıncının yazdığı kelimede OBS aksiyonu çalıştırıyor); seyircinin kelime oynadığı oyunlar ise yazılı chat'te kalıyor ([AnkhbotSecretWord](https://github.com/Yaz12321/AnkhbotSecretWord), [RobinSystem Word Guess](https://robinsystem.live/twitch-word-guess?lang=en), [Chatexto](https://chatexto.com/)). İkisi birden, yani gizli kelime artı yayıncının kendi ağzı, duruyor. Dud reveal ikinci bir final veriyor. DEFUSE, yanlış alarmı hem kurtarıyor hem videoda dürüst bir beat yapıyor. Accuracy harness de sizin asıl avantajınız: ölçülmüş bir speech-to-text, "Codex ile kuruldu" karesine ve Technological implementation'a aynı anda yarıyor.

Kötü tarafı, mayının kurallarının modeli dövmesi. "İlk 1000 kelime yasak" tam da Whisper'ın kaçırdığı kelimeleri seçtiriyor. `hotwords` seyrek kelimede isabeti artırıyor; sessizlikte ve ani perdeden değişimde o kelimeleri uyduruyor. VAD bunu azaltıyor, bitirmiyor. Bunu hem [issue 1356](https://github.com/SYSTRAN/faster-whisper/issues/1356) hem hotwords'ü ekleyen [PR 731](https://github.com/SYSTRAN/faster-whisper/pull/731) yazıyor: hayalet metin çoğu zaman hotword listesinin kendisi. İki saniyelik kayan pencere de buna davetiye. Sizin sesiniz aksanlı İngilizce olduğu için T1'i temiz bir TTS kaydıyla geçirmek videoyu kurtarmaz. Bir de eğlence, üç kişiyle yirmi dakikada hâlâ doğrulanmış değil. Troll riski gerçek; serbest metin, blocklist'ten sızar.

Şunları değiştirirdim:

- Serbest kelimeyi MVP'den çıkarın. Yaklaşık 150 somut, komik, Whisper'ın tanıdığı isimden bir deste yapın: pineapple, giraffe, spaghetti, keyboard. Kelime hâlâ gizli, chat hâlâ yönlendiriyor, küfür giremiyor. Deste, blocklist'in yerini tutar. Bunu videoda bir cümle söyleyin.
- Kayan pencereyi bırakın. VAD cümleyi kessin, `small.en` + int8 o sözceyi bir kez yazsın. 4070 Laptop 8 GB için bu model rahat. Eşleşme bütün kelime olsun; transkript yalnızca hotword listesiyse veya sözce enerjisi düşükse patlatmayın. Gecikme bütçesi 3 saniye, sözce başına tanıma bunun altında kalır. Windows süreci eşleşmeyi WSL'deki FastAPI'ye POST etsin; bu köprüyü 2,5 saatin içine yazın.
- Canlı mayın sayısını 4 ile sınırlayın. Uzun hotword listesi, o kelimelerin uydurulmasını kolaylaştırıyor.
- Harness'ı sizin ağzınızdan, cümle içinde, deste kelimeleriyle koşun. Video için hook'u en son, bildiğiniz isabetli kelimelerle çekin. Arkadaşlar desteden seçsin, siz bilmeyin; birkaç tur kaydedip en temiz patlamayı başa koyun.
- **Fuse'u alın** (1 saat). Yüksek güvende anında patlasın, orta güvende 3 saniyelik fitil yansın. Bu, Design kriterinin kendisi.
- **Sweep'i ve Bomb Squad'ı koymayın.** Sweep, hook'taki patlamayla aynı sahneyi paylaşıyor; yayıncı kelimeyi bilmiyorsa ya mayını söndürür ya da boşa harcar. Bomb Squad üç hesapla videoda görünmez ve yayınlar arası kayıt, "24 saatten fazla Twitch içeriği tutmama" kuralınızla da sürtünür.
- Plant page'i T4'e bağlamayın. Önce localhost form. Arkadaşlar aynı evdeyse bu yeter. OAuth'lu herkese açık sayfa T4 geçince gelir. Whisper intake ve "Call it" bu videoya sığmaz.
- Klip: patlama anında `POST /helix/clips` ile `title` ve `duration=30`. Bu iki parametre canlı uçta artık var ([referans](https://dev.twitch.tv/docs/api/reference/#create-clip)). Belgesiz olan, `duration`'ın 90 saniyelik pencerenin hangi ucunu tuttuğu. Belgelenen varsayılan davranış, pencerenin **son 30 saniyesi** ([clips rehberi](https://dev.twitch.tv/docs/api/clips/)). T5, 202 dönmesini değil, Get Clips'teki başlığı ve oynatılan klibin patlamayı içermesini ölçsün. Get Clips 60 saniyeye kadar sürebilir; videoyu klip hazır olana kadar bekletmeyin. Başlık AutoMod'dan geçmek zorunda.

Kesilemez üç şey: kelimesiz chip, gerçekten söylenmiş bir kelimede gerçek patlama, eken kişinin adı. Gerisi ikinci dakika.

## Tap on the Shoulder

Problem gerçek ve anlatması kolay. Susturulmuş mikrofon, uzak mikrofon, "chat bir şey diyor, yayıncı tam ekran oyunda". Muted Notification ve Remember to Talk yalnızca OBS'in gördüğü susturma ve sessizliği kapsıyor; "you sound far away" onların dışındayken sizin döngünüz insan raporunu oda içindeki bir yüze taşıyıp sonra chat'e soruyor. Bu, parça parça var olan şeylerin dürüst bir birleşimi. Snoop Dogg örneği de videonun ilk cümlesi olabilir.

Yarışma kaydı olarak zayıf. Innovation en ince burada; hakem "masaüstü uyarı artı maskot" diye kovaya atabilir. Potential Impact metinde duruyor, üç dakikada durmuyor: asıl acı bir saatlik sessiz yayın, siz onu üç test hesabıyla ancak canlandırabilirsiniz. Design kriterinin "fun to watch" yarısı bu fikirde yok. Topluluk oynamıyor, arıza bildiriyor. Telefon yüzü de 2,5 saatlik bir çekim kısıtı: Wake Lock için HTTPS, eşleşme, kadraj, encode'da okunacak punto. Sakin mod onu Mochi benzeri bir maskota yaklaştırır.

Kuracak olsaydım sakin modu ve Soundcheck'i tutar, kara ekran tespitini ve yayın sonu raporunu atardım. Saniyede bir screenshot, durağan bir sahnede "FROZEN?" üretir. Yine de bu kesintiler onu Minefield'ın önüne geçirmez.

## Checkpoint

Pivot işe yaramış. Soru kuyruğu Meld'te var; yayıncının cevabını kartın üstüne yazıp izleyicinin thread'ine alıntı olarak geri vermek, baktığım araçlarda yok. Eller işte kalıyor. Confidence gate de doğru: zayıf transkriptte alıntı yok, düz makbuz var. T1b, T1'den daha kolay geçer, çünkü cümleyi siz kuruyorsunuz ve seyrek bir mayın kelimesi beklemiyorsunuz. Çizim timelapse'i güzel çekilirse Design orta-iyi olur.

İki iddia videoda sizi bağlar. Birincisi, "çıkan izleyici sonra cevabı bulur". Thread'li yanıt herkese açık bir chat mesajı; DM değil, çevrimdışı bildirim de değil ([Send Chat Message](https://dev.twitch.tv/docs/chat/send-receive-messages/)). Ayrılmış Ana, ancak o sohbete geri dönerse görür. Videoda onun istemcisinde yanıtı göstermek yeterli; "Twitch ona haber verdi" demeyin. İkincisi, "Micron 05". Marka artı rakam, Whisper'ın düştüğü yer. Cevap düz kelime olsun: "the thin black pen, it doesn't bleed."

**FAQ'yi koymayın.** `all-MiniLM-L6-v2` ile 0,85 eşik, dört cevaplık bir yayında ya hiç tutmaz ya yanlış tutar. Videoda göstermek için aynı soruyu ikinci kez yazdırmak da sahne olur. Klip linkini makbuza koyma işi de 3 saniyelik pencereye sığmaz; klip async, Get Clips bir dakikayı bulabilir. **Undo penceresi** (0,5 saat) durabilir: alıntı, sizi utandırabilecek tek satır. Kristal, sıralama ve thread'li alıntı yeter. Hakem ilk on saniyede "yine bir soru kuyruğu" derse, kurtaran tek kare kartın üstünde beliren kelimeler ve hemen yanındaki thread.

## VAR

En güvenli gösteri. Konuşma tanıma yok, herkese açık URL yok, MVP en kısa (8,5 saat), kâğıt topu ticari oyun değil. Siren, ağır çekim, jüri sırası ve mühür, Design'da yüksek puan alır. Oyun kategorileri izlemenin çoğunluğu olduğu için etki cümlesi de güçlü, masa üstü numara o kitleyi temsil edebilirse.

Innovation en zayıf halka ve beraberlikte ilk kriter bu. Sohbetle replay, yavaş çekim ve anket ayrı ayrı duruyor. Hakem bunu "replay artı poll" diye okuyabilir. Tören o okumayı ancak görüntü çok iyiyse yener.

Klip de burada en keskin risk. Varsayılan yayın, pencerenin son 30 saniyesi. `duration` en fazla 60. Ritüel 25 saniyeyi geçerse, son 60 saniye orijinal anı kenara iter. Ağır çekim zaten review'ın içinde olduğu için klip review'ı tutuyorsa an kaybolmaz. Bunu T5'te oynatarak görün. Create Clip From VOD'u canlı demonun yoluna koymayın: Aralık 2025 beta duyurusunda `vod_offset`'in klibi birkaç saniye kaydırdığı yazılmış, Twitch bunu genel kullanıma çıkmadan düzeltme şartı saymış ([duyuru, Ocak 2026 yanıtı](https://discuss.dev.twitch.com/t/introducing-clip-api-improvements-and-clip-from-vod-in-open-beta/64492)). Ekim 2026'da düzelmiş olabilir; düzeldiğini ancak oynatılmış klip gösterir.

**VAR pending** tek alınacak ek (1 saat). Anında durduran review, kendi karşı sinyalinizdeki itiraz. Videoda auto mod hook olarak kalsın; pending'i açıklama metninde ve on saniyelik bir planda gösterin. **Telestrator'ı ve referee reputation'ı koymayın.** Çizim senkronu kolayca kötü görünür; üç jüriyle puan tablosu bir şey kanıtlamaz. Stinger ve mühür sizin çiziminiz olsun. Yayın paketinin çerçevesini kopyalamayın; kurallar, izinsiz üçüncü taraf markasını videodan çıkarıyor.

## Ben olsam

**Minefield'ı kurarım.** Fuse içeride, Sweep ve Bomb Squad dışarıda, deste kelimeleri, sözce bazlı `small.en`, localhost plant page. Harness sizin sesinizle. Video: öğle yemeği sohbeti, patlama, chip'te isim, bir yanlış alarmda DEFUSE, sonunda bir dud, sonra harness sayıları ve Codex karesi. İlk yirmi saniye puanın kendisi.

29 Ekim'de T1, kendi sesinizle, cümle içi deste kelimelerinde %80 isabet ve 10 dakikada en fazla bir yanlış alarm görmezse o gün Minefield'ı keserim. Aynı FastAPI, EventSub, OBS ve klip yolu üstüne **VAR**'ı kurarım: kâğıt topu, 25 saniyenin altında review, `duration=60`, pending badge. T2 de kötüyse Checkpoint'e geçmem, çünkü kalan sürede hem speech-to-text hem yeni overlay hem video yetişmez; o durumda VAR'ın replay'siz hali bile (çağrı, jüri, mühür, klip) Tap'ten iyi bir video olur. Checkpoint'i ancak T1 düşer, T1b temiz geçer ve VAR'ın replay'si T2'de şaşırırsa açarım.

Tap her durumda bu deadline'ın dışında kalır. İyi bir yayın aracı, zayıf bir üç dakika.

## Ayrı bir fikir

İki kartı tek üründe birleştirmeyin. 17,5 saat iki overlay'i yarışma kalitesinde bitirmez. Tek meşru birleşim, 29 Ekim'deki kill-switch: taban ortak, Codex artefaktı ya harness ya da replay pipeline. Beşinci bir fikir açmayın. Yarınki testler, yeni bir konseptten daha değerli.