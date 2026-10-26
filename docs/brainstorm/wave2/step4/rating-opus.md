# Rating: opus

## 1. Ratings table

| ID | Q1 | Q2 | Q3 | Q4 | Verdict | Reason for each FATAL (one short line each; empty if none) |
| --- | --- | --- | --- | --- | --- | --- |
| C01 | OK | OK | OK | OK | Keep | |
| C02 | FATAL | OK | OK | FATAL | Eliminate | Q1: Guest Star already has its own backstage/queue for picking guests; an overlay listing them adds no new experience. Q4: little more than a wrapper around the Guest Star feature. |
| C03 | FATAL | OK | OK | OK | Keep (flag) | Q1: chat-over-game overlays for single-monitor streamers are already sold; showing one filtered line is a settings tweak, and the experience stays "read chat over the game". |
| C04 | FATAL | OK | OK | FATAL | Eliminate | Q1: raid trains, Discord raid groups and Twitch's raid suggestions already do "who in my circle is live, raid them". Q4: a live-status list plus Start Raid and Shoutout API calls. |
| C05 | FATAL | OK | FATAL | FATAL | Eliminate | Q1: a sticky raid alert plus auto-shoutout, both already common. Q3: a tiny streamer rarely gets raided, and even more rarely while on BRB. Q4: one EventSub listener and one shoutout call. |
| C06 | FATAL | OK | OK | OK | Keep (flag) | Q1: chat-spike auto-clipping is on the expected-crowd list; lowering the threshold to "two chatters" doesn't change the experience. |
| C07 | OK | OK | OK | OK | Keep | |
| C08 | OK | OK | OK | OK | Keep | |
| C09 | OK | OK | OK | OK | Keep | |
| C10 | OK | FATAL | OK | FATAL | Eliminate | Q2: the value plays out over minutes (bookmark now, encore later), so a 10-second clip shows only a list and needs narration. Q4: a command logger plus a list view, which is thin. |
| C11 | FATAL | OK | OK | OK | Keep (flag) | Q1: OBS caption plugins and Twitch's caption support already do live captions; "local only" doesn't change what viewers see. |
| C12 | OK | OK | OK | OK | Keep | |
| C13 | OK | OK | OK | OK | Keep | |
| C14 | FATAL | OK | OK | OK | Keep (flag) | Q1: multi-platform chat aggregators (Restream and others) already put YouTube chat in front of the streamer; a "hellos only" filter is a minor twist. |
| C15 | FATAL | OK | FATAL | FATAL | Eliminate | Q1: Shared Chat already marks each message with its source channel. Q3: needs a Shared Chat collab, which a small streamer does rarely, and pen-pal pairing is a one-off gimmick. Q4: an overlay over an existing feature, which is thin. |
| C16 | OK | OK | FATAL | OK | Keep (flag) | Q3: a streamer would try the desk-foley performance segment once; it isn't a repeatable stream tool. |
| C17 | OK | OK | OK | OK | Keep | |
| C18 | FATAL | OK | OK | OK | Keep (flag) | Q1: once the envelopes are stripped away, it's a chat guessing game or prediction (expected crowd); sealing the guesses hardly changes the experience. |
| C19 | FATAL | OK | OK | OK | Keep (flag) | Q1: chat commands that trigger camera or filter effects are standard viewer-triggered effects (Crowd Control, Twitch Plays). |
| C20 | OK | OK | FATAL | OK | Keep (flag) | Q3: it only works when the raid target also runs the tool, so a real small streamer would almost never see it fire. |
| C21 | FATAL | OK | OK | FATAL | Eliminate | Q1: media-share overlays already do this. Q4: a thin pass-through from chat GIFs to a frame. |
| C22 | FATAL | OK | OK | FATAL | Eliminate | Q1: Twitch's emote-only toggle exists; the timer and restore are minor. Q4: a wrapper around one chat setting. |
| C23 | OK | OK | OK | OK | Keep | |
| C24 | OK | OK | OK | OK | Keep | |
| C25 | OK | OK | OK | OK | Keep | |
| C26 | OK | OK | OK | OK | Keep | |
| C27 | OK | OK | OK | OK | Keep | |
| C28 | OK | OK | OK | OK | Keep | |
| C29 | FATAL | OK | OK | OK | Keep (flag) | Q1: translation bots and extensions already do exactly this. |
| C30 | OK | OK | OK | OK | Keep | |
| C31 | FATAL | OK | OK | OK | Keep (flag) | Q1: question queues are on the expected-crowd list, and StreamerQnA and Meld already do this. |
| C32 | FATAL | FATAL | OK | OK | Eliminate | Q1: Chatterino filters, highlights and split views already do this. Q2: by design nothing appears on stream; it's a private view. |
| C33 | FATAL | OK | FATAL | OK | Eliminate | Q1: chat votes steering a shared pointer is Twitch Plays or a poll with an Ouija skin. Q3: a novelty stunt, played once. |
| C34 | OK | FATAL | FATAL | OK | Eliminate | Q2: "Stage C complete" on a paper creature can't be understood without narration. Q3: only maker streamers with checkable stages; rare. |
| C35 | OK | FATAL | OK | FATAL | Eliminate | Q2: it happens on a private mod phone, and the undo isn't visible on stream. Q4: a UI over the timeout and untimeout API calls, which is thin. |
| C36 | OK | OK | OK | FATAL | Keep (flag) | Q4: one Get Chat Settings read plus a confirm before Start Raid, which is thin. |
| C37 | FATAL | OK | OK | OK | Keep (flag) | Q1: Streamer.bot and Mix It Up remote triggers and Stream Deck mobile apps already let mods fire overlays privately. |

**Totals:** Keep 14, Keep (flag) 12, Eliminate 11.

## 2. Top 5 (optional)

1. **C09 Word mines:** a new game loop with a perfect wordless payoff (BOOM plus the planter's name), it works with three viewers, and STT plus a bot plus an overlay makes a solid Codex story.
2. **C07 VAR check:** instantly readable, funny with desk content, and the replay, slow motion, jury and clip stack shows real technical depth.
3. **C13 Lore footnotes:** an original take on newcomer onboarding that every channel with inside jokes can use, and the footnote pop is readable at a glance.
4. **C24 Production problems reach the streamer:** a real recurring pain (muted mic), a physical red lamp makes a vivid demo, and it turns chat into a useful signal.
5. **C28 Tiered hints:** solves the backseating fight in blind playthroughs, and the jar and nudge reveal is visual and easy to grasp.

## 3. Notes (optional)

- **Delete-to-seal (C09, C18, C28):** a message that the bot deletes "at once" is still briefly visible to everyone in chat, and mods can see it in logs. "Sealed" is not truly secret unless input goes through a web form or whisper, so the description overstates the secrecy.
- **C15:** Twitch Shared Chat already shows each message's source-channel avatar or badge, so the color-coding adds less than described.
- **C21:** I'm not confident that native GIFs in Twitch chat exist as described; verify before relying on them.
- **C26 / C31 pin variants:** I'm not sure Twitch exposes a public API for pinning chat messages; treat the "Pinned Chat API" as unverified.
- **C06:** the API-created clip length is constrained by Twitch (clips are short by default), so "the last ~85 s" may not be achievable as stated.
- **C02:** the Guest Star API has been beta or limited, and may not be available to new channels at all.
- **Overlaps:** C17, C31 and C32 all solve "surface the real questions or messages from chat". C03, C12 and C24 all solve "the streamer can't see chat while busy", and C12's smart-bulb variant overlaps with C24's lamp. C18 and C28 share the sealed-envelope mechanic. C26 and C27 both orient newcomers.
