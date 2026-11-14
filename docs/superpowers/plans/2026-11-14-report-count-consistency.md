# Report count consistency implementation plan

**Goal:** Correct report scope and distinguish answered from skipped questions consistently, then check search indexing without changing questionnaire content.

**Approved scope:** Targeted report-count/completion-label repairs from audit findings E2/E3. Preserve earlier applicable saved answers after section changes. Frequency wording stays deferred; question-focus and omission-note proposals are separate.

**Architecture:** `QuestionnaireModel.reportQuestions(state)` returns applicable questions from selected/required sections plus applicable questions with existing saved records elsewhere. Counters and clinician answer rendering consume that same pool. Results and PDF use the same covered/answered/skipped labels; section progress counts answers and skips separately. Recovery and question contracts stay unchanged.

**Files:** `src/app/core/model.js`, `src/app/core/app.js`, `src/app/screens/results.js`, `src/app/screens/section-selector.js`, `src/app/reports/reports.js`, four UI catalogs, `src/questionnaire/build.json`; focused model/screen/browser/report tests. Package and delivery records follow the standard release workflow.

**Invariants:** Required and selected applicable unanswered questions count toward coverage; untouched unselected questions do not. Previously saved applicable answers/skips from deselected sections remain counted and retain existing reporting behavior. Conditional hidden answers remain backed up and excluded. Unknown/refused choices remain recorded responses; skipping stays distinct. Report and UI language selection remain independent.

## Execution

- [x] Trace and reproduce root causes: report pool includes untouched unselected sections; results add skips to answered while report does not.
- [x] Add failing model/screen regressions and a four-language browser scenario for selected-only counts, skips, hidden follow-ups, preserved answers from deselected sections, independent report language and backup round trips.
- [x] Apply the smallest shared fixes; align LV/EN/RU/UK labels, coverage explanation and latest-ten patient notes; assign v0.2.9.
- [x] Run focused checks, all maintained checks in labelled local memory mode, and independent review. Inspect summary, selector and clinician output at phone widths; verify PDF print output.
- [ ] Commit clean source, archive v0.2.8, build/verify matching HTML/PDF/ZIP, integrate exact checked PR head, preserve a version tag, replace the same Drive IDs and compare exact downloaded bytes.
- [ ] Record delivery, current checkpoint and narrowly completed audit findings. Keep other audit proposals pending.
- [x] Check live landing page/sitemap and public search observations; distinguish crawl eligibility from confirmed indexing. Record owner-account steps if Search Console/Bing verification is unavailable; do not claim an index request or AI recommendation occurred without evidence.

## Record

- Baseline: main `2db69973e3a1ccfa0c77137e7823042ca4e84985`, verified v0.2.8 distribution. Audit evidence: `/workspace/scratch/TD_REVIEW_2026-11-14.md` E2/E3 (private local reference, not an added public artifact).

- Verification: original model/results/selector regressions failed before production changes and pass afterward. All 35 maintained scripts passed in memory mode; focused browser cases additionally cover partial unanswered states and optional-parent boundaries. Independent review found no Critical/Important issues; its minor partial-state coverage suggestion was addressed with a browser case. Search eligibility passed; Google/Bing indexing remains unverified, with no index request submitted.

- Full-bank visual evidence: each locale showed covered/answered/skipped = 63/2/1 for S11 plus one previously saved S12 response. Summary/selector width checks passed at 320/390px. Four generated clinician PDFs were rendered and inspected; no count/answer text clipping.

- Package preparation: clean source `792b192cf0f993ef9e98ed46a5dbca411154442d`; HTML/PDF/ZIP verified. Packaged full-bank counts and print generation match source in all four locales. Unchanged guide rendered and inspected. Checked integration and Drive readback pending.
