# Current working checkpoint

Updated 15 November 2026. Main is the sole active source.

## Current product and distribution

- New source/package candidate: **v0.2.11**, LV/EN/RU/UK, 712 questions and 15 sections. Current Google Drive reviewer distribution remains verified **v0.2.10** pending checked integration and exact-byte replacement/readback.
- The single-choice automatic save/advance delay is halved from **1,300 to 650 ms**. Selection highlighting, saving and navigation cancellation remain intact; other answer types, question text/scales/conditions and recovery are unchanged.
- All 35 maintained local checks passed in labelled memory mode (`dist/checks-faster-single-answer/results.json`); focused timing regression failed before and passes after. Independent review found no material issue. Required real-file CI is pending.
- Clean source `a80a4e1278eca9ca53c3798ba66b7b95556fe2da` produced verified v0.2.11 HTML/PDF/ZIP (`source_dirty: false`); guide PDF bytes unchanged. Candidate public names: `Mental_Health_Questionnaire_v0.2.11.html` and `Mental_Health_Questionnaire_Guide_v0.2.11.pdf`. Previous v0.2.10 pair preserved in `archive/four-language/v0.2.10/`.
- Four-language latest-ten notes describe the faster transition. Human language/clinical and physical-device reviews remain pending. No new clinical wording or scale redesign is included.

## Website and safeguards

- README and live GitHub Pages now use exactly one “Download from Google Drive” folder link each, with no separate PDF/raw artifact link. Published source `8063c261f1b33a23f3b78ade95a48178601cb6bf` via Pages run 43682403681; live page/sitemap and main README verified against tested/merged source. [Download-link evidence](review/checks/2026-11-15-single-drive-download-links.json). Queued-only PR #27 is closed as fulfilled. Download links remain unchanged for v0.2.11.
- Discovery page is live at https://janisp123.github.io/mental-health-questionnaire/ . It uses stable download labels/links and needs no version-specific text edits for this release. Public indexing checks did not confirm Google/Bing inclusion; no request was submitted. Owner-account inspection steps: [indexing status](discovery-preview/INDEXING_STATUS.md). Actual crawler visits and AI suggestions remain unverified.
- Protect main is active: PRs and three checks required, force pushes/deletion blocked, no bypass actors. Use checked short-lived PRs. About metadata still has integration settings-permission limits.

## Remaining work and next action

Read [TD](TD_LIST.md) before new work. Earlier wording/effectiveness audits were read-only; broader wording proposals, focus management and the separate omission-note repair are not implemented. Report counts/completion labels are delivered in v0.2.9. The English clinical-coverage verification plan is separate from validation or diagnosis. Dependency-security findings also remain unimplemented recommendations.

Frequency wording and numerical-guide proposals are deferred in TD. No scale redesign is approved; other tasks take priority. Frequency scales remain unchanged in v0.2.11.

Next action: finish required checked-PR integration for v0.2.11, then replace the same Drive HTML/PDF IDs and verify bytes, names, folder and sharing. Update this checkpoint and distribution manifest after readback. Search Console/Bing owner verification and unrelated TD work remain pending.
