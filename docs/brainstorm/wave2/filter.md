# Wave 2, step 3: hard filter

Applied 2026-10-25 to the 38 clusters in [inventory.md](inventory.md). Revised the same day after an independent review ([filter-review.md](filter-review.md)); see the change log at the end. This step checks **feasibility only**. Novelty, fun and impact are not judged here (step 4 and wave 3).

## Criteria

| # | Criterion | Source |
| --- | --- | --- |
| F1 | No Twitch Extension | brief §3 |
| F2 | Core does not depend on a Twitch feature that **may be gated** (Affiliate/Partner, beta, eligibility, or an unverified permission). A gated feature may only be a bonus. | brief §3 |
| F3 | Core uses only allowed surfaces: chat, overlay, EventSub, Helix, **plus our own local components** (obs-websocket, local speech-to-text, a phone web page, a desktop window). Third-party non-Twitch APIs (YouTube, cloud translators) are allowed only if we are authorized to use them (rules: third-party integrations), and get "~". | brief §3, rules |
| F4 | Tolerates 2–30 s viewer-side latency | brief §3 |
| F5 | No Twitch content or per-user Twitch data stored longer than 24 h | brief §3, Developer Agreement |
| F6 | Convincing demo with 1 streamer + 3 test accounts. A **second live channel we control** (a test account streaming from a phone or a second OBS) = "?". **Real third parties we cannot supply** = ✗. | brief §3 |
| F7 | The video can avoid third-party copyrighted material. "~" only where the source's own demo needs a third-party game or footage; the fix is our own content or a license-safe game. | rules §4 |
| F8 | Demo-quality MVP in ~10 agent-assisted hours, judged against the source's own MVP list. "~" = tight. | brief §3 |

Marks: ✓ pass · ✗ fail · ? depends on a test or setup · ~ passes with a stated constraint.

## Outcomes

| Outcome | Meaning |
| --- | --- |
| **Pass** | All criteria ✓ or ~. Goes to step 4. |
| **Test (low)** | The core depends on a standard broadcaster/moderator Helix operation that is documented and very likely to work. Goes to step 4; the test is on the day-1 list. |
| **Test (high)** | The core depends on something genuinely uncertain: a new or gated API, local tech accuracy, or a second live channel. Goes to step 4, and the risk is carried into scoring as delivery risk. |
| **Fail** | A core criterion fails. Moved to parked with what would need to be true. |

**Variant rule:** a cluster takes the outcome of its best variant **that keeps the cluster's core loop**. A variant that changes the loop does not rescue the cluster. Full cards also get their own outcome (section "Full cards").

---

## Results

| ID | Cluster | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 | Outcome | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| K01a | Question queue | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Pass** | Via Three Lines. Floor's core moment is the native pin, so that card is Test (high). |
| K01b | Focus capture, surfaced at a break | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | **Pass** | F7: Checkpoint's "boss fight" demo needs an IRL focus task (drawing, building) or a license-safe game. |
| K02 | Bookmark a moment for later | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Pass** | Rewind Request's clip step is a bonus (clip test). |
| K03 | Glanceable chat state in the room | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | ✓ | ✓ | **Pass** | Desk Buddy needs only a phone. F5: "returning regular" must mean seen this session, or come from badges in the chat event; no cross-stream memory. Bulb variants need a smart bulb (hardware on hand?). |
| K04 | One line over the game | ✓ | ✓ | ~ | ✓ | ✓ | ✓ | ~ | ? | **Test (high)** | The core is a click-through native window over a fullscreen game (F3 ~: a local window, not an OBS source). F7: use an open-source game. F8: window behavior is the unknown. L1-20's phone page is a different loop (looking away to a second screen) and does not rescue the cluster. |
| K05 | Private filtered chat view | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Pass** | |
| K06 | Production problems reach the streamer | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ~ | **Pass** | F8 ~: Tap on the Shoulder has four inputs plus a lamp. The lamp is optional (phone-flash fallback). Soundcheck handles latency with numbered test labels. |
| K07 | Private mod production panel | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Pass** | Marker Notebook needs the marker test. |
| K08 | Mobile moderation with undo | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Test (low)** | Core = ban/unban by a moderator bot within ~1 s. |
| K09 | Lore footnotes | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | ✓ | ✓ | **Pass** | F5: author the glossary in our own mod web panel, not by storing chat lines. |
| K10 | "You are here" context | ✓ | ✓ | ✓ | ✓ | ~ | ~ | ~ | ✓ | **Pass** | Via Previously On (L1-3): beats are session-only. The raid trigger can be shown with a manual trigger or a CLI mock; a real raid needs a second channel. F7: its demo names a commercial game; use our own content. **Story So Far** (L3-2): core is the native pin, so Test (high). **L2-12** (cold open from *last* stream): ✗ F5. |
| K11 | Newcomer welcome and orientation | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | ✓ | ✓ | **Pass** | F5: Name Card bios must be self-authored in our app or session-only; the welcome-duty roster is configured in our app. "First message" means first this session. Wall of Firsts needs a thermal printer (hardware on hand?). |
| K12a | Chat translation for the streamer | ✓ | ✓ | ~ | ✓ | ~ | ✓ | ✓ | ✓ | **Pass** | A cloud translator is a third-party API and sends chat to a third party (grey area, flag); a local model avoids both. |
| K12b | Local live captions for viewers | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ? | **Test (high)** | The core is local speech-to-text at **caption** accuracy, a higher bar than K19's keyword match. Audio stays local and is discarded continuously. |
| K13 | Raid pre-check | ✓ | ? | ✓ | ✓ | ✓ | ~ | ✓ | ✓ | **Test (low)** | Core = Get Chat Settings for a channel we don't moderate. Basis for "low": in our understanding, Get Chat Settings accepts an app or user token, and only the moderator-only fields need a moderator. This is unverified in-session; the source's fallback (`ROOMSTATE`) is outside the brief. The follow-age field is a separate unknown. The hero shot (raid held) needs no second channel. |
| K14 | Something travels with the raid | ✓ | ✓ | ✓ | ✓ | ~ | ? | ✓ | ? | **Test (high)** | F6: a second live channel running the tool. F5: a single hop within 24 h is fine; Raid Torch's multi-day journey ✗. F8: shared backend + two channels is the heaviest setup. The lightest variant (X-6 Handoff card) needs the same second channel. G-7 stays parked. |
| K15 | Raid lands at a bad moment | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ | **Test (high)** | F6: a convincing video needs a real incoming raid (second channel). Manual trigger or CLI mock for rehearsal. |
| K16 | Raid ring for small streamers | ✓ | ✓ | ✓ | ✓ | ~ | ? | ✓ | ~ | **Test (high)** | F6: the ring can be demoed with our own 2–3 channels, but each must be live: the heaviest demo setup. F5: ring membership is configured in our app. |
| K17 | Tiered hints | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | **Pass** | Via Hint Airlock (G-1, no delete). Hint Jar (L1-5) needs the delete test (low). F7: both demos are puzzle games; use our own puzzle (a paper riddle, an escape-room box). |
| K18a | Timed chat-settings mode | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | **Test (low)** | Core = Update Chat Settings (`emote_mode`) and restoring the previous object. F7: the demo is a story game; use our own content. |
| K18b | Spoiler-hold filter | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | **Pass** | Via X-16 (held from the *streamer's* view; same core loop: protect the streamer from spoilers). L1-14's public-chat version needs the delete test (low). F7 as K18a. |
| K19 | Viewer plants, streamer sets off | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | **Test (high)** | Minefield and Sound Tags depend on local speech-to-text accuracy on casual speech (source: 1-hour spike). Sealing also needs the delete test (low). Try Not To Laugh and Sip Watch need webcam vision instead. |
| K20 | Chat reactions amplified | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Pass** | CC0 sound samples only. Lurker seats need Get Chatters (low). |
| K21 | Viewers write the brief, streamer performs | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Pass** | |
| K22a | Viewers drive the physical/camera setup | ✓ | ✓ | ✓ | ~ | ✓ | ✓ | ✓ | ✓ | **Pass** | Via Director's Chair, **only with discrete commands** ("zoom on hands"), not fine control: the director sees results 2–30 s late. Haunt needs a horror game (F7 ~: license-safe only). Desk Orchestra stays parked (hardware). |
| K22b | Collective-control toys | ✓ | ✓ | ✓ | ~ | ✓ | ✓ | ✓ | ✓ | **Pass** | Via Ouija (slow collective vote, latency-safe). Gravity Tetris carries K19's speech-to-text risk. Trio Jam: viewers hear loop changes 2–30 s late, which weakens the "jam". |
| K23 | Per-viewer souvenir moment | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ~ | **Pass** | F8 ~: obs-websocket screenshots plus hosting. Viewers need a **public link** to the image, so we need hosting or a tunnel (unlike EventSub WebSocket). The photo is the streamer's own frame; it expires in 24 h. |
| K24 | Chat-called replay review | ✓ | ✓ | ✓ | ~ | ✓ | ✓ | ✓ | ~ | **Pass** | F8 ~: replay-buffer capture, slow motion, latency offset, jury, stamp (spike needed). A 60 s buffer plus an offset covers latency. The titled clip is a bonus. |
| K25 | Chat-consensus clipping | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Test (low)** | Core = the broadcaster's own Create Clip on a new channel. The X-9 posts show confusion about the viewer-side clip button, not about the broadcaster API. |
| K26 | Sealed predictions | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Test (low)** | Sealing = the delete test. The native-Predictions version stays parked. |
| K27 | Per-channel earned status | ✓ | ✓ | ✓ | ✓ | ✗ | ~ | ✓ | ✓ | **Fail** | The mechanic *is* per-user memory across streams (levels, decay, streaks, monthly sky). A session-only version loses it. **Would need:** written confirmation (e.g. from TwitchDev) that derived per-user counters may be kept beyond 24 h. |
| K28 | Lurker presence made visible | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Pass** | Silent test accounts are the lurkers. Get Chatters (low). |
| K29 | Maker continuity check | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Pass** | |
| K30 | Viewer voicemail call-in | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ~ | **Pass** | Viewers record on our own web page. **Privacy and safety:** recording consent, a mod approval step before anything airs (unmoderated viewer audio on stream is a risk to the streamer), and deletion after the stream. |
| K31 | Shared Chat collab bridge | ✓ | ? | ✓ | ✓ | ✓ | ? | ✓ | ✓ | **Test (high)** | F2: Shared Chat eligibility for new channels is unknown. F6: a second live channel. Parked by its source; the weakest of the tested clusters. |
| K32 | GIF jukebox | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ? | ✓ | **Test (high)** | F2: unknown whether GIFs in chat work for new channels and test accounts. F7: third-party GIFs on video may carry rights issues. |
| K33 | Guest Star green room | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Test (high)** | F2: Guest Star is in beta, with unknown eligibility. Test accounts can be the callers. Parked by its source. |
| K34 | Missed hellos from another platform | ✓ | ✓ | ~ | ✓ | ✓ | ? | ~ | ? | **Test (high)** | F3 ~: YouTube API (authorized use). F6: needs a YouTube channel with live streaming enabled; in our understanding this can take about 24 h and phone verification (verify). F7: YouTube UI/trademark on video. F8: API quota and simulcast setup. |

---

## Summary

| Outcome | Count | Clusters |
| --- | --- | --- |
| Pass | 22 | K01a, K01b, K02, K03, K05, K06, K07, K09, K10, K11, K12a, K17, K18b, K20, K21, K22a, K22b, K23, K24, K28, K29, K30 |
| Test (low) | 5 | K08, K13, K18a, K25, K26 |
| Test (high) | 10 | K04, K12b, K14, K15, K16, K19, K31, K32, K33, K34 |
| Fail | 1 | K27 |

**37 clusters go to step 4.** The filter is deliberately lenient. It removes only certain blockers; uncertainty is carried forward as delivery risk.

## Full cards

Step 4 and wave 3 mostly look at cards, so each of the 25 full cards gets its own outcome here.

| Card | Source | Cluster | Outcome | Why |
| --- | --- | --- | --- | --- |
| Checkpoint | L1 | K01b | Pass | F7 ~ (IRL focus task) |
| Footnotes | L1 | K09 | Pass | Glossary authored in our panel |
| Previously On | L1 | K10 | Pass | F7 ~; real raid needs a second channel, manual trigger otherwise |
| Tap on the Shoulder | L1 | K06 | Pass | F8 ~; lamp optional |
| Hint Jar | L1 | K17 | Test (low) | Delete |
| Minefield | L2 | K19 | Test (high) | Speech-to-text accuracy; delete (low) |
| Studio Audience | L2 | K20 | Pass | Get Chatters (low) for seats |
| VAR! | L2 | K24 | Pass | F8 ~; replay-buffer spike |
| Desk Buddy | L2 | K03 | Pass | "Regular" = this session or badges |
| Photo Booth | L2 | K23 | Pass | F8 ~; public image hosting |
| Story So Far | L3 | K10 | Test (high) | Native pin on a new channel |
| Floor | L3 | K01a | Test (high) | Native pin on a new channel |
| Raid Torch | L3 | K14 | Test (high) | Second live channel; only a same-day version (multi-day journey fails F5) |
| Lit Medals | L3 | K27 | **Fail** | F5 |
| Chat Footnotes | L3 | K09 | Pass | |
| Hint Airlock | G | K17 | Pass | F7 ~ (own puzzle) |
| Soundcheck Relay | G | K06 | Pass | |
| Footnotes | G | K09 | Pass | |
| Foley Pit | G | K21 | Pass | |
| Continuity Crew | G | K29 | Pass | |
| Raid Gate | X | K13 | Test (low) | Chat-settings read on a foreign channel |
| One Line | X | K04 | Test (high) | Click-through window over a fullscreen game |
| Blind Minute | X | K18a | Test (low) | Chat-settings write and restore |
| Three Lines | X | K01a | Pass | |
| Ten Seconds | X | K08 | Test (low) | Ban/unban |

**Totals:** 15 Pass, 4 Test (low), 5 Test (high), 1 Fail.

### Variants outside the card table

| Variant | Result | Reason |
| --- | --- | --- |
| L2-12 Previously On, cold open (K10) | Fail | F5 |
| Raid Torch, multi-day journey (K14) | Fail | F5 |
| Desk Orchestra (K22a) | Fail | Hardware, parked by its source |
| Haunt (K22a) | ~ | Needs a license-safe horror game |
| Trio Jam (K22b) | ~ | Latency weakens the core feel |
| Gravity Tetris (K22b), Sound Tags (K19) | Test (high) | Speech-to-text |
| Try Not To Laugh, Sip Watch (K19) | Test (high) | Webcam vision |
| Bulb, lamp and printer variants (K03, K06, K11) | Hardware on hand? | Fallbacks exist for K03 and K06 |

## Day-1 test list (consolidated)

**Low risk** (documented standard operations; one short script or Twitch CLI session):

| Test | Clusters |
| --- | --- |
| Bot as moderator deletes a message within ~1 s | K17 (Hint Jar), K18b (L1-14), K19, K26 |
| Ban and unban within ~1 s | K08 |
| Update Chat Settings (`emote_mode`) and restore the previous object | K18a |
| Get Chat Settings for a channel we don't moderate (`follower_mode`, duration) | K13 |
| Get Chatters (`moderator:read:chatters`) | K20, K28 |
| Create Clip as broadcaster on a new channel | K25 (core); bonus for K02, K10, K24 |
| Create Clip `title`/`duration` parameters [S] | K19, K24 (titled clips) |
| Create Stream Marker (enable "store past broadcasts" first) | K07, K10, K19, K24 |
| Twitch CLI mock of `channel.raid` | K10, K15 rehearsal |

**High risk** (needs a spike or setup):

| # | Test | Clusters |
| --- | --- | --- |
| 1 | Pin Chat Message on a new channel, a pin every few minutes | K01a (Floor), K10 (Story So Far) |
| 2 | Local speech-to-text: keyword matching on casual speech (1-hour spike); caption-grade accuracy | K19 (Minefield, Sound Tags), K22b (Gravity Tetris), K12b |
| 3 | Click-through window over a fullscreen open-source game | K04 |
| 4 | Second live channel from a test account plus a real raid between the two | K14, K15, K16, K31; demo for K10, K13 |
| 5 | obs-websocket replay buffer and screenshot | K24, K23 |
| 6 | GIFs in chat on a new channel | K32 |
| 7 | Shared Chat and Guest Star eligibility | K31, K33 |
| 8 | YouTube channel live-enabled plus API | K34 |
| 9 | Modify Channel Information rate limit for frequent title changes | K10 (optional title sync) |
| 10 | Hardware on hand: smart bulb, lamp, thermal printer | K03, K06, K11 variants |

The earlier tests still apply as bonuses only: Create Custom Reward, Create Poll, and Create Prediction.

---

## Change log

**2026-10-25, after the review.** All 12 findings were accepted:
- **#1:** One F6 rule: a second channel we control = "?", real third parties = ✗. K16, K31 and K33 move from Fail to Test (high). K33's reason was corrected to F2 eligibility.
- **#2:** K25 moves to Test (low). K13 stays Test (low), with the stated basis.
- **#3:** K12b moves to Test (high). The speech-to-text test is now linked to K12b, K19 and Gravity Tetris.
- **#4:** The full-card table was added, and the contradictory sentence removed.
- **#5:** The variant rule now requires the variant to keep the core loop. K04 is unchanged: the phone page is a different loop. K18b passes via X-16. K22a passes with discrete commands only.
- **#6:** F5 "~" for K11 (Name Card) and K03 (regulars).
- **#7:** The F3 boundary now covers third-party APIs; gated doubts moved to F2.
- **#8:** F8 "~" for K06, K23 and K24.
- **#9:** The day-1 list was split and completed with cluster links.
- **#10:** Setup and privacy notes for K23, K30 and K34, and hardware added to the day-1 list.
- **#11:** One F7 definition.
- **#12:** Resolved through #1 and #2.
