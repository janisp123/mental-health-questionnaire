# Current working checkpoint

Updated 15 November 2026. Main is the sole active source.

## Current product and distribution

- Source and current verified Drive distribution: **v0.2.12**, LV/EN/RU/UK, 712 questions, 48 preserved source modules and 15 optional sections. Technical review only; human language/clinical and physical-device review remain pending.
- Clinician preview has confirmed New questionnaire and public-only sharing/copy controls. Every provided answer, including No/uncertain/refused choices, remains; only skipped/missing/blank entries are omitted. Header shows provided-entry count plus brief omission explanation; no empty PDF action. Sharing/reset controls are excluded from print.
- Contributions stays visible in the first-page footer even without names; names require permission. Current public wording uses multilanguage rather than a fixed count. Original questions/scales/conditions, recovery and 650 ms auto-advance remain unchanged.
- PR #46 merged as `282a8dcd62beb427ea70bdc51164c67e097af25a`, preserving checked head `80466c571c4a8dd82cb91879d85e5e7978c4186d` tree. Clean package source `2e152a732b7077e9d35d5154b8c2828fdc13b4d6`; HTML/PDF/ZIP verified. Guide instructions unchanged; PDF title metadata uses Multilanguage. [Package manifest](../MH_Public_version/manifest.json).
- All 36 maintained local checks passed in labelled memory mode; independent review found no issues. Required full/app/discovery CI passed with real offline file opening (43688233639 / 43688233520 / 43688233475). Localized mobile layouts, clinician PDF isolation and companion guide inspected. Native sharing/clipboard scenarios use controlled synthetic APIs; physical-device OS sharing remains unverified.
- Current Drive filenames: `Mental_Health_Questionnaire_v0.2.12.html` and `Mental_Health_Questionnaire_Guide_v0.2.12.pdf`. Both downloads match exactly, with same IDs/folder and verified baseline sharing; exactly the current pair. Previous v0.2.11 archived; snapshot `review/v0.2.12` preserves rollback. [Delivery evidence](review/checks/2026-11-15-report-sharing-drive-sync.json). Existing downloads require a fresh HTML file.

## Website and safeguards

- README and live GitHub Pages now use exactly one “Download from Google Drive” folder link each, with no separate PDF/raw artifact link. Published source `8063c261f1b33a23f3b78ade95a48178601cb6bf` via Pages run 43682403681; live page/sitemap and main README verified against tested/merged source. [Download-link evidence](review/checks/2026-11-15-single-drive-download-links.json). Queued-only PR #27 is closed as fulfilled. Single-folder download routes remain unchanged; revised multilanguage wording awaits manual Pages publication.
- Discovery page is live at https://janisp123.github.io/mental-health-questionnaire/ . It uses stable download labels/links and needs no version-specific text edits for this release. Public indexing checks did not confirm Google/Bing inclusion; no request was submitted. Owner-account inspection steps: [indexing status](discovery-preview/INDEXING_STATUS.md). Actual crawler visits and AI suggestions remain unverified.
- Protect main is active: PRs and three checks required, force pushes/deletion blocked, no bypass actors. Use checked short-lived PRs. About metadata still has integration settings-permission limits.

## Remaining work and next action

Read [TD](TD_LIST.md) before new work. Earlier wording/effectiveness audits were read-only; broader wording proposals and focus management remain unimplemented. The clinician omission explanation is delivered in v0.2.12. Report counts/completion labels are delivered in v0.2.9. The English clinical-coverage verification plan is separate from validation or diagnosis. Dependency-security findings also remain unimplemented recommendations.

Frequency wording and numerical-guide proposals are deferred in TD. No scale redesign is approved; other tasks take priority. Frequency scales remain unchanged in v0.2.12.

Next action: implement and verify owner-requested English/Latvian/Russian discovery pages and publish through the Pages workflow, then verify live localized URLs/canonical/hreflang/sitemap and record actual deployment. App/Drive v0.2.12 is delivered; do not rebuild or upload it for website-only work. Search Console/Bing owner verification and unrelated TD remain pending.
