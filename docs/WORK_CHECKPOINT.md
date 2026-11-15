# Current working checkpoint

Updated 15 November 2026. Main is the sole active source.

## Current product and distribution

- New source/package candidate: **v0.2.12**, LV/EN/RU/UK, 712 questions, 48 source modules and 15 sections. Current verified Drive distribution remains v0.2.11 pending checked integration and byte readback.
- Clinician preview adds confirmed New questionnaire and public-only sharing/copy controls. Every provided answer, including No/uncertain/refusal, remains; only skipped/missing/blank entries are omitted. Header reports provided-entry count and a brief omission explanation; empty reports offer return/reset/share without printing an empty PDF.
- Contributions is visible in the first-page footer even without names, with consent-based invitation. Current public wording uses multilanguage rather than a fixed count. Questions, answer codes/scales/conditions, 650 ms auto-advance and recovery remain unchanged.
- All 36 maintained checks passed in labelled memory mode (`dist/checks-report-sharing/results.json`); focused regressions failed before fixes and pass after. Native share/clipboard success, missing/rejected APIs and cancellation use synthetic browser APIs; no external sharing took place. Mobile screen/PDF print isolation and the guide were inspected. Independent review found no issues.
- Clean source `2e152a732b7077e9d35d5154b8c2828fdc13b4d6` produced verified HTML/PDF/ZIP (`source_dirty: false`). Public filenames end in v0.2.12. Guide instructions are unchanged; PDF title metadata now says Multilanguage, producing a new PDF hash. Previous v0.2.11 archived exactly. Physical-device/native OS sharing and human language/clinical reviews remain pending.

## Website and safeguards

- README and live GitHub Pages now use exactly one “Download from Google Drive” folder link each, with no separate PDF/raw artifact link. Published source `8063c261f1b33a23f3b78ade95a48178601cb6bf` via Pages run 43682403681; live page/sitemap and main README verified against tested/merged source. [Download-link evidence](review/checks/2026-11-15-single-drive-download-links.json). Queued-only PR #27 is closed as fulfilled. Single-folder download routes remain unchanged; revised multilanguage wording awaits manual Pages publication.
- Discovery page is live at https://janisp123.github.io/mental-health-questionnaire/ . It uses stable download labels/links and needs no version-specific text edits for this release. Public indexing checks did not confirm Google/Bing inclusion; no request was submitted. Owner-account inspection steps: [indexing status](discovery-preview/INDEXING_STATUS.md). Actual crawler visits and AI suggestions remain unverified.
- Protect main is active: PRs and three checks required, force pushes/deletion blocked, no bypass actors. Use checked short-lived PRs. About metadata still has integration settings-permission limits.

## Remaining work and next action

Read [TD](TD_LIST.md) before new work. Earlier wording/effectiveness audits were read-only; broader wording proposals, focus management and the separate omission-note repair are not implemented. Report counts/completion labels are delivered in v0.2.9. The English clinical-coverage verification plan is separate from validation or diagnosis. Dependency-security findings also remain unimplemented recommendations.

Frequency wording and numerical-guide proposals are deferred in TD. No scale redesign is approved; other tasks take priority. Frequency scales remain unchanged in v0.2.12.

Next action: complete required checked-PR integration for v0.2.12, publish the approved landing-page wording, replace the same Drive HTML/PDF IDs and verify bytes/names/folder/sharing. Record delivery and mark the omission explanation delivered; unrelated TD and Search Console/Bing owner verification stay pending.
