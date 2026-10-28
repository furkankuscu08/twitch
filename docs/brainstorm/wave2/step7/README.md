# Step 7: scoring the 7 remaining cards (rules written before any scores)

Pre-registered 2026-10-28, before any rater saw the cards. These rules are not changed after seeing scores; any exception is logged at the end with a reason.

## Purpose

Score the 7 cards left after the evidence step on the four official criteria, so the user can choose finalists. **Scoring does not eliminate anything.** The user chooses.

Cards: Minefield, Tap on the Shoulder, VAR, Raid Torch, Studio Audience, Hint Jar, Checkpoint (revision 3 of [../step6/cards.md](../step6/cards.md)).

## Raters

| Rater | File given | How it runs | Result file |
| --- | --- | --- | --- |
| Grok | [paste-grok.md](paste-grok.md) | New chat, no file access, no search | results-grok.md |
| GPT 6 Astra | [paste-astra.md](paste-astra.md) | New chat, no file access, no search | results-astra.md |
| Claude agent (Opus, high effort) | [paste-claude.md](paste-claude.md) | Reads only its paste file; no search, no subagents | results-claude.md |

The three files are identical except for one sentence about search tools and the **card order**, which is shuffled per rater (fixed seeds 11, 22, 33) so no card always comes first:

| Rater | Order |
| --- | --- |
| Grok | Tap on the Shoulder, Minefield, VAR, Hint Jar, Checkpoint, Studio Audience, Raid Torch |
| Astra | Hint Jar, VAR, Studio Audience, Raid Torch, Minefield, Checkpoint, Tap on the Shoulder |
| Claude | Raid Torch, Minefield, Checkpoint, VAR, Hint Jar, Tap on the Shoulder, Studio Audience |

## What the raters see

- The four official criteria, verbatim, with equal weight, and the judging format (video under 3 minutes).
- The build conditions: 15 hours, 1 streamer + 3 test accounts, no commercial games or music, and the option of a small Codex-built original game or an MIT-licensed game (about 1 h).
- Shared base, how Codex is used, Twitch facts, and the day-1 tests for these 7 cards.
- Each card from cards.md revision 3, extracted by script: everything **except** the "Strengthening" section (the card's own advocacy) and the "Best variant" line (internal history).
- Each card's section of [../step6/evidence/aggregate.md](../step6/evidence/aggregate.md), placed right after the card, with the evidence legend.

## What the raters do not see

- Strengthening sections, earlier scores (step 5a), my impressions, the other raters' scores.
- The eliminated cards.
- The web: no search, so all three judge the same evidence.

## Scale

1–5 per criterion; 2 and 4 sit between the anchors.

| Criterion | 5 | 3 | 1 |
| --- | --- | --- | --- |
| Innovation | Nothing similar was found; the loop is new | A new combination of existing parts, with a difference that shows in the video | The same as a well-known product |
| Impact | The problem or desire is strongly evidenced, in common stream types, and the tool would be used every week | A real problem but a narrow audience, or only indirect evidence | No evidence; niche |
| Tech | Can be built well in 15 h, technically interesting, and Codex's role is concrete | Buildable but ordinary, or interesting but risky | Trivial, or does not fit 15 h |
| Design | Understood within the first 20 s of the video and fun to watch even with three test accounts | Understandable but visually ordinary | Confusing, or flat on video |

Each score needs a 1–2 sentence reason. Risk (Low / Medium / High, naming the day-1 test) is rated separately and is not part of the total. Each rater also ranks all 7 cards.

## Combining the scores

1. **Criterion score:** the median of the three raters.
2. **Total:** the sum of the four medians (maximum 20), equal weight as in the official rules.
3. **Disagreement:** if the three raters' scores on a criterion span 2 or more points, the card is flagged and the reasons are shown side by side. The median still stands unless the user decides otherwise.
4. **Order of the table:** by total; ties broken first by lower median risk, then by the median of the raters' rankings.

## Output

- `results-grok.md`, `results-astra.md`, `results-claude.md`: the raw answers, unedited.
- `ranking.md` (written by me): the combined table, and for each card what each rater said, flagged disagreements, and my own view, kept separate from the raters'. It ranks all 7 cards and eliminates none. The user picks the finalists.

After the user's pick: day-1 tests for the finalists that depend on one (T1/T1b, T3), then the final choice.

## Exceptions

None yet.
