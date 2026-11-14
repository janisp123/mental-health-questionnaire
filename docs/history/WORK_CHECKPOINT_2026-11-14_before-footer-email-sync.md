# Current working checkpoint

Updated 14 November 2026. Main is the sole active source.

## Current product and distribution

- Source and current reviewer distribution: **v0.2.6**, LV/EN/RU/UK, 712 questions, 48 preserved source modules and 15 optional sections. Technical review only; human language/clinical review and physical-phone testing remain pending.
- Worldwide local-help instructions and the M04_01 panic-peak explanation are implemented and distributed in all four languages. Titles, IDs, choices, conditions, time windows and recovery format remain intact. Frozen originals stay byte-verified; only scoped displayed notices/help differ.
- PR #28 merged as `e46f025ae7a8e73dbae146d443386ae7358e80c9`; tree matches checked head `bccc22536b85c0cb7dead6bb9121fbfcf56e0870`. Clean package source: `f77d91c`. [Package manifest](../MH_Public_version/manifest.json).
- Full/app/discovery CI passed with real offline file opening (43633128671 / 43633128667 / 43633128651); all 34 local scripts passed in explicitly labelled memory mode. New runtime checks verify four-language manual/emergency help, urgent guidance first, visible peak help and unchanged saved answers. Latvian packaged screens visually inspected.
- Drive HTML/PDF downloaded byte-identical, with stable IDs, parent folder and sharing. PDF guide bytes unchanged. [Drive verification](review/checks/2026-11-14-support-peak-drive-sync.json). Prior v0.2.4 and v0.2.5 pairs are preserved in archive/four-language. Old downloaded files do not auto-update.
- Four-language patch notes and README/package pointers are current. The feedback implementation already shipped in v0.2.5 and stays present; completed feedback/local-help tasks are removed from TD by the synchronization record.

## Website and safeguards

- Discovery page is live at https://janisp123.github.io/mental-health-questionnaire/ . It uses stable download labels/links and needs no version-specific text edits for this release. Actual indexing and AI suggestions remain unverified; see docs/discovery-preview/LAUNCH.md.
- Protect main is active: PRs and three checks required, force pushes/deletion blocked, no bypass actors. Use checked short-lived PRs. About metadata still has integration settings-permission limits.

## Remaining work and next action

Read [TD](TD_LIST.md) before new work. Earlier wording/effectiveness audits were read-only; broader wording proposals and report-count/completion/focus/omission repairs are not implemented. The English clinical-coverage verification plan is separate from validation or diagnosis. Dependency-security findings also remain unimplemented recommendations.

Next action: choose the next explicitly authorized task from TD. Do not rebuild or re-upload the already verified v0.2.6 pair. Obsolete package PR #23 is closed as superseded; snapshot review/v0.2.6 preserves this release. Keep unrelated queued README-link work separate.
