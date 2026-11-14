# Current working checkpoint

Updated 9 November 2026. `main` is the sole active source. This file describes current state; previous release narratives belong in [history](history/WORK_CHECKPOINT_2026-11-09_before-download-cleanup.md) and the [changelog](CHANGELOG.md).

## Product and package

- Application: **v0.2.4**, LV/EN/RU/UK, 712 questions, 48 immutable source modules and 15 optional sections. Latvian is the reference and initial language. This is a technical-review project; human language/clinical review and physical-phone downloaded-file testing remain pending.
- Build configuration: `src/questionnaire/build.json`. Preserve question IDs/codes and the `mental-pilot-recovery-v1` saved-data contract; follow [feature/module contracts](FEATURE_DEVELOPMENT.md).
- Current HTML/PDF files, hashes and clean build provenance: [package manifest](../MH_Public_version/manifest.json). Package source: `1c928a49c5f3475bcc04e9e5992b8bf2dd1185b2`.
- Current snapshot: [`review/v0.2.4-guide-medical-purpose`](https://github.com/janisp123/mental-health-questionnaire/tree/review/v0.2.4-guide-medical-purpose). Earlier tags and [archived packages](../archive/four-language/) preserve rollback; older product branches are historical.

## Distribution and audience

- Repository and [Drive review folder](https://drive.google.com/drive/folders/1BUlc5W7tRw06JOUE250wCuTe-1ick9xb) contain the same verified HTML/PDF pair. Both were downloaded back byte-identical, with IDs, folder and sharing preserved. [Current readback record](review/checks/2026-11-09-medical-purpose-guide-drive-sync.json).
- The one-page PDF contains opening instructions plus privacy, visit-preparation/non-diagnostic purpose and professional-interpretation notices in all four languages. It has no GitHub link, AI attribution or version-status prose.
- The app footer links GitHub immediately after `made by Janis Paegle`. AI-assisted implementation attribution remains in repository documentation. Follow the [audience/privacy and attribution rules](../AGENTS.md).
- README directs users to Drive for the HTML download, a direct PDF download, and explicit opening steps. GitHub HTML links are labelled as source; raw GitHub HTML is served as plain text. Phone-specific opening behavior remains unverified.
- No app, guide, package or Drive bytes change during this repository documentation maintenance; no distribution update is pending.

## Verification evidence

- Current product/package PR #14: checked head `c534254a9d4448fcd9c379f104478df270ef54f6`, merge `6819c21b06c0c6307f9191b8f84a706aa6d05fc7`; trees matched.
- Full CI [42602725439](https://github.com/janisp123/mental-health-questionnaire/actions/runs/42602725439) and app CI [42602725470](https://github.com/janisp123/mental-health-questionnaire/actions/runs/42602725470) passed with real offline file opening. The maintained suite includes 28 scripts, seven package tests and 5,696 question/locale/phone-width renders.
- Local product checks used explicitly labelled memory loading. The PDF was rendered and visually inspected. Structural/automated checks do not establish translation accuracy, clinical validation or physical-device compatibility.
- Standard verification/publication steps: [release policy](RELEASE_POLICY.md). Do not republish unchanged artifacts for repository-only edits.

## Active development — 14 November 2026

The main product/distribution above remains v0.2.4. Branch `feat/td-feedback-support` starts from main `763dcaa686f0235a342a4526fcc73b76b5db5ffd` and contains a v0.2.5 source candidate for the priority Send feedback / Copy feedback TD task. It does not publish to Drive. See the latest changelog entry and `docs/superpowers/plans/2026-11-14-feedback-sharing.md` for implementation and verification status. Keep the TD item until the verified integration is recorded.

The TD list now contains six tasks; the former one-item checkpoint is historical. Read-only wording triage and effectiveness evaluation are reported to the owner without questionnaire edits. Discovery preparation is an unpublished static preview only. Worldwide support wording needs a conflict decision for the frozen M30_17 safety text before implementation. Repository About description/topics remain blocked: both authenticated settings edits returned HTTP 403 on 14 November; metadata readback confirms topics remain empty.

Next action: finish the feedback source verification and checked PR; build/inspect a candidate package, retain the current Drive pair, and obtain the explicit release decision required by the priority TD task before replacing distribution files. Human language/clinical review, physical-phone file testing, wording decisions and discovery deployment remain separate gates.
