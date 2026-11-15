# Current working checkpoint

Updated 15 November 2026. Main is the sole active source.

## Current product and distribution

- Source and current reviewer distribution: **v0.2.9**, LV/EN/RU/UK, 712 questions, 48 preserved source modules and 15 optional sections. Technical review only; human language/clinical and physical-device review remain pending.
- Report coverage excludes untouched unselected questions and retains applicable saved records from other sections. Summary and clinician report share covered/answered/skipped counts; selector separates answers/skips. Existing conditional visibility, questions, answer scales and recovery are unchanged.
- Worldwide local-help instructions, M04_01 peak help, helpline reassurance and footer email cleanup remain present in all four locales. The creator GitHub link and dedicated feedback action/recipient remain.
- PR #37 merged as `3b96647acf662276830e43a4f868af984bf4000d` with checked head `be485f1bd6399b31c5294084588bf9aec5b8cd77` tree preserved. Clean package source `792b192cf0f993ef9e98ed46a5dbca411154442d`. [Package manifest](../MH_Public_version/manifest.json).
- All 35 local scripts passed in labelled memory mode; added count regressions failed before the fix and pass after it. Partial progress, hidden follow-ups, deselection, independent report language and saved-record round trips verified. Independent review found no blocking issue; its minor partial-state coverage suggestion was addressed.
- Required full/app/discovery CI passed with real offline file opening (43645566104 / 43645566062 / 43645566075). Four-language summaries, selector widths and generated clinician PDFs visually checked; unchanged guide rendered and inspected.
- Both Drive downloads match the verified package exactly. Stable IDs, folder and sharing preserved; previous v0.2.8 archived, snapshot review/v0.2.9 retained. [Delivery evidence](review/checks/2026-11-15-report-counts-drive-sync.json). Existing downloaded copies require a fresh HTML download.
- Four-language notes, README, distribution manifest and TD statuses agree with the delivered work. Frequency wording remains deferred; focus management and the separate omission-note proposal remain pending.

## Website and safeguards

- Discovery page is live at https://janisp123.github.io/mental-health-questionnaire/ . It uses stable download labels/links and needs no version-specific text edits for this release. Public indexing checks did not confirm Google/Bing inclusion; no request was submitted. Owner-account inspection steps: [indexing status](discovery-preview/INDEXING_STATUS.md). Actual crawler visits and AI suggestions remain unverified.
- Protect main is active: PRs and three checks required, force pushes/deletion blocked, no bypass actors. Use checked short-lived PRs. About metadata still has integration settings-permission limits.

## Remaining work and next action

Read [TD](TD_LIST.md) before new work. Earlier wording/effectiveness audits were read-only; broader wording proposals, focus management and the separate omission-note repair are not implemented. Report counts/completion labels are delivered in v0.2.9. The English clinical-coverage verification plan is separate from validation or diagnosis. Dependency-security findings also remain unimplemented recommendations.

Frequency wording and numerical-guide proposals are deferred in TD. No scale redesign is approved; other tasks take priority. Frequency scales remain unchanged in v0.2.9.

Next action: establish owner access to the landing-page URL-prefix property in Google Search Console (and Bing Webmaster Tools), inspect the actual indexed status and request indexing if appropriate. A public HTML verification tag can be added if supplied; no sign-in secrets are needed. Do not rebuild or re-upload the verified v0.2.9 pair for documentation-only work. Keep unrelated queued README-link work separate.
