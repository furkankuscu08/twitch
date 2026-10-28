# Evidence gathering: 10 hackathon idea cards

You are an independent researcher. Your job is to **gather evidence** about 10 idea cards for a hackathon entry. You do **not** score or rank the cards. Another step will score them later using your evidence and the evidence from other researchers, who work separately and whom you will never see.

## The competition

**Codex x TwitchCon Hackathon** (Devpost). Deadline: Nov 2, 2026. The brief: "Build something streamers and their community on Twitch could really use." Entries must connect to Twitch (chat, overlays, Twitch API, EventSub) and be built with OpenAI Codex.

**Judging criteria** (official text, four equally weighted):
1. **Innovation/Idea:** How creative and novel is the concept and does the project differ from existing concepts?
2. **Potential Impact:** How useful or entertaining is it for streamers and their communities?
3. **Technological implementation:** How well is it built, and how well does it use Codex?
4. **Design:** Is it easy to use and fun to watch?

Judges mostly watch a video of under 3 minutes. The builder is solo, new to Twitch and has no audience; the demo uses one streamer and three test accounts. The video **cannot show commercial games or copyrighted music**, so demos use desk/IRL content or original content.

## What to find for each card

**A. Closest existing things** (up to 5). Check the competitors the card already names (do they exist, and how close are they?) and look for ones it missed: commercial tools, bots, OBS plugins, Streamer.bot/StreamElements/Streamlabs widgets, Twitch extensions, GitHub projects, past hackathon entries (Devpost, earlier Twitch hackathons and game jams), and common streamer bits done by hand. For each give:
- name and **link**;
- what it does, in one line;
- **overlap:** `Same core loop` / `Partial` (shares an important part) / `Adjacent` (same problem, different approach);
- whether it looks active or popular (date, users, stars, installs) if visible.

**B. Does the claimed difference survive?** `Yes` / `Partly` / `No`, with one line of reasoning based on A.

**C. Demand signals** (up to 5, with links): posts, threads, videos or feature requests where streamers or viewers describe the problem the card solves or ask for something like it. Add **counter-signals** if you find them (people who say they dislike or would not use such a thing).

**D. Audience fit.** Use the stream-type data below.
- Which stream types or categories does the card work in?
- Roughly what share of Twitch viewing do those types represent?
- Can the 3-minute demo show the card in its **natural setting**, given the no-commercial-games rule? `Yes` / `Partly` / `No`, and why.
- Is it **type-independent** (works on almost any stream) or **tied** to a specific format?

**E. Fact problems** (optional): any Twitch API or platform fact in the card that your sources contradict, with a link.

## Rules

- **Every factual claim needs a link.** If you could not open a page and only saw a search snippet, mark it `(snippet)`.
- If you find nothing, write `Not found`. Never invent tools, posts, numbers or links.
- Prefer primary sources (the tool's own page, the repo, the post itself).
- Spend roughly equal effort on every card.
- Do not score, rank or recommend cards.

## Output format

One section per card, in the card order, with the headings **A. Closest existing things**, **B. Claimed difference**, **C. Demand signals**, **D. Audience fit**, **E. Fact problems**.

Then a final summary table:

| Card | Closest thing (link) | Overlap | Difference survives | Demand signals found | Counter-signals | Natural-setting demo | Type-independent |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Stream-type data (research of 2026-10-26)

Sources: TwitchTracker, SullyGnome, Streams Charts, Streamlabs/Stream Hatchet, Twitch State of Gaming 2026. Treat these as approximate.

- **Just Chatting** is #1: ~304K average viewers, **14.2% of Twitch viewing** (7 days, Oct 2026); its hours are flat in 2026.
- The top 15 is otherwise almost all **games** (League of Legends 8.6%, Minecraft 4.5%, GTA V 3.9%, Counter-Strike 3.2%, Call of Duty 3.0%, VALORANT, Fortnite, Dota 2, WoW ~2% each). **IRL** is #11 (1.8%).
- Mid-size non-gaming categories: Sports #29, ASMR #34, Art #40, DJs #41, Music #52, Talk Shows & Podcasts ~#66–71. Software & Game Development, Food & Drink and Makers & Crafting are far lower.
- Growing formats: **indie games** +51% YoY, **horror** +6% YoY (Jan–Sep 2026). IRL grew strongly in 2025, mixed in 2026. Event and marathon streams create spikes.
- Viewers per live channel: IRL ~75, Just Chatting ~66, Art ~17, Music ~14; platform average ~23. A low ratio means many channels share a small audience.
- Most channels are small: one unverified source says ~61% of channels average under 10 viewers.
- Twitch total hours fell ~8% YoY in Q2 2026; Kick grew ~37%.
- No usable data was found for co-streaming, speedruns, blind playthroughs or cooking.

## The 10 cards

Each card shows its one-liner, its best variant, its core loop and the competitors it already names.

## 1. Minefield

**One-liner:** Viewers secretly plant "word mines". When the streamer says a mined word out loud, it explodes on stream with the planter's name.

**Best variant:** Word mines with local speech-to-text. Dropped: Sound Tags, Try Not To Laugh, Sip Watch.

**Core loop:**
1. A viewer types `!mine`. The bot replies with a link to a plant page (Twitch login). Nobody else sees the word.
2. The overlay shows mine chips with owners' names, never the words. Rules: one live mine per viewer, 4+ letters, not a top-1000 common word, blocklist.
3. Viewers steer the conversation toward their word ("worst pizza topping?").
4. Local speech-to-text listens to the streamer's mic: faster-whisper (`base.en`/`small.en`) on a sliding ~2 s window, VAD on, live mines passed as `hotwords`, whole-word match on normalized text (plurals count).
5. Instant explosion, screen shake, the banner "Bo's mine: PINEAPPLE (planted 6 min ago)" and a stream marker. A mod can **DEFUSE** within 10 s: a rewind animation and a "false alarm" stamp, played as a gag. If not defused, a titled 30 s clip is created.
6. Unexploded mines flip over as "duds" at the end: "Cy's mine 'GIRAFFE' never went off".

**Closest existing things and claimed difference:** speech-recognition swear jars; the party game Taboo; a past Twitch hackathon entry that used streamer speech to start a poll; stream-bingo overlays (1up.vision Bingo); the "if I say X…" streamer challenge bit. *Difference:* the audience picks secret targets, so it is a viewer-vs-streamer game hidden inside ordinary talk, and detection is automatic.

---

## 2. Tap on the Shoulder (production problems reach the streamer)

**One-liner:** Chat can't tap you on the shoulder while you're heads-down. Now it can: viewer reports and mod cues become a face on your desk, and chat confirms the fix.

**Best variant:** Tap on the Shoulder (report detection and mod cues) with a simplified Soundcheck confirm loop, and **(absorbed)** Desk Buddy as the signal device. Dropped: the lamp.

**Core loop:**
1. **Inputs:**
   - ≥2 distinct viewers mention mic, audio, "far away", black screen or frozen within 60 s, or anyone types `!mic`;
   - a mod taps a preset on a private phone page ("you sound far away", "game too loud", "mic muted", "answer @x");
   - obs-websocket reports the mic input muted or silent while live.
2. A phone face on the desk, in the camera shot, turns alarmed and shows the issue in huge letters. A chime plays in the streamer's headphones only. When chat and OBS agree, the face says so ("chat + OBS: mic muted").
3. The streamer fixes it and taps a "fixed" hotkey.
4. The bot posts "Fix #2: sound right now? 👍/👎". Replies that arrive earlier than fix time plus the measured stream delay are ignored.
5. The issue resolves on the dock, and the overlay credits the first reporter.
6. When nothing is wrong, the face shows calm chat state (a first-time chatter waves, a question is waiting).

**Closest existing things and claimed difference:** Streamer.bot and WooferBot light lamps on Twitch events; OBS mute indicators and obs-websocket mute alerts; Twitch Guardian (keyword-alert Chrome extension); Elgato's Mochi chat pet and Prompter chat mode; a friend relaying chat. *Difference:* it routes human judgment (viewer reports, mod cues) to a signal in the room that survives a fullscreen game, cross-checks OBS, then closes the loop with the audience's confirmation.

---

## 3. VAR

**One-liner:** When chat disputes a moment, two `!var` calls start a broadcast-style review: slow-motion replay, a 15-second chat jury, a verdict stamp, and a titled clip.

**Best variant:** As designed, plus "Self-VAR". The replay is only the means; the verdict is the show.

**Core loop:**
1. The streamer claims something ("IN!").
2. Two distinct viewers type `!var` within 30 s. The threshold scales with active chatters, and mods or the streamer can also call it.
3. A "VAR CHECK" stinger plays. obs-websocket saves the 60 s replay buffer.
4. An OBS Media Source, driven by obs-websocket, plays the last ~10 s shifted by a latency offset, with the last 4 s at half speed.
5. Chat votes `!yes` or `!no` for 15 s; names appear on a jury bench.
6. The verdict stamp lands. Then the app creates a 60 s clip titled "VAR: NO BASKET" and a marker. The clip holds the review, and the review holds the replay of the moment.

**Closest existing things and claimed difference:** the OBS "Instant Replay" script triggered by a chat command; Streamer.bot instant-replay actions; native polls. *Difference:* a full review ritual (call, replay, jury, verdict, titled clip) instead of a replay or a poll alone.

---

## 4. Raid Torch

**One-liner:** A torch that only travels by raid: every chat that holds it leaves a mark, and the raiders who carried it light up when they arrive.

**Best variant:** A same-day relay with a visible journey and torch-bearers. Dropped: G-7 (an activity carried into the next stream) and the multi-day journey. Fallback: a one-sided send-off.

**Core loop:**
1. Channels join a circle with a code, on a hosted backend.
2. While a channel holds the torch, each chatter adds one mark with `!mark <emote>`, and rings grow on the torch. Twitch-native emotes render as images; third-party emotes show as text.
3. The streamer raids. EventSub `channel.raid` hands the torch over.
4. On the target's overlay, the torch flies in with its rings and a journey map ("3 channels, 14 marks tonight").
5. **Torch-bearers:** a raider who added a mark glows when they first chat in the new channel ("Ana carried a mark from A"). The target streamer sees who the raiders are.
6. A public journey page shows tonight's path. It resets after the evening.

**Closest existing things and claimed difference:** raid alerts; raid-train tools (R3dLabs Toolbox raid-train Stream Deck plugin, RaidRunner scheduling). *Difference:* state carried across channels; the raid becomes a visible object, and the raiders are recognized on arrival.

---

## 5. Previously On

**One-liner:** When raiders arrive, or a late viewer asks, the stream plays a 10-second TV-style "Previously on…" recap built from beats dropped during the stream.

**Best variant:** The overlay recap (L1-3), plus the pinned recap (Story So Far), now that Pin Chat Message is a documented endpoint.

**Core loop:**
1. During the stream, beats come from habits the streamer already has: every stream marker (Twitch's marker shortcut, a Stream Deck) becomes a beat, read every 30 s with Get Stream Markers. A hotkey or a mod's `!beat Beat the frog king on try 9` also adds one. Title and category changes become beats automatically.
2. On an incoming raid, the overlay runs a TV bumper: "Previously on…", the last three beats with timestamps and the current goal.
3. A late viewer types `!recap`. The bot posts a compact version and pins it for 10 minutes.
4. **(absorbed)** A first-time chatter gets one quiet chat reply with the current goal and `!recap`, never an on-screen spotlight.
5. **(absorbed, stretch)** A channel glossary: mods add a few lore terms, and the first mention of a term on a recap card gets a footnote.

**Closest existing things and claimed difference:** raid alerts and auto-shoutouts (they greet the raider); a hand-pinned "today's plan"; custom `!lore` commands; AI "what did I miss" summarizers; Twitch's automatic VOD chapters on category changes. *Difference:* a human-curated, TV-style briefing aimed at newcomers, triggered by their arrival, with no AI summary.

---

## 6. Studio Audience

**One-liner:** Chat becomes a live theater crowd you can hear. Every laugh belongs to a real, named viewer, and it only gets louder when more people react.

**Best variant:** As designed, with chants in the MVP. **(absorbed)** Lurker seats are a stretch and stay out of the video.

**Core loop:**
1. Emotes and keywords map to five reactions: laugh, gasp, aww, applause, boo.
2. A crowd engine mixes CC0 samples. Intensity scales with *distinct* reacting viewers, so spam can't inflate it, and the crowd never sounds bigger than the number of real reactors.
3. Each viewer has a signature laugh: a sample from a pool, a playback rate and an EQ, all derived from their user ID (changeable with `!mylaugh 7`). It rises out of the crowd, and their named seat silhouette bounces.
4. The same word from 2+ viewers within 10 s becomes a chant with the word on screen.
5. A follow brings applause; a raid opens the doors and adds seats.
6. A headphone-only mode lets the streamer hear the room without putting it on stream.

**Closest existing things and claimed difference:** Sound Alerts; per-user entrance sounds (Streamer.bot); Meld Emote Storm and StreamElements' KappaGen emote explosion (visual scaling). *Difference:* a scaled, mixed crowd you hear, where each voice belongs to a named viewer.

---

## 7. Foley Pit

**One-liner:** Chat writes the sound-effects score, the streamer performs it with a cup and a spoon, and an audio model judges how much the spoon sounded like footsteps.

**Best variant:** Foley Pit with a Foley meter. Variants (Prop Jury, Bench Test) are dropped.

**Core loop:**
1. The streamer opens a scene card ("A tiny detective enters a storm").
2. Three viewers claim a role (weather, footsteps, surprise) and pick one cue from a small vocabulary.
3. The three-beat score fills in on screen and locks.
4. The streamer advances beat by beat and performs each sound with desk objects. Local onset detection finds each performed sound.
5. **Foley meter:** a zero-shot audio-text model (CLAP) scores the sound against its cue text: "spoon footsteps: 71% footsteps". The beat lights up with its score.
6. The scene ends with a Foley score and a one-word chat verdict, and the app creates a titled "foley reel" clip.

**Closest existing things and claimed difference:** viewer-triggered sound effects (playback); ASMR trigger requests via channel points; Whose Line's "Sound Effects" game; improv games. *Difference:* the audience writes the score, the streamer performs it, and a model judges the performance.

---

## 8. Hint Jar

**One-liner:** On blind playthroughs, viewers who know the answer seal tiered hints into a jar instead of backseating. The streamer opens only the tier they want, when they want it.

**Best variant:** Hint Jar (L1-5) with Hint Airlock's mod classification (G-1). Hints go in through a private page, not public chat. The demo runs on a small original puzzle game built with Codex.

**Core loop:**
1. A viewer types `!hint` and gets a link to a hint page (Twitch login), where they pick a tier (nudge, method, answer) and write the hint.
2. Optionally, a mod approves each hint and corrects its tier on a private dock.
3. The overlay jar fills with envelopes by tier: "Nudge 2 · Method 1 · Answer 1".
4. The streamer says "okay, one nudge" and hits a hotkey. One nudge opens with its author; the answer stays visibly sealed.
5. If solved, "@ana saved the run ⭐". The same nudge from two viewers credits both.

**Closest existing things and claimed difference:** no-backseating rules; LeagueBackseat (queues backseat messages); channel-point "backseat allowed for 1 min" rewards. *Difference:* the help is tiered, gated by the streamer and revealed as a show.

---

## 9. Photo Booth

**One-liner:** Meet-and-greet for every viewer: type `!snap`, and you and the streamer pose together in a Polaroid that develops live, and the whole chat ends up on the corkboard.

**Best variant:** A photo *with* the viewer: their Twitch avatar is composited into the frame next to the streamer. The raid group photo is in the MVP. Dropped: ticket stubs, the museum.

**Core loop:**
1. A viewer types `!snap first win` (once per stream). The streamer hears a cue and leaves room in the frame.
2. The overlay counts 3-2-1; obs-websocket grabs the frame (the camera, or a "booth" scene).
3. The app places the viewer's avatar beside the streamer. A Polaroid develops over 5 s, captioned "Ana · first win · Oct 30". The viewer gets a link that expires after 24 h.
4. A raid triggers a group photo with all raiders' avatars squeezed in.
5. The outro shows a corkboard collage: "4 of us were here today".

**Closest existing things and claimed difference:** StreamUP's "Polaroid Picture" for Streamer.bot (a channel-point redeem takes a Polaroid of an OBS source; reported by the reviewer, to be verified); generic chat-to-overlay commands; physical subscriber-slip printers. *Difference:* the viewer appears in the photo with the streamer, the raid becomes a group photo, and the stream ends with a collage of everyone who was there.

---

## 10. Checkpoint

**One-liner:** Go heads-down without ghosting chat: messages become save crystals, and at the checkpoint each one gets a call-in card, an on-stream answer and a reply ping.

**Best variant:** Checkpoint (L1-1) with context thumbnails and reply pings. The mod-collected variant (G-18) is dropped.

**Core loop:**
1. The streamer hits a hotkey, a mod types `!focus`, or OBS switches to a "focus" scene. A corner badge: "Focus: messages saved 0".
2. Each normal viewer message drops a save crystal in the viewer's color. Commands and bot lines are filtered out. obs-websocket stores a screenshot of that moment, locally, deleted at the end of the stream.
3. The streamer hits "checkpoint". A lower-third call-in card shows the first saved message with its thumbnail: "you asked this while I was inking the eyes". Questions and first-time chatters come first. A mod's urgent lane breaks through at any time.
4. The streamer answers aloud and hits "next". The card stamps ✓, and the bot replies in thread to the viewer: "✓ answered on stream at 12:04".
5. At the end: "Checkpoint cleared: 4 answered".
6. A reminder fires if focus has run for N minutes without a checkpoint.

**Closest existing things and claimed difference:** StreamerQnA and Meld question queues; Chatterino highlights; AI "what did I miss" summaries; featured-message overlays (Social Stream Ninja, StreamElements). *Difference:* time-boxed to the busy stretch, captures normal messages without a command, shows the context of each message and pings the viewer when answered.


---

## Your sources

Search **X (Twitter)** first: streamers' and viewers' posts about these problems, announcements of similar tools, and reactions to them. Give the post link and date for each. Then use general web search for anything X does not cover. You have no access to any files; everything you need is in this message.
