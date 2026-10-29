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
    snapshot(page)
    boom(page)
    page.clock.fast_forward(8000)
    send(page, type="false_alarm", id="a", owner="mira")
    assert page.locator("#false-alarm").is_visible()
