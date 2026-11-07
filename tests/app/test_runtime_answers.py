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

    page.locator('input[name="answer"][value="B"]').check()
    assert page.locator('.question').get_attribute("data-question") == "SYN_02"
    assert downloads == [], "Answering a question must not trigger a download"
    saved = backup(page)
    assert saved["answers"]["SYN_01"]["codes"] == ["B"]

    page.locator('input[name="answer"][value="A"]').check()
    page.locator('input[name="answer"][value="B"]').check()
    page.locator('input[name="answer"][value="C"]').check()
    assert page.locator(".selection-hint").inner_text() == "Vari izvēlēties ne vairāk kā 3 atbildes."
    page.locator('input[name="answer"][value="D"]').check()
    assert page.locator('input[name="answer"][value="D"]').is_checked() is False
    assert "3" in page.locator(".notice").inner_text()
    assert backup(page)["answers"].get("SYN_02") is None
    act(page, "save")
    assert page.locator('.question').get_attribute("data-question") == "SYN_03"
    saved_codes = backup(page)["answers"].get("SYN_02", {}).get("codes", [])
    assert sorted(saved_codes) == ["A", "B", "C"], f"Expected up to three saved codes, got {saved_codes!r}"

    page.locator('[data-act="skip"]').click()
    assert page.locator('[data-act="saveAndContinue"]').is_visible()
    assert page.locator('[data-act="continueWithoutSaving"]').is_visible()
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
