# Evidence step: rules (written before any results)

Pre-registered 2026-10-26, before any evidence came in. These rules are not changed after seeing results; any exception is logged here with a reason.

## Purpose

Settle two unknowns before scoring the 10 cards in [../cards.md](../cards.md):
1. **Does it already exist?** This feeds Innovation.
2. **Do people want it, and who is it for?** This feeds Impact.

Nobody scores in this step. Researchers only gather evidence.

## Sources

| Researcher | File given | Source priority | Result file |
| --- | --- | --- | --- |
| Grok | `paste-grok.md` (removed after use; see git history) | X first, then web | evidence-grok.md |
| GPT 6 Astra | `paste-astra.md` (removed after use; see git history) | Its own web search | evidence-astra.md |
| Claude agent | `paste-claude.md` (removed after use; see git history) | GitHub, Devpost, Reddit, Twitch Extensions | evidence-claude.md |

The three prompts are identical except for the last paragraph. Grok and Astra run in new chats with no file access. The Claude agent reads only its paste file. The card text in the prompts was extracted from cards.md by script (one-liner, best variant, core loop, named competitors), so no card is described differently from another.

## Merging the three reports

- **Competitors** are merged by name. A competitor found by two or three researchers counts as confirmed. One found by a single researcher is checked by opening its link; if the link fails, it is dropped.
- **Overlap** is the highest level that survives the check.
- **Demand and counter-signals** are counted per card, after removing duplicates and dead links.
- **Audience fit** is taken where the researchers agree; disagreements are listed for the user.
- Output: `aggregate.md`, one section per card plus a summary table.

## What happens when something similar exists

Two questions decide it: how much does it overlap, and how well-known is it?

**Well-known** means at least one of:
- a product or feature of a major streaming platform or tool (Twitch itself, StreamElements, Streamlabs, Streamer.bot, Elgato, OBS, Meld, Sound Alerts, StreamUP);
- ≥1,000 users or installs shown on its page;
- ≥100 GitHub stars;
- a post or video about it with ≥10,000 views.

| Finding | Action |
| --- | --- |
| `Same core loop` + well-known | **One pivot chance.** I write a pivot that changes at least one core-loop step the competitor lacks. The change must be visible in the first 20 s of the video and fit the 15 h budget. The user approves or rejects it. Without an approved pivot, the card is **not eliminated**: it goes to scoring as it is, and its competitor is shown to the raters. |
| `Same core loop` + not well-known | No pivot required. The card names the competitor and states its difference. |
| `Partial` or `Adjacent` | Normal case. The difference is written into the card. |

A similar product that people use is also recorded as a **demand signal** for Impact.

"Same core loop" means the same input (who acts), the same trigger and the same output on stream. I propose the level with links; the user decides any disputed case.

## Order

Evidence → merge (`aggregate.md`) → pivots, if any (logged in cards.md revision log) → scoring with evidence. A pivoted card enters scoring in its new form. Each card gets at most one pivot.

## Exceptions logged after the results (2026-10-28)

- **Eliminations:** the user eliminated Previously On, Photo Booth and Foley Pit after reading the three reports, although this README says evidence alone does not eliminate a card. Reasons are in [aggregate.md](aggregate.md).
- **Targeted link check:** single-source competitors were checked only for the 6 cards still in play ([linkcheck.md](linkcheck.md)), by a Sonnet subagent. Checkpoint's competitors were rechecked by the pivot draft instead.
- **Unverifiable is not dead:** Reddit, X, Devpost and some news sites refused automated fetches. Competitors behind such links were not counted as confirmed (PROVE IT, Raid Train and Twitch Sense were dropped). Demand links behind them are listed as "unverified", not removed.
- **Checkpoint pivot:** the user ruled Checkpoint the same core loop as Meld X AMA Question Queue (only Astra had said so) and approved pivot C from [../pivots/checkpoint-draft.md](../pivots/checkpoint-draft.md). Its post-pivot difference rests on one source.
