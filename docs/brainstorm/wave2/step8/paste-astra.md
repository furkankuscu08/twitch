# Free review: 4 Twitch hackathon project ideas

You are an independent reviewer. We are a solo entrant in a hackathon and have narrowed our ideas to four. We want your honest, free-form opinion before we choose one and start building.

## What to read

Everything you need is in this message: the task, the builder, the four ideas with their evidence, and, at the end, the three official competition documents copied verbatim (rules, overview, FAQ/resources). The judging criteria are in those documents.

You may search the web (for example, for existing products or technical constraints). When a claim in your review comes from a search, give the link. Do not ask follow-up questions; if something is unclear, state your assumption and continue.

## What we want

Free format. No scoring table is required. For each idea, tell us what you think is good and what is bad about it, and what you would add, remove or change, and why. Then say which one you would build and why.

You may also propose a combination of these ideas or a different idea, in a short separate section.

The order of the ideas below is arbitrary.

**Write your review in Turkish** (technical terms and product names may stay in English), directly in your reply.

## The builder

- Solo. An ML engineer, strong in Python, FastAPI and Docker. New to Twitch, with no audience.
- Turkish; speaks English with an accent. The video will be in English.
- Machine: Windows 11 with WSL2 (the repo lives in WSL), RTX 4070 Laptop GPU with 8 GB, Ryzen 7 8845HS, 32 GB RAM. Mic capture from inside WSL2 is unreliable, so any speech-to-text would run as a native Windows Python process; OBS runs on Windows.
- Devices and people: one phone of their own, 2–3 more through friends; 1–2 friends can join the recording.
- Time: about 20–25 hours in total until the deadline, including recording and editing the video. The build budget is about 17.5 hours: a shared base (3.5 h) + the idea's MVP (up to 12 h) + at least 2 h of buffer. Video recording and editing come on top.
- Dates: today is 28 October 2026. Day-1 tests are planned for 29 October, the build for 30 October – 1 November, the video for 1–2 November. Deadline: 2 November 2026, 14:00 PT.

## Shared build facts (apply to every idea)

**Constraints**
- One streamer plus three test accounts (plus 1–2 friends). No real audience.
- No commercial games or commercial music in the video. Where an idea's natural setting is a game, the demo can use a small original game built with Codex (about 1 h, paid from the buffer) or an MIT-licensed open-source game.
- No Twitch content kept beyond 24 h.

**Shared base (built first for any idea, 3.5 h):** Twitch app with OAuth for broadcaster and bot and token refresh; EventSub WebSocket chat and Send Chat Message; a local FastAPI server pushing to OBS browser sources and an OBS dock; obs-websocket connection; and a Codex-built chat simulator in which the three test accounts post scripted chat over the real API (used for rehearsal, tests and recording).

**How Codex is used:** the whole project is built with Codex in one main thread. The chat simulator is the shared Codex-built part; each idea names one more concrete Codex artifact.

**Twitch facts**
- Create Clip takes `title` and `duration` (5–60 s). It captures the live output from roughly 85 s before to 5 s after the call and is asynchronous. Which part of that window `duration` keeps is not documented.
- Create Stream Marker needs VOD storage enabled.
- Send Chat Message supports threaded replies (`reply_parent_message_id`, 500-character limit; a dropped message returns `drop_reason`). A bot that is a moderator can send 100 messages per 30 s instead of 20.
- Threaded replies are ordinary public chat messages, visible to everyone in chat.
- The Wake Lock API (keeping a phone screen on) needs HTTPS.

**Day-1 tests (planned before building; a failed test means the fallback in the idea's risks)**

| Test | What it checks | Ideas | Pass condition |
| --- | --- | --- | --- |
| T1 | Real-time local speech-to-text keyword spotting during a live stream, with the builder's own voice | Minefield | ≥80% hits, ≤1 false alarm per 10 min, ≤3 s lag, no dropped frames |
| T1b | Local speech-to-text of spoken answers | Checkpoint | Quote ready ≤2 s after the streamer stops; ≥9 of 10 readable without edits |
| T2 | obs-websocket: replay buffer + Media Source slow motion; mute/silence events; source screenshots | VAR, Tap on the Shoulder | Replay on screen ≤5 s; mute event arrives |
| T4 | A Twitch-login page behind a public URL; for Tap, a phone page over HTTPS with Wake Lock | Minefield, Tap on the Shoulder | One path works end to end |
| T5 | API checks: Create Clip with title, Stream Marker, threaded reply | All | All succeed on a new channel |

## How to read the evidence

Three independent researchers searched the web for each card: **A**, **G** and **C**. A separate link check (**L**) opened pages that only one researcher had found. For Checkpoint, whose design changed after the research, the changed part was checked by one more source (**P**).

- **Confirmed**: found by two or more researchers.
- **Verified**: found by one researcher, and the link check opened the page.
- **Unverified**: the page could not be opened (blocked site, Reddit, X, or a search snippet only). It may exist; treat it as weaker evidence.
- **Overlap**: `Same core loop` (same who acts, same trigger, same output on stream), `Partial`, or `Adjacent`.
- **Well-known**: a major streaming platform or tool (Twitch, StreamElements, Streamlabs, Streamer.bot, Elgato, OBS, Meld, Sound Alerts, StreamUP), ≥1,000 users or installs, ≥100 GitHub stars, or a post with ≥10,000 views.
- Stream-type shares come from a research snapshot: Just Chatting 14.2% of viewing, IRL 1.8%, games make up most of the top 15 categories, indie games +51% YoY, horror +6%.

## The 4 ideas and their evidence

Each idea is followed by the evidence our research found, then by the additions we are considering for the 12 h MVP. The card text describes the original MVP (up to 9.5 h); the additions are separate so you can judge them on their own.

### Idea: Checkpoint

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

**Closest existing things and claimed difference:** Meld X AMA Question Queue (same core loop up to the featured question; well-known), StreamerQnA, Social Stream Ninja featured message, Senchabot featured message, Chatterino highlights. *Difference:* the streamer answers by voice without lifting a hand, and each viewer receives the streamer's actual words as a threaded reply.

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

**Proposed additions for the 12 h MVP (+3 h on top of the 9 h above):**

| Addition | Hours | What it does |
| --- | --- | --- |
| FAQ | 1.5 | Every answered card is stored (question, final transcript, confidence, time, clip link). When a new chat message looks like a question, it is compared with the questions already answered in this stream (small embedding model such as `all-MiniLM-L6-v2`, cosine threshold starting at 0.85). On a match with a confident earlier answer, the bot replies in the viewer's thread: "📌 Answered earlier (12:04): 'It's a Micron 05, it doesn't bleed' ▶ clip · type !ask to ask anyway". During focus the message does not become a crystal; the dock counts it as auto-answered. Same stream only. |
| Clip link in the receipt | 1 | The former stretch item: the receipt carries a link to a clip of the answer. |
| Undo window | 0.5 | The 3 s before the receipt is sent becomes a visible countdown on the dock; "undo" turns it into the plain receipt without the quote. |

---

### Idea: Minefield

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
| [Don't Get Got](https://draughtslondon.com/ultimate-guide-to-the-dont-get-got-game/) (Big Potato party game) | Players hold secret missions, one of which is "get a player to say the word 'banana'"; played face to face, no Twitch | Extra search, 28 Oct / verified | Adjacent (same "make someone say it" goal, different medium) | Retail party game; no counts checked |
| [Heads Up! Phones Down (Twitch extension)](https://support.aspyr.com/hc/en-us/articles/22586269678093-Heads-Up-Phones-Down-Edition-Twitch-Extension-Overview) | The game picks a word hidden from the streamer; viewers type hints in chat; no listening to the streamer | Extra search, 28 Oct / verified | Adjacent | Aspyr product; no counts checked |
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

**Proposed additions for the 12 h MVP (+2.5 h on top of the 9.5 h above):**

| Addition | Hours | What it does |
| --- | --- | --- |
| Fuse | 1 | If the match confidence is high, the mine explodes at once. If it is medium, a burning fuse and a 3 s ticking sound appear first; a mod or the streamer can cut it ("false alarm"). The threshold is tuned with the accuracy harness. |
| Sweep | 1 | The streamer has 3 sweeps per stream. Suspecting a trap, the streamer types the suspected word into the dock (saying it would set it off). If it matches a live mine, the mine is "SWEPT" and the planter's chip goes dark; if not, the sweep is lost. |
| Bomb Squad table | 0.5 | Kept across streams (SQLite): most explosions caused, longest-surviving mine, the streamer's sweep accuracy; shown with the dud reveal. |

---

### Idea: VAR

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

**Proposed additions for the 12 h MVP (+3.5 h on top of the 8.5 h above):**

| Addition | Hours | What it does |
| --- | --- | --- |
| VAR pending | 1 | When the call threshold is met, the replay buffer is saved at once, but the review does not start. A corner badge shows "🟨 VAR PENDING (2 calls)"; the streamer presses "review now" when ready. An "auto" mode keeps the original behaviour. Warning after 2 min, call dropped after 5 min. |
| Telestrator | 1.5 | At the end of the slow motion the frame freezes; a mod or the streamer draws a line or circle in the dock, and the drawing appears on stream over the frozen frame. The verdict stamp lands on it. |
| Referee reputation | 1 | Callers whose call overturns the claim and jurors who vote with the verdict earn points, kept across streams (SQLite). "Referee of the night" at the end of the stream. |

---

### Idea: Tap on the Shoulder

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

**Proposed additions for the 12 h MVP (+3 h on top of the 9 h above):**

| Addition | Hours | What it does |
| --- | --- | --- |
| Calm mode | 1 | The former stretch item moves into the MVP: when nothing is wrong, the face waves at first-time chatters, raises a hand for a waiting question, dozes when chat is quiet. |
| Soundcheck | 1 | At the start of a stream the streamer presses "soundcheck"; the face shows "SOUNDCHECK A", the streamer talks, the bot asks chat "Test A: mic vs game? !heard good / quiet / loud", and mic and game levels are measured from `InputVolumeMeters`. The face shows both: "chat: quiet · meter: −28 dB → raise mic". |
| Black or frozen screen | 0.5 | `GetSourceScreenshot` takes a small frame once a second; very low brightness → "BLACK SCREEN", no change for 10 s → "FROZEN?". Only on game or camera scenes. Shown as "chat + OBS" when chat reports the same. |
| End-of-stream issue report | 0.5 | "3 issues · avg fix 42 s · first reporter: @ana" on the dock and in chat. |

---

# Appendix: official competition documents (verbatim)

## Official rules (`rules.md`)

````text
Codex x TwitchCon Hackathon

Deadline: Nov 2, 2026 @ 5:00pm EST

Join hackathon
Codex x TwitchCon Hackathon (the "Hackathon") Official Rules

NO PURCHASE OR PAYMENT NECESSARY TO ENTER OR WIN. A PURCHASE OR PAYMENT WILL NOT INCREASE YOUR CHANCES OF WINNING.

SUBMISSION OF ANY ENTRY CONSTITUTES AGREEMENT TO THESE OFFICIAL RULES AS A CONTRACT BETWEEN ENTRANT (AND EACH INDIVIDUAL MEMBER OF ENTRANT), THE HACKATHON SPONSOR, AND DEVPOST.
1\. Dates and Timing

Submission Period: October 23, 2026 (10:00 am Pacific Time) – November 2, 2026 (2:00 pm Pacific Time) ("Submission Period").

Judging Period: November 5, 2026 (9:00 am Pacific Time) – November 15, 2026 (5:00 pm Pacific Time) ("Judging Period" and together with the Submission Period, the “Hackathon Period”).

Winners Announced: On or around November 15, 2026 at TwitchCon San Diego 2026 (“TwitchCon”).
2\. Sponsor and Administrator

Sponsor: Amazon Advertising LLC, 410 Terry Avenue North, Seattle, WA 98109

Administrator: Devpost, Inc. ("Devpost"), 250 Broadway, Floor 24, New York, NY 10007
3\. Eligibility

The Hackathon IS open to:

Individuals who are at least eighteen (18) years old or the age of majority where they reside as of the time of entry, whichever is older ("Eligible Individuals"); and
Teams of Eligible Individuals ("Teams").

(the above are collectively, "Entrants")

An Eligible Individual may join more than one Team and an Eligible Individual who is part of a Team may also enter the Hackathon on an individual basis. If a Team is entering the Hackathon, they must appoint and authorize one individual (the "Representative") to represent, act, and enter a Submission, on their behalf. By entering a Submission on behalf of a Team you represent and warrant that you are the Representative authorized to act on behalf of your Team.

The Hackathon IS NOT open to:

Organizations, including corporations, not-for-profit corporations and other nonprofit organizations, limited liability companies, partnerships, and other legal entities
Individuals who are residents of a country, state, province or territory where the laws of the United States or local law prohibits participating or receiving a prize in the Hackathon (including, but not limited to, Brazil, Quebec, Russia, Crimea, Cuba, Iran, and North Korea and any other country which is comprehensively sanctioned by the U.S. Treasury’s Office of Foreign Assets Control, and any applicable denied-party lists) as of the time of entry and at time of Prize payment)
Organizations involved with the design, production, paid promotion, execution, or distribution of the Hackathon, including the Sponsor, OpenAI and Administrator ("Promotion Entities")
Employees, representatives and agents\\ of such Promotion Entities, and all members of their immediate family or household\
Any other individual involved with the design, production, promotion, execution, or distribution of the Hackathon, and each member of their immediate family or household\
Any Judge (defined below), or company or individual that employs a Judge
Any parent company, subsidiary, or other affiliate\\\ of any organization described above
Any other individual or organization whose participation in the Hackathon would create, in the sole discretion of the Sponsor and/or Administrator, a real or apparent conflict of interest

\The members of an individual's immediate family include the individual's spouse, children and stepchildren, parents and stepparents, and siblings and stepsiblings. The members of an individual's household include any other person that shares the same residence as the individual for at least three (3) months out of the year.

\\Agents include individuals or organizations that in creating a Submission to the Hackathon, are acting on behalf of, and at the direction of, a Promotion Entity through a contractual or similar relationship.

\\\*An affiliate is: (a) an organization that is under common control, sharing a common majority or controlling owner, or common management; or (b) an organization that has a substantial ownership in, or is substantially owned by the other organization.
4\. How To Enter

Entrants may enter by visiting twitchcon-codex.devpost.com ("Hackathon Website") and following the below steps:

Register for the Hackathon on the Hackathon Website by clicking the "Join Hackathon" button. To complete registration, sign up to create a free Devpost account, or log in with an existing Devpost account. This will enable you to receive important updates and to create your Submission.
Entrants will obtain access to the required developer tools and complete a Project described below in Project Requirements. Use of the developer tools will be subject to the license agreement related thereto. Entry in the Hackathon constitutes consent for the Sponsor and Devpost to collect and maintain an entrant's personal information for the purpose of operating and publicizing the Hackathon.
Complete and enter all of the required fields on the "Enter a Submission" page of the Hackathon Website (each a "Submission") during the Submission Period and follow the requirements below.

Project Requirements

What to Create: Entrants must build for streamers and their community on www.twitch.tv (“Twitch”) with OpenAI Codex (each a "Project"). The Project must be an interactive experience that connects to Twitch, for example through chat, a stream overlay, the Twitch API, EventSub or an Extension.
Functionality: The Project must be capable of being successfully installed and running consistently on the platform for which it is intended and must function as depicted in the video and/or expressed in the text description.
Platforms: A submitted Project must run on the platform for which it is intended and which is specified in the Submission Requirements.
New: Projects must be newly created during the Submission Period. Participants may use standard development tools, including frameworks, libraries, starter templates, and AI coding assistants. The work described and submitted must have been built during the Submission Period.
Third Party Integrations: If a Project integrates any third-party SDK, APIs and/or data, Entrant must be authorized to use them in accordance with any terms and conditions or licensing requirements of the tool.

Submission Requirements

Submissions to the Hackathon must meet the following requirements:

Include a Project built with the required developer tools and meets the above Project Requirements.
Provide a URL to your code repository for judging and testing on GitHub, GitLab or Bitbucket. It must contain all source code, assets, and instructions needed for the project to run. The repository may be public or private. If private, it must be on GitHub or GitLab and shared with testing@devpost.com.
Include a text description that explains the Project's features and functionality and how you used Codex.
Provide the Codex session ID for the Codex thread where the Project was built.
Include a demonstration video of your Project. The video portion of the Submission:
  - should be less than three (3) minutes. Judges are not required to watch beyond three minutes
  - should include footage that shows the Project functioning on Twitch
  - Should include footage that shows how the project was built with Codex
  - must be uploaded to and made publicly visible on YouTube and a link to the video must be provided on the submission form on the Hackathon Website; and
  - must not include third party trademarks, or copyrighted music or other material unless the Entrant has permission to use such material.

Multiple Submissions

An Entrant may submit more than one Submission, however, each Submission must be unique and substantially different from each of the Entrant's other Submissions, as determined by the Sponsor and Devpost in their sole discretion.

Submission ownership

Be the original work of the Entrant, be solely owned by the Entrant, and not violate the IP rights of any other person or entity.

Testing

Access must be provided to an Entrant's working Project for judging and testing by providing a link to an accessible code repository as stated above in the Submission Requirements. The Entrant must make the Project available free of charge and without any restriction, for testing, evaluation and use by the Sponsor, Administrator and Judges until the Judging Period ends. Judges are not required to test the Project and may choose to judge based solely on the text description, images, and video provided in the Submission.

Language Requirements

All Submission materials must be in English or, if not in English, the Entrant must provide an English translation of the demonstration video, text description, and testing instructions as well as all other materials submitted.

Team Representation

If a team is entering the Hackathon, they must appoint and authorize one individual (the "Representative") to represent, act, and enter a Submission, on their behalf. The Representative must meet the eligibility requirements above. By entering a Submission on the Hackathon Website on behalf of a team you represent and warrant that you are the Representative authorized to act on behalf of your team.

Intellectual Property

Your Submission must: (a) be your (or your Team's) original work product; (b) be solely owned by you or your Team with no other person or entity having any right or interest in it; and (c) not violate the intellectual property rights or other rights including but not limited to copyright, trademark, patent, contract, and/or privacy rights, of any other person or entity. An Entrant may contract with a third party for technical assistance to create the Submission provided the Submission components are solely the Entrant's work product and the result of the Entrant's ideas and creativity, and the Entrant owns all rights to them. An Entrant may submit a Submission that includes the use of open source software or hardware, provided the Entrant complies with applicable open source licenses and, as part of the Submission, creates software that enhances and builds upon the features and functionality included in the underlying open source product. By entering the Hackathon, you represent, warrant, and agree that your Submission meets these requirements.

Financial or Preferential Support

A Project must not have been developed, or derived from a Project developed, with financial or preferential support from the Sponsor or Administrator. Such Projects include, but are not limited to, those that received funding or investment for their development, were developed under contract, or received a commercial license, from the Sponsor or Administrator any time prior to the end of the Submission Period. The Sponsor, at their sole discretion, may disqualify a Project, if awarding a prize to the Project would create a real or apparent conflict of interest.
5\. Submission Modifications

Draft Submissions

Prior to the end of the Submission Period, you may save draft versions of your submission on Devpost to your portfolio before submitting the Submission materials to the Hackathon for evaluation. Once the Submission Period has ended, you may not make any changes or alterations to your Submission, but you may continue to update the Project in your Devpost portfolio.

Modifications After the Submission Period

The Sponsor and Devpost may permit you to modify part of your Submission after the Submission Period for the purpose of adding, removing or replacing material that potentially infringes a third party mark or right, discloses personally identifiable information, or is otherwise inappropriate. The modified Submission must remain substantively the same as the original Submission with the only modification being what the Sponsor and Devpost permits.
6\. Judges & Criteria

Sponsor and Administrator reserve the sole right to determine the eligibility and judging methodologies for all submissions. This process may utilize expert panels, peer review, automated AI-driven analysis, or any combination thereof to ensure efficient, fair, and objective evaluation. Eligible submissions will be evaluated by a panel of judges selected by the Sponsor (the "Judges"). Judges may be employees of the Sponsor or third parties, may or may not be listed individually on the Hackathon Website, and may change before or during the Judging Period. Judging may take place in one or more rounds with one or more panels of Judges, at the discretion of the Sponsor.

Stage One: The first stage will determine via pass/fail whether the ideas meet a baseline level of viability, in that the Project reasonably fits the theme and reasonably applies the required developer tools featured in the Hackathon.

Stage Two: All Submissions that pass Stage One will be evaluated in Stage Two based on the following equally weighted criteria (the "Judging Criteria"). The five highest scoring Submissions will become finalists.

Innovation/Idea: How creative and novel is the concept and does the project differ from existing concepts?
Potential Impact: How useful or entertaining is it for streamers and their communities?
Technological implementation: How well is it built, and how well does it use Codex?
Design: Is it easy to use and fun to watch?

The scores from the Judges will determine the potential winners of the applicable prizes. The Entrant(s) that are eligible for a Prize, and whose Submissions earn the highest overall scores based on the applicable Judging Criteria, will become potential winners of that Prize.

Tie Breaking

For each Prize listed below, if two or more Submissions are tied, the tied Submission with the highest score in the first applicable criterion listed above will be considered the higher scoring Submission. In the event any ties remain, this process will be repeated, as needed, by comparing the tied Submissions' scores on the next applicable criterion. If two or more Submissions are tied on all applicable criteria, the panel of Judges will vote on the tied Submissions.
7\. Intellectual Property Rights

All Submissions remain the intellectual property of the individuals that developed them. By submitting an entry, entrants agree that the Sponsor will have a non-exclusive license to use such entry for judging the entry. Entrants agree that the Sponsor and Devpost shall have the right to promote the Submission and use the name, likeness, voice and image of all individuals contributing to a Submission, in any materials promoting or publicizing the Hackathon and its results, during the Hackathon Period and for three years thereafter. Some Submission components may be displayed to the public. Other Submission materials may be viewed by the Sponsor, Devpost, and judges for screening and evaluation. By submitting an entry or accepting any prize, entrants represent and warrant that (a) submitted content is not copyrighted, protected by trade secret or otherwise subject to third party intellectual property rights or other proprietary rights, including privacy and publicity rights, unless entrant is the owner of such rights or has permission from their rightful owner to post the content; and (b) the content submitted does not contain any viruses, Trojan horses, worms, spyware or other disabling devices or harmful or malicious code.
8\. Prizes

|     |     |
| --- | --- |
| Prize | Award |
| 1st Place | $10,000 USD and stage time at TwitchCon |
| 2nd Place | $6,000 USD and  stage time at TwitchCon |
| 3rd Place | $4,000 USD and stage time at TwitchCon |
| Runner Ups (2) | $2,500 USD each and stage time at TwitchCon |

Substitutions & Changes: Prizes are non-transferable by the winner. Sponsor in its sole discretion has the right to make a prize substitution of equivalent or greater value. Sponsor will not award a prize if there are no eligible Submissions entered in the Hackathon, or if there are no eligible Entrants or Submissions for a specific prize.

Verification Requirement: THE AWARD OF A PRIZE TO A POTENTIAL WINNER IS SUBJECT TO VERIFICATION OF THE IDENTITY, QUALIFICATIONS AND ROLE OF THE POTENTIAL WINNER IN THE CREATION OF THE SUBMISSION. No Submission or Entrant shall be deemed a winning Submission or winner until their post-competition prize affidavits have been completed and verified, even if prospective winners have been announced verbally or on the competition website. The final decision to designate a winner shall be made by the Sponsor and/or Administrator.

Prize Delivery: Prizes will be payable to the Entrant, if an individual, or to the Entrant's Representative, if a Team. It will be the responsibility of the winning Entrant's Representative to allocate the Prize among their Team's participating members, as the Representative deems appropriate. Travel, lodging, and related expenses to attend TwitchCon are the responsibility of the winners. Declining or failing to appear in-person at TwitchCon will not cause a winner to forfeit the monetary portion of the Prize. A monetary Prize will be mailed to the winning Entrant's address (if an individual) or the Representative's address (if a Team), or sent electronically to the Entrant or Entrant's Representative's bank account, only after receipt of the completed winner affidavit and other required forms (collectively the "Required Forms"), if applicable. The deadline for returning the Required Forms to the Administrator is ten (10) business days after the Required Forms are sent. Failure to provide correct information on the Required Forms, or other correct information required for the delivery of a Prize, may result in delayed Prize delivery, disqualification of the Entrant, or forfeiture of a Prize. Prizes will be delivered within 60 days of the Sponsor or Devpost's receipt of the completed Required Forms.

Fees & Taxes: Winners (and in the case of a Team, all participating members) are responsible for any fees associated with receiving or using a prize, including but not limited to, wiring fees or currency exchange fees. Winners (and in the case of a Team, all participating members) are responsible for reporting and paying all applicable taxes in their jurisdiction of residence (federal, state/provincial/territorial and local). Winners may be required to provide certain information to facilitate receipt of the award, including completing and submitting any tax or other forms necessary for compliance with applicable withholding and reporting requirements. United States residents may be required to provide a completed form W-9 and residents of other countries may be required to provide a completed W-8BEN form. Winners are also responsible for complying with foreign exchange and banking regulations in their respective jurisdictions and reporting the receipt of the Prize to relevant government departments/agencies, if necessary. The Sponsor, Devpost, and/or Prize provider reserves the right to withhold a portion of the prize amount to comply with the tax laws of the United States or other Sponsor jurisdiction, or those of a winner's jurisdiction.
9\. Entry Conditions and Release

By entering the Hackathon, you (and, if you are entering on behalf of a Team, each participating member) agree(s) to the following:

The relationship between you, the Entrant, and the Sponsor and Administrator, is not a confidential, fiduciary, or other special relationship.
You will be bound by and comply with these Official Rules and the decisions of the Sponsor, Administrator, and/or the Hackathon Judges which are binding and final in all matters relating to the Hackathon.
You release, indemnify, defend and hold harmless the Promotion Entities, and their respective parent, subsidiary, and affiliated companies, the Prize suppliers and any other organizations responsible for sponsoring, fulfilling, administering, advertising or promoting the Hackathon, and all of their respective past and present officers, directors, employees, agents and representatives (hereafter the "Released Parties") from and against any and all claims, expenses, and liabilities (including reasonable attorneys' fees), including but not limited to negligence and damages of any kind to persons and property, defamation, slander, libel, violation of right of publicity, infringement of trademark, copyright or other intellectual property rights, property damage, or death or personal injury arising out of or relating to a Entrant's entry, creation of Submission or entry of a Submission, participation in the Hackathon, acceptance or use or misuse of the Prize (including any travel or activity related thereto) and/or the broadcast, transmission, performance, exploitation or use of the Submission as authorized or licensed by these Official Rules.

Without limiting the foregoing, the Released Parties shall have no liability in connection with: (a) Any incorrect or inaccurate information, whether caused by the Sponsor or Administrator's electronic or printing error, or by any of the equipment or programming associated with or utilized in the Hackathon; (b) Technical failures of any kind, including, but not limited to malfunctions, interruptions, or disconnections in phone lines, internet connectivity or electronic transmission errors, or network hardware or software or failure of the Hackathon Website; (c) Unauthorized human intervention in any part of the entry process or the Hackathon; (d) Technical or human error which may occur in the administration of the Hackathon or the processing of Submissions; or (e) Any injury or damage to persons or property which may be caused, directly or indirectly, in whole or in part, from the Entrant's participation in the Hackathon or receipt or use or misuse of any Prize.

The Released Parties are not responsible for incomplete, late, misdirected, damaged, lost, illegible, or incomprehensible Submissions or for address or email address changes of the Entrants. Proof of sending or submitting the aforementioned will not be deemed to be proof of receipt by the Sponsor or Administrator. If for any reason any Entrant's Submission is determined to have not been received or been erroneously deleted, lost, or otherwise destroyed or corrupted, the Entrant's sole remedy is to request the opportunity to resubmit its Submission. Such a request must be made promptly after the Entrant knows or should have known there was a problem and will be determined at the sole discretion of the Sponsor.
10\. Publicity

By participating in the Hackathon, Entrant consents to the promotion and display of the Entrant's Submission, and to the use of personal information about themselves for promotional purposes, by the Sponsor, Administrator, and third parties acting on their behalf. Such personal information includes, but is not limited to, your name, likeness, photograph, voice, opinions, comments and hometown and country of residence. It may be used in any existing or newly created media, worldwide without further payment or consideration or right of review, unless prohibited by law. Authorized use includes but is not limited to advertising and promotional purposes.
11\. General Conditions

Sponsor and Administrator reserve the right, in their sole discretion, to cancel, suspend and/or modify the Hackathon, or any part of it, in the event of a technical failure, fraud, or any other factor or event that was not anticipated or is not within their control.
Sponsor and Administrator reserve the right in their sole discretion to disqualify any individual or Entrant if it finds to be actually or presenting the appearance of tampering with the entry process or the operation of the Hackathon or to be acting in violation of these Official Rules or in a manner that is inappropriate, unsportsmanlike, not in the best interests of this Hackathon, or a violation of any applicable law or regulation.
Any attempt by any person to undermine the proper conduct of the Hackathon may be a violation of criminal and civil law. Should the Sponsor or Administrator suspect that such an attempt has been made or is threatened, they reserve the right to take appropriate action including but not limited to requiring an Entrant to cooperate with an investigation and referral to criminal and civil law enforcement authorities.
If there is any discrepancy or inconsistency between the terms and conditions of the Official Rules and disclosures or other statements contained in any Hackathon materials, including but not limited to the Hackathon Submission form, Hackathon Website, or advertising, the terms and conditions of the Official Rules shall prevail.
The terms and conditions of the Official Rules are subject to change at any time, including the rights or obligations of the Entrant, the Sponsor and Administrator. The Sponsor and Administrator will post the terms and conditions of the amended Official Rules on the Hackathon Website. To the fullest extent permitted by law, any amendment will become effective at the time specified in the posting of the amended Official Rules or, if no time is specified, the time of posting.
If at any time prior to the deadline, an Entrant or prospective Entrant believes that any term in the Official Rules is or may be ambiguous, they must submit a written request for clarification.
The Sponsor or Administrator's failure to enforce any term of these Official Rules shall not constitute a waiver of that provision. Should any provision of these Official Rules be or become illegal or unenforceable in any jurisdiction whose laws or regulations may apply to an Entrant, such illegality or unenforceability shall leave the remainder of these Official Rules, including the Rule affected, to the fullest extent permitted by law, unaffected and valid. The illegal or unenforceable provision shall be replaced by a valid and enforceable provision that comes closest and best reflects the Sponsor's intention in a legal and enforceable manner with respect to the invalid or unenforceable provision.
Excluding Submissions, all intellectual property related to this Hackathon, including but not limited to copyrighted material, trademarks, trade-names, logos, designs, promotional materials, web pages, source codes, drawings, illustrations, slogans and representations are owned or used under license by the Sponsor and/or Administrator. All rights are reserved. Unauthorized copying or use of any copyrighted material or intellectual property without the express written consent of its owners is strictly prohibited. Any use in a Submission of Sponsor or Administrator's intellectual property shall be solely to the extent provided for in these Official Rules.
12\. Limitations of Liability

By entering, all Entrants (including, in the case of a Team, all participating members) agree to release the Released Parties from any and all liability in connection with the Prizes or Entrant's participation in the Hackathon. Provided, however, that any liability limitation regarding gross negligence or intentional acts, or events of death or body injury shall not be applicable in jurisdictions where such limitation is not legal.
13\. Disputes

Except where prohibited by law, as a condition of participating in this Hackathon, Entrant agrees that: (a) Any and all disputes and causes of action arising out of or connected with this Hackathon, or any Prizes awarded, shall be resolved individually, without resort to any form of class action lawsuit, and exclusively by final and binding arbitration under the rules of the American Arbitration Association and held at the AAA regional office nearest the contestant; (b) The Federal Arbitration Act shall govern the interpretation, enforcement and all proceedings at such arbitration; and (c) Judgment upon such arbitration award may be entered in any court having jurisdiction.

Under no circumstances will Entrant be permitted to obtain awards for, and Entrant hereby waives all rights to claim, punitive, incidental or consequential damages, or any other damages, including attorneys' fees, other than contestant's actual out-of-pocket expenses (i.e., costs associated with entering this Hackathon), and Entrant further waives all rights to have damages multiplied or increased.

All issues and questions concerning the construction, validity, interpretation and enforceability of these Official Rules, or the rights and obligations of the Entrant and Sponsor in connection with this Hackathon, shall be governed by, and construed in accordance with, the substantive laws of the State of New York, USA without regard to New York choice of law rules.

SOME JURISDICTIONS DO NOT ALLOW THE LIMITATIONS OR EXCLUSION OF LIABILITY FOR INCIDENTAL OR CONSEQUENTIAL DAMAGES, SO THE ABOVE LIMITATIONS OF LIABILITY MAY NOT APPLY TO YOU.
14\. Additional Terms

Please review the Devpost Terms of Service at https://info.devpost.com/terms for additional rules that apply to your participation in the Hackathon and more generally your use of the Hackathon Website. Such Terms of Service are incorporated by reference into these Official Rules, including that the term "Poster" in the Terms of Service shall mean the same as "Sponsor" in these Official Rules. If there is a conflict between the Terms of Service and these Official Rules, these Official Rules shall control with respect to this Hackathon only.
15\. Entrant's Personal Information

Information collected from Entrants is subject to Devpost's Privacy Policy, which is available at https://info.devpost.com/privacy.

For questions, send an email to support@devpost.com.

Previous imageNext image
````

## Overview and submission requirements (`overview.md`)

````text
Codex x TwitchCon Hackathon

Deadline: Nov 2, 2026 @ 5:00pm EST

Join hackathon
Codex x TwitchCon Hackathon
Build for streamers and their community on Twitch with OpenAI Codex. $25,000 in prizes, and the top 5 are shown on the Codex Booth stage at TwitchCon.

Join hackathon
Who can participate

Above legal age of majority in country of residence
Companies/professional organizations excluded from participation
All countries/territories, excluding
standard exceptions

View full rules

8 more days to deadline

View schedule

Deadline
Nov 2, 2026 @ 5:00pm EST

Apple
Google
Outlook

|     |     |
| --- | --- |
| Online | Public |
| $25,000 in cash | 473<br> participants |

Twitch

Managed by Devpost

Communication Gaming Machine Learning/AI

Twitch is the home of shared live experiences, and developers shape how streamers and their communities experience them.

OpenAI and Twitch are teaming up to see what developers can build for the Twitch community with AI. In the Codex x TwitchCon Hackathon, you'll use OpenAI Codex to build useful and creative experiences for Twitch streamers and their community. Give chat a way to play along, help streamers create together, or add something new to enhance the content they stream. You’ll leave with a working project and hands-on experience building with Codex.

The top 5 projects will be showcased on the Codex Booth stage at TwitchCon San Diego on November 15, where winners will be announced live.
Why join?

$25,000 in prizes, and a spot on the TwitchCon stage for the top 5
Build with Codex: tell Codex what you're building and let it help you get set up with the Twitch API, EventSub and chat
Connect streamers and their community: build something streamers and viewers can use live on stream
Get started

Sign in to Codex and start a new thread for your project. You’ll need its session ID when you submit.
Find everything you need to build at dev.twitch.tv. Not sure where to start? Get a chatbot running in minutes with the Example Chatbot guide
Join the TwitchDev Discord and ask questions in the channel that fits what you're building. Say hi in #codex-twitchcon-hackathon channel for general questions and updates.
Requirements
What to build

Build for streamers and their community on Twitch with OpenAI Codex.

Not sure where to start? No problem. Here are a few directions to explore:

Streamer collaboration: help streamers talk, play or create together on stream
Audience participation: let chat join in via a Twitch Plays game, live polls or even streamer distractions
Content enhancements: build around what's being streamed, like a dice roller for tabletop streams, a live sports overlay or a tool for IRL and science streams

These are starting points, not templates. Judges are looking for original ideas, so don’t just rebuild the examples above. Go big, or build something small and scrappy over a weekend. It all counts as long as it ​​connects to Twitch (e.g. Twitch API, EventSub, chat, Extensions, overlays) and was built with OpenAI Codex.
What to submit

Provide a URL to your code repositoryfor judging and testing on GitHub, GitLab or Bitbucket.

  - It must contain all source code, assets, and instructions needed for the project to run.
  - The repository may be public or private. If private, it must be on GitHub or GitLab and shared with testing@devpost.com.
A demo video. Include a video (max 3 minutes) that shows your project working on Twitch and how you used Codex. Videos must be uploaded to YouTube and made publicly visible.
A project description. Include a text description that explains the project's features and functionality and how you used Codex.
Codex Session ID. Provide the Codex session ID for the thread where you built most of your project (type /status in Codex to see it). If you used multiple threads, include the one where most of the build happened.
Hackathon Sponsors
Prizes

$25,000 in prizes
1st Place

$10,000 in cash

1 winner

$10,000 USD and stage time at TwitchCon
2nd Place

$6,000 in cash

1 winner

$6,000 USD and stage time at TwitchCon
3rd Place

$4,000 in cash

1 winner

$4,000 USD and stage time at TwitchCon
Runner Ups

$2,500 in cash

2 winners

$2,500 USD and stage time at TwitchCon
Devpost Achievements

Submitting to this hackathon could earn you:
Judges

A panel of qualified judges
Judging Criteria

Innovation/Idea

How creative and novel is the concept and does the project differ from existing concepts?

Potential Impact

How useful or entertaining is it for streamers and their communities?

Technological implementation

How well is it built, and how well does it use Codex?

Design

Is it easy to use and fun to watch?

Questions?
Email the hackathon manager

Invite others to compete

This site is protected by reCAPTCHA and the Google
Privacy Policy and
Terms of Service apply.

Previous imageNext image
````

## Resources and FAQ (`resources.md`)

````text
Codex x TwitchCon Hackathon

Deadline: Nov 2, 2026 @ 5:00pm EST

Join hackathon

Twitch developer docs: https://dev.twitch.tv/docs/
Topical docs

Chat & Chatbots https://dev.twitch.tv/docs/chat/
EventSub https://dev.twitch.tv/docs/eventsub/
Twitch API https://dev.twitch.tv/docs/api/
Extensions https://dev.twitch.tv/docs/extensions/
Showcase for inspiration https://dev.twitch.tv/showcase/
FAQs
General and TwitchCon

What is the Codex x TwitchCon Hackathon? An online hackathon where you use OpenAI Codex to build an interactive experience for streamers and their community on Twitch. Give chat a way to play along, help streamers create together, or add something new to the content they stream. The top 5 projects are showcased on the Codex Booth stage at TwitchCon San Diego on November 15, where winners are announced live.

What should I build? Build for streamers and their community on Twitch with OpenAI Codex. A few directions to explore:

Streamer collaboration: help streamers talk, play or create together on stream
Audience participation: let chat join in with a Twitch Plays game, live polls or streamer distractions
Content enhancements: build around what's being streamed, like a dice roller for tabletop streams, a live sports overlay or a tool for IRL and science streams

These are starting points, not templates. Judges are looking for original ideas, so don’t just rebuild the examples above. Go big, or build something small and scrappy over a weekend. It all counts as long as it connects to Twitch and was built with Codex.

Do I need to be a developer? No. Streamers and newer builders are welcome. Codex can help you set up the Twitch API, EventSub and chat. Your project still needs to run and work as shown in your video.

What are the key dates?

|     |     |
| --- | --- |
| Milestone | Date |
| Submissions open | October 23, 2026, 10:00 AM PT |
| Submission deadline | November 2, 2026, 2:00 PM PT |
| Judging Period | November 5, 2026 (9:00 AM PT) – November 15, 2026 (5:00 PM PT) |
| Winners announced | On or around November 15, 2026 at TwitchCon San Diego |

Do I have to attend TwitchCon to enter? No. The hackathon is fully online. Attending TwitchCon is not a requirement. The top 5 projects will be showcased on the Codex Booth stage at TwitchCon San Diego.

Is there a cost to enter? No. From the Official Rules: "NO PURCHASE OR PAYMENT NECESSARY TO ENTER OR WIN."
Eligibility

Who can enter? The Hackathon IS open to:

Individuals who are at least eighteen (18) years old or the age of majority where they reside as of the time of entry, whichever is older ("Eligible Individuals"); and
Teams of Eligible Individuals ("Teams").

I'm under 18. Can I enter? No. The Hackathon is open to "Individuals who are at least eighteen (18) years old or the age of majority where they reside as of the time of entry, whichever is older ("Eligible Individuals")." There is no waiver for participants under 18.

Which countries are excluded? The Hackathon IS NOT open to: "Individuals who are residents of a country, state, province or territory where the laws of the United States or local law prohibits participating or receiving a prize in the Hackathon (including, but not limited to, Brazil, Quebec, Russia, Crimea, Cuba, Iran, and North Korea and any other country which is comprehensively sanctioned by the U.S. Treasury’s Office of Foreign Assets Control, and any applicable denied-party lists)"

Is eligibility based on citizenship or where I live? Where you legally reside. The rules refer to "residents of a country, state, province or territory," not citizenship.

Can my company, startup or student club enter? No. The Hackathon IS NOT open to: "Organizations, including corporations, not-for-profit corporations and other nonprofit organizations, limited liability companies, partnerships, and other legal entities". You can enter as an individual or as a team of eligible individuals.

Can I join more than one team, or enter solo and on a team? Yes. "An Eligible Individual may join more than one Team and an Eligible Individual who is part of a Team may also enter the Hackathon on an individual basis."

How do teams submit? One person, the team Representative, clicks Start Project on the hackathon page, then adds teammates in the Manage Team section of the project. Each teammate must accept the invite to appear on the submission. The Representative enters the submission for the whole team. From the Official Rules: "If a Team is entering the Hackathon, they must appoint and authorize one individual (the "Representative") to represent, act, and enter a Submission, on their behalf." Prizes are paid to the Representative, who splits them with the team.

Is there a maximum team size? The Official Rules do not set a maximum team size. Every team member must be an Eligible Individual.

I work at Twitch, Amazon, OpenAI or Devpost. Can I enter? No. The Hackathon IS NOT open to "Organizations involved with the design, production, paid promotion, execution, or distribution of the Hackathon, including the Sponsor, OpenAI and Administrator ("Promotion Entities")", "Employees, representatives and agents of such Promotion Entities, and all members of their immediate family or household", or "Any parent company, subsidiary, or other affiliate of any organization described above". See Section 3 of the Official Rules for the full list.
Submission requirements

What do I need to submit?

Provide a URL to your code repository for judging and testing on GitHub, GitLab or Bitbucket. It must contain all source code, assets, and instructions needed for the project to run. The repository may be public or private. If private, it must be on GitHub or GitLab and shared with testing@devpost.com.
Include a text description that explains the Project's features and functionality and how you used Codex.
Provide the Codex session ID for the Codex thread where the Project was built.
A demonstration video under three minutes that shows your project working on Twitch and how it was built with Codex.

Does my project have to connect to Twitch? Yes. "The Project must be an interactive experience that connects to Twitch, for example through chat, a stream overlay, the Twitch API, EventSub or an Extension."

Can I use a project I started before the hackathon? No. "Projects must be newly created during the Submission Period. Participants may use standard development tools, including frameworks, libraries, starter templates, and AI coding assistants. The work described and submitted must have been built during the Submission Period."

Can I start from Twitch's Example Chatbot guide? Yes. Starter templates are allowed. Judges focus on what you built on top of it.

Can my repo be private? Yes. "The repository may be public or private. If private, it must be on GitHub or GitLab and shared with testing@devpost.com."

What are the video rules? The video portion of the Submission:

should be less than three (3) minutes. Judges are not required to watch beyond three minutes
should include footage that shows the Project functioning on Twitch
Should include footage that shows how the project was built with Codex
must be uploaded to and made publicly visible on YouTube and a link to the video must be provided on the submission form on the Hackathon Website; and
must not include third party trademarks, or copyrighted music or other material unless the Entrant has permission to use such material.

Can my YouTube video be unlisted? Yes, unlisted is fine. Private videos can't be viewed by judges.

Can I show other streamers, games or music in my video? Only with permission. The video must not include third party trademarks, or copyrighted music or other material unless the Entrant has permission to use such material.

Can I submit more than one project? Yes. "An Entrant may submit more than one Submission, however, each Submission must be unique and substantially different from each of the Entrant's other Submissions, as determined by the Sponsor and Devpost in their sole discretion."

Does my submission have to be in English?"All Submission materials must be in English or, if not in English, the Entrant must provide an English translation of the demonstration video, text description, and testing instructions as well as all other materials submitted."

Do judges have to test my project? No. "Judges are not required to test the Project and may choose to judge based solely on the text description, images, and video provided in the Submission." Make your video count.
Technical and Codex

How do I get started with OpenAI Codex? Sign in to Codex and tell it what you're building. Codex can help you get set up with the Twitch API, EventSub and chat.

Do I need a paid Codex plan? No. Use the free version of Codex. Free usage has limits, so keep an eye on your usage as you build and leave some headroom for final fixes before the deadline.

What's the fastest way to connect a project to Twitch? Start with Twitch's Example Chatbot guide. It gets a chatbot running in minutes, and you can build from there. Everything else you need is in the Twitch developer docs.

Which Twitch docs are most useful?

Chat & Chatbots: read and respond to chat
EventSub: react to follows, subs, raids and other live events
Twitch API: channel, stream and user data
Showcase: see what other developers have built

Should I build an Extension? You can, but please note that it can take 5–14 days for it to be reviewed and judges can't install an unreviewed Extension. Chat, overlays, the Twitch API and EventSub are faster paths.

Where do I find my Codex session ID? Type /status in the Codex thread where you built most of your project. Paste that ID into the submission form.

I used several Codex threads. Which session ID do I submit? The one for the thread where you built most of your project.

Can I use other AI tools too? Yes. The rules allow "standard development tools, including frameworks, libraries, starter templates, and AI coding assistants." Your project must be built with Codex, and Codex use is part of the Technological Implementation criterion.

How much can Codex build for me? As much as helps. The Submission must "be the original work of the Entrant" and be "the result of the Entrant's ideas and creativity." You direct the idea and the decisions. Be ready to explain how your project works.

My project uses API keys. What do judges need? Never commit keys to your repo. Use environment variables and list them in your setup instructions. Your repo must contain "all source code, assets, and instructions needed for the project to run."

Can I use third-party APIs, games or assets? Yes, if you're allowed to. "If a Project integrates any third-party SDK, APIs and/or data, Entrant must be authorized to use them in accordance with any terms and conditions or licensing requirements of the tool."
Deadline, judging and prizes

When exactly is the deadline? November 2, 2026, 2:00 PM Pacific Time. That's 5:00 PM ET, 10:00 PM in London and 9:00 PM UTC. Check the countdown on the hackathon page for your local time.

I saved my project. Is it submitted? Not until you click Submit. A saved draft is not entered. To check, open the My projects tab on the hackathon page. Your project should show as Submitted before the deadline.

Can I submit late? No. Submissions must be entered "during the Submission Period." Submit early and keep editing until the deadline.

Can I edit my project after the deadline? No. "Once the Submission Period has ended, you may not make any changes or alterations to your Submission, but you may continue to update the Project in your Devpost portfolio." Don't change your repo, video or linked materials until winners are announced. To keep building, copy your repo and work in the copy.

How is judging done? In two stages. Stage One checks "via pass/fail whether the ideas meet a baseline level of viability, in that the Project reasonably fits the theme and reasonably applies the required developer tools featured in the Hackathon." In Stage Two, judges score submissions on four equally weighted criteria, and the five highest scoring Submissions will become finalists.

What are the judging criteria?

Innovation/Idea: How creative and novel is the concept and does the project differ from existing concepts?
Potential Impact: How useful or entertaining is it for streamers and their communities?
Technological implementation: How well is it built, and how well does it use Codex?
Design: Is it easy to use and fun to watch?

Is AI used in judging? The rules say judging "may utilize expert panels, peer review, automated AI-driven analysis, or any combination thereof to ensure efficient, fair, and objective evaluation."

What are the prizes? $25,000 USD in total.

|     |     |
| --- | --- |
| Prize | Award |
| 1st Place | $10,000 USD and stage time at TwitchCon |
| 2nd Place | $6,000 USD and stage time at TwitchCon |
| 3rd Place | $4,000 USD and stage time at TwitchCon |
| Runner Ups (2) | $2,500 USD each and stage time at TwitchCon |

When and how are prizes paid? After winners complete the required forms. "The deadline for returning the Required Forms to the Administrator is ten (10) business days after the Required Forms are sent." "Prizes will be delivered within 60 days of the Sponsor or Devpost's receipt of the completed Required Forms."

Who pays taxes on prizes?"Winners (and in the case of a Team, all participating members) are responsible for reporting and paying all applicable taxes in their jurisdiction of residence." US residents may need a W-9; others may need a W-8BEN.

Do I keep ownership of my project? Yes. "All Submissions remain the intellectual property of the individuals that developed them."
Support

Where do I ask technical questions? In the TwitchDev Discord. Ask in the help channel that fits what you're building, where the developer community answers.

Will Twitch or OpenAI staff answer questions? The community answers most technical questions in the TwitchDev Discord. Staff aren't guaranteed to be online, and Devpost checks in regularly to route questions.

How do I find teammates? Use the Participants tab on the hackathon page to find people looking for a team, or post in the #codex-twitchcon-hackathon channel in the TwitchDev Discord.

Who do I contact about eligibility, submissions or prizes? If your question isn't answered in this FAQ post your question in the #codex-twitchcon-hackathon channel in the TwitchDev Discord. Responses might take a business day or two.

Previous imageNext image
````
