"""Shared offline browser helpers for synthetic questionnaire fixtures."""
import json
import os
import sys

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))


def launch(pw):
    return pw.chromium.launch(executable_path=os.getenv("QUESTIONNAIRE_BROWSER"), args=["--no-sandbox"])


def act(page, key):
    button = page.locator(f'[data-act="{key}"]:visible').first
    if not button.count():
        page.locator("footer details").first.locator("summary").click()
        button = page.locator(f'[data-act="{key}"]:visible').first
    button.click()
    if key not in ("saveAndContinue", "continueWithoutSaving"):
        continue_button = page.locator('[data-act="continueWithoutSaving"]:visible')
        if continue_button.count():
            continue_button.click()


def qid(page):
    return page.locator(".question").get_attribute("data-question")


def choose(page, code):
    # The app deliberately ignores rapid taps for 500 ms to prevent double answers.
    page.wait_for_timeout(520)
    page.locator(f'input[name="answer"][value="{code}"]').locator("..").click()
    continue_button = page.locator('[data-act="continueWithoutSaving"]:visible')
    if continue_button.count():
        continue_button.click()


def backup(page):
    with page.expect_download() as event:
        act(page, "backup")
    return json.loads(event.value.path().read_text())


def restore(page, payload):
    page.locator("#restore").set_input_files({
        "name": "synthetic-recovery.json",
        "mimeType": "application/json",
        "buffer": json.dumps(payload).encode(),
    })
    page.wait_for_timeout(100)


def open_page(browser, path: Path):
    page = browser.new_page(accept_downloads=True, offline=True, viewport={"width": 390, "height": 844})
    errors, network = [], []
    page.on("pageerror", lambda error: errors.append(str(error)))
    page.on("request", lambda request: network.append(request.url)
            if request.url.startswith(("http:", "https:")) else None)
    page.on("dialog", lambda dialog: dialog.accept())
    page.goto(path.as_uri())
    page.select_option("#language", "en")
    return page, errors, network
