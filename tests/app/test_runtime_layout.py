"""Small browser layout check using the synthetic bundle and real app CSS."""
import tempfile
import sys
import re
from pathlib import Path

from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "full_bank"))
from browser_helpers import launch, open_page
from runtime_fixture import write_fixture, LOCALES


with tempfile.TemporaryDirectory() as tmp, sync_playwright() as pw:
    html_path = Path(tmp) / "synthetic.html"
    write_fixture(html_path)
    browser = launch(pw)
    page, errors, network = open_page(browser, html_path)
    assert not page.locator('[data-act="guide"]').count()
    assert page.locator("[data-act=start]").count() == 1
    page.locator('[data-act="start"]').click()
    assert page.locator("[data-module]").count() == 2
    assert "3 questions" in page.locator(".card").inner_text()
    assert not re.search(r"\b0/\d+\b", page.locator(".card").inner_text())
    assert not page.locator(".section-progress").count()
    page.set_viewport_size({"width": 320, "height": 844})
    for locale in LOCALES:
        page.select_option("#language", locale)
        confirm = page.locator('[data-act="confirm"]').bounding_box()
        cancel = page.locator('[data-act="cancel"]').bounding_box()
        horizontal_gap = cancel["x"] - (confirm["x"] + confirm["width"])
        vertical_gap = cancel["y"] - (confirm["y"] + confirm["height"])
        assert max(horizontal_gap, vertical_gap) >= 8, f"Section buttons touch in {locale}"
    page.select_option("#language", "en")
    page.locator('[data-module="S01"]').check()
    page.locator('[data-act="confirm"]').click()
    page.wait_for_selector(".question-nav")

    for width, height in ((390, 844), (1280, 720)):
        page.set_viewport_size({"width": width, "height": height})
        assert page.evaluate("document.documentElement.scrollWidth <= innerWidth"), f"Horizontal overflow at {width}px"
        nav = page.locator(".question-nav")
        box = nav.bounding_box()
        assert page.evaluate("getComputedStyle(document.querySelector('.question-nav')).position") == "fixed"
        assert abs(box["y"] + box["height"] - height) < 2, f"Navigation not anchored to viewport at {width}px"
        assert nav.locator('[data-act="skip"]').bounding_box()["height"] >= 44
    assert page.locator(".feedback-flag").get_attribute("aria-label")
    for locale in LOCALES:
        page.select_option("#language", locale)
        tools = page.locator("footer details").first
        summary = tools.locator("summary")
        summary.click()
        assert tools.get_by_role("navigation", name=summary.inner_text(), exact=True).count() == 1, locale
    assert not errors, errors
    assert not network, network
    browser.close()

print("PASS: synthetic mobile/desktop layout, fixed skip navigation, accessible flag label, offline load.")
