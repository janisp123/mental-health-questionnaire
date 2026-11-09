"""Focused browser check for synthetic answer backup and restore."""
import tempfile
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "full_bank"))
from browser_helpers import act, backup, choose, launch, open_page, restore
from runtime_fixture import write_fixture


with tempfile.TemporaryDirectory() as tmp, sync_playwright() as pw:
    html_path = Path(tmp) / "synthetic.html"
    write_fixture(html_path)
    browser = launch(pw)
    page, errors, network = open_page(browser, html_path)
    page.locator('[data-act="start"]').click()
    page.locator('[data-module="S01"]').check()
    page.locator('[data-act="confirm"]').click()
    choose(page, "B")
    act(page, "skip")
    saved = backup(page)
    assert saved["answers"]["SYN_01"]["codes"] == ["B"]
    assert saved["answers"]["SYN_02"]["kind"] == "skip"

    restored, restore_errors, restore_network = open_page(browser, html_path)
    restore(restored, saved)
    restored.wait_for_selector('.question[data-question="SYN_03"]')
    round_trip = backup(restored)
    assert round_trip["answers"] == saved["answers"]
    assert not errors and not restore_errors, errors + restore_errors
    assert not network and not restore_network, network + restore_network
    browser.close()

print("PASS: synthetic choice and skip records restore offline with conditions respected.")
