# Current working checkpoint

Updated 16 November 2026. Main is the sole active source.

## Product and distribution

- Last published/verified product remains **v0.2.14**, 712 frozen questions, LV/EN/RU/UK. Existing GitHub/Drive/hosted parity records remain valid for that version. [Previous checkpoint](history/WORK_CHECKPOINT_2026-11-16_before-feedback-m46.md).
- Current short-lived branch targets v0.2.15: immediate question-only email/copy feedback and three independent supplemental M46 questions (715 active total). Original source question/answer contracts and mental-pilot-recovery-v1 remain unchanged.
- Immediate feedback never sends automatically or adds an attempted email to queued feedback; the user reviews/sends in an email app. Copy/manual fallback and explicit save-for-later remain available. Opening the flag pauses the pending choice timer while preserving the selection.
- All active locales and update notes aligned. New items use neutral draft editorial review priorities, not diagnostic scores. Human clinical/language review and physical-phone testing remain pending.

## Verification and synchronization

- Focused Node/build checks passed after observed missing-feature failures. Focused memory-mode browser tests passed for feedback privacy, all locales, Unicode/copy failure, timer/draft/queue preservation; M46 negative screening, old/current progress and clinician PDFs passed.
- Independent review found stale manual-copy preview after editing: reproduced by regression and corrected; final verification pending. Initial full run: 43 passed/1 test-setup failure, subsequently corrected. Managed Chromium blocks file URLs, so local browser runs are explicitly memory mode; CI must verify real file opening.
- Changes are local on feat/question-feedback-m46; no new package or Drive/hosted update yet. Existing distribution is preserved.

## Next action

Finish review-fix regression and full checks, build clean-source v0.2.15 package, use checked PR and verified Drive/hosted delivery. TD entries remain pending until completion. [Session checkpoint](CHANGELOG.md).
