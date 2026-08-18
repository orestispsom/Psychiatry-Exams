# Q11–Q19 Targeted Current Verification Handoff

Status: READY_FOR_CURRENT_VERIFICATION

Purpose: perform only the minimum current-authoritative checks needed to update the existing Oxford batch map for Q11–Q19. This is **not** a broad research assignment and must not recreate Q12-style literature review depth.

## Inputs

Read only:

1. `oral/100-crucial-questions/attempts/011.md` — Q11–Q19 wording.
2. `oral/100-crucial-questions/answers/source-packets/Q011-Q019-oxford-map.md` — primary exam/base-source map.
3. `oral/100-crucial-questions/answers/source-packets/Q012-contemporary.md` only where it already resolves a Q11–Q13 point and avoids duplicate work.
4. `oral/100-crucial-questions/internal/board-fact-anchors.yml` — psychosis/clozapine anchors only.
5. `oral/100-crucial-questions/internal/answer-production/agent-prompts.md` — current Targeted Current Verifier rules.

Do not read local textbooks. Do not write model answers.

## Governing method

For each listed vulnerable point below:

- inspect the best current authoritative source;
- return one of `KEEP`, `UPDATE`, `ADD`, `EXAM_CURRENT_SPLIT`, `UNRESOLVED`;
- state the current fact/recommendation in concise original wording;
- cite the exact source actually inspected;
- stop once the listed point is resolved.

Do **not** research the entire question.
Do **not** maximise source count.
Do **not** generate epidemiology or mechanisms unless specifically requested below.
Do **not** reproduce DSM criterion text.

Preferred source logic:

- classification: WHO ICD-11 first where adequate; DSM-5-TR only for a genuinely DSM-specific distinction;
- treatment: current major schizophrenia/psychosis guideline(s), using one strong guideline where possible;
- TRS/clozapine: current consensus/guideline plus current prescribing/regulatory sources for monitoring/safety;
- smoking/infection/clozapine: current prescribing/regulatory or high-authority pharmacology source;
- scientific/prognostic claims: one strong recent review/meta-analysis only if the Oxford framing appears materially dated.

## Work package A — Q11 + Q13

### Q11. First-episode psychosis approach + cannabis follow-up

Verify only:

1. Current first-episode psychosis diagnostic approach: first episode psychosis is a presentation, not automatically schizophrenia.
2. Current classification logic for substance/medication-induced psychotic disorder versus primary psychotic disorder.
3. Cannabis-specific points that materially help distinguish causation/precipitation from coincidental use, including the importance of temporal relationship, persistence after cessation, prior symptoms, family/history/context, and whether current guidance gives any specific observation period or cautions against rigid timing rules.
4. Whether routine neuroimaging is recommended in uncomplicated first-episode psychosis or only when clinically indicated.
5. Any current high-value early-management point that Oxford 2017 clearly misses and that could realistically enter a 1–2 page Q11 answer.

### Q13. Schizophrenia vs schizoaffective vs mood disorder with psychotic features

Verify only:

1. Current ICD-11 distinction between schizophrenia, schizoaffective disorder and mood disorder with psychotic symptoms.
2. Whether current schizoaffective diagnosis still depends on psychosis occurring outside a mood episode, and how ICD-11 versus DSM-5-TR differ if materially relevant to an oral exam.
3. Current duration/longitudinal logic only to the extent it discriminates these three diagnoses.

Do not expand into the full schizophrenia-spectrum differential.

## Work package B — Q14–Q17

### Q14. Neurobiology

Verify only whether these Oxford pillars remain defensible as current high-level teaching:

- polygenic architecture + gene–environment interaction;
- neurodevelopmental model;
- increased presynaptic/striatal dopamine synthesis or release as a robust finding;
- glutamatergic/NMDA hypotheses as supported but not a settled singular mechanism;
- structural/functional connectivity abnormalities as group-level, non-diagnostic findings;
- cannabis/urbanicity/migration/obstetric or developmental exposures as risk associations rather than deterministic causes.

Return only material corrections or one major omission. No exhaustive neuroscience review.

### Q15. Prognosis

Verify only:

- major robust poor-prognosis factors relevant to a viva answer;
- duration of untreated psychosis as a prognostic association;
- functional versus symptomatic recovery distinction;
- current broad mortality/suicide framing only if Oxford's figures are materially outdated;
- sex/age-of-onset pattern only if worth retaining as a board fact.

Do not compile a new prognostic meta-analysis.

### Q16. Acute schizophrenia treatment

Verify current recommendations for:

- initial antipsychotic choice and shared decision-making;
- oral antipsychotic trial principles;
- role of benzodiazepines/rapid tranquillisation only where relevant to acute agitation rather than routine schizophrenia treatment;
- whether a 2-week early-response rule should influence switching or is too simplistic for the final answer;
- role/timing of psychosocial intervention in the acute phase;
- any current recommendation about first-episode dosing or avoiding unnecessary polypharmacy.

### Q17. Long-term management

Verify current recommendations for:

- maintenance antipsychotic treatment after first episode and after recurrent illness;
- duration of maintenance treatment: give current guidance and uncertainty, not one universal number if guidelines differ;
- LAI role and whether it is only for poor adherence or also a preference/relapse-prevention option;
- routine metabolic/physical-health monitoring;
- psychosocial interventions with strongest guideline support;
- management framing for persistent negative/cognitive symptoms;
- Q17a: secondary causes of negative-looking symptoms that should be excluded before calling them primary negative symptoms.

## Work package C — Q18 + Q19

This package receives the most rigorous verification because exact errors could be clinically consequential.

### Q18. Treatment-resistant schizophrenia

Verify:

1. Current operational definition of TRS.
2. What constitutes an adequate antipsychotic trial: dose, duration and adherence/exposure principles.
3. Number of failed adequate trials required before clozapine is indicated.
4. Main causes of pseudoresistance that must be excluded: non-adherence, inadequate dose/duration, substance use, diagnostic error, pharmacokinetic issues, etc.
5. Whether plasma-level confirmation or other exposure verification is recommended before declaring TRS.

Prefer current consensus/guideline definitions rather than Oxford-era wording.

### Q19. Clozapine

Verify only the high-yield material needed for a specialist viva answer and its board-fact block:

1. Current indications.
2. Current haematological initiation/continuation/interruption framework relevant to Greece/EU or broadly applicable practice; flag jurisdictional differences rather than importing a US-only rule.
3. Current blood-monitoring schedule if there is a stable applicable standard; identify major jurisdictional variation if present.
4. Myocarditis recognition/monitoring principles.
5. Severe constipation/gastrointestinal hypomotility and ileus risk.
6. Seizure risk in broad practical terms; exact dose-dependent percentages only if genuinely necessary.
7. Metabolic, sedation and hypersalivation risks only at viva-relevant level.
8. Smoking/CYP1A2 interaction: effect of stopping/restarting smoking on clozapine exposure.
9. Infection/inflammation and pneumonia: effect on clozapine metabolism/toxicity and immediate clinical implications.
10. Interruption/restart: when re-titration is needed and the safe restart principle.
11. Role of clozapine plasma levels in non-response, suspected toxicity, smoking change, infection or adherence uncertainty.
12. Q19a specifically: pneumonia + abrupt smoking cessation — concise expected problem and action priorities.

Do not generate a full clozapine monograph.

## Output format

Write exactly one file:

`oral/100-crucial-questions/answers/source-packets/Q011-Q019-current-verification.md`

Use this structure:

```markdown
# Q11–Q19 Current Verification Delta

## A. Q11 + Q13
| Question | Point | Decision | Current concise finding | Source |

## B. Q14–Q17
| Question | Point | Decision | Current concise finding | Source |

## C. Q18 + Q19
| Question | Point | Decision | Current concise finding | Source |

## Board-fact anchors resolved
- anchor → concise verified answer → source

## Exam/current splits worth preserving
- only genuine differences

## Unresolved items
- only items that still block an answer brief

## Sources actually inspected
- exact guideline/regulatory/review titles and relevant sections
```

## Output limit

Target **2,500–4,500 words for the entire Q11–Q19 verification file**.

If the task is trending longer, compress rather than widening scope.

## Completion gate

Return `BATCH_CURRENT_READY` only if:

- every listed vulnerable point has `KEEP`, `UPDATE`, `ADD`, `EXAM_CURRENT_SPLIT`, or `UNRESOLVED`;
- Q18/Q19 exact safety/treatment claims are supported by current authoritative sources;
- no broad topic reconstruction was performed;
- no final model-answer prose was written;
- the file was committed and re-fetched/verified.
