# Current working checkpoint

Updated 14 November 2026. Main is the sole active source.

## Current product and distribution

- Source and current reviewer distribution: **v0.2.7**, LV/EN/RU/UK, 712 questions, 48 preserved source modules and 15 optional sections. Technical review only; human language/clinical review and physical-phone testing remain pending.
- Worldwide local-help instructions and the M04_01 panic-peak explanation are implemented and distributed in all four languages. Titles, IDs, choices, conditions, time windows and recovery format remain intact. Frozen originals stay byte-verified; only scoped displayed notices/help differ.
- Footer contact email and its otherwise empty panel are removed in all four locales. The creator GitHub link and separate Send feedback action/recipient remain. Questions, saved answers and recovery format are unchanged.
- PR #32 merged as `454aae3987104633fbf3e0227087ee775911eff4`; tree matches checked head `1a01922e30a02f008d7cc1807df2c10180c82322`. Clean package source: `e6771d25db407ec24e70df9dd8f79cb09d228122`. [Package manifest](../MH_Public_version/manifest.json).
- Full/app/discovery CI passed, including real offline file opening (43637161224 / 43637161170 / 43637161166); all 34 local scripts passed in labelled memory mode. Four-language footer checks, dedicated feedback/recovery regressions, clean package verification and independent review passed. Latvian packaged phone layout visually inspected.
- Drive HTML/PDF downloaded byte-identical with stable IDs, folder and sharing. Guide PDF bytes unchanged; prior v0.2.6 pair archived. [Drive verification](review/checks/2026-11-14-footer-email-drive-sync.json). Old downloaded files do not auto-update.
- Four-language patch notes and README/package pointers are current. Helpline reassurance remains queued in TD, without implementation or distribution changes for that task.

## Website and safeguards

- Discovery page is live at https://janisp123.github.io/mental-health-questionnaire/ . It uses stable download labels/links and needs no version-specific text edits for this release. Actual indexing and AI suggestions remain unverified; see docs/discovery-preview/LAUNCH.md.
- Protect main is active: PRs and three checks required, force pushes/deletion blocked, no bypass actors. Use checked short-lived PRs. About metadata still has integration settings-permission limits.

## Remaining work and next action

Read [TD](TD_LIST.md) before new work. Earlier wording/effectiveness audits were read-only; broader wording proposals and report-count/completion/focus/omission repairs are not implemented. The English clinical-coverage verification plan is separate from validation or diagnosis. Dependency-security findings also remain unimplemented recommendations.

Next action: choose the next explicitly authorized task from TD. Do not rebuild or re-upload the already verified v0.2.7 pair. Obsolete package PR #23 is closed as superseded; snapshot review/v0.2.7 preserves this release. Keep unrelated queued README-link work separate.
