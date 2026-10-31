"""WP15 score acceptance: pure state, bounded storage and public messages."""

import json
from dataclasses import replace

import pytest
from fastapi.testclient import TestClient

from minefield.core.config import Config
from minefield.core.deck import Deck
from minefield.core.game import Game
from minefield.core.matcher import Matcher
from minefield.server.app import create_app


@pytest.fixture
def game():
    deck = Deck(
        [{"word": "pineapple", "variants": []}, {"word": "volcano", "variants": []}]
    )
    instance = Game(deck, replace(Config(), ARM_DELAY_S=0))
    instance.start(0)
    return instance


def award(game, owner, now):
    mine_id = game.plant(owner, "pineapple", now)[0]["id"]
    game.arm(now)
    events = Matcher(game).process(
        {
            "utt_id": f"u{mine_id}",
            "seq": 1,
            "final": True,
            "utt_start_wall": now,
            "words": [{"text": "pineapple", "start": 0, "end": 0.1, "prob": 1}],
        },
        now + 0.2,
    )
    assert events[-1]["type"] == "boom"
    return mine_id, game.score_boom(mine_id)


def test_award_once_correct_once_and_no_dud_points(game):
    mine_id, points = award(game, "alice", 1)
    assert points == game.score_boom(mine_id) == 1
    assert game.leaderboard() == [{"owner": "alice", "points": 1}]
    correction = game.false_alarm(2)[0]
    assert correction["scores"] == []
    assert game.false_alarm(2) == []
    game.plant("bob", "volcano", 3)
    reveal, recap = game.end(4)
    assert reveal[0]["round_top"] == reveal[0]["scores"] == []
    assert "Top trappers" not in recap


def test_scores_survive_rounds_and_compaction_but_round_counts_reset(game):
    award(game, "alice", 1)
    game.compact(12)
    assert game.mines == {}
    events, recap = game.end(13)
    assert events[0]["round_top"] == [{"owner": "alice", "booms": 1}]
    assert recap.endswith("Top trappers: @alice 1.")
    assert game.snapshot(14)["scores"] == [{"owner": "alice", "points": 1}]
    assert game.start(15)[0]["scores"] == [{"owner": "alice", "points": 1}]
    assert game.end(16)[0][0]["round_top"] == []
    assert Game(game.deck).leaderboard() == []


def test_rank_by_points_then_resulting_total_sequence_after_correction(game):
    award(game, "alice", 1)
    award(game, "bob", 2)
    award(game, "alice", 3)
    assert game.leaderboard() == [
        {"owner": "alice", "points": 2},
        {"owner": "bob", "points": 1},
    ]
    game.false_alarm(4)
    assert game.leaderboard() == [
        {"owner": "bob", "points": 1},
        {"owner": "alice", "points": 1},
    ]
    top = game.end(5)[0][0]["round_top"]
    assert top == [{"owner": "alice", "booms": 1}, {"owner": "bob", "booms": 1}]


def test_leaderboard_limit_and_correction_timeout(game):
    for i, owner in enumerate(["a", "b", "c", "d"]):
        award(game, owner, i * 12 + 1)
    assert len(game.leaderboard()) == 3
    assert [entry["owner"] for entry in game.leaderboard()] == ["a", "b", "c"]
    assert game.false_alarm(60) == []


def test_cap_prunes_lowest_then_oldest_positive_award(game):
    game.config = replace(game.config, SCORE_MAX_PLAYERS=2)
    award(game, "a", 1)
    award(game, "a", 2)
    award(game, "b", 3)
    award(game, "c", 4)
    assert set(game.scores) == {"a", "c"}
    # A separate game makes the tie policy explicit at a fixed configured cap.
    other = Game(game.deck, replace(game.config, SCORE_MAX_PLAYERS=2))
    other.start(0)
    award(other, "a", 1)
    award(other, "b", 2)
    award(other, "c", 3)
    assert set(other.scores) == {"b", "c"}
    assert other.end(4)[0][0]["round_top"] == [
        {"owner": "b", "booms": 1},
        {"owner": "c", "booms": 1},
    ]


def test_old_credit_does_not_retract_returning_owners_new_credit(game):
    game.config = replace(game.config, SCORE_MAX_PLAYERS=1)
    award(game, "a", 1)
    award(game, "b", 2)
    award(game, "a", 3)
    game.false_alarm(4)  # Retract A's new point.
    game.false_alarm(4)  # B was evicted.
    game.false_alarm(4)  # A's old credit belongs to the discarded entry.
    assert game.leaderboard() == []
    assert game.scores["a"].points == 0


def test_cap_correction_can_leave_no_ranked_owner_with_nonzero_round_stats(game):
    game.config = replace(game.config, SCORE_MAX_PLAYERS=1)
    award(game, "a", 1)
    award(game, "b", 2)
    game.false_alarm(3)
    reveal = game.end(4)[0][0]
    assert reveal["stats"]["booms"] == 1
    assert reveal["round_top"] == []


def test_recap_drops_score_suffix_before_entries_and_stays_bounded(game):
    award(game, "alice", 1)
    game.plant("bob", "volcano", 2)
    base = 'Round over: 1 booms. 💥 @alice (pineapple). Survived: @bob\'s "volcano".'
    game.config = replace(game.config, CHAT_MAX_CHARS=len(base))
    assert game.end(3)[1] == base
    game.start(4)
    award(game, "alice", 5)
    game.config = replace(game.config, CHAT_MAX_CHARS=35)
    recap = game.end(6)[1]
    assert len(recap) <= 35 and recap.endswith("…")
    assert "Top trappers" not in recap


def test_score_projections_never_contain_words(game):
    award(game, "alice", 1)
    game.plant("bob", "volcano", 2)
    snapshot = game.snapshot(3)
    assert "pineapple" not in json.dumps(snapshot)
    assert "volcano" not in json.dumps(snapshot)
    reveal = game.end(4)[0][0]
    assert all(set(row) == {"owner", "points"} for row in reveal["scores"])
    assert all(set(row) == {"owner", "booms"} for row in reveal["round_top"])


def test_server_score_messages_batch_booms_and_idle_snapshots():
    now = [100.0]
    app = create_app(
        config=replace(Config(), ARM_DELAY_S=0), clock=lambda: now[0], debug=True
    )
    with TestClient(app) as client:
        client.post("/dock/round/start")
        for owner, word in [("a", "pineapple"), ("b", "volcano")]:
            client.post("/dock/debug/plant", json={"owner": owner, "word": word})
        with (
            client.websocket_connect("/ws/overlay") as overlay,
            client.websocket_connect("/ws/dock") as dock,
        ):
            assert (
                overlay.receive_json()["scores"] == dock.receive_json()["scores"] == []
            )
            dock.receive_json()  # Initial health status.
            client.post("/dock/typed", json={"text": "pineapple volcano"})
            for ws in [overlay, dock]:
                booms = []
                while len(booms) < 2:
                    event = ws.receive_json()
                    if event["type"] == "boom":
                        booms.append(event)
                assert booms[0]["scores"] == [{"owner": "a", "points": 1}]
                assert booms[1]["scores"] == [
                    {"owner": "a", "points": 1},
                    {"owner": "b", "points": 1},
                ]
            client.post("/dock/false-alarm")
            for ws in [overlay, dock]:
                assert ws.receive_json()["scores"] == [{"owner": "a", "points": 1}]
            client.post("/dock/round/end")
            for ws in [overlay, dock]:
                assert ws.receive_json()["round_top"] == [{"owner": "a", "booms": 1}]
        with client.websocket_connect("/ws/overlay") as reloaded:
            idle = reloaded.receive_json()
            assert not idle["round"]["running"]
            assert idle["scores"] == [{"owner": "a", "points": 1}]
