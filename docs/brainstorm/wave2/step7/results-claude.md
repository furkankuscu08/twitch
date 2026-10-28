## Scores
| Card | Innovation | Impact | Tech | Design | Total | Risk | Risk depends on |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Raid Torch | 4 | 2 | 3 | 3 | 12 | High | T3: a second live channel and a real raid between them, with the raid event arriving within 5 s; also a free-PaaS deploy working on demo day |
| Minefield | 5 | 3 | 4 | 5 | 17 | Medium | T1: ≥80% hits, ≤1 false alarm per 10 min, ≤3 s lag on casual speech; T4 plant page behind a public URL; T5 marker and titled clip |
| Checkpoint | 4 | 4 | 4 | 4 | 16 | Medium | T1b: quote ready ≤2 s after the streamer stops and ≥9/10 readable; the 2 s silence rule not closing cards on thinking pauses |
| VAR | 3 | 3 | 4 | 5 | 15 | Medium | T2: replay buffer saved and Media Source slow motion on screen ≤5 s; latency offset landing on the moment; T5 titled clip window |
| Hint Jar | 4 | 3 | 3 | 4 | 14 | Low | T4: one sealed-intake path (login page behind a public URL) works end to end; the Codex-built puzzle feeling like a real first playthrough |
| Tap on the Shoulder | 3 | 3 | 3 | 4 | 13 | Low | T2: obs-websocket mute event arrives (and silence detection from volume levels); phone page over HTTPS with Wake Lock |
| Studio Audience | 3 | 3 | 3 | 3 | 12 | Low | No MVP test; T5 Get Chatters only for the lurker-seat stretch |

## Reasons
### Raid Torch
- Innovation (4): No researcher found a visible object with per-chatter marks carried from channel to channel by raid; raid-train tools (R3dLabs, RaidRunner, RaidPort) handle scheduling and the raid itself, and A only rates the difference "partly".
- Impact (2): Raid trains are an active practice, but no one has asked for a carried object or named raiders, value needs both channels to adopt it, and hate-raid wariness and raiders leaving quickly cut against it.
- Tech (3): A hosted backend with cross-channel state is more interesting than a local overlay and the Codex artifact (backend + deploy + journey page) is concrete, but the MVP uses the full 9.5 h and depends on a second live channel.
- Design (3): The torch fly-in is a clear visual hook, but the evidence says a real multi-community relay can't be shown with one streamer, so two of our own channels plus "rehearsal hops" will look staged.
- Risk (High): T3 needs a second live channel (phone or second OBS) and a real raid with its 90 s countdown, and the event must arrive within 5 s; the multi-hop journey is partly rehearsal by design.
- Biggest weakness: The whole point is a community relay, and the demo can only show one person raiding themselves.

### Minefield
- Innovation (5): All three researchers and the link check agree the loop survives: every speech trigger found (OK Gamers, Streamer.bot Voice Control, swear jars) uses words the streamer chose, and every viewer-chosen secret-word game runs in typed chat.
- Impact (3): It fits any talking stream (Just Chatting 14.2%, IRL 1.8%, talkative game streams), but demand is only indirect (manual swear jars, bingo cards, unverified Reddit asks) and the fun is unvalidated.
- Tech (4): Local faster-whisper keyword spotting with hotwords, VAD and whole-word matching is technically interesting and fits 9.5 h, and the accuracy harness is a concrete, showable Codex artifact; T1's false-alarm bar is the risk.
- Design (5): "pineapple on pizza is—" BOOM with the planter's name is understood in seconds and works with three accounts, and DEFUSE turns a misheard word into a gag instead of a failure.
- Risk (Medium): T1 must hit ≥80% with ≤1 false alarm per 10 min on casual speech; DEFUSE and the blocklist soften misfires, and the plant page (T4) is a standard login page behind a public URL.
- Biggest weakness: There is no listed fallback if speech-to-text keyword spotting fails T1; the card's core loop depends entirely on it.

### Checkpoint
- Innovation (4): Source P found no tool that listens to the streamer's answer and sends the actual words back as a threaded reply, but the call-in card half is Meld's well-known question queue and the post-pivot difference rests on one source.
- Impact (4): The problem is evidenced (Streamlabs guide on manual chat breaks, art streamers missing messages, Twitch building Chat History) and heads-down formats (art, making, coding, focused gameplay) would use it every stream; much demand evidence is unverified.
- Tech (4): Voice segmenting, live partial transcripts, a silence close with a hold key, a confidence gate and threaded replies with `drop_reason` handling fit in 9 h with a 1 h margin, and the voice-to-receipt pipeline tested on recorded audio is a concrete Codex role.
- Design (4): The hook resolves by 0:19 with words typing onto the card and a split screen of Ana's threaded quote, but a lower-third card and a chat reply are calmer to watch than an explosion or a replay.
- Risk (Medium): T1b needs the quote ready within 2 s and 9 of 10 readable; a fallback (pause trigger) and a plain-receipt confidence gate exist, so a failure degrades the demo rather than breaking it.
- Biggest weakness: Without the voice receipt it is Meld's question queue, so the novelty depends on speech-to-text working well on the day.

### VAR
- Innovation (3): Chat-called replays (tomaae, BarRaider, Fyre), branded slow-motion replays (Glitch Studios) and chat votes all exist; only the full ritual (call threshold, replay, jury, verdict, titled clip) is new, and it is visible in the video.
- Impact (3): It fits competitive games and desk challenges, but the only evidence is a historic 12.6k-download replay script, there are no requests for a chat jury, and a streamer wanted control over when replays interrupt play.
- Tech (4): Replay buffer, Media Source slow motion via obs-websocket and a latency offset with a nudge-back hotkey are technically interesting and fit 8.5 h, and the replay pipeline plus simulator-driven threshold tests is a concrete Codex artifact.
- Design (5): Everyone knows VAR, so "IN!", two `!var`, siren, slow motion off the rim and a "NO BASKET" stamp read in seconds and are fun with three accounts; the self-VAR beat adds a second laugh.
- Risk (Medium): T2 must show the replay within 5 s, and the latency offset must land on the right moment; the 60 s clip may lose the original moment (the replay inside the review still shows it).
- Biggest weakness: It is a well-staged combination of existing replay and poll tools, so a judge may read it as polish rather than a new idea.

### Hint Jar
- Innovation (4): The link check found no Twitch tool with private submission, sealed tiered hints and a streamer-controlled reveal one tier at a time; queued backseat messages (LeagueBackseat) and offline tiered hints exist, and A calls the difference "narrow".
- Impact (3): Backseating complaints are real (Limbus thread, "no backseating" titles), but most replies say rules and bans fix it, some streamers want no hints at all, and the audience is first playthroughs of puzzle-style games.
- Tech (3): Hint page, mod dock, jar overlay and reveal hotkey are buildable in 8.5 h but ordinary web plumbing; the Codex-built puzzle game is a concrete artifact but not technically deep.
- Design (4): The backseat line turned into "seal it instead: !hint", and one nudge opening while the answer stays visibly sealed, are understood quickly; it depends on the original puzzle feeling like a real playthrough.
- Risk (Low): T4 only needs one path to work, and a login page behind a public URL is standard; the main demo risk is the puzzle looking staged.
- Biggest weakness: The evidence says rules and timeouts already solve backseating for most streamers, so the problem may be smaller than the card assumes.

### Tap on the Shoulder
- Innovation (3): Each part exists alone (Muted Notification, Remember to Talk, Twitch Guardian, reactive mascots); the new combination is viewer and mod reports cross-checked against OBS, delivered in the room and closed by chat confirmation.
- Impact (3): The problem is strongly evidenced (Snoop Dogg with no audio for an hour, the OBS forum request) and fits every type of stream, but real failures are rare, well-known plugins already cover the mute case, and calm mode, which would make it a weekly tool, is a stretch goal.
- Tech (3): Report detector, phone page over HTTPS with Wake Lock and pairing, obs-websocket mute/silence and a delay-aware confirm loop fit 9 h, but it is mostly integration rather than a technically interesting core.
- Design (4): A phone face panicking in the camera shot is easy to read and physical, and the "OBS can see this one… but not this one" hook makes the difference visible within 30 s.
- Risk (Low): T2's mute event is a standard obs-websocket event and silence comes from volume levels; HTTPS for Wake Lock on the phone is the fiddliest part.
- Biggest weakness: The trigger it is built for (a production failure chat notices) rarely happens, so the tool is idle most of the time unless the calm-mode stretch ships.

### Studio Audience
- Innovation (3): Sound Alerts, walk-on sounds and chat-scaled visuals exist, and G notes per-viewer sounds already tie a noise to a viewer; one mixed crowd scaled by distinct reactors, with signature laughs and chants, is a new combination.
- Impact (3): Sound features are widely used and streaming to a silent chat is demoralising, but sound-spam complaints, "canned laughter" perception and delight fading after 10 minutes limit weekly use.
- Tech (3): A Web Audio mixer with distinct-viewer scaling and per-ID signature laughs is buildable and low-risk in 9 h, but ordinary; the Codex artifact is concrete.
- Design (3): The boo-then-laugh hook is understandable, but three accounts make at most three voices, so the core idea (loudness follows the number of real reactors) can only be shown with a labeled simulation.
- Risk (Low): Nothing in the MVP needs a day-1 test; T5 Get Chatters only matters for the lurker-seat stretch.
- Biggest weakness: Its main claim, a crowd that grows with real reactors, cannot be shown with three test accounts.

## Ranking
1. Minefield: The most novel loop in the set (viewers secretly choose the words, the streamer's speech sets them off) with a hook that lands in seconds; it depends on T1.
2. Checkpoint: It solves a well-evidenced problem for heads-down streamers every stream, and the spoken answer arriving as a threaded quote is new and shows clearly in the video.
3. VAR: The most fun to watch and the strongest technically on video, held back by being a combination of replay and poll tools that already exist.
4. Hint Jar: A neat, low-risk answer to backseating with a clear difference, but a narrow audience and an ordinary build.
5. Tap on the Shoulder: Well-evidenced and type-independent, with a nice physical signal, but the events are rare and much of it overlaps existing mute plugins.
6. Raid Torch: A genuinely new cross-channel idea, but adoption needs both sides and the demo can't show a real community relay with one streamer.
7. Studio Audience: Pleasant and low-risk, but the distinct-reactor scaling it depends on can't be shown with three accounts, and sound-spam and canned-laughter concerns weigh on it.
