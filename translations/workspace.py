"""Export a small Latvian source batch and check isolated translation files."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parent.parent
MODULES = tuple(f"{number:02d}" for number in range(1, 49))
QUESTION_COUNT = 712


def unique_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_keys)


def load_source(module):
    path = ROOT / "src" / "modules" / f"182_MODULE_{module}_LV_EN_RU_v16.json"
    bundle = read_json(path)
    questions = {}
    for entry in bundle["entries"]:
        lv = entry["lv"]
        questions[lv["id"]] = {key: lv[key] for key in ("title", "time", "help", "choices") if key in lv}
    if len(questions) != bundle["count"]:
        raise ValueError(f"Unexpected source question count in module {module}")
    return questions


def source_digest(questions):
    text = json.dumps(questions, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def check_text(source, translation, field):
    if not isinstance(translation, str) or bool(source.strip()) != bool(translation.strip()):
        raise ValueError(f"{field}: expected a translation for each nonempty source field")
    if not source.strip() and translation != source:
        raise ValueError(f"{field}: preserve the empty source field")


def check_pack(source, pack, *, complete=False):
    if not isinstance(pack, dict) or pack.keys() != {"source_sha256", "questions"}:
        raise ValueError("Expected source_sha256 and questions")
    if pack["source_sha256"] != source_digest(source):
        raise ValueError("Latvian source hash differs. Compare the source before updating translations.")
    translations = pack["questions"]
    if not isinstance(translations, dict):
        raise ValueError("questions must be an object keyed by question ID")
    extra = translations.keys() - source.keys()
    missing = source.keys() - translations.keys()
    if extra:
        raise ValueError("Unknown question IDs: " + ", ".join(sorted(extra)))
    if complete and missing:
        raise ValueError("Missing question IDs: " + ", ".join(sorted(missing)))
    for qid, translation in translations.items():
        original = source[qid]
        if not isinstance(translation, dict) or translation.keys() != original.keys():
            raise ValueError(f"{qid}: translation fields must match the source")
        choices = translation["choices"]
        if not isinstance(choices, dict) or list(choices) != list(original["choices"]):
            raise ValueError(f"{qid}: answer codes and their order must match the source")
        for code, text in choices.items():
            check_text(original["choices"][code], text, f"{qid}.choices.{code}")
        for key in original.keys() - {"choices"}:
            check_text(original[key], translation[key], f"{qid}.{key}")
    return len(translations)


def check_workspace(locale, module, complete):
    folder = ROOT / "translations" / locale
    if not folder.is_dir():
        raise ValueError(f"No workspace for {locale}")
    paths = {path.stem: path for path in (folder / "questions").glob("*.json")}
    if paths.keys() - set(MODULES):
        raise ValueError("Unknown translation module files: " + ", ".join(sorted(paths.keys() - set(MODULES))))
    selected = (module,) if module else MODULES
    total = 0
    missing = []
    for number in selected:
        if number not in paths:
            missing.append(number)
            if module:
                print(f"Module {number}: 0/{len(load_source(number))} questions. No translation file yet.")
            continue
        source = load_source(number)
        try:
            count = check_pack(source, read_json(paths[number]), complete=complete)
        except ValueError as error:
            raise ValueError(f"Module {number}: {error}") from error
        print(f"Module {number}: {count}/{len(source)} questions passed structural checks.")
        total += count
    if not module:
        print(f"{locale}: {total}/{QUESTION_COUNT} questions passed structural checks.")
    if complete and missing:
        raise ValueError("Missing translation modules: " + ", ".join(missing))
    if complete and not module and total != QUESTION_COUNT:
        raise ValueError(f"Expected {QUESTION_COUNT} questions, found {total}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--locale", default="uk", help="workspace folder name, default uk")
    commands = parser.add_subparsers(dest="command", required=True)
    export = commands.add_parser("source", help="print one batch of Latvian source as JSON")
    export.add_argument("module", choices=MODULES)
    export.add_argument("--start", type=int, default=1, help="one-based position in the module")
    export.add_argument("--limit", type=int, default=12)
    check = commands.add_parser("check", help="check one module or all saved modules")
    check.add_argument("module", nargs="?", choices=MODULES)
    check.add_argument("--complete", action="store_true", help="require every question in the selected scope")
    args = parser.parse_args()

    try:
        if args.command == "source":
            source = load_source(args.module)
            if not 1 <= args.start <= len(source) or args.limit < 1:
                raise ValueError(f"Expected a start between 1 and {len(source)} and a positive limit")
            start = args.start - 1
            batch = dict(list(source.items())[start:start + args.limit])
            print(json.dumps({"source_sha256": source_digest(source), "questions": batch}, ensure_ascii=False, indent=2))
        else:
            if not re.fullmatch(r"[a-z]{2,3}(?:-[A-Za-z0-9]{2,8})*", args.locale):
                raise ValueError("Invalid locale code")
            check_workspace(args.locale, args.module, args.complete)
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
