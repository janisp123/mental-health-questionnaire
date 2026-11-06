"""Small browser layout check using the synthetic bundle and real app CSS."""
import tempfile
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "full_bank"))
from browser_helpers import launch, open_page
from runtime_fixture import write_fixture


with tempfile.TemporaryDirectory() as tmp, sync_playwright() as pw:
    html_path = Path(tmp) / "synthetic.html"
    write_fixture(html_path)
    browser = launch(pw)
    page, errors, network = open_page(browser, html_path)
    page.locator('[data-act="start"]').click()
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
    assert not errors, errors
    assert not network, network
    browser.close()

print("PASS: synthetic mobile/desktop layout, fixed skip navigation, accessible flag label, offline load.")
