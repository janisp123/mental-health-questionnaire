# Development changelog — mental-health-questionnaire

**Active task log:** This file on GitHub `develop`, effective 2026-11-05.
**Development edits:** GitHub only, after the relevant sources have been imported and verified.
**Google Drive:** distribution of Latvian public files only. Existing Drive archives are read-only source references following the completed migration; do not update its old changelog for routine work.

## 2026-11-06 · UX-SUPPORT-REPORT-REDESIGN · IN_PROGRESS

Scope: the existing 60-question pilot. Preserve original wording/codes and all pilot recovery records. Make all groups optional, redistribute opening items by original theme with personal details last, single-tap single-choice navigation, fixed Skip/Back, persistent gentle support, independent readable AI export, ascending answer-level report presentation priorities. Include previously requested bottom guide/version notes. Verify helpline facts, all three languages, and structural/fidelity/browser regressions. No release or frozen-source edits.

Stages: (1) inspect and pin design/source mappings plus failing acceptance tests; (2) navigation and recovery; (3) support and reports; (4) mobile-width offline regression, documents and checkpoint. Current: inspected AGENTS, changelog, manifest, file index and architecture. Next: fetch current sources and establish the test baseline.

## 2026-11-05 · SOURCE-FIDELITY-AND-SECTION-21 · TASK_DONE

Plan: verify active modules against frozen v16 by ID and exact codes, demonstrate rejection of swapped labels, inspect section 21 dependencies, import its three existing locales, verify in offline Chromium and checkpoint the artifact. Checkpoint: 41 active questions passed exact v16 logic and LV/EN/RU text comparisons locally. Deliberately swapping English labels B/C at M02_01 failed at the expected ID, locale and field. The gate runs in pilot CI. Section 21 has 19 questions (orders 387–405), no opening overlap or condition parents, and an incompatible A/E pair at M21_06 requiring generic runtime enforcement. Source gate committed at c7e0f37804c93013fb44bff9e776b205012e6594.

Imported real section 21 directly from v16 in its three languages. All 60 questions passed the structural and independent fidelity checks locally. Runtime now rejects incompatible selections on both save and restore. M21_15 retains the v16 immediate-help trigger B. Browser test exercises all 19 items, reports and recovery. Verified commit 5c851b0d1d7a273dabc7ed3563db68c42a449cd2 in [passing run 42067275015](https://github.com/janisp123/mental-health-questionnaire/actions/runs/42067275015). All three browser suites passed. The workflow uploaded artifact 13433203221. Built HTML SHA256 95019a68bda97bdc1f15d9d8e6dcb5d0f67bf6e76e6a24847d253369fbe24055 matches the local build. Next device check: open the 60-question pilot in Android Chrome and test downloading/restoring a backup.

## 2026-11-05 · PILOT-GENERIC-MODULE-AUDIT · TASK_DONE

**Goal:** audit the existing pilot against LV v16; remove module-specific engine/build assumptions; verify translation independence and additional-module registration; document remaining parity gaps and active source pointers.
**Plan:** inspect sources and successful CI evidence; checkpoint findings; make targeted generic changes; run structural and browser regressions; update architecture/index/manifest and verified status. Preserve original IDs, codes, conditions and recovery semantics. No release, Drive edits or main changes.
**Final verified checkpoint:** All pilot checks passed at b7a627b9e86ce97cf079fe272e5de59efe5b22b6 in [run 42064471277](https://github.com/janisp123/mental-health-questionnaire/actions/runs/42064471277). The third-module fixture, English-only edit, cross-build backup, safety review, conditional status, real mood multi-select, print PDF page count and copy payload all passed. The distributable test HTML is the workflow artifact. The production registry still enables only opening and section 02.

**Broader pilot status: PARTIAL.** See PILOT_ARCHITECTURE.md for scope. Next: check the artifact on Android Chrome (local opening, automatic recovery download, restore, clipboard and print), compare legacy v16 recovery and clinician-report requirements, then complete professional wording checks before any release. Full v16 backups cannot be loaded into this two-section pilot. EN/RU remain drafts.

**At registration:** the implementation had not yet been audited. See verified checkpoints below.
**Audit checkpoint:** Verified CI run 42057715895 passed on 231f537 (browser smoke + structure). Found fixed section counts and section-specific selector, reports and restore. LV v16 skip-section continues to the next eligible section. Pilot previously finished immediately.

**Implementation checkpoint:** Registry drives selection, progress, report section lines, skip continuation and recovery. Module locale files own their titles. Existing structural checks and JS syntax pass locally. Verified registry implementation on develop at 9ddc7d87681e4313ca7a497e685e65ad2a179b78. Added a disposable third-module + locale-edit Chromium test with cumulative tenth-save check and cross-build restore. CI run 42062287500 passed at f996d9ce739125d81bdf297f0311144ccdbb8c59, including the new browser regression.

**Next batch:** match opening safety prompts, flag incomplete safety coverage, validate restored choices, preserve status precedence, and print the full report. Structural checks and JavaScript syntax pass. Verified A4 PDF and opening safety behavior at b06f42271a2fd7905dbb6d08f69b6f1aa8f58eb7 in run 42062504929.

**Next batch:** verify optional topic guidance, section jumping and omitted/hidden report statuses. Manifest and file index now point to active pilot sources. Remaining parity and device limitations are listed in docs/PILOT_ARCHITECTURE.md. Run 42062907339 at 0ac0dd3 passed the smoke journey but the expanded test found two valid section controls and stopped on an ambiguous selector. Target the toolbar control and verify again.

**Safety review:** traverse all eleven opening safety items even when previously answered, restore the review queue from a pilot backup, and show saved timestamps on flagged answers. Require confirmation before replacing a session containing saved answers. CI run 42063169851 passed at d2456a4a2394cb9ae57cc1f2cd9b75c08398422d. Confirmed the toolbar fix, safety review sequence, third-module registration, guided selection, conditional parent edit, section jump, omitted/hidden exports and restoration.

**Source comparison:** verified all 41 IDs and original order, LV/EN/RU prompt/choice/time/help text, multiple-choice/exclusive/incompatible settings, conditions, type, maximum choices and answer statuses against the frozen source modules. Zero differences in those fields.

**Final browser batch:** exercise real section 02 multiple-choice combinations, exclusive options, save/back/edit, and doctor-copy payload at phone width and offline. Mobile-width offline run 42063375002 passed at a3e4582042aa670e16bbac5c312f6ef4e62ad57e. Native Android and legacy v16 migration remain separate acceptance items.

**Recovery guard:** reject backups referencing unavailable selected sections before replacing the current answers. If a backup points beyond an incomplete required opening, resume the opening first. A Chromium regression checks that a rejected backup preserves the current session.

**Clinician summary:** include opening visit context and priorities, each safety answer and its original saved time, and uncertain/refused counts. Test the representative completed report for one A4 page. Long responses may continue onto further pages to retain their text. Recovery guard passed on f23aafc in run 42063533966.

**CI runtime:** use installed Chrome when the runner provides it and fall back to installing Playwright Chromium if absent. This avoids downloading a second browser on supported runners. Repeat the full PDF and offline browser suites.

## 2026-11-05 · PROGRESS-UPDATES-RULE · TASK_DONE

Added `AGENTS.md` to require brief user-visible updates approximately every minute during active multi-step tasks (more frequently when practical), actual progress details, immediate blocker notices, and durable changelog checkpoints after verified batches. This is a workflow instruction rather than a guaranteed timer or background process. The active two-section pilot remains `IN_PROGRESS`.

## 2026-11-05 · MODULAR-THREE-LANGUAGE-TWO-SECTION-PILOT · IN_PROGRESS

**Goal:** a self-contained offline three-language HTML prototype with the authentic original 20-question required opening sequence and one additionally selectable section (02, depression). Preserve user-visible button workflows and build the application from independent question logic + LV/EN/RU text per section, so a one-language one-section edit never touches other language files or module logic.

**Scope:** new `src/pilot/` architecture, localized text and core files, `tools/build_pilot.py`, `tests/pilot/`, `dist/` prototype, `docs/PILOT_ARCHITECTURE.md`, version pointers, changelog. Current `src/modules/182_*` and `reference/baseline/` remain immutable. Do NOT edit distribution Drive or GitHub main. Draft language status retained.

**Workflow:** checkpoint each independently verifiable part; extract original 20 opening questions by original global order 0-19 from six source modules and section 02 by original section number; split logic/text, ensure IDs/codes/branch conditions remain stable; implement shared UI and all existing controls, localized LV/EN/RU interface, offline output; run structural and functionality checks without asserting unperformed clinical review. Add an extensible module registry where more sections can be activated without changing the engine.

**At registration:** source migration verified, before the pilot was built. See PILOT-GENERIC-MODULE-AUDIT above for current progress.
**Next:** create independent per-module per-language source and registry; verify ID and answer-code equality.

## 2026-11-05 · GITHUB-FULL-SOURCE-IMPORT-AND-LV-DISTRIBUTION-NAME · TASK_DONE

**Goal:** import all relevant Google Drive project source/reference files to GitHub `develop`, organize under clearly separated source, test, document, translation and immutable reference/history folders, establish a stable CURRENT file/version index so future work needs no Drive reads; rename the public Latvian Google Drive distribution folder for Latvian-language outreach.

**Boundaries:** preserve existing Drive files; rename the distribution FOLDER only. Do not modify GitHub `main`, publish unreviewed EN/RU, claim complete source migration without 48/48 files and SHA256 readback, or accidentally publish real user answers or private communication. Existing archived Drive source is read-only pending verified Git migration.

**Steps:** (1) inventory Git and ZIP/Drive sources; (2) rename Drive folder and verify; (3) attempt approved source import on `develop`, verify full source list/checksums; (4) create or update manifest/index with active versions, archived versions and exact Git paths; (5) document any blocked operation and a reproducible one-time manual import path; (6) read back GitHub changes, close `TASK_DONE` only if fully satisfied, otherwise `BLOCKED`.

**Historical obstacle (resolved):** previous Google Drive -> public GitHub imports failed with connector safety checks; GitHub held 0/48 modules at that point. Recovery ZIP `190_GITHUB_MIGRATION_READY_MANUAL_UPLOAD.zip` exists locally, 79 Drive-origin reference/source files. Current original documents and completed Latvian HTML are on Drive; development work log is here.

**Verified checkpoint:** Google Drive distribution folder renamed and read back (2 Latvian files). All 79 of 79 Drive-origin development files imported on GitHub `develop` at commit `24d25c992cd866daf0589e16b4c4a1a9b8b7d63f`. Remote and local Git file hash inventories match, with 48 modules present. This validates transfer integrity only, not any release. **Final verification:** 79/79 source/reference files committed on `develop`, with matching local and remote Git file hashes and 48/48 original modules, v16 712-question baseline. Established `project-manifest.json` (79 paths, exact Git SHA1 and byte sizes, version/status roles), `docs/FILE_INDEX.md` (human navigation), and `tools/verify_project_index.py` (local checkout checker). Updated and read back README, migration plan/status, import checklist and integrity script. The verification script was saved and read back; it has not been executed against a local fresh Git checkout in this session. Git `main` untouched. Drive public folder renamed in Latvian, unchanged two LV distribution files. Source transfer task complete; all EN/RU language review, new unified app build, release CI and browser/clinical tests remain separate pending tasks.

## 2026-11-05 · GITHUB-CHANGELOG-HANDOFF · TASK_DONE

**Goal:** switch ongoing task tracking to GitHub, without pretending that the questionnaire source migration is complete.

**Scope:** `docs/CHANGELOG.md`, `docs/MIGRATION_STATUS.md`, `docs/MIGRATION_PLAN.md`, `README.md` (only repository docs). Do not modify published `main`, Google Drive questionnaire or questionnaires.

**Steps:**
1. Create this active changelog with a verified checkpoint.
2. Update conflicting repository instructions and migration status.
3. Read back from GitHub and mark `TASK_DONE` only if all intended documentation is verified.

**At the time of this historical entry:** GitHub contained repository scaffolding but **0/48 questionnaire modules**. Direct transfer from Drive to GitHub was blocked. Existing ZIP import package is ready for manual upload; GitHub source is not yet authoritative.
**Next:** revise repository instructions, verify, then close task.

## Historical pending list from before the verified import

- **GITHUB-SOURCE-MIGRATION — subsequently completed (24d25c9):** 48/48 multilingual source modules, HTML reference baselines, translation catalogs, QA tools and archival materials remain on Drive. The verified ZIP package `190_GITHUB_MIGRATION_READY_MANUAL_UPLOAD.zip` must be extracted and manually uploaded on `develop`, then checked against hashes and counts. Do not claim GitHub holds code until file readback.
- **ENRU-V16-RELEASE — IN_PROGRESS:** EN/RU are drafts and require linguistic, functional and safety checks; never publish as ready.
- **RELEASE-GATE-POLICY — PARTIALLY IMPLEMENTED:** documented fail-closed policy and evidence checker exist, but GitHub Actions and enforced branch protection are not yet installed. Syntax passes alone cannot authorize release.
- **LV public distribution:** Google Drive main folder currently contains exactly `162_Sagatavosanas_vizitei_LV_v16.html` and `163_README_LV_v16.md`. Development changes must not silently modify those releases.

## Prior history — immutable reference

Complete detailed historical Latvian changelog remains in the [archived Drive `166_CHANGELOG_LV.md`](https://drive.google.com/file/d/1rfJWIhSogO-vxiabkZWgE0zmFMuk6MBd/view). That file is **read-only** and is not a competing live changelog. Import a historical snapshot into `docs/history/` only after public-repository privacy checks; never overwrite the active log.

## Required operating procedure

1. Start every new editing task by adding a dated `IN_PROGRESS` entry with scope, source paths, plan and next action.
2. Commit and checkpoint after each meaningful, verified step.
3. After actual tests and remote readback, set `TASK_DONE`; for interruptions or failed actions leave `IN_PROGRESS` or `BLOCKED` with exact next action.
4. Only one active task log: `docs/CHANGELOG.md`. `docs/MIGRATION_STATUS.md` may remain a concise directory/reference but is not a second mutable task log after this handoff.
5. `develop` is the work branch; `main` is not a workbench. Publishing to Drive occurs only from an approved tested release candidate, never directly from unverified development.
6. No real patient information, user answers, recovery files, personal medical records, credentials or private correspondence in this public repository.

### UX-SUPPORT-REPORT-REDESIGN — stage 1 checkpoint (IN_PROGRESS)
- Implemented independent per-answer presentation metadata and compact self-contained AI/doctor text. No codes/JSON/decoding keys in AI. Doctor ordering is ascending; uncertainty/refusal are null, not zero. Original language and logic files unchanged.
- Verified locally: new report acceptance test first failed against old API, then passed; structural 60-question check, frozen-source fidelity including swapped-label rejection, JS syntax passed.
- Browser verification NOT performed for this stage. Existing browser journeys still need updating for the authorized UX/export changes. Local Chromium installation failed (invalid download archive).
- This intermediate checkpoint deliberately skips CI; full browser CI must run after stages 2–3 to avoid obsolete expected-export failures. Not TASK_DONE and not a release.
- Next: optional display layout, fixed navigation, single-tap guard, support communication, legacy restore and browser regression updates.

- Stage 1 implementation commit: `c89a601c6caa7cef7fd80692ebe8dfa0adf6c954`; develop head readback confirmed.

### UX-SUPPORT-REPORT-REDESIGN — stage 2 checkpoint (IN_PROGRESS)
- Implemented pilot v0.2 optional thematic display layout (60 unchanged source questions); personal details last; ordinary goals first. The old opening files remain source storage, not a mandatory questionnaire sequence.
- Single-choice taps save/advance with 500 ms answer-only protection; multi/text retain manual save. Every question is skippable with fixed centered Skip and Back. Scrollable content reserves the navigation viewport. Back/edit and conditional navigation retain saved data.
- Added persistent, focusable, calm LV/EN/RU support with verified 116 123 and distinct 112 guidance. Duplicate messages are suppressed; explicit immediate-help disclosures can show emergency guidance. No automatic contacting or diagnostic categories.
- Added legacy opening-group migration and preserved pilot-v1 recovery/review queues. Tools, usage guide and v0.1/v0.2 notes are collapsed below the questionnaire. No separate user README is needed for the new test artifact.
- Doctor ordering now puts personal information first among equally neutral entries; serious entries remain last. Recorded applicable answers survive topic deselection in exports; conditionally hidden answers remain in recovery. AI copy contains plain self-contained responses, not codes/JSON/key. All underlying source files remain unchanged.
- Verified locally: structural/source-fidelity/layout/report tests and JS syntax; offline Chromium UX journey (single/multi/text, physical double click, back/edit, 320/390/540 px repeated Skip, every-ten recovery, legacy/invalid restore, support accessibility, clipboard, HTML/PDF print, all language structures); module/locale independence and real section 21 journeys passed. Source wording and code mappings are compared to frozen originals. Inspected mobile screenshot and extracted printed sample text.
- An alternate Playwright download succeeded: local browser is Chromium Headless Shell 141 on Linux. This does NOT verify native Android Chrome or human translation quality.
- Next: full develop CI (including all 79 imported-file hashes/712-question inventory), final browser regressions and recorded exact commit/run. TASK_DONE not yet claimed.
- Stage 2 implementation commit: `ee84b5e0f25e2ce52cf3154daa3aaf52b837b19d`; develop head readback confirmed. Local final browser regressions all passed. Built HTML SHA256: `4dca1ed7b0b8d50dfaaad098dd8e2a2e048d2f322d7f94ae7e815282035c737c`. Full CI status pending.

### UX-SUPPORT-REPORT-REDESIGN — final verification update (IN_PROGRESS)
- Final review separated ordinary support from emergency guidance: 116 123 appears for supportive prompts; 112 appears only for immediate-danger triggers, while remaining available in the expanded support details. This preserves 112 without suggesting every distressed response means emergency danger.
- Reran all three local Chromium suites after the change: general browser UX, registry/condition independence, real section 21. All passed. Rebuilt artifact SHA256: `9247828dd55f100c12c449154ee77686397b280139fc2eb28c297c2230c0b0a0`. Full develop CI for this last adjustment pending.
- Native Android Chrome remains UNVERIFIED. Human translation and professional review of source wording and provisional report priorities remain outstanding.

### UX-SUPPORT-REPORT-REDESIGN — TASK_DONE

**Pilot v0.2 implementation complete on `develop`.** The current test pilot contains 60 original questions; the larger 712-question bank is not implemented by this change. No frozen original question data, public `main`, or Google Drive files were changed.

**Verified:**
- Full GitHub Actions run `42162346126` passed at implementation checkpoint `ee84b5e0f25e2ce52cf3154daa3aaf52b837b19d`: all 79 imported file hashes, 48 sections/712 questions, structural/source fidelity, layout/report tests, offline Chromium user journeys, independence and section 21 report journey; prototype artifact built and uploaded as an expiring test artifact.
- The final safety-card adjustment and regression expectation are at `60cc44f429697bc3711a9c80c85ac1504e40b40b`. After that adjustment, all three local Chromium suites passed with Chromium Headless Shell 141: single/multi/text, double taps, Skip/back, 116123 versus 112 display, recovery migration, condition handling, clipboard/print, independence, and frozen section 21 report mapping. Structural, source-fidelity, layout and report tests also passed; final built HTML SHA256 `9247828dd55f100c12c449154ee77686397b280139fc2eb28c297c2230c0b0a0`.
- The final small adjustment was not observed in a new Actions run. Its browser regressions passed locally; do not describe the final code SHA as having a separate green CI run.

**Still unverified:** native Android Chrome touch/file-picker/clipboard/printing; human review of EN/RU and the new interface/report translations; psychiatrist review of provisional question wording and report-priority rules; all imported modules outside the 60-question pilot. This build is ready for another desktop/mobile UX test, not a clinical validation or public release.


## 2026-11-06 · COMPLETE-QUESTIONNAIRE-REVIEW-FEEDBACK · IN_PROGRESS

**Starting commit:** `fd61b0504c8396d5f53fdb9aba5c44dcdefa5414` on `develop`. Current implementation is pilot v0.2: 60 active questions. The frozen source bank has 48 modules/712 questions. Do not call the full questionnaire complete until all modules, behavior and exports are checked.

**Critical design decisions:** Remove the pilot's AI/coded export and presentation weights; use a small, explicit, answer-code allowlist to bold only clearly serious reported answers. Keep one compact clinician report. Green-flag feedback is separate from medical answers, optional, locally backed up, and exports no medical responses or personal details. Feedback Save & Continue preserves an existing answer; if no answer exists it records a skip. Backward compatibility means new code continues to restore pilot-v1 files; old code is not assumed to preserve new feedback fields. Add source modules by stable batches, not one large import, and preserve exact original text/IDs/codes/conditions.

**Numbered checklist**
1. [IN_PROGRESS] Remove AI/coded-answer UI/export and weighting; retain one clinician report with explicit bold-answer mappings.
2. [TODO] Add per-question project-feedback flag and non-destructive Save & Continue; persist in new recovery fields and restore old pilot-v1 backups.
3. [TODO] Add isolated project-feedback copy/export and clinician-report ordering/privacy checks.
4. [TODO] Audit the full 48-module schema against engine capabilities (types, conditions, status, choice constraints, language coverage); register gaps before integration.
5. [TODO] Integrate the original 712 questions in small tested batches; update fidelity/navigation tests after each batch.
6. [TODO] Build the complete offline HTML; update manifest, architecture/index and minimal user-facing documentation after functionality works.
7. [TODO] Run full source-integrity, browser/export/privacy/offline regressions; record unverified Android and human review.

**Next action:** implement checklist item 1 in the pilot only, add focused report tests, run the existing browser/source checks, commit and record the exact checkpoint. No frozen source, `main`, or Drive release edits.
