# M06 Responsibilities Context Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans task-by-task.

**Goal:** Add M06_25 in every active language with explicit report review priority.
**Architecture:** One supplemental JSON catalog owns the new item and its editorial metadata. A narrow builder hook inserts it after M06_24 and extends only its named report family; unchanged runtime and recovery format.
**Tech Stack:** JSON, Python builder, existing JavaScript runtime, Playwright.
**Spec:** docs/superpowers/specs/2026-11-16-m06-responsibilities-design.md

## Global Constraints
Preserve 712 frozen records, current M46 additions, old IDs/codes/conditions, mental-pilot-recovery-v1 and offline/no-transmission behavior. M06_25 codes A–F: more/less/same/not-applicable/unsure/refusal. A priority4, all others3; no new emergency trigger. LV/EN/RU/UK aligned.

## Review Focus
- More likely is hypothetical, never substituted for current intent or automatically treated as emergency.
- Less likely, no change and nonapplicable must not become a reassuring clinical rating.
- Old progress import and each new response must survive round trips, reports and locale switching.
- New item must remain visible after No to current suicidal thoughts; skip remains available.
- Rollback must isolate the addition; newer backups containing its ID require a deliberate compatibility decision.

### Task 1: Catalog, integration and priority
Files: src/questionnaire/m06-responsibility-context.json; tools/build_questionnaire.py; tests/full_bank/test_m06_responsibility_context.py; existing count/contract tests.
Interface: apply_m06_responsibility_context(bundle, priority) adds one question to existing group and its priority/family metadata; touches no other records.
- [ ] Write build regression asserting ID/module/order/locales/codes/priority, unchanged frozen/old items, rejected malformed metadata and isolated disabled-hook rollback; observe missing-item failure.
- [ ] Implement validated catalog/hook with M06_25 unique order715 and code statuses; assert complete active locales before applying only enabled packs.
- [ ] Run focused build, translation, report-priority and source checks; expect PASS.

### Task 2: Runtime and review
Files: tests/full_bank/test_runtime_m06_context.py; tests/full_bank/test_report_priority.js; active UI notes.
- [ ] Add real browser old-progress import, No-to-current-thoughts reachability, all A–F choices/locales, skip/back, response-conserving clinician PDF/recovery, existing urgent triggers and no HTTP request checks.
- [ ] Run regression against missing item first, then real implementation; verify all locales at 320/390px and inspect renders.
- [ ] Add bounded report-priority regression and full-suite run; get fresh independent review and fix important findings with regressions.

### Task 3: Release and publication
Files: version config/manifest, README/landing/active docs, checkpoint/changelog, current package and delivery evidence.
- [ ] Bump to v0.2.16 and716 active questions; align user notes/counts, leave frozen count712 intact. Commit tested source with checkpoint.
- [ ] Build from clean source, verify HTML/PDF/ZIP, render PDF and archive v0.2.15. Require three exact-head CI checks and checked PR merge.
- [ ] Replace same Drive IDs, download both and verify exact bytes/permissions/folder. Merge distribution metadata, observe Pages and verify live bytes, M06 question, priorities/progress/report flows.
- [ ] Record final live evidence/checkpoint and ensure README/landing/Drive all current. Keep human reviews pending.

Release ruling: keep landing counts aligned with verified Drive distribution while package16 is staged. Move716 public counts into the delivery commit alongside verified distribution metadata. Regression observed staged716/verified715 failure before fixing its expectation; deployment guard remains strict.
