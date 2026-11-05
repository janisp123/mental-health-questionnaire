#!/usr/bin/env python3
"""Standard-library structural checks for the two-section, 3-language pilot."""
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("pilot_build", ROOT / "tools" / "build_pilot.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
bundle = module.build_bundle()
assert bundle["schema"] == "offline-questionnaire-pilot-v1"
groups = {g["id"]: g for g in bundle["groups"]}
opening = groups["opening"]["questions"]
mood = groups["02"]["questions"]
questions = [q for group in groups.values() for q in group["questions"]]
assert len({q["id"] for q in questions}) == len(questions)
assert [q["order"] for q in opening] == list(range(20))
assert [q["order"] for q in mood] == list(range(43, 64))
assert opening[0]["id"] == "M33_01"
assert opening[5]["id"] == "M06_01"
assert mood[-1]["id"] == "M02_21"
assert all(set(q["translations"]) == {"lv","en","ru"} for q in questions)
for q in questions:
    codes=set(q["choiceCodes"])
    assert len(codes) == len(q["choiceCodes"])
    assert all(set(q["translations"][lang]["choices"]) == codes for lang in ("lv","en","ru"))
    assert all(q["translations"][lang]["title"] for lang in ("lv","en","ru"))
assert set(bundle["ui"]) == {"lv","en","ru"}
keys={lang:set(v) for lang,v in bundle["ui"].items()}
assert keys["lv"] == keys["en"] == keys["ru"], "Missing UI translations"
html = module.make_html()
assert len(html)>60000 and "<!doctype html>" in html
assert html.count('id="pilot-data"') == 1
assert "<script src=" not in html and "<link rel=" not in html
assert "connect-src &#39;none&#39;" in html
assert "navigator.sendBeacon" not in html and "fetch(" not in html and "XMLHttpRequest" not in html
blob=re.search(r'<script id="pilot-data" type="application/json">(.*?)</script>',html,re.S)
assert blob, "Embedded data missing"
stored=json.loads(blob.group(1))
assert stored == bundle
assert stored["release_status"]["en"] == "DRAFT_NOT_RELEASED"
assert stored["release_status"]["ru"] == "DRAFT_NOT_RELEASED"
print(f"PASS structural: {len(questions)} questions, 3 languages, no runtime network imports")
print("NOT tested: clinical wording, user-interface behavior or real Android Chrome.")

