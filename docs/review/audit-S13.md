# S13 translation audit

Compared every Latvian question, time label, help text and answer option in S13 with the English and Russian drafts at `85f4332`.

| Module | Questions | Answer labels per language | EN fields corrected | RU fields corrected |
| --- | ---: | ---: | ---: | ---: |
| 31 | 20 | 112 | 24 | 37 |
| 32 | 50 | 311 | 35 | 87 |

The source audit identified five invalid dotted keys in three Russian entries. M32_36 and M32_42 now display the intended options for codes E and F. M32_40 now displays the intended option for code B. The five invalid keys were removed.

| Question | Language | Field(s) | Reason |
| --- | --- | --- | --- |
| M31_01 | EN | `help` | Makes clear that routine childcare counts even without illness or disability and keeps the instruction to omit names. |
| M31_01 | EN | `title` | Makes the recurring activity read naturally. The time label specifies the current period. |
| M31_01 | RU | `choices.C` | Preserves “I’m not sure” as distinct from “hard to say.” |
| M31_01 | RU | `title` | Applies formal singular address per the language guide. |
| M31_02 | RU | `choices.C` | Preserves regular help with some daily activities in idiomatic Russian. |
| M31_02 | RU | `choices.D` | Preserves daily care and the breadth of activities needing support. |
| M31_02 | RU | `title` | Applies formal singular address per the language guide. |
| M31_03 | RU | `choices.C` | Preserves “I’m not sure” as distinct from “hard to say.” |
| M31_03 | RU | `title` | Restores the degree of difficulty and clarifies that this concerns the respondent’s own medical visits. |
| M31_04 | RU | `choices.C` | Preserves “I’m not sure” as distinct from “hard to say.” |
| M31_04 | RU | `title` | Applies formal singular address per the language guide. |
| M31_05 | RU | `choices.C` | Preserves “I’m not sure” as distinct from “hard to say.” |
| M31_05 | RU | `title` | Applies formal singular address per the language guide. |
| M31_06 | RU | `choices.C` | Preserves “I’m not sure” as distinct from “hard to say.” |
| M31_06 | RU | `title` | Applies formal singular address per the language guide. |
| M31_07 | RU | `choices.C` | Preserves “I’m not sure” as distinct from “hard to say.” |
| M31_07 | RU | `title` | Restores inability to rest or take time for oneself. |
| M31_08 | EN | `title` | Restores caregiving duties as the cause and the sense that continuing is no longer possible. |
| M31_08 | RU | `choices.C` | Preserves “I’m not sure” as distinct from “hard to say.” |
| M31_08 | RU | `title` | Restores caregiving duties as the cause. |
| M31_09 | EN | `title` | Restores the full scope of the safety question, which includes any person needing care. |
| M31_09 | RU | `choices.C` | Preserves “I’m not sure” as distinct from “hard to say.” |
| M31_09 | RU | `title` | Restores the full scope of the safety question, which includes any person needing care. |
| M31_10 | RU | `choices.C` | Preserves “I’m not sure” as distinct from “hard to say.” |
| M31_10 | RU | `title` | Uses the idiomatic verb for facing threats or violence while retaining the current home setting. |
| M31_11 | RU | `choices.C` | Preserves “I’m not sure” as distinct from “hard to say.” |
| M31_12 | RU | `title` | Applies formal singular address per the language guide. |
| M31_13 | EN | `title` | Clarifies both circumstances and keeps caregiving broader than duties. |
| M31_13 | RU | `title` | Keeps caregiving circumstances broader than duties. |
| M31_14 | EN | `choices.C` | Makes the two uncertainty responses grammatical. |
| M31_14 | EN | `help` | Keeps the qualification and presents declining the question as a choice. |
| M31_14 | RU | `title` | Applies formal singular address per the language guide. |
| M31_15 | EN | `choices.C` | Makes the two uncertainty responses grammatical. |
| M31_15 | EN | `help` | Clarifies whose safety supervision protects and that the follow-up asks about reasons. |
| M31_15 | EN | `title` | Asks whether care was missing in neutral language. |
| M31_15 | RU | `help` | Clarifies the purpose of supervision and that the follow-up asks about reasons. |
| M31_15 | RU | `title` | Describes the missing care without adding any implication of legal guardianship or deliberate withholding. |
| M31_16 | EN | `choices.C` | Clarifies whose safety supervision protects and uses ordinary words for mobility assistance. |
| M31_16 | EN | `choices.F` | Makes the two uncertainty responses grammatical. |
| M31_16 | EN | `title` | Uses plain wording for missing care. |
| M31_16 | RU | `choices.C` | Clarifies that supervision keeps the person safe. |
| M31_16 | RU | `choices.D` | Uses the ordinary expression for needed health care. |
| M31_16 | RU | `title` | Asks what care was missing in neutral language. |
| M31_17 | EN | `choices.F` | Identifies the care recipient in any setting. |
| M31_17 | EN | `choices.I` | Makes the two uncertainty responses grammatical. |
| M31_17 | RU | `choices.E` | Restores the first-person lack of knowledge. |
| M31_18 | EN | `choices.C` | Makes the two uncertainty responses grammatical. |
| M31_18 | EN | `title` | Clarifies that help is needed to provide care to the recipient. |
| M31_18 | RU | `title` | Clarifies that help is needed to provide care and uses ordinary wording for someone receiving care. |
| M31_19 | EN | `choices.C` | Preserves having a thought, which is distinct from deliberating about acting. |
| M31_19 | EN | `choices.E` | Makes the two uncertainty responses grammatical. |
| M31_19 | EN | `help` | Preserves the distinction between thoughts, wishes and intent, the exclusion for agreed medical symptom relief, and the permission to omit the type of harm. |
| M31_19 | RU | `help` | Clarifies the exclusion for agreed medical measures and the permission to omit the type of harm. |
| M31_19 | RU | `title` | Applies formal singular address per the language guide. |
| M31_20 | EN | `choices.C` | Identifies the respondent’s experience of the thought as what varied. |
| M31_20 | EN | `choices.E` | Makes the two uncertainty responses grammatical. |
| M31_20 | EN | `help` | Clarifies what the respondent should consider and how this differs from the separate questions on intent and preparation. |
| M31_20 | EN | `title` | Keeps the follow-up linked to the person in the previous question. |
| M31_20 | RU | `choices.C` | Preserves how the respondent experienced the thought, including mixed feelings. |
| M31_20 | RU | `help` | Restores the focus on experiencing this particular thought. |
| M31_20 | RU | `title` | Keeps the referent from the preceding question and frames the experience as having a thought. |
| M32_01 | RU | `title` | Makes the question apply to respondents regardless of whether they have a partner. |
| M32_03 | EN | `title` | Makes the “With…” choices answer the question directly. |
| M32_03 | RU | `title` | Applies formal singular address per the language guide. |
| M32_04 | RU | `title` | Applies formal singular address per the language guide. |
| M32_05 | RU | `choices.C` | Preserves “I’m not sure” as distinct from “hard to say.” |
| M32_05 | RU | `title` | Applies formal singular address per the language guide. |
| M32_06 | RU | `choices.C` | Preserves regular help with some daily activities in idiomatic Russian. |
| M32_06 | RU | `choices.D` | Preserves daily care and the breadth of activities needing support. |
| M32_06 | RU | `title` | Applies formal singular address per the language guide. |
| M32_07 | RU | `title` | Uses the correct preposition for difficulties with health or development. |
| M32_08 | RU | `choices.C` | Preserves “I’m not sure” as distinct from “hard to say.” |
| M32_08 | RU | `title` | Applies formal singular address per the language guide. |
| M32_09 | RU | `title` | Applies formal singular address per the language guide. |
| M32_10 | RU | `title` | Applies formal singular address per the language guide. |
| M32_11 | RU | `title` | Applies formal singular address per the language guide. |
| M32_12 | RU | `title` | Applies formal singular address per the language guide. |
| M32_13 | RU | `choices.D` | Distinguishes a residential care setting from a guardianship authority. |
| M32_13 | RU | `choices.E` | Makes the option answer who raised the respondent during different periods. |
| M32_13 | RU | `title` | Applies formal singular address per the language guide. |
| M32_14 | RU | `choices.C` | Preserves “I’m not sure” as distinct from “hard to say.” |
| M32_14 | RU | `title` | Applies formal singular address per the language guide. |
| M32_15 | RU | `time`, `title` | Applies formal singular address per the language guide. |
| M32_16 | EN | `choices.D` | Covers forms of study beyond school or higher education. |
| M32_16 | RU | `choices.C` | Uses the established term for self-employment. |
| M32_16 | RU | `title` | Applies formal singular address per the language guide. |
| M32_17 | RU | `title` | Applies formal singular address per the language guide. |
| M32_18 | EN | `title` | Fits the separate 28-day reference period. |
| M32_18 | RU | `title` | Restores the respondent’s perspective and fits the separate 28-day reference period. |
| M32_19 | EN | `title` | Uses the direct expression for insufficient money. |
| M32_20 | RU | `choices.C` | Preserves “I’m not sure” as distinct from “hard to say.” |
| M32_20 | RU | `title` | Applies formal singular address per the language guide. |
| M32_21 | EN | `title` | Fits the separate 28-day reference period. |
| M32_21 | RU | `choices.B`, `choices.C`, `choices.D`, `choices.E` | Counts affected days without implying an unbroken stretch. |
| M32_21 | RU | `title` | Fits the separate 28-day reference period and states the effects directly. |
| M32_22 | RU | `choices.C` | Preserves “I’m not sure” as distinct from “hard to say.” |
| M32_22 | RU | `title` | Applies formal singular address per the language guide. |
| M32_23 | RU | `choices.C` | Preserves “I’m not sure” as distinct from “hard to say.” |
| M32_23 | RU | `title` | Restores whose stress is asked about and uses plain wording for a police matter. |
| M32_24 | RU | `choices.C` | Preserves “I’m not sure” as distinct from “hard to say.” |
| M32_24 | RU | `title` | Uses idiomatic wording for the effects of a crime the respondent experienced or witnessed. |
| M32_25 | RU | `choices.C` | Preserves “I’m not sure” as distinct from “hard to say.” |
| M32_25 | RU | `title` | Applies formal singular address per the language guide. |
| M32_26 | EN | `title` | Restores “currently” as a qualifier for which event the respondent wishes to discuss. |
| M32_26 | RU | `time` | Uses an idiomatic phrase for time elapsed since the event. |
| M32_26 | RU | `title` | Applies formal singular address per the language guide. |
| M32_27 | RU | `choices.B`, `choices.C`, `choices.D`, `choices.E` | Counts affected days without implying an unbroken stretch. |
| M32_27 | RU | `title` | Asks for days with impaired well-being or disruption of daily life in the 28-day period. |
| M32_28 | RU | `choices.C` | Preserves “I’m not sure” as distinct from “hard to say.” |
| M32_28 | RU | `title` | Applies formal singular address per the language guide. |
| M32_29 | RU | `choices.C` | Preserves “I’m not sure” as distinct from “hard to say.” |
| M32_29 | RU | `title` | Applies formal singular address per the language guide. |
| M32_30 | RU | `title` | Restores the relation between drinking problems and their effects on the person or others. |
| M32_31 | EN | `time` | Preserves the age boundary and the choice to omit names and details or skip the question. |
| M32_31 | EN | `title` | Makes the caregiving sense of “care” clear. |
| M32_31 | RU | `title` | Clarifies the relationship between substance use and difficulties at home or in caregiving. |
| M32_32 | EN | `time` | Preserves the age boundary and the choice to omit names and details or skip the question. |
| M32_32 | RU | `title` | Applies formal singular address per the language guide. |
| M32_33 | EN | `time` | Preserves the age boundary and the choice to omit names and details or skip the question. |
| M32_33 | RU | `title` | Uses a transitive verb that fits the existing accusative options. Preserves the threshold of one episode and optional details. |
| M32_34 | EN | `choices.B` | Preserves both safety and regularity. |
| M32_34 | EN | `time` | Preserves the age boundary and the choice to omit names and details or skip the question. |
| M32_34 | EN | `title` | Restores the sense of being able to approach the adult without fear. |
| M32_34 | RU | `choices.B` | Preserves the single negation of being able to approach the adult both safely and regularly. |
| M32_34 | RU | `title` | Uses an idiomatic expression for approaching the adult without fear. |
| M32_35 | EN | `choices.C` | Makes the two uncertainty responses grammatical. |
| M32_35 | EN | `time` | Clarifies that earlier workplaces and study settings count within the six-month period. |
| M32_35 | RU | `time` | Clarifies that earlier workplaces and study settings count within the six-month period. |
| M32_35 | RU | `title` | Applies formal singular address per the language guide. |
| M32_36 | EN | `choices.E` | Includes all study settings. |
| M32_36 | EN | `choices.F` | Restores the plural in the source option. |
| M32_36 | RU | `choices.A` | Restores name-calling as a specific example. |
| M32_36 | RU | `choices.D` | Clarifies that this option concerns social exclusion. |
| M32_36 | RU | `choices.E`, `choices.F` | Moves the intended correction into the displayed option and removes the invalid dotted key. |
| M32_36 | RU | `choices.H` | Includes online mistreatment beyond stalking. |
| M32_36 | RU | `title` | Applies formal singular address per the language guide. |
| M32_37 | RU | `title` | Applies formal singular address per the language guide. |
| M32_38 | EN | `title` | Explicitly covers ended and ongoing situations. |
| M32_39 | EN | `choices.C` | Makes the two uncertainty responses grammatical. |
| M32_39 | RU | `title` | Clarifies that the group supports the other person. |
| M32_40 | RU | `choices.B` | Moves the intended correction into the displayed option and removes the invalid dotted key. |
| M32_40 | RU | `choices.F` | Keeps the broader education role. |
| M32_40 | RU | `title` | Applies formal singular address per the language guide. |
| M32_41 | EN | `choices.C` | Makes the two uncertainty responses grammatical. |
| M32_41 | RU | `title` | Uses correct cases and makes clear the respondent is the one acting. |
| M32_42 | EN | `choices.E` | Includes all study settings. |
| M32_42 | EN | `choices.F` | Restores the plural in the source option. |
| M32_42 | RU | `choices.A` | Restores name-calling as a specific example. |
| M32_42 | RU | `choices.D` | Clarifies that this option concerns social exclusion. |
| M32_42 | RU | `choices.E`, `choices.F` | Moves the intended correction into the displayed option and removes the invalid dotted key. |
| M32_42 | RU | `choices.H` | Includes online mistreatment beyond stalking. |
| M32_42 | RU | `title` | Applies formal singular address per the language guide. |
| M32_43 | RU | `title` | Applies formal singular address per the language guide. |
| M32_44 | EN | `choices.C` | Makes the two uncertainty responses grammatical. |
| M32_44 | RU | `title` | Keeps the reference to position and clarifies who received support from the group. |
| M32_45 | EN | `choices.C` | Makes the two uncertainty responses grammatical. |
| M32_45 | EN | `title` | Includes all work and study settings within the six-month period. |
| M32_45 | RU | `title` | Includes all work and study settings within the six-month period. |
| M32_46 | EN | `choices.C` | Makes the two uncertainty responses grammatical. |
| M32_46 | EN | `time` | Makes the under-18 boundary explicit. |
| M32_46 | RU | `title` | Removes the added requirement that school exclusion be deliberate. |
| M32_47 | EN | `choices.C` | Makes the two uncertainty responses grammatical. |
| M32_47 | EN | `time` | Makes the under-18 boundary explicit. |
| M32_47 | EN | `title` | Uses retrospective tense and retains the broad meaning of exclusion. |
| M32_47 | RU | `title` | Removes the added requirement of deliberate exclusion and fixes the parallel verb construction. |
| M32_48 | RU | `title` | Restores “currently” and the alternatives among the areas affected. |
| M32_49 | EN | `choices.C` | Makes the two uncertainty responses grammatical. |
| M32_49 | EN | `title` | Uses natural wording for whether the same treatment is ongoing. |
| M32_49 | RU | `title` | Applies formal singular address per the language guide. |
| M32_50 | EN | `choices.C` | Makes the two uncertainty responses grammatical. |
| M32_50 | EN | `title` | Includes places of study beyond schools. |
| M32_50 | RU | `title` | Includes places of study beyond schools and uses natural wording for feeling physically safe. |
| M32_51 | EN | `choices.C` | Makes the two uncertainty responses grammatical. |
| M32_51 | RU | `title` | Uses idiomatic wording for being able to seek help safely. |

## Human review priorities

- Confirm the breadth of M31_09, which asks about the safety of a child or other person needing care. M31_18 concerns the respondent’s care recipients. Its Latvian source leaves open who should help provide the care.
- Confirm the distinction in M31_19–20 among wishing for an end to suffering, wishing for death, having a thought about causing death, and wanting to act. The Latvian exclusion refers to agreed medical symptom relief and leaves open who must agree.
- Confirm terminology for childhood residential care in M32_13 and for exclusion and harassment in work or educational settings in M32_35–50.
- Confirm the emphasis of Latvian “droši” in M32_34. It can mean being able to approach an adult safely, with confidence, or both.

The comparison with the starting Git blobs verified all 70 Latvian entries and their order, conditions, codes, answer status mappings and other nontranslation fields. English and Russian remain drafts pending human language and clinical review.
