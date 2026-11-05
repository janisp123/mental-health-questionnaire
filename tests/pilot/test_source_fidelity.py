"""Compare every registered group's built content to the separate frozen v16 bank."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from build_pilot import build_bundle

TEXT = {"title", "choices", "help", "time"}
PILOT_LOGIC = {"translations", "module", "safetyRequired", "urgentCodes", "discussCodes"}


def equal(at, actual, expected):
    if actual != expected:
        raise ValueError(f"{at}: differs from frozen v16")


def verify(groups, originals):
    for group in groups:
        key = group["id"]
        expected = sorted(
            ((section, e) for section, e in originals
             if (e["order"] < 20 if key == "opening" else
                 section == int(key) and e["order"] >= 20)),
            key=lambda pair: pair[1]["order"])
        equal(f"{key}/question IDs and sequence", [q["id"] for q in group["questions"]],
              [e["lv"]["id"] for _, e in expected])
        for q, (section, e) in zip(group["questions"], expected):
            at = f"{key}/{q['id']}"
            lv = e["lv"]
            logic = {k:v for k,v in lv.items() if k not in TEXT}
            logic.update(order=e["order"], originModule=section, choiceCodes=list(lv["choices"]))
            equal(at+"/logic", {k:v for k,v in q.items() if k not in PILOT_LOGIC}, logic)
            for lang in ("lv", "en", "ru"):
                t = q["translations"][lang]
                for field in TEXT:
                    equal(f"{at}/{lang}/{field}", t.get(field), e[lang].get(field))
    return sum(len(g["questions"]) for g in groups)


if __name__ == "__main__":
    originals = []
    for path in sorted((ROOT/"src/modules").glob("182_MODULE_*_v16.json")):
        source = json.loads(path.read_text(encoding="utf-8"))
        originals.extend((source["section"], e) for e in source["entries"])
    groups = build_bundle()["groups"]
    count = verify(groups, originals)
    # Damage only the in-memory bundle, after the clean comparison passes.
    q = next(q for g in groups for q in g["questions"] if q["id"]=="M02_01")
    choices = q["translations"]["en"]["choices"]
    choices["B"], choices["C"] = choices["C"], choices["B"]
    try:
        verify(groups, originals)
    except ValueError as error:
        if str(error) != "02/M02_01/en/choices: differs from frozen v16":
            raise
    else:
        raise AssertionError("The deliberately swapped English labels escaped detection")
    print(f"PASS: {count} questions matched frozen v16 in three languages; swapped labels rejected.")
