#!/usr/bin/env python3
"""Build the complete offline questionnaire from separate app and question sources.

Usage: python tools/build_questionnaire.py
       python tools/build_questionnaire.py --output /tmp/questionnaire.html
"""
import argparse
import hashlib
import html
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "src" / "app"
QUESTIONNAIRE = ROOT / "src" / "questionnaire"
LANGS = ("lv", "en", "ru")


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_app_sources():
    """Assemble the app's explicit ordered source list without reading question data."""
    manifest = read_json(APP / "build.json")
    if manifest.get("schema") != "questionnaire-app-build-v1":
        raise ValueError("Invalid application build manifest")

    def read_sources(key):
        paths = manifest.get(key)
        if not isinstance(paths, list) or not paths or len(paths) != len(set(paths)):
            raise ValueError("Application manifest must list unique " + key)
        sources = []
        for relative_path in paths:
            if not isinstance(relative_path, str) or not relative_path.strip():
                raise ValueError("Invalid application source path in " + key)
            path = (APP / relative_path).resolve()
            if not path.is_relative_to(APP.resolve()) or not path.is_file():
                raise ValueError("Application source is missing or outside src/app: " + relative_path)
            sources.append(path.read_text(encoding="utf-8"))
        return "".join(sources)

    return read_sources("styles"), read_sources("scripts")


def load_module_titles():
    """Load exact frozen section headings for the full-bank module selector."""
    result = {}
    expected = [f"{number:02d}" for number in range(1, 49)]
    for lang in LANGS:
        catalog = read_json(QUESTIONNAIRE / "i18n" / ("module-titles." + lang + ".json"))
        titles = catalog.get("titles")
        if (catalog.get("schema") != "frozen-module-titles-v1" or catalog.get("lang") != lang
                or not isinstance(titles, dict) or list(titles) != expected
                or not all(isinstance(title, str) and title.strip() for title in titles.values())):
            raise ValueError("Invalid full-bank module titles: " + lang)
        result[lang] = titles
    return result


def adapt_source_entry(entry):
    """Map one frozen LV/EN/RU module entry to the shared engine's question shape."""
    lv = entry["lv"]
    section = lv["section"]
    q = {
        "id": lv["id"],
        "order": entry["order"],
        "module": str(section).zfill(2),
        "sourceModule": str(section).zfill(2),
        "originModule": section,
        "section": section,
        "profile": lv["profile"],
        "multi": lv["multi"],
        "context": lv["context"],
        "choiceCodes": list(lv["choices"]),
        "exclusive": lv["exclusive"],
        "incompatible": lv["incompatible"],
        "answerStatus": lv["answerStatus"],
        "type": lv.get("type", "choice"),
        "translations": {},
    }
    if "maxChoices" in lv:
        q["maxChoices"] = lv["maxChoices"]
    if "help" in lv:
        q["help"] = lv["help"]
    for lang in LANGS:
        source = lv if lang == "lv" else entry[lang]
        translation = {
            "title": source["title"],
            "time": source["time"],
            "choices": source["choices"],
        }
        if "help" in source:
            translation["help"] = source["help"]
        q["translations"][lang] = translation
    return q


def build_source_groups():
    """Build optional engine groups directly from the immutable 48-module bank."""
    titles = load_module_titles()
    files = sorted((ROOT / "src" / "modules").glob("182_MODULE_*_LV_EN_RU_v16.json"))
    if len(files) != 48:
        raise ValueError(f"Expected 48 original module files; found {len(files)}")
    groups = {}
    ids, orders = set(), set()
    for expected_section, path in enumerate(files, 1):
        module = read_json(path)
        section = module.get("section")
        if (module.get("schema") != "question-module-bundle-v1" or section != expected_section
                or module.get("count") != len(module.get("entries", []))):
            raise ValueError("Invalid source module: " + path.name)
        for lang in LANGS:
            if module["published_status"].get(lang) not in ("v16", "draft-not-reviewed"):
                raise ValueError("Unknown source language status: " + lang)
        for entry in module["entries"]:
            q = adapt_source_entry(entry)
            if q["id"] in ids or q["order"] in orders:
                raise ValueError("Duplicate full-bank ID/order: " + q["id"])
            ids.add(q["id"]);orders.add(q["order"])
            key = q["module"]
            if key not in groups:
                group_titles = {lang: titles[lang][key] for lang in LANGS}
                groups[key] = {"id": key, "titles": group_titles, "concerns": group_titles,
                               "required": False, "questions": []}
            groups[key]["questions"].append(q)
    by_id = {q["id"]: q for group in groups.values() for q in group["questions"]}
    for group in groups.values():
        for q in group["questions"]:
            context = q.get("context")
            if context and (context["id"] not in by_id or by_id[context["id"]]["order"] >= q["order"]):
                raise ValueError("Invalid source condition: " + q["id"])
    expected_groups = {f"{number:02d}" for number in range(1, 49)}
    if set(groups) != expected_groups or len(ids) != 712:
        raise ValueError(f"Full-bank count/group mismatch: {len(groups)} groups, {len(ids)} questions")
    return [groups[key] for key in sorted(groups)]


def contains_weight_key(value):
    if isinstance(value, dict):
        return any("weight" in key.lower() or contains_weight_key(item)
                   for key, item in value.items())
    if isinstance(value, list):
        return any(contains_weight_key(item) for item in value)
    return False


def check_catalog(reference, translation, field):
    if type(reference) is not type(translation):
        raise ValueError(f"{field}: translation type differs")
    if isinstance(reference, dict):
        if reference.keys() != translation.keys():
            raise ValueError(f"{field}: translation keys differ")
        for key in reference:
            check_catalog(reference[key], translation[key], f"{field}.{key}")
    elif isinstance(reference, list):
        if len(reference) != len(translation):
            raise ValueError(f"{field}: translation list length differs")
        for index, (source, translated) in enumerate(zip(reference, translation)):
            check_catalog(source, translated, f"{field}[{index}]")
    elif isinstance(reference, str):
        placeholders = r"\{[A-Za-z_][A-Za-z_0-9]*\}"
        if (bool(reference.strip()) != bool(translation.strip())
                or Counter(re.findall(placeholders, reference)) != Counter(re.findall(placeholders, translation))):
            raise ValueError(f"{field}: translation text or placeholders differ")


def apply_translation_packs(bundle, packs):
    """Add validated wording only. The source bank still owns question behavior."""
    # The script is also launched directly from tools/, where the repo is not on sys.path.
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from translations import workspace

    reference_ui = bundle["ui"]["lv"]
    question_rules = bundle["presentation"]["questions"]
    reference_sections = {group["id"]: group["titles"]["lv"] for group in bundle["groups"]}
    reference_reports = {qid: rule["labels"]["lv"] for qid, rule in question_rules.items() if "labels" in rule}
    for locale in packs:
        folder = ROOT / "translations" / locale

        def catalog(filename, key, reference, schema=None):
            document = workspace.read_json(folder / filename)
            if (not isinstance(document, dict) or document.get("lang") != locale
                    or (schema and document.get("schema") != schema)):
                raise ValueError(f"{locale}/{filename}: invalid catalog header")
            translated = document.get(key)
            check_catalog(reference, translated, f"{locale}/{filename}")
            return translated

        ui = catalog("ui.json", "strings", {k: v for k, v in reference_ui.items() if k != "medicine"},
                     "questionnaire-ui-locale-v1")
        ui["medicine"] = catalog("medicine.json", "strings", reference_ui["medicine"], "medicine-list-ui-v1")
        sections = catalog("section-titles.json", "titles", reference_sections)
        labels = catalog("report-labels.json", "labels", reference_reports)
        question_files = {path.stem for path in (folder / "questions").glob("*.json")}
        unexpected = question_files - set(workspace.MODULES)
        if unexpected:
            raise ValueError(f"{locale}: unknown translation module files: {', '.join(sorted(unexpected))}")
        by_id = {}
        for module in workspace.MODULES:
            path = folder / "questions" / f"{module}.json"
            try:
                pack = workspace.read_json(path)
                workspace.check_pack(workspace.load_source(module), pack, complete=True)
            except (OSError, ValueError) as error:
                raise ValueError(f"{locale}/questions/{module}.json: {error}") from error
            by_id.update(pack["questions"])

        bundle["ui"][locale] = ui
        for group in bundle["groups"]:
            # Concerns and titles share the same dictionary in the full-bank bundle.
            group["titles"][locale] = sections[group["id"]]
            for question in group["questions"]:
                question["translations"][locale] = by_id[question["id"]]
        for qid, label in labels.items():
            question_rules[qid]["labels"][locale] = label
        bundle["release_status"][locale] = "DRAFT_NOT_RELEASED"
    bundle["languageNames"] = packs


def build_bundle():
    """Assemble the complete 48-section bank without copying question sources."""
    config = read_json(QUESTIONNAIRE / "build.json")
    if config.get("schema") != "questionnaire-build-v1":
        raise ValueError("Invalid questionnaire build configuration")
    packs = config.get("translationPacks", {})
    if not isinstance(packs, dict) or any(
        locale in LANGS or not re.fullmatch(r"[a-z]{2,3}(?:-[A-Za-z0-9]{2,8})*", locale)
        or not isinstance(name, str) or not name.strip()
        for locale, name in packs.items()
    ):
        raise ValueError("Invalid translationPacks language registry")
    ui = {}
    for lang in LANGS:
        catalog = read_json(APP / "i18n" / ("ui." + lang + ".json"))
        if catalog.get("lang") != lang:
            raise ValueError("Wrong interface locale: " + lang)
        ui[lang] = catalog["strings"]
        medicine = read_json(APP / "i18n" / ("medicine." + lang + ".json"))
        if medicine.get("schema") != "medicine-list-ui-v1" or medicine.get("lang") != lang:
            raise ValueError("Wrong medicine-list locale: " + lang)
        ui[lang]["medicine"] = medicine["strings"]

    source_groups = build_source_groups()
    by_id = {q["id"]: q for group in source_groups for q in group["questions"]}
    layout = read_json(QUESTIONNAIRE / "layout.json")
    presentation = read_json(QUESTIONNAIRE / "presentation.json")
    if (layout.get("schema") != "questionnaire-layout-v1"
            or presentation.get("schema") != "questionnaire-presentation-v1"):
        raise ValueError("Invalid questionnaire presentation configuration")
    if contains_weight_key(presentation):
        raise ValueError("Weight metadata is no longer supported")
    contact = presentation.get("feedbackContactEmail", "")
    if not isinstance(contact, str) or not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", contact):
        raise ValueError("A valid project-feedback contact email is required")
    for qid, rule in presentation["questions"].items():
        if qid not in by_id:
            raise ValueError("Presentation references an unknown question: " + qid)
        q = by_id[qid]
        if "allowAllChoices" in rule and (rule["allowAllChoices"] is not True or not q.get("maxChoices")):
            raise ValueError("Expected a capped question for allowAllChoices: " + qid)
        if "labels" in rule and set(rule["labels"]) != set(LANGS):
            raise ValueError("Missing report label language: " + qid)
        if any(code not in q["choiceCodes"] or level not in ("support", "emergency")
               for code, level in rule.get("support", {}).items()):
            raise ValueError("Invalid support trigger: " + qid)
    for qid, codes in presentation.get("boldAnswers", {}).items():
        if qid not in by_id or not isinstance(codes, list) or not codes:
            raise ValueError("Invalid bold-answer question: " + qid)
        if len(set(codes)) != len(codes) or any(code not in by_id[qid]["choiceCodes"] for code in codes):
            raise ValueError("Invalid bold-answer code: " + qid)

    module_ids = {f"{number:02d}" for number in range(1, 49)}
    full_order = layout.get("full_order", [])
    section_groups = layout.get("section_groups", [])
    section_ids = [group.get("id") for group in section_groups if isinstance(group, dict)]
    topic_order = presentation.get("topicOrder", [])
    if (len(full_order) != 48 or len(set(full_order)) != 48 or set(full_order) != module_ids
            or len(section_groups) == 0 or len(section_ids) != len(section_groups)
            or len(set(section_ids)) != len(section_ids)
            or len(topic_order) != len(section_ids) or len(set(topic_order)) != len(topic_order)
            or set(topic_order) != set(section_ids)):
        raise ValueError("Source-module order and user-section/report order must be complete and unique")
    source_to_section = {}
    for section_group in section_groups:
        if set(section_group.get("title", {})) != set(LANGS):
            raise ValueError("Each user-facing section requires a title in all languages")
        modules = section_group.get("source_modules")
        if not isinstance(modules, list) or not modules:
            raise ValueError("Each user-facing section must list its source modules")
        for module_id in modules:
            if module_id not in module_ids or module_id in source_to_section:
                raise ValueError("User-facing section mapping has an unknown or duplicate source module")
            source_to_section[module_id] = section_group["id"]
    if set(source_to_section) != module_ids:
        raise ValueError("Every original source module must belong to exactly one user-facing section")
    source_by_group = {group["id"]: group for group in source_groups}
    ordered_groups = []
    for section_group in section_groups:
        section_id = section_group["id"]
        questions = []
        for module_id in full_order:
            if source_to_section[module_id] != section_id:
                continue
            for source_question in source_by_group[module_id]["questions"]:
                question = dict(source_question)
                question["sourceModule"] = module_id
                question["module"] = section_id
                if presentation["questions"].get(question["id"], {}).get("allowAllChoices"):
                    del question["maxChoices"]
                questions.append(question)
        if len(questions) < 30:
            raise ValueError("Each user-facing section must contain at least 30 source questions: " + section_id)
        ordered_groups.append({
            "id": section_id,
            "titles": section_group["title"],
            "concerns": section_group["title"],
            "required": False,
            "questionCount": len(questions),
            "sourceModules": section_group["source_modules"],
            "questions": questions,
        })
    groups = ordered_groups
    by_id = {q["id"]: q for group in groups for q in group["questions"]}
    positions = {q["id"]: index for index, q in enumerate(
        question for group in groups for question in group["questions"])}
    for qid, q in by_id.items():
        if q.get("context") and positions[q["context"]["id"]] >= positions[qid]:
            raise ValueError("Navigation must keep condition parent before follow-up: " + qid)

    bundle = {
        "schema": "offline-questionnaire-full-bank-v1",
        "version": config["version"],
        "layout_version": layout["version"],
        "source_module_to_section": source_to_section,
        "previous_layout_versions": ["optional-topics-v1-full-bank"],
        "legacy_opening_groups": [],
        "baseline": config["baseline"],
        "ui": ui,
        "groups": groups,
        "presentation": presentation,
        "release_status": {"lv": "PROTOTYPE", "en": "DRAFT_NOT_RELEASED", "ru": "DRAFT_NOT_RELEASED"},
    }
    if packs:
        apply_translation_packs(bundle, packs)
    return bundle


def make_html(data=None):
    data = build_bundle() if data is None else data
    style, scripts = load_app_sources()
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
            '<script id="questionnaire-data" type="application/json">' + data_json + '</script>'
            '<script>' + scripts + '</script>'
            '</body></html>\n')


def main():
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--output", type=Path, default=None)
    mode.add_argument("--translation-pack-test", action="store_true",
                      help="write a TEST file in this checkout's dedicated dist folder")
    args = parser.parse_args()
    data = build_bundle()
    locale_suffix = "_".join(data["ui"]).upper()
    output_path = args.output or (ROOT / "dist" / f"QUESTIONNAIRE_{locale_suffix}_NOT_RELEASED.html")
    if args.translation_pack_test:
        output_path = ROOT / "dist" / "translation-pack-test" / "QUESTIONNAIRE_TRANSLATION_PACK_TEST.html"
        if output_path.resolve() != output_path:
            parser.error("Test output must stay inside this checkout and cannot use redirected paths")
    output = make_html(data).encode("utf-8")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Test mode never overwrites an existing file, including a link to another artifact.
    with output_path.open("xb" if args.translation_pack_test else "wb") as handle:
        handle.write(output)
    print("COMPLETE QUESTIONNAIRE BUILT:", output_path)
    print("SHA256:", hashlib.sha256(output).hexdigest())
    print("Languages:", ", ".join(data["ui"]))
    print("PROTOTYPE ONLY: browser, translation, and clinical approval NOT implied.")


if __name__ == "__main__":
    main()

