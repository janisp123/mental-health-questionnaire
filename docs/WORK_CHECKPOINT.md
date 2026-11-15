# Current working checkpoint

Updated 15 November 2026. Main is the sole active source.

## Current product and distribution

- Source and current verified Drive distribution: **v0.2.13**, LV/EN/RU/UK, 712 questions, 48 preserved source modules and 15 optional sections. Technical review only; human language/clinical and physical-device review remain pending.
- Clinician report responses use internal **1–5 editorial review priority**, with explicit ID/code rules, linked context families and stable original-order ties. Preview/PDF/HTML/text share one entry order. Priorities are not summed or displayed as clinical scores and do not assess risk/triage; professional calibration remains pending. [Policy and limits](review/REPORT_REVIEW_PRIORITY.md).
- All previously included responses retain identical ID/plain/HTML payloads in every active locale. Original question/choice/condition/navigation data, recovery, feedback/help behavior, 650 ms timing and inclusion rules are unchanged. Negative, uncertain and refused responses remain; uncertainty/refusal are not converted to affirmative danger. Optional identifiers remain background.
- PR #50 merged as `0f2f0b62cb1584bc39e751ed4d732ed8c66464d3`, preserving checked head `63fd436c02552ba28a3b99029ff4f02c26e6090d` tree. Clean package source `2bb5f012ea6504427db1ffcc3c9c15cfa0599f89`, `source_dirty: false`; matching HTML/PDF/ZIP verified. [Package manifest](../MH_Public_version/manifest.json).
- All 39 maintained checks pass in final labelled memory mode (`dist/checks-report-priority-final/results.json`). Review-direction/identifier fixes have observed failing-then-passing regressions. Real preview/PDF ordering, old/current progress round trips and packaged mobile layouts passed; guide/clinician PDF inspected. Required full/app/discovery CI passed with real offline file opening (43716679186 / 43716679194 / 43716679044); app CI's missing PDF test dependency was corrected.
- Current Drive filenames: `Mental_Health_Questionnaire_v0.2.13.html` and `Mental_Health_Questionnaire_Guide_v0.2.13.pdf`. Both downloads match exactly; stable IDs/folder/sharing and exactly the current pair. Guide bytes unchanged, previous v0.2.12 archived, snapshot `review/v0.2.13` retained. [Delivery evidence](review/checks/2026-11-15-report-priority-drive-sync.json). Existing downloads require the new HTML to use priority order.

## Website and safeguards

- Live discovery pages: [English](https://janisp123.github.io/mental-health-questionnaire/), [Latviešu](https://janisp123.github.io/mental-health-questionnaire/lv/), [Русский](https://janisp123.github.io/mental-health-questionnaire/ru/). Native visible appointment/depression/anxiety wording and metadata, language navigation, self-canonicals, reciprocal language alternatives, social metadata and a complete sitemap. No scripts/tracking, fixed language-count promise, diagnostic claim or bot/training policy change.
- PR #48 merged as `dc6b46d8ea5a0a68e181ff5aacf7777513300372`, preserving checked head `a3e3ad1f023e9e1e146e8ffbc7bdca9db272cc3d` tree. All required CI passed. Manual Pages run 43706924365 succeeded for that exact source. Every live locale and sitemap returned HTTPS 200 and byte-identical builder output; one stable Drive folder download action per page. Root robots 404 and simulated search-agent requests allow access; actual crawler visits/indexing/AI suggestions remain unverified. [Deployment/readback evidence](review/checks/2026-11-15-localized-discovery-live.json).
- JavaScript-disabled 320/390/1280 layouts, keyboard skip links, language navigation and native content retrieval passed; independent review found no issues. Localized website is unchanged by the report-order update.
- Search Console/Bing owner verification, actual indexed status and index requests remain pending. [Current indexing status](discovery-preview/INDEXING_STATUS.md). Public reachability is not indexing or guaranteed AI recommendation.
- Protect main remains active: PRs/three required checks, blocked force pushes/deletion, no bypass actors. About metadata retains its integration settings-permission limit.

## Remaining work and next action

Read [TD](TD_LIST.md) before new work. Earlier wording/effectiveness audits were read-only; broader wording proposals and focus management remain unimplemented. The clinician omission explanation is delivered in v0.2.12. Report counts/completion labels are delivered in v0.2.9. The English clinical-coverage verification plan is separate from validation or diagnosis. Dependency-security findings also remain unimplemented recommendations.

Frequency wording and numerical-guide proposals are deferred in TD. No scale redesign is approved; other tasks take priority. Frequency scales remain unchanged in v0.2.13.

Next action: obtain professional clinical calibration of the draft editorial report-priority rules before treating their order as clinical importance. Preserve every included answer regardless of position. Search Console/Bing ownership/indexing and unrelated TD remain pending. v0.2.13 GitHub/Drive delivery is verified; do not repeat app uploads for documentation-only work.
