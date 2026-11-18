#!/usr/bin/env python3
"""Validate the shared agent-project file layout (stdlib only)."""
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
required = (
    "AGENTS.md",
    "docs/TD_LIST.md",
    "docs/WORK_CHECKPOINT.md",
    "docs/CHANGELOG.md",
    "docs/DECISIONS.md",
    "docs/PROJECT_PLAYBOOK.md",
    "docs/AGENT_PROTOCOL.md",
    "docs/NEW_PROJECT_SETUP.md",
    ".github/workflows/project-protocol.yml",
    ".github/pull_request_template.md",
)
errors = [f"Missing file: {p}" for p in required if not (root / p).is_file()]
agents = root / "AGENTS.md"
if agents.is_file():
    content = agents.read_text(encoding="utf-8")
    for token in ("Project protocol v1.0", "docs/TD_LIST.md", "chat", "cw", "codex"):
        if token not in content:
            errors.append(f"AGENTS.md missing: {token}")
    if "docs/TD.learn.md" in content or "docs/TD.question.md" in content:
        errors.append("AGENTS.md refers to a legacy TD path")
for p in ("docs/TD.learn.md", "docs/TD.question.md"):
    if (root / p).exists():
        errors.append(f"Legacy active task list exists: {p}")
td = root / "docs/TD_LIST.md"
if td.is_file() and not td.read_text(encoding="utf-8").lstrip().startswith("#"):
    errors.append("docs/TD_LIST.md needs a Markdown heading")
if errors:
    for issue in errors:
        print("FAIL:", issue, file=sys.stderr)
    sys.exit(1)
print("PASS: Shared agent protocol v1.0 file layout.")
