"""WP1 acceptance: pure game logic, matcher and public-output secrecy."""

import json
import random
from dataclasses import replace

import pytest

from minefield.core.config import Config
from minefield.core.deck import Deck
from minefield.core.game import Game
from minefield.core.matcher import Matcher
from minefield.core.normalize import normalize


@pytest.fixture
def deck():
    return Deck(
        [
            {"word": "pineapple", "variants": ["pineapples", "pine apple"]},
            {"word": "volcano", "variants": ["volcanoes"]},
            {"word": "banana", "variants": ["bananas"]},
            {"word": "alligator", "variants": []},
            {"word": "astronaut", "variants": []},
            {"word": "umbrella", "variants": []},
        ]
    )


def setup_game(deck, **overrides):
    game = Game(deck, replace(Config(), ARM_DELAY_S=0, **overrides))
    game.start(100)
    game.plant("alice", "pineapple", 100)
    game.arm(100)
    return game, Matcher(game)


def hypothesis(
    seq=1,
    texts=("pineapple",),
    *,
    probs=None,
    start=1.0,
    final=False,
    utt_id="u1",
    utt_start_wall=100,
):
    return {
        "utt_id": utt_id,
        "seq": seq,
        "final": final,
        "utt_start_wall": utt_start_wall,
        "emitted_wall": 103,
        "lag_ms": 10,
        "words": [
            {
                "text": text,
                "start": start + i * 0.1,
                "end": start + i * 0.1 + 0.1,
                "prob": probs[i] if probs else 0.95,
            }
            for i, text in enumerate(texts)
        ],
    }


def types(events):
    return [event["type"] for event in events]


@pytest.mark.parametrize("count", [2, 3])
def test_consecutive_confirmation(deck, count):
    game, matcher = setup_game(deck, CONFIRM_N=count)
    assert types(matcher.process(hypothesis(), 103)) == ["spark"]
    for seq in range(2, count):
        assert matcher.process(hypothesis(seq), 103) == []
    events = matcher.process(hypothesis(count), 103)
    assert types(events) == ["boom"]
    assert events[0]["word"] == "pineapple"
    assert events[0]["latency_ms"] == pytest.approx(1900)
    assert matcher.process(hypothesis(count + 1), 104) == []
    assert game.mines["1"].status == "exploded"


def test_fizzle_on_absence_and_low_confidence(deck):
    _, matcher = setup_game(deck)
    assert matcher.process(hypothesis(probs=[0.59]), 103) == []
    matcher.process(hypothesis(2), 103)
    assert types(matcher.process(hypothesis(3, ("hello",)), 103)) == ["fizzle"]


@pytest.mark.parametrize("cleanup", ["final", "abort", "round_end"])
def test_pending_cleanup(deck, cleanup):
    game, matcher = setup_game(deck, CONFIRM_N=3)
    matcher.process(hypothesis(), 103)
    if cleanup == "final":
        events = matcher.process(hypothesis(2, final=True), 103)
    elif cleanup == "abort":
        events = matcher.abort("u1")
    else:
        events = matcher.abort()
        game.end(104)
    assert types(events) == ["fizzle"]
    assert matcher.process(hypothesis(3), 105) == []


@pytest.mark.parametrize(
    "prob,expected", [(0.59, []), (0.65, ["spark", "fizzle"]), (0.7, ["spark", "boom"])]
)
def test_final_solo(deck, prob, expected):
    _, matcher = setup_game(deck)
    assert types(matcher.process(hypothesis(final=True, probs=[prob]), 103)) == expected


def test_final_solo_requires_normal_floor_too(deck):
    _, matcher = setup_game(deck, MIN_WORD_PROB=0.9)
    assert matcher.process(hypothesis(final=True, probs=[0.8]), 103) == []


def test_timestamp_shift_identity_and_restart(deck):
    _, matcher = setup_game(deck)
    matcher.process(hypothesis(), 103)
    assert types(matcher.process(hypothesis(2, start=1.4), 103)) == ["boom"]
    _, matcher = setup_game(deck)
    matcher.process(hypothesis(), 103)
    assert types(matcher.process(hypothesis(2, start=1.6), 103)) == ["fizzle", "spark"]
    assert types(matcher.process(hypothesis(3, start=1.6), 103)) == ["boom"]


def test_occurrence_number_counts_low_confidence_occurrences(deck):
    _, matcher = setup_game(deck)
    matcher.process(
        hypothesis(texts=("pineapple", "pineapple"), probs=[0.1, 0.95]), 103
    )
    events = matcher.process(hypothesis(2, texts=("pineapple",), probs=[0.95]), 103)
    assert types(events) == ["fizzle", "spark"]


def test_multiword_confidence_and_normalization(deck):
    assert normalize("（PINEAPPLES!）") == "pineapples"
    _, matcher = setup_game(deck)
    assert (
        matcher.process(hypothesis(texts=("Pine", "apple!"), probs=[0.95, 0.5]), 103)
        == []
    )
    assert types(matcher.process(hypothesis(2, texts=("Pine", "apple!")), 103)) == [
        "spark"
    ]
    event = matcher.process(hypothesis(3, texts=("pine", "apple")), 103)[0]
    assert event["receipt"] == [{"text": "pine apple", "hit": True}]


@pytest.mark.parametrize(
    "forms",
    [
        [("pineapple", ["pine apple"]), ("apple", [])],
        [("pineapple", ["pine apple"]), ("applecake", ["apple cake"])],
        [("pineapple", ["fruit"]), ("banana", ["FRUIT!"])],
    ],
)
def test_ambiguous_deck_rejected(forms):
    with pytest.raises(ValueError, match="ambiguous"):
        Deck([{"word": word, "variants": variants} for word, variants in forms])


def test_speech_time_eligibility(deck):
    game = Game(deck, Config())
    game.start(100)
    game.plant("alice", "pineapple", 100)
    game.arm(140)
    matcher = Matcher(game)
    assert matcher.process(hypothesis(start=29, final=True), 140) == []
    assert types(
        matcher.process(
            hypothesis(start=30, final=True, utt_id="u2", utt_start_wall=101), 140
        )
    ) == ["spark", "boom"]
    game.end(141)
    assert matcher.process(hypothesis(utt_id="u3", final=True), 142) == []
    game.start(200)
    game.plant("alice", "pineapple", 200)
    game.arm(240)
    assert matcher.process(hypothesis(utt_id="old", final=True), 240) == []


def test_live_limits_and_replanting(deck):
    game, matcher = setup_game(deck, MAX_MINES=2)
    for status in ("arming", "armed", "sparking"):
        game.mines["1"].status = status
        with pytest.raises(ValueError, match="already"):
            game.plant("alice", "volcano", 101)
    game.mines["1"].status = "armed"
    with pytest.raises(ValueError, match="taken"):
        game.plant("bob", "pineapple", 101)
    game.plant("bob", "volcano", 101)
    with pytest.raises(ValueError, match="full"):
        game.plant("charlie", "banana", 101)
    matcher.process(hypothesis(final=True), 103)
    game.plant("alice", "banana", 104)


def test_false_alarm_latest_eligible_and_stats(deck):
    game, matcher = setup_game(deck)
    matcher.process(hypothesis(final=True), 103)
    game.plant("bob", "volcano", 103)
    game.arm(103)
    matcher.process(
        hypothesis(texts=("volcano",), final=True, utt_id="u2", utt_start_wall=103), 105
    )
    assert game.false_alarm(106)[0]["owner"] == "bob"
    assert game.false_alarm(107)[0]["owner"] == "alice"
    assert game.false_alarm(108) == []
    events, recap = game.end(109)
    assert events[-1]["stats"] == {"booms": 0}
    assert recap == "Round over: no booms."


def test_false_alarm_deadline_and_idle(deck):
    game, matcher = setup_game(deck)
    matcher.process(hypothesis(final=True), 103)
    assert game.false_alarm(113.01) == []
    game.end(114)
    assert game.false_alarm(115) == []


def test_receipt_window_highlight_masking_and_secrecy(deck):
    game, matcher = setup_game(deck)
    game.plant("bob", "volcano", 100)
    game.arm(100)
    matcher.process(hypothesis(texts=("volcano",)), 102)
    texts = (
        "before",
        "this",
        "is",
        "a",
        "banana",
        "volcano",
        "and",
        "a",
        "pine",
        "apple",
        "after",
    )
    probs = [0.95] * len(texts)
    probs[5] = 0.1  # The fizzled live volcano remains private.
    events = matcher.process(hypothesis(2, texts=texts, probs=probs, start=1.1), 103)
    boom = matcher.process(hypothesis(3, texts=texts, probs=probs, start=1.1), 103)[0]
    assert "fizzle" in types(events)
    assert sum(item["hit"] for item in boom["receipt"]) == 1
    assert boom["receipt"][-1] == {"text": "pine apple", "hit": True}
    receipt = json.dumps(boom["receipt"])
    assert "volcano" not in receipt and "banana" not in receipt
    assert "before" not in receipt and "after" not in receipt
    assert "volcano" not in json.dumps(game.snapshot(104))
    assert "pineapple" not in json.dumps(game.snapshot(104))


def test_round_end_duds_clear_and_recap(deck):
    game, matcher = setup_game(deck)
    game.plant("bob", "volcano", 100)
    matcher.process(hypothesis(final=True), 103)
    events, recap = game.end(104)
    assert events[-1] == {
        "type": "reveal",
        "duds": [{"owner": "bob", "word": "volcano"}],
        "stats": {"booms": 1},
    }
    assert (
        recap
        == 'Round over: 1 booms. 💥 @alice (pineapple). Survived: @bob\'s "volcano".'
    )
    assert game.snapshot(105)["mines"] == []
    assert not game.snapshot(105)["round"]["running"]


def test_recap_truncates_entries(deck):
    game, _ = setup_game(deck, CHAT_MAX_CHARS=65)
    game.plant("viewer_" + "x" * 100, "volcano", 100)
    _, recap = game.end(103)
    assert len(recap) <= 65 and recap.endswith("…")
    assert "viewer_" not in recap


def test_whole_deck_hand_even_taken(deck):
    game, _ = setup_game(deck)
    assert set(deck.hand(random.Random(1), 6)) == set(deck.words)
    assert "pineapple" in deck.hand(random.Random(1), 6)
    with pytest.raises(ValueError, match="taken"):
        game.plant("bob", "pineapple", 101)


def test_snapshot_remaining_arming_and_no_words(deck):
    game = Game(deck, Config())
    game.start(100)
    event = game.plant("alice", "pineapple", 100)
    assert event == [
        {"type": "mine_planted", "id": "1", "owner": "alice", "arms_in_s": 30}
    ]
    assert game.snapshot(107)["mines"] == [
        {"id": "1", "owner": "alice", "status": "arming", "arms_in_s": 23}
    ]
    assert game.snapshot(140)["mines"][0]["arms_in_s"] == 0


@pytest.mark.parametrize(
    "kwargs",
    [
        {"CONFIRM_N": 0},
        {"MIN_WORD_PROB": 2},
        {"GAME_PORT": 0},
        {"ARM_DELAY_S": -1},
        {"AGREE_TOL_S": float("nan")},
    ],
)
def test_config_rejects_invalid_values(kwargs):
    with pytest.raises(ValueError):
        replace(Config(), **kwargs)


def test_utterance_started_before_round_can_have_eligible_speech(deck):
    game = Game(deck, replace(Config(), ARM_DELAY_S=0))
    game.start(100)
    game.plant("alice", "pineapple", 100)
    matcher = Matcher(game)
    events = matcher.process(hypothesis(final=True, utt_start_wall=99, start=2), 103)
    assert "boom" in types(events)


def test_false_alarm_uses_latest_emission_when_boom_times_tie(deck):
    game, matcher = setup_game(deck)
    game.plant("bob", "volcano", 100)
    events = matcher.process(
        hypothesis(texts=("pineapple", "volcano"), final=True), 103
    )
    assert [event["owner"] for event in events if event["type"] == "boom"] == [
        "alice",
        "bob",
    ]
    assert game.false_alarm(104)[0]["owner"] == "bob"


def test_expired_history_is_compact_but_preserves_total_and_recap_prefix(deck):
    game = Game(deck, replace(Config(), ARM_DELAY_S=0))
    game.start(100)
    matcher = Matcher(game)
    for index in range(100):
        now = 100 + index * 11
        game.plant(f"viewer_{index}", "pineapple", now)
        matcher.process(
            hypothesis(final=True, utt_id=f"u{index}", utt_start_wall=now), now + 2
        )
        game.snapshot(now + 13)
        assert len(game.mines) == 0
        assert (
            sum(len(entry) for entry in game.archived_entries)
            <= game.config.CHAT_MAX_CHARS
        )
    events, recap = game.end(1300)
    assert events[-1]["stats"] == {"booms": 100}
    assert "@viewer_0 (pineapple)" in recap
    assert "viewer_99" not in recap
    assert len(recap) <= 500 and recap.endswith("…")
    assert game.archived_entries == []
    assert game.archived_booms == 0


def test_compaction_preserves_correction_window_and_excludes_false_alarms(deck):
    game, matcher = setup_game(deck)
    matcher.process(hypothesis(final=True), 103)
    assert game.snapshot(113)["mines"][0]["status"] == "exploded"
    assert game.false_alarm(113)
    assert game.snapshot(113)["mines"][0]["status"] == "false_alarm"
    assert game.snapshot(113.01)["mines"] == []
    assert game.false_alarm(114) == []
    events, recap = game.end(115)
    assert events[-1]["stats"] == {"booms": 0}
    assert recap == "Round over: no booms."


def test_compacted_and_recent_recap_entries_follow_boom_emission_order(deck):
    game, matcher = setup_game(deck)
    game.plant("bob", "volcano", 100)
    matcher.process(hypothesis(final=True, texts=("volcano",)), 103)
    matcher.process(hypothesis(final=True, utt_id="u2", utt_start_wall=101), 104)
    game.snapshot(113.5)  # Only Bob's earlier boom has expired.
    events, recap = game.end(114)
    assert events[-1]["stats"] == {"booms": 2}
    assert recap.index("@bob") < recap.index("@alice")


def test_compaction_does_not_skip_an_oversized_first_recap_entry(deck):
    game, matcher = setup_game(deck, CHAT_MAX_CHARS=70)
    game.mines["1"].owner = "x" * 100
    matcher.process(hypothesis(final=True), 103)
    game.snapshot(114)
    game.plant("bob", "volcano", 114)
    matcher.process(
        hypothesis(final=True, texts=("volcano",), utt_id="u2", utt_start_wall=114), 116
    )
    events, recap = game.end(117)
    assert events[-1]["stats"] == {"booms": 2}
    assert "@bob" not in recap and recap.endswith("…")
