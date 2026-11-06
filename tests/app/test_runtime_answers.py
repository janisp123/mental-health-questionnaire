"""Focused browser check for single, multi-select, and skipped answers."""
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
    page.locator('[data-act="start"]').click()
    assert page.locator('.question').get_attribute("data-question") == "SYN_01"

    page.locator('input[name="answer"][value="B"]').check()
    assert page.locator('.question').get_attribute("data-question") == "SYN_02"
    saved = backup(page)
    assert saved["answers"]["SYN_01"]["codes"] == ["B"]

    page.locator('input[name="answer"][value="A"]').check()
    page.locator('input[name="answer"][value="B"]').check()
    assert backup(page)["answers"].get("SYN_02") is None
    act(page, "save")
    assert page.locator('.question').get_attribute("data-question") == "SYN_03"
    assert backup(page)["answers"]["SYN_02"]["codes"] == ["A", "B"]

    act(page, "skip")
    assert page.locator("#app").inner_text().find("Results / copy") >= 0
    assert backup(page)["answers"]["SYN_03"]["kind"] == "skip"
    assert not errors, errors
    assert not network, network
    browser.close()

print("PASS: synthetic single choice, deferred multi-select, skip, offline load.")
