# Usage guide and update information implementation plan

**Goal:** Implement the existing task from PR73 at107d0b5; Added by ChatGPT, implementation by Codex.
**Architecture:** Keep the existing footer and single hosted/offline application. Retain detailed notesHistory records; display a separate aligned list of concise dated summaries. Remove plans labels/markup from active patient UI only. No saved-data or question changes.
**Requirements:** Both opening modes; actual latest ten updates with DD.MM.YYYY dates; LV/EN/RU/UK; unchanged answers/progress/reports; preserve internal history/planning. User explicitly authorized implementation of this complete specification.

- [ ] Merge checked PR73 so its existing task reaches main; create one implementation branch from current main.
- [ ] Add regression coverage for concise dated history, retained detailed history, complete removal of plans and online/offline guidance/links; observe failure.
- [ ] Update footer and all catalogs. Preserve original dates/records and add one truthful current update. Align concise guide PDF opening instructions.
- [ ] Verify focused regressions, all locales, phone widths, keyboard access, existing answers/progress/reports and no answer network traffic; run full suite.
- [ ] Commit clean v0.2.19 source, build/verify package and inspect PDF. Archive18. Remove the completed existing TD entry only after verification and record attribution/evidence.
- [ ] Merge checked implementation PR; replace existing Drive pair and verify byte readback; publish matching guarded Pages through checked delivery record.
- [ ] Verify live bytes/UI/links, record final result/checkpoint and merge checked evidence PR.

Review focus: brief/detail dates stay aligned; separate same-day updates remain separate; no empty plans containers; links only navigate deliberately and preserve offline answering; old progress and report behavior remain unchanged.
