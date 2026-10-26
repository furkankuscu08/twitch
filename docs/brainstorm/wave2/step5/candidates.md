# Scoring: candidates

20 candidates, in random order. Each has the same fields. "Notes" are feasibility notes; they are tested separately.

## R01: Tiered hints

- **What it is:** On blind playthroughs or puzzles, viewers who know the answer submit hints at a strength (nudge / method / answer) instead of backseating. Hints are sealed: sent by whisper or a small web form into a private queue (optionally mod-approved), so they never appear in public chat. An overlay jar fills with envelopes. When stuck, the streamer opens only the level they want, and the helper gets credit.
- **First 10 seconds of the demo:** The streamer is stuck on a puzzle; envelopes drop into a jar; the streamer sighs, hits a key, and a nudge appears while the answer stays sealed.
- **Closest existing things:** No-backseating rules, backseat queues (LeagueBackseat).
- **Notes:** The demo would use our own puzzle, not a commercial game.

## R02: Focus capture, surfaced at a break

- **What it is:** Before a busy stretch (a hard level, a tricky drawing section) the streamer hits a hotkey. Every normal chat message is held (commands and bot lines filtered out) and shown as a growing pile of colored "save crystals" in a corner. At the next break the streamer hits "checkpoint" and pages through the held messages as on-stream call-in cards, answering each aloud; first-time chatters come first. Variant: a moderator collects one question, one contribution and one announcement for the streamer's return.
- **First 10 seconds of the demo:** Crystals stack up while the streamer is busy; "CHECKPOINT" flashes and the first viewer's message appears as a TV-style call-in card.
- **Closest existing things:** Q&A queues, chat highlight tools, AI "what did I miss" summaries. Claimed difference: no command needed, no summary, every message keeps its author.
- **Notes:** none

## R03: Per-viewer souvenir moment

- **What it is:** A viewer types `!snap <caption>`. The streamer hears a cue and poses, the overlay counts down, a flash fires, and a Polaroid of the moment develops on screen with the viewer's name and caption; the viewer gets a link to save it (expires in 24 h). At stream end all snaps form a "who was here today" collage. Variants: a numbered ticket stub per attendee; an end-of-stream "museum" crediting viewer contributions.
- **First 10 seconds of the demo:** A viewer types `!snap first win`; the streamer holds up a mug; a flash; a Polaroid develops in the corner.
- **Closest existing things:** Generic chat-to-overlay commands, physical subscriber-slip printers.
- **Notes:** Image links need public hosting.

## R04: "You are here" context for late arrivals and raiders

- **What it is:** During the stream the streamer or mods drop short beats or chapter titles ("beat the frog king on try 9"). When a raid arrives, or on request, the stream shows a 10-second TV-style "Previously on…" card with the last three beats. Variant: each new chapter is pinned at the top of native Twitch chat, creates a stream marker, updates the stream title, and saves a clip of the last 90 s.
- **First 10 seconds of the demo:** A raid lands; the screen dims and a "PREVIOUSLY ON" card sweeps in with three beats; a raider types "ahh ok, frog king".
- **Closest existing things:** Raid alerts and auto-shoutouts (they welcome the raider, they don't brief the raiders), a hand-pinned "today's plan" message.
- **Notes:** A real raid needs a second live channel; the pin variant depends on an API untested on a new channel.

## R05: Chat reactions amplified

- **What it is:** Chat emotes and keywords become a live theater-crowd soundscape (laughs, gasps, boos, applause). Intensity scales with the number of distinct viewers reacting, so three viewers sound like a full house. Each viewer has a recognizable signature laugh and a bouncing seat silhouette with their name. A headphone-only mode lets the streamer hear chat without reading it.
- **First 10 seconds of the demo:** The streamer misses a paper-ball shot; one viewer types "L", two type "LUL"; a packed theater boos, then laughs, and three named silhouettes bounce.
- **Closest existing things:** Sound Alerts (paid soundboard), per-user entrance sounds, visual emote walls.
- **Notes:** none

## R06: Something travels with the raid

- **What it is:** When a channel raids another, something travels with the raid and appears on the target stream: a one-line note from the outgoing streamer or co-written by chat ("we just finished a pie"), or a digital torch that collects an emote mark from every chat that held it and arrives showing its journey. Both channels run the tool.
- **First 10 seconds of the demo:** Channel A's torch glows with emote rings; raid; on channel B the torch flies in with its rings and raiders type "we brought that!".
- **Closest existing things:** Raid alerts, raid trains (no state carried between channels).
- **Notes:** Needs a second live channel; only same-day journeys are allowed because the Twitch Developer Agreement forbids keeping Twitch data longer than 24 h.

## R07: Bookmark a moment for later

- **What it is:** A viewer bookmarks something to revisit: "show that brush again", `!rewind` on a funny moment, or a promise the streamer made ("I'll show you later"). The streamer gets a short list at a break or at the end and picks one for a deliberate encore or replay, crediting the viewer.
- **First 10 seconds of the demo:** During a drawing a viewer types `!encore brush`; at the end the streamer opens the encore list and redoes the stroke slowly while the viewer's name shows.
- **Closest existing things:** Stream markers, clip requests in chat, mod notes.
- **Notes:** none

## R08: Newcomer welcome and orientation

- **What it is:** When someone chats for the first time this stream, the channel orients them without a public spotlight: a regular on "welcome duty" is pinged to say hi, or a small menu card appears on stream only then, or regulars' self-written one-line bios appear the first time they talk so newcomers know who's who. Variant: a thermal printer prints each first-time chatter's name and the streamer pins it on a real wall.
- **First 10 seconds of the demo:** A new account says hi; a small card introduces the regular who answers ("@kay: mod, makes the bad puns"); the newcomer replies.
- **Closest existing things:** First-chatter alerts in Streamlabs and Streamer.bot, Twitch's own first-time-chatter highlight.
- **Notes:** none

## R09: Sealed predictions

- **What it is:** Before an outcome, viewers send their guess by whisper to the bot or through a small web form, so no one can see or copy it; the overlay shows named sealed envelopes; at the reveal they all open together.
- **First 10 seconds of the demo:** Three named envelopes on screen; the outcome happens; they flip open showing who called it.
- **Closest existing things:** Twitch Predictions (channel points), chat guessing games.
- **Notes:** none

## R10: Viewer voicemail call-in

- **What it is:** Viewers leave 15-second voice messages on a web page; a mod approves them; the streamer airs them during a break with a retro phone overlay and answers.
- **First 10 seconds of the demo:** A ringing-phone overlay; a viewer's recorded voice plays; the streamer answers live.
- **Closest existing things:** Paid text-to-speech messages, call-in segments over Discord.
- **Notes:** Needs recording consent and mod approval before airing.

## R11: Viewers write the brief, the streamer performs it

- **What it is:** The streamer opens a short scene ("a tiny detective enters a storm"). Three viewers each claim a role (weather, footsteps, surprise) and pick a cue; the score fills in on screen; the streamer then performs the sounds live with desk objects (paper, cup, spoon) as the overlay advances. Variants: viewers assign fictional identities to three real props for an improvised scene; viewers propose tiny experiments the streamer predicts and then performs.
- **First 10 seconds of the demo:** The brief and three viewer cues appear; the streamer crinkles paper for rain and produces an absurd thunderclap with a cup.
- **Closest existing things:** Viewer-triggered sound effects (playback, not performance), improv games.
- **Notes:** none

## R12: Chat-called replay review

- **What it is:** When viewers dispute a moment, two of them type `!var`. A "VAR CHECK" stinger plays, the last ~20 s replay from the local replay buffer with the final seconds in slow motion, chat votes yes/no for 20 s with names on a jury bench, a verdict stamp lands, and a titled clip is created.
- **First 10 seconds of the demo:** The streamer throws a paper ball: "IN!"; two viewers call VAR; slow motion shows it bouncing off the rim; the jury votes; "NO BASKET".
- **Closest existing things:** An OBS instant-replay script triggered by chat, native polls.
- **Notes:** none

## R13: Lore footnotes

- **What it is:** Moderators keep a small glossary of the channel's inside jokes in a web panel. When a term appears in chat, a small numbered footnote card slides into a corner of the stream explaining it, credited to the lore author, with a cooldown per term. Variant: footnotes appear only on request (`!why <term>`) without showing who asked.
- **First 10 seconds of the demo:** A regular types "bean moment again"; a footnote pops up ("1 the bean: ate a raw coffee bean on stream and cried"); the newcomer account types "ohhh lol".
- **Closest existing things:** Bot custom commands (`!bean`) that answer only people who already know to ask; channel About panels.
- **Notes:** none

## R14: Maker continuity check

- **What it is:** A maker streamer declares a checkable step ("Stage C: both wings get two blue dots"). Viewers submit observations tagged to that stage (`!mark C left wing has one`); a mod approves; at a planned checkpoint the streamer opens a small checklist, fixes or dismisses each, and stamps the stage complete.
- **First 10 seconds of the demo:** A paper creature with mismatched wings; at the checkpoint one viewer observation appears; the streamer adds the missing dot and stamps "Stage C complete".
- **Closest existing things:** Checklists, backseating in chat, mod relays.
- **Notes:** none

## R15: Glanceable chat state in the room

- **What it is:** A spare phone propped on the desk shows a cartoon face that represents chat: it waves and shows a new chatter's name in huge letters, raises a hand with a counter when a question is waiting, changes expression with emote mood, and dozes when chat is quiet. One tap shows the waiting question. It sits in the camera shot, so viewers see their message move an object in the room. Variants: a smart bulb that takes the chatter's color; distinct headphone sounds per message type.
- **First 10 seconds of the demo:** The streamer is drawing; a test account types "hi, first time here"; the phone waves and shows the name; the streamer greets them without putting the pen down.
- **Closest existing things:** On-screen chat pets (Elgato Mochi), Elgato Prompter chat mode, Lumia Stream light effects, reading chat on a propped phone.
- **Notes:** none

## R16: Lurker presence made visible

- **What it is:** Silent viewers appear as dim lanterns or stars on a small skyline overlay, built from the list of logged-in accounts connected to chat (logged-out viewers are invisible to Twitch tools), with no names and no prompt to speak. A viewer's first message makes their light flare. `!lurk` lets someone say "I'm here, don't wait for me".
- **First 10 seconds of the demo:** Five dim lights on a skyline; one viewer types; a light flares.
- **Closest existing things:** Lurk commands, viewer counters.
- **Notes:** none

## R17: Spoiler-hold filter

- **What it is:** While a story section is on, chat lines that look like spoilers or directions are held out of the streamer's own chat view in a drawer that the streamer opens after the section.
- **First 10 seconds of the demo:** A viewer types "the key is behind the painting"; it slides into a "held" drawer; after the chapter the streamer opens it.
- **Closest existing things:** AutoMod and blocked terms, no-spoiler rules.
- **Notes:** none

## R18: Raid lands at a bad moment

- **What it is:** If a raid lands while the streamer is on a BRB or starting-soon screen, the raider's name stays on screen and the streamer gets a reminder until they tap "thanks", which also sends the official shoutout. Variant: the scene switches automatically to a live welcome.
- **First 10 seconds of the demo:** BRB screen; a raid arrives; a persistent "Raid from X: thank them!" card; the streamer returns, taps, and the shoutout fires.
- **Closest existing things:** Raid alerts, auto-shoutout bots.
- **Notes:** A real raid needs a second live channel.

## R19: Viewer plants it, the streamer sets it off

- **What it is:** Viewers secretly plant word mines by whispering the bot or using a small web form (`pineapple`), so no one else sees the word. The overlay shows the mines with owners' names, never the words. Viewers steer the conversation toward their word. When the streamer says it, local speech-to-text catches it: explosion, the planter's name, and an auto-titled clip. Variants: viewers attach sound effects to the streamer's catchphrases; webcam smile detection in a "try not to laugh" round.
- **First 10 seconds of the demo:** Three mines live; the streamer says "honestly, pineapple on pizza is—" BOOM; a banner names the planter; cut to that viewer's bait question from minutes earlier.
- **Closest existing things:** Speech-recognition swear jars, the party game Taboo.
- **Notes:** Depends on speech-to-text accuracy on casual speech.

## R20: Production problems reach the streamer

- **What it is:** When the stream has a problem the streamer can't notice (mic muted, game too loud, hand covering the camera), viewer reports and moderator cues reach the streamer through a private channel that works over a fullscreen game: a desk lamp turns red, a headphone-only chime plays, the dock shows the issue in big text. Trigger: two or more viewers mention "mic/audio" within 60 s, or a mod taps a preset. The helper gets an on-stream thank-you. Variant: a repair-and-confirm loop where the streamer says "Test B" after a fix and viewers reply `!heard B good` or `!heard B quiet`.
- **First 10 seconds of the demo:** Close-up of a muted mic; chat fills with "MIC??"; a lamp behind the streamer turns red; the streamer winces, unmutes, and a thank-you credit pops.
- **Closest existing things:** Smart lights on Twitch events (WooferBot, Streamer.bot), OBS mute indicators, a friend relaying chat.
- **Notes:** Lamp is optional (a phone-flash fallback exists).
