#!/usr/bin/env python3
"""Run the maintained app, full-bank, translation and package checks."""
import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--load-mode", choices=("file", "memory"), default="file")
    parser.add_argument("--suite", choices=("all", "app", "non-browser"), default="all")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist/checks")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    folders = ["tests/app"] if args.suite == "app" else ["tests/app", "tests/full_bank", "tests/package"]
    checks = [path for folder in folders for path in sorted((ROOT / folder).glob("test_*")) if path.suffix in (".py", ".js")]
    if args.suite != "app":
        checks = [ROOT / "tools/verify_project_index.py", *checks, ROOT / "translations/test_workspace.py"]
    environment = dict(os.environ, QUESTIONNAIRE_LOAD_MODE=args.load_mode)
    results = []
    for path in checks:
        browser = path.name.startswith("test_runtime") or path.name in ("test_multilingual_qa.py", "test_layout_sweep.py")
        if args.suite == "non-browser" and browser:
            continue
        start = time.monotonic()
        result = subprocess.run(["node" if path.suffix == ".js" else sys.executable, str(path)],
                                cwd=ROOT, env=environment, capture_output=True, text=True)
        name = str(path.relative_to(ROOT))
        record = {"test": name, "exit": result.returncode, "seconds": round(time.monotonic()-start, 2),
                  "browser_load_mode": args.load_mode if browser else None}
        results.append(record)
        (args.output_dir / (name.replace("/", "_")+".log")).write_text(result.stdout+result.stderr, encoding="utf-8")
        print(("PASS" if result.returncode == 0 else "FAIL"), name, flush=True)
        if result.returncode:
            print((result.stdout+result.stderr)[-3000:], flush=True)
    for path in sorted((ROOT / "src/app").rglob("*.js")):
        result = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)
        if result.returncode:
            results.append({"test": str(path.relative_to(ROOT))+" syntax", "exit": result.returncode})
            print(result.stderr, flush=True)
    report = {"load_mode": args.load_mode, "suite": args.suite, "results": results,
              "passed": sum(item["exit"] == 0 for item in results), "failed": sum(item["exit"] != 0 for item in results)}
    (args.output_dir / "results.json").write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
    print(f"{report['passed']} passed; {report['failed']} failed. Browser load mode: {args.load_mode}.")
    if args.load_mode == "memory":
        print("Direct file:// opening remains unverified in this run.")
    return bool(report["failed"])


if __name__ == "__main__":
    raise SystemExit(main())
