# Kalan 10 aday (adım 5a sonrası)

Kaynak: [step5/aggregate.md](step5/aggregate.md) (puanlar, notlar), [shortlist-20.md](shortlist-20.md) (adayların ayrıntılı açıklamaları), [filter.md](filter.md) (1. gün testleri). Puanlar üç modelin toplamı (Opus + Astra + Grok, 60 üzerinden). Kriter toplamları her biri 15 üzerinden: Y yenilik, E etki, Te teknik, Ta tasarım.

Karar (kullanıcı, 2026-10-26): önceden yazılan kural olduğu gibi uygulandı. Elenen 10 adaydan bazılarının fikirleri, aşağıda "Eklenen özellik" satırlarında, kalan adaylara taşındı.

## Özet

| # | K | Aday | Puan | Y | E | Te | Ta | En zayıf kriter | Ana risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | K19 | Minefield | 54 | 14 | 12 | 13 | 15 | Etki | STT doğruluğu, gizli giriş |
| 2 | K06 | Prodüksiyon sorunları (Tap) | 49 | 12 | 15 | 11 | 11 | Teknik / tasarım | Basit görünme |
| 3 | K24 | VAR | 49 | 11 | 10 | 13 | 15 | Etki | Replay buffer spike |
| 4 | K14 | Raid'le taşınan şey (Raid Torch) | 46 | 14 | 9 | 11 | 12 | Etki | İkinci canlı kanal |
| 5 | K10 | Previously On | 45 | 11 | 11 | 11 | 12 | Dengeli | "Süslü raid uyarısı" algısı |
| 6 | K20 | Studio Audience | 45 | 9 | 11 | 11 | 14 | Yenilik | Kalabalık alan (ses efektleri) |
| 7 | K21 | Foley Pit | 44 | 14 | 8 | 8 | 14 | Etki / teknik | Tek seferlik segment |
| 8 | K17 | Hint Jar | 43 | 12 | 10 | 9 | 12 | Teknik | Gizli giriş |
| 9 | K23 | Photo Booth | 40 | 8 | 9 | 10 | 13 | Yenilik | Hosting / tünel |
| 10 | K01b | Checkpoint | 39 | 9 | 11 | 9 | 10 | Yenilik / teknik | Soru kuyruğuna benzeme |

## Adaylar

### 1. K19 Minefield (54)

- **Fikir:** İzleyiciler gizlice kelime mayını gömer. Yayıncı o kelimeyi söyleyince STT yakalar: patlama, gömenin adı, klip.
- **Güçlü yanı:** Üç modelin de 1 numarası. Yenilik ve tasarımda en yüksek puan.
- **Zayıf yanı:** Etki. Bu bir oyun segmenti, sürekli kullanılan bir araç değil.
- **Eklenen özellik:** K26 Mühürlü tahminler, mini mod olarak. Aynı gizli giriş altyapısı kullanılır: tahminler zarf olarak görünür, hepsi birlikte açılır.
- **Açık noktalar:**
  - **Gizli giriş.** Whisper için gönderen hesabın telefonu doğrulanmış olmalı, günde 40 alıcı sınırı var, mesaj sessizce düşebilir. Yedek yol: Twitch girişli bir web sayfası, herkese açık bir tünel arkasında. 1. gün testi #11.
  - **STT.** Gündelik konuşmada doğruluk (spike #2). Ayrıca yanlış tetiklemeye karşı kelime sınırı kontrolü ve kısa bir onay penceresi gerekir.

### 2. K06 Prodüksiyon sorunları yayıncıya ulaşır (49)

- **Fikir:** Mikrofon kapalıysa ya da ses bozuksa, izleyici raporları ve mod uyarıları yayıncıya özel bir kanaldan ulaşır: lamba, kulaklık sesi, dock. Yardım eden izleyiciye yayında teşekkür edilir.
- **Güçlü yanı:** Etkide en yüksek puan (15/15). Bu derdi her yayıncı yaşıyor.
- **Zayıf yanı:** Grok tekniği "eşik + uyarı" olarak gördü. Opus'a göre tasarımda ekranda pek bir şey görünmüyor.
- **Eklenen özellik:** K03 Desk Buddy, uyarı cihazı olarak. Kadrajdaki telefon yüzü sorunu gösterir, izleyici raporunun "ulaştığını" kamerada görür. Bu, tasarım zayıflığına doğrudan cevap. Soundcheck'in "Test B" onay döngüsü de teknik derinlik katar.
- **Açık noktalar:** Lamba opsiyonel (yedek: telefon flaşı veya Desk Buddy yüzü). Donanım var mı (test #10)?

### 3. K24 VAR (49)

- **Fikir:** İki izleyici `!var` yazar. Yerel replay buffer'dan ağır çekim tekrar oynar, jüri oylar, karar damgası basılır.
- **Güçlü yanı:** Tasarımda en yüksek puan (15/15), videoda en çok tekrar izlenecek an.
- **Zayıf yanı:** Etki. Sadece tartışmalı bir an olduğunda işe yarar.
- **Açık noktalar:**
  - obs-websocket replay buffer spike'ı (#5).
  - Twitch klibi yerel tekrardan değil, Twitch'in kendi yayınından alınır. Klip başlığı API'den ayarlanamayabilir. Klip bonus, çekirdeğin parçası değil.

### 4. K14 Raid'le taşınan şey / Raid Torch (46)

- **Fikir:** Raid'le birlikte bir not ya da meşale hedef kanala gider. Meşale her kanaldan bir emote izi toplar, yolculuğunu gösterir.
- **Güçlü yanı:** Yenilikte en yüksek puanlardan (14). Grok'un 2 numarası.
- **Zayıf yanı:** Etki (9). İki kanalın da aracı kullanması gerekiyor. Puanını en çok bu düşürdü.
- **Açık noktalar:**
  - İkinci canlı kanal ve gerçek raid (test #4).
  - Developer Agreement IV.C (test #12): sadece kendi verimizi (kanal ID'leri, sayaçlar) tutarsak, çok günlük yolculuk mümkün olabilir.

### 5. K10 Previously On (45)

- **Fikir:** Yayın sırasında kısa olaylar girilir. Raid gelince ya da istek üzerine TV tarzı bir "Önceki bölümlerde…" kartı çıkar.
- **Güçlü yanı:** Dört kriterde de dengeli. Opus'un ve Grok'un ilk 5'inde.
- **Zayıf yanı:** Jüri bunu "süslü raid uyarısı" olarak okuyabilir. Olayları birinin girmesi gerekiyor.
- **Eklenen özellik:** K09 Lore dipnotları ve K11 Yeni gelene karşılama. Kart "yeni gelen herkese bağlam" olarak genişler: raider, geç gelen ve ilk kez yazan izleyici aynı kartı görür, içinde kanalın sözlüğünden 1–2 dipnot da olur.
- **Açık noktalar:** Gerçek raid için ikinci kanal. Provada CLI mock kullanılabilir. Pin varyantı test #1'e bağlı.

### 6. K20 Studio Audience (45)

- **Fikir:** Chat tepkileri canlı bir seyirci sesine dönüşür. Ses, tepki veren izleyici sayısıyla büyür, her izleyicinin kendine özgü bir kahkahası ve koltuğu vardır.
- **Güçlü yanı:** Tasarım (14). Üç modelin puanı da 15, en tutarlı aday.
- **Zayıf yanı:** Yenilik (9). Ses efekti alanı kalabalık. Fark "ölçeklenen seyirci" ve "isimli koltuk" olarak net anlatılmalı.
- **Eklenen özellik:** K28 Lurker fenerleri, boş koltuk olarak. Sessiz izleyiciler soluk koltuklarda oturur, ilk tepkilerinde koltukları yanar. Botlar filtrelenir; "izleyen herkes" iddiası yapılmaz.
- **Açık noktalar:** Yalnızca CC0 sesler kullanılır. Get Chatters testi (düşük risk).

### 7. K21 Foley Pit (44)

- **Fikir:** İzleyiciler bir sahnenin seslerini yazar (hava, ayak sesi, sürpriz). Yayıncı bu sesleri masadaki eşyalarla canlı yapar.
- **Güçlü yanı:** Yenilik ve tasarım (14 / 14). Grok'un 3 numarası.
- **Zayıf yanı:** Etki ve teknik (8 / 8). Tek seferlik bir segment olabilir, teknik hikâyesi ince.
- **Açık noktalar:** Teknik derinlik katmak için seçenekler var: kayıttan "foley reel" çıkarmak, chat'in performansı oylaması, ses analiziyle zamanlama. Bu adım 6'nın işi.

### 8. K17 Hint Jar (43)

- **Fikir:** Kör oynanışta izleyiciler kademeli ipucu bırakır (dürtme / yöntem / cevap). Yayıncı takılınca sadece istediği seviyeyi açar.
- **Güçlü yanı:** Opus'un ve Astra'nın ilk 5'inde. Backseat'i yardıma çeviriyor.
- **Zayıf yanı:** Teknik (9).
- **Açık noktalar:** Minefield ile aynı gizli giriş sorunu (test #11). G-1 Hint Airlock varyantı mod onaylı kuyruk kullanır, silme gerektirmez. Demo için kendi bulmacamız lazım.

### 9. K23 Photo Booth (40)

- **Fikir:** İzleyici `!snap` yazar. Yayıncı poz verir, flaş patlar, ekranda izleyicinin adıyla bir Polaroid belirir. Yayın sonunda hepsinden bir kolaj çıkar.
- **Güçlü yanı:** Astra'nın 4 numarası (16 verdi).
- **Zayıf yanı:** Yenilik (8). Grok yalnızca 11 verdi; modeller arasındaki en büyük fark bu adayda.
- **Açık noktalar:** obs-websocket ekran görüntüsü (#5) ve izleyicinin linki açabilmesi için herkese açık hosting veya tünel.

### 10. K01b Checkpoint (39)

- **Fikir:** Yayıncı meşgulken chat mesajları "kayıt kristali" olarak birikir. Molada call-in kartları olarak tek tek açılır.
- **Güçlü yanı:** Grok 15 verdi, gerçek bir dert ("meşgulken chat'i kaçırıyorum").
- **Zayıf yanı:** Yenilik ve teknik (9 / 9). Soru kuyruğu ve "ne kaçırdım" araçlarına yakın.
- **Not:** Kesime eşit puanla, yenilik farkıyla girdi (Desk Buddy de 39 aldı). Listenin en kırılgan adayı.

## Ortak altyapılar

Birkaç aday aynı parçayı kullanıyor. Finalde bunlardan biri seçilirse, aynı parça diğerinin de yolunu açar:

| Parça | Adaylar |
| --- | --- |
| Gizli giriş (whisper veya web formu) | Minefield, Hint Jar (+ Mühürlü tahminler modu) |
| obs-websocket (replay, ekran görüntüsü) | VAR, Photo Booth |
| Raid olayı + ikinci kanal | Raid Torch, Previously On |
| Herkese açık tünel | Photo Booth, web formu yedeği |

## Sıradaki adım (6)

1. **Kartları eşitlemek.** Her aday için en iyi varyant, MVP kapsamı, 3 dakikalık video akışı ve Codex'in rolü yazılır. Eklenen özellikler ve zayıf kriterin güçlendirilmesi de buraya işlenir.
2. **Üç kaynaktan kanıt toplamak:**
   - Grok: X taraması.
   - Claude ajanı: web, GitHub, Devpost.
   - Astra: kendi araması.
3. **Kanıtla birlikte 1–5 puanlama.** Ardından son 6 aday için video senaryosu ve spike'lar.
