# Current working checkpoint

Updated 14 November 2026. Main is the sole active source.

## Current product and distribution

- Source and current reviewer distribution: **v0.2.8**, LV/EN/RU/UK, 712 questions, 48 preserved source modules and 15 optional sections. Technical review only; human language/clinical review and physical-phone testing remain pending.
- Worldwide local-help instructions and the M04_01 panic-peak explanation are implemented and distributed in all four languages. Titles, IDs, choices, conditions, time windows and recovery format remain intact. Frozen originals stay byte-verified; only scoped displayed notices/help differ.
- Footer contact email and its otherwise empty panel are removed in all four locales. The creator GitHub link and separate Send feedback action/recipient remain. Questions, saved answers and recovery format are unchanged.
- Helpline reassurance is implemented in all four locales before the existing short opening phrase: no prepared speech, listening/help without judgment, possible specialist/local-support suggestions, and asking about confidentiality before personal disclosure. Urgent emergency guidance remains first.
- PR #35 merged as `3c4d9833e42f83751f61b9e9f0598dea205094ac`, with checked head `81d0a4d1009a19384749d81a0559e445e3339a43` tree preserved. Clean package source `7c961f6cfaf95e62c52aa70f852b759b35ea8a7c`. [Package manifest](../MH_Public_version/manifest.json).
- Full/app/discovery CI passed, including real offline file opening (43643161675 / 43643161619 / 43643161661). All 34 local checks passed in labelled memory mode. Shared support paths, saved answers, recovery and reports passed; four-language panels and unchanged guide visually inspected. Independent review found no material issues.
- Drive HTML/PDF downloaded byte-identical, with stable IDs, folder and sharing. Guide PDF unchanged; prior v0.2.7 pair archived. [Drive verification](review/checks/2026-11-14-helpline-reassurance-drive-sync.json). Old downloaded files do not auto-update.
- Four-language patch notes and README/package pointers are current. Completed helpline reassurance is removed from TD; frequency wording remains explicitly deferred.

## Website and safeguards

- Discovery page is live at https://janisp123.github.io/mental-health-questionnaire/ . It uses stable download labels/links and needs no version-specific text edits for this release. Actual indexing and AI suggestions remain unverified; see docs/discovery-preview/LAUNCH.md.
- Protect main is active: PRs and three checks required, force pushes/deletion blocked, no bypass actors. Use checked short-lived PRs. About metadata still has integration settings-permission limits.

## Remaining work and next action

Read [TD](TD_LIST.md) before new work. Earlier wording/effectiveness audits were read-only; broader wording proposals and report-count/completion/focus/omission repairs are not implemented. The English clinical-coverage verification plan is separate from validation or diagnosis. Dependency-security findings also remain unimplemented recommendations.

Frequency wording and numerical-guide proposals are deferred in TD. No scale redesign is approved; other tasks take priority. Frequency scales remain unchanged in v0.2.8.

Next action: choose the next explicitly authorized task from TD. Do not rebuild or re-upload the already verified v0.2.8 pair. Obsolete package PR #23 is closed as superseded; snapshot review/v0.2.8 preserves this release. Keep unrelated queued README-link work separate.
