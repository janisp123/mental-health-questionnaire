# Resume checkpoint

Updated 9 November 2026, Riga time. Active fix branch: `codex/fix-four-language-qa`, based on `codex/four-language-candidate` at `9f62ed84f35137e110695c48c23bbe0a97c735cb`.

## Four-language QA fix checkpoint

- Owner requested the four fixes found in the 9 November audit. Implementation and local verification are complete on the dedicated fix branch; main and the shared reviewer files remain unchanged.
- Medication widths, seven Russian heading/flag layouts, unsaved feedback across language changes and the independent report heading locale are corrected.
- All 26 active scripts passed; the four new browser regressions pass after failing on the baseline. Browser checks used in-memory HTML because this managed Chromium blocks file navigation.
- The four-language `v0.2.1-reports` HTML rebuild has SHA-256 `4bbcccbdfd06a124bb28d13fd843e23e303464c0e05796a4d403dad3848a82b7`. The 2,848-layout sweep and 112 sampled screens have no overflow; PDF data separation and offline behavior passed.
- Evidence: `docs/review/checks/2026-11-09-four-language-qa.json`. Independent review found no blockers. The latest changelog entry records the fix details. Check the GitHub branch/PR for synchronization; a local checkpoint alone does not imply a push.
- Next action: integrate the verified fix branch into the four-language candidate, then run physical-phone downloaded-file testing and human language/clinical review before promotion.

## Translation audit

- Verified sections: S11, S01, S09, S06, S10, S13 (323 of 712 questions).
- S13 covered 70 questions. Independent review corrections and the repair of five invalid Russian option keys are included. All 24 local checks passed, including offline Chromium and exact Latvian source parity.
- Evidence: [S13 audit](review/audit-S13.md) and [local test log](review/checks/S13-local.txt).
- S12 complete: 42 questions in modules 19, 24 and 38. Source integrity, frozen LV parity, locale catalogs, full offline build and Chromium journey passed. Verified total: 365 of 712 questions across seven sections.
- S14 complete: 49 questions across modules 20, 28, 36, 37, 44 and 45. Source integrity, frozen LV parity, locale catalogs, full offline build and Chromium journey passed. Verified total: 414 of 712 questions across eight sections.
- S15 complete: 47 questions across modules 26, 27, 34 and 40. Source integrity, frozen LV parity, locale catalogs, full offline build and Chromium journey passed. Verified total: 461 of 712 questions across nine sections.
- S07 complete: 45 questions in modules 09, 29, 39, 47 and 48. Source integrity, frozen LV parity, locale catalogs, full offline build and Chromium journey passed. Verified total: 506 of 712 questions across ten sections.
- S08 complete: 48 questions in modules 10, 35, 41 and 42. Source integrity, frozen LV parity, locale catalogs, full offline build and Chromium journey passed. Verified total: 554 of 712 questions across eleven sections.
- S02 complete: 38 questions in modules 02 and 05. The first nine legacy screening records were preserved. Source integrity, frozen LV parity, locale catalogs, full offline build and Chromium journey passed. Verified total: 592 of 712 questions across twelve sections.
- S03 complete: 40 questions in modules 03, 04 and 22. Seven legacy screening records were preserved. Source integrity, frozen Latvian parity, locale catalogs, offline HTML build and Chromium journey passed. Total audited: 632 of 712 across thirteen sections.
- S04 complete: 44 questions in modules 06 and 21. Source integrity, frozen Latvian parity, locale catalogs, offline HTML build and Chromium journey passed. Total audited: 676 of 712 across fourteen sections.
- S05 complete: 36 questions in module 18. Source integrity, frozen Latvian parity, locale catalogs, offline HTML build and Chromium journey passed. Translation audit complete: 712 of 712 questions across all 15 sections.
- Technical QA: all 23 active checks passed. Verified the packaged HTML offline, including emergency support, recovery compatibility and 45 viewport and locale combinations. See the [reviewer test plan](superpowers/plans/2026-11-08-reviewer-release-testing.md) for evidence and outstanding checks.
- Toolbar landmark localization fixed and verified in LV, EN and RU. Rebuilt and tested the repository reviewer HTML.
- The updates panel shows the latest ten changes and future plans in all three languages. Feedback and acknowledgements have a separate panel. Rebuilt and verified the reviewer HTML in all three languages.
- The footer shows question counts, professional interpretation wording, the inline creator credit and a statement that the questionnaire is free for everyone to use. Verified in the rebuilt reviewer HTML.
- The Latvian HTML interface uses polite address. All 712 frozen Latvian questions were screened for informal address and source parity passed. The PDF guide now uses formal Latvian address.
- Reviewer HTML and PDF include PC zoom instructions in all three languages. The HTML omits the translation draft notices.
- The results screen offers a separate report language. Offline Chromium verified all three report languages, unchanged answers and PDF output.
- Results offers a separate feedback PDF preview with email instructions. Verified the printed PDF in all three languages with no questionnaire answers.
- Report print layout keeps the local file path out of clinician and feedback PDFs. Verified multipage output with Chromium headers and footers enabled.
- Fixed the gap between the section picker’s bottom buttons. Verified at phone widths in Chromium and added a device retest to the checklist.
- The improvement goals checklist accepts all 12 applicable choices. Verified exclusivity, save and restore in offline Chromium.
- Next action: run the physical Android journey and obtain human language and clinical review.

## Reviewer package

- The repository reviewer copies are kept under `MH_Public_version`. The shared Google Drive folder is updated separately by the owner.
- Human language and clinical review and physical Android testing are outstanding.
