"""Round state and public projections; no I/O or implicit clocks."""

from dataclasses import dataclass, field

from .config import Config


@dataclass
class Score:
    points: int = 0
    reached: int = 0
    last_award: int = 0
    round_booms: int = 0


@dataclass
class Mine:
    id: str
    owner: str
    word: str = field(repr=False)
    planted_at: float = 0
    arms_at: float = 0
    status: str = "arming"
    boom_at: float | None = None
    boom_order: int = 0
    credit: Score | None = field(default=None, repr=False)

    @property
    def live(self):
        return self.status in {"arming", "armed", "sparking"}


class Game:
    def __init__(self, deck, config=None):
        self.deck = deck
        self.config = config or Config()
        self.running = False
        self.started_at = 0
        self.round_id = 0
        self.mines = {}
        self.next_id = 1
        self.scores = {}
        self.score_sequence = 0
        self.boom_sequence = 0
        self.archived_booms = 0
        self.archived_entries = []
        self.archived_truncated = False

    def start(self, now):
        if self.running:
            raise ValueError("Round already running")
        self.running = True
        for score in self.scores.values():
            score.round_booms = 0
        self.round_id += 1
        self.started_at = now
        self.boom_sequence = 0
        self.archived_booms = 0
        self.archived_entries.clear()
        self.archived_truncated = False
        self.mines.clear()
        return [self.snapshot(now)]

    def leaderboard(self):
        ranked = sorted(
            ((owner, score) for owner, score in self.scores.items() if score.points),
            key=lambda item: (-item[1].points, item[1].reached),
        )
        return [
            {"owner": owner, "points": score.points}
            for owner, score in ranked[: self.config.SCOREBOARD_SIZE]
        ]

    def score_boom(self, mine_id):
        """Credit an emitted boom once; the server calls this before broadcast."""
        mine = self.mines[mine_id]
        if mine.credit is not None:
            return mine.credit.points
        if mine.status != "exploded":
            raise ValueError("Mine has not exploded")
        if mine.owner not in self.scores:
            if len(self.scores) >= self.config.SCORE_MAX_PLAYERS:
                oldest = min(
                    self.scores,
                    key=lambda owner: (
                        self.scores[owner].points,
                        self.scores[owner].last_award,
                    ),
                )
                del self.scores[oldest]
            self.scores[mine.owner] = Score()
        score = self.scores[mine.owner]
        self.score_sequence += 1
        score.points += 1
        score.round_booms += 1
        score.reached = score.last_award = self.score_sequence
        mine.credit = score
        return score.points

    def round_top(self):
        highest = max((score.round_booms for score in self.scores.values()), default=0)
        return [
            {"owner": owner, "booms": highest}
            for owner, score in sorted(self.scores.items())
            if highest and score.round_booms == highest
        ]

    def plant(self, owner, word, now):
        if not self.running:
            raise ValueError("No active round")
        self.compact(now)
        live = [mine for mine in self.mines.values() if mine.live]
        if any(mine.owner == owner for mine in live):
            raise ValueError("Owner already has a live mine")
        if any(mine.word == word for mine in live):
            raise ValueError("Word taken, pick another")
        if len(live) >= self.config.MAX_MINES:
            raise ValueError("Minefield full")
        if word not in self.deck.words:
            raise ValueError("Unknown deck selection")
        mine = Mine(str(self.next_id), owner, word, now, now + self.config.ARM_DELAY_S)
        self.next_id += 1
        self.mines[mine.id] = mine
        return [
            {
                "type": "mine_planted",
                "id": mine.id,
                "owner": owner,
                "arms_in_s": self.config.ARM_DELAY_S,
            }
        ]

    def arm(self, now):
        self.compact(now)
        events = []
        for mine in self.mines.values():
            if mine.status == "arming" and now >= mine.arms_at:
                mine.status = "armed"
                events.append({"type": "mine_armed", "id": mine.id})
        return events

    def snapshot(self, now, plant_url=None):
        self.compact(now)
        return {
            "type": "snapshot",
            "round": {"running": self.running},
            "plant_url": plant_url,
            "scores": self.leaderboard(),
            "mines": [
                {
                    "id": mine.id,
                    "owner": mine.owner,
                    "status": mine.status,
                    "arms_in_s": max(0, mine.arms_at - now),
                }
                for mine in self.mines.values()
            ],
        }

    def false_alarm(self, now):
        if not self.running:
            return []
        self.compact(now)
        eligible = [
            mine
            for mine in self.mines.values()
            if mine.status == "exploded"
            and 0 <= now - mine.boom_at <= self.config.FALSE_ALARM_WINDOW_S
        ]
        if not eligible:
            return []
        mine = max(eligible, key=lambda item: (item.boom_at, item.boom_order))
        mine.status = "false_alarm"
        score = self.scores.get(mine.owner)
        if score is not None and score is mine.credit:
            self.score_sequence += 1
            score.points -= 1
            score.round_booms -= 1
            score.reached = self.score_sequence
        return [
            {
                "type": "false_alarm",
                "id": mine.id,
                "owner": mine.owner,
                "scores": self.leaderboard(),
            }
        ]

    def end(self, now):
        if not self.running:
            return [], ""
        self.compact(now)
        booms = sorted(
            (mine for mine in self.mines.values() if mine.status == "exploded"),
            key=lambda mine: mine.boom_order,
        )
        duds = [mine for mine in self.mines.values() if mine.live]
        for mine in duds:
            mine.status = "dud"
        events = [
            {
                "type": "reveal",
                "duds": [{"owner": mine.owner, "word": mine.word} for mine in duds],
                "stats": {"booms": self.archived_booms + len(booms)},
                "round_top": self.round_top(),
                "scores": self.leaderboard(),
            }
        ]
        recap = self._recap(booms, duds)
        self.running = False
        for score in self.scores.values():
            score.round_booms = 0
        self.mines.clear()
        self.archived_booms = 0
        self.archived_entries.clear()
        self.archived_truncated = False
        return events, recap

    def compact(self, now):
        expired = sorted(
            (
                mine
                for mine in self.mines.values()
                if not mine.live
                and mine.boom_at is not None
                and now - mine.boom_at > self.config.FALSE_ALARM_WINDOW_S
            ),
            key=lambda mine: mine.boom_order,
        )
        for mine in expired:
            if mine.status == "exploded":
                self.archived_booms += 1
                entry = f"@{mine.owner} ({mine.word})"
                used = sum(len(item) + 2 for item in self.archived_entries)
                if (
                    not self.archived_truncated
                    and used + len(entry) + 2 <= self.config.CHAT_MAX_CHARS
                ):
                    self.archived_entries.append(entry)
                else:
                    self.archived_truncated = True
            del self.mines[mine.id]

    def _recap(self, booms, duds):
        count = self.archived_booms + len(booms)
        prefix = f"Round over: {count} booms." if count else "Round over: no booms."
        entries = [("boom", entry) for entry in self.archived_entries]
        if not self.archived_truncated:
            entries += [("boom", f"@{mine.owner} ({mine.word})") for mine in booms]
            entries += [("dud", f'@{mine.owner}\'s "{mine.word}"') for mine in duds]

        def render(items):
            hits = [text for kind, text in items if kind == "boom"]
            survivors = [text for kind, text in items if kind == "dud"]
            return (
                prefix
                + (" 💥 " + ", ".join(hits) + "." if hits else "")
                + (" Survived: " + ", ".join(survivors) + "." if survivors else "")
            )

        message = render(entries)
        leaders = self.leaderboard()
        if leaders and not self.archived_truncated:
            suffix = (
                " Top trappers: "
                + ", ".join(f"@{row['owner']} {row['points']}" for row in leaders)
                + "."
            )
            if len(message + suffix) <= self.config.CHAT_MAX_CHARS:
                return message + suffix
        truncated = self.archived_truncated
        while entries and len(message) + int(truncated) > self.config.CHAT_MAX_CHARS:
            entries.pop()
            truncated = True
            message = render(entries)
        if truncated:
            message = message[: self.config.CHAT_MAX_CHARS - 1] + "…"
        return message[: self.config.CHAT_MAX_CHARS]
