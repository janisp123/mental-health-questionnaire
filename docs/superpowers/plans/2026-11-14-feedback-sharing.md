# Feedback sharing implementation plan

**Goal:** Implement the priority feedback task specified in docs/TD_LIST.md.
**Architecture:** Reuse QuestionnaireReports.projectFeedbackText and the separate feedback report. Only saved feedback enters the message. No answers, identity, medication, progress or automatic network activity.
**Tech stack:** Existing vanilla JavaScript, four locale catalogs, Python/Playwright checks.

## Tasks

- [x] Add failing tests for encoded mailto messages, empty feedback, long messages and privacy allowlisting.
- [x] Add a small feedback delivery module with a conservative 1,800-character encoded URL limit. Oversized messages use copying without truncation. A permanent labelled read-only text field provides manual selection if clipboard access fails.
- [x] Add Send feedback and Copy feedback on the existing feedback report; expose that report directly from results when feedback exists. Explain local-only flagging and email privacy in LV/EN/RU/UK. Require deliberate confirmation before opening email; never claim delivery succeeded.
- [x] Run focused tests and the maintained suite; inspect mobile layout, clipboard failure, Unicode, multiple flags, and absence of HTTP requests.
- [ ] Record exact verification and remaining release gates; create a reviewable branch/PR. Preserve existing distributed bytes until release gates and any required owner decisions are satisfied.

## Review focus

Clipboard rejection must leave manual copying available. No-email-client detection is unreliable, so fallback remains visible at all times. Long messages must not truncate. Comments may contain user-entered sensitive content, so warning and confirmation are required. No clinician data may enter the message.
