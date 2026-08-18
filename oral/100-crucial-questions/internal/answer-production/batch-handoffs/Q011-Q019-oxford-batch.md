# Q11–Q19 Lean Oxford Batch Handoff

Status: CURRENT BATCH WORK ORDER
Target: Greek Adult Psychiatry specialist-board model-answer production
Primary source: **Shorter Oxford Textbook of Psychiatry, 7th ed. / 2017 exam edition**

## Goal

Create **one reusable schizophrenia/psychosis chapter map** that supports Q11–Q19 without rereading the same Oxford material nine times.

Do not write model answers. Do not perform current-guideline research. Do not open multiple textbooks for confirmation.

## Reuse first

Before opening Oxford, read:

`oral/100-crucial-questions/answers/source-packets/Q012-local.md`

That file already contains a detailed extraction of Oxford Shorter Ch. 11 for:

- clinical picture;
- diagnosis/classification;
- schizophrenia-like disorders and differential diagnosis;
- cognition;
- first-rank symptoms;
- classic subtypes;
- comorbidity;
- the opening epidemiology anchors.

**Do not re-extract those sections. Reuse them.**

The Q12 packet explicitly did **not** read these later Ch. 11 sections:

- aetiology;
- neurobiology;
- neurodevelopmental model;
- course and prognosis;
- treatment;
- management.

Those are the main sections to retrieve now.

## Questions to support

### Q11 — First-episode psychosis case
**A 23-year-old presents with persecutory ideas, auditory hallucinations and social withdrawal. How would you approach the case?**
- Q11a: heavy cannabis use — substance-induced vs primary psychosis.

Need from Oxford:
- immediate assessment priorities for a first psychotic presentation;
- differential / organic / substance considerations already extracted in Q12 packet;
- investigations and baseline assessment if covered;
- initial treatment/management principles;
- engagement/family/early-intervention material if present;
- exam-relevant treatment-duration/response anchors only if clearly stated.

### Q12 — Schizophrenia clinical picture and diagnosis
Already extracted and drafted. **No further Oxford work required.**

### Q13 — Schizophrenia vs schizoaffective vs mood disorder with psychotic features
Reuse Q12 diagnosis/differential material.
Need only any later Oxford material that materially sharpens the longitudinal mood–psychosis distinction. Do not reread diagnosis pages unless a single unresolved point requires it.

### Q14 — Neurobiology of schizophrenia
Need:
- major neurobiological models worth saying in a 2–4 minute answer;
- dopamine;
- glutamate if covered;
- neurodevelopmental model;
- genetics/environment/neuroimaging only to the extent needed for the answer spine;
- major limitations / no single explanatory model.

Avoid encyclopaedic molecular detail.

### Q15 — Prognosis in schizophrenia
Need:
- major prognostic factors;
- DUP if covered;
- sex/age-of-onset/course patterns if clinically useful;
- suicide/physical-health considerations only if they genuinely belong in prognosis;
- avoid long epidemiology tables.

### Q16 — Acute treatment of schizophrenia
Need:
- immediate assessment/safety;
- antipsychotic treatment principles;
- route/adherence/agitation considerations if covered;
- non-pharmacological/environmental measures;
- treatment response and next-step logic;
- what Oxford says that is likely to require current verification.

Do **not** turn this into Q19 clozapine or Q18 TRS.

### Q17 — Long-term management of schizophrenia
Need:
- maintenance antipsychotic strategy;
- adherence / LAIs where relevant;
- relapse prevention;
- psychosocial interventions, family work, psychoeducation, rehabilitation/recovery;
- negative/cognitive symptoms and functional recovery;
- physical-health monitoring;
- duration-of-maintenance anchors if Oxford gives them.

Q17a requires distinguishing primary negative symptoms from depression, adverse effects, active psychosis and environmental deprivation; Q12 packet already contains some of this.

### Q18 — Treatment-resistant schizophrenia
Need:
- Oxford definition / threshold;
- adequate-treatment-trial logic;
- pseudoresistance causes;
- clozapine place in sequence;
- what appears outdated or vague and therefore needs current verification.

### Q19 — Clozapine
Need only Oxford's exam framing:
- indications;
- major adverse effects;
- monitoring concepts;
- practical risks/interactions if covered;
- smoking/infection relevance if covered.

Do **not** spend time extracting exact current ANC thresholds, monitoring schedules, restart rules or current plasma-level targets. Those will come from current prescribing/regulatory verification, not Oxford 2017.

## Output

Write one file:

`oral/100-crucial-questions/answers/source-packets/Q011-Q019-oxford-map.md`

Target length: **2,000–4,000 words for the whole nine-question batch**, not per question.

Use this structure:

1. `Oxford sections newly inspected` — exact printed/PDF pages.
2. `Reusable chapter map` — only the later chapter sections not already captured in Q12-local.
3. `Question map` — Q11, Q13, Q14, Q15, Q16, Q17, Q18, Q19; for each:
   - 4–7 answer-spine bullets;
   - core Oxford points;
   - classic exam facts worth keeping;
   - 1–5 points likely to require current verification;
   - deliberate exclusions / overlap with neighbouring questions.
4. `Reuse notes from Q12-local` — identify which pre-existing sections support Q11/Q13/Q17a rather than copying them again.
5. `Stop/escalation notes` — only genuine gaps.

## Hard constraints

- Oxford Shorter only for new retrieval.
- Do not open DSM, New Oxford, Kaplan, Maudsley, Stahl or the web.
- Do not write learner-facing answers.
- Do not reproduce long textbook passages.
- Do not repeat material already available in Q012-local.md.
- Do not extract facts that cannot plausibly affect the final 1–2 page answer, board-fact block or a genuine follow-up.
- If Oxford is outdated or vague, flag the point for current verification rather than solving it yourself.
- Stop once all eight remaining question maps are supported.

## Completion report

Return only:

1. `BATCH_OXFORD_READY` or `BLOCKED`,
2. commit SHA,
3. output path,
4. exact new Oxford page ranges actually read,
5. any question that still lacks an adequate exam-source base,
6. the 10 most important points needing current verification across Q11–Q19.
