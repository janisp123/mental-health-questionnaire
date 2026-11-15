# Report review priority

Approved scope: order clinician report responses with internal 1–5 editorial review priorities, answer-aware rules and stable ties; keep linked context together. Same ordering feeds preview, print/PDF, HTML and text. Original questionnaire/branching/languages/answers/recovery and report inclusion remain intact. No diagnostic, severity, risk or triage score is computed/displayed; no new support-trigger or treatment rule. Every included response still needs clinician review. Priority configuration is an explicit ID/code table, separate from the frozen bank, requiring future clinical review.

Implementation decisions: complete 712-question coverage with base priorities for supporting context/current concerns; explicit coded response priorities for existing safety prompts, current vs historical self-harm/attempts, acute substance/neurological cues, reported functional impact and medication difficulties. Negative safety responses are retained without inheriting urgency simply from the topic. Uncertain/refused responses remain explicit, neutral review entries. Free text/medicine descriptions are not clinically interpreted. Existing condition parent families and named safety/history families stay together, using their highest included response priority for ordering only; original order breaks ties. Missing policy preserves legacy order for synthetic/older callers.

- [x] Write and observe failing priority/configuration and report regressions.
- [x] Add validated locale-independent metadata and pure report-only ordering module; align explanatory note/latest-ten notes in active locales and v0.2.13.
- [x] Verify response conservation, stable/contextual order, all locales, nonmutation, old progress, PDF/preview consistency; full checks and independent review.
- [x] Commit clean source, build/archive/check v0.2.13, checked PR merge and same-ID Drive update/readback.
- [ ] Merge exact delivery/checkpoint records. No landing-page changes or unrelated TD execution.

Review focus: inverted/protective questions; explicit No vs Yes; uncertainty/refusal; recent vs past events; sensitive histories/identity not automatically urgent; context-family precedence; free-text limits; no automatic clinical interpretation or aggregate score; unchanged report payloads and saved records. Values remain editorial draft, not clinically validated.

Independent review fix pass: corrected protective/safe-care direction, graded dependence, extreme-vs-severe impact and supporting-context absence inversions. The supporting-context finding was treated as the same priority-direction defect class and included in the consolidated fix. New explicit ID/code regressions were observed failing before corrections; full verification follows. Professional clinical validation remains pending.

Reviewed fixes: all focused regressions and the complete 39-check suite pass in memory mode after the consolidated correction. No second clinical-validation claim is made.

Delivery: PR #50 and exact Drive readback verified; final record integration proceeds through the protected checked-documentation PR. Priorities remain explicitly unvalidated editorial choices requiring professional clinical review.
