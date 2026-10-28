## Scores
| Card | Innovation | Impact | Tech | Design | Total | Risk | Risk depends on |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Hint Jar | 4 | 3 | 4 | 5 | 16 | Low | T4: private submission through the public login page; correct tier isolation on reveal |
| VAR | 3 | 3 | 4 | 5 | 15 | Medium | T2: correctly timed replay within 5 s; T5: the resulting clip contains the review |
| Studio Audience | 3 | 3 | 4 | 4 | 14 | Low | Three-account audio test: distinct voices, spam-resistant scaling and headphone routing |
| Raid Torch | 4 | 3 | 3 | 3 | 13 | High | T3: a real raid between two live channels, followed by correct torch and mark transfer |
| Minefield | 5 | 3 | 3 | 5 | 16 | High | T1: hit rate, false alarms and lag; T4: sealed planting; three-person playtest |
| Checkpoint | 4 | 4 | 3 | 4 | 15 | High | T1b: readable quotes within 2 s; answer-boundary and threaded-reply tests |
| Tap on the Shoulder | 3 | 4 | 4 | 4 | 15 | Medium | T2: mute and silence signals; phone pairing, headphone-only chime and delayed confirmation |

## Reasons
### Hint Jar
- Innovation (4): Sealed submission, tier selection and streamer-controlled reveal create a visible difference from LeagueBackseat and permission-based backseating. Existing tiered hints and queued help keep it short of an entirely new interaction.
- Impact (3): The verified complaints and gentle-nudge guide support a real problem for first playthroughs. However, rules and bans already satisfy many streamers, and others want no hints at all.
- Tech (4): The 8.5-hour MVP plus shared base leaves three hours of headroom, with the original puzzle already budgeted. Private intake, moderation, selective reveal and duplicate credit form a substantial but manageable implementation with a concrete Codex-built demonstration.
- Design (5): The opening shows the essential choice immediately: open a nudge while the answer remains sealed. Three accounts can populate the jar, demonstrate moderation and earn credit without pretending to be a larger audience.
- Risk (Low): T4 must establish a working public login page and private submission path; a reveal test should verify that unopened tiers remain hidden. The core avoids speech recognition, replay timing and a second live channel.
- Biggest weakness: It depends on viewers accepting an extra submission step when ordinary chat remains the easiest place to spoil something.

### VAR
- Innovation (3): Chat-triggered replays, branded slow motion, polls and clip posting already exist in the supplied evidence. Combining them into a complete review ritual is distinctive on video, matching the new-combination anchor.
- Impact (3): Replay downloads support interest in replay tools, and disputed outcomes fit games and desk challenges. Demand for the jury itself is unproven, while automatic interruption conflicts with the cited preference for replaying between rounds.
- Tech (4): The replay pipeline and simulator-tested vote timing give Codex a concrete, technically interesting role within an 8.5-hour MVP. Latency adjustment and asynchronous clipping prevent this from being a confidently polished 5.
- Design (5): A disputed basket, slow-motion evidence, named jurors and a verdict stamp provide an immediately understandable story. Three accounts are sufficient for both the two-person trigger and a convincing small jury.
- Risk (Medium): T2 must show the relevant moment within five seconds, not merely play any saved footage. T5 must also demonstrate that the generated clip contains the review, since the supplied facts leave duration-window selection uncertain.
- Biggest weakness: A successful technical demonstration still does not establish that streamers want chat to interrupt play with repeated reviews.

### Studio Audience
- Innovation (3): Distinct-viewer mixing and recurring voices combine existing sound alerts, personal sounds and activity-scaled visuals. The collective soundtrack is a visible and audible difference, but its ingredients and individual-viewer association are established.
- Impact (3): The verified emote-to-laugh guide supports the behavior, and sound tools have an established audience. Repetition complaints weaken weekly-use confidence, while a silent chat produces no reactions for this tool to amplify.
- Tech (4): The Web Audio mixer, deterministic voice identities and burst-testing simulator are concrete technical work that fits the nine-hour MVP. Sample selection and audio tuning require care, but the core avoids the speech-recognition and replay dependencies of other cards.
- Design (4): Three named seats reacting to a missed shot communicate the premise quickly and can be entertaining. However, three voices cannot demonstrate the promised larger crowd naturally, and recognizable signature laughs require more listening than a single gag.
- Risk (Low): A three-account rehearsal should test distinguishable voices, repeated-message handling, volume limits and headphone-only routing. T5 concerns optional lurker seats; the proposed real raid segment additionally needs a second live channel if retained.
- Biggest weakness: Traceability explains where the laughter comes from, but does not establish that people will enjoy hearing it repeatedly.

### Raid Torch
- Innovation (4): None of the supplied competitors carries an audience-marked object and its history through raids. The arrival of recognizable marks makes the difference from scheduling tools and ordinary raid alerts visible.
- Impact (3): Active raid-train communities provide a plausible audience and recurring occasion. Evidence supports organized raids rather than demand for a traveling object, and usefulness requires adoption by multiple channels.
- Tech (3): Shared state, deployment, cross-channel subscriptions and arrival recognition are meaningful engineering. The 9.5-hour MVP leaves only the minimum buffer while requiring more operational setup than the single-channel cards.
- Design (3): The torch arrival and glowing bearers are understandable visual rewards. With one streamer controlling both channels and two journey hops labeled as rehearsals, the demo cannot fully convey the multi-community experience.
- Risk (High): T3 must establish two live channels and a timely real raid, followed by an end-to-end check that marks transfer and known bearers light up on chat. The one-sided send-off fallback removes the central cross-channel payoff.
- Biggest weakness: Its most compelling benefit depends on a network of participating communities that this demo cannot supply.

### Minefield
- Innovation (5): The supplied research found no equivalent loop where viewers secretly choose words and the streamer's ordinary speech detonates them. Changing who chooses the trigger and who unknowingly activates it creates a new game, clearly demonstrated by the bait-and-reveal sequence.
- Impact (3): Talkative streams provide broad potential applicability, but demand rests on adjacent swear jars, bingo and weaker requests for mic-triggered effects. The card explicitly leaves the game's sustained fun unvalidated.
- Tech (3): The accuracy harness is an excellent concrete Codex artifact, and the implementation is more than a simple keyword effect. However, reliable casual-speech detection, low latency and false-alarm control are substantial uncertainties inside the maximum-size MVP.
- Design (5): The spoken word, explosion, planter credit and bait-question callback explain the game immediately. Three participants can produce genuine suspense, competing traps and a funny dud reveal without audience-scale simulation.
- Risk (High): T1 must meet all three thresholds—at least 80% hits, at most one false alarm per ten minutes and at most three seconds of lag—and T4 must keep words private. The 20-minute playtest must also show that unscripted baiting works; DEFUSE does not compensate for frequent detection errors.
- Biggest weakness: The central joke depends on speech recognition being reliable enough that viewers credit the planter rather than question the detector.

### Checkpoint
- Innovation (4): Voice-transcribed answers returned to the original viewer visibly extend the familiar question queue. The post-pivot search supports that distinction, although it has only one research source and the surrounding queue remains established.
- Impact (4): The Streamlabs guide documents the underlying workflow of scheduled chat breaks and moderator-maintained questions. Returning the actual answer addresses missed interactions across drawing, making and focused gameplay, though demand for quoted receipts specifically is not established.
- Tech (3): The voice-to-receipt pipeline and recorded-audio tests are concrete and technically meaningful. Partial transcription, answer segmentation, confidence gating and reliable reply delivery make the allocated speech and closure work ambitious.
- Design (4): Crystals becoming a question card, live words and a threaded answer give the opening a clear progression with three accounts. The payoff is useful but less immediately theatrical than a mine explosion or replay verdict, and requires showing both stream and chat.
- Risk (High): T1b must produce readable quotes within two seconds, while additional tests must check thinking pauses, skip behavior and actual threaded delivery. The named pause-trigger fallback is insufficiently specified to establish that the quoted-answer demonstration survives failure.
- Biggest weakness: An early close or confidently wrong transcript can send an incomplete or incorrect answer under the streamer's apparent authority.

### Tap on the Shoulder
- Innovation (3): The evidence already contains private mic alerts, chat keyword alerts and reactive mascots. Combining human reports, OBS checks, an in-room signal and audience confirmation produces a useful, visibly different workflow that fits the combination anchor.
- Impact (4): Verified prolonged audio failures and a forum request establish a concrete problem across common mic-based broadcasts. Reports such as “you sound far away” extend beyond mute detection, although failure frequency and existing self-monitoring limit the case for a 5.
- Tech (4): The nine-hour MVP combines testable report logic, OBS signals, authenticated mod cues and a paired phone display. The noisy-chat test suite is a specific Codex contribution, with more predictable implementation than speech transcription.
- Design (4): The alarmed phone face and muted-versus-far-away comparison make the benefit easy to grasp. The confirmation loop gives it a satisfying ending, but the camera must clearly show the phone, and the proposed calm-mode segment is stretch work.
- Risk (Medium): T2 must distinguish mute state from sustained low levels; an end-to-end rehearsal must verify HTTPS pairing, an awake phone, private audio routing and confirmation after stream delay. Those device and routing dependencies are not covered by the detector tests alone.
- Biggest weakness: The strongest everyday-use argument relies on calm mode, which is outside the MVP.

## Ranking
1. Hint Jar: It ties for the highest total while offering the clearest path to a polished, credible three-account demonstration within the build budget.
2. Minefield: It has the strongest new interaction and immediate entertainment payoff, but its untested speech detection makes it a less dependable winner than Hint Jar.
3. Checkpoint: Among the 15-point cards, its distinctive answer receipts and documented attention-management problem give it the strongest combination of usefulness and originality.
4. VAR: Its exceptionally watchable review ritual and concrete replay engineering narrowly outweigh its indirect demand evidence.
5. Tap on the Shoulder: It addresses a well-supported practical problem with achievable engineering, but its combined-alert workflow is less distinctive and theatrical than the cards above it.
6. Studio Audience: It is feasible and easy to demonstrate, but three voices underrepresent its main promise and repeated-use enjoyment remains uncertain.
7. Raid Torch: Its original shared object is appealing, but cross-channel setup and the lack of real participating communities most constrain what this entrant can convincingly show.