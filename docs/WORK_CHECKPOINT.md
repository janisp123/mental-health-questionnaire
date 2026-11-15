# Current working checkpoint

Updated 15 November 2026. Main is the sole active source.

## Current product and distribution

- Source and current reviewer distribution: **v0.2.10**, LV/EN/RU/UK, 712 questions, 48 preserved source modules and 15 optional sections. Technical review only; human language/clinical and physical-device review remain pending.
- Public downloads: `Mental_Health_Questionnaire_v0.2.10.html` and `Mental_Health_Questionnaire_Guide_v0.2.10.pdf`. Optional ZIP: `Mental_Health_Questionnaire_Package_v0.2.10.zip`. No internal numeric prefixes or build-detail suffixes; shared version immediately before extension.
- The builder/verifier enforce the naming convention. Each delivered app/guide/package change increments the shared version and updates changelog/manifest/checkpoint; exact Git commits track intermediate work. Historical archives retain original names. See AGENTS.md and RELEASE_POLICY.md.
- Previous report-count fixes, worldwide help/helpline reassurance, M04_01 clarification, footer email cleanup and dedicated feedback remain intact. Only embedded version and four latest-ten download-related notes differ from v0.2.9; other questionnaire data, runtime and guide content are unchanged.
- PR #40 merged as `d89cb1848df11223c0e571111bb689155a7156e3`, preserving checked head `9a277bc846e17dec90ca691f4b7b49764b813683` tree. Clean package source `538427b6eb0a3dfa65be50a5b830194605a5d69e`. [Package manifest](../MH_Public_version/manifest.json).
- All 35 local checks passed in labelled memory mode, plus eight package tests. Original naming regressions failed before the fix and pass after it, including direct HTML/ZIP prefix rejection. Independent review found no Critical/Important issue; its minor ZIP test suggestion was addressed.
- Required full/app/discovery CI passed with real offline file opening (43680973892 / 43680973918 / 43680973893); clean HTML/PDF/ZIP verification passed. Unchanged guide rendered and inspected.
- Both Drive downloads match the verified package exactly under their clean names. Stable file IDs, folder and sharing preserved; folder label remains “Mental health questionnaire — current review files”. [Delivery evidence](review/checks/2026-11-15-clean-download-names-drive-sync.json). Archived v0.2.9 and snapshot review/v0.2.10 preserve rollback. Old local downloads retain their original names/bytes.
- Four-language notes, README links and current distribution pointers agree with v0.2.10. Frequency wording stays deferred; other pending TD work is unchanged.

## Website and safeguards

- Discovery page is live at https://janisp123.github.io/mental-health-questionnaire/ . It uses stable download labels/links and needs no version-specific text edits for this release. Public indexing checks did not confirm Google/Bing inclusion; no request was submitted. Owner-account inspection steps: [indexing status](discovery-preview/INDEXING_STATUS.md). Actual crawler visits and AI suggestions remain unverified.
- Protect main is active: PRs and three checks required, force pushes/deletion blocked, no bypass actors. Use checked short-lived PRs. About metadata still has integration settings-permission limits.

## Remaining work and next action

Read [TD](TD_LIST.md) before new work. Earlier wording/effectiveness audits were read-only; broader wording proposals, focus management and the separate omission-note repair are not implemented. Report counts/completion labels are delivered in v0.2.9. The English clinical-coverage verification plan is separate from validation or diagnosis. Dependency-security findings also remain unimplemented recommendations.

Frequency wording and numerical-guide proposals are deferred in TD. No scale redesign is approved; other tasks take priority. Frequency scales remain unchanged in v0.2.10.

Next action: establish owner access to the landing-page URL-prefix property in Google Search Console (and Bing Webmaster Tools), inspect the actual indexed status and request indexing if appropriate. A public HTML verification tag can be added if supplied; no sign-in secrets are needed. Do not rebuild or re-upload the verified v0.2.10 pair for documentation-only work. Keep unrelated queued README-link work separate.
