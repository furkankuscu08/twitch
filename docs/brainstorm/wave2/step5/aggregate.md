# Step 5a aggregate

**Decision (user, 2026-10-26):** the pre-registered rule in [key.md](key.md) is applied as is. No user marks (★/✗). **10 candidates go on** (the "pass" rows below); the other 10 are out. Features from some eliminated candidates are carried into survivors: see [../shortlist-10.md](../shortlist-10.md).

The table was first shown to the user as a simulation, before the decision.

## Scores (sum of Opus + Astra + Grok, 0–60)

Criterion columns are sums over the three raters (0–15 each). Z-rank = order after normalizing each rater's totals.

| # | R | K | Name | Total | O / A / G | Inn | Imp | Tech | Des | Top 5 | Z-rank | Rule |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | R19 | K19 | Minefield | 54 | 19 / 18 / 17 | 14 | 12 | 13 | 15 | 3 | 1 | pass |
| 2 | R20 | K06 | Production problems | 49 | 16 / 17 / 16 | 12 | 15 | 11 | 11 | 3 | 3 | pass |
| 3 | R12 | K24 | VAR | 49 | 16 / 17 / 16 | 11 | 10 | 13 | 15 | 3 | 2 | pass |
| 4 | R06 | K14 | Raid carries something | 46 | 15 / 15 / 16 | 14 | 9 | 11 | 12 | 2 | 4 | pass |
| 5 | R04 | K10 | Previously On | 45 | 16 / 14 / 15 | 11 | 11 | 11 | 12 | 1 | 5 | pass |
| 6 | R05 | K20 | Studio Audience | 45 | 15 / 15 / 15 | 9 | 11 | 11 | 14 | 0 | 6 | pass |
| 7 | R11 | K21 | Foley Pit | 44 | 13 / 15 / 16 | 14 | 8 | 8 | 14 | 1 | 7 | pass |
| 8 | R01 | K17 | Tiered hints | 43 | 14 / 15 / 14 | 12 | 10 | 9 | 12 | 1 | 8 | pass |
| 9 | R03 | K23 | Photo Booth | 40 | 13 / 16 / 11 | 8 | 9 | 10 | 13 | 1 | 9 | pass |
| 10 | R02 | K01b | Checkpoint | 39 | 13 / 11 / 15 | 9 | 11 | 9 | 10 | 0 | 10 | pass (tie with R15, won on Innovation 9 vs 8) |
| 11 | R15 | K03 | Desk Buddy | 39 | 14 / 13 / 12 | 8 | 10 | 10 | 11 | 0 | 11 | out (no Top 5) |
| 12 | R10 | K30 | Voicemail | 38 | 13 / 12 / 13 | 8 | 9 | 9 | 12 | 0 | 12 | out (no Top 5) |
| 13 | R13 | K09 | Lore footnotes | 35 | 14 / 10 / 11 | 9 | 9 | 7 | 10 | 0 | 13 | out (no Top 5) |
| 14 | R14 | K29 | Continuity check | 29 | 9 / 11 / 9 | 8 | 6 | 7 | 8 | 0 | 15 | out (no Top 5) |
| 15 | R09 | K26 | Sealed predictions | 29 | 8 / 11 / 10 | 5 | 7 | 6 | 11 | 0 | 14 | out |
| 16 | R08 | K11 | Newcomer welcome | 28 | 9 / 9 / 10 | 5 | 8 | 6 | 9 | 0 | 16 | out |
| 17 | R07 | K02 | Bookmark | 26 | 8 / 9 / 9 | 6 | 7 | 6 | 7 | 0 | 18 | out |
| 18 | R17 | K18b | Spoiler hold | 26 | 8 / 8 / 10 | 6 | 9 | 7 | 4 | 0 | 17 | out |
| 19 | R16 | K28 | Lurker lanterns | 24 | 10 / 6 / 8 | 6 | 5 | 6 | 7 | 0 | 19 | out |
| 20 | R18 | K15 | Raid at a bad moment | 22 | 7 / 9 / 6 | 3 | 7 | 6 | 6 | 0 | 20 | out |

**Would pass (10):** R19, R20, R12, R06, R04, R05, R11, R01, R03, R02. No rescues: none of ranks 11–14 is in any Top 5.

## Checks

- **Rater calibration:** means 12.5 / 12.6 / 12.4, spreads 3.3 / 3.3 / 3.2. Nearly identical, so normalization changes nothing at the cut.
- **Disagreement (≥3 on one criterion):** none.
- **Cut sensitivity:** R02 and R15 tie at 39 (Innovation decides by 1 point); R10 is 1 point behind. Ranks 10–12 are effectively a tie.
- **Top 5 lists:** R19, R20, R12 are in all three; R06 in two; R04, R11, R03, R01 in one.

## Notes from raters, assessed

| # | Note | Rater | Assessment | Affects |
| --- | --- | --- | --- | --- |
| 1 | R01, R09 and R19 share the sealed whisper/web-form intake. | O, G | **Valid, and important.** Our own wave-1 research (A-capabilities) found that whispers need a phone-verified sender, are capped (40 recipients/day, may be silently dropped), and inventory parked "whisper ballots" for this reason. The web-form fallback needs public hosting and a Twitch login to know who planted what. This fix was added by us in step 5; it now carries a real build and demo cost. | R19, R01 (passing) |
| 2 | Create Clip clips from Twitch's own stream, not the local OBS replay; a clip title may not be settable. | O | **Valid.** The on-stream replay and the Twitch clip are separate pieces. Clip title/duration is already on the day-1 test list. The clip is a bonus, not the core. | R12 |
| 3 | The Pinned Chat API may not exist. | O | **Wrong per our wave-2 check** (L3: GA 2026-05-29, `pin: true` on Send Chat Message). Still untested on a new channel. Only the variant needs it; the "Previously on" card does not. | R04 |
| 4 | The "24 h" rule is broader than Twitch's actual wording. | A, O | **Partly fair.** The Developer Agreement (IV.C, per A-capabilities) restricts storing *Twitch Content* unless authorized or cached ≤24 h. A torch that stores only our own state (channel IDs, counts) might be allowed beyond 24 h. Worth reading the clause: it could unlock the multi-day torch journey. | R06 |
| 5 | Get Chatters needs a moderator token, includes bots, and is not "people watching". | O, A | **Valid.** Filter bots; narrow the claim. | R16 (out) |
| 6 | A tool cannot hide lines from native Twitch chat; R17 only works in a custom view. | O | **Valid** (that is what "own chat view" means). | R17 (out) |
| 7 | Speech-to-text may detonate by accident or miss. | A | **Valid.** Already the STT spike; add false-positive handling (word boundaries, confirm window). | R19 |
| 8 | Weakest criteria: R20 Technical (G: "a keyword threshold plus a cue"), R11 Technical (O, G), R06 Impact (all), R12 Impact (O, G). | all | Inputs for step 6 card work: each passing idea has one clear weak spot to strengthen. | several |
