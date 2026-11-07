"""Focused browser check for single, multi-select, and skipped answers."""
import json
import tempfile
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "full_bank"))
from browser_helpers import act, backup, launch, open_page
from runtime_fixture import write_fixture


with tempfile.TemporaryDirectory() as tmp, sync_playwright() as pw:
    html_path = Path(tmp) / "synthetic.html"
    write_fixture(html_path)
    browser = launch(pw)
    page, errors, network = open_page(browser, html_path)
    downloads = []
    page.on("download", lambda download: downloads.append(download.suggested_filename))
    page.locator('[data-act="start"]').click()
    page.locator('[data-module="S01"]').check()
    page.locator('[data-module="S02"]').check()
    page.locator('[data-act="confirm"]').click()
    assert page.locator('.question').get_attribute("data-question") == "SYN_01"

    single_choice = page.locator('input[name="answer"][value="B"]')
    single_choice.click()
    assert single_choice.is_checked(), "The selected answer should be visible immediately"
    assert single_choice.locator("..").locator(".choice-checkmark").is_visible(), "Selected answer needs a clear checkmark"
    selected_color = single_choice.locator("..").evaluate("el => getComputedStyle(el).backgroundColor")
    assert selected_color != "rgb(27, 44, 58)", f"Selected choice is not visually highlighted: {selected_color}"
    assert page.locator('.question').get_attribute("data-question") == "SYN_01"
    page.wait_for_timeout(500)
    assert page.locator('.question').get_attribute("data-question") == "SYN_01"
    page.wait_for_timeout(500)
    assert page.locator('.question').get_attribute("data-question") == "SYN_01"
    page.wait_for_timeout(400)
    assert page.locator('.question').get_attribute("data-question") == "SYN_02"
    assert downloads == [], "Answering a question must not trigger a download"
    saved = backup(page)
    assert saved["answers"]["SYN_01"]["codes"] == ["B"]

    page.locator('input[name="answer"][value="A"]').check()
    page.locator('input[name="answer"][value="B"]').check()
    page.locator('input[name="answer"][value="C"]').check()
    selection_hint = page.locator(".selection-hint").inner_text()
    assert selection_hint == "You can select up to 3 answers.", f"Unexpected selection hint: {selection_hint!r}"
    page.locator('input[name="answer"][value="D"]').locator("..").click()
    assert page.locator('input[name="answer"][value="D"]').is_checked() is False
    assert "3" in page.locator(".notice").inner_text()
    assert backup(page)["answers"].get("SYN_02") is None
    act(page, "save")
    assert page.locator('.question').get_attribute("data-question") == "SYN_03"
    saved_codes = backup(page)["answers"].get("SYN_02", {}).get("codes", [])
    assert sorted(saved_codes) == ["A", "B", "C"], f"Expected up to three saved codes, got {saved_codes!r}"

    page.locator('input[name="answer"][value="A"]').click()
    assert page.locator('input[name="answer"][value="A"]').is_checked()
    page.locator('.question-nav [data-act="skip"]').click()
    assert page.locator('[data-act="saveAndContinue"]').is_visible()
    assert page.locator('[data-act="continueWithoutSaving"]').is_visible()
    page.wait_for_timeout(1400)
    assert page.locator('[data-act="continueWithoutSaving"]').is_visible(), "A pending answer must not replace a later Skip"
    assert len(downloads) == 3, downloads
    with page.expect_download() as event:
        page.locator('[data-act="saveAndContinue"]').click()
    saved_at_boundary = json.loads(event.value.path().read_text())
    assert saved_at_boundary["currentId"] == "SYN_04"
    assert page.locator('.question').get_attribute("data-question") == "SYN_04"
    page.locator('[data-act="skip"]').click()
    assert page.locator('[data-act="continueWithoutSaving"]').is_visible()
    assert len(downloads) == 4
    page.locator('[data-act="continueWithoutSaving"]').click()
    assert page.locator("#app").inner_text().find("Results / copy") >= 0
    assert saved_at_boundary["answers"]["SYN_03"]["kind"] == "skip"
    assert not errors, errors
    assert not network, network
    browser.close()

print("PASS: synthetic single choice, deferred multi-select, skip, offline load.")
