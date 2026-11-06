#!/usr/bin/env python3
"""Build one deterministic offline HTML prototype from separate module logic and LV/EN/RU text.

Usage: python tools/build_pilot.py
       python tools/build_pilot.py --output /tmp/pilot.html

To add section 21: create src/pilot/modules/21/{logic,lv,en,ru}.json and
add a registry entry. No edits to existing modules, engine, or translator files.
"""
import argparse
import hashlib
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "src" / "pilot"
LANGS = ("lv", "en", "ru")


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def build_bundle():
    registry = read_json(SOURCE / "modules" / "registry.json")
    ui = {}
    for lang in LANGS:
        catalog = read_json(SOURCE / "i18n" / ("ui." + lang + ".json"))
        assert catalog["lang"] == lang
        ui[lang] = catalog["strings"]
    groups = []
    group_ids = set()
    ids, orders = set(), set()
    for group in registry["groups"]:
        key = group["id"]
        if not isinstance(key, str) or not key.isalnum() or key in group_ids:
            raise ValueError(f"Invalid or duplicate module ID: {key}")
        group_ids.add(key)
        folder = SOURCE / "modules" / key
        logic = read_json(folder / "logic.json")
        if logic["group"] != key:
            raise ValueError("Wrong module ID in " + key)
        local = {lang: read_json(folder / (lang + ".json")) for lang in LANGS}
        questions = []
        for q in logic["questions"]:
            qid = q["id"]
            if qid in ids or q["order"] in orders:
                raise ValueError("Duplicate ID/order: " + qid)
            ids.add(qid)
            orders.add(q["order"])
            clone = dict(q)
            clone["module"] = key
            clone["translations"] = {}
            for lang in LANGS:
                localized = local[lang]
                if localized["module"] != key or localized["lang"] != lang:
                    raise ValueError("Wrong locale module/language " + key + " " + lang)
                t = localized["questions"].get(qid)
                if not isinstance(t, dict) or not t.get("title"):
                    raise ValueError("Missing title " + qid + " / " + lang)
                if set(t["choices"]) != set(q["choiceCodes"]):
                    raise ValueError("Incorrect answer codes " + qid + " / " + lang)
                clone["translations"][lang] = t
            questions.append(clone)
        for lang in LANGS:
            if set(local[lang]["questions"]) != {q["id"] for q in questions}:
                raise ValueError("Missing/extra translation IDs: " + key + "/" + lang)
        titles = {lang: local[lang]["title"] for lang in LANGS}
        if not all(isinstance(t, str) and t.strip() for t in titles.values()):
            raise ValueError("Missing section title: " + key)
        if len(questions) != group["question_count"]:
            raise ValueError("Question count mismatch: " + key)
        groups.append({"id": key, "titles": titles,
                       "concerns": {lang: local[lang].get("concern", titles[lang]) for lang in LANGS}, "required": bool(group["required"]), "questions": questions})
    by_id = {q["id"]: q for group in groups for q in group["questions"]}
    for group in groups:
        for q in group["questions"]:
            context = q.get("context")
            if context and context.get("id") not in ids:
                raise ValueError("Unresolved condition " + q["id"])
            if context and by_id[context["id"]]["order"] >= q["order"]:
                raise ValueError("Condition must reference an earlier question: " + q["id"])
    return {"schema": "offline-questionnaire-pilot-v1", "version": registry["app_version"],
            "baseline": registry["baseline"], "ui": ui, "groups": groups,
            "presentation": read_json(SOURCE / "reports" / "presentation.json"),
            "release_status": {"lv": "PROTOTYPE", "en": "DRAFT_NOT_RELEASED", "ru": "DRAFT_NOT_RELEASED"}}


def make_html():
    data = build_bundle()
    style = (SOURCE / "core" / "styles.css").read_text(encoding="utf-8")
    reports = (SOURCE / "reports" / "reports.js").read_text(encoding="utf-8")
    app = (SOURCE / "core" / "app.js").read_text(encoding="utf-8")
    data_json = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    # Never allow JSON values to prematurely terminate their script tag.
    data_json = data_json.replace("<", "\\u003c").replace(">", "\\u003e")
    return ('<!doctype html><html lang="lv"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1">'
            '<meta http-equiv="Content-Security-Policy" content="default-src &#39;none&#39;; '
            'script-src &#39;unsafe-inline&#39;; style-src &#39;unsafe-inline&#39;; '
            'img-src data:; connect-src &#39;none&#39;; form-action &#39;none&#39;; '
            'base-uri &#39;none&#39;; object-src &#39;none&#39;">'
            '<meta name="project-status" content="TEST ONLY — not clinically validated">'
            '<title>' + html.escape(data["ui"]["lv"]["project"]) + '</title>'
            '<style>' + style + '</style></head><body><div id="app"></div>'
            '<script id="pilot-data" type="application/json">' + data_json + '</script>'
            '<script>' + reports + '</script><script>' + app + '</script>'
            '</body></html>\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "dist" / "PILOT_offline_LV_EN_RU_v0.1_NOT_RELEASED.html")
    args = parser.parse_args()
    output = make_html().encode("utf-8")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(output)
    print("PILOT BUILT:", args.output)
    print("SHA256:", hashlib.sha256(output).hexdigest())
    print("Languages:", ", ".join(LANGS))
    print("PROTOTYPE ONLY: browser, translation, and clinical approval NOT implied.")


if __name__ == "__main__":
    main()

