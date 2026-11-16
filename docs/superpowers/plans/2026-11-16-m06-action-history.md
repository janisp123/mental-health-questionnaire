# M06 Action History Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans task-by-task.

**Goal:** Integrate the approved seven-choice history question and conditional timing inside existing M06.
**Architecture:** Separate supplemental catalog and narrow builder hook, after M06_09. Reuse standard choice/context/report/recovery runtime unchanged.
**Tech Stack:** Python, JSON, existing JavaScript runtime and Playwright.
**Spec:** docs/superpowers/specs/2026-11-16-m06-action-history-design.md

## Global Constraints
No changes to 712 frozen records, earlier additions, old codes/conditions, recovery schema or current emergency mappings. M06_26 seven agreed choices A–G; M06_27 existing recency A–H with showValues A–D. All active languages and notes align. No automatic attempt classification or clinical score.

## Review Focus
- Earlier No answers must not hide the independent item.
- Timing must follow the same most-recent occasion and hide for No/unsure/refusal.
- Broad historical danger must not be labelled current suicidal intent or a suicide attempt.
- Branch changes must not leak hidden stale timing into clinician reports.
- Older exports must import, new responses/locale switching must round-trip; rollback must be deliberate.

### Task 1: Modular catalog and builder
Files: src/questionnaire/m06-action-history.json, tools/build_questionnaire.py, tests/full_bank/test_m06_action_history.py.
Interface: apply_m06_action_history(bundle, priority) inserts M06_26/27 after M06_09 and their explicit editorial rules without changing old data.
- [ ] Write missing-item/locale/code/priority/condition/rollback regression and observe RED.
- [ ] Implement fixed IDs/orders716/717, context, all locales, reused timing choices and independent report family via parent context.
- [ ] Run build/translation/source/priority checks; expect PASS.

### Task 2: Runtime and release source
Files: tests/full_bank/test_runtime_m06_action_history.py; existing count tests; UI notes/version/public docs.
- [ ] Verify RED with hook disabled; then all7 answers/all locales, each timing code, No gate, skip/back, current prompts, old/current progress and PDF/hidden-timing behavior.
- [ ] Render 320/390px and inspect all languages; fresh independent review; fix important findings with regressions.
- [ ] Bump v0.2.17/718, align README/active docs and all notes. Keep public landing count at verified716 until delivery. Commit source/checkpoint; full suite must pass.

### Task 3: Checked publication
- [ ] Build clean-source HTML/PDF/ZIP, verify and visually inspect guide, archive16. Checked PR and three exact-head CI checks before merge.
- [ ] Update same Drive IDs, read back exact bytes/metadata; merge distribution + landing718 together, observe Pages and live question/routing/report/progress/hash tests.
- [ ] Save final evidence/checkpoint and current pointers; retain five unrelated TD items and actual human-review limitations.
