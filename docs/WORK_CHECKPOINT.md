# Current working checkpoint

Updated 16 November 2026. Main is the sole active source.

## Product and distribution

- Source/package and verified Drive distribution: **v0.2.16**, 716 active questions, LV/EN/RU/UK, 15 optional sections. 712 frozen questions, three additive M46 items and one additive M06 item. Human clinical/translation, report-priority calibration and physical-phone testing remain pending.
- Optional **M06_25** is in existing M06/current safety section after M06_24. It asks how having no family/other responsibilities or people depending on the respondent would affect considering ending their life. Six explicit choices; no current-thoughts gate. The separate catalog owns translations/codes/editorial metadata; runtime and frozen question sources remain unchanged.
- Draft review priority: more likely4; less likely/no change/nonapplicable/uncertainty/refusal3. These are report-order positions only, not clinical ratings or a new emergency trigger. Existing current-intent/safety prompts remain unchanged.
- Package source `d981f1f3a1c575f1f6f0ca998dd3501c66800d30`, source_dirty:false. PR #64 merged as `f5ba8acd326cbb89d202c2597636253765c80737`, matching checked `5d1d4c75c727ebac7d224842ed91b88166de40d7` tree. [Package manifest](../MH_Public_version/manifest.json). v0.2.15 archived intact and review/v0.2.16 snapshot retained.

## Verification and synchronization

- Final local maintained suite **46/46 passed** in explicitly labelled memory mode; managed Chrome blocks file URLs. All three required CI checks passed, with real offline file opening: app43841399631 / discovery43841399706 / full43841399665. [Verification](review/checks/2026-11-16-m06-context-verification.json).
- Focused tests covered every answer in every active locale, old/current progress, clinician preview/PDF text, skip/back, current emergency prompts and absence of requests/errors. All phone renders at320/390px checked and visually inspected. Independent review found no actionable issue. Disabling the single additive hook reproduces the previous question/priority bundle exactly; old progress imports remain valid. Newer exports containing M06_25 require a retained reader/explicit migration if rolling back; never silently drop that answer.
- Drive contains exactly v0.2.16 HTML/PDF, downloaded byte-identical. IDs/folder/sharing preserved; guide bytes unchanged and rendered page inspected. HTML SHA256 `6eccfdbedb9e1cd2bf33ff2b4cbf501ec3babf777e8e652e4db8914ab6c46495`. [Drive readback](review/checks/2026-11-16-m06-context-drive-sync.json).
- README, active docs, landing716 and hosted **v0.2.16 are live/current**. PR #65 merged as `ee8060222e3b4ebdc18903e78f0227b8aee497bb`, matching checked head `6fcdc43c28ed1290c3a615e119cdc1e125552085` tree; three required CI checks passed and Pages **43843288872** succeeded. All native landing bytes/counts/open/download links match checked output. Actual live app bytes equal Drive/package; LV/EN/RU/UK M06_25, prior-version progress, affirmative/uncertain answers, clinician PDF text, 320/390/1280px and hosted/offline transfer passed without browser errors or answer-related requests. The older-progress fixture now uses the canonical version field; complete all24 response/locale local PDF/recovery run and live rerun passed. [Live evidence](review/checks/2026-11-16-m06-context-live.json). Preview counts follow verified Drive distribution; deployment guard remains strict. Save progress manually before closing/reloading.

## Remaining work and next action

Five unrelated TD items remain untouched. Both the new M06 item and GitHub/Drive/hosted v0.2.16 delivery are verified; nothing is partially implemented. Next: human clinical/translation review and physical downloaded-file device testing, or separately authorized TD work. [Previous checkpoint](history/WORK_CHECKPOINT_2026-11-16_before-m06-responsibilities.md). Human reviews remain pending; no clinical validation is claimed.
