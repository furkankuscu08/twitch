# Wave 2 inventory and clusters

Built 2026-10-25 from five idea files. Revised the same day after an independent review ([inventory-review.md](inventory-review.md)); see the change log at the end. Steps 1–2 of the funnel only: inventory and clustering. No filtering or scoring yet.

| Source | File | Lens | Wide list | Full cards |
| --- | --- | --- | --- | --- |
| L1 | [L1-need.md](L1-need.md) | Need-driven (Opus high) | 20 | 5 |
| L2 | [L2-spectacle.md](L2-spectacle.md) | Spectacle-driven (Opus xhigh) | 22 | 5 |
| L3 | [L3-capability.md](L3-capability.md) | Capability and transfer (Opus high) | 20 | 5 |
| G | [G-gpt-open.md](G-gpt-open.md) | Open (GPT 6 Astra) | 22 | 5 |
| X | [X-grok-open.md](X-grok-open.md) | Open, grounded in X (Grok) | 17 | 5 |
| | | **Total** | **101** | **25** |

Idea IDs are `<source>-<wide-list number>`, e.g. `L1-1`. ★ marks a full card. "(parked by source)" means the source itself parked that idea.

**Clustering rule:** ideas are merged by **core loop** (what the viewer does → what happens → who benefits), not by name. A cluster keeps its variants, because the twist often lives in a variant. Split clusters keep their original number with a letter (K01a, K01b) so references stay stable.

**Independence caveat:** the five sources shared one brief, and the brief names several themes (raid as handoff, needs #1/#3/#4/#6, YouTube Q&A mode, lurkers). The L1 and L3 lens blocks also name needs or mechanisms, and L1–L3 could read wave 1 files and synthesis.md. Only G and X were lens-free, and only they were limited to the brief. Convergence below is therefore **partly prompt-induced**, not purely independent.

---

## 1. Union crowd map

What the five agents expect most entrants to build. Count = in how many of the 5 crowd maps the category appears.

| Category | Count | Maps |
| --- | --- | --- |
| AI co-host or chatbot | 5 | all |
| AI "what did I miss" summarizer | 5 | all (L2 and G name it together with a queue) |
| Twitch Plays | 5 | all |
| Polls and predictions overlay | 5 | all |
| Trivia or quiz | 5 | all |
| Dice or TTRPG overlay | 5 | all |
| Viewer-triggered distractions, effects, sounds | 5 | all |
| Auto-clipper or AI highlights | 5 | all |
| Collab or cross-channel game, shared scene, matchmaking | 5 | all (L2's entry is shared with sports) |
| Chat-fed pet, avatar, or creature | 4 | L1, L2, L3, G (G only in passing) |
| Bingo | 4 | L1, L3, G, X |
| Sports or game-stat overlay | 3 | L2, L3, X |
| **Question queue or question-surfacing dashboard** | **2** | L2, G |
| Loyalty levels or badges | 2 | L1, G |
| Skinned alert pack | 2 | G, X |
| Command bot with an overlay | 1 | X |

This is our working picture of "the likely competition" for the Innovation criterion. The maps are themselves LLM guesses, not observations.

---

## 2. Clusters

The Sources column counts sources (max 5). Crowd map: **yes** = the core loop is a union-map category; **adjacent** = close to a map category; **no** = not on the map. ⚠ marks a hard-filter risk that a source or the review flagged; these are checked in step 3.

### A. The streamer can't follow chat while busy (need #1, #6)

| ID | Cluster (core loop) | Members | Sources | Crowd map |
| --- | --- | --- | --- | --- |
| K01a | **Question queue.** Viewers ask with `!ask` or `?`; questions wait visibly; the streamer pulls one when free. | L3-1 Floor★ (`+1` votes; the viewer's own message is natively pinned and marked) · X-4 Three Lines★ (max 3 on screen, verbatim, non-questions ignored) · G-22 One Good Question (replace your own pending question) · G-15 Explanation Ladder (requested depth) | 3 (L3, X, G) | **yes** (question queue, 2 maps) |
| K01b | **Focus capture, surfaced at a break.** During a busy stretch, *all* normal messages are held without commands; at a checkpoint they are paged on stream as call-in cards and answered. | L1-1 Checkpoint★ (explicitly not a summary) · G-18 Intermission Dispatch (a mod collects for the return) · L1-11 Answered Wall (credit ribbon for answered viewers, output variant) | 2 (L1, G) | adjacent (summarizer) |
| K02 | **Bookmark a moment for a later revisit.** A viewer marks "come back to this"; the streamer gets the list at a break. | G-5 Loose Ends · G-11 Encore Ledger · L1-16 Rewind Request | 2 (G, L1) | adjacent (clips) |
| K03 | **Glanceable chat state in the streamer's room.** An ambient device (phone face, bulb, earcon) shows new chatter / question waiting / mood without reading. | L2-7 Desk Buddy★ · L2-8 Glow · X-11 A lamp, not a summary · L1-7 Chat Sonar (see also K20's headphone-only mode) | 3 (L2, X, L1) | adjacent (pet; L2 differentiates Desk Buddy from a pet) |
| K04 | **One line over the game.** Only first messages and questions reach a minimal display the streamer can see mid-game. | X-2 One Line★ (click-through always-on-top window) · L1-20 VR Mirror (big-font phone page) | 2 (X, L1) | adjacent (chat overlay) |
| K05 | **Streamer's private filtered chat view.** Lenses: questions, first-timers, mentions, mods. | L1-8 Streamer's Lens (cf. K04, same filters) | 1 | no |

### B. Production and moderation behind the scenes (need #4, #9)

| ID | Cluster (core loop) | Members | Sources | Crowd map |
| --- | --- | --- | --- | --- |
| K06 | **Production problems reach the streamer privately.** Viewer reports or mod cues ("mic muted") go to a streamer-only channel (lamp, chime, dock), with confirmation and credit. | L1-4 Tap on the Shoulder★ · G-2 Soundcheck Relay★ (numbered test, "heard B good") · G-10 Camera Scout · G-21 Audience Accessibility Check · L1-13 Dead-Air Coach (automatic mic-silence variant) | 2 (L1, G) | no |
| K07 | **Private mod production panel.** Mods queue messages, fire cards, drop markers, send cues from a phone, not via public `!commands`. | L1-6 Producer's Desk · L3-7 Mod Cockpit · G-16 Mod Stage Manager · L1-17 Shift Log · L3-17 Marker Notebook (private annotated markers → post-stream list) | 3 (L1, L3, G) | no |
| K08 | **Mobile moderation with confirm and undo.** A big-button phone page; timeouts have a 10-second undo. | X-5 Ten Seconds★ | 1 | no |

### C. Newcomers, late arrivals, raiders (need #3)

| ID | Cluster (core loop) | Members | Sources | Crowd map |
| --- | --- | --- | --- | --- |
| K09 | **Lore footnotes for inside jokes.** Mods write a glossary; when a term appears in chat (L1, L3) or on request with `!why` (G), a small footnote explains it on stream. | L1-2 Footnotes★ · L3-3 Chat Footnotes★ · G-3 Footnotes★ (on request, requester not shown) · G-19 Shared Vocabulary (weak member: chat names new terms) | 3 (L1, L3, G) | no |
| K10 | **"You are here" context for late arrivals and raiders.** Chapters, beats, or a short note are set during the stream; a pin, overlay card, or raid-triggered recap shows them. | L3-2 Story So Far★ (native pin + marker + title + clip) · L1-3 Previously On★ (raid triggers a TV-style recap of beats) · X-12 Glossary on arrival (streamer's 3 lines shown when a raid lands) · L2-12 Previously On (last stream's moments as a cold open ⚠ 24 h) · L3-6 Raid Doorway · L3-11 Chapter Title Sync | 4 (L3, L1, X, L2) | no |
| K11 | **Newcomer welcome and orientation.** First chatters get a guide, a bio card, a quiet orientation, or a keepsake. | L1-9 Welcome Mat · L1-10 Name Card · G-8 Welcome Without Spotlight · L1-18 Commands Menu card · L2-9 Wall of Firsts (thermal printer; cf. K23 souvenirs) | 3 (L1, G, L2) | adjacent (alerts) |
| K12a | **Chat translation for the streamer.** | L1-19 Bilingual Bridge (⚠ chat text to a third party) | 1 | no |
| K12b | **Local live captions for viewers.** | X-14 Caption row (local STT, nothing kept) | 1 | no |

### D. Raids

| ID | Cluster (core loop) | Members | Sources | Crowd map |
| --- | --- | --- | --- | --- |
| K13 | **Raid pre-check.** Before raiding, show whether the target chat is follower-only and how long the wait is; raid only on confirm. | X-1 Raid Gate★ | 1 | no |
| K14 | **Something travels with the raid.** A note, an activity, or an object is carried to the target channel and shown on arrival. | L3-5 Raid Torch★ (cumulative multi-hop object: each chat adds `!mark`s, the journey is shown) · L1-15 Raid Baton · L2-17 Raid Baton (chat co-writes the line) · G-7 Raid Baton (recipient-approved activity carried into the next stream; parked by source) · X-6 Handoff card · L3-20 Raid Last Call (chat votes the line, pinned before raiding out) | 5 (all) | adjacent (collab) |
| K15 | **Raid lands at a bad moment.** The streamer is on BRB or a starting screen; keep the raider visible until thanked, or switch scene. | X-7 BRB receipt · X-17 Starting-soon raid flash (source: "not a clear pain") | 1 | adjacent (alerts) |
| K16 | **Raid ring for small streamers.** An opt-in ring suggests a live member to raid at stream end. | L3-15 Shoutout Ring | 1 | adjacent (matchmaking) |

### E. Spoilers and backseating

| ID | Cluster (core loop) | Members | Sources | Crowd map |
| --- | --- | --- | --- | --- |
| K17 | **Tiered hints, released only when the streamer asks.** Nudge / method / answer tiers. Two variants: **delete and seal** from public chat (L1-5), or a **private mod-approved queue** that leaves the originals in chat (G-1). | L1-5 Hint Jar★ · G-1 Hint Airlock★ | 2 (L1, G) | adjacent (question queue) |
| K18a | **Timed chat-settings mode.** One key turns on emote-only for a scene, then restores the previous settings automatically. | X-3 Blind Minute★ · X-15 Own-channel expire · L3-13 Emote-Only Rush (game variant: emotes as ammo) | 2 (X, L3) | no |
| K18b | **Spoiler-hold filter.** Lines that look like spoilers or directions are held in a drawer until the chapter ends. | L1-14 Spoiler Airlock · X-16 Spoiler drawer (source: weaker than Blind Minute) | 2 (L1, X) | no |

### F. Spectacle: the streamer as the payoff

| ID | Cluster (core loop) | Members | Sources | Crowd map |
| --- | --- | --- | --- | --- |
| K19 | **Viewer plants it, the streamer sets it off.** Viewers secretly pick a trigger; the streamer's own speech or action fires the payoff. | L2-1 Minefield★ (secret word mines, speech-to-text) · L2-2 Sound Tags · L2-3 Try Not To Laugh · L2-18 Sip Watch | 1 (L2) | no |
| K20 | **Chat reactions amplified.** Reactions become a scaled crowd soundscape (with signature laughs and a headphone-only mode), a per-viewer motif, or a restrained visual flourish. | L2-4 Studio Audience★ (cf. K03 Chat Sonar) · L2-5 Leitmotif · G-12 Quiet Applause (visual) | 2 (L2, G) | **yes** (sound effects) |
| K21 | **Viewers write the brief, the streamer performs it.** A small score, prompt, dare, or experiment, performed live with real objects. | G-4 Foley Pit★ · G-13 Prop Jury · G-17 The Other Take · G-9 Bench Test · L2-22 Bounty Board | 2 (G, L2) | adjacent (distractions) |
| K22a | **Viewers drive the streamer's physical or camera setup.** | G-20 Desk Orchestra (parked by source: hardware) · L2-13 Director's Chair · L2-15 Haunt | 2 (G, L2) | **yes** (distractions) |
| K22b | **Collective-control toys.** | L2-16 Ouija · L2-21 Gravity Tetris · L2-20 Trio Jam | 1 (L2) | **yes** (Twitch Plays) |
| K23 | **Per-viewer souvenir moment.** `!snap` makes a Polaroid; a numbered ticket stub; credited artifacts in a "museum". | L2-10 Photo Booth★ · L2-19 Ticket Stubs (cf. K27 Daily Stamp) · G-14 Community Museum | 2 (L2, G) | no |

### G. Clips and predictions

| ID | Cluster (core loop) | Members | Sources | Crowd map |
| --- | --- | --- | --- | --- |
| K24 | **Chat-called replay review.** Viewers call `!var`; slow-motion replay, a jury vote, a verdict, a titled clip. | L2-11 VAR!★ | 1 | adjacent (polls + clips) |
| K25 | **Chat-consensus clipping.** Agreement or an emote spike makes a clip or a vertical crop. | L3-8 Consensus Clip · X-8 Vertical pact · X-9 Clip That for a new channel | 2 (L3, X) | **yes** (auto-clipper) |
| K26 | **Sealed predictions.** `!seal <guess>` is deleted at once; named envelopes open together. | L3-9 Sealed Envelope (native-Predictions version parked by source) | 1 | **yes** (predictions) |

### H. Viewer identity and presence

| ID | Cluster (core loop) | Members | Sources | Crowd map |
| --- | --- | --- | --- | --- |
| K27 | **Per-channel earned status.** A free level or medal shown next to names, earned by attendance and streaks, decaying when absent. ⚠ 24 h: the source says retention must be resolved first, or the idea is parked. | L3-4 Lit Medals★ (long-memory version parked by source) · L3-16 Daily Stamp · L3-12 Watch Streak Constellation (⚠ monthly sky) | 1 (L3) + G parked "viewer passports" | **yes** (loyalty) |
| K28 | **Lurker presence made visible.** Silent viewers appear as lanterns or stars, or are counted, with no call to speak. | L1-12 Lurker Lantern · L2-6 Lurker Sky · L3-14 Lurker Lanterns · X-13 Lurk receipt | 4 (L1, L2, L3, X) | no |

### I. Single-source and other

| ID | Cluster (core loop) | Members | Sources | Crowd map |
| --- | --- | --- | --- | --- |
| K29 | **Maker continuity check.** The streamer declares a stage; viewers flag mismatches; review at a checkpoint. (cf. K01b, K02: same "held for review" shape, but bound to a declared intention) | G-6 Continuity Crew★ | 1 | no |
| K30 | **Viewer voicemail call-in.** 15-second voice messages aired with a retro phone overlay. | L2-14 Call-in Line | 1 | no |
| K31 | **Shared Chat collab bridge.** Color-codes messages by source channel and pairs viewers across communities. | L3-10 Shared Chat Bridge (parked by source) | 1 | **yes** (collab) |
| K32 | **GIF jukebox.** Chat GIFs queue into an overlay frame with a mod veto. | L3-18 GIF Jukebox | 1 | adjacent (alerts) |
| K33 | **Guest Star green room.** Viewers queue to join as callers. | L3-19 Guest Star Green Room (parked by source) | 1 | no |
| K34 | **Missed hellos from another platform.** A tray of YouTube live greetings the Twitch streamer never saw. | X-10 Missed hello | 1 | no (but the brief notes high tool supply for multi-platform chat) |

---

## 3. Convergence

Clusters reached by 3 or more sources. "Seeded by" = where the theme was named in the shared inputs.

| Cluster | Sources | Full cards | Seeded by | Note |
| --- | --- | --- | --- | --- |
| K14 Something travels with the raid | 5 | 1 | brief ("raid as handoff"), L3 lens | Not listed directly on any crowd map; adjacent to collab. Needs two live channels. |
| K10 "You are here" context | 4 | 2 | brief (need #3, raids), L1 and L3 lenses | Not on any crowd map. |
| K28 Lurker presence | 4 | 0 | brief (lurker norm under need #2) | Nobody chose to card it. |
| K01a Question queue | 3 | 2 | brief (YouTube Q&A, needs #1/#6), L3 lens | On 2 crowd maps. |
| K09 Lore footnotes | 3 | 3 | brief (need #3), L1 lens | Not on any crowd map. X found no posts of newcomers lost in jokes (counter-signal). |
| K03 Glanceable chat state | 3 | 1 | brief (need #1) | |
| K07 Private mod panel | 3 | 0 | brief (need #4), L1 lens | |
| K11 Newcomer welcome | 3 | 0 | brief (need #3), L1 lens | |

Because convergence is partly prompt-induced, it says more about what the brief makes obvious than about idea quality. Teams using Codex or GPT with similar framing may reach the same places. It is passed to the Innovation evaluation as information, not as a bonus or a penalty.

## 4. Cross-cutting mechanisms

Reusable building blocks that appeared in several clusters:
- **The bot deletes a message to seal a secret** (needs moderator scope): K17 (L1-5 only), K19 mines, K26 predictions.
- **Streamer-side trigger, so viewer latency doesn't matter:** K01a, K01b, K17, K19, K21, K24.
- **Native Pinned Chat as a surface:** K01a Floor, K10 Story So Far, K09 start-of-stream pin, K14 arrival pin.
- **obs-websocket (replay buffer, screenshots, mic level):** K23, K24, K06 Dead-Air.
- **A physical or room-level output** (lamp, phone, printer, desk objects): K03, K06, K11 Wall of Firsts, K21, K22a.

## 5. Parked roll-up

Ideas the sources parked themselves (hard-filter breakers):
- **Needs an Extension:** viewer-side hover footnotes, click-on-video placement, clickable in-player annotations, a personal word block for viewers.
- **Needs Affiliate or uncertain API access:** channel-point versions (Checkpoint skip-the-line, Foley commissions, physical rewards), channel-point battles, gift effects, prediction games as the core, Custom Power-Up quests, native Predictions (Sealed Envelope), stream delay, hype train, ads, subs, charity.
- **Breaks the 24 h storage rule:** cross-stream helper levels, Lit Medals with long memory, viewer passports, a buddy that remembers you, an auto "previously on" from old VODs, searchable VOD memory, first-ever-chatter detection across streams.
- **Latency:** Red Light Green Light, live cross-channel Pong, frame-matched rhythm games.
- **Needs hardware:** Desk Orchestra with custom actuators, VR in-headset chat (also SteamVR work).
- **Needs a second live channel or broadcaster:** cross-channel Raid Baton (G), Shared Chat Bridge. Also affects the demos of K13, K14, and K10's raid variant.
- **Other:** STT-triggered footnotes (budget), Guest Star (beta), whisper ballots (phone verification and caps), an AI co-host that speaks as the talent (red line), fixing Twitch's caption track.

## 6. API claims and demo dependencies to test

Agent claims, unverified on our channel. They feed the day-1 test list.

| Claim | Clusters that depend on it |
| --- | --- |
| Pin Chat Message works on a new non-Affiliate channel, at a pin every few minutes | K01a (Floor), K10 (Story So Far) |
| A user token can read chat settings (`follower_mode_duration`) of a channel we don't moderate | K13 Raid Gate |
| A moderator token can write `emote_mode` and restore settings | K18a Blind Minute |
| A bot moderator can delete messages within ~1 s | K17 (L1-5), K19, K26 |
| A bot moderator can ban and unban within ~1 s | K08 Ten Seconds |
| Create Clip works on a new channel, with `title`/`duration` parameters [S] | K10, K19, K24, K25 |
| Create Stream Marker works on a new channel (needs VODs enabled) | K10, K19, K24, K07 |
| Modify Channel Information rate limit for frequent title changes [U] | K10 (optional title sync) |
| Get Chatters with `moderator:read:chatters` [S] | K20 Studio Audience (lurker seats), K28 |
| Watch Streaks arrive in `channel.chat.notification`; per-user counters beyond 24 h are allowed [U] | K27 Lit Medals (conditional) |
| Local speech-to-text catches casual speech over game audio | K19 Minefield |
| An always-on-top click-through window works over a fullscreen game without being captured | K04 One Line |
| **Demo:** a second live channel for a real raid (e.g. a test account streaming from a phone) | K10 raid variant, K13, K14 |

---

## Change log

**2026-10-25, after the review.** Accepted:
- **#1:** independence caveat; "Seeded by" column.
- **#2:** union row split into summarizer (5) and question queue (2); K01 → K01a/K01b; L1-11 → K01b.
- **#3:** K34 relabeled.
- **#4:** X-12 → K10 (K09 now 3, K10 now 4); G-19 marked weak.
- **#5:** K18 → K18a/K18b, removed from the convergence table.
- **#6:** parked items and categories added.
- **#7:** API rows added.
- **#8:** K17 variants; delete claim limited to L1-5.
- **#9:** K22 → K22a/K22b.
- **#10:** L3-17 → K07.
- **#11:** K15 reworded to cover X-17.
- **#12:** K12 → K12a/K12b.
- **#13:** Raid Torch twist added.
- **#14:** K20 reworded.
- **#15:** labels made consistent; the novelty note was removed from K28.
- **#16:** ⚠ flags added.
- **#17, #18:** cross-references added.
- **#19:** parked marks made consistent.

Not changed: none of the findings was rejected.
