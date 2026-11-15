# Current working checkpoint

Updated 15 November 2026. Main is the sole active source.

## Current product and distribution

- Source and current reviewer distribution: **v0.2.11**, LV/EN/RU/UK, 712 questions, 48 preserved modules and 15 optional sections. Technical review only; human language/clinical and physical-device review remain pending.
- Single-choice automatic save/advance now waits **650 ms instead of 1,300 ms**. Highlighting, saved answers and cancellation on navigation remain intact. Other answer kinds, questions, answer codes/scales/conditions and recovery schema are unchanged.
- Public downloads: `Mental_Health_Questionnaire_v0.2.11.html` and `Mental_Health_Questionnaire_Guide_v0.2.11.pdf`; optional ZIP ends in the same version. Four-language latest-ten notes describe the faster transition.
- PR #44 merged as `9bd0b3b19113d9b39a24a3349c956be0bb3c3ec8`, preserving checked head `66284ec410a875c8dfb9b45ed0236327b98d77a9` tree. Clean package source `a80a4e1278eca9ca53c3798ba66b7b95556fe2da`, `source_dirty: false`. [Package manifest](../MH_Public_version/manifest.json).
- All 35 local checks passed in labelled memory mode; timing regression failed before and passes after. Actual packaged HTML in all four locales retains selection at virtual 649 ms and saves/advances at virtual 650 ms; backups contain the selected answer, no errors/network calls. Independent review found no issues.
- Required full/app/discovery CI passed with real offline file opening (43683758114 / 43683758095 / 43683758099); matching HTML/PDF/ZIP verification passed. Unchanged guide rendered and inspected.
- Both Drive files downloaded byte-identical under the clean versioned names. Same IDs, folder and sharing; exactly the current HTML/PDF pair. [Delivery evidence](review/checks/2026-11-15-faster-single-answer-drive-sync.json). Previous v0.2.10 archived; snapshot `review/v0.2.11` pins this release. Existing downloaded copies need a fresh HTML download.

## Website and safeguards

- README and live GitHub Pages now use exactly one “Download from Google Drive” folder link each, with no separate PDF/raw artifact link. Published source `8063c261f1b33a23f3b78ade95a48178601cb6bf` via Pages run 43682403681; live page/sitemap and main README verified against tested/merged source. [Download-link evidence](review/checks/2026-11-15-single-drive-download-links.json). Queued-only PR #27 is closed as fulfilled. Download links remain unchanged for v0.2.11.
- Discovery page is live at https://janisp123.github.io/mental-health-questionnaire/ . It uses stable download labels/links and needs no version-specific text edits for this release. Public indexing checks did not confirm Google/Bing inclusion; no request was submitted. Owner-account inspection steps: [indexing status](discovery-preview/INDEXING_STATUS.md). Actual crawler visits and AI suggestions remain unverified.
- Protect main is active: PRs and three checks required, force pushes/deletion blocked, no bypass actors. Use checked short-lived PRs. About metadata still has integration settings-permission limits.

## Remaining work and next action

Read [TD](TD_LIST.md) before new work. Earlier wording/effectiveness audits were read-only; broader wording proposals, focus management and the separate omission-note repair are not implemented. Report counts/completion labels are delivered in v0.2.9. The English clinical-coverage verification plan is separate from validation or diagnosis. Dependency-security findings also remain unimplemented recommendations.

Frequency wording and numerical-guide proposals are deferred in TD. No scale redesign is approved; other tasks take priority. Frequency scales remain unchanged in v0.2.11.

Next action: establish owner access to the landing-page URL-prefix property in Google Search Console (and Bing Webmaster Tools), inspect indexed status and request indexing if appropriate. A public HTML verification tag can be added if supplied; no sign-in secrets are needed. Do not rebuild or re-upload the verified v0.2.11 pair for documentation-only work. The faster-answer and README/Pages download-link tasks are delivered; unrelated pending TD work is unchanged.
