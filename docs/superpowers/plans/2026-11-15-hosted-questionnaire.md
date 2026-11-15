# Hosted Questionnaire Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Let a visitor launch the existing questionnaire from the landing page while preserving the working offline download.

**Architecture:** Extend the current Pages staging builder to copy exactly the verified package HTML to `questionnaire/index.html`, add localized open actions and two-mode instructions, retain one Drive-folder download. Deploy only an allowlisted site. The deployment builder checks package hash/size and recorded Drive version/files. Future automatic publication runs after Drive-sync evidence changes or approved website edits; questionnaire source/package merges alone do not publish ahead of Drive verification.

**Tech Stack:** Existing Python static builder, HTML/CSS, GitHub Pages Actions, shared self-contained HTML, Playwright.

**Spec:** Approved request: online launch plus existing Drive download use the same questionnaire/version, no separate maintenance; test both modes. Exact scope/constraints below are the written design.

## Global constraints

- Reuse exact v0.2.14 HTML bytes; no questionnaire/app/translation/guide changes or version bump. The app still starts in Latvian and retains its existing language selector.
- Localize public launch/download instructions in EN/LV/RU, preserve search metadata/canonicals and the multilanguage wording policy. Leave all answer processing local; hosting receives ordinary page requests, never questionnaire answers automatically.
- One distinct online launch plus one stable Drive-folder download per landing page. No raw GitHub or separate PDF download actions.
- Keep manual progress save/import explicit for both modes; no account, server storage, analytics, new dependencies or service worker.
- Staged output: only three landing HTML pages, hosted questionnaire HTML and sitemap. Validate exact HTML name/hash/size; reject unsafe/missing/mismatched package records. Deployment must reject a package not matching verified Drive distribution.
- Preserve existing original sources, backups, answer codes/conditions, clinician output, report ordering and sharing privacy. No outreach or personal messages.

## Review focus

- Wrong/stale/tampered package or mismatched Drive version must block publication while ordinary preview/test builds still support unshipped packages.
- Every localized open link resolves under a GitHub project base path; one unchanged Drive-folder link remains.
- Hosted and file modes import each other’s progress; provided No/uncertain/refusal/medicine notes survive into clinician output.
- After initial hosted load, answering/saving/reporting makes no HTTP requests; reloading needs manual recovery, as before.
- Landing/app at 320/390px and desktop remain usable; download/clipboard/print behavior is verified without claiming physical-device tests.

### Task 1: Publication and user flow

**Files:** `tools/build_discovery.py`; `docs/discovery-preview/{index,lv,ru}.html`; `tests/discovery/test_build.py`; new `tests/full_bank/test_runtime_hosted.py`; publication/check workflows; README and focused release/architecture rules.

**Interfaces:** Existing `build(base_url, output)` remains valid; optional publication guard verifies current `MH_Public_version/manifest.json` against project manifest Drive records. Reuse current app exactly.

- [x] Add failing tests for five-file staging, identical app bytes, localized links and invalid/stale/unsafe package rejection.
- [x] Implement narrow artifact copy/guard and localized two-mode actions/instructions/privacy.
- [x] Add HTTPS-hosted synthetic flow covering actual start/answer, locales, recoveries between modes, report/PDF, share payload and no answer requests.
- [ ] Run focused publication/browser checks and existing package/source integrity; record/push checkpoint; one independent review and fixes as needed.

### Task 2: Checked launch and durable evidence

**Files:** `.github/workflows/discovery-pages.yml`, delivery evidence, current checkpoint/changelog/TD. No reviewer package or Drive-byte change.

**Interfaces:** Consume checked main and already verified Drive package; publish stable `/questionnaire/` and byte-readback of every locale/app/sitemap.

- [ ] Push checked PR; require exact-head CI and merge without changing the product tree.
- [ ] Run/observe Pages deployment from checked main; verify actual HTTPS content type, links and identical app bytes; smoke-test live flow and compare Drive readback.
- [ ] Record exact commits/run IDs/hashes and test limits, preserve old checkpoint, remove completed task after verification and merge final docs.

## Resume ledger

- Start: clean main `65454bf`; no product edits yet. TD/changelog/planning checkpoint will be pushed before implementation. Live landing pages still download-only, v0.2.14 downloadable pair is unchanged.
- Execution: dedicated branch in the current checkout; do the small tasks inline and request one independent review. Use this checklist plus changelog and pushed commits to resume; do not restart completed work.

- Source checkpoint: publication regressions pass (5 tests), package/source integrity passes, and real local HTTPS + offline-memory integration passes. Initial browser harness import confirmation corrected; app bytes remain identical. Review and live deployment remain pending.

- Review correction: ordinary CI must support unshipped packages; positive parity fixture is synthetic, preview staging does not enable deployment-only verification. Reproduced RED fixture and GREEN publication suite. Actual current Drive HTML downloaded equal to package. Final exact-head CI and deployment remain pending; PR #56.

- CI correction: initial final-head full suite had 40 pass/1 fail for RU 320px heading overflow. Reproduced using wider system font; font regression RED then GREEN after heading wrapping. Focused HTTPS/offline flow and publication tests pass. Require fresh final-head CI before publication.
