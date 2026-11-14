# Project-state evaluation and next-step plan

**Status:** Prepared; evaluation not started beyond the baseline readback below.
**Goal:** Establish what is working, what genuinely needs repair, what remains unverified and which three tasks should come next.
**Scope:** Adult, offline, non-diagnostic mental-health appointment preparation. English-only clinical-content review; technical consistency checks across all four active locales. No diagnostic or suicide-prediction claim.
**Method:** Reuse existing audits and executed evidence, then perform only checks needed to resolve current uncertainty. Evaluation does not itself authorize repairs, new languages, settings changes or publication.

## Confirmed starting point — 14 November 2026

- Main: `25bd39f5bfcd9eb4a73eb6d4f7bdde4d0ef417e1`; delivered version v0.2.6, LV/EN/RU/UK, 712 questions, 15 optional sections.
- Local-helpline instructions, M04_01 peak explanation and feedback delivery are already implemented in all four languages. Do not reopen them as unfinished work.
- Current package/Drive provenance: `MH_Public_version/manifest.json`, `project-manifest.json` and `docs/review/checks/2026-11-14-support-peak-drive-sync.json`. Downloaded files were verified byte-identical; stable IDs/sharing retained.
- All 34 maintained local scripts passed in labelled memory mode; product PR CI passed with real offline file opening. Latest main full workflow succeeded. These are technical checks, not clinical validation or physical-device evidence.
- Landing page is live with stable wording and links. Actual search indexing and AI suggestions are unverified.
- Main protection is active. Older package PR #23 is closed; PR #27 queues README download-link work and remains separate.
- Read first: AGENTS.md, docs/WORK_CHECKPOINT.md, docs/TD_LIST.md, docs/FEATURE_DEVELOPMENT.md, docs/LANGUAGE_STYLE_GUIDE.md and docs/RELEASE_POLICY.md. Preserve unrelated work and reassess this baseline if main moves.

## 1. Reconcile the project record

- [ ] Record exact current main/version, dirty or unsynchronized work, open PRs, latest checks, package hashes and actual Drive/site state. Reuse the existing byte-readback record unless a file changed or there is evidence of drift.
- [ ] Classify each backlog item as delivered, implementation pending, proposal awaiting decision, externally blocked, or verification pending. Do not treat an audit finding as an implemented fix.
- [ ] Extract remaining findings from the completed wording/effectiveness/security reviews; do not repeat the entire audits. Ask for a missing report only if the workspace copy cannot be recovered and existing records do not contain the needed detail.

Existing detailed workspace reports: `/workspace/scratch/TD_REVIEW_2026-11-14.md`, `/workspace/scratch/REPOSITORY_SECURITY_REVIEW_2026-11-14.md`, and `/workspace/scratch/english-clinical-review/VERIFICATION_PLAN.md`. They are supporting work artifacts, not proof that their recommendations shipped. Carry concise verified findings into the final durable evaluation report; do not publish private correspondence or patient data.

**Output:** One current-state inventory, with links to evidence and an explicit status for every task. Keep the checkpoint short; put history in the changelog.

## 2. Verify security and release reliability

- [ ] Recheck the known `pypdf==6.10.0` advisory finding against current official advisories; identify an appropriate fixed release. Establish actual exposure: this is PDF test tooling, not a public PDF-upload service or part of the offline application. A high package severity does not automatically mean a critical deployed-site defect.
- [ ] Confirm whether Dependabot alerts remain disabled and list any owner-only actions. Mark inaccessible secret-scanning/account settings unverified; do not infer they are safe or disabled from HTTP 403.
- [ ] Inspect workflow permissions, dependency/action pinning, branch rules and rollback references. Do not rotate credentials or change protections merely because a check is unavailable.
- [ ] Verify that source, downloadable artifacts and update notes agree, older progress files remain supported and rollback is preserved. Exercise save/restore/report generation if changed or unsupported by current evidence.

**Output:** Confirmed issues versus hardening suggestions, practical exposure, urgency, exact affected dependency/file and a separately proposed repair. No dependency or settings update during evaluation.

## 3. Assess practical user and clinician value

Use synthetic data, not real health answers. Prioritize short, representative sessions rather than completing all 712 questions repeatedly.

- [ ] Follow download/open, choose a small section set, answer/skip/backtrack, save progress, close/reopen/restore, change language and prepare a partial PDF. Check whether the next step is understandable without developer knowledge.
- [ ] Reproduce the previously observed report denominator problem: selecting one section can still produce a much larger count labelled "Selected questions". Identify the correct count/label contract without discarding earlier answers from deselected sections.
- [ ] Check inconsistent "completed" counts across Results and PDF, and whether omitted/skipped items could be mistaken for negative answers. Existing `omissionNote` is a candidate for a minimal clarification, not an automatic fix.
- [ ] Verify question focus after navigation/autoadvance with keyboard and, where available, a screen reader. Earlier review found missing focus handling; user impact needs focused execution, not a claim based solely on CSS.
- [ ] Inspect a representative medication/long-answer PDF visually for clipping, missing context and scanability. Confirm feedback remains separate from clinical answers.
- [ ] Record physical-phone downloaded-file results only if a real named device/browser is actually tested. Simulated widths do not replace those results.

**Output:** Verified defects and observed friction, with screenshots/reproductions where useful. Separate inferred accessibility risks and untested devices. Leave already-sufficient flows alone.

## 4. Evaluate English clinical coverage and wording

Use the existing English clinical verification plan rather than starting another whole-bank review. It inventories 712 questions and identifies 161 in the direct target modules.

- [ ] Map relevant English IDs/choices/time windows/conditions to authoritative assessment guidance for depression, anxiety, bipolar presentations, ADHD, autism, medication/substance problems, self-harm and suicidality.
- [ ] Check developmental onset, episode timing, impairment, context, overlap and alternative explanations; verify that negative/uncertain/skipped gate answers cannot create misleading reassurance.
- [ ] Reuse the earlier shortlist of approximately 20 wording candidates. M04_01 is already clarified. Prioritize actual ambiguity or answer gaps, including current-versus-historical wording, recency boundaries and incomplete answer choices; do not rewrite subjective language for style alone.
- [ ] Distinguish collecting useful history from validated screening or diagnosis. No questionnaire-only assessment establishes presence/absence of these conditions or predicts future suicide. A qualified clinician must review proposed changes to clinical meaning.
- [ ] List any standardized instruments or reuse/translation permissions needing verification. Familiar wording alone does not establish valid instrument administration.

**Output:** A concise English coverage matrix and prioritized exact change proposals, with existing IDs, evidence, missing information and rationale. No clinical edits during evaluation. Do not promise sensitivity/specificity without an appropriate validation study.

## 5. Check localization maintainability

- [ ] Reuse existing catalog/source/ID/code/placeholder parity and recovery evidence for LV/EN/RU/UK. Review clinically only in English at this stage; check other locales technically and visually where affected.
- [ ] Record which existing translations and safety wording lack fluent human/clinical review. AI review and passing tests do not supply that review.
- [ ] For each proposed future change, classify it as meaning-preserving help, wording change, new choice/question, or retirement. Never reuse IDs/codes for a new meaning or silently reinterpret saved answers.
- [ ] Define targeted four-language translation/review and explicit migration requirements only for the changes actually recommended. Preserve frozen originals and tested presentation boundaries.

**Output:** A safe-change checklist attached to each proposed repair, not a new translation project. No fifth language until its purpose, reviewer availability and ongoing maintenance are justified.

## 6. Assess discovery and GitHub interest

- [ ] Check the real landing page, canonical, sitemap, download paths, ordinary crawler restrictions and factual positioning. Reuse current good results unless deployment changed.
- [ ] Separate page accessibility from actual indexing. Record Search Console/Bing ownership or index-request steps requiring the owner; simulated crawler requests are not actual crawler visits.
- [ ] Observe a small set of realistic English searches, such as appointment-preparation questions and offline questionnaires. Label each service/query/date/result; do not treat one generated AI answer as a stable ranking measurement.
- [ ] Review README clarity, working screenshots, obvious download path, contribution instructions and code/content reuse terms. A public repository is not automatically licensed open source; licensing decisions belong to the owner.
- [ ] Measure available repository visits, referrers, stars and useful feedback without collecting questionnaire answers. Record inaccessible traffic metrics as unavailable. No invented visitor-to-star conversion estimates.
- [ ] Consider a small Brazilian Portuguese project-summary experiment only after core quality findings are addressed. Compare genuine interest/reviewer availability with Spanish reach before translating all questions. Language expansion is a hypothesis, not a stars guarantee.

**Output:** A short discovery/positioning report and an evidence-backed decision: improve existing presentation, perform an indexing step, test a localized summary, or defer expansion. No spam, fabricated endorsements or ranking promises.

## 7. Choose the next three tasks

Create one table with: finding, current evidence, verified/inferred status, user/security consequence, benefit, effort, dependencies, reviewer/owner action and recommended order.

Use these decision rules:

1. Immediate priority for a verified serious safety/privacy problem or broken core journey, if found. Do not invent a critical issue to fill the category.
2. Next, small confirmed repairs that improve report accuracy, accessibility or dependency safety.
3. Then, targeted wording changes with clinical approval and indexing/presentation improvements supported by evidence.
4. Defer new languages, hosting changes and speculative features unless demonstrated demand outweighs maintenance cost.

Provisional candidates to evaluate first: the known PDF-tooling vulnerability/dependency alerts, report counting and keyboard/focus behavior. This is a starting hypothesis, not authorization to implement all three. Country-neutral help and peak clarification are complete.

**Final decision:** State readiness as Ready / Ready after targeted fixes / Significant work required / Insufficient evidence. Name exactly three proposed next tasks, explain why they outrank alternatives and state what remains blocked. Do not equate technical-review readiness with clinical validation.

## Recordkeeping and later implementation

Deliver the evaluation as `docs/review/YYYY-MM-DD-project-state-review.md` with concise evidence links and limitations. Update the checkpoint, changelog and TD through the protected PR workflow once authorized; preserve chronological history and never mark a proposal done.

For an approved repair: write a focused failing regression when warranted, implement the smallest change, verify relevant locale/branching/recovery/report behavior, run required checks and integrate only a checked PR. Product-byte changes need a new package/version, four-language notes, archive/rollback, deliberate distribution and downloaded-byte verification. Repository-only evaluation/doc edits must not trigger an unchanged Drive upload.

**Stop point:** Present the evaluation and ranked next-three-task recommendation before implementing recommendations. This plan creates no automatic background work or deployment.
