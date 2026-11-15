# Clinician-report review order

The internal 1–5 values are draft editorial ordering priorities, not validated clinical severity, risk, diagnostic or triage scores. They are never summed, displayed as patient ratings, or used to suppress answers, change advice, or change questionnaire navigation. Every included answer still requires clinician review. Professional review of the rules remains pending.

`src/questionnaire/report-priority.json` covers every question ID and answer code explicitly, independent of language. `tools/build_questionnaire.py` rejects missing/unknown IDs, mismatched codes, values outside integer 1–5, overlapping named groups, clinical weight metadata, and urgent-priority assignments to uncertainty/refusal codes. New questions require deliberate metadata review. A new translation using the same IDs/codes inherits the same order.

## Meaning and limits

| Value | Editorial purpose |
|---|---|
| 5 | Explicit current safety/help cue to review first |
| 4 | Serious reported concern or marked reported impact to review early |
| 3 | Current concern or answer needing clarification |
| 2 | Supporting history and context |
| 1 | Background, explicit absence or reassuring response |

Supporting medical/developmental/family/context questions generally start at 2; current concern topics at 3; basic background at 1. Free-text reasons and medicine records stay at 3 without interpreting their contents. Exact ID/code exceptions govern safety, medication difficulties, severe reported impact and temporal distinctions. Positive wellbeing and protective questions have explicit inverse handling. Uncertain/refused codes are kept at neutral review priority 3, not treated as affirmative danger or reassurance. A lower position does not establish safety, irrelevance or absence of illness. No clinical cut-off or total exists.

## Context and stable ordering

Only the previously included report entries are sorted. Existing condition-parent families and named current-safety/self-harm-episode/suicide-history families stay together. The highest included response positions a family; other responses within it are context, not equally severe findings. Original topic/question order breaks ties. Recent/history wording is retained verbatim. Missing/skipped/blank entries remain omitted under the existing report contract; all included negative, uncertain and refused responses remain. Preview, print/PDF, HTML and text use this one entry-order function. Progress records, original data and feedback order do not change. Callers without priority metadata retain the previous topic order.

## Important explicit distinctions

- Current suicidal intent/plan, inability to stay safe, current intent/preparation to harm others, immediate help and current safeguarding cues reuse existing explicit safety-prompt mappings for priority 5. Current thoughts/urges mapped to support are at 4; uncertainty is 3 and explicit denial 1. Protective-question No/Yes meaning is reversed where appropriate.
- Current severe alcohol-withdrawal symptoms (M15_19 B) precede historical severe withdrawal (M15_18 B). Acute neurological/current-help cues M30_13/M30_24/M30_25 B are explicitly prioritized. Substance-use categories, diagnosis histories, identity and unwanted intrusive thoughts are not automatically assigned priority 5.
- A suicide attempt within the past 24 hours (M06_09 A) has priority 5; other recent and remote options have separate explicit review values. Self-harm recency and past-month episodes are explicit context for review, not predicted suicide risk.
- Severe/very severe reported functional impact and selected medication difficulties have explicit code priorities. Positive wellbeing frequency is handled in its own direction, avoiding the assumption that every higher response code means worse health.

## Verification

Focused regressions cover all coded choices in all active locales, exact response-payload conservation, no mutation, descending priorities, stable/contextual order (including absent parent entries), protective inversions, history/recency, uncertainty/refusal and invalid metadata. Runtime checks exercise real preview/PDF order, old/current progress round trips, offline behavior and phone widths. Automated verification establishes implementation behavior; it cannot validate clinical usefulness or calibrate these draft editorial choices.
