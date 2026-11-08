"""Focused browser check for feedback independence, recovery, and removal."""
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
    contact = page.get_by_role("link", name="test@example.invalid", exact=True)
    for locale in ("lv", "en", "ru"):
        page.select_option("#language", locale)
        assert contact.is_visible()
        assert contact.get_attribute("href") == "mailto:test@example.invalid"
    page.select_option("#language", "en")
    page.locator('[data-act="start"]').click()
    page.locator('[data-module="S01"]').check()
    page.locator('[data-act="confirm"]').click()
    choose(page, "A")
    act(page, "previous")
    act(page, "feedback")
    page.locator('[data-feedback-reason="question"]').check()
    page.locator('[data-feedback-reason="answer:B"]').check()
    page.locator("#feedback-comment").fill("Synthetic feedback only")
    act(page, "feedbackContinue")

    saved = backup(page)
    assert saved["answers"]["SYN_01"]["codes"] == ["A"]
    assert saved["feedback"]["SYN_01"]["reasons"] == ["question", "answer:B"]
    assert saved["feedback"]["SYN_01"]["comment"] == "Synthetic feedback only"
    restore(page, saved)
    restored = backup(page)
    assert restored["answers"] == saved["answers"]
    assert restored["feedback"] == saved["feedback"]

    act(page, "previous")
    act(page, "feedback")
    act(page, "removeFeedback")
    removed = backup(page)
    assert "SYN_01" not in removed["feedback"]
    assert removed["answers"]["SYN_01"]["codes"] == ["A"]
    act(page, "results")
    assert contact.is_visible()
    assert page.locator('[data-act="copyFeedback"]').is_visible()
    assert not errors, errors
    assert not network, network
    browser.close()

print("PASS: synthetic feedback saves independently, round-trips, and can be removed.")
