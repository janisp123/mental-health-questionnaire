# Current working checkpoint

**Active work:** hosted questionnaire on `feat/host-questionnaire-20261115`; pushed planning/TD checkpoint `3087dc3`. Resume from [plan](superpowers/plans/2026-11-15-hosted-questionnaire.md) and latest changelog. Local publication and HTTPS/browser tests pass; review, checked merge/deployment and live readback remain pending. The downloadable v0.2.14 pair is unchanged; the current live landing pages still offer download only.

Updated 15 November 2026. Main is the sole active source.

## Current product and distribution

- Source, repository package and verified Drive distribution: **v0.2.14**, LV/EN/RU/UK, 712 preserved questions, 48 source modules and 15 optional sections. Technical review only; human language/clinical and physical-device review remain pending.
- Existing M14_02 medicine entry now has clearer instructions, strength/effects/dose-timing wording and optional observation examples. Existing M02_09 has optional help locating the separate safety questions. All active locales updated. Frozen question titles, codes, conditions, support triggers, 650 ms timing, progress schema, report inclusion and editorial ordering remain unchanged. No new clinical question or score.
- PR #52 merged as `7c755fa0325ed20dd3a77874770cff531cc999f6`; tree equals checked head `633c9c0ab15833b9b78acfec260afceacfab6d81`. All three required CI runs passed with real offline file opening (43733188539 / 43733188532 / 43733188566). Clean package source `8e63aefa0c53a505af0867db964e7848f1ad7215`, `source_dirty: false`. [Package manifest](../MH_Public_version/manifest.json).
- All 40 final local checks passed in labelled memory mode (`dist/checks-appointment-guidance-final/results.json`). Initial legacy-language compatibility and browser-selector failures were corrected and verified. One independent source review found no additional actionable issues. All guidance locales at 320/390px and actual packaged synthetic older-progress/clinician preview/PDF response preservation passed; guide rendered and inspected. [Verification](review/checks/2026-11-15-appointment-guidance-verification.json).
- Drive contains exactly `Mental_Health_Questionnaire_v0.2.14.html` and `Mental_Health_Questionnaire_Guide_v0.2.14.pdf`, downloaded byte-identical to the checked package. Existing IDs, folder and sharing preserved; guide bytes unchanged. Previous v0.2.13 pair archived, snapshot `review/v0.2.14` retained. [Delivery readback](review/checks/2026-11-15-appointment-guidance-drive-sync.json). Existing downloads need the new HTML to show the wording changes.
- Clinician report ordering remains draft internal 1–5 editorial priority, without a summed/displayed clinical score or triage assessment. Professional calibration is pending. Negative, uncertain and refused provided answers remain; omissions are not negative responses. [Priority policy](review/REPORT_REVIEW_PRIORITY.md).

## Website and safeguards

- Live discovery pages: [English](https://janisp123.github.io/mental-health-questionnaire/), [Latviešu](https://janisp123.github.io/mental-health-questionnaire/lv/), [Русский](https://janisp123.github.io/mental-health-questionnaire/ru/). Native visible appointment/depression/anxiety wording and metadata, language navigation, self-canonicals, reciprocal language alternatives, social metadata and a complete sitemap. No scripts/tracking, fixed language-count promise, diagnostic claim or bot/training policy change.
- PR #48 merged as `dc6b46d8ea5a0a68e181ff5aacf7777513300372`, preserving checked head `a3e3ad1f023e9e1e146e8ffbc7bdca9db272cc3d` tree. All required CI passed. Manual Pages run 43706924365 succeeded for that exact source. Every live locale and sitemap returned HTTPS 200 and byte-identical builder output; one stable Drive folder download action per page. Root robots 404 and simulated search-agent requests allow access; actual crawler visits/indexing/AI suggestions remain unverified. [Deployment/readback evidence](review/checks/2026-11-15-localized-discovery-live.json).
- JavaScript-disabled 320/390/1280 layouts, keyboard skip links, language navigation and native content retrieval passed; independent review found no issues. Localized website is unchanged by the report-order update.
- Search Console/Bing owner verification, actual indexed status and index requests remain pending. [Current indexing status](discovery-preview/INDEXING_STATUS.md). Public reachability is not indexing or guaranteed AI recommendation.
- Protect main remains active: PRs/three required checks, blocked force pushes/deletion, no bypass actors. About metadata retains its integration settings-permission limit.

## Remaining work and next action

Read [TD](TD_LIST.md) before new work. The focused coverage audit is delivered; its two targeted guidance improvements are shipped. Optional general-context question and frequency wording/scale redesign remain deferred. Broader wording proposals, question focus management, English clinical-coverage verification and dependency-security recommendations remain separate unfinished work; do not repeat completed audits or shipped report/help fixes.

Next action: obtain professional clinical calibration of draft report priorities and human review of clinical/language wording. Search Console/Bing ownership/indexing and physical downloaded-file device tests remain pending. v0.2.14 GitHub/Drive delivery is verified; documentation-only updates do not require another upload. [Previous checkpoint](history/WORK_CHECKPOINT_2026-11-15_before-appointment-guidance-sync.md).
