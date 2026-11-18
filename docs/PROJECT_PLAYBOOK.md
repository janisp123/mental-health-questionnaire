# Project playbook — reusable verified lessons

This file holds evidence-based development lessons, not active tasks, personal conversations or completed-release records. Mandatory rules live in `AGENTS.md` and `docs/AGENT_PROTOCOL.md`.

## PB-01 — One canonical task path

**Observation (2026-11-18):** Two active projects used different TD filenames, causing agents to search for the right backlog.
**Prevention:** Use the project-local `docs/TD_LIST.md` in every repository and fetch latest remote `main` first.
**Verification:** `python tools/check_project_protocol.py` and GitHub PR checks.
**Confidence:** PROVEN for the observed naming problem; automated enforcement only checks structure.

## PB-02 — Verify cross-agent handoff

**Observation:** Local changes, PRs, merged source and published websites have different completion states.
**Prevention:** Record exact commit/PR, tests actually run, real blockers and one next action in `docs/WORK_CHECKPOINT.md`; confirm completion by remote readback.
**Verification:** Read the linked GitHub commit, CI and deployed artifact when relevant.
**Confidence:** PROVEN as a coordination safeguard.

Further entries should use: trigger → observed issue → preventive action → verification/evidence → confidence. Do not add unsupported speculation as fact.
