# Current working checkpoint

Updated 16 November 2026. Main is the sole active source.

## Product and distribution

- **v0.2.15**, LV/EN/RU/UK, 715 active questions: 712 unchanged frozen records plus three additive M46 items. 48 source modules, 15 optional sections. Human clinical/language review and physical-phone tests remain pending; this is technical review only.
- Per-question feedback has explicit email preparation, copy/manual fallback and save-for-later. Email contains only the current question and its feedback; no medical answers/identity. The user reviews/sends in an email app. Immediate attempts never enter the queue or advance the question. Opening the flag pauses pending choice auto-save while retaining the selection; save-for-later retains existing behavior.
- Independent M46_07/08/09 ask about coordination/bumping into objects, speech clarity and stuttering including very rare episodes. They remain visible after a negative broad M46 screen. Existing onset/impact and urgent neurological items, frozen IDs/codes/conditions and mental-pilot-recovery-v1 remain unchanged. New report priorities are neutral draft editorial metadata, not clinical scores.
- Source `2b81137751b57f196862ccba468073fa8b54c7ea`, package `source_dirty: false`. PR #59 merged as `45c4c8cfc1db56ed2f58b8b8caa7602216781198`, tree identical to checked head `ffea6336a5231c9204d5661cf838649593d82ade`. [Package manifest](../MH_Public_version/manifest.json). v0.2.14 archived intact; review/v0.2.15 tag retained.

## Verification and synchronization

- Final maintained local suite: **44 passed, 0 failed**, explicitly labelled memory loading because managed Chrome blocks file URLs. All three required CI runs passed, with real offline file opening in CI: app 43832907609, discovery 43832907547, full 43832907669. [Verification](review/checks/2026-11-16-feedback-m46-verification.json).
- Focused tests cover feedback privacy, empty reasons, Unicode/long text, clipboard denial/no mail app, cancellation, queued feedback, pending choice/drafts and navigation; M46 all locales, negative broad screening, old/current recovery and clinician PDFs. Fresh independent review found stale manual copy after edits; regression reproduced the bug, fix invalidates the preview, final suite passed. 320/390px new controls visually inspected in all locales. No real email sent.
- Drive contains exactly the v0.2.15 HTML/PDF, downloaded byte-identical. Stable IDs/folder/sharing preserved; guide bytes unchanged, rendered PDF inspected. HTML SHA256 `71c9036ed014b2e7d2a91b37cd1c431ec7c829fe17dad0cf6738218e07ad242e`. [Drive delivery](review/checks/2026-11-16-feedback-m46-drive-sync.json).
- Hosted **v0.2.15 is live**, byte-identical to the package/Drive HTML. PR #60 merged as `fb680457a81ef9a6d0d8ee3ac798fdd9bd6ca1d2`, matching checked head `8d94f409bebae35abaec44d22e3997a8d96ccd76` tree; all three required delivery CI checks passed. Pages run **43834305197** succeeded. Live HTTPS 200/HTML response, all active locales, 320/390/1280px, immediate feedback/copy/draft editing and queue privacy, M46 negative-screen/rare-choice navigation, older/current progress and clinician PDF text passed. No browser errors or answer-related HTTP requests. [Live evidence](review/checks/2026-11-16-feedback-m46-live.json). Public URLs remain stable; save progress manually before closing/reloading.

## Remaining work and next action

Five unrelated pending/deferred [TD items](TD_LIST.md) remain. Both implemented tasks were removed only after technical verification and Drive readback. Human clinical/translation review, editorial-priority calibration, physical-device tests and actual indexing/AI discovery remain pending; no such validation is claimed.

Next action: obtain human clinical/language review and physical downloaded-file device checks, or separately authorize one of the remaining TD items. Both additions and GitHub/Drive/hosted v0.2.15 delivery are verified; nothing is partially implemented. [Previous checkpoint](history/WORK_CHECKPOINT_2026-11-16_before-feedback-m46.md).
