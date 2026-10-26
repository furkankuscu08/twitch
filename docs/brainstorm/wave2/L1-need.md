# L1: Need-driven ideas (wave 2)

Written 2026-10-25. Lens: start from a concrete moment of pain (needs #1, #3, #4, #6 first), then give it a visible on-stream moment.

Labels: **[V]** verified (source read, or search result confirming a tool exists), **[I]** inference, **[U]** unknown. Evidence numbers refer to brief section 5.

Prior-art searches (2026-10-25; tools [V exists], gaps [I], absence not proven):
- **Q&A queue:** StreamerQnA (OBS forum) shows `!command` questions on stream one by one.
- **Backseat queue:** LeagueBackseat (GitHub) queues timestamped backseat messages. No tool seals hints until the streamer asks.
- **Raid recap:** no "what you missed" card for raiders found; raid tools are confetti and auto-shoutouts (Sidekick).
- **Smart lights:** WooferBot drives Hue/Nanoleaf from events, including "New Chatter". Nothing routes *urgent human reports* ("your mic is muted") to the streamer.
- **Lore glossary:** nothing explains a channel's in-jokes on stream; the workaround is Nightbot commands.

---

## A. Crowd map

These are the ~10 ideas I expect most entrants to build.

1. **AI co-host or chatbot persona** that answers chat by voice or text (TTS avatar).
2. **AI "what did I miss" chat summarizer** for the streamer.
3. **Twitch Plays:** chat commands control a game, an emulator or a web mini-game.
4. **Live polls or predictions overlay** with nicer visuals than native polls.
5. **Chat trivia or quiz** with a leaderboard overlay.
6. **TTRPG dice roller or character-sheet overlay** (the organizer's example).
7. **Streamer distractions:** chat triggers screen shake, sounds, filters or TTS. A Crowd Control-lite.
8. **Chat-fed overlay creature or boss fight:** a pet, tamagotchi, fishing or "chat vs boss" game.
9. **Stream bingo or prediction bingo cards.**
10. **Auto-clipper:** a chat-spike detector that creates clips or AI highlights.
11. **Cross-channel collab game or duel** between two streamers' chats.
12. **Free loyalty XP or levels with badges on the overlay** (a Kick Level Up clone).

## B. Wide list

Format: pain → idea.

1. **Checkpoint** (`need #1, #6`). Messages pile up unseen during a boss fight → "focus mode" saves them; at the next checkpoint the streamer pages through them as on-stream call-in cards.
2. **Footnotes** (`need #3`). A newcomer sees "classic bean moment" and feels shut out → a mod-written lore glossary pops a footnote card when a term appears in chat.
3. **Previously On** (`need #3, raid`). Raiders land mid-fight with no context → mods drop "beats"; an incoming raid plays a 10-second TV-style recap.
4. **Tap on the Shoulder** (`need #1, #4, #9`). "Your mic is muted" goes unseen → mod cues and repeated viewer tech reports reach the streamer via desk lamp or headphone chime; the helper gets on-stream credit.
5. **Hint Jar** (`backseating`). Stuck on a blind run with a no-backseat rule → viewers seal hints (deleted from chat); the streamer opens the jar only when stuck, nudge first.
6. **Producer's Desk** (`need #4`). Mods can only use public `!scene` → a private phone panel to queue messages, fire lower-thirds, drop markers.
7. **Chat Sonar** (`need #1`). Can't look away from the game → message types become distinct earcons in the streamer's headphones only.
8. **Streamer's Lens** (`need #6`). Trivia answers flood the view → private dock with lenses (Questions, First-timers, Mentions, Mods).
9. **Welcome Mat with a guide** (`need #3`). A first message gets no reply → a regular on "welcome duty" is pinged to greet new chatters.
10. **Name Card** (`need #3`). Newcomers can't tell who's who → regulars set a one-line bio shown the first time they talk each stream.
11. **Answered Wall** (`need #1`). Short answers drive viewers away → an "answered tonight" ribbon credits each viewer who got a real answer.
12. **Lurker Lantern** (`lurkers`). Silent presence → `!lurk` lights a lantern on a skyline, no callouts. *Weak novelty.*
13. **Dead-Air Coach** (`need #9`). Long silences → OBS websocket detects 90 s of mic silence and nudges the streamer privately.
14. **Spoiler Airlock** (`moderation`). Story spoilers in chat → messages with spoiler terms are held until the chapter ends.
15. **Raid Baton** (`raid`). Raids are a cold handoff → the outgoing streamer's note shows on the target stream if both run the tool.
16. **Rewind Request** (`need #1, clips`). The streamer missed a funny moment → `!rewind` marks/clips it for a "replay review" at the next break.
17. **Shift Log** (`need #4`). Rotating mods on a marathon lack context → a private handoff log purged at 24 h.
18. **Commands Menu card** (`B2 N5`). Bot auto-messages annoy newcomers → a menu board appears on stream only when a new chatter arrives.
19. **Bilingual Bridge** (`need #3`). A newcomer writes in Turkish → the streamer's dock translates. Flag: chat text to a third party.
20. **VR Mirror** (`need #1`). VR streamers can't see chat → big-font triage page on a phone visible in passthrough. *Partly parked.*

## C. Five full cards

### Checkpoint
- **One-liner:** a save-point for chat. While the streamer is in a fight, every message is "saved". At the next checkpoint, the streamer pages through the saved messages on stream and answers each one.
- **Who installs it / who gets the value:** the streamer installs (bot, overlay, private dock). Streamer: focuses without guilt, then gets a ready list. Viewers: see their message on screen with their name, answered aloud; nothing lost to "sorry, missed that". Mods (optional): reorder or skip from the dock.
- **Streamer category fit:** action, story and competitive games, rhythm and music performance, art during a hard section, speedrun attempts. Anything with natural "break" moments.
- **Moment of pain:** a 0–10 viewer streamer, single monitor, on a 4-minute boss fight. Two viewers ask questions and one first-timer says hi. When the fight ends, chat has scrolled past or looks like 6 unread lines. The streamer gives a short answer or none, and the first-timer leaves. Evidence: #1 [V]; viewers leave after "very short closed answers" [V, B2]; first-chat viewers are 50% more likely to return [V, Twitch self-reported].
- **Core loop:**
  1. The streamer hits a hotkey (or a mod types `!focus`).
  2. A small corner badge appears: "🎧 Focus — messages saved: 0".
  3. Each viewer message drops a save-crystal into the badge with the viewer's color. Command spam and bot lines are filtered out.
  4. The streamer hits "checkpoint". A lower-third card shows the first saved message ("@ana_23 asked: what's your sens?"). The dock orders questions and first-timers first.
  5. The streamer answers aloud and hits "next". The card stamps ✓ and the next one slides in.
  6. At the end: "Checkpoint cleared — 4 answered".
- **First 10 seconds of the demo:** split screen. On the left, the streamer mid-fight. On the right, three test accounts typing. The save-crystals stack up in the corner. The fight ends, "CHECKPOINT" flashes, and the first viewer's message appears as a TV-style call-in card.
- **Twitch surfaces used:** EventSub `channel.chat.message`; Helix Send Chat Message (one "your messages are saved" line per focus stretch); Pinned Chat API to pin it (bonus, [U] on our channel); OBS browser source plus a custom browser dock.
- **Works with 1 streamer + 3 test accounts? How?** Yes, ideal. Three messages make a full checkpoint, each account gets its own on-screen moment. Latency does not matter: the card appears when the streamer speaks.
- **Closest existing thing and the meaningful difference:** StreamerQnA, YouTube Q&A mode and Chatterino highlights need a `!q` command or only filter the streamer's view. Checkpoint is time-boxed to the busy stretch, captures normal messages without commands, and makes the catch-up an on-stream ritual. Lurkers are never prompted. **Familiar base: AI "what did I miss" summarizer (crowd #2).** Twist: no summary; each message keeps its author and gets a real answer.
- **Why wouldn't 30 other teams build this?** Most "can't read chat" entries will reach for an LLM summary or TTS reader [I]. A queue sounds dull until framed as a save-point ritual. Some teams may build a Q&A queue, so framing and visuals must carry it.
- **Evidence it links to:** #1 [V, three sources]; #6 [V, one GitHub issue]; viewers leaving after closed answers [V, B2, one thread]; Twitch's first-chat retention claim [V, self-reported].
- **MVP scope / explicitly out of scope:**
  - **In:** focus toggle (hotkey page plus mod command), filter rules (commands, bots, emote-only), question and first-message-this-stream ordering, overlay badge and call-in card, dock with next/skip.
  - **Stretch:** an urgent lane that breaks through focus (see Tap on the Shoulder).
  - **Out:** auto-detecting fights from game video, LLM summaries, long-term history (everything is purged at stream end).
- **Riskiest assumption:** streamers will remember to toggle focus and then run the checkpoint, rather than skipping it. Mitigation: an auto-checkpoint reminder after N minutes, and focus can auto-start when no `!checkpoint` has run for 10 minutes [I].

### Footnotes
- **One-liner:** the channel's inside jokes get on-stream footnotes. When a lore term shows up in chat, a small numbered card explains it to whoever is new.
- **Who installs it / who gets the value:** the streamer installs. Mods and regulars: write lore (`!lore add bean = …`, mods approve). New viewers: get the joke. Streamer: keeps in-jokes without the clique effect; writing lore is fun in itself (#10).
- **Streamer category fit:** Just Chatting, variety, long-running community channels, VTubers (heavy lore), TTRPG campaigns (NPCs and running gags).
- **Moment of pain:** a new viewer's first 5 minutes. Chat writes "bean again 💀", the streamer laughs, and the newcomer feels like an outsider and closes the tab. Evidence: #3, a 169-point comment on "super alienating" close-knit chat [V].
- **Core loop:**
  1. A regular types "classic bean".
  2. The bot matches the glossary term (exact or alias, with a cooldown per term).
  3. A footnote slides in at the screen edge: "¹ **the bean**: Oct '25, Ana ate a raw coffee bean on stream and cried. *Lore by @mod_kay*".
  4. `!what bean` answers in chat for anyone.
  5. Optional rule: footnotes fire only when someone chatted for the first time this stream, so regulars do not see the same card every day.
- **First 10 seconds of the demo:** a regular types a meme and a "Pop-Up Video"-style footnote bubbles up. The test account playing "new viewer" types "ohhh LOL".
- **Twitch surfaces used:** EventSub `channel.chat.message`; Helix Send Chat Message (`!what`), Get Moderators; OBS overlay; Pinned Chat (bonus: "today's lore").
- **Works with 1 streamer + 3 test accounts? How?** Yes. One account is a mod who adds lore live on camera, one is a regular who uses the term, and one is a newcomer who asks.
- **Closest existing thing and the meaningful difference:** Nightbot custom commands (`!bean`) only answer someone who already knows to ask. Footnotes are triggered by the jokes themselves, aimed at newcomers, and shown with mod credit.
- **Why wouldn't 30 other teams build this?** It comes from a culture-specific pain that builders new to Twitch rarely see. It is not a game and has no AI angle [I].
- **Evidence it links to:** #3 [V, two sources]; #10 customization as a hobby [V]; B2 N5 "new viewer offended by auto messages" (why we use an overlay, not chat spam) [V].
- **MVP scope / explicitly out of scope:**
  - **In:** glossary CRUD via chat (mods) plus an approval queue, term and alias matching, cooldowns, footnote overlay, `!what`.
  - **Out:** detecting terms from the streamer's speech (STT), auto-discovering lore with an LLM, and a viewer-side hover tooltip (needs an Extension).
- **Riskiest assumption:** regulars will find the footnotes charming, not a buzzkill that explains the joke. Also unknown whether a mod-authored glossary counts as "Twitch content" under the 24 h rule. It is user-written in our app, so probably fine [U].

### Previously On
- **One-liner:** when raiders arrive, the stream plays a 10-second "Previously on…" recap built from beats the streamer and mods dropped during the stream.
- **Who installs it / who gets the value:** the streamer installs. Raiders and late joiners: context in 10 s. Streamer: no mid-fight re-explaining. Mods: become "story editors" via `!beat`.
- **Streamer category fit:** story games, challenge runs ("deathless attempt 14"), IRL trips, TTRPG sessions, building/crafting projects.
- **Moment of pain:** 15 raiders arrive in the middle of a fight. The streamer either ignores them (they leave) or breaks focus to recap awkwardly. Guides tell streamers to "introduce yourself and what you're doing" when raided [V, Streamlabs guide via search]. Korean ex-users value raids as social discovery [V].
- **Core loop:**
  1. During the stream, `!beat Beat the frog king on try 9` (streamer, mod, or a hotkey) saves a beat. It also creates a Helix stream marker; whether that works without Affiliate is [U], so it is a bonus.
  2. When `channel.raid` (incoming) fires, the overlay runs a TV-bumper animation: "Previously on Ana's Elden Ring…", 3 latest beats with timestamps, plus "Current goal: …".
  3. One welcome line goes to chat with `!recap`.
  4. Any newcomer can type `!recap` later.
- **First 10 seconds of the demo:** a test account's channel raids ours. The screen dims and a "PREVIOUSLY ON" title card sweeps in with three beats, like a TV recap. The raiding account types "ahh ok, frog king".
- **Twitch surfaces used:** EventSub `channel.raid`, `channel.chat.message`, `stream.online`; Helix Create Stream Marker (bonus), Send Chat Message; overlay.
- **Works with 1 streamer + 3 test accounts? How?** Yes. A test account goes live briefly and raids for real; Twitch CLI can probably mock `channel.raid` for rehearsal [I]. A 1–3 viewer raid is the small-channel reality.
- **Closest existing thing and the meaningful difference:** raid alerts and auto-shoutouts (Sidekick plays the raider's clips) welcome the *raider*. Previously On briefs the *raiders* on what they walked into. No existing tool found [V search, absence not proven].
- **Why wouldn't 30 other teams build this?** Raids are a Twitch-specific ritual that builders new to Twitch will treat as "just an alert" [I].
- **Evidence it links to:** #3 [V]; raids as social handoff [V]; Twitch's 2026 priority on discoverability (raids are the native discovery channel) [V].
- **MVP scope / explicitly out of scope:**
  - **In:** beats via chat and hotkey, recap overlay on raid plus a manual trigger, `!recap`, beats cleared after 24 h.
  - **Out:** auto-generating beats from chat spikes or an LLM (grey area, flag), clip playback inside the recap.
- **Riskiest assumption:** streamers and mods will actually drop beats during the stream. With no beats, the recap is empty. Fallback: auto-beats from stream title, category changes (`channel.update`) and `!beat` from viewers with mod approval [I].

### Tap on the Shoulder
- **One-liner:** a private "tap on the shoulder" for a streamer who cannot see chat. Mods and repeated viewer reports of tech problems reach the streamer through a desk lamp or a headphone chime, never through the stream itself.
- **Who installs it / who gets the value:** the streamer installs. Streamer: learns in seconds that the mic is muted. Mods: a private surface to reach the streamer (#4). Viewers: reporting a problem works, and the helper is credited.
- **Streamer category fit:** every category, and most valuable for single-monitor, VR, music and art streamers.
- **Moment of pain:** the streamer unmuted Discord but left the mic muted. For 12 minutes, three viewers type "no audio?", "mic??", "MIC". The streamer is in a full-screen game and sees none of it. Two viewers leave. Mods typing in chat or DMing on Discord fails for the same reason.
- **Core loop:**
  1. Inputs:
     - a mod taps a preset cue on a private phone page ("mic muted", "game too loud", "answer @x", free text);
     - ≥2 distinct viewers mention mic, audio, black screen or frozen within 60 s, or anyone types `!mic`;
     - an optional OBS websocket check: mic input silent for 90 s while live.
  2. Output: a streamer-only signal. A smart bulb or USB LED turns red, a chime plays on the OBS monitor-only channel, and the dock shows the cue in big text.
  3. The streamer fixes the problem and taps "resolved".
  4. The overlay shows a small credit: "🔧 Thanks @ana_23 for the heads-up".
- **First 10 seconds of the demo:** a close-up of a muted mic icon. Chat fills with "MIC??". A desk lamp behind the streamer turns red. The streamer winces and unmutes, and the on-stream credit pops. A physical, clip-able moment.
- **Twitch surfaces used:** EventSub `channel.chat.message`; Helix Get Moderators (mod OAuth login to the cue page), Send Chat Message; overlay; local lamp API (Hue/LIFX/Govee LAN) or a full-screen flash page on a spare device.
- **Works with 1 streamer + 3 test accounts? How?** Yes. One mod, two viewers reporting. Easy to script and believe.
- **Closest existing thing and the meaningful difference:** WooferBot and Streamer.bot light Hue on Twitch *events*; OBS mute indicators only help if you look at OBS. Tap on the Shoulder routes *human judgment* (mod cue, viewer report) through a channel that survives a full-screen game, and credits the helper.
- **Why wouldn't 30 other teams build this?** It solves a rare-but-painful moment, not a daily game, and hardware scares teams [I]. Past winners had physical outputs [V, description only].
- **Evidence it links to:** #1, #4, #9 (production quality is the top small-streamer complaint) [all V]; X post "can't get the chat overlay for the game, @friend will relay chat" [V]; B2 N3 "exactly one person can touch OBS" [V].
- **MVP scope / explicitly out of scope:**
  - **In:** mod cue page with presets, viewer-report detector (keyword list plus distinct-user threshold), one lamp integration plus a screen-flash fallback, headphone chime, credit overlay.
  - **Out:** mods controlling OBS scenes (the Producer's Desk direction, crowded), ML audio-quality analysis.
- **Riskiest assumption:** urgent moments happen often enough that a streamer keeps it installed. The mod-cue lane carries everyday value; the mute alarm is the hero moment. The builder also needs a controllable lamp; the fallback is a phone flash page [U, hardware on hand].

### Hint Jar
- **One-liner:** on blind playthroughs, viewers who know the answer seal hints into a jar instead of backseating. The streamer opens the jar only when stuck, and gets a nudge first, the solution last.
- **Who installs it / who gets the value:** the streamer installs. Streamer: stays blind, with a way out. Knowledgeable viewers: a legitimate role and credit. Other viewers: no spoilers. Mods: stop timing out well-meaning backseaters.
- **Streamer category fit:** blind story games, puzzle games, soulslikes, escape-room games, metroidvanias. "First blind playthrough" is a common small-streamer format [I].
- **Moment of pain:** stuck on a puzzle for 15 minutes on a "no backseating" channel. A viewer who knows the answer stays silent, frustrated, or posts it, gets timed out, and spoils it for everyone. Evidence: backseating rules are widespread and the main gameplay friction [S, B culture research].
- **Core loop:**
  1. A viewer types `!hint nudge <text>` or `!hint full <text>`.
  2. The bot (a moderator) deletes the message from public chat and seals it in the jar.
  3. The overlay jar fills with envelopes; "4 hints waiting" is visible but the content is hidden.
  4. The streamer says "okay, I give up" and hits a hotkey. The jar tips and reveals the first nudge with its author.
  5. If still stuck, the streamer pulls the next tier.
  6. If solved, the card stamps "@ana_23 saved the run ⭐".
- **First 10 seconds of the demo:** the streamer is visibly stuck. Envelopes drop into a glass jar on screen as viewers type. The streamer sighs, slams the hotkey, and the jar cracks open with a nudge.
- **Twitch surfaces used:** EventSub `channel.chat.message`; Helix Delete Chat Messages (bot must be a moderator; scope `moderator:manage:chat_messages` [I]), Send Chat Message ("hint sealed ✓", rate-limited); overlay.
- **Works with 1 streamer + 3 test accounts? How?** Yes. Two accounts submit nudge and full hints and one asks "is there a hint?". The jar reads fine with 2–3 envelopes.
- **Closest existing thing and the meaningful difference:** LeagueBackseat queues backseat messages for later review [V exists]. Hint Jar hides them from other viewers, gates them on the streamer's request, tiers them, and makes the reveal a show. Not from the crowd map.
- **Why wouldn't 30 other teams build this?** Backseating is an insider norm. Outsiders think in terms of "chat controls the game", the opposite direction [I].
- **Evidence it links to:** unvalidated as tool demand. To validate: search Reddit for "backseat"/"backseating" posts by small streamers (B2's Arctic Shift method), and check whether hint-request commands appear in community bots.
- **MVP scope / explicitly out of scope:**
  - **In:** `!hint` with two tiers, sealed delete, jar overlay, reveal hotkey, credit card.
  - **Out:** auto-detecting the stuck state, LLM spoiler detection, persistent helper leaderboards beyond 24 h.
- **Riskiest assumption:** the delete-and-seal step feels good, not like censorship. Latency is harmless because puzzles last minutes [I].

## D. Parked

- **Cross-stream "Helper" level** from Hint Jar / Tap credits. Breaks 24 h storage. Needs: derived per-user counters ruled allowed.
- **Checkpoint "skip the line" channel-point reward.** Needs custom rewards. Needs: Day 1 test passes on a non-Affiliate channel.
- **Footnotes as viewer-side hover tooltips.** Needs an Extension. Needs: >14 days for review.
- **VR chat mirror inside the headset.** Needs a SteamVR overlay app. Needs: more time and VR hardware.
- **Footnotes triggered by the streamer's speech (STT).** Over budget. Needs: a reusable Whisper pipeline.
- **First-ever-chatter detection across streams.** Needs long-lived history. Needs: user IDs/first-seen ruled fine, or EventSub `user_intro` covering it [U].

## E. My pick

**Checkpoint.** It sits on the best-evidenced need (#1, three independent sources) and fixes the quiet harm behind "dead chat": not that viewers don't talk, but that the few who do get missed or brushed off. It never asks lurkers to speak. It is built for tiny channels (three messages make a full checkpoint, each test account gets its own on-screen moment) and tolerates latency, because the card appears when the streamer speaks. The save-point framing turns a dull queue into something gamers recognize instantly, which carries Design. Chat + EventSub + overlay only, ~10 hours. Natural stretch: Tap on the Shoulder's urgent lane (a muted mic breaking through focus, plus a desk lamp) as a physical, clip-able second act in the video.
