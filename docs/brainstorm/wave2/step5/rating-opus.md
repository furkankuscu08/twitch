# Rating: opus

**1. Scores.**

| ID | Name | Innovation | Impact | Technical | Design | Total | One-line reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R01 | Tiered hints | 4 | 3 | 3 | 4 | 14 | Sealed, graded hints turn backseating into help, which is rare. The envelope jar reads well on screen, but it is only useful to puzzle and blind-playthrough streamers. |
| R02 | Focus capture, surfaced at a break | 3 | 4 | 3 | 3 | 13 | Solves a real "I missed chat while busy" pain without a summary. It sits close to Q&A queues and "what did I miss" tools. |
| R03 | Per-viewer souvenir moment | 3 | 3 | 3 | 4 | 13 | The Polaroid flash-and-develop is charming and easy to read. Underneath it is a chat-to-overlay command with a screenshot. |
| R04 | "You are here" context for late arrivals and raiders | 4 | 4 | 4 | 4 | 16 | Briefing raiders instead of only greeting them is a fresh angle on a constant problem. It uses raid EventSub, markers, the title and clips together. |
| R05 | Chat reactions amplified | 3 | 4 | 3 | 5 | 15 | Making three viewers sound like a packed theater speaks directly to small streamers. It works instantly on video, though soundboards are a crowded space. |
| R06 | Something travels with the raid | 5 | 3 | 3 | 4 | 15 | Carrying state between channels through a raid is genuinely new, but it is only valuable once both channels adopt it. |
| R07 | Bookmark a moment for later | 2 | 2 | 2 | 2 | 8 | It is close to stream markers and clip requests, with a weak on-stream moment and occasional use. |
| R08 | Newcomer welcome and orientation | 2 | 3 | 2 | 2 | 9 | First-chatter handling already exists natively and in Streamer.bot. The regular-bio twist is small. |
| R09 | Sealed predictions | 1 | 2 | 2 | 3 | 8 | This is native Predictions with hidden guesses: a crowd idea with a cosmetic twist. |
| R10 | Viewer voicemail call-in | 3 | 3 | 3 | 4 | 13 | Hearing a real viewer voice on a retro phone is warm and fun. Approval and moderation add friction, and it is close to TTS and Discord call-ins. |
| R11 | Viewers write the brief, the streamer performs it | 5 | 2 | 2 | 4 | 13 | Live foley from viewer cues is memorable and unlike anything else. The tech is thin, and it is a performer-dependent, occasional segment. |
| R12 | Chat-called replay review | 4 | 3 | 4 | 5 | 16 | The VAR stinger, slow motion, jury and verdict stamp is a replayable moment built on the replay buffer and clips. It is a segment, not a daily tool. |
| R13 | Lore footnotes | 4 | 3 | 3 | 4 | 14 | Footnotes that explain inside jokes to newcomers are a clever, readable framing. Small channels have limited lore to fill them. |
| R14 | Maker continuity check | 3 | 2 | 2 | 2 | 9 | It is a niche maker workflow that looks like a checklist on video. |
| R15 | Glanceable chat state in the room | 3 | 3 | 4 | 4 | 14 | A physical chat face in the camera shot is a nice twist. It still sits near chat pets and the Elgato Prompter. |
| R16 | Lurker presence made visible | 3 | 2 | 2 | 3 | 10 | It is a pleasant ambient visual, but on a tiny channel it is just a few dim dots with little to do. |
| R17 | Spoiler-hold filter | 2 | 3 | 2 | 1 | 8 | It is AutoMod-adjacent, and it lives in the streamer's private view, so viewers see almost nothing. |
| R18 | Raid lands at a bad moment | 1 | 2 | 2 | 2 | 7 | It is a persistent raid alert plus the shoutout API: a rare situation and a crowd-tool tweak. |
| R19 | Viewer plants it, the streamer sets it off | 5 | 4 | 5 | 5 | 19 | Secret word mines plus speech-to-text is a fresh game with a guaranteed BOOM moment. It combines whispers, local STT, the overlay and clips. |
| R20 | Production problems reach the streamer | 4 | 5 | 4 | 3 | 16 | The muted-mic problem is universally felt, and the crowd-triggered private alert is smart. Most of the signal is off-stream by design. |

**2. Top 5.**

- **R19: Viewer plants it, the streamer sets it off (19).**
  - Why it would win: The concept is new, it is easy to explain, and the demo has a built-in punchline: the BOOM, the planter's name, and a cut back to their bait question. It also has real technical substance (local STT, sealed input, auto-clip) and is a segment communities would ask for again.
  - Weakest criterion: Impact (4). It is a game segment rather than an always-on tool, and STT misses could dull it.
- **R20: Production problems reach the streamer (16).**
  - Why it would win: Every streamer has played to a muted mic, so judges will nod instantly. Aggregating chat reports into a private, fullscreen-proof signal is a clear improvement over existing tools.
  - Weakest criterion: Design (3). By design it shows little on stream beyond a red lamp and a thank-you credit.
- **R04: "You are here" context for late arrivals and raiders (16).**
  - Why it would win: The "Previously on..." card is instantly readable and solves a problem every channel has. It uses several Twitch surfaces (raid EventSub, markers, title, clips).
  - Weakest criterion: Balanced across all four. The real risk is that judges read it as a fancy raid alert, and its value depends on someone logging beats.
- **R12: Chat-called replay review (16).**
  - Why it would win: VAR is a universally understood format, and slow motion plus a jury bench plus a verdict stamp is the most replayable video moment in the pool. Wiring the replay buffer, the vote and clip creation is solid, demonstrable engineering.
  - Weakest criterion: Impact (3). It only matters when there is something disputable to review.
- **R06: Something travels with the raid (15).**
  - Why it would win: No existing tool carries anything between channels during a raid, so judges would remember this. The torch arriving with emote rings is a nice visual.
  - Weakest criterion: Impact (3). It needs both channels to run it, and the demo is harder to make convincing with one real streamer.

**3. Bottom 5.**

- **R18 (7):** This is a persistent raid alert plus the shoutout API, for a situation that rarely happens.
- **R09 (8):** This is Twitch Predictions without the points; judges will see it as a crowd idea.
- **R07 (8):** Stream markers and clip requests already cover this, and the encore list makes a dull video.
- **R17 (8):** This is mostly AutoMod-style filtering into a private drawer, so there is almost nothing for viewers or judges to watch.
- **R08 (9):** First-time-chatter highlights already exist natively and in Streamer.bot, so the twist is too small to stand out.

**4. Notes.**

- **R09 and R19 overlap:** Both use the same mechanic: sealed whisper or web-form input shown as named, hidden tokens. R19 is the far stronger use of it. R01 also shares the sealed-whisper intake.
- **R01 and R17 overlap:** Both target backseating. R01 channels it into help; R17 filters it out.
- **R17 factual point:** A tool cannot hide lines from the streamer's native Twitch chat. It only works if the streamer reads a custom chat view, which weakens the claim.
- **R16 factual point:** The Get Chatters endpoint needs a moderator token. It lists logged-in accounts connected to chat, including bots, so "lurkers" will include bot accounts unless they are filtered out.
- **R04 factual point:** I am not confident that a public Helix endpoint for pinning chat messages exists. The pin variant may not be buildable.
- **R12 factual point:** Twitch's Create Clip API clips from Twitch's own buffer, not the local OBS replay. Setting a clip title through the API may not be supported.
- **R06 factual point:** I cannot confirm the exact "24 h retention" wording in the Developer Agreement. Keeping journeys to the same day is a safe interpretation anyway.
