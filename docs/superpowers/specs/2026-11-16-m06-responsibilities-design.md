# M06 hypothetical responsibilities question

Add one optional independent question, M06_25, to the existing M06 module and its current user section immediately after M06_24. Separate additive catalog and narrow build hook; no rewrite of frozen M06 source or app runtime.

English meaning: If nobody depended on you and you had no family or other responsibilities, how would that affect the likelihood of you considering ending your life? Choices: more likely / less likely / no change / does not apply / unsure / prefer not to answer. Clarify it is hypothetical, does not mean these circumstances will change, and does not replace questions about current thoughts and safety. LV/EN/RU/UK equivalents; formal address per style guide. Applicable now as a hypothetical; no new diagnostic or validated-assessment claim.

Use the existing editorial 1–5 report order as the requested weight: A (more likely) = 4; B–F = 3, default 3. Keep with current-safety report context. Hypothetical less likely/no change is not reassurance about current safety. Never sum/display a score or introduce a new emergency trigger. Existing urgent questions/support remain unchanged.

## Approaches and modularity
Selected: separate one-question catalog containing its translations and report metadata, loaded by a narrow build function into existing M06. Editing the frozen module would destroy reference parity; restructuring the runtime is unnecessary. User approved adding to existing M06 with a distinct ID and requested a weight. Exact wording, answer codes and conservative editorial values are implementation decisions within that request.

Existing IDs/codes/conditions, section mapping and recovery schema remain unchanged. Current application imports old progress missing M06_25. Old application versions cannot necessarily import a newer backup containing the new ID: rollback must retain an explicit reader/migration or require keeping the newer export; never silently discard that response. Test that disabling the additive hook reproduces the prior question/priority bundle without other changes.

Release v0.2.16 through checked PR, clean-source HTML/PDF package, Drive byte readback and exact hosted parity. Update notes all active catalogs, counts/README/landing/active docs together. Technical verification only; human clinical/translation and physical-device review remain pending.
