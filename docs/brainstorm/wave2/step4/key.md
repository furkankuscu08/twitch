# Step 4 key (DO NOT give to raters)

Random order, seed 20261026.

| Candidate | Cluster |
| --- | --- |
| C01 | K28 |
| C02 | K33 |
| C03 | K04 |
| C04 | K16 |
| C05 | K15 |
| C06 | K25 |
| C07 | K24 |
| C08 | K20 |
| C09 | K19 |
| C10 | K02 |
| C11 | K12b |
| C12 | K03 |
| C13 | K09 |
| C14 | K34 |
| C15 | K31 |
| C16 | K21 |
| C17 | K01b |
| C18 | K26 |
| C19 | K22a |
| C20 | K14 |
| C21 | K32 |
| C22 | K18a |
| C23 | K18b |
| C24 | K06 |
| C25 | K30 |
| C26 | K10 |
| C27 | K11 |
| C28 | K17 |
| C29 | K12a |
| C30 | K23 |
| C31 | K01a |
| C32 | K05 |
| C33 | K22b |
| C34 | K29 |
| C35 | K08 |
| C36 | K13 |
| C37 | K07 |

## Aggregation rule (fixed before any rating was seen, 2026-10-26)

- Raters: Opus 5.5 (Claude subagent), GPT 6 Astra, Grok. All work blind: the rubric and candidates are their only input.
- **A candidate is eliminated only if at least 2 of the 3 raters give it "Eliminate"** (2 or more FATAL).
- All other candidates go on to step 5. Every FATAL reason travels with them as a flag.
- The aggregator (Claude main session) does not vote. It may only mark a rater's reason as **factually wrong** about Twitch, with evidence. Such a case is reported to the user, never silently overridden.
- Top-5 lists are recorded separately. They are not used for elimination.

## Amendment (2026-10-26, after ratings)

The user replaced the rule above with: **eliminate if at least 2 of the 3 raters gave at least one FATAL.** The original rule would have cut only 4 of 37. See [aggregate.md](aggregate.md).
