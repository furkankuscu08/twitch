# Wave 2: Open-Lens Ideas

**Claim labels:** **[V-brief]** means the supplied brief reports something as verified; I have not independently reverified it. **[I]** means an inference or design proposal. **[U]** means an unknown requiring validation. Product names below are working names.

## A. Crowd map

**[I]** These are the ten submission clusters I would expect, rather than predictions about particular participants:

1. An AI co-host that reads chat, jokes, and reacts to stream events.
2. Chat-controlled platformers, pets, or other “Twitch Plays” games.
3. Polls, predictions, trivia, and bingo with polished overlays.
4. An AI highlight finder or automatic clip editor.
5. Animated alerts and celebrations for follows, raids, and milestones.
6. Viewer-triggered distractions, sound effects, or game modifiers.
7. Loyalty points, viewer levels, leaderboards, and collectible badges.
8. Streamer matchmaking or collaboration scheduling.
9. A question queue or AI summary that helps streamers catch up with chat.
10. Tabletop companions: dice, character sheets, encounters, and maps.

A familiar starting point can still produce a memorable entry. The question is whether the distinguishing behavior survives after removing the branding and visual polish.

## B. Wide list

All entries are **[I] design proposals**, not validated demand.

1. **Hint Airlock:** Viewers submit hints at different strengths; the streamer releases only the level of help they want. `need #1; audience boundaries`
2. **Soundcheck Relay:** Viewers report a specific production problem and confirm whether the streamer’s attempted fix actually worked. `need #9`
3. **Footnotes:** Moderators attach short explanations to recurring jokes, names, and projects; newcomers can summon a compact explanation without interrupting the streamer. `need #3`
4. **Foley Pit:** Three viewers build a sound-effects score that the streamer performs with ordinary desk objects. `audience participation; physical output`
5. **Loose Ends:** A viewer bookmarks “I’ll show you later”; the streamer gets a short list of unresolved promises at the next break. `need #1; continuity`
6. **Continuity Crew:** Viewers flag discrepancies against a maker’s explicitly stated current step; the streamer reviews them at a planned checkpoint. `need #1; science/maker streams`
7. **Raid Baton:** An outgoing community hands its host one unfinished, recipient-approved activity to carry into the next stream. `raid; social handoff`
8. **Welcome Without Spotlight:** A newcomer requests orientation without triggering a public welcome, username announcement, or demand to participate. `need #3; lurker respect`
9. **Bench Test:** Chat proposes tiny experiments for a maker; the streamer accepts one, predicts the result, and performs it live. `science streams; audience participation`
10. **Camera Scout:** Viewers report “your hand hides the important part”; the streamer sees a small framing diagram with the affected area. `need #9; IRL/maker streams`
11. **Encore Ledger:** Viewers bookmark moments they want explained or demonstrated again; the streamer chooses one for a deliberate end-of-stream encore. `need #1; content enhancement`
12. **Quiet Applause:** Optional chat reactions accumulate into a restrained visual flourish only when the streamer finishes a performance. `need #5; latency tolerance`
13. **Prop Jury:** Viewers assign unexpected fictional identities to three real objects; the streamer improvises a scene incorporating them. `physical output; improvisation`
14. **Community Museum:** The streamer labels a few artifacts created during the session, crediting specific viewer contributions instead of ranking activity. `per-channel identity; need #10`
15. **Explanation Ladder:** Viewers request “define the term,” “show an example,” or “show the full method”; the streamer sees the requested depth at a break. `need #1; educational streams`
16. **Mod Stage Manager:** Moderators send private production cues—“guest ready,” “link corrected,” “question cleared”—with explicit acknowledgement. `need #4`
17. **The Other Take:** After a creator finishes one interpretation, viewers commission a short second version under a different constraint. `creative participation; reveal`
18. **Intermission Dispatch:** A moderator collects one question, one community contribution, and one practical announcement for the streamer’s return. `needs #1 and #4`
19. **Shared Vocabulary:** Chat proposes names for newly invented techniques or recurring mishaps; the streamer canonizes one into the session’s glossary. `need #3; community identity`
20. **Desk Orchestra:** Viewers control physical lights and small instruments around the streamer, with locally scheduled playback. `physical output; Twitch Plays`
21. **Audience Accessibility Check:** Viewers request a larger label, repeated instruction, or spoken description through a few explicit commands. `production quality; accessibility`
22. **One Good Question:** Each viewer can replace their own pending question, encouraging revision rather than repeated messages. `needs #1 and #5`

## C. Five full cards

### 1. Hint Airlock

**Familiar base: question queue / chat catch-up tool**

- **One-liner:** **[I]** A backseating boundary the streamer can operate: “Give me a nudge, but keep the answer sealed.”
- **Who installs it / who gets the value:** The streamer installs the overlay and private dashboard. Viewers get a legitimate way to help. Moderators approve and classify submissions without posting control commands publicly.
- **Streamer category fit:** Puzzle games, coding challenges, escape-room streams, and creative problem-solving where assistance is welcome only on request.
- **Core loop:** Viewer submits `!hint nudge <text>` or `!hint answer <text>` → the submission enters a private moderator queue → a moderator approves its actual strength → the streamer opens the “nudge” compartment → one approved hint appears on screen. The streamer can request another or close the compartment.
- **First 10 seconds of the demo:** A puzzle and three sealed compartments: **Nudge / Method / Answer**. The streamer says, “One nudge.” A modest clue opens; the solution stays visibly sealed.
- **Twitch surfaces used:** EventSub chat ingestion, an OBS browser source, a private moderator dashboard, and optional Helix acknowledgements.
- **Works with 1 streamer + 3 test accounts? How?** One viewer submits a useful nudge, one submits the answer, and one acts as moderator. The streamer demonstrates selective release. Submission and reveal are separate phases, so viewer latency does not determine success.
- **Closest existing thing and the meaningful difference:** **[U]** Question queues and spoiler rules are the nearest functional substitutes; exact product overlap needs checking. **[I]** This adds an explicit permission boundary around *how much help* reaches the streamer, rather than merely prioritizing messages.
- **Why wouldn’t 30 other teams build this?** **[I]** Most catch-up tools optimize for more information reaching the streamer. This deliberately withholds information until requested. The sealed answer is also an immediately legible demo object.
- **Evidence it links to:** **[V-brief]** Need #1 establishes attention constraints; need #4 establishes missing private moderator controls. **[U]** Demand for graded assistance specifically is unvalidated.
- **MVP scope / explicitly out of scope:** Three compartments, one active challenge, manual approval, reveal controls, and clear/reset. No automatic spoiler classification, game integration, or LLM. Delete submissions at session end or within 24 hours.
- **Riskiest assumption:** **[U]** Viewers will use the submission convention. Their original messages still exist in public Twitch chat: this protects the streamer’s dedicated hint view, not every viewer from spoilers. The streamer must avoid the raw chat view during the challenge.

### 2. Soundcheck Relay

- **One-liner:** **[I]** Turn “your audio is broken” into a short, visible repair-and-confirm loop.
- **Who installs it / who gets the value:** The streamer installs a private status panel and optional small overlay. Viewers get an easy way to report problems. Moderators consolidate reports and start confirmation checks.
- **Streamer category fit:** Music, interviews, console streams, IRL setups, and any small stream without a dedicated producer.
- **Core loop:** Viewer sends `!check mic quiet` → the streamer sees an issue ticket → the streamer makes a change and starts **Test B** → viewers hear the spoken test label when their delayed stream reaches it, then send `!heard B good` or `!heard B quiet` → the panel distinguishes improvement from continuing trouble.
- **First 10 seconds of the demo:** The mic is audibly too quiet. Two reports create **Mic: hard to hear**. The streamer changes the level and says “Test B.” The video cuts forward explicitly to two confirming replies; the ticket resolves.
- **Twitch surfaces used:** EventSub chat ingestion, private web dashboard, OBS overlay, and occasional Helix instructions.
- **Works with 1 streamer + 3 test accounts? How?** Two listeners report and later confirm; the third can show a conflicting result. Three accounts demonstrate the workflow, although they do not establish diagnostic accuracy. Test labels bind replies to the correct attempt despite stream latency.
- **Closest existing thing and the meaningful difference:** **[U]** Monitoring meters, ordinary chat reports, and moderator messages are the comparison set. **[I]** The distinction is closing the loop using the audience’s received experience, including which repair attempt they actually heard.
- **Why wouldn’t 30 other teams build this?** **[I]** Hackathon entries are likely to add entertainment to a functioning stream. This makes restoring a broken stream the interactive experience. A genuine before/after is easy to understand.
- **Evidence it links to:** **[V-brief]** Need #9 identifies poor audio as a meaningful production problem; need #1 explains why chat reports can be missed.
- **MVP scope / explicitly out of scope:** Three report types—mic quiet, program audio missing, voice/music imbalance—plus test IDs, per-user deduplication, confirmation, and dismissal. No audio capture, automatic diagnosis, OBS control, or claim that a majority proves correctness.
- **Riskiest assumption:** **[U]** Audience reports may reflect individual devices rather than a stream-wide defect. The interface must show “two listeners report…” rather than declare an objective fault. Validate with deliberately introduced problems and mixed listener setups.

### 3. Footnotes

- **One-liner:** **[I]** Give inside jokes a footnote so newcomers can understand the room without stopping the show.
- **Who installs it / who gets the value:** The streamer installs a small overlay; the streamer or moderator authors explanations. Newcomers get context. Regulars keep their existing vocabulary without repeatedly explaining it.
- **Streamer category fit:** Recurring creative projects, tabletop campaigns, challenge runs, and personality-led streams with established lore.
- **Core loop:** A moderator creates a short entry such as **“the spoon incident”** → a compact footer occasionally shows that context is available → a viewer sends `!why spoon` → a three-line explanation appears briefly on screen, without identifying the requester. Repeated requests merge during a cooldown.
- **First 10 seconds of the demo:** Everyone laughs when the streamer says, “No spoons this time.” A viewer requests the footnote. A restrained card explains the earlier mishap, then folds away while the stream continues.
- **Twitch surfaces used:** EventSub chat ingestion, OBS browser source, moderator authoring panel, and optional short Helix response.
- **Works with 1 streamer + 3 test accounts? How?** Two accounts establish the recurring reference; the third requests its meaning. The effect requires only one requester and no popularity threshold. Requests remain useful after ordinary stream delay.
- **Closest existing thing and the meaningful difference:** **[U]** Custom bot commands, channel FAQs, and lore documents are the nearest substitutes. **[I]** The difference is contextual, temporary delivery on the stream itself, with a current-session relevance indicator. This is a modest distinction; execution must prove that it feels easier than `!lore`.
- **Why wouldn’t 30 other teams build this?** **[I]** It approaches community growth through comprehension rather than rewards, forced greetings, or increased message volume. However, this has less novelty protection than the other cards.
- **Evidence it links to:** **[V-brief]** Need #3 directly identifies exclusion through inside jokes. Needs #5 and #9 support quiet delivery and a small visual footprint.
- **MVP scope / explicitly out of scope:** Five manually authored entries, one compact display component, relevance toggles, cooldowns, and preview. No AI-generated lore, transcript summarization, or personal histories. For the MVP, expire all session entries within 24 hours.
- **Riskiest assumption:** **[U]** Asking for context may itself feel awkward, and moderators may not maintain the cards. Validate whether newcomers actually request explanations and whether a moderator can author useful entries in seconds.

### 4. Foley Pit

**Familiar base: viewer-triggered sound effects**

- **One-liner:** **[I]** Chat writes the sound-effects score; the streamer performs it live with paper, a cup, and a spoon.
- **Who installs it / who gets the value:** The streamer installs the score overlay and conductor controls. Viewers become sound directors. The audience watches the streamer translate a ridiculous brief into a physical performance.
- **Streamer category fit:** Just Chatting, music, improv, theater, and maker streams; also a short intermission segment.
- **Core loop:** The streamer opens a scene such as **“A tiny detective enters a storm”** → viewers claim **weather**, **footsteps**, and **surprise** using chat → each chooses one permitted cue → a three-beat score fills in → the streamer locks it and advances through the beats while performing the sounds with real objects.
- **First 10 seconds of the demo:** A card reads **Tiny detective. Enormous thunder.** Three viewer contributions fill the score. The streamer crinkles paper for rain, taps a spoon for footsteps, then produces an absurd thunderclap with the cup.
- **Twitch surfaces used:** EventSub chat ingestion, OBS score overlay, local conductor controls, and one Helix invitation per round.
- **Works with 1 streamer + 3 test accounts? How?** Each account owns one role. One viewer can also fill all three roles if necessary. Viewers submit asynchronously; only the streamer controls performance timing, so they never need to synchronize to the delayed video.
- **Closest existing thing and the meaningful difference:** **[V-brief]** Viewer-triggered sound tools are an established category. **[U]** Exact overlap with live Foley participation needs checking. **[I]** Here the payoff is a human interpretation of a shared score, not playback of a purchased or selected recording.
- **Why wouldn’t 30 other teams build this?** **[I]** It places the surprising output on the streamer’s actual desk. The memorable image is a person struggling to make a cup sound like a monster, while three visible contributors direct the scene.
- **Evidence it links to:** **[V-brief]** Past winners included physical outputs, although that does not establish why they won. **[I]** The idea also respects the brief’s preference for empowering the streamer. **[U]** Repeat entertainment value is unvalidated.
- **MVP scope / explicitly out of scope:** Three roles, six scene prompts, a small cue vocabulary, role ownership, score lock, conductor advance, and reset. No generated audio, music licensing dependency, hardware integration, speech recognition, or unrestricted text on the overlay.
- **Riskiest assumption:** **[U]** The streamer must enjoy performing. Software cannot rescue a reluctant host. Validate with three scenes: do the cues produce amusingly different performances without extensive rehearsal?

### 5. Continuity Crew

- **One-liner:** **[I]** Give a maker a tiny audience-assisted continuity check before moving to the next stage.
- **Who installs it / who gets the value:** The streamer installs a stage panel and overlay. Viewers can contribute careful observation. Moderators approve observations; the streamer decides whether they matter.
- **Streamer category fit:** Crafts, model building, drawing demonstrations, miniature painting, and other visibly staged work.
- **Core loop:** The streamer declares a checkable intention—**Stage C: both wings get two blue dots** → viewers submit `!mark C left wing has one` → approved observations collect privately → at the planned checkpoint, the streamer opens a compact checklist → they inspect, correct, or dismiss each observation, then advance the stage.
- **First 10 seconds of the demo:** A paper creature has mismatched wings. The streamer reaches the checkpoint. One viewer observation appears beside the stated intention; the streamer notices the missing dot, fixes it, and stamps the stage complete.
- **Twitch surfaces used:** EventSub chat ingestion, OBS stage/checkpoint overlay, private moderation and stage controls.
- **Works with 1 streamer + 3 test accounts? How?** One account spots the discrepancy, another submits a duplicate, and the third moderates. The demo shows merging and one accepted observation. Stage IDs prevent delayed messages from silently becoming observations about the next stage.
- **Closest existing thing and the meaningful difference:** **[U]** Checklists, chat backseating, and moderator relays are the closest functional alternatives. **[I]** This binds observations to a declared intention and a deliberate review point, rather than creating a continuous distraction feed.
- **Why wouldn’t 30 other teams build this?** **[I]** It starts with the continuity problems of physical making, not generic chat engagement. The correction happens to a real artifact and remains visible after the overlay disappears.
- **Evidence it links to:** **[V-brief]** Need #1 covers streamers occupied with performing or working. **[U]** Whether viewers want this role, and whether creators welcome it, require validation.
- **MVP scope / explicitly out of scope:** Manual stage text, tagged observations, approval, duplicate merging, checkpoint review, and resolution. No computer vision, automatic correctness judgment, safety-critical procedures, or dependency on catching errors immediately. Session observations expire within 24 hours.
- **Riskiest assumption:** **[U]** The checkpoint may feel like a school inspection. The creator must explicitly invite a narrow observation task; otherwise this could formalize unwanted backseating. Delay also means checkpoints need a reasonable response window.

## D. Parked

These remain **[I] proposals**; each needs a blocking condition resolved.

- **Cross-channel Raid Baton:** Needs a cooperating second live broadcaster to demonstrate the actual handoff convincingly; the constrained single-streamer demo is insufficient.
- **Desk Orchestra with custom actuators:** Needs reliable hardware already available and tested; procurement and physical debugging threaten the ten-hour build limit.
- **Channel-point-funded Foley commissions:** Needs confirmed new-channel API access; the ungated chat version is the viable MVP.
- **Persistent viewer passports:** Needs a reviewed data-retention design and evidence that the proposed stored fields are permitted; retaining Twitch-derived participation history beyond 24 hours conflicts with the brief’s conservative constraint.
- **Frame-accurate audience rhythm game:** Needs a separate synchronized client experience that removes stream delay from the timing loop; video-based reaction timing fails the latency filter.
- **Clickable in-player context annotations:** Needs an approved Extension or an already available equivalent surface; a browser-source overlay cannot supply viewer-side clicks.
- **Automatic “previously on” using old VODs:** Needs a permissible content-access and retention approach; a growing archive of Twitch content falls outside the supplied constraint.

## E. Your pick

**I would build Foley Pit.** **[I]** It offers the strongest combination of a memorable opening shot, a complete three-viewer interaction, a manageable implementation, and a reason to watch the human streamer. Its difference survives without AI: viewers compose, the streamer interprets, and ordinary objects produce the payoff. The principal uncertainty is entertainment value, so I would first run three rounds using paper cue cards before spending the build budget. If that works, the software’s job is precise: make claiming roles, composing the score, and conducting the performance effortless. The submission can then show the actual Codex development record alongside the working Twitch experience.