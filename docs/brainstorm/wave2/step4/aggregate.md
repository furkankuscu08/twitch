# Step 4 aggregate (quality gate)

Raters: Opus 5.5 ([rating-opus.md](rating-opus.md)), GPT 6 Astra ([rating_astra.md](rating_astra.md)), Grok ([rating_grok.md](rating_grok.md)). All blind.

## Rule used

**Eliminate a candidate if at least 2 of the 3 raters gave it at least one FATAL** (verdict Keep (flag) or Eliminate). Proposed by the user on 2026-10-26, after the ratings were in.

This replaces the rule in [key.md](key.md) (eliminate only if 2 raters say Eliminate, i.e. 2+ FATAL each). That rule would have cut only 4 of 37 (C02, C15, C22, C32), because Astra and Grok almost never gave two FATALs to one idea. The goal for this step was ~12–15 survivors.

Robustness check: for all 17 eliminated candidates, at least 2 raters flagged the **same question** (15 on Q1 Innovation, 2 on Q4 Technical). A stricter "same weakness" rule gives the identical result.

## Per-candidate table

O / A / G = number of FATALs from Opus / Astra / Grok. "Raters" = how many raters gave ≥1 FATAL.

| C | K | Name | O | A | G | Raters | Shared FATAL | Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C01 | K28 | Lurker presence | 0 | 1 | 0 | 1 | | Go on |
| C02 | K33 | Guest Star | 2 | 2 | 1 | 3 | Q1 ×3 | **Out** |
| C03 | K04 | One line | 1 | 1 | 0 | 2 | Q1 ×2 | **Out** (borderline) |
| C04 | K16 | Raid ring | 2 | 1 | 1 | 3 | Q1 ×3 | **Out** |
| C05 | K15 | Raid at a bad moment | 3 | 0 | 0 | 1 | | Go on |
| C06 | K25 | Consensus clip | 1 | 1 | 1 | 3 | Q1 ×3 | **Out** |
| C07 | K24 | Replay review (VAR) | 0 | 0 | 0 | 0 | | Go on |
| C08 | K20 | Reactions amplified | 0 | 0 | 0 | 0 | | Go on |
| C09 | K19 | Viewer plants / streamer triggers | 0 | 0 | 0 | 0 | | Go on |
| C10 | K02 | Bookmark | 2 | 0 | 0 | 1 | | Go on |
| C11 | K12b | Captions | 1 | 1 | 1 | 3 | Q1 ×3 | **Out** |
| C12 | K03 | Glanceable chat state | 0 | 0 | 1 | 1 | | Go on |
| C13 | K09 | Lore footnotes | 0 | 0 | 0 | 0 | | Go on |
| C14 | K34 | Missed hellos | 1 | 1 | 1 | 3 | Q1 ×3 | **Out** |
| C15 | K31 | Shared Chat | 3 | 2 | 1 | 3 | Q1 ×3 | **Out** |
| C16 | K21 | Viewers write brief / streamer performs | 1 | 0 | 0 | 1 | | Go on |
| C17 | K01b | Focus capture | 0 | 1 | 0 | 1 | | Go on |
| C18 | K26 | Sealed predictions | 1 | 0 | 0 | 1 | | Go on |
| C19 | K22a | Viewers drive camera | 1 | 1 | 1 | 3 | Q1 ×3 | **Out** |
| C20 | K14 | Raid carries something | 1 | 0 | 0 | 1 | | Go on |
| C21 | K32 | GIF jukebox | 2 | 1 | 1 | 3 | Q1 ×3 | **Out** |
| C22 | K18a | Timed chat mode | 2 | 1 | 2 | 3 | Q1 ×3 | **Out** |
| C23 | K18b | Spoiler hold | 0 | 0 | 0 | 0 | | Go on |
| C24 | K06 | Production problems | 0 | 0 | 0 | 0 | | Go on |
| C25 | K30 | Voicemail | 0 | 0 | 0 | 0 | | Go on |
| C26 | K10 | "You are here" | 0 | 1 | 0 | 1 | | Go on |
| C27 | K11 | Newcomer welcome | 0 | 0 | 0 | 0 | | Go on |
| C28 | K17 | Tiered hints | 0 | 0 | 0 | 0 | | Go on |
| C29 | K12a | Translation | 1 | 1 | 1 | 3 | Q1 ×3 | **Out** |
| C30 | K23 | Souvenir | 0 | 0 | 0 | 0 | | Go on |
| C31 | K01a | Question queue | 1 | 1 | 1 | 3 | Q1 ×3 | **Out** |
| C32 | K05 | Private filtered view | 2 | 1 | 2 | 3 | Q1 ×3 | **Out** |
| C33 | K22b | Collective toys | 2 | 0 | 1 | 2 | Q1 ×2 | **Out** (borderline) |
| C34 | K29 | Continuity check | 2 | 0 | 0 | 1 | | Go on |
| C35 | K08 | Mobile mod undo | 2 | 1 | 1 | 3 | Q4 ×3 | **Out** |
| C36 | K13 | Raid pre-check | 1 | 1 | 1 | 3 | Q4 ×3 | **Out** |
| C37 | K07 | Mod panel | 1 | 1 | 1 | 3 | Q1 ×3 | **Out** |

**Result:** 17 out, 20 go on. 10 of the 20 got no FATAL from anyone.

## Survivors (20)

- **Clean (0 FATAL from all three), 10:** K24 VAR, K20, K19 Minefield, K09 Footnotes, K18b, K06 Tap, K30 Voicemail, K11, K17 Hint Jar, K23 Souvenir.
- **One rater flagged, 10:** K28 (A: Q1), K15 (O: Q1, Q3, Q4), K02 (O: Q2, Q4), K03 (G: Q1 chat pet), K21 (O: Q3 one-off), K01b (A: Q1), K26 (O: Q1), K14 (O: Q3 needs both sides), K10 (A: Q1 "what did I miss"), K29 (O: Q2, Q3).

Flags travel with each survivor into step 5.

## Top 5 lists (not used for elimination)

| Candidate | Opus | Astra | Grok | Votes |
| --- | --- | --- | --- | --- |
| C07 K24 VAR | 2 | 1 | 4 | 3 |
| C09 K19 Minefield | 1 | 2 | 2 | 3 |
| C28 K17 Tiered hints | 5 | 3 | | 2 |
| C20 K14 Raid carries something | | 5 | 5 | 2 |
| C13 K09 Lore footnotes | 3 | | | 1 |
| C24 K06 Production problems | 4 | | | 1 |
| C08 K20 Reactions amplified | | 4 | | 1 |
| C16 K21 Brief / perform | | | 1 | 1 |
| C26 K10 "You are here" | | | 3 | 1 |

All nine survive.

## Factual checks on rater reasons and notes

No FATAL that decided an elimination rests on a wrong fact. Notes to carry forward:

| Note | Raters | Status |
| --- | --- | --- |
| Delete-to-seal is not secret: a deleted message is briefly visible and stays in mod logs (C09, C18, C28; C23 for spoilers). | O, A | **Valid.** Sealed input should go through whisper or a web form. Design fix, not a FATAL. |
| Get Chatters lists accounts connected to chat, not everyone watching (C01 K28). | A, G | **Valid.** Logged-out viewers never appear. Narrow the claim to "logged-in lurkers". |
| Pinned Chat API may not exist (C26, C31). | O | **Wrong per L3's check:** GA 2026-05-29, `pin: true` on Send Chat Message. Still on the day-1 test list. Not used in any FATAL. |
| Create Clip tops out at 60 s, so "~85 s" is wrong (C06). | O, G | **Valid.** C06 is out anyway. |
| "24-hour data rule" source unclear (C20, C30). | A | Our source is the Twitch Developer Agreement. No change. |
| GIFs in Twitch chat unverified (C21). | O | Already Test (high). C21 is out. |

## Deviations from plan

- Rule changed after the ratings were seen (see top). The old rule is kept in key.md for the record.
- The rubric's criteria text was shortened from rules.md: Innovation dropped "How creative and novel is the concept", Technical dropped "How well is it built". Q4 partly covers build quality. Wave 3 cards must quote rules.md §6 verbatim.
