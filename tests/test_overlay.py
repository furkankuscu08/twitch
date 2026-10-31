"""WP3 acceptance checks; run explicitly with ``pytest -m browser``."""

import functools
import http.server
import threading
from pathlib import Path

import pytest

pytestmark = pytest.mark.browser
ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def static_url():
    class QuietHandler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *_):
            pass

    handler = functools.partial(QuietHandler, directory=str(ROOT / "web"))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{server.server_port}"
    server.shutdown()
    server.server_close()
    thread.join()


@pytest.fixture
def page(static_url):
    from playwright.sync_api import sync_playwright

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport={"width": 1920, "height": 1080})
        page.set_default_timeout(5000)
        page.add_init_script("""
            window.socketCount = 0;
            window.WebSocket = class {
                constructor() { window.socketCount++; window.testSocket = this; }
                close() {}
            };
            window.deliver = (message) => window.testSocket.onmessage({
                data: JSON.stringify(message)
            });
        """)
        page.goto(f"{static_url}/overlay/?latency=1")
        page.wait_for_function("window.overlayReady === true")
        yield page
        browser.close()


def send(page, **message):
    if message.get("type") in {"snapshot", "boom", "false_alarm", "reveal"}:
        message.setdefault("scores", [])
    if message.get("type") == "reveal":
        message.setdefault("round_top", [])
    page.evaluate("message => window.deliver(message)", message)


def snapshot(page, *, running=True, mines=None):
    send(
        page,
        type="snapshot",
        round={"running": running},
        plant_url="https://example.org/plant",
        mines=mines or [],
    )


def boom(page, owner="mira", word="pineapple"):
    send(
        page,
        type="boom",
        id="a",
        owner=owner,
        word=word,
        planted_ago_s=125,
        latency_ms=370,
        source="stt",
        at=1730000000,
        receipt=[
            {"text": "honestly I could go for some", "hit": False},
            {"text": word, "hit": True},
        ],
    )


def test_every_message_and_readable_boom(page):
    snapshot(page)
    assert page.locator("#plant-url").inner_text() == "example.org/plant"
    assert page.locator("#qr canvas").count() == 1
    send(page, type="mine_planted", id="a", owner="mira", arms_in_s=30)
    chip = page.locator('[data-id="a"]')
    assert chip.get_attribute("data-status") == "arming"
    assert chip.locator(".arming-ring").is_visible()
    send(page, type="mine_armed", id="a")
    assert chip.get_attribute("data-status") == "armed"
    send(page, type="spark", id="a")
    assert chip.get_attribute("data-status") == "sparking"
    send(page, type="fizzle", id="a")
    assert chip.get_attribute("data-status") == "armed"
    boom(page)
    assert chip.get_attribute("data-status") == "exploded"
    assert page.locator("#boom-word").inner_text() == "PINEAPPLE"
    assert page.locator("#receipt mark").inner_text() == "pineapple"
    assert "2 min" in page.locator("#boom-age").inner_text()
    assert "370 ms" in page.locator("#latency").inner_text()
    box = page.locator("#boom-banner").bounding_box()
    assert box and 0 <= box["x"] < box["x"] + box["width"] <= 1920
    assert (
        page.locator("#boom-word").evaluate(
            "element => parseFloat(getComputedStyle(element).fontSize)"
        )
        >= 80
    )
    send(page, type="false_alarm", id="a", owner="mira")
    assert page.locator("#false-alarm").is_visible()
    assert chip.get_attribute("data-status") == "false_alarm"
    send(
        page,
        type="reveal",
        duds=[{"owner": "alex", "word": "volcano"}],
        stats={"booms": 0},
    )
    assert "volcano" in page.locator("#reveal").inner_text()
    assert "0 booms" in page.locator("#reveal").inner_text()
    assert page.evaluate("getComputedStyle(document.body).backgroundColor") == (
        "rgba(0, 0, 0, 0)"
    )


def test_snapshot_is_silent_and_never_replays_banners(page):
    page.evaluate(
        "() => { window.AudioContext = class { "
        "constructor() { throw Error('audio'); } }; }"
    )
    snapshot(
        page,
        mines=[
            {"id": "a", "owner": "mira", "status": "exploded", "arms_in_s": 0},
            {"id": "b", "owner": "alex", "status": "arming", "arms_in_s": 12},
        ],
    )
    assert page.locator(".mine-chip").count() == 2
    assert not page.locator("#boom-banner").is_visible()
    assert not page.locator("#reveal").is_visible()
    assert "12" in page.locator('[data-id="b"]').inner_text()
    # Blocked audio must not interrupt any game presentation.
    boom(page)
    assert page.locator("#boom-banner").is_visible()


def test_reveal_survives_idle_snapshot_and_new_round_clears_it(page):
    snapshot(page)
    send(
        page,
        type="reveal",
        duds=[{"owner": "alex", "word": "volcano"}],
        stats={"booms": 1},
    )
    snapshot(page, running=False)
    assert page.locator("#reveal").is_visible()
    snapshot(page)
    assert not page.locator("#reveal").is_visible()


def test_untrusted_text_and_malformed_messages_do_not_break_rendering(page):
    snapshot(page)
    page.evaluate("window.testSocket.onmessage({data: '{broken'})")
    send(page, type="boom")
    send(page, type="unknown")
    name = '<img src=x onerror="window.injected=true">'
    send(page, type="mine_planted", id="a", owner=name, arms_in_s=0)
    boom(page, owner=name, word="<script>bad</script>")
    assert page.locator("img, script:not([src])").count() == 0
    assert page.evaluate("window.injected === undefined")
    assert name.upper() in page.locator("#boom-owner").inner_text()


def test_websocket_reconnects(page):
    assert page.evaluate("window.socketCount") == 1
    page.evaluate("window.testSocket.onclose()")
    page.wait_for_function("window.socketCount === 2")
    snapshot(
        page, mines=[{"id": "b", "owner": "alex", "status": "armed", "arms_in_s": 0}]
    )
    assert page.locator('[data-id="b"]').get_attribute("data-status") == "armed"
    assert not page.locator("#boom-banner").is_visible()


def test_demo_never_connects_and_steps_are_frozen(page, static_url):
    errors = []
    page.on("pageerror", lambda error: errors.append(error))
    page.goto(f"{static_url}/overlay/?demo=1&step=6&latency=1")
    page.wait_for_function("window.overlayReady === true")
    assert page.evaluate("window.socketCount") == 0
    assert page.locator("#boom-banner").is_visible()
    before = page.locator("#stage").inner_text()
    page.wait_for_timeout(1100)
    assert page.locator("#stage").inner_text() == before
    assert not errors
    page.goto(f"{static_url}/overlay/?demo=1")
    page.wait_for_function("window.overlayReady === true")
    assert page.evaluate("window.socketCount") == 0
    page.wait_for_function("document.documentElement.dataset.demoStep !== '0'")


def test_demo_keeps_second_boom_and_reveals_only_the_remaining_duds(page, static_url):
    page.goto(f"{static_url}/overlay/?demo=1&step=0")
    page.wait_for_function("window.overlayReady === true")
    steps = page.evaluate("window.overlayDemoSteps")
    booms = [
        (i, event)
        for i, step in enumerate(steps)
        for event in step
        if event["type"] == "boom"
    ]
    assert len(booms) == 2
    second_step, second = booms[1]
    assert not any(
        event["type"] == "false_alarm" and event["id"] == second["id"]
        for step in steps
        for event in step
    )
    page.goto(f"{static_url}/overlay/?demo=1&step={second_step}")
    page.wait_for_function("window.overlayReady === true")
    assert page.locator("#boom-word").inner_text() == second["word"].upper()
    assert not page.locator("#false-alarm").is_visible()
    assert page.locator(f'[data-id="{second["id"]}"]').get_attribute("data-status") == (
        "exploded"
    )
    reveal_step = next(
        i
        for i, step in enumerate(steps)
        if any(event["type"] == "reveal" for event in step)
    )
    page.goto(f"{static_url}/overlay/?demo=1&step={reveal_step}")
    page.wait_for_function("window.overlayReady === true")
    assert page.locator("#round-stats").inner_text() == "1 boom"
    assert second["word"] not in page.locator("#duds").inner_text()
    assert page.locator("#duds p").count() == 2


def test_no_tunnel_url_hides_plant_panel(page):
    send(
        page,
        type="snapshot",
        round={"running": True},
        plant_url=None,
        mines=[{"id": "a", "owner": "mira", "status": "armed", "arms_in_s": 0}],
    )
    assert page.locator(".mine-chip").count() == 1
    assert not page.locator("#plant").is_visible()


def test_new_tunnel_snapshot_replaces_link_and_qr(page):
    snapshot(page)
    original = page.locator("#qr canvas").evaluate("canvas => canvas.toDataURL()")
    send(
        page,
        type="snapshot",
        round={"running": True},
        plant_url="https://replacement.trycloudflare.com",
        mines=[],
    )
    assert page.locator("#plant-url").inner_text() == "replacement.trycloudflare.com"
    assert (
        page.locator("#qr canvas").evaluate("canvas => canvas.toDataURL()") != original
    )


def test_snapshot_prioritizes_all_live_mines(page):
    mines = [
        {"id": str(index), "owner": f"viewer{index}", "status": "armed", "arms_in_s": 0}
        for index in range(1, 4)
    ]
    mines += [
        {"id": "4", "owner": "old", "status": "exploded", "arms_in_s": 0},
        {"id": "5", "owner": "new", "status": "arming", "arms_in_s": 20},
    ]
    snapshot(page, mines=mines)
    assert page.locator(".mine-chip").count() == 4
    for mine_id in ("1", "2", "3", "5"):
        assert page.locator(f'[data-id="{mine_id}"]').count() == 1


def test_false_alarm_stamp_appears_late_within_legal_window(page):
    page.clock.install()
    page.clock.pause_at(page.evaluate("Date.now() + 1000"))
    snapshot(page)
    boom(page)
    page.clock.fast_forward(8000)
    send(page, type="false_alarm", id="a", owner="mira")
    assert page.locator("#false-alarm").is_visible()


def test_older_boom_correction_stamps_its_chip_without_relabeling_banner(page):
    snapshot(
        page,
        mines=[
            {"id": "a", "owner": "mira", "status": "armed", "arms_in_s": 0},
            {"id": "b", "owner": "alex", "status": "armed", "arms_in_s": 0},
        ],
    )
    boom(page)
    send(
        page,
        type="boom",
        id="b",
        owner="alex",
        word="volcano",
        planted_ago_s=61,
        latency_ms=300,
        source="stt",
        at=1730000001,
        receipt=[{"text": "volcano", "hit": True}],
    )
    send(page, type="false_alarm", id="b", owner="alex")
    send(page, type="false_alarm", id="a", owner="mira")
    assert page.locator('[data-id="a"] .false-alarm-stamp').is_visible()
    assert page.locator('[data-id="b"] .false-alarm-stamp').is_visible()
    assert page.locator("#boom-owner").inner_text() == "ALEX'S MINE:"
    assert page.locator("#boom-word").inner_text() == "VOLCANO"
    assert page.locator("#false-alarm").is_visible()
    snapshot(
        page,
        mines=[
            {"id": "a", "owner": "mira", "status": "false_alarm", "arms_in_s": 0},
        ],
    )
    assert page.locator('[data-id="a"] .false-alarm-stamp').is_visible()
    assert not page.locator("#boom-banner").is_visible()


def test_boom_burst_is_single_local_and_reused_then_cleans_up(page):
    snapshot(page)
    boom(page)
    burst = page.locator("#explosion")
    assert burst.is_visible()
    flash = page.locator(".blast-flash")
    style = flash.evaluate("""element => {
        const style = getComputedStyle(element);
        const box = element.getBoundingClientRect();
        return {iterations: style.animationIterationCount,
            duration: parseFloat(style.animationDuration),
            width: box.width, height: box.height, x: box.x, y: box.y};
    }""")
    assert style["iterations"] == "1"
    assert 0 < style["duration"] <= 0.2
    assert style["width"] <= 900 and style["height"] <= 600
    assert style["x"] > 300 and style["y"] > 200
    fragments = page.locator(".fragment").count()
    assert 4 <= fragments <= 16
    boom(page, owner="alex", word="volcano")
    assert page.locator(".fragment").count() == fragments
    page.wait_for_timeout(1100)
    assert not burst.is_visible()
    assert "shaking" not in page.locator("#stage").get_attribute("class")
    assert page.locator("#boom-word").inner_text() == "VOLCANO"
    boom(page)
    snapshot(page)
    assert not burst.is_visible()


def test_long_owner_word_and_receipt_fit_without_covering_correction(page):
    snapshot(page)
    send(
        page,
        type="boom",
        id="a",
        owner="a_very_long_viewer_name_25",
        word="rollercoaster",
        planted_ago_s=125,
        latency_ms=370,
        source="stt",
        receipt=[
            {"text": word, "hit": word == "rollercoaster"}
            for word in (
                "Honestly unexpectedly everybody enthusiastically recommended "
                "another enormous rollercoaster"
            ).split()
        ],
    )
    send(page, type="false_alarm", id="a", owner="a_very_long_viewer_name_25")
    page.wait_for_timeout(1100)
    banner = page.locator("#boom-banner").bounding_box()
    assert banner and banner["y"] + banner["height"] <= 1080
    for selector in ("#boom-owner", "#boom-word", "#receipt", "#false-alarm"):
        box = page.locator(selector).bounding_box()
        assert box and banner["x"] <= box["x"]
        assert box["x"] + box["width"] <= banner["x"] + banner["width"]
        assert box["y"] + box["height"] <= banner["y"] + banner["height"]
        assert page.locator(selector).evaluate("el => el.scrollWidth <= el.clientWidth")
    stamp = page.locator("#false-alarm").bounding_box()
    owner = page.locator("#boom-owner").bounding_box()
    assert stamp["y"] + stamp["height"] <= owner["y"]


def test_suspended_audio_schedules_nothing_and_does_not_replay_after_resume(page):
    page.evaluate("""async () => {
        const audio = new AudioContext();
        await audio.suspend();
        window.testAudio = audio;
        window.resumeAudio = audio.resume.bind(audio);
        audio.resume = () => new Promise(() => {});
        window.createdSources = 0;
        for (const name of ['createOscillator', 'createBufferSource']) {
            const create = audio[name].bind(audio);
            audio[name] = (...args) => {
                window.createdSources++; return create(...args);
            };
        }
        window.AudioContext = function() { return audio; };
        for (let i = 0; i < 100; i++) {
            window.deliver({type: 'boom', id: 'a', owner: 'mira', word: 'pineapple',
                planted_ago_s: 100, latency_ms: 300, source: 'stt',
                receipt: [{text: 'pineapple', hit: true}], scores: []});
        }
    }""")
    assert page.locator("#boom-banner").is_visible()
    assert page.evaluate("window.testAudio.state") == "suspended"
    assert page.evaluate("window.createdSources") == 0
    page.mouse.click(100, 100)
    page.evaluate("window.resumeAudio()")
    assert page.evaluate("window.testAudio.state") == "running"
    assert page.evaluate("window.createdSources") == 0
    boom(page)
    assert page.evaluate("window.createdSources") == 1
    page.evaluate("window.testAudio.close()")
    boom(page)
    assert page.evaluate("window.createdSources") == 1


@pytest.mark.parametrize("repeat", [False, True])
@pytest.mark.parametrize("sample_rate", [44100, 48000])
def test_soft_airy_boom_has_loud_peak_and_rumble_without_stacking(
    page, repeat, sample_rate
):
    page.evaluate(
        """sampleRate => {
        window.testAudio = new OfflineAudioContext(1, sampleRate * 2, sampleRate);
        // Model an unlocked live context; offline audio starts after scheduling.
        Object.defineProperty(window.testAudio, 'state', {value: 'running'});
        window.resumeRendering = window.testAudio.resume.bind(window.testAudio);
        window.testAudio.resume = () => Promise.resolve();
        window.AudioContext = function() { return window.testAudio; };
    }""",
        sample_rate,
    )
    boom(page)
    result = page.evaluate(
        """async repeat => {
        const context = window.testAudio;
        const paused = repeat ? context.suspend(.05) : null;
        const rendering = context.startRendering();
        if (repeat) {
            await paused;
            window.deliver({type: 'boom', id: 'b', owner: 'alex', word: 'volcano',
                planted_ago_s: 100, latency_ms: 300, source: 'stt',
                receipt: [{text: 'volcano', hit: true}], scores: []});
            await window.resumeRendering();
        }
        const samples = (await rendering).getChannelData(0);
        let peak = 0, energy = 0, tail = 0, tailCount = 0;
        for (let i = 0; i < samples.length; i++) {
            const sample = samples[i];
            peak = Math.max(peak, Math.abs(sample));
            energy += sample * sample;
            if (i >= .5 * context.sampleRate && i < context.sampleRate) {
                tail += sample * sample; tailCount++;
            }
        }
        return {peak, rms: Math.sqrt(energy / samples.length),
            tailRms: Math.sqrt(tail / tailCount)};
    }""",
        repeat,
    )
    assert 0.86 <= result["peak"] <= 0.92  # Around -1 dBFS, including resampling.
    assert result["rms"] < 0.18
    assert result["tailRms"] > 0.01  # A sustained rumble, not a short noise burst.


@pytest.mark.parametrize("kind", ["mine_planted", "mine_armed", "spark", "fizzle"])
def test_small_cues_are_about_four_times_louder_with_a_soft_attack(page, kind):
    page.evaluate("""() => {
        window.testAudio = new OfflineAudioContext(1, 24000, 48000);
        Object.defineProperty(window.testAudio, 'state', {value: 'running'});
        window.AudioContext = function() { return window.testAudio; };
    }""")
    send(page, type=kind, id="a", owner="mira", arms_in_s=30)
    result = page.evaluate("""async () => {
        const context = window.testAudio;
        const samples = (await context.startRendering()).getChannelData(0);
        let peak = 0, first = -1;
        for (let i = 0; i < samples.length; i++) {
            peak = Math.max(peak, Math.abs(samples[i]));
            if (first === -1 && Math.abs(samples[i]) > .00001) first = i;
        }
        let attackPeak = 0;
        for (let i = first; i < first + 48; i++) {
            attackPeak = Math.max(attackPeak, Math.abs(samples[i]));
        }
        return {peak, attackPeak};
    }""")
    assert 0.17 <= result["peak"] <= 0.19
    assert result["attackPeak"] < result["peak"] * 0.6


def test_wp15_shrink_keeps_full_banner_then_moves_smoothly_to_compact(page):
    page.clock.install()
    page.clock.pause_at(page.evaluate("Date.now() + 1000"))
    snapshot(page)
    boom(page)
    page.clock.run_for(2990)
    box = page.locator("#boom-banner").bounding_box()
    assert box["x"] == 300 and box["width"] == 1320
    page.clock.run_for(20)
    page.locator("#boom-banner").evaluate(
        "el => el.getAnimations({subtree: true}).forEach(a => { "
        "a.pause(); a.currentTime = 150; })"
    )
    middle = page.locator("#boom-banner").bounding_box()
    assert 560 < middle["width"] < 1320
    page.locator("#boom-banner").evaluate(
        "el => el.getAnimations({subtree: true}).forEach(a => a.finish())"
    )
    box = page.locator("#boom-banner").bounding_box()
    assert box == pytest.approx({"x": 48, "y": 772, "width": 560, "height": 260})
    assert page.locator("#receipt mark").inner_text() == "pineapple"
    assert (
        page.locator("#receipt").evaluate(
            "el => parseFloat(getComputedStyle(el).fontSize)"
        )
        >= 22
    )
    send(page, type="false_alarm", id="a", owner="mira", scores=[])
    assert page.locator("#false-alarm").is_visible()
    assert page.locator("#boom-banner").bounding_box() == box


def test_wp15_leaderboard_updates_restores_and_clears_feedback(page):
    scores = [{"owner": "mira", "points": 2}, {"owner": "alex", "points": 1}]
    send(
        page,
        type="snapshot",
        round={"running": True},
        plant_url="https://example.org",
        mines=[],
        scores=scores,
    )
    assert page.locator("#scoreboard").is_visible()
    assert page.locator(".score-row").count() == 2
    assert page.locator(".score-owner").all_text_contents() == ["mira", "alex"]
    boom(page)
    # An authoritative empty score list replaces the previous one.
    assert page.locator(".score-row").count() == 0
    send(
        page,
        type="boom",
        id="b",
        owner="alex",
        word="volcano",
        planted_ago_s=30,
        latency_ms=10,
        source="typed",
        receipt=[{"text": "volcano", "hit": True}],
        scores=[{"owner": "alex", "points": 3}, {"owner": "mira", "points": 2}],
    )
    assert page.locator(".score-owner").all_text_contents() == ["alex", "mira"]
    assert page.locator(".score-gain").inner_text() == "+1"
    page.wait_for_timeout(1100)
    assert page.locator(".score-gain").count() == 0
    send(
        page,
        type="snapshot",
        round={"running": False},
        plant_url=None,
        mines=[],
        scores=scores,
    )
    assert not page.locator("#boom-banner").is_visible()
    assert page.locator(".score-owner").all_text_contents() == ["mira", "alex"]
    assert page.locator(".score-gain").count() == 0


def test_wp15_new_boom_resets_shrink_and_snapshot_cancels_it(page):
    page.clock.install()
    page.clock.pause_at(page.evaluate("Date.now() + 1000"))
    snapshot(page)
    boom(page)
    page.clock.run_for(2500)
    boom(page, owner="alex", word="volcano")
    page.clock.run_for(1000)
    assert page.locator("#boom-banner").bounding_box()["width"] == 1320
    snapshot(page)
    page.clock.run_for(4000)
    assert not page.locator("#boom-banner").is_visible()
    assert "compact" not in page.locator("#boom-banner").get_attribute("class")


@pytest.mark.parametrize(
    "leaders,count,headline",
    [
        ([{"owner": "mira", "booms": 2}], 3, "TOP TRAPPER: mira · 2 booms"),
        (
            [{"owner": "alex", "booms": 1}, {"owner": "mira", "booms": 1}],
            2,
            "TOP TRAPPERS: alex, mira · 1 boom",
        ),
        ([], 2, "2 booms"),
        ([], 0, "No booms this round"),
    ],
)
def test_wp15_reveal_headline_and_lower_band(page, leaders, count, headline):
    snapshot(page)
    send(
        page,
        type="reveal",
        duds=[{"owner": "sam", "word": "telescope"}],
        stats={"booms": count},
        round_top=leaders,
        scores=[{"owner": "mira", "points": 4}],
    )
    assert page.locator("#round-top").inner_text() == headline
    assert page.locator("#reveal").bounding_box() == pytest.approx(
        {"x": 48, "y": 728, "width": 1240, "height": 304}
    )
    assert page.locator("#scoreboard").is_visible()
    send(
        page,
        type="snapshot",
        round={"running": False},
        plant_url=None,
        mines=[],
        scores=[{"owner": "mira", "points": 4}],
    )
    assert page.locator("#round-top").inner_text() == headline


def test_wp15_frozen_demo_covers_compact_correction_and_session_panel(page, static_url):
    page.goto(f"{static_url}/overlay/?demo=1&step=0")
    page.wait_for_function("window.overlayReady === true")
    compact_steps = page.evaluate("window.overlayDemoCompactSteps")
    assert len(compact_steps) == 2
    for step in compact_steps:
        page.goto(f"{static_url}/overlay/?demo=1&step={step}")
        page.wait_for_function("window.overlayReady === true")
        assert page.locator("#boom-banner").bounding_box()["width"] == 560
        assert page.locator("#receipt mark").inner_text()
        assert page.locator(".score-row").count() > 0
    steps = page.evaluate("window.overlayDemoSteps")
    correction_step = next(
        i
        for i, events in enumerate(steps)
        if any(e["type"] == "false_alarm" for e in events)
    )
    page.goto(f"{static_url}/overlay/?demo=1&step={correction_step}")
    page.wait_for_function("window.overlayReady === true")
    assert page.locator("#false-alarm").is_visible()
    assert page.locator("#boom-banner").bounding_box()["width"] == 560


def test_wp15_reveal_cancels_shrink_and_malformed_scores_are_ignored(page):
    page.clock.install()
    page.clock.pause_at(page.evaluate("Date.now() + 1000"))
    snapshot(page)
    boom(page)
    send(
        page,
        type="false_alarm",
        id="a",
        owner="mira",
        scores=[{"owner": "mira", "points": "invalid"}],
    )
    assert not page.locator("#false-alarm").is_visible()
    send(
        page,
        type="reveal",
        stats={"booms": 1},
        round_top=[{"owner": "mira", "booms": 1}],
        duds=[],
        scores=[{"owner": "mira", "points": 1}],
    )
    page.clock.run_for(4000)
    assert not page.locator("#boom-banner").is_visible()
    assert "compact" not in page.locator("#boom-banner").get_attribute("class")
    assert page.locator("#reveal").is_visible()


def test_wp15_long_compact_receipt_and_tied_reveal_stay_in_their_boxes(page):
    snapshot(page)
    send(
        page,
        type="boom",
        id="a",
        owner="a_very_long_viewer_name_25",
        word="rollercoaster",
        planted_ago_s=120,
        latency_ms=12,
        source="stt",
        receipt=[
            {"text": word, "hit": word == "rollercoaster"}
            for word in (
                "Honestly unexpectedly everybody enthusiastically recommended "
                "another enormous rollercoaster"
            ).split()
        ],
    )
    page.wait_for_timeout(3400)
    box = page.locator("#boom-banner").bounding_box()
    for selector in ["#boom-owner", "#boom-word", "#receipt"]:
        child = page.locator(selector).bounding_box()
        assert child["x"] >= box["x"]
        assert child["x"] + child["width"] <= box["x"] + box["width"]
        assert child["y"] + child["height"] <= box["y"] + box["height"]
    leaders = [{"owner": f"viewer_{i:03}", "booms": 1} for i in range(200)]
    send(
        page, type="reveal", stats={"booms": 200}, round_top=leaders, duds=[], scores=[]
    )
    assert all(
        row["owner"] in page.locator("#round-top").inner_text() for row in leaders
    )
    assert page.locator("#round-top").evaluate(
        "el => el.scrollHeight > el.clientHeight"
    )
    assert page.locator("#reveal").bounding_box()["height"] == 304
