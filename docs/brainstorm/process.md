# Brainstorm süreci

İki ajanın önerilerinin birleştirilmiş hali (2026-10-25). Amaç: her aşama bir sonraki kararı verebilmemizi sağlasın, daha fazla metin değil.

## Girdiler

- Tek kişi, toplam **20–25 insan saati**, çok sayıda paralel AI agent.
- Güçlü: Python, FastAPI, Docker, Redis, Qdrant, ML (4 yıl). OpenRouter üzerinden LLM. Başka teknolojilere açık.
- Twitch deneyimi yok, topluluk yok. Demo kanalı: 1 yayıncı (sen) + birkaç test hesabı.

## Saat bütçesi ve takvim

| Blok | İnsan saati | Ne zaman |
| --- | ---: | --- |
| Twitch kurulumu ve tanışma | 2 | 25–26 Ekim |
| Saha gözlemi (yayın izleme) | 2 | 25–26 Ekim |
| Brainstorm, daraltma, karar | 3 | 25–27 Ekim |
| Finalistler için teknik deneme | 2 | 27 Ekim |
| Geliştirme (agent yönetimi, inceleme, canlı test) | 9–10 | 27–31 Ekim |
| Video ve teslim metni | 4 | 1 Kasım |
| Yedek | 2 | 2 Kasım |

Teslim hedefi: **2 Kasım, İstanbul saatiyle en geç 20:00** (resmi son: 3 Kasım 01:00).

## Akış

1. **Dalga 1: araştırma** (4 agent, paralel). Sen aynı anda Twitch kurulumu ve saha gözlemi yaparsın.
2. **Senin bağımsız girdin:** Agent çıktılarını okumadan önce 5 gözlem ve varsa birkaç ham fikir yazarsın (`human-notes.md`).
3. **Dalga 2: fikir üretimi** (3 Claude agent + GPT 6 Astra + Grok, farklı mercekler, birbirini görmez). Brief: [wave2/brief.md](wave2/brief.md), mercekler: [wave2/prompts.md](wave2/prompts.md). Ardından Grok, fikir kümeleri için X'te benzer ürün ve talep araması yapar.
4. **Sentez** (ben): Tekrarlar ayıklanır, kümelenir. Yaygın fikirler işaretlenir, ama elenmez.
5. **Dalga 3: değerlendirme.** Kör iki değerlendirici: ürün/özgünlük ve uygulama/demo. Kaynak ve tercihlerimiz gizli tutulur.
6. **Kısa liste:** 2–3 aday. Her biri için uygulama taslağı ve en riskli varsayım.
7. **Teknik deneme:** En riskli varsayımlar 1–2 saatte sınanır.
8. **Karar** (sen). Ardından Codex'te ana thread açılır.

## Model ve effort

| Aşama | Model | Effort | Neden |
| --- | --- | --- | --- |
| Dalga 1: A, B, C, D | Sonnet 5.5 | high | Senin kararın (2026-10-25): dördü de aynı ayarla |
| Dalga 2: L1, L3 | Opus 5.5 | high | Kalitenin en çok önemli olduğu yer |
| Dalga 2: L2 (gösteri) | Opus 5.5 | xhigh | En yaratıcı mercek. Fable pakette yok (2026-10-25). |
| Dalga 2: G | GPT 6 Astra | – | Farklı model ailesi, merceksiz |
| Dalga 2: X | Grok | – | Merceksiz, canlı X postlarına dayalı |
| Dalga 3: kör değerlendirme | Opus + GPT 6 Astra | high | Eleştiri kalitesi. Karışık model ailesi, kendi fikrini kayırma yanlılığını azaltır. |
| Kısa liste: uygulama taslağı | Opus | xhigh | Mimari ve riskler |

İsteğe bağlı: Aynı fikir prompt'unu başka bir modelde (ör. Codex/GPT) de çalıştırmak, fikir çeşitliliğini artırır.

**Fiyatlar** (API, 1M token başına, girdi / çıktı):

| Model | Fiyat | Not |
| --- | --- | --- |
| Haiku 5.5 | $0,10 / $0,50 | 100K token'a kadar olan prompt'lar |
| Haiku 5.5 | $0,50 / $2,50 | 100K token'ı aşan prompt'lar |
| Sonnet 5.5 | $2 / $10 | |
| Opus 5.5 | $4 / $20 | |
| Fable 5.1 | $10 / $50 | |

Kaynak: Claude Code'daki `claude-api` skill'i (önbellek tarihi 2026-10-06). Web'den doğrulanmadı. Abonelikle kullanımda maliyet para olarak değil, kullanım limitinden düşüş olarak yansır.

## Değerlendirme

**Sert filtreler (geçti/kaldı):** Bunlar yapılabilirlik filtresi. Kanıtsız fikir bu yüzden elenmez.
- Affiliate/Partner özelliği gerektirmiyor (ya da yedeği var).
- Extension gerektirmiyor.
- 1 yayıncı + birkaç test hesabıyla inandırıcı demosu çekilebiliyor.
- Geliştirme bloğunun saat bütçesine sığıyor.

**Puanlama:** Resmi 4 kriter eşit ağırlıkta (1–5 arası). **Kanıt gücü** ve **teslim riski** ayrı sütunlarda gösterilir. Puanlar tartışmayı düzenler, kararı vermez.

**Benzerlik kontrolü:** Tanıdık görünen bir aday, "mevcut yaklaşımdan anlamlı farkı ne ve bu fark deneyimi nasıl değiştiriyor?" sorusuna güçlü cevap vermek zorunda.

## Senin görevlerin (dalga 1 sırasında)

**Twitch kurulumu.** Gereksinimlerin doğrulamasını Agent A yapacak.
- Hesap aç, iki adımlı doğrulamayı aç, dev.twitch.tv console'da uygulama kaydet.
- OBS'yi kur ve kendi kanalına kısa bir test yayını yap. Yüz ve ses gerekmez.
- Chat testi için 2–3 yardımcı hesap aç.

**Saha gözlemi (~2 saat).** Farklı kategorilerden canlı yayın izle: Just Chatting, IRL, Art, Music, bir oyun, bir eğitim/bilim yayını. Her dikkat çekici an için şunları not et:
- kategori ve izleyici sayısı
- ne oldu
- chat ne yaptı
- yayıncı ne yaptı
- sürtünme veya elle yapılan iş
- şaşırtıcı olan

Hedef 5 somut gözlem. `docs/brainstorm/human-notes.md` dosyasına yaz.

## Klasör yapısı

```
docs/brainstorm/
  process.md          bu dosya
  human-notes.md      senin gözlemlerin
  wave1/              A–D araştırma çıktıları
  wave2/              fikir kartları
  wave3/              değerlendirmeler
  shortlist/          finalist dosyaları
  synthesis.md        Türkçe sentez ve kararlar
```

---

## Ortak brief (her prompt'un başına eklenir)

```
CONTEXT
We are preparing an entry for the Codex x TwitchCon Hackathon (Devpost).
Read docs/competition/overview.md, rules.md and resources.md before starting.

COMPETITION REQUIREMENTS (from the official rules)
- Interactive experience that connects to Twitch (chat, overlay, Twitch API,
  EventSub or Extension), built with OpenAI Codex, newly created after Oct 23, 2026.
- Submit: code repo with run instructions; <3 min public YouTube demo showing it
  working on Twitch and how Codex was used; English description; Codex session ID.
- Four equally weighted criteria: Innovation/Idea, Potential Impact,
  Technical implementation (incl. use of Codex), Design (easy to use, fun to watch).
  Ties are broken by Innovation first. Judges are not required to run the project.
- Deadline: Nov 2, 2026, 14:00 PT.

OUR STRATEGIC CHOICES (not rules)
- Avoid Extensions (5–14 day review). Prefer chat, OBS browser-source overlays,
  Twitch API, EventSub.
- Solo builder, ~20–25 human hours total, many AI coding agents available.
  Strong in Python/FastAPI/Docker/Redis/Qdrant/ML, open to other stacks;
  LLMs available via OpenRouter.
- Builder is new to Twitch and has no audience: the demo channel will have one
  streamer plus a few test accounts.

UNVERIFIED ASSUMPTIONS (treat as hypotheses, flag evidence for or against)
- Many entrants will build close to the organizer's examples (Twitch Plays, polls,
  dice rollers, sports overlays) or generic AI chatbots.
- Judges will mostly judge from the video and description.
- Affiliate/Partner-only features are unavailable to us.

EVIDENCE RULES
- Separate: verified fact / inference / unknown. Label each claim.
- Every decision-relevant claim needs a source URL and date, and the source must
  actually support the claim (a marketing page is not evidence of user success).
  If you only saw a search snippet, say so.
- If a source is inaccessible, say so; never guess its content.
- "I didn't find it" is not "it doesn't exist".
- Look for evidence against your own conclusions.
- Stay in scope. Do not spawn other agents. Do not write code.
```

## Dalga 1 prompt'ları

Her prompt şöyle kurulur: ortak brief + aşağıdaki blok. Araştırma agent'ları için daha hızlı bir model yeterli.

### A — Twitch yetenek ve kısıt haritası

```
TASK
Map what we can technically do on Twitch within our constraints, and what blocks us.
Do NOT propose product ideas.

ANSWER
1. Surfaces: chat (read/send, bot accounts, commands, whispers), EventSub event
   types (list all, mark which need which scopes / broadcaster role / affiliate),
   Helix API endpoints with unusual or underused affordances, OBS browser-source
   overlays (how they get data), clips/VOD/stream metadata, raids, shoutouts.
2. Gating: which features require Affiliate/Partner (polls, predictions, channel
   points, bits, hype train, etc.). What the Affiliate requirements are and whether
   reaching them before Nov 2 is realistic.
3. Practical setup for a brand-new account: 2FA, app registration, OAuth flows
   (which grant type for a bot vs. a broadcaster), tokens, rate limits.
4. Testing without an audience: Twitch CLI (mock EventSub triggers, mock API),
   multiple test accounts, chat simulation, and any ToS limits on these.
5. Latency: chat, EventSub, stream delay. What can and cannot feel "real-time"
   to viewers.
6. Content/ToS rules that affect a demo (music, game footage, bots).

OUTPUT
docs/brainstorm/wave1/A-capabilities.md, max ~1500 words:
- capability table: surface | what it allows | requirements | latency | source
- constraint table: constraint | impact on us | workaround | source
- open questions
STOP when all six questions are answered or listed as open with the reason.
```

### B — Twitch kültürü, kullanım ve acı noktaları

```
TASK
The builder has never used Twitch. Explain how streams actually work socially,
and where streamers, viewers and moderators struggle. Do NOT propose product ideas.

ANSWER
1. Roles and their motivations: streamer, moderators, VIPs, subscribers, regulars,
   lurkers, new viewers. Small streamers (0–50 viewers) vs. large.
2. Rituals and conventions: emotes, commands, raids, hype trains, channel points,
   clips, predictions, alerts, "chat plays", copypasta, backseating, etc.
3. Category differences: Just Chatting, IRL, Art/Creative, Music, Games,
   Science/Education, TTRPG. How interaction differs.
4. Pain points with evidence (UserVoice twitch.uservoice.com, r/Twitch,
   r/Twitch_Startup, r/streaming, TwitchDev forum). For each: who, context,
   how often it appears, current workaround, why the workaround falls short.
   Mark which are solvable from outside Twitch (chat/overlay/API) and which
   need Twitch itself to change. Treat "many votes" as a signal, not a verdict.
5. Viewer-side and streamer-side needs listed separately.

OUTPUT
docs/brainstorm/wave1/B-culture-needs.md, max ~1800 words:
- short primer (roles, rituals, categories)
- needs table: need | who | context | evidence strength | solvable by us? | source
STOP when a new source mostly repeats findings already recorded.
```

### C — Diğer platformlardan mekanizmalar

```
TASK
Find interaction mechanisms from other live/social platforms that Twitch lacks
or underuses. Report mechanisms, not products to clone. Do NOT pitch ideas.

SCOPE
TikTok Live (gifts, interactive live games, battles), YouTube Live, Kick,
Instagram Live, Bilibili/Douyin/Niconico (danmaku), Chinese live commerce,
Jackbox audience mode, HQ-style live quizzes, Discord Activities/Stages,
sports/esports second-screen and broadcast tooling.

ANSWER for each mechanism
- what it is, where it lives
- evidence of success (usage, repeat use, revenue, user stories); if none found,
  label "success unverified"
- whether it already exists on Twitch natively or via a third-party tool
- what it would take to work with Twitch's surfaces and a tiny audience

OUTPUT
docs/brainstorm/wave1/C-mechanisms.md, max ~1500 words:
table: mechanism | platform | evidence of success | on Twitch already? |
transfer conditions | source
STOP at ~15 well-evidenced mechanisms or when sources start repeating.
```

### D — Mevcut araçlar ve rakip manzarası

```
TASK
Map what already exists for Twitch so we can later judge novelty, and calibrate
the scope/quality bar of hackathon entries. Do NOT propose ideas.

ANSWER
1. Popular third-party tools and what they cover: StreamElements, Streamlabs,
   Streamer.bot, Nightbot, Moobot, Crowd Control, Sound Alerts, Mix It Up,
   SAMMI, popular Extensions, AI co-host / AI chatbot products.
   Group by job-to-be-done.
2. dev.twitch.tv/showcase: what is featured.
3. Past Twitch or livestreaming hackathon winners (Devpost and others): scope,
   presentation, demo style. Describe them. Do not claim why they won.
4. Signals about this hackathon's entries, if public (Devpost participants page,
   TwitchDev Discord announcements). Report only what is observable.

OUTPUT
docs/brainstorm/wave1/D-landscape.md, max ~1500 words:
- tools table: tool | jobs covered | strength | gap | source
- past entries table: name | event | what it did | demo style | source
STOP when the major tools per job are covered.
```

## Fikir kartı şablonu (dalga 2)

```
### <Name>
- One-liner:
- Who installs it / who gets the value (streamer, viewers, mods — separately):
- Streamer category fit:
- Core loop (what the viewer does → what happens on screen):
- First 10 seconds of the demo (what a judge sees):
- Twitch surfaces used:
- Works with 1 streamer + 3 test accounts? How?
- Closest existing thing and the meaningful difference:
- Evidence it links to (wave 1 files/rows), or "unvalidated — how we'd validate":
- MVP scope / explicitly out of scope:
- Riskiest assumption:
```
