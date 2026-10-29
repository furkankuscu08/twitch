"""One ordered hypothesis stream, with bounded candidate and retirement state."""

from dataclasses import dataclass


@dataclass
class Candidate:
    start: float
    count: int = 1


class Matcher:
    def __init__(self, game):
        self.game = game
        self.utt_id = None
        self.utt_start = float("-inf")
        self.closed_through = float("-inf")
        self.last_aborted_utt_id = None
        self.seq = -1
        self.candidates = {}

    def abort(self, utt_id=None):
        if utt_id is not None:
            self.last_aborted_utt_id = utt_id
        if utt_id is not None and utt_id != self.utt_id:
            return []
        events = self._clear_candidates()
        if self.utt_id is not None:
            self.closed_through = max(self.closed_through, self.utt_start)
        self.utt_id = None
        self.seq = -1
        return events

    def _clear_candidates(self):
        events = []
        for mine_id, _ in self.candidates:
            mine = self.game.mines.get(mine_id)
            if mine is not None and mine.status == "sparking":
                mine.status = "armed"
                events.append({"type": "fizzle", "id": mine.id})
        self.candidates.clear()
        return events

    def process(self, hypothesis, now, source="stt"):
        game = self.game
        if not game.running:
            return []
        start = hypothesis["utt_start_wall"]
        utt_id = hypothesis["utt_id"]
        if utt_id == self.last_aborted_utt_id or start <= self.closed_through:
            return []
        events = []
        if self.utt_id != utt_id:
            if start < self.utt_start:
                return []
            events += self.abort()
            if start <= self.closed_through:
                return events
            self.utt_id = utt_id
            self.utt_start = start
        if hypothesis["seq"] <= self.seq:
            return events
        self.seq = hypothesis["seq"]
        events += game.arm(now)
        occurrences = game.deck.occurrences(hypothesis["words"])
        present = {}
        for occurrence in occurrences:
            if occurrence.prob < game.config.MIN_WORD_PROB:
                continue
            for mine in game.mines.values():
                if (
                    mine.word == occurrence.word
                    and mine.status in {"armed", "sparking"}
                    and start + occurrence.start >= max(game.started_at, mine.arms_at)
                ):
                    present[(mine.id, occurrence.number)] = occurrence
        for key, candidate in list(self.candidates.items()):
            occurrence = present.get(key)
            if (
                occurrence is None
                or abs(occurrence.start - candidate.start) > game.config.AGREE_TOL_S
            ):
                self.candidates.pop(key)
                mine = game.mines[key[0]]
                mine.status = "armed"
                events.append({"type": "fizzle", "id": mine.id})
        for key, occurrence in present.items():
            mine = game.mines[key[0]]
            if not mine.live:
                continue
            candidate = self.candidates.get(key)
            fresh = candidate is None
            if fresh:
                candidate = Candidate(occurrence.start)
                self.candidates[key] = candidate
                mine.status = "sparking"
                events.append({"type": "spark", "id": mine.id})
            else:
                candidate.count += 1
            solo = fresh and hypothesis["final"]
            confirmed = candidate.count >= game.config.CONFIRM_N
            if solo:
                confirmed = occurrence.prob >= game.config.FINAL_SOLO_MIN_PROB
            if confirmed:
                mine.status = "exploded"
                mine.boom_at = now
                game.boom_sequence += 1
                mine.boom_order = game.boom_sequence
                events.append(
                    {
                        "type": "boom",
                        "id": mine.id,
                        "owner": mine.owner,
                        "word": mine.word,
                        "planted_ago_s": now - mine.planted_at,
                        "latency_ms": (now - start - occurrence.end) * 1000,
                        "source": source,
                        "at": now,
                        "receipt": game.deck.receipt(
                            hypothesis["words"], occurrence, game.config.RECEIPT_WORDS
                        ),
                    }
                )
                for pending in list(self.candidates):
                    if pending[0] == mine.id:
                        self.candidates.pop(pending)
        if hypothesis["final"]:
            events += self.abort()
        return events
