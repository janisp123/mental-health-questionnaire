# Active development changelog — mental-health-questionnaire

**Active branch:** `develop`. Main and the historical Google Drive release remain untouched.
**Current build:** one self-contained offline HTML with all 48 modules and 712 original questions. Automated desktop Chromium checks pass. This is a technical-review build, not a release or clinical validation.
**Outstanding external checks:** actual Android Chrome use; human review of LV interface wording and EN/RU drafts; professional/clinical review. Do not mark those complete without evidence.
**History:** the prior pilot and full-build chronology is preserved in [CHANGELOG_HISTORY_2026-11-06.md](history/CHANGELOG_HISTORY_2026-11-06.md). Read it only when a task needs that history.

## 2026-11-06 · RUNTIME-MODULARITY-AND-FOCUSED-TESTS · IN_PROGRESS

**Goal:** make current project status unambiguous, separate runtime tests by behavior, and split shared runtime logic only along independently testable boundaries. Preserve the 48-module bank and single-file offline build.

**Baseline:** `d250271a83dfcb17799fdbf66f26bf416488722a` on `develop`; it matches the GitHub branch. Checklist commit: `5ef185a`.

**Verified baseline:** component workflow 42247708071 and full offline Chromium workflow 42247707973 passed at code commit `4d6ff92002b1b3a686954eaf95743b0d61c5f398`. Source integrity confirmed 48 modules/712 IDs; no physical Android check was run.

**Checklist:**

1. [DONE] Audit current source, test, and branch state.
2. [IN_PROGRESS] Replace pilot-first status with this active handoff and archive the previous chronology.
3. [TODO] Split runtime browser checks into focused synthetic-data cases.
4. [TODO] Extract query/model, answer-flow, and recovery behavior into tested modules.
5. [TODO] Add a focused browser layout check for CSS changes.
6. [TODO] Update architecture, file index, manifest, and CI routing as needed.
7. [TODO] Run the relevant GitHub checks and one full integration run after structural work.
8. [BLOCKED] Physical Android testing and human language/clinical review require a device or reviewers.

**Guardrails:** keep source questions, IDs, codes, conditions, and frozen references unchanged; preserve recovery compatibility; keep script and style order explicit in `src/app/build.json`; add no runtime dependencies. Work in small verified commits.

**Exact next action:** finish this changelog archive checkpoint, then build a small synthetic runtime fixture and use it to split the existing sequential browser journey by behavior.
