"""WP4 browser acceptance; intentionally excluded from the default suite."""

import socket
import threading
import time
from dataclasses import replace

import pytest

pytestmark = pytest.mark.browser


@pytest.fixture(scope="module")
def server_url():
    import uvicorn

    from minefield.core.config import Config
    from minefield.server.app import create_app

    listener = socket.socket()
    listener.bind(("127.0.0.1", 0))
    port = listener.getsockname()[1]
    server = uvicorn.Server(
        uvicorn.Config(
            create_app(config=replace(Config(), ARM_DELAY_S=0), debug=True),
            log_level="error",
            lifespan="on",
        )
    )
    thread = threading.Thread(
        target=server.run, kwargs={"sockets": [listener]}, daemon=True
    )
    thread.start()
    deadline = time.monotonic() + 5
    while not server.started and time.monotonic() < deadline:
        time.sleep(0.01)
    assert server.started
    yield f"http://127.0.0.1:{port}"
    server.should_exit = True
    thread.join(timeout=5)
    assert not thread.is_alive()


@pytest.fixture
def page(server_url):
    from playwright.sync_api import sync_playwright

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport={"width": 400, "height": 900})
        page.request.post(server_url + "/dock/round/end")
        yield page
        browser.close()


def test_round_controls_typed_and_false_alarm(page, server_url):
    from playwright.sync_api import expect

    page.goto(server_url + "/dock")
    expect(page.get_by_text("Connected", exact=True)).to_be_visible()
    page.get_by_role("button", name="Start round", exact=True).click()
    expect(page.get_by_role("button", name="End round", exact=True)).to_be_enabled()
    response = page.request.post(
        server_url + "/dock/debug/plant", data={"owner": "alice", "word": "pineapple"}
    )
    assert response.ok
    expect(page.locator("#mines")).to_contain_text("alice")
    assert "pineapple" not in page.locator("#mines").inner_text()
    page.get_by_label("Typed speech").fill("I would like pineapple")
    page.get_by_role("button", name="Send typed speech", exact=True).click()
    button = page.get_by_role("button", name="False alarm", exact=True)
    expect(button).to_be_enabled()
    button.click()
    expect(page.locator("#mines")).to_contain_text("false_alarm")
    expect(button).to_be_disabled()
    page.get_by_role("button", name="End round", exact=True).click()
    expect(page.get_by_role("button", name="Start round", exact=True)).to_be_enabled()


def test_false_alarm_expires_after_ten_seconds(page, server_url):
    from playwright.sync_api import expect

    page.clock.install()
    page.goto(server_url + "/dock")
    page.get_by_role("button", name="Start round", exact=True).click()
    page.request.post(
        server_url + "/dock/debug/plant", data={"owner": "bob", "word": "volcano"}
    )
    page.get_by_label("Typed speech").fill("volcano")
    page.get_by_role("button", name="Send typed speech", exact=True).click()
    button = page.get_by_role("button", name="False alarm", exact=True)
    expect(button).to_be_enabled()
    page.clock.fast_forward(10_100)
    expect(button).to_be_disabled()
    expect(page.locator("#mines")).not_to_contain_text("bob")


def test_status_snapshot_reload_and_400px_layout(page, server_url):
    from playwright.sync_api import expect

    page.request.post(server_url + "/dock/round/start")
    owner = "a_very_long_viewer_name_" * 4
    page.request.post(
        server_url + "/dock/debug/plant", data={"owner": owner, "word": "pineapple"}
    )
    page.request.post(
        server_url + "/stt/status",
        data={
            "ok": True,
            "backend": "flux",
            "deepgram": "connected",
            "mic": "connected",
            "lag_ms_p95": 100,
            "reconnects": 0,
        },
    )
    page.goto(server_url + "/dock")
    expect(page.locator("#mines")).to_contain_text(owner)
    expect(page.locator('[data-health="engine"]')).to_have_attribute(
        "data-state", "connected"
    )
    assert "pineapple" not in page.locator("#mines").inner_text()
    assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth")
    page.reload()
    expect(page.locator("#mines")).to_contain_text(owner)
    expect(page.get_by_role("button", name="False alarm", exact=True)).to_be_disabled()


def test_dropped_socket_reconnects_and_restores_snapshot(page, server_url):
    from playwright.sync_api import expect

    page.add_init_script("""
      window.WebSocket = class extends WebSocket {
        constructor(...args) { super(...args); window.testSocket = this; }
      };
    """)
    page.request.post(server_url + "/dock/round/start")
    page.request.post(
        server_url + "/dock/debug/plant",
        data={"owner": "reconnect_viewer", "word": "banana"},
    )
    page.goto(server_url + "/dock")
    expect(page.locator("#mines")).to_contain_text("reconnect_viewer")
    page.evaluate("window.oldSocket = window.testSocket; window.testSocket.close()")
    page.wait_for_function(
        "window.testSocket !== window.oldSocket && "
        "window.testSocket.readyState === WebSocket.OPEN"
    )
    expect(page.get_by_text("Connected", exact=True)).to_be_visible()
    expect(page.locator("#mines")).to_contain_text("reconnect_viewer")
