# Attempt 010 — Mapping of the 129 Curated Greek Oral Items to the 100

Status: internal empirical coverage audit. Source-locked to the curated `orestispsom/Psych/src/data/oral.js` bank and `ORAL_QUALITY_AUDIT.md`; it does not treat older answer content as current treatment authority.

## Purpose

Test the board-sufficiency hypothesis against the existing 129-item Greek oral bank. Every curated oral item is classified as one of:

- `COVERED_DIRECTLY` — the target is explicitly represented by a main question or genuine visible follow-up in Attempt 010.
- `COVERED_WITHIN_ANSWER` — a competent final answer package to the mapped 010 question must contain this material, but it does not justify another visible prompt.
- `FACT_ANCHOR` — the item is primarily a precise/classic/factual probe best protected in the board-fact layer rather than by inflating the visible 100.
- `LOWER_PRIORITY_NOT_FORCED` — consciously not required for the sufficiency set. None of the current 129 items landed here in this audit.

## Result

- Curated items audited: **129/129**.
- `COVERED_DIRECTLY`: **44**.
- `COVERED_WITHIN_ANSWER`: **55**.
- `FACT_ANCHOR`: **30**.
- `LOWER_PRIORITY_NOT_FORCED`: **0**.

No curated Greek oral item currently requires a new main-question slot merely to preserve it. The 30 factual probes are the principal reason a board-fact layer is necessary.

## Mapping

### Psychosis and schizophrenia

| Oral ID | Source topic | Attempt 010 destination | Classification | Note |
|---|---|---|---|---|
| `1Aa1` | Schizophrenia symptom dimensions | Q12 | `COVERED_WITHIN_ANSWER` | |
| `1Aa2` | Schneider first-rank symptoms | Q12 | `FACT_ANCHOR` | Historical/current-status distinction |
| `1Aa3` | DSM/ICD schizophrenia criteria differences | Q12 | `FACT_ANCHOR` | Exam-edition/classification sensitive |
| `1Aa4` | Prodromal/high-risk psychosis assessment | Q11/Q15 | `COVERED_WITHIN_ANSWER` | |
| `1Ab1` | First-episode psychosis management | Q11 | `COVERED_DIRECTLY` | |
| `1Ab2` | FEP response and treatment duration | Q11/Q17 | `FACT_ANCHOR` | Duration/response figures source-sensitive |
| `1Ab3` | Duration of untreated psychosis | Q15 | `COVERED_WITHIN_ANSWER` | |
| `1Ab4` | Schizophrenia prognostic factors | Q15 | `COVERED_DIRECTLY` | |
| `1Ab5` | Sex differences in schizophrenia | Q15 | `FACT_ANCHOR` | |
| `1Ab6` | Suicide in schizophrenia | Q5/Q15 | `COVERED_WITHIN_ANSWER` | |
| `1Ag1` | Cognitive domains impaired in schizophrenia | Q12/Q17 | `COVERED_WITHIN_ANSWER` | |
| `1Ag2` | Magnitude/profile of cognitive impairment | Q12/Q17 | `FACT_ANCHOR` | |
| `1Ag3` | Timing/premorbid cognitive impairment | Q15/Q17 | `COVERED_WITHIN_ANSWER` | |
| `1Ag4` | Cognitive assessment/treatment limitations | Q17 | `COVERED_WITHIN_ANSWER` | |
| `1Ad1` | Definition of treatment-resistant schizophrenia | Q18 | `COVERED_DIRECTLY` | |
| `1Ad2` | Adequate antipsychotic trials/pseudoresistance | Q18 | `FACT_ANCHOR` | |
| `1Ad3` | Clozapine indications | Q19 | `COVERED_DIRECTLY` | |
| `1Ad4` | Clozapine monitoring/serious adverse effects | Q19 | `FACT_ANCHOR` | Current prescribing verification required |
| `1Ad5` | Common clozapine adverse effects | Q19 | `COVERED_WITHIN_ANSWER` | |
| `1Ad6` | Clozapine response/levels/discontinuation | Q19 | `FACT_ANCHOR` | Current prescribing verification required |
| `1Ad7` | Clozapine hypersalivation management | Q19 | `COVERED_WITHIN_ANSWER` | |
| `1Ad8` | Glutamatergic model of resistant schizophrenia | Q14/Q18 | `COVERED_WITHIN_ANSWER` | |
| `1Ae1` | Dopamine and glutamate models of schizophrenia | Q14/Q95 | `COVERED_DIRECTLY` | |
| `1Ae2` | Dopamine pathways and negative symptoms | Q95/Q17 | `COVERED_DIRECTLY` | |
| `1Ae3` | Negative symptoms and treatment | Q17 | `COVERED_DIRECTLY` | |
| `1Ae4` | Psychosocial/environmental risk in schizophrenia | Q14 | `COVERED_WITHIN_ANSWER` | |
| `1Ae5` | Neuroimaging/hypofrontality findings | Q14/Q94 | `COVERED_WITHIN_ANSWER` | |
| `1Az1` | Psychosocial treatment/family work in schizophrenia | Q17/Q93 | `COVERED_WITHIN_ANSWER` | |
| `1Az2` | Depot/LAI antipsychotics | Q17/Q76 | `COVERED_WITHIN_ANSWER` | |
| `1Az3` | Adherence/non-adherence in schizophrenia | Q17 | `COVERED_WITHIN_ANSWER` | |

### Delirium

| Oral ID | Source topic | Attempt 010 destination | Classification |
|---|---|---|---|
| `1B1` | Delirium definition/core features | Q45 | `COVERED_DIRECTLY` |
| `1B2` | Causes of delirium | Q45 | `COVERED_WITHIN_ANSWER` |
| `1B3` | Delirium vs dementia vs depression | Q45/Q46/Q57 | `COVERED_WITHIN_ANSWER` |
| `1B4` | Why psychiatric patients are vulnerable to delirium | Q45/Q56 | `COVERED_WITHIN_ANSWER` |
| `1B5` | Restraint and delirium | Q45/Q7 | `COVERED_WITHIN_ANSWER` |
| `1B6` | Delirium tremens | Q38/Q45 | `COVERED_WITHIN_ANSWER` |
| `1B7` | Violent/agitated patient in ED | Q7 | `COVERED_DIRECTLY` |
| `1B8` | Medication in hospital delirium | Q45 | `COVERED_WITHIN_ANSWER` |

### Mood and suicide

| Oral ID | Source topic | Attempt 010 destination | Classification | Note |
|---|---|---|---|---|
| `1Ca1` | Depression types/severity/specifiers | Q20 | `COVERED_WITHIN_ANSWER` | |
| `1Ca2` | Melancholic depression | Q20 | `COVERED_WITHIN_ANSWER` | |
| `1Ca3` | Atypical depression | Q20 | `COVERED_WITHIN_ANSWER` | |
| `1Ca4` | Seasonal depression | Q20/Q89 | `COVERED_WITHIN_ANSWER` | |
| `1Ca5` | Persistent depressive disorder/dysthymia | Q20 | `FACT_ANCHOR` | Classification/duration sensitive |
| `1Ca6` | Postpartum depression vs postpartum psychosis | Q27 | `COVERED_DIRECTLY` | |
| `1Cb1` | Mild depression: psychotherapy vs antidepressant | Q21 | `COVERED_WITHIN_ANSWER` | |
| `1Cb2` | Antidepressant treatment strategy | Q21/Q79/Q80 | `COVERED_WITHIN_ANSWER` | |
| `1Cb3` | Treatment-resistant depression definition/steps | Q22 | `COVERED_DIRECTLY` | |
| `1Cb4` | Ketamine/esketamine in TRD | Q22 | `COVERED_WITHIN_ANSWER` | |
| `1Cg1` | Unipolar vs bipolar depression | Q23/Q25 | `COVERED_WITHIN_ANSWER` | |
| `1Cg2` | Mixed features and rapid cycling | Q23/Q26 | `FACT_ANCHOR` | |
| `1Cg3` | Apathy vs depression | Q57 | `COVERED_DIRECTLY` | |
| `1Cd1` | Suicide risk factors | Q4/Q5 | `COVERED_WITHIN_ANSWER` | Recommend explicit Q5 probe |
| `1Cd2` | Assessment of suicidal intent | Q4 | `COVERED_DIRECTLY` | |
| `1Cd3` | Sex differences in suicidality | Q5 | `FACT_ANCHOR` | |
| `1Cd4` | Suicidality in schizophrenia vs depression | Q5/Q15/Q20 | `COVERED_WITHIN_ANSWER` | |

### Psychopharmacology

| Oral ID | Source topic | Attempt 010 destination | Classification | Note |
|---|---|---|---|---|
| `2Aa1` | Lithium therapeutic levels | Q81 | `FACT_ANCHOR` | Current prescribing verification required |
| `2Aa2` | Lithium adverse effects | Q81 | `COVERED_WITHIN_ANSWER` | |
| `2Aa3` | Causes/interactions causing lithium toxicity | Q81/Q75 | `COVERED_DIRECTLY` | |
| `2Aa4` | Management of lithium toxicity | Q81 | `COVERED_WITHIN_ANSWER` | |
| `2Aa5` | Renal and thyroid effects of lithium | Q81 | `COVERED_WITHIN_ANSWER` | |
| `2Ab1` | Valproate levels and adverse effects | Q82 | `FACT_ANCHOR` | Current prescribing verification required |
| `2Ab2` | Valproate teratogenic/neurodevelopmental risk | Q82/Q86 | `FACT_ANCHOR` | Current regulatory verification required |
| `2Ab3` | Other valproate adverse effects/monitoring | Q82 | `COVERED_WITHIN_ANSWER` | |
| `2Ag1` | Clinically important differences among SSRIs | Q79/Q80 | `FACT_ANCHOR` | |
| `2Ag2` | Most selective SSRI | Q79 | `FACT_ANCHOR` | Low-depth but direct oral-bank fact |
| `2Ad1` | Antipsychotic extrapyramidal adverse effects | Q77 | `COVERED_DIRECTLY` | |
| `2Ad2` | Tardive dyskinesia | Q77 | `COVERED_WITHIN_ANSWER` | |
| `2Ad3` | Metabolic adverse effects and QTc | Q78 | `COVERED_DIRECTLY` | |
| `2Ad4` | Antipsychotic hyperprolactinaemia | Q78 | `COVERED_WITHIN_ANSWER` | |
| `2Ad5` | Choosing antipsychotic by adverse-effect profile | Q76/Q78 | `COVERED_DIRECTLY` | |
| `2Ad6` | Sex-specific/other antipsychotic adverse-effect considerations | Q76/Q78 | `COVERED_WITHIN_ANSWER` | |
| `2B1` | Serotonin syndrome clinical features | Q87 | `COVERED_DIRECTLY` | |
| `2B2` | Serotonin syndrome vs NMS | Q87 | `COVERED_DIRECTLY` | |
| `2B3` | NMS features and management | Q87 | `COVERED_DIRECTLY` | |
| `2C1` | Trazodone mechanism and priapism | Q79/Q80 | `FACT_ANCHOR` | |
| `2C2` | Psychotropic-associated hyponatraemia/SIADH | Q80 | `FACT_ANCHOR` | |
| `2C3` | High-yield psychotropic interactions | Q75 | `COVERED_DIRECTLY` | |

### Anxiety and trauma

| Oral ID | Source topic | Attempt 010 destination | Classification |
|---|---|---|---|
| `3A1` | Panic disorder clinical picture and cognitive model | Q28/Q90 | `COVERED_WITHIN_ANSWER` |
| `3A2` | Panic disorder treatment | Q28 | `COVERED_DIRECTLY` |
| `3A3` | PTSD clinical picture | Q32 | `COVERED_DIRECTLY` |
| `3A4` | Acute stress vs adjustment disorder | Q33 | `COVERED_DIRECTLY` |
| `3A5` | PTSD psychotherapy / trauma-focused CBT | Q32/Q90 | `COVERED_WITHIN_ANSWER` |
| `3A6` | EMDR | Q32 | `COVERED_WITHIN_ANSWER` |
| `3A7` | Social anxiety disorder | Q30 | `COVERED_DIRECTLY` |
| `3A8` | Performance anxiety / beta-blocker role | Q30 | `FACT_ANCHOR` |

### Substance use

| Oral ID | Source topic | Attempt 010 destination | Classification | Note |
|---|---|---|---|---|
| `3B1` | Alcohol withdrawal presentation and timing | Q38 | `FACT_ANCHOR` | |
| `3B2` | Alcohol withdrawal treatment | Q38 | `COVERED_DIRECTLY` | |
| `3B3` | Chronic alcohol complications | Q37/Q39 | `COVERED_WITHIN_ANSWER` | |
| `3B4` | Alcohol relapse-prevention pharmacotherapy | Q39 | `COVERED_DIRECTLY` | |
| `3B5` | Wernicke-Korsakoff syndrome | Q38 | `COVERED_WITHIN_ANSWER` | |
| `3B6` | Opioid withdrawal/OUD treatment | Q40 | `COVERED_WITHIN_ANSWER` | |
| `3B7` | Urine drug detection windows | Q37 | `FACT_ANCHOR` | Lower-priority exact recall; assay/context dependent |
| `3B8` | Amphetamine vs cocaine mechanism | Q42/Q95 | `FACT_ANCHOR` | |
| `3B9` | Neurobiology of tolerance | Q37/Q74 | `COVERED_WITHIN_ANSWER` | |

### Neurocognitive / Parkinson

| Oral ID | Source topic | Attempt 010 destination | Classification |
|---|---|---|---|
| `3C1` | Alzheimer vs DLB vs FTD differential | Q47/Q48/Q49 | `COVERED_WITHIN_ANSWER` |
| `3C2` | DLB clinical features | Q48 | `COVERED_DIRECTLY` |
| `3C3` | BPSD/antipsychotic caution | Q51 | `COVERED_DIRECTLY` |
| `3C4` | Cholinesterase inhibitors | Q47/Q48 | `FACT_ANCHOR` |
| `3C5` | Memantine | Q47 | `FACT_ANCHOR` |
| `3C6` | Psychosis in dementia | Q51/Q48 | `COVERED_WITHIN_ANSWER` |
| `3C7` | Psychiatric manifestations of Parkinson disease | Q48/Q57 | `COVERED_WITHIN_ANSWER` |
| `3C8` | Management of psychosis in Parkinson disease | Q48 | `COVERED_DIRECTLY` |
| `3C9` | Charles Bonnet and Diogenes/severe self-neglect syndromes | Q58/Q52 | `COVERED_DIRECTLY` |

### Biological treatments

| Oral ID | Source topic | Attempt 010 destination | Classification | Note |
|---|---|---|---|---|
| `4A1` | ECT indications/efficacy/precautions | Q89 | `COVERED_DIRECTLY` | |
| `4A2` | Medication management around ECT | Q89 | `FACT_ANCHOR` | Current authoritative verification required |
| `4A3` | Phototherapy mechanism/indications | Q20/Q89 | `FACT_ANCHOR` | |
| `4A4` | Melatonin mechanism/clinical use | Q65/Q67 | `FACT_ANCHOR` | |

### Psychotherapy / ethics

| Oral ID | Source topic | Attempt 010 destination | Classification |
|---|---|---|---|
| `4B1` | CBT, applications and schemas | Q90 | `COVERED_DIRECTLY` |
| `4B2` | IPT and indications | Q92 | `COVERED_DIRECTLY` |
| `4B3` | Transference and countertransference | Q91 | `COVERED_DIRECTLY` |
| `4B4` | Psychoeducation | Q93 | `COVERED_DIRECTLY` |
| `4B5` | Confidentiality / Greek law | Q98 | `COVERED_DIRECTLY` |

### Sleep

| Oral ID | Source topic | Attempt 010 destination | Classification |
|---|---|---|---|
| `4C1` | Sleep stages and EEG | Q67 | `COVERED_DIRECTLY` |
| `4C2` | REM sleep characteristics | Q67 | `COVERED_WITHIN_ANSWER` |
| `4C3` | Sleep changes in depression | Q67 | `COVERED_DIRECTLY` |
| `4C4` | Insomnia in older adults | Q65/Q46 | `COVERED_WITHIN_ANSWER` |

### Autism

| Oral ID | Source topic | Attempt 010 destination | Classification | Note |
|---|---|---|---|---|
| `4D1` | DSM-IV vs DSM-5 autism classification | Q60 | `FACT_ANCHOR` | Historical classification |
| `4D2` | Autism clinical picture/prognosis | Q60 | `COVERED_WITHIN_ANSWER` | |
| `4D3` | Empathy in autism | Q60 | `COVERED_WITHIN_ANSWER` | |
| `4D4` | Sex differences/masking in autism | Q60 | `COVERED_DIRECTLY` | |

### Genetics / epidemiology

| Oral ID | Source topic | Attempt 010 destination | Classification |
|---|---|---|---|
| `5A1` | Heritability | Q96 | `COVERED_DIRECTLY` |
| `5A2` | Familial schizophrenia risk figures | Q96 | `FACT_ANCHOR` |
| `5A3` | GWAS/polygenic risk | Q96 | `COVERED_DIRECTLY` |
| `5A4` | NNT calculation | Q97 | `FACT_ANCHOR` |
| `5A5` | Environmental risk factors in schizophrenia | Q14/Q96 | `COVERED_WITHIN_ANSWER` |

### Personality

| Oral ID | Source topic | Attempt 010 destination | Classification |
|---|---|---|---|
| `5B1` | Borderline personality disorder | Q69 | `COVERED_DIRECTLY` |
| `5B2` | Antisocial personality disorder / psychopathy | Q70 | `COVERED_DIRECTLY` |
| `5B3` | Personality clusters / other major PDs | Q68 | `COVERED_WITHIN_ANSWER` |
| `5B4` | Paranoid personality disorder | Q68 | `COVERED_WITHIN_ANSWER` |

## Interpretation

### What this audit supports

- The existing 100-question allocation does not appear to have sacrificed a high-value item from the curated Greek oral bank.
- The oral bank is not equivalent to 129 separate required main questions. Most narrower prompts naturally live inside a larger senior-resident answer.
- The 30 `FACT_ANCHOR` items are disproportionately exact, historical/classificatory, numerical, drug-specific or mechanism-specific. They should be retrievable without forcing the visible guide to become a list of trivia questions.

### Important limitations

- This is a mapping audit, not current-clinical verification. Older doses, thresholds, monitoring schedules, prevalence figures, DSM/ICD comparisons and treatment recommendations in `oral.js` must not be copied uncritically.
- The source bank itself contains historical/exam-specific material. Final answers must separate exam-source truth from current clinical truth where they diverge.
- `COVERED_WITHIN_ANSWER` is a requirement, not an assumption: the eventual answer specifications must explicitly contain the mapped material before board sufficiency can be claimed.

## Immediate actions generated by the audit

1. Seed `internal/board-fact-anchors.yml` from all 30 `FACT_ANCHOR` rows plus additional high-yield diagnostic-duration/monitoring anchors already present in the Psych SOS/MCQ material.
2. Keep the 100 main slots frozen provisionally.
3. During answer writing, require every `COVERED_WITHIN_ANSWER` row to be explicitly satisfied by the relevant answer package.
4. Add a compact suicide risk/disorder-pattern probe to the next visible attempt, because `1Cd1` is important enough that relying only on hidden coverage is unnecessarily fragile.
5. Re-audit after answers are drafted: a row counts as truly covered only when the written answer/fact layer can be pointed to, not merely because its destination question is semantically related.
