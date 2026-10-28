# Scoring task: 7 Twitch hackathon project cards

You are one of three independent raters. Score each of the 7 project cards below the way the hackathon judges would, using only what is in this message. **Do not search the web, do not use outside knowledge about these specific products, and do not ask follow-up questions.** Read only this file; do not open other files.

## The hackathon

Codex x TwitchCon Hackathon. Solo entrant. Judges watch a demo video under 3 minutes and score four criteria with **equal weight**:

- **Innovation:** "How creative and novel is the concept and does the project differ from existing concepts?"
- **Impact:** "How useful or entertaining is it for streamers and their communities?"
- **Tech:** "How well is it built, and how well does it use Codex?"
- **Design:** "Is it easy to use and fun to watch?"

**Score the project that can actually be built and shown under these conditions, not the idea in the abstract:** 15 build hours, one streamer and three test accounts, no commercial games or music (a small Codex-built original game or an MIT-licensed game may stand in, about 1 h), a video under 3 minutes.

## Scale (1–5 per criterion; 2 and 4 sit between the anchors)

| Criterion | 5 | 3 | 1 |
| --- | --- | --- | --- |
| Innovation | Nothing similar was found; the loop is new | A new combination of existing parts, with a difference that shows in the video | The same as a well-known product |
| Impact | The problem or desire is strongly evidenced, in common stream types, and the tool would be used every week | A real problem but a narrow audience, or only indirect evidence | No evidence; niche |
| Tech | Can be built well in 15 h, technically interesting, and Codex's role is concrete | Buildable but ordinary, or interesting but risky | Trivial, or does not fit 15 h |
| Design | Understood within the first 20 s of the video and fun to watch even with three test accounts | Understandable but visually ordinary | Confusing, or flat on video |

Rules:
1. The anchors are absolute. Do not give every card the same scores; if two cards differ, the scores should show it.
2. Give every score a 1–2 sentence reason that points to something specific in the card or its evidence.
3. Rate **risk** separately (Low / Medium / High): how likely it is that a day-1 test fails or the demo can't be shown as described. Name the test. Risk is not part of the total.
4. Then rank all 7 cards from the one you would most like to see win to the least, one sentence each.
5. The evidence lists competitors. A card is not worse just because related tools exist; judge how much the card's own loop differs, and whether that difference is visible in the video.

## Output format (use exactly this)

```
## Scores
| Card | Innovation | Impact | Tech | Design | Total | Risk | Risk depends on |
| --- | --- | --- | --- | --- | --- | --- | --- |
(one row per card, in the order the cards appear below)

## Reasons
### <card name>
- Innovation (n): ...
- Impact (n): ...
- Tech (n): ...
- Design (n): ...
- Risk (Low/Medium/High): ...
- Biggest weakness: ...

## Ranking
1. <card name>: one sentence
...
7. <card name>: one sentence
```

The cards appear in this order: Raid Torch, Minefield, Checkpoint, VAR, Hint Jar, Tap on the Shoulder, Studio Audience.

## Shared build facts (apply to every card)

**Constraints**
- One streamer plus three test accounts. No real audience.
- No commercial games or commercial music in the video. Where a card's natural setting is a game, the demo can use a small original game built with Codex (about 1 h, paid from the buffer) or an MIT-licensed open-source game.
- No Twitch content kept beyond 24 h.
- Build budget: 15 hours total, excluding recording and editing the video. Each card = shared base (3.5 h) + its own MVP (at most 9.5 h); at least 2 h stay free as a buffer.

**Shared base (already built for every card, 3.5 h):** Twitch app with OAuth for broadcaster and bot and token refresh; EventSub WebSocket chat and Send Chat Message; a local FastAPI server pushing to OBS browser sources and an OBS dock; obs-websocket connection; and a Codex-built chat simulator in which the three test accounts post scripted chat over the real API (used for rehearsal, tests and recording).

**How Codex is used:** the whole project is built with Codex in one main thread. The chat simulator is the shared Codex-built part; each card names one more concrete Codex artifact.

**Twitch facts used across cards**
- Create Clip takes `title` and `duration` (5–60 s). It captures the live output from roughly 85 s before to 5 s after the call and is asynchronous. Which part of that window `duration` keeps is not documented.
- `channel.raid` gives the two channels and a viewer count, not the list of raiders. Individual raiders can only be recognized when they chat.
- Create Stream Marker needs VOD storage enabled.
- Send Chat Message supports threaded replies (`reply_parent_message_id`).

**Day-1 tests (run before building; a failed test means the fallback in the card's risks)**

| Test | What it checks | Cards | Pass condition |
| --- | --- | --- | --- |
| T1 | Real-time local speech-to-text keyword spotting during a live stream | Minefield | ≥80% hits, ≤1 false alarm per 10 min, ≤3 s lag |
| T1b | Local speech-to-text of spoken answers | Checkpoint | Quote ready ≤2 s after the streamer stops; ≥9 of 10 readable without edits |
| T2 | obs-websocket: replay buffer + Media Source slow motion, mute/silence events | Tap, VAR | Replay on screen ≤5 s; mute event arrives |
| T3 | Second live channel + a real raid between the two | Raid Torch | Both live; raid event ≤5 s |
| T4 | Sealed input: viewer → bot whisper, or a login page behind a public URL | Minefield, Hint Jar | One path works end to end |
| T5 | API checks: Create Clip with title, Stream Marker, Get Chatters | Minefield, VAR, Studio Audience, Checkpoint (stretch) | All succeed on a new channel |

## How to read the evidence

Three independent researchers searched the web for each card: **A**, **G** and **C**. A separate link check (**L**) opened pages that only one researcher had found. For Checkpoint, whose design changed after the research, the changed part was checked by one more source (**P**).

- **Confirmed**: found by two or more researchers.
- **Verified**: found by one researcher, and the link check opened the page.
- **Unverified**: the page could not be opened (blocked site, Reddit, X, or a search snippet only). It may exist; treat it as weaker evidence.
- **Overlap**: `Same core loop` (same who acts, same trigger, same output on stream), `Partial`, or `Adjacent`.
- **Well-known**: a major streaming platform or tool (Twitch, StreamElements, Streamlabs, Streamer.bot, Elgato, OBS, Meld, Sound Alerts, StreamUP), ≥1,000 users or installs, ≥100 GitHub stars, or a post with ≥10,000 views.
- Stream-type shares come from a research snapshot: Just Chatting 14.2% of viewing, IRL 1.8%, games make up most of the top 15 categories, indie games +51% YoY, horror +6%.

## The 7 cards and their evidence

Each card is followed by its evidence.

### Card: Raid Torch

**One-liner:** A torch that only travels by raid: every chat that holds it leaves a mark, and the raiders who carried it light up when they chat on arrival.

**Core loop:**
1. Channels join a circle with a code, on a hosted backend.
2. While a channel holds the torch, each chatter adds one mark with `!mark <emote>`, and rings grow on the torch. Twitch-native emotes render as images; third-party emotes show as text.
3. The streamer raids. EventSub `channel.raid` hands the torch over.
4. On the target's overlay, the torch flies in with its rings and a journey map ("3 channels, 14 marks tonight").
5. **Torch-bearers:** a raider who added a mark glows when they first chat in the new channel ("Ana carried a mark from A"). The target streamer sees which torch-bearers arrived; Twitch's raid event gives only a count, so raiders without a mark stay anonymous.
6. A public journey page shows tonight's path. It resets after the evening.

**3-minute video:**
- 0:00 Hook: channel A's torch glowing, the raid, cut to channel B: the torch flies in, raiders' names glow as they chat "we brought that!".
- 0:25 How marks are added.
- 0:50 The journey map with three hops (two rehearsal hops, labeled as such) and the public page.
- 1:30 Torch-bearers from the host's view.
- 2:00 How the hosted backend links channels.
- 2:30 Codex artifact, close.

**Codex artifact:** the hosted backend with its deploy, and the journey page.

**MVP:**
- **In:** circle code, `!mark`, torch overlay, raid handoff, fly-in, torch-bearers, journey page, hosted backend.
- **Stretch:** one-sided send-off, pinned arrival message.
- **Out:** multi-day journeys, multiple torches, leaderboards.

**Build parts:**

| Part | Hours |
| --- | --- |
| Hosted backend + circle state + deploy (free PaaS) | 2.5 |
| Raid events for circle channels | 0.5 |
| `!mark` with emote fragments | 0.5 |
| Torch overlay with rings + fly-in | 2.5 |
| Torch-bearers | 1 |
| Journey page | 1.5 |
| Polish | 1 |
| **MVP subtotal** | **9.5** |
| Stretch: send-off 0.5, pinned arrival 0.5 | 1 |

**Twitch surfaces, scopes and local parts:** EventSub `channel.raid` (no authorization needed) and `channel.chat.message` in each circle channel, Get Users (avatars), optional Start a Raid and Pin Chat Message; OBS browser source; a hosted backend with a public URL.

**Demo setup:** 1 streamer + 3 test accounts, and **a second live channel** (a test account streaming from a phone or a second OBS).

**Closest existing things and claimed difference:** raid alerts; raid-train tools (R3dLabs Toolbox Stream Deck plugin, RaidRunner scheduling and lineups); RaidPort (beta: streamers raid a hub channel and a wheel picks the next raid); Teams+ (TwitchCon Hackathon 2019: trusted-viewer labels shared across a Team); organised relays and raid-train communities (Twitch Storm 2020, Raid Train Central). *Difference:* state carried across channels; the raid becomes a visible object, and marked raiders are recognized when they chat on arrival.

**Risks and day-1 tests:**
- Second live channel and a real raid (T3).
- One person's two channels may not make "community relay" feel real.
- Value depends on both sides adopting it; the send-off is the one-sided fallback.
- Hate raids made small streamers wary of raids; only channels that joined the circle with its code take part.
- Many raiders leave quickly; torch-bearers only light up for those who chat.

### Evidence: Raid Torch

**Card in one line:** a torch travels between channels by raid; chatters add marks to it, and when it arrives, torch-bearers who chat in the new channel light up.

**Competitors**

| Name | What it does | Found by / status | Overlap | Well-known |
| --- | --- | --- | --- | --- |
| [R3dLabs Toolbox](https://r3dlabs.com/tools) | Raid-train scheduling and one-press raid to the next slot | A, G, C / confirmed | Partial–Adjacent | No counts (Elgato marketplace listing, v0.1.1.3, Dec 2024) |
| [RaidRunner](https://raidrunner.net/) | Raid-train sign-ups, slots, lineup API, Twitch extension | A, G, C / confirmed | Partial–Adjacent | No counts |
| [RaidPort](https://raidport.tv) | Streamers raid a hub channel and earn a wheel slice; chat votes; the wheel picks a live channel to raid. Beta | C (snippet) → L / verified | Adjacent | No |
| [Teams+](https://blog.twitch.tv/en/2019/10/31/highlights-from-the-twitchcon-hackathon-2019) (TwitchCon Hackathon 2019) | Trusted-viewer labels shared across a Team | C / verified | Adjacent | No |
| [Raid Train Central](https://raidtraincentral.carrd.co/), raid trains as a format | Organised themed trains | C, G / confirmed | Adjacent | No counts |
| WooferBot raid pose | Mascot and lights react to raids | G | Adjacent | No |
| Twitch Storm (2020 relay, ~200 streamers) | Organised 24 h relay | C / snippet | Adjacent | Claimed 156k viewers (unverified) |
| Native highlighting of arriving raiders | Users report Twitch marking raiders' messages | A / Reddit, unverified | Partial | Twitch |

Dropped: Raid Train (Devpost, unverifiable).

**Difference:** tools handle scheduling and the raid itself; none carries a visible object with per-chatter marks from channel to channel. A: "partly" (the difference rests on the shared object and its history); G and C: "yes".

**Demand**
- Raid trains are an active practice in October 2026: DJ, VTuber, artist and horror charity trains (G, X, unverified); [Raid Train Central](https://raidtraincentral.carrd.co/) active in 2026 (L / verified); RaidRunner's guide says picking the next raid becomes "a second job" (G).
- Raids count toward Partner status since Oct 2024 (C, snippet; page blocked).
- No request for a carried object or named raiders on arrival (A, G, C).

**Counter-signals**
- Hate raids made small streamers wary of raids ([PinkNews, 2021](https://thepinknews.com/2021/08/31/twitch-hate-raids-solution-rekitraven/), L / verified); a raid-blocker extension exists (C, snippet).
- Many raiders leave right away (A, Reddit, unverified; C, snippet).

**Audience fit:** any category that raids; in practice small and mid streamers in raid circles. Type-independent: G and C yes (needs a circle of channels), A no (needs an opted-in relay format). Natural-setting demo: G yes; A and C partly: a real raid between our own channels works, but a real multi-community relay cannot be shown with one streamer and three viewer accounts.

**Fact issues**
- `channel.raid` gives the two channels and a viewer count, **not** the list of raiders (A, G, C). The torch can only recognise people it already knows (torch-bearers with marks) when they chat in the new channel.
- Raids have a 90 s countdown and can be cancelled (C).

---

### Card: Minefield

**One-liner:** Viewers secretly plant "word mines". When the streamer says a mined word out loud, it explodes on stream with the planter's name.

**Core loop:**
1. A viewer types `!mine`. The bot replies with a link to a plant page (Twitch login). Nobody else sees the word.
2. The overlay shows mine chips with owners' names, never the words. Rules: one live mine per viewer, 4+ letters, not a top-1000 common word, blocklist.
3. Viewers steer the conversation toward their word ("worst pizza topping?").
4. Local speech-to-text listens to the streamer's mic: faster-whisper (`base.en`/`small.en`) on a sliding ~2 s window, VAD on, live mines passed as `hotwords`, whole-word match on normalized text (plurals count).
5. Instant explosion, screen shake, the banner "Bo's mine: PINEAPPLE (planted 6 min ago)" and a stream marker. A mod can **DEFUSE** within 10 s: a rewind animation and a "false alarm" stamp, played as a gag. If not defused, a titled 30 s clip is created.
6. Unexploded mines flip over as "duds" at the end: "Cy's mine 'GIRAFFE' never went off".

**3-minute video:**
- 0:00 Hook: chatting about lunch, "pineapple on pizza is—" BOOM, banner, Bo's chat line "GOT HIM 😈", cut back to Bo's bait question.
- 0:20 How it works: `!mine`, the plant page, chips, the rules.
- 0:50 Round two: two viewers bait; one mine hits, one fails; a misheard word fires and a mod defuses it.
- 1:40 The dud reveal at the end of the stream.
- 2:00 Under the hood: local speech-to-text, nothing recorded, hotwords and whole-word matching, with accuracy numbers from our test harness.
- 2:30 Codex artifact, close.

**Codex artifact:** an accuracy harness that replays recorded test talk through the spotter and reports hits, false alarms and lag.

**MVP:**
- **In:** plant page, chips overlay, local keyword spotting, explosion and banner, marker, titled clip, DEFUSE, dud reveal.
- **Stretch:** whisper intake (if T4 passes), "Call it" mode.
- **Out:** leaderboards across streams, multi-word phrases, any LLM.

**Build parts:**

| Part | Hours |
| --- | --- |
| Plant page with Twitch login + public URL | 1.5 |
| Speech-to-text spotter + matching rules | 2.5 |
| Accuracy harness | 1 |
| Overlay: chips, explosion, banner | 2 |
| Marker, clip, DEFUSE, duds | 1.5 |
| Polish | 1 |
| **MVP subtotal** | **9.5** |
| Stretch: whisper intake 0.5, "Call it" 1.5 | 2 |

**Twitch surfaces, scopes and local parts:** EventSub `channel.chat.message` (`user.whisper.message` in stretch), Send Chat Message, Create Stream Marker (`channel:manage:broadcast`, VOD storage on), Create Clip (`clips:edit`); OBS browser source; local speech-to-text on the mic only; a public URL for the plant page.

**Demo setup:** 1 streamer + 3 test accounts. Mic and webcam. To keep the demo from looking staged, one or two friends plant words through the page, so the streamer really doesn't know them.

**Closest existing things and claimed difference:** OK Gamers (TwitchCon Hackathon 2019 grand prize: streamer speech starts a chat poll); Streamer.bot Voice Control (phrases the streamer configured trigger actions); speech-recognition swear jars (Blabla Radar Swear Jar, obs-popup-overlay); stream-bingo overlays (1up.vision Bingo); secret-word chat games (AnkhbotSecretWord) and Taboo-style games (Wordeous). *Difference:* every speech trigger found uses words the streamer chose, and every viewer-chosen secret-word game runs in typed chat. Here viewers secretly choose the words and the streamer's own speech sets them off, inside ordinary talk.

**Risks and day-1 tests:**
- Speech-to-text accuracy and false hits on casual speech (T1).
- Sealed intake: the plant page needs a public URL and login; whisper intake is unverified (T4).
- Fun is unvalidated: a 20-minute session with three people.
- Trolls already try to bait streamers into saying things on air; the blocklist screens planted words before they go live.
- faster-whisper hotwords can be hallucinated on silence; VAD stays on (known fix).

### Evidence: Minefield

**Card in one line:** viewers secretly plant words; when the streamer says one, an automatic explosion names the planter.

**Competitors**

| Name | What it does | Found by / status | Overlap | Well-known |
| --- | --- | --- | --- | --- |
| [OK Gamers](https://devpost.com/software/ok-gamers) (TwitchCon Hackathon 2019, grand prize) | Streamer says "Ok gamers" + a question; speech-to-text starts a chat poll | A, G, C / confirmed | Partial | No (archived 2020, 3 stars) |
| [Streamer.bot Voice Control](https://docs.streamer.bot/guide/voice-control) | Phrases the streamer configured trigger actions, including mid-sentence | A, C / confirmed | Partial | Yes (Streamer.bot) |
| [1up.vision Bingo](https://www.1up.vision/en/features/bingo) | Bingo board of stream events, marked by hand | A, G, C / confirmed | Partial–Adjacent | No counts found |
| [Blabla Radar Swear Jar](https://blablaradar.com/en/swear-jar) | Browser speech recognition counts words from the user's own list | A / verified | Partial | No |
| [obs-popup-overlay](https://github.com/erfur/obs-popup-overlay) | Offline speech recognition shows an image on one hotword | G / verified | Partial | No (0 stars) |
| [scpedicini/swearjar](https://github.com/scpedicini/swearjar) | Browser beep on a censored-word list | G / verified | Partial–Adjacent | No |
| AnkhbotSecretWord, Wordeous (19 Steam reviews), Kloot swear-jar counter, Taboo, Nightbot counters, LocalVocal (1.7k stars, captions only) | Secret word typed in chat; Taboo-style games; manual counters; speech-to-text building block | C, G, A / verified or common knowledge | Adjacent | LocalVocal only |

**Difference:** all three researchers say it survives. Every speech trigger found uses words the streamer chose; every viewer-chosen secret-word game runs in typed chat. A re-search in the link check found nothing closer.

**Demand**
- No direct request for this game (A, G, C).
- Indirect: streamers run manual swear jars and bingo cards (G: X posts, unverified; A: a channel's `!swear` command page). Two Reddit threads ask for mic word detection to trigger an effect (A, G; unverified, Reddit).

**Counter-signals**
- Trolls already try to make streamers say things on air ([Dexerto, 2019](https://www.dexerto.com/entertainment/korean-irl-streamers-baited-lewd-donation-prank-1045134/), C / verified). A tool that rewards steering the streamer into a word needs a word filter.
- faster-whisper hotwords can hallucinate on silence; the maintainer's fix is the VAD filter ([issue 1356](https://github.com/SYSTRAN/faster-whisper/issues/1356), A / verified).

**Audience fit:** any stream where the streamer talks: Just Chatting (14.2%) and IRL (1.8%), plus talkative game streams (share not measured). English speech-to-text as specified. Researchers disagree on "type-independent" (A yes if the streamer talks, G no, C mostly); they agree it depends on talk. Natural-setting demo: Yes (all three).

**Fact issues:** none contradicted. Create Clip with title and 5–60 s duration is supported. VAD is required.

---

### Card: Checkpoint

**One-liner:** Go heads-down without ghosting chat: messages become save crystals, and at the checkpoint the streamer answers out loud, the words type onto the card, and each viewer gets a threaded reply quoting what the streamer said.

**Core loop:**
1. The streamer hits a hotkey or a mod types `!focus`. A corner badge: "Focus: messages saved 0".
2. Each normal viewer message drops a save crystal in the viewer's color. Commands and bot lines are filtered out. The app keeps the message id, author, text and first-time flag.
3. The streamer hits "checkpoint". A lower-third call-in card shows the first saved message. Questions and first-time chatters come first.
4. The streamer answers aloud without stopping work. Local speech-to-text (faster-whisper) types the words onto the card as they are spoken.
5. About 2 s of silence, or "next", closes the card: it stamps ✓ and flies off. After 3 s the bot replies in the viewer's thread: "✓ answered on stream: 'It's a Micron 05, it doesn't bleed' (12:04)". If the transcript is empty or low-confidence, the reply drops the quote: "✓ answered on stream (12:04)". "Skip" closes the card with no reply.
6. At the end: "Checkpoint cleared: 4 answered, 4 receipts sent".
7. *(Stretch)* When a clip of the answer is confirmed, a second threaded reply adds "▶ watch it: <clip link>".

**3-minute video:**
- 0:00 Hook: inking time-lapse, 6 crystals stack. The streamer taps checkpoint; the card reads "@ana (first time!): what pen is that?". Still inking, the streamer says "Ana, it's a Micron 05, it doesn't bleed"; the words type onto the card; silence, ✓, fly-off; split screen of Ana's chat with the threaded quote. The next card is up at 0:19.
- 0:20 Two more cards: one closed with "skip", one with a low-confidence transcript that sends the plain receipt.
- 1:00 A viewer who "left" opens chat later and finds the answer.
- 1:30 Under the hood: voice segmenting, the silence rule, reply threading.
- 2:05 Codex artifact.
- 2:30 Close. If the clip stretch is done, it gets 10 s around 1:00.

**Codex artifact:** the voice-to-receipt pipeline, tested with recorded answer audio and simulated chat during focus.

**MVP:**
- **In:** focus toggle (hotkey, mod), filter, crystal badge, call-in card with live transcript line, dock with next/skip, ordering, local speech-to-text, silence close with hold key, answer receipt with confidence gate.
- **Stretch:** clip link reply; closing on the next viewer's name; reminder; scene auto-start.
- **Out:** context thumbnails (cut in revision 3; also removes the stream-delay mismatch), urgent lane, LLM summaries, history beyond the stream.

**Build parts:**

| Part | Hours |
| --- | --- |
| Focus toggle (hotkey, mod `!focus`) + filter | 1 |
| Crystal badge overlay | 1.5 |
| Call-in card overlay with live transcript line and ✓ stamp | 1.5 |
| Dock + ordering + next/skip | 1 |
| Local speech-to-text: mic capture, voice-activity segmenting, faster-whisper, partial updates | 2 |
| Voice close: silence rule, hold key, tuned on recorded clips | 0.5 |
| Answer receipt: confidence gate, trim to 500 chars, threaded reply, `drop_reason` handling | 0.5 |
| Polish | 1 |
| **MVP subtotal** | **9** |
| Stretch: clip link reply (Create Clip From VOD, fallback Create Clip; poll Get Clips) 1, name-based close 0.5, reminder 0.5 | 2 |

**Twitch surfaces, scopes and local parts:** EventSub chat (`message_id`), Send Chat Message with `reply_parent_message_id` (500-char limit, read `is_sent` / `drop_reason`); the bot is a moderator (100 messages per 30 s instead of 20). Stretch: `clips:edit` or `channel:manage:clips`, Get Clips. OBS browser source and dock; local mic + faster-whisper (shared with Minefield).

**Demo setup:** 1 streamer + 3 test accounts. Webcam and mic. A focus task on our own content (drawing, building, or a small Codex-built game).

**Closest existing things and claimed difference:** Meld X AMA Question Queue (same core loop up to the featured question; well-known, so this card used its one pivot), StreamerQnA, Social Stream Ninja featured message, Senchabot featured message, Chatterino highlights. *Difference:* the streamer answers by voice without lifting a hand, and each viewer receives the streamer's actual words as a threaded reply.

**Risks and day-1 tests:**
- Speech-to-text speed and accuracy on the user's machine (T1b). If it fails, switch to the pause-trigger fallback.
- A thinking pause closes the card early: 2 s threshold plus a hold key.
- A misheard word in a viewer's quote: the confidence gate sends the plain receipt instead.
- AutoMod or blocked terms drop the reply: read `drop_reason`.

### Evidence: Checkpoint

**Card in one line (after the pivot):** during a focus stretch messages become save crystals; at the checkpoint the streamer answers out loud, the words type onto the card, and each viewer gets a threaded reply quoting what the streamer said.

**Evidence status:** competitors and demand below were found by A, G and C for the pre-pivot card. The post-pivot difference was checked by one source (P).

**Competitors**

| Name | What it does | Found by / status | Overlap | Well-known |
| --- | --- | --- | --- | --- |
| [Meld X AMA Question Queue](https://meldstudio.co/gallery/x-ama-question-queue/) | Messages ending in "?" or `!ask` collect in an on-screen queue; the streamer clicks one to feature it | A, G, C / confirmed | Same core loop **before** the pivot (user's ruling); after the pivot: Partial | Yes (Meld) |
| [StreamerQnA](https://obsproject.com/forum/resources/streamerqna.1977/) | Command-submitted questions shown one at a time; bot replies on submission, not on answer | A, G, C / confirmed | Partial | Yes (9,543 downloads) |
| [Social Stream Ninja featured message](https://socialstream.ninja/docs/dock-live-guide.html) | Operator features a message; replying to the viewer is manual | A, G, C / confirmed | Partial | No counts |
| Meld Chat Highlight, Senchabot Featured Message, AskMeLive | Put one message on screen | G / verified or snippet | Adjacent–Partial | Meld |
| Chatterino highlights, Twitch Chat History | Help find or catch up on messages | A, C | Adjacent | Chatterino, Twitch |

**Difference after the pivot (P):** none of Meld, StreamerQnA, Social Stream Ninja or Senchabot listens to the streamer or sends anything back after an answer; a search for a Twitch tool that transcribes the streamer's answer found none. The nearest hits are tools where an AI answers chat by text-to-speech, the opposite direction. Senchabot's after-answer behaviour is unverified.

**Demand (for the problem)**
- A Streamlabs guide describes the manual version: scheduled breaks to read chat, mods keeping a running list of questions ([Streamlabs](https://streamlabs.com/content-hub/post/how-to-maintain-game-concentration-while-streaming), C).
- An art streamer misses greetings while drawing; viewers stop chatting when their messages get no reaction (A, Reddit, unverified); a paid question-queue product launched in October 2026 (G, X, unverified); Twitch built Chat History so newcomers can catch up (C).

**Counter-signals:** some viewers won't wait through a long non-response; a saved message does not mean its author stays (A, unverified). After the pivot, a misheard word could end up in a viewer's quote (P; the card sends a plain receipt when the transcript is weak).

**Audience fit:** heads-down formats: art (#40, about 17 viewers per channel), making, coding, cooking, and focused gameplay. Natural-setting demo: Yes (drawing, building, or a small original game). Type-independent: partly.

**Fact issues:** the pre-pivot context-screenshot timing problem (A) no longer applies; thumbnails were cut. Threaded replies (`reply_parent_message_id`) are documented (A, C, P). Local speech-to-text speed and accuracy on the user's machine are untested (day-1 test T1b).

---

### Card: VAR

**One-liner:** When chat disputes a moment, two `!var` calls start a broadcast-style review: slow-motion replay, a 15-second chat jury, a verdict stamp, and a titled clip.

**Core loop:**
1. The streamer claims something ("IN!").
2. Two distinct viewers type `!var` within 30 s. The threshold scales with active chatters, and mods or the streamer can also call it.
3. A "VAR CHECK" stinger plays. obs-websocket saves the 60 s replay buffer.
4. An OBS Media Source, driven by obs-websocket, plays the last ~10 s shifted by a latency offset, with the last 4 s at half speed.
5. Chat votes `!yes` or `!no` for 15 s; names appear on a jury bench.
6. The verdict stamp lands. Then the app creates a 60 s clip titled "VAR: NO BASKET" and a marker. The clip holds the review, and the review holds the replay of the moment.

**3-minute video:**
- 0:00 Hook: paper ball, "IN!", two `!var`, siren, slow motion off the rim, jury, "NO BASKET" stamp.
- 0:25 The clip link lands; play 5 s of it.
- 0:45 Self-VAR: "I can draw a perfect circle", the streamer calls VAR on themselves, chat overturns it.
- 1:30 How the latency offset lands the replay on the right moment, and the nudge-back hotkey.
- 2:10 Codex artifact, close.

**Codex artifact:** the replay pipeline (buffer save → Media Source → slow motion) and a simulator-driven test of call thresholds and vote timing.

**MVP:**
- **In:** call threshold, replay buffer save, Media Source slow-motion playback, latency offset and nudge-back hotkey, vote, jury bench, stamp, titled clip, marker.
- **Stretch:** verdict history strip ("claims upheld 2/5 today", counters only), a second camera angle.
- **Out:** telestrator, AI judging.

**Build parts:**

| Part | Hours |
| --- | --- |
| Replay save + Media Source playback | 2 |
| Latency offset + hotkey | 1 |
| Call and vote logic | 1 |
| Overlay: stinger, jury bench, stamp | 2.5 |
| Clip + marker | 0.5 |
| Polish | 1.5 |
| **MVP subtotal** | **8.5** |
| Stretch: history strip 0.5, second angle 1 | 1.5 |

**Twitch surfaces, scopes and local parts:** EventSub chat; Create Clip (`clips:edit`), Create Stream Marker (`channel:manage:broadcast`, VOD storage on), Send Chat Message; OBS replay buffer and Media Source via obs-websocket; OBS browser source.

**Demo setup:** 1 streamer + 3 test accounts. A webcam on the action, a mic, desk props. Optionally a small Codex-built game designed to produce close calls (about 1 h, from the buffer) to show the game-stream setting.

**Closest existing things and claimed difference:** chat-called replays: tomaae OBS instant replay (12.6k downloads, last updated 2019), BarRaider OBS Tools `!replay` (can also post a clip), Fyre Instant Replay (StreamElements widget; mentions vote-to-trigger without details); Glitch Studios Instant Replay (mod-triggered branded replay with slow motion); Streamer.bot replay-buffer actions; native polls and Senchabot chat polls; Streamer's Court (a Steam game where chat votes a verdict, no replay). *Difference:* a full review ritual (call, replay, jury, verdict, titled clip) instead of a replay or a poll alone.

**Risks and day-1 tests:**
- Replay buffer and Media Source playback (T2).
- Latency means the replay must land on the right moment (offset + nudge-back).
- The 60 s clip may cut the original moment; the replay inside the review still shows it. Clip title and window (T5).
- An immediate review interrupts play; a streamer asking for replays wanted control over when they run.

### Evidence: VAR

**Card in one line:** chat calls a VAR review on a disputed moment; a slow-motion replay plays, a 15 s chat jury votes, a verdict stamp lands, and a titled clip is made.

**Competitors**

| Name | What it does | Found by / status | Overlap | Well-known |
| --- | --- | --- | --- | --- |
| [tomaae OBS instant replay](https://obsproject.com/forum/resources/picture-in-picture-instant-replay.746/) | Replay buffer as picture-in-picture; viewers can trigger it by chat command | G, C / confirmed | Partial | Yes (12,642 downloads; last update Oct 2019) |
| [Streamer.bot replay buffer actions](https://docs.streamer.bot/api/sub-actions/obs-studio/replay/set-replay-buffer-state) | Save and play replay-buffer footage from any trigger | A, G / confirmed | Partial | Yes (Streamer.bot) |
| [Twitch native polls](https://dev.twitch.tv/docs/api/reference/#create-poll) | Timed chat vote | A, C / confirmed | Partial (jury half) | Yes (Twitch) |
| [Fyre Instant Replay](https://thefyrewire.com/login/instant-replay) | StreamElements widget: `!replay` plays a clip on the overlay; mentions "vote-to-trigger options" without details | A / verified | Partial | No |
| [Glitch Studios Instant Replay](https://overlay.glitchstudios.dev/instant-replay) | Mod-triggered branded replay with countdown and 0.5× slow motion; no voting | A / verified | Partial | No |
| [BarRaider OBS Tools](https://docs.barraider.com/faqs/obs-tools/actions/) | `!replay` instant replay; can create and post a Twitch clip; no voting | C / verified | Partial | Not verified |
| [Senchabot chat poll](https://extensions.senchabot.com/setup/chat-poll) | Mod-started chat poll with on-stream bars | G / verified | Partial (jury half) | No |
| Streamer's Court (Steam, 2022) | Streamer rules on a viewer "crime", chat votes guilty/not guilty; no replay | L / verified | Adjacent | No |
| OK Gamers; Oddshot (defunct) | Speech-started poll; `!shot` replay | G; C (snippet) | Adjacent | No |

Dropped: PROVE IT (unverifiable). Unverified: RTS Action Replay (X post).

**Difference:** replay on command and chat votes both ship, and slow-motion branded replays exist. Not found: call threshold → replay → timed jury → verdict → titled clip as one ritual. A and G: "partly"; C: "yes". A re-search for VAR overlays, `!var` bots and replay-then-vote tools found nothing closer.

**Demand**
- Indirect: 12.6k downloads of a chat-called replay script (historic; last updated 2019) (C, L / verified).
- A streamer asks how to save moments and replay them between rounds (A, Reddit, unverified). Streamers are advised to use the replay buffer (G, X, unverified). Twitch tested a live rewind for viewers (C, snippet).
- Direct requests for a chat jury or VAR review: not found (A, G, C).

**Counter-signals:** the replay request wants control over *when* the replay happens, not an immediate interruption (A, unverified).

**Audience fit:** tied to disputed, visible outcomes: competitive games (the bulk of viewing), sports-like IRL challenges, desk trick shots. Natural-setting demo: Yes with a small original game designed to produce close calls ("did it touch the line?"), or a desk challenge.

**Fact issues**
- Create Clip captures the live output in a window of about 85 s before and 5 s after the call; `duration` 5–60 s; creation is asynchronous (A, G, C, P). The clip must be created while the review is on the live output, and a long review can push the original moment out of the clip.

---

### Card: Hint Jar

**One-liner:** On first (blind) playthroughs, viewers who know the answer seal tiered hints into a jar instead of backseating. The streamer opens only the tier they want, when they want it.

**Core loop:**
1. A viewer types `!hint` and gets a link to a hint page (Twitch login), where they pick a tier (nudge, method, answer) and write the hint.
2. Optionally, a mod approves each hint and corrects its tier on a private dock.
3. The overlay jar fills with envelopes by tier: "Nudge 2 · Method 1 · Answer 1".
4. The streamer says "okay, one nudge" and hits a hotkey. One nudge opens with its author; the answer stays visibly sealed.
5. If solved, "@ana saved the run ⭐". The same nudge from two viewers credits both.

**3-minute video:**
- 0:00 Hook: a backseat line "IT'S THE LEFT DOOR" in chat, the bot answers "seal it instead: !hint", the jar shows "3 hints sealed"; the stuck streamer taps once, a nudge opens, the answer stays sealed.
- 0:25 How viewers submit privately.
- 0:55 The mod reclassifies a "nudge" that is really the answer.
- 1:25 The second tier, solved, credit.
- 2:00 Under the hood, and the puzzle game Codex built for the demo.
- 2:35 Close.

**Codex artifact:** the demo puzzle game itself, plus the tool.

**MVP:**
- **In:** hint page, tiers, mod dock, jar overlay (simple physics or CSS stacking), reveal hotkey, credit, duplicate merging, demo puzzle game.
- **Stretch:** whisper intake (if T4 passes), a chat vote to open a nudge early.
- **Out:** automatic spoiler detection, commercial game integration.

**Build parts:**

| Part | Hours |
| --- | --- |
| Hint page with Twitch login + public URL | 1.5 |
| Mod dock | 1.5 |
| Jar overlay | 1 |
| Reveal logic + hotkey | 1 |
| Credit + merging | 1 |
| Demo puzzle game | 1.5 |
| Polish | 1 |
| **MVP subtotal** | **8.5** |
| Stretch: whisper intake 0.5, chat vote 0.5 | 1 |

**Twitch surfaces, scopes and local parts:** EventSub chat (`user.whisper.message` in stretch), Get Moderators (`moderation:read`), Send Chat Message; OBS browser source and dock; a public URL.

**Demo setup:** 1 streamer + 3 test accounts (one as mod). Webcam and mic. The Codex-built puzzle game.

**Closest existing things and claimed difference:** no-backseating rules and help safe words; LeagueBackseat (queues backseat messages); channel-point backseat rewards and paid backseat windows; Backseat Me (Channel Points Hackathon 2021: points buy temporary control); Universal Hint System (offline tiered hints since 1988); Chat Curtain (shows only mod-approved messages). *Difference:* the help is tiered, gated by the streamer and revealed as a show.

**Risks and day-1 tests:**
- Sealed intake (T4).
- Backseating complaints are common, but many say rules and bans are enough, and some viewers want no hints at all. The jar is where unwanted hints go; the streamer may never open it.
- Twitch's tag is "First Playthrough" ("Blind Playthrough" was removed in 2020); use that wording in the video.
- The demo puzzle must feel like a real playthrough.

### Evidence: Hint Jar

**Card in one line:** viewers drop tiered hints into a sealed jar instead of backseating in chat; the streamer opens one tier at a time on stream, only when stuck.

**Competitors**

| Name | What it does | Found by / status | Overlap | Well-known |
| --- | --- | --- | --- | --- |
| [LeagueBackseat](https://github.com/HerXayah/LeagueBackseat) | Viewers queue timestamped backseat messages for later | A, C / confirmed (G could not find it) | Partial | No (0 stars) |
| [Backseat Me](https://devpost.com/software/backseat-me) (Channel Points Hackathon 2021) | Channel points let a viewer temporarily control or talk to the streamer | A, G / confirmed | Adjacent–Partial | No |
| No-backseat rules, help safe words, `!backseat` | Manual practice: ask before hinting | A, G, C / confirmed | Partial | n/a |
| Channel-point "backseat" rewards | Temporary permission to backseat | A, G / confirmed | Partial | Twitch mechanism |
| evils_presley "backseating costs 5 dollars" | A paid backseat window in stream titles | G / verified | Adjacent | No |
| Universal Hint System (1988) | Offline tiered hints revealed in order | C / verified by search | Adjacent | No counts |
| [Chat Curtain](https://chromeboard.com/extension/chat-curtain-ofdmpokiehfdakmadncelpmnnhmbgabp) | Shows only mod-approved chat messages to extension users | C / verified | Adjacent | No (14 users) |

**Difference:** queued help and streamer permission exist; tiered hints exist offline. Not found: private submission, tiered sealed hints, streamer-controlled reveal one tier at a time. A: "yes, narrowly"; G: "partly"; C: "yes". The link check's search for tiered-hint Twitch tools found none.

**Demand**
- Backseating complaints: a Steam thread says constant backseating pushes people away from a game's streams ([Limbus Company, 2025](https://steamcommunity.com/app/1973530/discussions/0/597397269594002793), L / verified); many "no backseating / no spoilers" stream titles and rules (G, X, unverified); puzzle and blind-run discussions separating nudges from spoilers (A, Reddit, unverified); streamer outbursts at backseaters (C, snippets).
- A streamer guide describes the "gentle nudge when stuck" play style ([StreamHub, 2026](https://streamhub.world/streamer-blog/strategy/1199-how-to-handle-viewer-spoilers-and-backseating-on-stream/), L / verified). Correction: it does **not** say backseating is "one of the most frequent" problems.

**Counter-signals**
- Most replies in the Limbus thread say rules, timeouts and bans fix it (L / verified).
- Some viewers and streamers want no hints at all (A, C); some streamers invite backseating as content (G, X, unverified).

**Audience fit:** blind or first playthroughs of puzzle, adventure, horror and indie games (indie +51% YoY, horror +6%); no share data for blind runs. Natural-setting demo: Yes with an original Codex-built puzzle game (already in the card).

**Fact issues:** Twitch removed the "Blind Playthrough" tag in 2020; "First Playthrough" and "No Spoilers" are the current wording (C, snippet).

---

### Card: Tap on the Shoulder

**One-liner:** Chat can't tap you on the shoulder while you're heads-down. Now it can: viewer reports and mod cues become a face on your desk, and chat confirms the fix.

**Core loop:**
1. **Inputs:**
   - ≥2 distinct viewers mention mic, audio, "far away", black screen or frozen within 60 s, or anyone types `!mic`;
   - a mod taps a preset on a private phone page ("you sound far away", "game too loud", "mic muted", "answer @x");
   - obs-websocket reports the mic input muted, or its level below a silence threshold for N s while live (two separate signals).
2. A phone face on the desk, in the camera shot, turns alarmed and shows the issue in huge letters. A chime plays in the streamer's headphones only. When chat and OBS agree, the face says so ("chat + OBS: mic muted").
3. The streamer fixes it and taps a "fixed" hotkey.
4. The bot posts "Fix #2: sound right now? 👍/👎". Replies that arrive earlier than fix time plus an estimated stream delay are ignored (latency differs per viewer, so the result reads "chat confirmed", not "everyone heard it").
5. The issue resolves on the dock, and the overlay credits the first reporter.
6. When nothing is wrong, the face shows calm chat state (a first-time chatter waves, a question is waiting).

**3-minute video:**
- 0:00 Hook: a muted mic, caption "OBS can see this one…", the face panics, unmute. Then "…but not this one": the mic is turned away, chat says "you sound far away", the face shows FAR AWAY, the streamer fixes it.
- 0:30 The bot asks "sound right now?", two 👍, a credit pops.
- 1:00 A mod cue from a phone: "game too loud".
- 1:30 Calm mode: the face waves at a first-time chatter and raises a hand for a question.
- 2:00 Why it works through a fullscreen game and stream delay.
- 2:30 Codex artifact, close.

**Codex artifact:** the phone face page and the detector's test suite, driven by the chat simulator with noisy chat scripts.

**MVP:**
- **In:** report detector, mod cue page, phone face (QR pairing, Wake Lock, HTTPS), headphone chime, obs-websocket mute/silence check, confirm prompt, credit overlay.
- **Stretch:** calm mode (everyday chat states), a Stream Deck "fixed" button.
- **Out:** lamp, OBS scene control, ML audio analysis.

**Build parts:**

| Part | Hours |
| --- | --- |
| Report detector | 1 |
| Mod cue page with Twitch login | 1.5 |
| Phone face page + pairing over HTTPS | 2.5 |
| obs-websocket mute/silence check | 1 |
| Confirm loop + dock | 1.5 |
| Credit overlay | 0.5 |
| Polish | 1 |
| **MVP subtotal** | **9** |
| Stretch: calm mode 1 | 1 |

**Twitch surfaces, scopes and local parts:** EventSub chat, Get Moderators (`moderation:read`), Send Chat Message; OBS browser source and dock; obs-websocket; a phone web page over a secure WebSocket (public URL or local certificate; Wake Lock needs HTTPS).

**Demo setup:** 1 streamer + 3 test accounts (one as mod). A spare phone in the camera shot, a webcam and a mic. For the fullscreen-game case, a small Codex-built game (about 1 h, from the buffer).

**Closest existing things and claimed difference:** OBS plugins that warn the streamer privately: Muted Notification (12.4k downloads; talking into a muted mic), Remember to Talk (2.4k downloads; mic silent too long), Audio Source Mute Indicator; Twitch Guardian (keyword-alert Chrome extension); Elgato Prompter chat mode and Mochi chat pet; WooferBot and Streamer.bot lights on Twitch events; a friend relaying chat. The well-known plugins cover only the "your mic is muted or silent" input. *Difference:* it routes human judgment (viewer reports, mod cues) to a signal in the room that survives a fullscreen game, cross-checks OBS, then closes the loop with the audience's confirmation.

**Risks and day-1 tests:**
- Real problems may be too rare to keep it installed; calm mode answers this.
- Reports may reflect one viewer's device, so the UI says "2 listeners report…", not "your mic is broken".
- obs-websocket mute and silence events (T2).
- Some streamers monitor their own mic, and viewers sometimes do tell them in chat. The hook's second case ("you sound far away") is one no OBS plugin can detect.

### Evidence: Tap on the Shoulder

**Card in one line:** viewers and mods report production problems (muted mic, black screen, "you're too far away"); the report is checked against OBS, reaches the streamer in the room, and chat confirms the fix.

**Competitors**

| Name | What it does | Found by / status | Overlap | Well-known |
| --- | --- | --- | --- | --- |
| [Muted Notification](https://obsproject.com/forum/resources/muted-notification.1706/) | OBS filter: sound or red mark when you talk into a muted source | G / verified | Partial | Yes (12,466 downloads) |
| [Remember to Talk](https://obsproject.com/forum/resources/remember-to-talk.2484/) | Private alert when the mic has been silent too long | C / verified | Partial | Yes (2,448 downloads) |
| [Audio Source Mute Indicator](https://obsproject.com/forum/resources/audio-waves-visualizer.2247/) | Tone and overlay on mute/unmute | C / verified | Partial | No |
| [Twitch Guardian](https://chromewebstore.google.com/detail/twitch-guardian/fcfdekecgocobpjhldifpplcifkfflme) | Desktop alert when chat keywords appear | A, G, C / confirmed | Partial | No (about 40–60 users) |
| [Elgato Prompter Chat Mode](https://help.elgato.com/hc/en-us/articles/20461145372813-Elgato-Prompter-Chat-Mode) | Chat shown behind the camera lens | A, G, C / confirmed | Adjacent–Partial | Yes (Elgato) |
| [WooferBot](https://wooferbot.com/), [Mochi the Cat](https://marketplace.elgato.com/product/mochi-the-cat-6ac71734-f507-4887-8350-10357f6e6ea0) | Mascots that react to stream events; WooferBot drives smart lights | A, G, C / confirmed | Adjacent–Partial | Mochi via Elgato |
| StreamNotch (Mac app), ViperVex mic widget | Own-mic warnings | G / verified; ViperVex unverified | Adjacent | No |

**Difference:** each part exists alone (OBS mute/silence alerts, chat keyword alerts, reactive mascots). Not found: viewer reports and mod cues cross-checked against OBS, delivered as one in-room signal, closed by a chat confirmation. A: "yes, narrowly"; G: "partly"; C: "yes, parts exist". The well-known plugins cover only the streamer-private "your mic is muted/silent" input.

**Demand**
- Snoop Dogg streamed with no audio for over an hour; chat was emote-only and could not tell him ([Kotaku, 2021](https://kotaku.com/twitch-spammers-just-wanted-to-save-snoop-dogg-from-str-1847293788), C / verified).
- OBS forum request for a streamer-only mute icon, "streamers often forget they've muted" ([2018](https://obsproject.com/forum/threads/mic-mute-notifier-icon-main-screen.80363), C / verified).
- A new streamer talked for two hours on a muted mic, through a raid (G, Reddit, unverified); raided streams left on a black screen (G, X, unverified); viewers reporting audio and confirming fixes (A, Reddit, unverified); an art streamer and a moderator asking how to get the streamer's attention (A, Reddit, unverified).

**Counter-signals**
- "Monitor your own mic in OBS instead of waiting for chat" (G, Reddit, unverified); the OBS-only plugins above show some streamers solve the mute case privately (C).
- DrDisrespect muted himself for about 10 minutes and viewers did tell him ([mein-mmo](https://mein-mmo.de/en/drdisrespect-experiences-an-outburst-in-cod-warzone-accidentally-mutes-himself,611302/), L / verified).
- Viewers' audio reports can conflict (A, Reddit, unverified).

**Audience fit:** any broadcast with a mic: all three say type-independent. Most useful when the streamer is heads-down or in a fullscreen game. Natural-setting demo: Yes with a small original fullscreen game; the desk failure cases (muted, black scene, far away) need no game.

**Fact issues**
- OBS reports mute state and volume levels; "muted" and "unexpectedly silent" are different signals and need thresholds (A).
- Viewer latency is per player, so "everyone has seen the fix" cannot be guaranteed; "chat confirmed" can (A).

---

### Card: Studio Audience

**One-liner:** Chat becomes a live theater crowd you can hear. Every laugh belongs to a real, named viewer, and it only gets louder when more people react.

**Core loop:**
1. Emotes and keywords map to five reactions: laugh, gasp, aww, applause, boo.
2. A crowd engine mixes CC0 samples. Intensity scales with *distinct* reacting viewers, so spam can't inflate it, and the crowd never sounds bigger than the number of real reactors.
3. Each viewer has a signature laugh: a sample from a pool, a playback rate and an EQ, all derived from their user ID (changeable with `!mylaugh 7`). It rises out of the crowd, and their named seat silhouette bounces.
4. The same word from 2+ viewers within 10 s becomes a chant with the word on screen.
5. A follow brings applause; a raid opens the doors and adds seats.
6. A headphone-only mode lets the streamer hear the room without putting it on stream.

**3-minute video:**
- 0:00 Hook: a missed paper-ball shot, "L" and "LUL", the crowd boos then laughs, three named seats bounce.
- 0:20 Signature laughs, so you hear who is laughing.
- 0:50 A chant forms, the word on screen.
- 1:15 A raid opens the doors.
- 1:40 Headphone mode shown as a picture-in-picture "what the streamer hears", with a waveform.
- 2:05 How mixing and scaling work; every voice traceable.
- 2:30 Codex artifact, close.

**Codex artifact:** the Web Audio crowd mixer, tuned with the chat simulator sending bursts of different sizes.

**MVP:**
- **In:** 5 reactions, 20+ CC0 samples, distinct-viewer scaling, signature laughs, seat strip, chants, follow and raid events, monitor-only toggle, volume cap.
- **Stretch:** lurker seats (silent logged-in chatters in dim seats, bots filtered; a seat lights on first reaction).
- **Out:** TTS chants, viewer-recorded audio.

**Build parts:**

| Part | Hours |
| --- | --- |
| Chat mapping | 1 |
| Web Audio crowd mixer + scaling | 2.5 |
| Signature laughs (sample × rate × EQ per ID) | 1 |
| Seat strip overlay | 2 |
| Chants | 0.5 |
| Follow and raid events | 0.5 |
| Monitor mode + picture-in-picture view | 0.5 |
| Polish | 1 |
| **MVP subtotal** | **9** |
| Stretch: lurker seats 1 | 1 |

**Twitch surfaces, scopes and local parts:** EventSub chat, `channel.follow` (`moderator:read:followers`), `channel.raid`; Get Chatters (`moderator:read:chatters`, stretch); OBS browser source with audio.

**Demo setup:** 1 streamer + 3 test accounts. Headphones, mic, webcam. Three accounts make at most three voices; a larger crowd can only be shown with the chat simulator, labeled as a simulation in the video.

**Closest existing things and claimed difference:** Sound Alerts and Blerp (viewer-triggered sounds, one clip per trigger); per-viewer entrance sounds (Streamer.bot Walkon Sounds, Blerp walk-ons); Meld Emote Storm and StreamElements' KappaGen (visual scaling with chat); hand-fired laugh tracks (Elgato sound packs, emote soundboards). Per-viewer sounds already tie a noise to a viewer. *Difference:* one mixed crowd you hear, scaled by the number of distinct reactors, with recurring voices tied to named viewers and chants.

**Risks and day-1 tests:**
- The delight may fade after 10 minutes.
- It may read as "canned laughter / fake engagement"; traceability is the answer and leads the pitch.
- Get Chatters for the stretch (T5).
- Sound spam is a known complaint about sound alerts; distinct-viewer scaling and the volume cap are the answer.

### Evidence: Studio Audience

**Card in one line:** chat reactions become a live studio-audience soundtrack: laughs, gasps and chants mixed from real, named viewers, never louder than the number of people actually reacting.

**Competitors**

| Name | What it does | Found by / status | Overlap | Well-known |
| --- | --- | --- | --- | --- |
| [Sound Alerts](https://soundalerts.com/) | Viewers trigger sounds with Bits or channel points | A, G, C / confirmed | Partial–Adjacent | Yes |
| [Meld Emote Storm](https://meldstudio.co/gallery/emote-storm/) | Emote storm that grows with chat activity; visual | A, G, C / confirmed | Partial | Yes (Meld) |
| [StreamElements KappaGen](https://docs.streamelements.com/chatbot/commands/default/kappagen) | Emote explosions on screen | A, G, C / confirmed | Partial–Adjacent | Yes (StreamElements) |
| [Streamer.bot Walkon Sounds](https://extensions.streamer.bot/t/walkon-sounds-aka-sub-sounds/77) | A personal entrance sound when a viewer first chats | A, G / confirmed | Partial | Yes (Streamer.bot) |
| [Blerp](https://blerp.com/streaming) walk-ons and soundboard | Viewer soundboard plus per-subscriber walk-on sounds | G / unverified (site blocked) | Partial | Likely |
| VoxBooster emote-laugh soundboard guide; Elgato "Popular Sounds" (sitcom laugh tracks); Crowd Sounds app | Laugh and crowd sounds fired by hand | C / verified | Adjacent | Elgato |
| Plus 2 (1 user), Chat Decoder hype meter | Visual chat-excitement gauges | C / verified | Adjacent | No |

Dropped: Twitch Sense (unverifiable).

**Difference:** chat-scaled visuals, viewer-triggered sounds and per-viewer entrance sounds all exist; G notes per-viewer sounds already cover "this noise belongs to that viewer". Not found: one mixed crowd whose loudness follows the number of distinct reactors, with recurring voices tied to named viewers and chants. A and G: "partly"; C: "yes". A re-search found nothing closer.

**Demand**
- Sound features are in wide, current use: streamers redoing sound alerts, chat-controlled alerts, custom alert commissions (G, X, unverified); a streamer added Sound Alerts after viewers asked (A, Reddit, unverified); requests for personal entrance sounds (A, Reddit, unverified).
- Streamers build emote-to-laugh soundboards by hand ([VoxBooster](https://voxbooster.com/blog/soundboard-meme-audios-twitch-chat-emotes/), L / verified).
- Streaming to a silent or lurking chat is demoralising ([Dexerto, 2018](https://www.dexerto.com/entertainment/emotional-streamer-rage-quits-his-broadcast-because-no-one-was-putting-anything-in-the-chat-141564/), L / verified).

**Counter-signals**
- Sound spam: a streamer asks to block one viewer who over-uses Sound Alerts ([feedback board, 2022, 7 votes](https://feedback.soundalerts.com/p/restrict-a-specific-user-from-using-sound-alerts), L / verified); "firing KEKW audio every time the emote appears turns a comedic tool into repetitive noise" (VoxBooster, verified); viewers list excessive sound effects among things they dislike (A, Reddit, unverified).
- G's X search for sound alerts described as annoying returned 0 posts.
- With 0–3 chatters the crowd stays tiny (C, inference).

**Audience fit:** talk, comedy and variety streams first (Just Chatting 14.2%, IRL 1.8%); usable on game streams with an active chat if the audio doesn't clash. Mostly type-independent. Natural-setting demo: A and G yes; C partly: three test accounts make at most three voices, so the scaling cannot be shown with real viewers.

**Fact issues:** none. Samples must be CC0 or self-recorded (no commercial audio).

---

Now write your scores in the output format above.
