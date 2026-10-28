# Step 7: combined ranking

Written 2026-10-28 from [results-grok.md](results-grok.md), [results-astra.md](results-astra.md) and [results-claude.md](results-claude.md), using the rules in [README.md](README.md). By the user's decision, the total uses the **mean** of the three raters, not the median; see the exception in the README. **Nothing is eliminated here; the user picks the finalists.**

Codes: G = Grok, A = GPT 6 Astra, C = Claude agent (Opus, high). Risk: L / M / H.

## Combined table

Each cell shows the mean, with the three raw scores in brackets (G / A / C). The total is the sum of the four means, which equals the mean of the three raters' totals. Risk and rank still use the median, because the tie-breakers were not changed.

| # | Card | Innovation | Impact | Tech | Design | **Total** | Risk (median) | Rank (median) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Minefield | 5.0 (5/5/5) | 3.0 (3/3/3) | 3.3 (3/3/4) | 5.0 (5/5/5) | **16.3** | H (H/H/M) | 1 (1/2/1) |
| 2= | Checkpoint | 3.7 (3/4/4) | 4.0 (4/4/4) | 3.3 (3/3/4) | 4.0 (4/4/4) | **15.0** | M (M/H/M) | 3 (4/3/2) |
| 2= | VAR | 3.0 (3/3/3) | 3.0 (3/3/3) | 4.0 (4/4/4) | 5.0 (5/5/5) | **15.0** | M (M/M/M) | 3 (3/4/3) |
| 4 | Hint Jar | 4.0 (4/4/4) | 3.0 (3/3/3) | 3.3 (3/4/3) | 4.3 (4/5/4) | **14.7** | L (L/L/L) | 4 (5/1/4) |
| 5 | Tap on the Shoulder | 3.0 (3/3/3) | 3.7 (4/4/3) | 3.7 (4/4/3) | 4.0 (4/4/4) | **14.3** | M (M/M/L) | 5 (2/5/5) |
| 6 | Studio Audience | 3.0 (3/3/3) | 3.0 (3/3/3) | 3.7 (4/4/3) | 3.3 (3/4/3) | **13.0** | L (L/L/L) | 6 (6/6/7) |
| 7 | Raid Torch | 4.0 (4/4/4) | 2.3 (2/3/2) | 3.0 (3/3/3) | 3.0 (3/3/3) | **12.3** | H (H/H/H) | 7 (7/7/6) |

Raw totals per rater:

| Card | G | A | C | Mean | (Median, the original rule) |
| --- | --- | --- | --- | --- | --- |
| Minefield | 16 | 16 | 17 | 16.3 | 16 |
| Checkpoint | 14 | 15 | 16 | 15.0 | 15 |
| VAR | 15 | 15 | 15 | 15.0 | 15 |
| Hint Jar | 14 | 16 | 14 | 14.7 | 14 |
| Tap on the Shoulder | 15 | 15 | 13 | 14.3 | 15 |
| Studio Audience | 13 | 14 | 12 | 13.0 | 13 |
| Raid Torch | 12 | 13 | 12 | 12.3 | 12 |

## What the numbers say

- **Moving to the mean changes one place.** Hint Jar (14.7) moves above Tap on the Shoulder (14.3). Under the median, Tap was 15 and Hint Jar 14. The reason: under the mean, C's lower scores pull Tap down and A's higher scores lift Hint Jar, while the median ignored both outliers. Every other position stays the same.
- **No disagreement flags.** On every card and criterion the three scores span at most 1 point, so the ≥2 rule never triggers. Innovation and Design are almost unanimous. The differences are in Tech and Risk.
- **The tie at 15.0 remains.** Checkpoint and VAR both have median risk M and median rank 3, so the registered tie-breakers cannot separate them. They share second place; see the exception in [README.md](README.md). For information only: if risk were also averaged, VAR (2.0) would come before Checkpoint (2.3).
- **14.3–16.3 is a narrow band.** The difference between the top five cards comes down to a few single 3-versus-4 scores. The clear split is between the top five and the bottom two (12.3–13.0).
- **The bottom two share a cause.** For both Studio Audience and Raid Torch, all three raters say the core promise cannot be shown with one streamer and three accounts: Studio Audience's crowd scaling and Raid Torch's community relay.
- **Checkpoint's place depends partly on the Claude rater.** Without C, the average of G and A is: Minefield 16; VAR, Tap and Hint Jar 15; Checkpoint 14.5. C is the most generous rater on Checkpoint (16) and on Minefield (17), and under the mean those scores count in full. The Claude rater may favour Checkpoint: I (Claude) drafted the Checkpoint pivot. Checkpoint's post-pivot evidence also has a single source (P).

## Per card: what the raters said

### 1. Minefield: 16.3, risk H

- **G:** Innovation 5: "the loop the search actually missed". Tech 3: T1's bar is unmet, and "a miss or a bogus boom is the product". Risk H: there is no fallback spotter, and faster-whisper hotword hallucinations are a verified failure mode. Ranked #1.
- **A:** Same scores. Says DEFUSE "does not compensate for frequent detection errors". Also says the 20-minute playtest must show that unscripted baiting works. Ranked #2, behind Hint Jar, because the speech detection is untested.
- **C:** Tech 4, Risk M, because DEFUSE and the blocklist soften misfires. Agrees the card has no fallback if T1 fails. Ranked #1.
- **Agreement:** All three see it as the most novel loop of the seven and the most watchable in the first 20 seconds. All three say the whole card stands or falls on T1.

### 2=. Checkpoint: 15.0, risk M

- **G:** Innovation 3: a featured queue question is well known (Meld, StreamerQnA). The difference is the spoken answer typing onto the card plus the threaded quote. Impact 4: Streamlabs documents the manual version as a weekly habit. Ranked #4.
- **A:** Innovation 4. Risk H: the pause-trigger fallback "is insufficiently specified". Biggest weakness: an early close or a confidently wrong transcript sends a wrong answer "under the streamer's apparent authority". Design: useful, but "less immediately theatrical" than an explosion or a replay. Ranked #3.
- **C:** 4 on every criterion. "Without the voice receipt it is Meld's question queue." Ranked #2.
- **Agreement:** the strongest Impact case in the set (4/4/4). Both the novelty and the demo depend on T1b.

### 2=. VAR: 15.0, risk M

- **G, A and C give identical scores:** Innovation 3, Impact 3, Tech 4, Design 5, risk M. It is the only fully unanimous card.
- **G:** "The most broadcast-like tape in the set." The weakness is the automatic stoppage, which goes against a streamer who wants to control when a replay plays.
- **A:** T5 must also show that the clip actually contains the review, because the Create Clip window is uncertain.
- **C:** "A judge may read it as polish rather than a new idea."
- **Agreement:** the most fun to watch, with the most build slack (8.5 h). Its novelty is a combination of existing replay and poll tools.

### 4. Hint Jar: 14.7, risk L

- **A:** Tech 4, Design 5, ranked **#1**: "the clearest path to a polished, credible three-account demonstration".
- **G and C:** Tech 3 ("ordinary web plumbing") and Design 4. Ranked #5 and #4.
- **Agreement:** It is the only card that all three rate Low risk. All three name the same weakness: the Limbus thread itself says rules and bans already handle backseating.

### 5. Tap on the Shoulder: 14.3, risk M

- **G:** Impact 4, Tech 4. Ranked #2, because the pain is documented and the demo needs only a mic, a spare phone and three accounts.
- **A:** Same scores as G, but ranked #5: "less distinctive and theatrical". Calm mode, the strongest argument for everyday use, is outside the MVP.
- **C:** Impact 3: real failures are rare, and well-known plugins already cover the mute case. Tech 3: mostly integration. Risk L. Ranked #5.
- **Note:** G and A each give it 15, yet A ranks it 5th. The criteria look solid one by one, but two raters judge it unlikely to win overall.

### 6. Studio Audience: 13.0, risk L

- All three rate it the surest build. All three agree the crowd scaling can only be shown as a labelled simulation. Sound-spam and "canned laughter" concerns count against weekly use. Ranked 6 / 6 / 7.

### 7. Raid Torch: 12.3, risk H

- Innovation is 4 from all three raters, because the visible object carried between channels is new. G and C give Impact 2: nobody asked for it, both sides have to adopt it, and hate-raid wariness counts against it. T3 is the most fragile day-1 test. Ranked 7 / 7 / 6.

## My view (separate from the raters)

These are my opinions, not part of the scores.

1. **Minefield is the only card that could win outright rather than just place.** It is the only card that all three raters score 5 on both Innovation and Design, the criteria a three-minute video sells. The raters are right that it has no fallback. **T1 decides whether this card stays.**
2. **Checkpoint and Minefield share a technical bet.** Both need speech-to-text on this machine, so T1 and T1b can run in the same session with the same setup (about 1–1.5 h). The bars differ:
   - Checkpoint needs a readable transcript, which Whisper does well, so T1b should be easier to pass.
   - Minefield needs a low false-alarm rate on arbitrary words, which is harder.

   So T1 can fail while T1b passes.
3. **Astra's criticism of Checkpoint is factually right.** The card only names the fallback ("switch to the pause-trigger fallback"). Its details are in candidate B of [../step6/pivots/checkpoint-draft.md](../step6/pivots/checkpoint-draft.md), which the raters did not see. Even after that is fixed, the fallback is close to Meld, so it saves the demo but not the innovation. Read Checkpoint's shared second place with this in mind, together with the possible bias above.
4. **VAR is the strongest hedge.** It needs no speech-to-text, it is the only fully unanimous card, and it has the most build slack. Its ceiling is Innovation 3: a safe, good project, but probably not a surprising one.
5. **Hint Jar and Tap are solid but have a lower ceiling.** Hint Jar is the lowest-risk option. Two raters rank Tap 5th, which tells me judges are unlikely to remember it.
6. **I see no reason to pick Studio Audience or Raid Torch.** The three-account rule takes away the core of both. This is not an elimination; that decision is yours.

### Suggested finalists and a decision rule (for you to approve)

My suggested finalists are **Minefield, Checkpoint and VAR**. Together they cover a high-risk speech-to-text path and a hedge that needs no speech-to-text. Day-1 tests: T1 and T1b in one session, plus T2 for VAR.

| T1 (Minefield) | T1b (Checkpoint) | Choice |
| --- | --- | --- |
| Passes | — | Minefield |
| Fails | Passes | Checkpoint or VAR. You decide; I lean towards VAR, because Checkpoint's lead depends partly on C. |
| Fails | Fails | VAR |

Variation: Hint Jar, now 4th, is the lowest-risk option. You could put it in place of Checkpoint, or add it as a fourth finalist.
