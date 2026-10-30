"""Save browser screenshots; overlay demo needs no running game server."""

import argparse
import base64
import functools
import http.server
import os
import threading
from contextlib import contextmanager
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


@contextmanager
def static_server():
    class QuietHandler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *_):
            pass

    handler = functools.partial(QuietHandler, directory=str(ROOT / "web"))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}"
    finally:
        server.shutdown()
        server.server_close()
        thread.join()


def shoot_overlay(browser, output):
    with static_server() as base:
        page = browser.new_page(viewport={"width": 1920, "height": 1080})
        page.goto(f"{base}/overlay/?demo=1&step=0&latency=1")
        page.wait_for_function("window.overlayReady === true")
        count = page.evaluate("window.overlayDemoSteps.length")
        shots = []
        for step in range(count):
            page.goto(f"{base}/overlay/?demo=1&step={step}&latency=1")
            page.wait_for_function("window.overlayReady === true")
            page.evaluate("document.fonts.ready")
            image = page.screenshot(
                path=str(output / f"overlay-{step:02}.png"), omit_background=True
            )
            label = page.evaluate(
                "[...new Set(window.overlayDemoSteps["
                f"{step}].map(event => event.type))].join(' + ')"
            )
            encoded = base64.b64encode(image).decode("ascii")
            shots.append(
                f'<figure><img src="data:image/png;base64,{encoded}">'
                f"<figcaption>{step:02} · {label}</figcaption></figure>"
            )
        page.set_viewport_size({"width": 1500, "height": 1200})
        page.set_content(
            "<style>body{margin:0;padding:24px;background:#11131a;color:#eee;"
            "font:16px Arial}h1{font-size:24px;margin:0 0 20px}"
            "main{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}"
            "figure{margin:0;border:1px solid #42444e;background:"
            "repeating-conic-gradient(#242731 0% 25%,#20232b 0% 50%) 0/24px 24px}"
            "img{display:block;width:100%}figcaption{padding:12px;background:#191b23}"
            "</style><h1>Minefield · all demo steps · "
            "transparent background preview</h1>"
            "<main>" + "".join(shots) + "</main>"
        )
        page.screenshot(path=str(output / "overlay-gallery.png"), full_page=True)
        page.close()
        print(f"Saved {count} overlay steps and overlay-gallery.png to {output}")


def shoot_page(browser, name, output):
    port = (
        os.environ.get("PLANT_PORT", "8101")
        if name == "plant"
        else (os.environ.get("GAME_PORT", "8100"))
    )
    path = "/" if name == "plant" else f"/{name}"
    width = {"dock": 400, "plant": 390, "mic": 1000}[name]
    page = browser.new_page(viewport={"width": width, "height": 900})
    page.goto(f"http://127.0.0.1:{port}{path}")
    page.evaluate("document.fonts.ready")
    page.wait_for_timeout(300)
    if page.evaluate("document.documentElement.scrollWidth > innerWidth"):
        raise RuntimeError(f"{name} overflows its {width}px viewport")
    target = output / f"{name}.png"
    page.screenshot(path=str(target), full_page=True)
    page.close()
    print(f"Saved {target}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("page", choices=("overlay", "dock", "plant", "mic"))
    args = parser.parse_args()
    from playwright.sync_api import sync_playwright

    output = ROOT / "data" / "shots"
    output.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        try:
            if args.page == "overlay":
                shoot_overlay(browser, output)
            else:
                shoot_page(browser, args.page, output)
        finally:
            browser.close()


if __name__ == "__main__":
    main()
