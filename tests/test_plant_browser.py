"""WP11 phone flow; Chromium is optional for the default suite."""

import json
import re
import socket
import threading
import time

import pytest

pytestmark = pytest.mark.browser


@pytest.fixture(scope="module")
def plant_server():
    import uvicorn

    from minefield.server.app import create_app
    from minefield.server.plant import create_plant_app

    runtime = create_app().state.runtime
    runtime.game.start(time.time())
    listener = socket.socket()
    listener.bind(("127.0.0.1", 0))
    port = listener.getsockname()[1]
    server = uvicorn.Server(
        uvicorn.Config(create_plant_app(runtime), log_level="error")
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
def phone(plant_server):
    from playwright.sync_api import sync_playwright

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.new_context(
            viewport={"width": 390, "height": 844},
            permissions=["clipboard-read", "clipboard-write"],
        )
        page = context.new_page()
        yield page
        browser.close()


def test_six_cards_pick_copy_expiry_and_new_hand(phone, plant_server):
    from playwright.sync_api import expect

    phone.clock.install()
    phone.goto(plant_server)
    cards = phone.locator("#cards button")
    expect(cards).to_have_count(6)
    assert not phone.evaluate("document.documentElement.scrollWidth > innerWidth")
    selected = cards.first.inner_text()
    cards.first.click()
    expect(phone.locator("#selected-word")).to_have_text(selected)
    expect(phone.locator("#command")).to_have_value(re.compile(r"!mine [A-Z2-9]{4}"))
    phone.get_by_role("button", name="Copy command", exact=True).click()
    expect(phone.get_by_role("button", name="Copied!", exact=True)).to_be_visible()
    assert (
        phone.evaluate("navigator.clipboard.readText()")
        == phone.locator("#command").input_value()
    )
    assert not phone.evaluate("document.documentElement.scrollWidth > innerWidth")
    phone.clock.fast_forward(301_000)
    expect(phone.locator("#expiry")).to_contain_text("expired")
    expect(
        phone.get_by_role("button", name="Copy command", exact=True)
    ).to_be_disabled()
    phone.get_by_role("button", name="Pick a new hand", exact=True).click()
    expect(cards).to_have_count(6)


def test_errors_retry_and_clipboard_fallback(phone, plant_server):
    from playwright.sync_api import expect

    phone.route(
        "**/api/hand",
        lambda route: route.fulfill(
            status=409,
            content_type="application/json",
            body=json.dumps({"detail": "No active round"}),
        ),
    )
    phone.goto(plant_server)
    expect(phone.get_by_role("alert")).to_contain_text("No active round")
    phone.unroute("**/api/hand")
    phone.get_by_role("button", name="Try again", exact=True).click()
    cards = phone.locator("#cards button")
    expect(cards).to_have_count(6)
    phone.route(
        "**/api/pick",
        lambda route: route.fulfill(
            status=409,
            content_type="application/json",
            body=json.dumps({"detail": "Unknown or expired hand, pick a new hand"}),
        ),
    )
    cards.first.click()
    expect(phone.get_by_role("alert")).to_contain_text("expired hand")
    expect(cards.first).to_be_enabled()
    phone.unroute("**/api/pick")
    phone.evaluate(
        "Object.defineProperty(navigator, 'clipboard', "
        "{value: {writeText: () => Promise.reject(new Error())}})"
    )
    cards.first.click()
    phone.get_by_role("button", name="Copy command", exact=True).click()
    expect(phone.locator("#copy-help")).to_contain_text("select")
    expect(phone.locator("#command")).to_be_editable(editable=False)
