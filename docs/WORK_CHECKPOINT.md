# Current working checkpoint

Updated 15 November 2026. Main is the sole active source.

## Current product and distribution

- New source/package candidate: **v0.2.13**, LV/EN/RU/UK, 712 questions and 15 optional sections. Verified current Drive remains **v0.2.12** pending required real-file CI, checked merge and readback.
- Report-only internal 1–5 editorial priorities order clinician responses, keeping related condition/named context together and preserving original-order ties. Preview/PDF/HTML/text share one implementation. No aggregate score, clinical severity/risk rating or triage is produced; professional clinical review of the draft rules remains pending.
- Every coded choice in every active locale retains the same report payload; original questions/choices/conditions/navigation, recovery, feedback/help behavior, 650 ms timing and report inclusion are unchanged. Negative/uncertain/refused responses remain included. Uncertain/refused codes retain neutral review priority and are never converted to affirmative risk.
- All 39 maintained checks pass after reviewed fixes (`dist/checks-report-priority-reviewed/results.json`, local memory loading). Independent review's protective, dependence, extreme-impact and supporting-context inversions were corrected in one regression-covered pass. Runtime preview/PDF and old/current progress round trips passed; packaged mobile layouts and guide inspected. Actual physical-device and clinical/language review remain pending.
- Clean source `188574dd048cab90883f91000c3342e896776893` produced verified v0.2.13 HTML/PDF/ZIP (`source_dirty: false`). Public names end in v0.2.13; guide PDF bytes unchanged. Exact v0.2.12 preserved in `archive/four-language/v0.2.12/`. Four-language latest-ten notes explain report order.

## Website and safeguards

- Live discovery pages: [English](https://janisp123.github.io/mental-health-questionnaire/), [Latviešu](https://janisp123.github.io/mental-health-questionnaire/lv/), [Русский](https://janisp123.github.io/mental-health-questionnaire/ru/). Native visible appointment/depression/anxiety wording and metadata, language navigation, self-canonicals, reciprocal language alternatives, social metadata and a complete sitemap. No scripts/tracking, fixed language-count promise, diagnostic claim or bot/training policy change.
- PR #48 merged as `dc6b46d8ea5a0a68e181ff5aacf7777513300372`, preserving checked head `a3e3ad1f023e9e1e146e8ffbc7bdca9db272cc3d` tree. All required CI passed. Manual Pages run 43706924365 succeeded for that exact source. Every live locale and sitemap returned HTTPS 200 and byte-identical builder output; one stable Drive folder download action per page. Root robots 404 and simulated search-agent requests allow access; actual crawler visits/indexing/AI suggestions remain unverified. [Deployment/readback evidence](review/checks/2026-11-15-localized-discovery-live.json).
- JavaScript-disabled 320/390/1280 layouts, keyboard skip links, language navigation and native content retrieval passed; independent review found no issues. Localized website is unchanged by the report-order update.
- Search Console/Bing owner verification, actual indexed status and index requests remain pending. [Current indexing status](discovery-preview/INDEXING_STATUS.md). Public reachability is not indexing or guaranteed AI recommendation.
- Protect main remains active: PRs/three required checks, blocked force pushes/deletion, no bypass actors. About metadata retains its integration settings-permission limit.

## Remaining work and next action

Read [TD](TD_LIST.md) before new work. Earlier wording/effectiveness audits were read-only; broader wording proposals and focus management remain unimplemented. The clinician omission explanation is delivered in v0.2.12. Report counts/completion labels are delivered in v0.2.9. The English clinical-coverage verification plan is separate from validation or diagnosis. Dependency-security findings also remain unimplemented recommendations.

Frequency wording and numerical-guide proposals are deferred in TD. No scale redesign is approved; other tasks take priority. Frequency scales remain unchanged in v0.2.13.

Next action: complete required checked-PR integration for v0.2.13, then replace the same Drive HTML/PDF IDs, verify names/bytes/folder/sharing and record delivery. Leave localized Pages and unrelated TD unchanged. Search Console/Bing ownership/indexing remains pending; priorities need professional clinical calibration.
