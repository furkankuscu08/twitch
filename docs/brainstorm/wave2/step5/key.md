# Step 5a key (DO NOT give to raters)

Random order, seed 20261027. R = this step, C = step 4 ID, K = cluster.

| R | C | K | Name |
| --- | --- | --- | --- |
| R01 | C28 | K17 | Tiered hints |
| R02 | C17 | K01b | Focus capture, surfaced at a break |
| R03 | C30 | K23 | Per-viewer souvenir moment |
| R04 | C26 | K10 | "You are here" context for late arrivals and raiders |
| R05 | C08 | K20 | Chat reactions amplified |
| R06 | C20 | K14 | Something travels with the raid |
| R07 | C10 | K02 | Bookmark a moment for later |
| R08 | C27 | K11 | Newcomer welcome and orientation |
| R09 | C18 | K26 | Sealed predictions |
| R10 | C25 | K30 | Viewer voicemail call-in |
| R11 | C16 | K21 | Viewers write the brief, the streamer performs it |
| R12 | C07 | K24 | Chat-called replay review |
| R13 | C13 | K09 | Lore footnotes |
| R14 | C34 | K29 | Maker continuity check |
| R15 | C12 | K03 | Glanceable chat state in the room |
| R16 | C01 | K28 | Lurker presence made visible |
| R17 | C23 | K18b | Spoiler-hold filter |
| R18 | C05 | K15 | Raid lands at a bad moment |
| R19 | C09 | K19 | Viewer plants it, the streamer sets it off |
| R20 | C24 | K06 | Production problems reach the streamer |

## Aggregation rule (fixed before any score was seen, 2026-10-26)

- Raters: Opus 5.5 (new, independent Claude subagent), GPT 6 Astra, Grok. All blind: rubric.md and candidates.md are their only input. No web search.
- **Score:** each rater gives 0–5 on Innovation, Impact, Technical and Design (0–20 per rater). The final score is the sum over the three raters (**0–60**). Final order is by this sum.
- **Pass:** the top 10 by final score.
- **Rescue:** ranks 11–14 also pass if at least one rater has the candidate in their Top 5.
- **Ties at the cut:** broken by the summed Innovation score (as in the official rules), then by the number of raters with the candidate in their Top 5. If still tied, all tied candidates pass.
- **User marks** (recorded in shortlist-20.md before the scores are shown): ★ always passes, ✗ is always out.
- Expected result: 10–13 candidates.
- **Checks, reported but not deciding:** (a) per-rater mean and spread; if one rater's spread is much larger than the others', a per-rater normalized order is shown next to the raw one; (b) any criterion where two raters differ by 3 or more on the same candidate is flagged for discussion.
- The aggregator (Claude main session) does not score. It may only flag reasons that are factually wrong about Twitch, with evidence, and report them to the user.

## Changes to step 4 descriptions

Known design fixes from step 4, applied before scoring:
- C09, C18, C28: sealing by whisper or web form instead of deleting the chat message (deletion is not secret).
- C23: spoilers held only from the streamer's own view (the public-chat variant needs deletion after posting).
- C01: lurkers limited to logged-in accounts connected to chat.
- C20: the 24 h rule's source named (Twitch Developer Agreement).
