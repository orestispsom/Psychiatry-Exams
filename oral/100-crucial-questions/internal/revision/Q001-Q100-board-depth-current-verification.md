# Q001–Q100 Global Board-Depth Current Verification

Scope: targeted adjudication of consequential enrichments proposed in `Q001-Q100-board-depth-enrichment-audit.md` (audit commit `a3c78d275c648d6837210f9fd9866de2cf8614da`). This document does **not** rewrite final answers. It decides whether candidate enrichments are safe for a high-level Greek Adult Psychiatry board-review manuscript.

Decision vocabulary in the ledger is limited to `KEEP / MODIFY / DROP / UNRESOLVED`. Where the underlying qualitative point survives but a numerical estimate does not, the correction explicitly uses `DROP_NUMBER_KEEP_QUALITATIVE` inside a `MODIFY` or `DROP` decision.

## 1. Executive adjudication

### Overall result

The CLI audit is directionally useful but **too numerically aggressive and too absolute** for publication without adjudication. Its strongest contributions are diagnostic timing distinctions, high-yield treatment sequencing, a small number of emergency doses, current monitoring schedules, classic psychopathology clearly labelled as historical, and Greek statutory anchors. Its weakest layer is the conversion of memorable textbook figures into universal “must-know board facts.”

This pass adjudicates **349 consequential claim units** across Q001–Q100: **152 KEEP, 161 MODIFY, 31 DROP, 5 UNRESOLVED**.

### What survives well

- Current DSM/ICD **duration/count distinctions** when they genuinely discriminate diagnoses.
- Operational **guideline monitoring** where the interval is explicit: rapid-tranquillisation observations, lithium monitoring, antipsychotic metabolic monitoring, current clozapine ANC monitoring.
- A small set of **emergency anchors**: lorazepam challenge, malignant-catatonia BAP dosing/escalation, current IV thiamine for suspected Wernicke encephalopathy, and sodium bicarbonate treatment principles in TCA cardiotoxicity.
- **Current regulatory changes** that the older source base could not contain: 2025 EU clozapine neutropenia monitoring; 2024–26 valproate male reproductive precautions; 2026 EU deutetrabenazine authorisation; current EU anti-amyloid restrictions.
- **Greek legal facts** that are both current and board-relevant: consent/confidentiality, involuntary-admission criteria and timetable, the corrected 2022 transport law, criminal responsibility, and the post-2024 national mental-health network.

### Main overstatements

1. **Risk multipliers and prognosis percentages.** Suicide, violence, schizophrenia outcome, bipolar recurrence, BPD prognosis, heritability and many relapse figures are too heterogeneous to freeze.
2. **Screening cut-offs treated as diagnoses.** 4AT, MoCA, MMSE, BVC, COWS, CIWA-Ar and BFCRS need explicit purpose/limitations.
3. **Guideline recommendations upgraded to mandates.** Examples: lorazepam in RT, NMS 14-day restart, antidepressant stopping in mania, benzodiazepine 2–4-week “limit.”
4. **Historical or heuristic thresholds treated as universal biology.** D2 occupancy windows, fixed PTA bins, exact sleep percentages, Geschwind syndrome.
5. **Licensing and guideline conflation.** International evidence does not equal current EMA indication or Greek availability.
6. **Older legal/statutory summaries.** Most importantly, the audit cites the wrong 2022 Greek law for involuntary transport.

### Main under-enrichments corrected here

- **Clozapine ANC monitoring changed materially in Europe in 2025.**
- **Male valproate reproductive precautions** now belong in a current European board package.
- **Deutetrabenazine received EU-wide TD authorisation in January 2026.**
- **Anti-amyloid treatment rules** must be separated from ordinary Alzheimer diagnosis.
- **Law 4931/2022**, not Law 4999/2022, inserted Article 96A on involuntary transport.
- **Law 3500/2006 Article 23 has been amended** in 2024 and 2025; the original child/domestic-violence reporting wording is no longer sufficient.
- **Law 5129/2024** changed the Greek service architecture but not the substantive involuntary-admission criteria.

### Unsafe/materially wrong CLI claims

The following should not enter the manuscript unchanged: a delusion as virtually pathognomonic; suicide-tool PPV `<5%`; prior-attempt `15–30×` risk; SMI victim/perpetrator `3–5×`; “mandatory” lorazepam RT wording; Law `4999/2022` for Art 96A; FEP `70–80%` response and “50% dose” rule; one-SGA requirement attributed to TRRIP; the old clozapine ANC schedule; fixed schizophrenia outcome thirds; bipolar recurrence/heredity tables; routine supra-licensed OCD SSRI doses; “glucose only after thiamine”; fixed COWS threshold; fixed dementia-screening diagnostic cut-offs; universal PTA bins; BMI `<18.5` as AN diagnosis; PCL-R `30` as universal psychopathy threshold; lithium dialysis by serum level alone; fixed `3–5 day` lamotrigine restart rule; and minimum ECT seizure-duration rules.

### Source strategy

For exact current claims, the pass prioritises current major guidelines, EMA/SmPC/regulatory material, EXTRIP/poison-centre guidance, and current Greek statutes. Stable phenomenology/anatomy was not repeatedly re-researched. Prior `Qxxx-current-verification.md` packets were reused where they had already resolved the same question, with fresh verification for materially time-sensitive or disputed points.

### Principal source key

- **NICE NG225 — Self-harm: assessment, management and preventing recurrence:** https://www.nice.org.uk/guidance/ng225/chapter/recommendations
- **NICE NG10 — Violence and aggression: short-term management:** https://www.nice.org.uk/guidance/ng10/chapter/recommendations
- **BAP 2023 — Evidence-based consensus guidelines for catatonia/NMS:** https://pmc.ncbi.nlm.nih.gov/articles/PMC10101189/
- **NICE CG178 — Psychosis and schizophrenia in adults:** https://www.nice.org.uk/guidance/cg178/chapter/recommendations
- **TRRIP — Treatment Response and Resistance in Psychosis consensus:** https://pmc.ncbi.nlm.nih.gov/articles/PMC6231547/
- **EMA clozapine 2025 — PRAC neutropenia-monitoring update:** https://www.ema.europa.eu/en/documents/prac-recommendation/new-product-information-wording-extracts-prac-recommendations-signals-adopted-7-10-july-2025-prac_en.pdf
- **NICE NG222 — Depression in adults:** https://www.nice.org.uk/guidance/ng222/chapter/recommendations
- **NICE CG185 — Bipolar disorder:** https://www.nice.org.uk/guidance/cg185/chapter/recommendations
- **EMA valproate — Valproate reproductive restrictions / male precautions:** https://www.ema.europa.eu/en/news/precautionary-measures-address-potential-risk-neurodevelopmental-disorders-children-born-men-treated-valproate-medicines
- **NICE CG31 — OCD/BDD treatment:** https://www.nice.org.uk/guidance/cg31/chapter/recommendations
- **NICE CG159 — Social anxiety disorder:** https://www.nice.org.uk/guidance/cg159/chapter/recommendations
- **AAN 2025 — Management of Functional Seizures:** https://www.aan.com/Guidelines/Home/GuidelineDetail/1150
- **NICE NG69 — Eating disorders:** https://www.nice.org.uk/guidance/ng69/chapter/recommendations
- **MEED 2022 — Medical Emergencies in Eating Disorders:** https://www.rcpsych.ac.uk/improving-care/campaigning-for-better-mental-health-policy/college-reports/2022-college-reports/cr233
- **NICE NG87 — ADHD diagnosis and management:** https://www.nice.org.uk/guidance/ng87/chapter/recommendations
- **EXTRIP — Lithium poisoning extracorporeal treatment:** https://www.extrip-workgroup.org/lithium
- **EMA Quviviq — Daridorexant EPAR:** https://www.ema.europa.eu/en/medicines/human/EPAR/quviviq
- **EMA Austedo — Deutetrabenazine EPAR:** https://www.ema.europa.eu/en/medicines/human/EPAR/austedo
- **EMA Kisunla — Donanemab EPAR:** https://www.ema.europa.eu/en/medicines/human/EPAR/kisunla
- **AASM RBD — 2023 RBD guideline summary:** https://aasm.org/new-guideline-provides-treatment-recommendations-for-people-who-act-out-their-dreams-while-asleep/
- **Greek Medical Code — Law 3418/2005:** https://www.e-nomothesia.gr/kat-ygeia/n-3418-2005.html
- **Greek involuntary law — Law 2071/1992:** https://www.e-nomothesia.gr/inner.php/kat-ygeia/n-2071-1992.html?print=1
- **Greek transport reform — Law 4931/2022 Art 59 / Art 96A:** https://www.e-nomothesia.gr/kat-ygeia/nomos-4931-2022-phek-94a-13-5-2022.html
- **Greek Penal Code — Law 4619/2019, current codification:** https://www.e-nomothesia.gr/kat-poinikos-kodikas/nomos-4619-2019-phek-95a-11-6-2019.html
- **Greek domestic violence — Law 3500/2006 Art 23, amended:** https://www.e-nomothesia.gr/kat-oikogeneia/n-3500-2006.html
- **Greek mental-health reform — Law 5129/2024 / MoH implementation:** https://www.moh.gov.gr/articles/ministry/grafeio-typoy/press-releases/12618-sthn-olomeleia-ths-boylhs-pros-syzhthsh-kai-pshfish-to-nomosxedio-toy-ypoyrgeioy-ygeias-me-titlo-laquo-oloklhrwsh-ths-psyxiatrikhs-metarrythmishs-raquo
- **TCA poison guideline — Evidence-based poison-centre consensus:** https://pubmed.ncbi.nlm.nih.gov/17453872/
- **Utah Poison Control 2025 — Sodium bicarbonate use in toxicology:** https://poisoncontrol.utah.edu/news/2025/09/covering-bases-sodium-bicarbonate-use-toxicology

## 2. Global corrections to the CLI revision rules

| Area | CLI rule/problem | Approved replacement |
|---|---|---|
| Numerical scaffold | `Every major disorder must contain duration, symptom count, age boundary and frequency.` | `Add numerical anchors only when they improve discrimination and are stable enough to teach; label DSM/ICD system explicitly.` |
| Mechanism density | `Whenever a psychotropic is named, add a precise receptor/transporter mechanism.` | `Add a one-line mechanism only when it explains selection, adverse effects, interaction or a common viva distinction; avoid mechanistic decoration.` |
| Emergency dosing | `Every emergency answer needs exact doses, repeats and maximum ceilings.` | `Use exact emergency doses only from current authoritative protocols and scope them to that protocol; do not fabricate a universal regimen where guidelines differ.` |
| Monitoring thresholds | `Replace vague monitoring with exact cutoffs and mandatory action.` | `Use exact thresholds only when operationally validated; distinguish risk flags, screening scores, product stop rules and specialist-toxicology criteria.` |
| Risk epidemiology | `Include stable multipliers such as 15–30× after attempt, 2–5× cannabis risk, 70–85% bipolar heritability.` | `Do not promote heterogeneous observational estimates into universal board truths. Prefer direction/magnitude category unless the number is regulatory or diagnostically discriminating.` |
| Scale performance | `Every named scale should include sensitivity/specificity and cutoff.` | `State the scale's clinical purpose, horizon and limitations. Add performance metrics only when they are robust and materially useful.` |
| Treatment sequence | `Present one first-line/second-line sequence as current practice.` | `Name the guideline or licensing jurisdiction when sequencing differs. Do not merge NICE, international consensus and EMA licensing into one hierarchy.` |
| Absolute wording | `Mandatory/always/never/gold standard/contraindicated` when common teaching suggests it. | `Use the authority's actual verb and reserve absolutes for true statutory, regulatory or product contraindications.` |
| Historical material | `Retain classic material alongside current facts.` | `Retain only when examination value is real and label it HISTORICAL_EXAM_FACT so it cannot be mistaken for current diagnostic truth.` |
| Greek law | `Use familiar legal summaries.` | `Use current Greek statutory text and later procedural amendments. Never import UK capacity/ECT/Tarasoff rules or rely on a superseded Greek provision.` |
| Local availability | `EMA authorisation implies routine Greek use.` | `Separate EU marketing authorisation from Greek market availability, reimbursement and local formulary access.` |
| Publication economy | `More board facts are always better.` | `Prefer a small number of discriminating, current facts. Delete numbers that add apparent precision without changing a viva answer or a safe clinical decision.` |

## 3. Q001–Q100 adjudication ledger

### Q001

- `DROP` — “A persistent unshakeable delusion is virtually pathognomonic of mental disorder.” — **Do not teach any single delusional feature as pathognomonic. Delusions require phenomenological and cultural-contextual assessment and occur across multiple psychiatric, neurological and medical disorders.**
  - Placement: `TRAP`
  - Source: Current descriptive psychopathology; DSM-5-TR/ICD-11 principles
- `KEEP` — Jaspers’ Verstehen versus Erklären distinction. **Approved:** Retain as a classic descriptive-psychopathology framework, explicitly labelled historical/conceptual rather than a current diagnostic criterion.
  - Placement: `HISTORICAL`
  - Source: Jaspers/descriptive psychopathology
- `KEEP` — Standard MSE domains and 4Ps biopsychosocial formulation. **Approved:** Retain as organisational frameworks; there is no statutory or diagnostic requirement for one exact domain count.
  - Placement: `BOARD_FACT`
  - Source: Stable psychiatric practice

### Q002

- `MODIFY` — Jaspers’ three delusion criteria presented as a current definition. → **Retain conviction, incorrigibility and implausibility/falsity as classic Jaspersian teaching, but label HISTORICAL_EXAM_FACT; modern diagnosis cannot require literal falsity or impossibility in every case.**
  - Placement: `HISTORICAL`
  - Source: Jaspers; current DSM/ICD descriptive principles
- `KEEP` — Wernicke overvalued idea as an emotionally charged, understandable, dominating belief. **Approved:** Retain as historical descriptive psychopathology and distinguish from obsession and delusion.
  - Placement: `HISTORICAL`
  - Source: Classical descriptive psychopathology
- `KEEP` — OCD can occur with poor or absent insight. **Approved:** Retain; poor insight does not by itself transform OCD into schizophrenia/delusional disorder.
  - Placement: `BOARD_FACT`
  - Source: DSM-5-TR; ICD-11 OCD architecture

### Q003

- `MODIFY` — Oxford four-step causal rule requiring parallel resolution of psychiatric syndrome when physical cause resolves. → **Use temporality, biological plausibility, known causal association, dechallenge/rechallenge information and exclusion of better explanations as supportive causal evidence; parallel resolution is helpful but not required.**
  - Placement: `FOLLOWUP`
  - Source: Modern causal reasoning; Q004-Q007-Q010 current verification
- `MODIFY` — First psychosis/mania after age 40–50 as a fixed organic threshold. → **Late or atypical onset is a red flag that lowers the threshold for medical/neurological investigation, but no single age cut-off diagnoses a secondary syndrome.**
  - Placement: `BOARD_FACT`
  - Source: Current neuropsychiatric practice
- `KEEP` — Clouding/fluctuation, focal neurological signs, abnormal vitals, atypical hallucinations and medication/substance exposure as red flags. **Approved:** Retain qualitatively.
  - Placement: `BOARD_FACT`
  - Source: Current neuropsychiatric practice

### Q004

- `MODIFY` — Suicide risk tools/categorical stratification have PPV <5% for completed suicide. → **DROP_NUMBER_KEEP_QUALITATIVE: risk tools and global low/medium/high categories have insufficient predictive accuracy for individual suicide and must not determine discharge or treatment eligibility.**
  - Placement: `BOARD_FACT`
  - Source: NICE NG225 1.6.1–1.6.6
- `KEEP` — Do not use global low/medium/high suicide-risk stratification to predict or decide discharge. **Approved:** Retain exactly at the principle level; use needs-focused psychosocial assessment and risk formulation.
  - Placement: `TRAP`
  - Source: NICE NG225 1.6
- `MODIFY` — Static versus dynamic factors, with dynamic drivers dictating immediate containment. → **Retain the distinction, but avoid implying any factor mechanically dictates disposition; management follows formulation, intent, means, imminence, supports and treatable drivers.**
  - Placement: `MODEL`
  - Source: NICE NG225; contemporary suicide-risk formulation

### Q005

- `MODIFY` — Aftercare within 48 hours is mandatory after every self-harm discharge. → **NICE recommends initial aftercare within 48 hours when there are ongoing safety concerns; it is not a universal mandate for every presentation.**
  - Placement: `BOARD_FACT`
  - Source: NICE NG225 1.10.2
- `KEEP` — Offer a structured, person-centred psychological intervention after self-harm, commonly brief CBT-informed/problem-solving work. **Approved:** Retain; NICE gives 4–10 sessions as a typical structure for adults, tailored to need.
  - Placement: `BOARD_FACT`
  - Source: NICE NG225 1.11
- `MODIFY` — Prior suicide attempt confers 15–30× later suicide risk and is the single strongest predictor; highest risk is first 3–12 months. → **DROP_NUMBER_KEEP_QUALITATIVE: a previous attempt is a major marker of future suicide/self-harm risk, and risk is particularly elevated soon after an attempt or psychiatric discharge; exact multipliers and one fixed window are heterogeneous and should not be taught.**
  - Placement: `BOARD_FACT`
  - Source: NICE NG225; contemporary suicide meta-analyses
- `MODIFY` — Means restriction is the most robust intervention for individual and population suicide reduction. → **Means-safety interventions are evidence-based and should be included when relevant; avoid a universal superlative across all clinical contexts.**
  - Placement: `BOARD_FACT`
  - Source: NICE NG225; WHO suicide-prevention principles

### Q006

- `KEEP` — BVC consists of six observable behaviours and estimates very short-term inpatient violence risk. **Approved:** Retain as a short-horizon structured adjunct, not as a replacement for clinical formulation.
  - Placement: `FOLLOWUP`
  - Source: BVC validation literature; current violence-risk practice
- `MODIFY` — BVC score ≥2 predicts violence in exactly the next 24 hours. → **Score ≥2 is a commonly used alert threshold in validation studies, but predictive performance and action thresholds are setting-dependent; teach as a screening/escalation anchor, not a deterministic cut-off.**
  - Placement: `FOLLOWUP`
  - Source: BVC validation/meta-analysis
- `DROP` — People with SMI are 3–5× more likely to be victims than perpetrators. — **The comparison is not a stable or well-defined board statistic; retain only that people with severe mental illness experience substantial victimisation and that mental illness alone is a weak explanation of community violence.**
  - Placement: `BOARD_FACT`
  - Source: Contemporary violence/victimisation epidemiology
- `KEEP` — Substance intoxication, acute threat/persecutory states, impulsivity and situational conflict are important dynamic violence drivers. **Approved:** Retain with scenario-specific formulation.
  - Placement: `MODEL`
  - Source: Contemporary violence-risk formulation

### Q007

- `MODIFY` — NICE RT doses are IM lorazepam 1–2 mg OR IM haloperidol 2.5–5 mg + promethazine 25–50 mg. → **NICE NG10 specifies the regimen choices but not these exact milligram doses. If dose anchors are retained, label them BNF/local-formulary examples and verify the exact product/formulary used; do not attribute the doses to NICE itself.**
  - Placement: `BOARD_FACT`
  - Source: NICE NG10 1.4.37–1.4.45; current BNF/local formulary
- `MODIFY` — IM lorazepam is mandatory when antipsychotic-naïve, QT risk, or ECG unavailable. → **NICE recommends IM lorazepam alone when there is insufficient information about prior antipsychotic exposure and recommends avoiding haloperidol+promethazine when cardiovascular disease/QT prolongation is present or no ECG has been done; ‘mandatory’ is too absolute.**
  - Placement: `TRAP`
  - Source: NICE NG10
- `KEEP` — After RT: physical observations at least hourly; every 15 min in higher-risk situations. **Approved:** Retain as NICE-specific monitoring: q15 min if sedated/asleep, intoxicated, pre-existing physical illness, harm from restrictive intervention, or BNF maximum exceeded.
  - Placement: `BOARD_FACT`
  - Source: NICE NG10 1.4.45
- `UNRESOLVED` — Routine Greek availability/protocol status of IM olanzapine, IM aripiprazole and zuclopenthixol acetate for acute behavioural disturbance. — **Do not add a national Greek protocol claim without authoritative Greek formulary/hospital guidance.**
  - Placement: `FOLLOWUP`
  - Source: Greek national availability/protocol not established in this pass

### Q008

- `KEEP` — Greek informed-consent basis: Law 3418/2005 Arts 11–12; mental disorder/admission does not automatically remove consent rights. **Approved:** Retain; also distinguish clinical decision-making ability from the legal rules governing consent.
  - Placement: `BOARD_FACT`
  - Source: Law 3418/2005 Arts 11,12,28; Law 2619/1998 Oviedo
- `MODIFY` — Substitute-consent hierarchy lists spouse, parents, adult children, siblings after judicial supporter. → **Greek Code: if an adult cannot consent, the appointed judicial supporter consents if one exists; otherwise the statute refers broadly to ‘οικείοι’. Do not invent a priority order among relatives.**
  - Placement: `TRAP`
  - Source: Law 3418/2005 Art 12(2)(bb)
- `KEEP` — Emergency exception includes urgent care when appropriate consent cannot be obtained and attempted suicide. **Approved:** Retain the statutory emergency exceptions, without expanding them into a general power to override non-urgent refusals.
  - Placement: `BOARD_FACT`
  - Source: Law 3418/2005 Art 12(3); Oviedo Art 8

### Q009

- `KEEP` — Law 2071/1992 has two alternative substantive routes for involuntary admission. **Approved:** Retain Route I (mental disorder + inability to judge own health interest + treatment exclusion/deterioration without admission) and Route II (mental disorder + admission necessary to prevent violence to self/others).
  - Placement: `BOARD_FACT`
  - Source: Law 2071/1992 Art 95
- `KEEP` — 48 h examination stay, prosecutor 3-day filing, court within 10 days, ≥48 h summons, ordinary 6-month maximum, review report after first 3 months. **Approved:** Retain as statutory procedural anchors; note that 48 h is for temporary examination when prior examination was impossible, not the duration of involuntary admission.
  - Placement: `BOARD_FACT`
  - Source: Law 2071/1992 Arts 96,99
- `MODIFY` — Law 4999/2022 Art 96A created healthcare-led/EKAB transfer. → **Incorrect statute. Law 4931/2022 Art 59 inserted Art 96A. The statutory model is a mixed initial visit (psychiatrist+nurse+police officer), then community mental-health vehicle with psychiatrist+nurse; police accompaniment during onward transfer is exceptional under stated safeguards. EKAB coordinates the process but is not simply the transport provider in every case.**
  - Placement: `BOARD_FACT`
  - Source: Law 4931/2022 Art 59; KYA G3a,b/GP oik 72109/2022
- `KEEP` — Current first-instance court is Μονομελές Πρωτοδικείο despite legacy Law 2071 wording. **Approved:** Retain as a current-procedure/legacy-text split.
  - Placement: `FOLLOWUP`
  - Source: CPC Art 740 as amended; Greek appellate case law; Q008–Q009 current-law packet
- `KEEP` — Law 5129/2024 reorganised mental-health services but did not replace Art 95 substantive involuntary-admission criteria. **Approved:** Retain.
  - Placement: `TRAP`
  - Source: Law 5129/2024; Law 2071/1992

### Q010

- `KEEP` — Catatonia diagnostic architecture uses ≥3 characteristic signs. **Approved:** Retain as the DSM-5-TR/ICD-11-compatible high-yield threshold; do not imply BFCRS itself is the diagnostic law.
  - Placement: `BOARD_FACT`
  - Source: DSM-5-TR; ICD-11; BAP Catatonia Guideline 2023
- `KEEP` — BFCRS has 14 screening items and 23 total severity items. **Approved:** Retain as examiner follow-up; it is a rating instrument, not a required diagnostic test.
  - Placement: `FOLLOWUP`
  - Source: Bush–Francis scale; BAP 2023
- `KEEP` — Lorazepam challenge 1–2 mg IV/IM or 2 mg oral with short reassessment interval. **Approved:** Retain as a guideline-supported diagnostic/therapeutic challenge; response supports but does not prove catatonia.
  - Placement: `BOARD_FACT`
  - Source: BAP Catatonia Guideline 2023
- `MODIFY` — Therapeutic lorazepam 8–16 mg/day, up to 24 mg/day in malignant catatonia; ECT after 48–72 h for any inadequate response. → **High-dose lorazepam is often required, but the precise regimen is context-specific. BAP specifically recommends 8 mg/day titrated up to 24 mg/day for malignant catatonia and bilateral ECT if partial/no response within 48–72 h. Do not universalise this timing to all catatonia.**
  - Placement: `FOLLOWUP`
  - Source: BAP Catatonia Guideline 2023
- `MODIFY` — Bromocriptine/dantrolene are required NMS antidotes and antipsychotics must never restart before 14 days. → **Stop dopamine antagonists and provide aggressive supportive/critical care. Lorazepam, bromocriptine/amantadine, dantrolene and ECT are severity-dependent options. BAP recommends delaying antipsychotic restart ≥2 weeks after NMS resolution; label this as a guideline recommendation, not a universal legal rule.**
  - Placement: `BOARD_FACT`
  - Source: BAP Catatonia/NMS recommendations 2023

### Q011

- `MODIFY` — DUP is an independent, modifiable predictor of remission/function. → **Longer DUP is consistently associated with poorer symptomatic/functional outcomes and early-intervention services aim to reduce treatment delay; avoid implying that DUP is a proven independent causal variable in every dataset.**
  - Placement: `BOARD_FACT`
  - Source: Early psychosis systematic evidence; NICE CG178
- `DROP` — FEP response is 70–80% and dose requirement is ~50% of multi-episode dosing, with fixed example ranges. — **DROP_NUMBER_KEEP_QUALITATIVE: antipsychotic-naïve FEP patients often respond at the lower end of licensed dose ranges and are vulnerable to adverse effects; titrate individually.**
  - Placement: `BOARD_FACT`
  - Source: NICE CG178; first-episode psychosis evidence
- `MODIFY` — High-potency/daily cannabis causes 2–5× schizophrenia-spectrum psychosis risk and advances onset by 2.7 years. → **DROP_NUMBER_KEEP_QUALITATIVE: frequent/high-potency cannabis exposure is associated with higher psychosis risk and earlier onset in dose-response fashion; exact multipliers/onset shifts are population-specific.**
  - Placement: `BOARD_FACT`
  - Source: Large observational/meta-analytic cannabis–psychosis literature

### Q012

- `MODIFY` — Schizophrenia lifetime prevalence 0.7–1.0%, incidence 15/100,000/y, M:F 1.4:1 and fixed sex-specific onset ranges. → **Use only a broad epidemiological anchor if desired: schizophrenia affects roughly around one half to one percent of the population depending on definition/population; incidence is modestly higher and onset generally earlier in men. Do not teach one fixed incidence or age window as diagnostic.**
  - Placement: `FOLLOWUP`
  - Source: Recent global schizophrenia epidemiology reviews
- `KEEP` — DSM-5-TR active-phase/continuous-duration versus ICD-11 ≥1-month architecture. **Approved:** Retain as a system-specific board distinction: DSM requires an active phase plus ≥6 months continuous disturbance; ICD-11 does not impose the DSM 6-month residual-duration requirement.
  - Placement: `BOARD_FACT`
  - Source: DSM-5-TR; ICD-11 CDDR
- `KEEP` — Classical schizophrenia subtypes and Schneiderian first-rank symptoms as historical material. **Approved:** Retain only as HISTORICAL_EXAM_FACT; neither is a current subtype/diagnostic requirement.
  - Placement: `HISTORICAL`
  - Source: Descriptive psychopathology; DSM/ICD history

### Q013

- `KEEP` — DSM-5-TR schizoaffective 2-week psychosis-without-major-mood-episode rule and mood episodes present for majority of illness. **Approved:** Retain explicitly as DSM-specific.
  - Placement: `BOARD_FACT`
  - Source: DSM-5-TR
- `MODIFY` — Mood disorder with psychotic features means psychosis resolves completely whenever euthymia is achieved. → **The diagnostic boundary is that psychotic symptoms occur only during mood episodes; do not require an absolute statement that every symptom immediately ‘resolves completely’ at euthymia.**
  - Placement: `TRAP`
  - Source: DSM-5-TR mood/psychosis architecture
- `KEEP` — Brief psychotic <1 month; schizophreniform 1–6 months; schizophrenia ≥6 months. **Approved:** Retain only as DSM-specific duration hierarchy; do not present it as ICD-11.
  - Placement: `FOLLOWUP`
  - Source: DSM-5-TR

### Q014

- `MODIFY` — Mesolimbic hyperdopaminergia + mesocortical D1 hypodopaminergia is established schizophrenia neurobiology. → **Present the classic dual-dopamine model as a useful heuristic. Current evidence is strongest for increased presynaptic striatal dopamine synthesis/release in psychosis; cortical dopamine findings and circuit mapping are more complex.**
  - Placement: `BOARD_FACT`
  - Source: Modern schizophrenia dopamine imaging literature
- `MODIFY` — NMDA hypofunction on PV interneurons causes cortical disinhibition and downstream striatal hyperdopaminergia. → **Retain as a mechanistic hypothesis/model, not established causal chain.**
  - Placement: `FOLLOWUP`
  - Source: Current glutamate/NMDA schizophrenia reviews
- `KEEP` — Group-level ventricular/grey-matter/hippocampal structural differences are seen in schizophrenia. **Approved:** Retain as group-level research findings that are not diagnostic in individuals.
  - Placement: `FOLLOWUP`
  - Source: Large neuroimaging meta-analyses
- `MODIFY` — Heritability 70–80%, >250 loci, C4/CACNA1C, 22q11.2 deletion causes 25–30% schizophrenia risk. → **Retain high polygenicity and the importance of common small-effect variants plus rare CNVs such as 22q11.2 deletion. Drop a moving GWAS-locus count and avoid freezing one penetrance number; these are research/genetic-counselling facts, not diagnostic thresholds.**
  - Placement: `BOARD_FACT`
  - Source: Psychiatric genomics consensus; ISPG

### Q015

- `DROP` — Schizophrenia outcomes divide into 20–25% good / 35–40% intermediate / 35–40% chronic severe. — **Outcome distributions are cohort-, era- and endpoint-dependent; teach heterogeneity and prognostic factors rather than one three-bin table.**
  - Placement: `BOARD_FACT`
  - Source: Long-term schizophrenia cohort/meta-analytic literature
- `MODIFY` — SMR 2.5–3.0, life expectancy −15–20 years, suicide ~4.9%. → **DROP_NUMBER_KEEP_QUALITATIVE for the manuscript core: schizophrenia has a major excess-mortality gap, substantially shortened life expectancy, and elevated suicide mortality, especially early in illness. A broad 10–20-year life-expectancy gap may be used only as a contextual follow-up if sourced to a contemporary dataset.**
  - Placement: `BOARD_FACT`
  - Source: Recent schizophrenia mortality meta-analyses
- `KEEP` — Acute onset, good premorbid function, shorter DUP, adherence and fewer negative symptoms are favourable prognostic correlates. **Approved:** Retain as correlates, not deterministic predictors.
  - Placement: `BOARD_FACT`
  - Source: Schizophrenia prognosis literature

### Q016

- `MODIFY` — 65–80% D2 occupancy is therapeutic and >80% causes EPS/prolactin without benefit. → **Retain only as a classic PET heuristic: response probability rises around mid-range striatal D2 occupancy and EPS/prolactin risk rises at higher occupancy, but thresholds vary by drug, partial agonism and individual.**
  - Placement: `FOLLOWUP`
  - Source: PET D2-occupancy literature
- `KEEP` — Adequate antipsychotic trial generally 4–6 weeks at an effective therapeutic dose. **Approved:** Retain as guideline-level board anchor; re-evaluate adherence, diagnosis and tolerability rather than automatically escalating dose.
  - Placement: `BOARD_FACT`
  - Source: NICE CG178
- `MODIFY` — <20% improvement at 2–4 weeks is a powerful negative predictor and should trigger switch. → **Early non-improvement is prognostically informative and should prompt reassessment; it is not an automatic universal switch rule.**
  - Placement: `FOLLOWUP`
  - Source: Early-response meta-analyses; NICE trial principles
- `KEEP` — Avoid routine combined antipsychotics except short periods during switching. **Approved:** Retain as NICE principle.
  - Placement: `TRAP`
  - Source: NICE CG178

### Q017

- `MODIFY` — One-year relapse 70–80% off medication versus 20–30% on medication. → **DROP_NUMBER_KEEP_QUALITATIVE: maintenance antipsychotics substantially reduce relapse, while discontinuation after remission increases relapse risk; absolute rates vary by population and withdrawal strategy.**
  - Placement: `BOARD_FACT`
  - Source: Maintenance/discontinuation meta-analyses
- `MODIFY` — Minimum 1–2 years after first episode; 2–5 years or indefinite after multiple episodes. → **Guidelines differ. NICE emphasises high relapse risk in the next 1–2 years if medication is stopped and recommends gradual withdrawal with prolonged monitoring; duration should be individualised by episode history, risk, preference and recovery.**
  - Placement: `BOARD_FACT`
  - Source: NICE CG178; current first-episode guidelines
- `MODIFY` — Primary deficit syndrome occurs in 15–20%. → **DROP_NUMBER_KEEP_QUALITATIVE: retain the clinically useful distinction between primary/enduring negative symptoms and secondary negative symptoms due to psychosis, depression, EPS, sedation, substance use or deprivation.**
  - Placement: `FOLLOWUP`
  - Source: Negative-symptom consensus

### Q018

- `MODIFY` — TRRIP requires ≥2 AP trials, one of them an SGA, ≥600 mg CPZ for ≥6 weeks each. → **TRRIP requires ≥2 adequate trials of different antipsychotics, each ≥6 weeks at therapeutic dose (CPZ-equivalent benchmark may be used when product target unclear) with adherence established. TRRIP does not require one SGA; NICE separately requires at least one failed non-clozapine SGA before offering clozapine.**
  - Placement: `BOARD_FACT`
  - Source: TRRIP consensus; NICE CG178/QS80
- `MODIFY` — TRS affects 20–30%. → **A substantial minority of schizophrenia is treatment-resistant; exact prevalence depends on operational definition and cohort, so the number is optional rather than a core board anchor.**
  - Placement: `FOLLOWUP`
  - Source: TRRIP/TRS epidemiology
- `MODIFY` — Non-adherence accounts for up to 50% of apparent resistance. → **DROP_NUMBER_KEEP_QUALITATIVE: adherence failure and inadequate exposure are major causes of pseudoresistance and must be actively excluded.**
  - Placement: `BOARD_FACT`
  - Source: TRRIP consensus
- `MODIFY` — Clozapine is the sole evidence-based medication and is mandated immediately after two failures. → **Clozapine is the established treatment of choice and NICE says it should be offered after two adequate failures (with its one-SGA condition). Avoid ‘sole’ and ‘mandated’ as universal wording.**
  - Placement: `BOARD_FACT`
  - Source: NICE CG178/QS80

### Q019

- `MODIFY` — Old clozapine ANC schedule: weekly 18 weeks, fortnightly to 52 weeks, monthly thereafter. → **Update to EU 2025 PRAC wording: weekly for first 18 weeks, then monthly for the next 34 weeks to complete year 1; if no neutropenia in year 1, every 12 weeks; after 2 years without neutropenia, annually. Mild neutropenia requires monthly monitoring.**
  - Placement: `BOARD_FACT`
  - Source: EMA/PRAC clozapine neutropenia update 2025
- `KEEP` — Baseline ANC ≥1500/mm³ general and ≥1000/mm³ confirmed BEN. **Approved:** Retain under current EU product-information update.
  - Placement: `BOARD_FACT`
  - Source: EMA/PRAC clozapine update 2025
- `MODIFY` — Stop ANC <1000/mm³ general / <500 BEN and never rechallenge; old WBC rules. → **Retain the current ANC stop thresholds from product information; avoid obsolete WBC-only rules. Re-exposure after severe clozapine-induced neutropenia/agranulocytosis is generally contraindicated but exceptional specialist rechallenge decisions should not be collapsed into an unqualified universal statement.**
  - Placement: `BOARD_FACT`
  - Source: EMA/PRAC clozapine update 2025; product information
- `MODIFY` — Clozapine myocarditis: troponin/CRP/ECG are universally mandatory; cardiomyopathy needs long-term echo. → **Myocarditis surveillance protocols using symptoms, pulse, CRP/troponin and ECG are widely used specialist practice in early treatment, but exact schedules are not universally legally mandatory; echocardiography is indication/protocol-specific.**
  - Placement: `BOARD_FACT`
  - Source: Specialist clozapine myocarditis guidance; current product info
- `DROP` — Seizure level >600–1000 ng/mL with prophylactic valproate. — **Clozapine seizure risk is dose/level-related, but no single concentration mandates prophylactic valproate; manage individual risk and interactions.**
  - Placement: `FOLLOWUP`
  - Source: Clozapine TDM/seizure guidance
- `MODIFY` — Therapeutic trough 350–600 ng/mL; >1000 ng/mL toxicity. → **Use ≥350 ng/mL as a useful adequacy/response benchmark for assessing clozapine nonresponse; higher levels increase dose-related adverse effects, but 600 and 1000 are not deterministic efficacy/toxicity borders.**
  - Placement: `FOLLOWUP`
  - Source: TRRIP; clozapine TDM consensus
- `KEEP` — Interruption >48 h requires low-dose restart/re-titration. **Approved:** Retain as product-specific safety rule; restart from the product’s low initial dose (commonly 12.5 mg once/twice on day 1) and re-titrate according to SmPC and prior tolerance.
  - Placement: `BOARD_FACT`
  - Source: Current clozapine SmPC
- `MODIFY` — Smoking cessation raises clozapine by 50–100%; infection causes toxic spikes through cytokine CYP1A2 downregulation. → **Retain mechanisms: tobacco-smoke PAHs induce CYP1A2; abrupt smoking reduction/cessation can raise clozapine exposure; systemic inflammation/infection can suppress CYP1A2 and raise levels. Drop the universal percentage and use clinical/TDM-guided dose adjustment.**
  - Placement: `BOARD_FACT`
  - Source: MHRA/SPS smoking guidance; clozapine infection literature

### Q020

- `KEEP` — DSM major depressive episode ≥5 of 9 symptoms for ≥2 weeks with at least one core symptom. **Approved:** Retain as a concise DSM-specific diagnostic scaffold without reproducing criteria verbatim.
  - Placement: `BOARD_FACT`
  - Source: DSM-5-TR
- `KEEP` — PMDD prospective confirmation across at least 2 symptomatic cycles. **Approved:** Retain as DSM-specific board fact; distinguish PMDD from premenstrual exacerbation.
  - Placement: `FOLLOWUP`
  - Source: DSM-5-TR; Q020–Q027 current packet
- `KEEP` — Melancholic and atypical feature contrasts. **Approved:** Retain qualitative phenotype distinctions; exact early-morning-awakening clock cutoffs are optional and DSM-specific.
  - Placement: `FOLLOWUP`
  - Source: DSM-5-TR; descriptive psychiatry

### Q021

- `MODIFY` — Continue antidepressant 6–9 months after remission for one episode; ≥2 years after ≥2–3 episodes. → **Do not make one duration universal. Continue treatment after remission and review relapse risk, prior episodes, severity, residual symptoms, comorbidity and preference; longer-term maintenance is appropriate for higher relapse risk. A 6-month continuation anchor may be mentioned as traditional/minimum guidance, not a hard rule.**
  - Placement: `BOARD_FACT`
  - Source: NICE NG222 relapse-prevention recommendations
- `DROP` — Recurrence is ~50% after one episode, 70% after two, 90% after three. — **These textbook percentages are unstable and should not enter a premium current board book; retain that recurrence risk rises with prior episodes and residual symptoms.**
  - Placement: `BOARD_FACT`
  - Source: Modern depression prognosis literature
- `KEEP` — CBT modifies maladaptive appraisals; behavioural activation reverses avoidance/withdrawal by re-engagement. **Approved:** Retain mechanism at high level.
  - Placement: `BOARD_FACT`
  - Source: NICE NG222; CBT/BA models

### Q022

- `MODIFY` — TRD = failure of ≥2 different antidepressant classes for ≥4–8 weeks. → **Use the conventional operational definition of failure of at least two adequate antidepressant trials with adherence confirmed; they need not be different classes. Distinguish this from broader difficult-to-treat depression.**
  - Placement: `BOARD_FACT`
  - Source: Current TRD consensus; Q020–Q027 current packet
- `MODIFY` — Lithium augmentation target 0.4–0.8 mmol/L plus fixed aripiprazole/quetiapine dose tiers are the strongest strategies. → **Lithium and selected second-generation antipsychotics are evidence-based augmentation options; lithium levels are generally kept within the therapeutic range with lower targets often used for augmentation, but avoid one universal augmentation range or fixed SGA dose table.**
  - Placement: `FOLLOWUP`
  - Source: NICE NG222; SmPCs
- `MODIFY` — Esketamine is licensed for TRD and is a standard treatment step. → **Esketamine has EU marketing authorisation for selected TRD use with an oral antidepressant, but NICE does not recommend it for NHS use; label licensing versus guideline/reimbursement context.**
  - Placement: `FOLLOWUP`
  - Source: EMA Spravato EPAR; NICE TA854

### Q023

- `KEEP` — DSM mania ≥7 days or any duration if hospitalisation necessary; hypomania ≥4 days; rapid cycling ≥4 episodes/12 months. **Approved:** Retain as DSM-specific diagnostic/episode specifier anchors; ICD-11 uses different wording/duration framing.
  - Placement: `BOARD_FACT`
  - Source: DSM-5-TR; ICD-11 comparison
- `KEEP` — Bipolar I requires mania; Bipolar II requires hypomania + major depression and no mania. **Approved:** Retain as DSM-compatible high-yield distinction.
  - Placement: `BOARD_FACT`
  - Source: DSM-5-TR; ICD-11
- `MODIFY` — Bipolar I prevalence ~1%, M:F 1:1, first-degree risk 8–10%, heritability 70–85%. → **DROP_NUMBER_KEEP_QUALITATIVE: bipolar disorder is highly familial/polygenic and among the most heritable major psychiatric disorders; exact prevalence, sex ratio, FDR recurrence and heritability estimates vary by phenotype and study.**
  - Placement: `FOLLOWUP`
  - Source: Modern bipolar epidemiology/genetics reviews

### Q024

- `MODIFY` — Immediately discontinue any antidepressant in mania. → **NICE says consider stopping antidepressants in mania/hypomania; abrupt cessation may itself be problematic for some agents, so do not convert this into an unqualified ‘immediate stop’ rule.**
  - Placement: `MODEL`
  - Source: NICE CG185
- `MODIFY` — Antipsychotic or lithium/valproate are co-equal first-line options; combination required for severe mania. → **Treatment sequence is guideline-specific. NICE initially offers an antipsychotic, then another antipsychotic if needed, then adds lithium, and then considers valproate if lithium is unsuitable/ineffective. Other international guidelines differ. Label the chosen hierarchy.**
  - Placement: `BOARD_FACT`
  - Source: NICE CG185
- `DROP` — Valproate loading 20–30 mg/kg/day and serum 50–125 µg/mL as universal antimanic board anchors. — **These are regimen/TDM conventions rather than a universal psychiatry-board requirement; dosing should follow current product/guideline and reproductive restrictions.**
  - Placement: `FOLLOWUP`
  - Source: Valproate SmPC; prescribing guidance
- `MODIFY` — Valproate is absolutely contraindicated in all women of childbearing potential; ~10% malformation and 30–40% neurodevelopmental risk. → **For bipolar disorder, valproate is contraindicated during pregnancy. In girls/women able to become pregnant, use is contraindicated unless Pregnancy Prevention Programme conditions are fulfilled and alternatives are ineffective/not tolerated. Official European information cites major malformation risk around 10–11% and developmental problems up to ~30–40%; these may be retained as regulatory counselling anchors, not generic epidemiology.**
  - Placement: `BOARD_FACT`
  - Source: EMA valproate referral; current SmPC/PPP
- `KEEP` — Current male valproate reproductive precautions. **Approved:** Add: specialist initiation/supervision, discuss effective contraception for patient and female partner during treatment and at least 3 months after stopping, no sperm donation for at least 3 months, and regular review; emphasise this is precautionary based on a potential risk signal.
  - Placement: `BOARD_FACT`
  - Source: EMA PRAC/CMDh 2024; 2026 product wording

### Q025

- `MODIFY` — Quetiapine, lurasidone, OFC, cariprazine and lithium at listed doses are all current first-line bipolar-depression options. → **Do not merge international evidence and European licensing. NICE recommends options such as quetiapine or fluoxetine+olanzapine depending current treatment; lamotrigine may be considered in selected pathways. Lurasidone/cariprazine have international evidence but current EMA indications are not a generic EU bipolar-depression licence. Drop the fixed cross-guideline dose list.**
  - Placement: `BOARD_FACT`
  - Source: NICE CG185; EMA SmPCs; Q020–Q027 current packet
- `MODIFY` — SSRI/SNRI monotherapy is contraindicated in Bipolar I depression. → **Use ‘avoid/not recommended’ rather than a universal regulatory contraindication. If an antidepressant is used, it should be selected cautiously with an antimanic strategy and monitoring for switch/destabilisation.**
  - Placement: `TRAP`
  - Source: NICE CG185; CANMAT/ISBD principles

### Q026

- `KEEP` — Lithium maintenance 0.6–0.8 mmol/L, 12-hour sample. **Approved:** Retain; consider 0.8–1.0 mmol/L for selected people with relapse/persistent subthreshold symptoms under NICE.
  - Placement: `BOARD_FACT`
  - Source: NICE CG185/QS95
- `MODIFY` — Lithium reduces completed suicide by 60–80%. → **DROP_NUMBER_KEEP_QUALITATIVE: lithium has evidence for reducing suicide/self-harm risk in mood disorders, but exact effect estimates vary by study design and should not be frozen.**
  - Placement: `BOARD_FACT`
  - Source: Systematic reviews/meta-analyses of lithium and suicide
- `MODIFY` — Group psychoeducation reduces relapse 30–40%. → **DROP_NUMBER_KEEP_QUALITATIVE: psychoeducation/family-focused and rhythm-based interventions can reduce relapse and improve self-management in selected bipolar populations; effect size varies.**
  - Placement: `FOLLOWUP`
  - Source: NICE CG185; psychotherapy trials
- `KEEP` — Pole-specific maintenance tendencies. **Approved:** Retain qualitatively: lamotrigine is stronger for prevention of depressive relapse; aripiprazole evidence is stronger for mania prevention; lithium/quetiapine have broader maintenance roles.
  - Placement: `FOLLOWUP`
  - Source: NICE/SmPC/systematic evidence

### Q027

- `KEEP` — Postpartum psychosis incidence around 1–2 per 1,000 births. **Approved:** This is a sufficiently stable broad epidemiological anchor if kept as approximate and used in FOLLOWUP rather than the model answer.
  - Placement: `FOLLOWUP`
  - Source: Major postpartum psychosis reviews; NICE perinatal context
- `MODIFY` — Bipolar-associated postpartum psychosis risk 25–50%; recurrence in subsequent deliveries 50–60%. → **DROP_NUMBER_KEEP_QUALITATIVE: bipolar I or prior postpartum psychosis confers high postpartum recurrence risk and warrants specialist preconception/perinatal planning; exact recurrence estimates vary markedly by history and treatment.**
  - Placement: `BOARD_FACT`
  - Source: Perinatal bipolar/postpartum psychosis cohort/meta-analysis
- `DROP` — Postpartum blues 50–80% and postpartum depression 10–15% as must-know board numbers. — **Low-value, population-dependent prevalence numbers. Retain clinical timing/severity distinctions.**
  - Placement: `FOLLOWUP`
  - Source: Perinatal epidemiology
- `KEEP` — Postpartum psychosis is a psychiatric emergency; urgent specialist assessment and MBU admission where possible. **Approved:** Retain; NICE calls for immediate assessment and specialist perinatal involvement.
  - Placement: `MODEL`
  - Source: NICE CG192

### Q028

- `KEEP` — DSM panic disorder requires ≥1 month of worry/behavioural change; agoraphobia requires ≥2 situation types and ≥6 months. **Approved:** Retain as DSM-specific anchors; ICD-11 timing differs.
  - Placement: `BOARD_FACT`
  - Source: DSM-5-TR; ICD-11 comparison
- `KEEP` — Interoceptive exposure targets catastrophic interpretation and avoidance of bodily sensations. **Approved:** Retain.
  - Placement: `BOARD_FACT`
  - Source: CBT panic models; NICE CG113
- `MODIFY` — Long-term benzodiazepines are contraindicated in panic disorder. → **Use ‘not recommended for routine long-term treatment’ because of dependence/tolerance and poorer long-term outcomes; ‘contraindicated’ is too strong.**
  - Placement: `TRAP`
  - Source: NICE CG113

### Q029

- `KEEP` — DSM GAD ≥6 months and ≥3 associated symptoms in adults. **Approved:** Retain as DSM-specific; ICD-11 uses ‘several months’ rather than a fixed 6-month rule.
  - Placement: `BOARD_FACT`
  - Source: DSM-5-TR; ICD-11
- `KEEP` — Pregabalin alpha2-delta ligand; buspirone 5-HT1A partial agonist. **Approved:** Mechanisms are accurate; treatment positioning is jurisdiction/guideline-specific.
  - Placement: `FOLLOWUP`
  - Source: SmPCs; NICE CG113
- `KEEP` — CBT targets worry processes/intolerance of uncertainty. **Approved:** Retain qualitatively.
  - Placement: `BOARD_FACT`
  - Source: CBT GAD literature

### Q030

- `MODIFY` — Individual CBT and SSRIs/SNRIs are co-equal first-line treatment for generalized social anxiety. → **NICE offers disorder-specific individual CBT first. If the person declines CBT and prefers medication, offer an SSRI such as sertraline or escitalopram.**
  - Placement: `BOARD_FACT`
  - Source: NICE CG159
- `DROP` — Propranolol 10–40 mg has evidence only for performance-only SAD and is a board treatment fact. — **Beta-blockers may reduce peripheral autonomic symptoms in selected performance situations, but they are not a core evidence-based treatment for social anxiety disorder; drop the fixed dose and ‘only’ formulation.**
  - Placement: `FOLLOWUP`
  - Source: NICE CG159; performance-anxiety literature

### Q031

- `MODIFY` — OCD requires supramaximal SSRI doses such as escitalopram 40 mg and 12 weeks at maximum tolerated dose. → **Use licensed/SmPC dose escalation. NICE: if standard dose inadequate and tolerated after 4–6 weeks, consider gradual increase in line with SmPC; allow a sufficiently long overall trial, often up to 12 weeks. Do not teach routine supra-licensed escitalopram dosing.**
  - Placement: `BOARD_FACT`
  - Source: NICE CG31; current SSRI SmPCs
- `MODIFY` — Clomipramine or atypical-antipsychotic augmentation are immediate standard next steps. → **Clomipramine is a later option after an adequate SSRI/CBT pathway; antipsychotic augmentation is a specialist strategy for resistant OCD after standard approaches.**
  - Placement: `FOLLOWUP`
  - Source: NICE CG31
- `KEEP` — ERP breaks the obsession–compulsion negative-reinforcement cycle; inhibitory-learning framing is contemporary. **Approved:** Retain without claiming one exclusive neurobiological mechanism.
  - Placement: `BOARD_FACT`
  - Source: ERP literature
- `KEEP` — Hoarding disorder is distinct from OCD. **Approved:** Retain, while avoiding an overly simple ego-syntonic versus ego-dystonic dichotomy.
  - Placement: `FOLLOWUP`
  - Source: DSM-5-TR; ICD-11

### Q032

- `KEEP` — DSM PTSD symptoms >1 month; ICD-11 CPTSD = PTSD + disturbances in self-organisation. **Approved:** Retain as system-specific board distinctions.
  - Placement: `BOARD_FACT`
  - Source: DSM-5-TR; ICD-11
- `MODIFY` — Prazosin is a standard pharmacological treatment for PTSD nightmares. → **Prazosin may be considered for trauma-related nightmares in some guidelines/populations, but it is not a universal first-line PTSD treatment; trauma-focused psychotherapy remains central.**
  - Placement: `FOLLOWUP`
  - Source: Current PTSD guidelines
- `MODIFY` — EMDR works because bilateral stimulation facilitates trauma-memory reprocessing. → **EMDR is evidence-based trauma-focused psychotherapy; bilateral stimulation is part of the protocol, but the precise mechanism of benefit is not established and should not be taught as causal fact.**
  - Placement: `BOARD_FACT`
  - Source: NICE NG116; EMDR evidence

### Q033

- `MODIFY` — ASD lasts 3 days–1 month and automatically converts to PTSD if >1 month. → **DSM acute stress disorder lasts 3 days to 1 month after trauma. If clinically significant trauma symptoms persist beyond 1 month, reassess for PTSD; conversion is not automatic. ICD-11 instead treats acute stress reaction as a non-disorder response.**
  - Placement: `BOARD_FACT`
  - Source: DSM-5-TR; ICD-11
- `MODIFY` — Adjustment disorder must start within 3 months and resolve within 6 months after stressor termination. → **That is DSM-specific. ICD-11 usually expects onset within about 1 month and symptoms generally resolve within 6 months after the stressor/consequences end unless stressor persists. Label the classification system.**
  - Placement: `FOLLOWUP`
  - Source: DSM-5-TR; ICD-11

### Q034

- `KEEP` — Reality testing is preserved in depersonalization/derealization disorder. **Approved:** Retain as a key DSM discriminator.
  - Placement: `BOARD_FACT`
  - Source: DSM-5-TR
- `MODIFY` — DID is strongly caused by severe chronic childhood maltreatment. → **Trauma and childhood maltreatment are strongly associated with DID in clinical literature, but causal direction and ascertainment are complex; avoid presenting trauma as a necessary causal criterion.**
  - Placement: `FOLLOWUP`
  - Source: Dissociation literature; DSM-5-TR
- `KEEP` — TGA and temporal lobe epilepsy are important organic differentials for amnestic/dissociative presentations. **Approved:** Retain qualitatively; TGA duration <24 h is a neurological diagnostic anchor, not a general dissociation criterion.
  - Placement: `FOLLOWUP`
  - Source: Neurology diagnostic criteria

### Q035

- `KEEP` — SSD and IAD are distinguished by prominent somatic symptoms versus minimal/absent symptoms with illness preoccupation. **Approved:** Retain, noting that SSD does not require symptoms to be medically unexplained.
  - Placement: `BOARD_FACT`
  - Source: DSM-5-TR; Q028–Q036 current packet
- `KEEP` — DSM health preoccupation/excessive response persists ≥6 months. **Approved:** Retain as DSM-specific; do not generalise as an ICD-11 rule.
  - Placement: `FOLLOWUP`
  - Source: DSM-5-TR
- `KEEP` — Old somatization/hypochondriasis/pain-disorder framework is historical. **Approved:** Retain as HISTORICAL_EXAM_FACT only.
  - Placement: `HISTORICAL`
  - Source: DSM-IV/ICD-10 history

### Q036

- `MODIFY` — Functional seizures are supported by closed eyes/resistance to opening and a normal post-ictal EEG. → **Diagnosis should rest on positive semiology and, when needed, video-EEG capture of a typical event without an ictal epileptiform correlate. A normal interictal or post-event EEG alone does not diagnose functional seizures.**
  - Placement: `TRAP`
  - Source: AAN Functional Seizures Guideline 2025
- `KEEP` — Hoover sign/hip abductor inconsistency and tremor entrainment/distractibility are positive FND signs. **Approved:** Retain as examples of positive rule-in signs when appropriately elicited.
  - Placement: `BOARD_FACT`
  - Source: Modern FND neurology guidance
- `MODIFY` — TPJ hypoactivity and abnormal limbic-motor connectivity explain FND. → **Predictive-processing, agency and limbic–motor network models are active research frameworks; label as emerging neurobiology rather than established mechanism.**
  - Placement: `FOLLOWUP`
  - Source: Current FND neurobiology reviews
- `KEEP` — FND is involuntary and distinct from factitious disorder and malingering. **Approved:** Retain.
  - Placement: `TRAP`
  - Source: DSM-5-TR; AAN/neurology guidance

### Q037

- `KEEP` — DSM SUD severity: 2–3 mild, 4–5 moderate, ≥6 severe among 11 criteria. **Approved:** Retain as DSM-specific board fact without reproducing criteria text.
  - Placement: `BOARD_FACT`
  - Source: DSM-5-TR
- `MODIFY` — Tobacco smoke lowers clozapine/olanzapine levels by ~50%. → **Retain the mechanism—PAHs in smoke induce CYP1A2; nicotine/NRT do not. Drop a universal percentage and use clinical/TDM-guided adjustment.**
  - Placement: `BOARD_FACT`
  - Source: MHRA/SPS smoking interaction guidance
- `DROP` — Fixed urine toxicology detection windows for cannabinoids, cocaine, amphetamines, opioids and benzodiazepines. — **Detection depends on assay, dose, chronicity, renal function, specimen and analyte; not suitable as a compact psychiatry-board truth table.**
  - Placement: `FOLLOWUP`
  - Source: Laboratory toxicology principles

### Q038

- `MODIFY` — Alcohol withdrawal follows exact 6–12 h autonomic, 12–24 h hallucinosis, 24–48 h seizures, 48–72 h DT sequence. → **Retain only as approximate typical timing windows with substantial overlap and variation; clinical severity/history matter more than the clock.**
  - Placement: `BOARD_FACT`
  - Source: Current alcohol-withdrawal guidance
- `MODIFY` — Diazepam/chlordiazepoxide are preferred in healthy liver; lorazepam/oxazepam mandatory in hepatic impairment/elderly. → **Long-acting benzodiazepines are often useful for withdrawal; lorazepam/oxazepam are often preferred when hepatic oxidative metabolism is impaired. ‘Mandatory’ is too strong.**
  - Placement: `BOARD_FACT`
  - Source: Current alcohol-withdrawal guidance
- `MODIFY` — Wernicke: IV thiamine 500 mg TDS and it MUST precede any glucose. → **For suspected Wernicke encephalopathy, current UK guidance uses IV thiamine 300–500 mg three times daily for 3–5 days, with further daily IV treatment if symptoms persist, plus magnesium correction. Give thiamine before or with carbohydrate when feasible, but do not delay emergency glucose for hypoglycaemia.**
  - Placement: `BOARD_FACT`
  - Source: UK alcohol-treatment guideline 2025/26; Q037–Q044 current packet
- `MODIFY` — CIWA-Ar <8–10 needs no medication; >10–15 mandates symptom-triggered benzodiazepines. → **CIWA-Ar is a symptom-severity aid in suitable communicative patients; cut-offs and medication protocols are local/guideline-specific and it is not a diagnostic test or safe sole guide in complicated withdrawal.**
  - Placement: `FOLLOWUP`
  - Source: Alcohol-withdrawal protocols

### Q039

- `MODIFY` — Acamprosate is an NMDA antagonist and GABA-A modulator with defined chemical-balancing mechanism. → **Acamprosate’s clinically relevant mechanism is not fully settled; it modulates glutamatergic/GABAergic signalling. Avoid an over-specific receptor claim.**
  - Placement: `FOLLOWUP`
  - Source: Acamprosate SmPC/pharmacology reviews
- `MODIFY` — Naltrexone is hepatotoxic and strictly contraindicated with opioids. → **Naltrexone is an opioid-receptor antagonist; it must not be initiated in current opioid use/dependence because of precipitated withdrawal and blocks opioid analgesia. Hepatic contraindications/monitoring follow the current product label; ‘hepatotoxic’ as a blanket descriptor is misleading.**
  - Placement: `BOARD_FACT`
  - Source: Naltrexone SmPC; NICE alcohol guidance
- `KEEP` — Disulfiram inhibits aldehyde dehydrogenase and creates an aversive acetaldehyde reaction. **Approved:** Retain, noting supervised/selected use and contraindications.
  - Placement: `FOLLOWUP`
  - Source: Disulfiram SmPC
- `MODIFY` — Nalmefene is an on-demand universal alcohol-reduction option. → **It is a jurisdiction- and licensing-specific option for selected adults with high drinking-risk levels; not a universal board-treatment step.**
  - Placement: `FOLLOWUP`
  - Source: EMA Selincro EPAR/current national guidance

### Q040

- `MODIFY` — Methadone half-life is 24–36 h. → **Methadone has a long and highly variable elimination half-life with accumulation risk; drop a single range as a dosing rule.**
  - Placement: `FOLLOWUP`
  - Source: Methadone SmPC/pharmacology
- `KEEP` — Buprenorphine is a high-affinity partial µ-opioid agonist and can precipitate withdrawal by displacing full agonists before sufficient withdrawal. **Approved:** Retain; this is a high-value safety mechanism.
  - Placement: `BOARD_FACT`
  - Source: Buprenorphine SmPC; opioid-treatment guidelines
- `MODIFY` — Start buprenorphine at COWS ≥8–12. → **Initiate when objective withdrawal is established; the exact COWS threshold/timing depends on opioid type, formulation and fentanyl exposure. Do not teach one universal number.**
  - Placement: `BOARD_FACT`
  - Source: Current opioid-use-disorder guidance
- `MODIFY` — Sublingual naloxone has <5% bioavailability and always precipitates withdrawal if injected. → **Retain the diversion-deterrence rationale: naloxone has low sublingual bioavailability relative to parenteral use and can antagonise opioids if injected. Drop the fixed percentage/absolute outcome.**
  - Placement: `FOLLOWUP`
  - Source: Buprenorphine/naloxone SmPC
- `MODIFY` — Naloxone 0.4–2 mg IV/IM or 1.8–4 mg IN is the emergency dose. → **Naloxone dosing is product/route and clinical-goal specific; titrate to adequate ventilation and repeat because naloxone may wear off before the opioid. Avoid one universal cross-product dose table unless a Greek/local product is specified.**
  - Placement: `BOARD_FACT`
  - Source: Naloxone SmPC/emergency toxicology

### Q041

- `MODIFY` — CHS triad requires compulsive hot-water bathing and resolves permanently only with complete abstinence. → **CHS is recurrent nausea/vomiting in chronic cannabis exposure; hot bathing is characteristic but not required. Sustained cannabis cessation is the definitive preventive treatment, though symptom resolution/relapse varies.**
  - Placement: `BOARD_FACT`
  - Source: Current CHS reviews
- `MODIFY` — CBD is simply a CB1 negative allosteric modulator with antipsychotic/anxiolytic profile. → **THC is a partial CB1/CB2 agonist and drives intoxication/psychotomimetic effects. CBD has complex multi-target pharmacology; do not reduce it to one CB1 mechanism or present antipsychotic efficacy as established routine treatment.**
  - Placement: `FOLLOWUP`
  - Source: Cannabinoid pharmacology reviews
- `MODIFY` — Cannabis withdrawal always starts within 24–72 h. → **Symptoms typically emerge within the first several days after cessation, but timing varies; use as an approximate course, not a criterion.**
  - Placement: `FOLLOWUP`
  - Source: DSM-5-TR; cannabis withdrawal reviews

### Q042

- `KEEP` — Cocaine mainly blocks monoamine reuptake transporters; amphetamines increase monoamine release/reverse transport and affect VMAT2. **Approved:** Retain as a useful mechanistic contrast, without implying either drug acts through only one target.
  - Placement: `BOARD_FACT`
  - Source: Stimulant pharmacology
- `DROP` — Pure beta-blockers are categorically contraindicated in acute cocaine toxicity because of unopposed alpha stimulation. — **This blanket teaching is outdated. Benzodiazepines remain first-line for sympathomimetic agitation/hypertension; if beta blockade is clinically required, agent and context matter, and combined alpha/beta blockade is often preferred.**
  - Placement: `TRAP`
  - Source: Contemporary stimulant-toxicity guidance
- `KEEP` — Stimulant psychosis may include paranoia, hallucinations and formication. **Approved:** Retain qualitatively.
  - Placement: `FOLLOWUP`
  - Source: Clinical toxicology/psychiatry

### Q043

- `MODIFY` — Switch all dependent patients to diazepam and taper 5–10% every 1–2 weeks over 8–12+ weeks. → **Tapering is individualised. ASAM 2025 suggests initial reductions around 5–10% every 2–4 weeks and generally not exceeding 25% every 2 weeks; transition to a longer-acting benzodiazepine may help selected patients but is not mandatory.**
  - Placement: `BOARD_FACT`
  - Source: ASAM Joint Benzodiazepine Tapering Guideline 2025
- `KEEP` — Flumazenil can precipitate severe withdrawal/seizures in chronic benzodiazepine dependence or mixed pro-convulsant overdose. **Approved:** Retain as a toxicology safety fact; use requires specialist indication.
  - Placement: `TRAP`
  - Source: Toxicology guidance
- `KEEP` — Benzodiazepine withdrawal can cause seizures and delirium. **Approved:** Retain.
  - Placement: `BOARD_FACT`
  - Source: ASAM 2025; SmPCs

### Q044

- `KEEP` — DSM gambling disorder is in addictive disorders and requires ≥4 of 9 criteria over 12 months. **Approved:** Retain as DSM-specific board fact.
  - Placement: `BOARD_FACT`
  - Source: DSM-5-TR
- `KEEP` — Gambler’s fallacy and near-miss cognitions are clinically relevant cognitive distortions. **Approved:** Retain qualitatively.
  - Placement: `FOLLOWUP`
  - Source: Gambling-disorder literature

### Q045

- `MODIFY` — 4AT score ≥4 equals delirium diagnosis. → **4AT ≥4 indicates possible delirium and/or cognitive impairment and should trigger clinical assessment; 4AT is a screening tool, not a stand-alone diagnosis.**
  - Placement: `BOARD_FACT`
  - Source: 4AT official guidance; NICE CG103
- `MODIFY` — CAM is the current general-hospital preferred tool alongside 4AT. → **NICE 2023 uses 4AT in general hospital/long-term care; CAM-ICU or ICDSC in critical care/recovery. Standard CAM remains valid elsewhere but is not NICE’s general-setting first choice.**
  - Placement: `FOLLOWUP`
  - Source: NICE CG103 2023
- `DROP` — Hypoactive/hyperactive/mixed delirium are 50/25/25%, with hypoactive having the worst mortality. — **Subtype prevalence and mortality estimates vary; retain only that hypoactive delirium is common and easily missed.**
  - Placement: `BOARD_FACT`
  - Source: Delirium reviews
- `MODIFY` — Haloperidol 0.5–1 mg or quetiapine are strict rescue drugs; benzodiazepines are contraindicated except withdrawal/catatonia. → **Antipsychotics do not treat the underlying delirium. NICE allows short-term low-dose haloperidol for severe distress/risk when de-escalation fails; PD/DLB are key contraindications. Benzodiazepines are not routine delirium treatment but may be appropriate for alcohol/sedative withdrawal or catatonia.**
  - Placement: `BOARD_FACT`
  - Source: NICE CG103; MHRA haloperidol safety

### Q046

- `KEEP` — Major versus mild NCD/dementia distinction hinges on interference with independent everyday functioning. **Approved:** Retain as a high-yield functional distinction; terminology differs between DSM and ICD.
  - Placement: `BOARD_FACT`
  - Source: DSM-5-TR; ICD-11
- `MODIFY` — MoCA <26, MMSE <24, ACE-III <88 are diagnostic thresholds. → **Treat these only as screening anchors whose operating characteristics vary with age, education, language and setting. A normal screen does not exclude dementia; no score alone diagnoses a major NCD.**
  - Placement: `TRAP`
  - Source: NICE NG97; instrument validation literature
- `MODIFY` — MRI MTA/Fazekas/Koedam scores are routine diagnostic thresholds. → **These visual scales can support specialist imaging interpretation but are not required board-level diagnostic cut-offs and should not replace clinical/subtype assessment.**
  - Placement: `FOLLOWUP`
  - Source: NICE NG97; neuroradiology guidance
- `MODIFY` — Every suspected dementia needs a fixed reversible-dementia blood panel. → **Perform physical examination and targeted blood/urine tests for reversible/contributing causes based on clinical context; do not teach a universal one-size panel.**
  - Placement: `MODEL`
  - Source: NICE NG97

### Q047

- `KEEP` — AChEI and memantine core mechanisms. **Approved:** Donepezil/galantamine are reversible AChE inhibitors; rivastigmine inhibits AChE and BuChE; memantine is an uncompetitive NMDA-receptor antagonist. Retain one-line mechanisms if useful.
  - Placement: `FOLLOWUP`
  - Source: Current SmPCs; NICE NG97
- `MODIFY` — CSF/plasma ATN biomarkers ‘confirm Alzheimer disease’. → **Biomarkers establish amyloid/tau pathology and increase etiological confidence in the appropriate clinical syndrome; they do not replace clinical assessment or make every biomarker-positive person clinically demented.**
  - Placement: `BOARD_FACT`
  - Source: NICE NG97; Alzheimer biomarker guidelines
- `MODIFY` — Lecanemab/donanemab require serial MRI and APOE genotyping for all AD. → **For the current EU-authorised restricted early-AD indications, confirmed amyloid pathology, APOE ε4 eligibility assessment and MRI ARIA monitoring are treatment-specific requirements. Do not generalise them to ordinary AD diagnosis.**
  - Placement: `FOLLOWUP`
  - Source: EMA Leqembi/Kisunla EPARs 2025–26
- `KEEP` — ARIA-E/ARIA-H are the defining anti-amyloid safety issue. **Approved:** Retain qualitatively; any incidence percentages must remain product/trial/genotype-specific.
  - Placement: `BOARD_FACT`
  - Source: EMA Leqembi/Kisunla EPARs

### Q048

- `KEEP` — DLB/PDD 1-year rule and four current DLB core clinical features. **Approved:** Retain; explicitly label the 1-year rule as an operational classification convention, not a biological boundary.
  - Placement: `BOARD_FACT`
  - Source: 2017 DLB Consortium; NICE NG97
- `MODIFY` — Neuroleptic sensitivity causes 2–3× mortality. → **DROP_NUMBER_KEEP_QUALITATIVE: severe antipsychotic sensitivity is a major safety warning in DLB; avoid one mortality multiplier.**
  - Placement: `BOARD_FACT`
  - Source: DLB Consortium; NICE NG97
- `KEEP` — Reduced striatal DAT, low cardiac MIBG uptake and PSG REM-without-atonia are indicative biomarkers. **Approved:** Retain with caveats: availability/confounders matter and biomarkers support rather than replace syndrome assessment.
  - Placement: `FOLLOWUP`
  - Source: 2017 DLB Consortium
- `MODIFY` — Dopamine-agonist ICDs occur in 15–20% because D3 stimulation causes gambling/hypersexuality/spending. → **DROP_NUMBER_KEEP_QUALITATIVE: dopamine agonists are a major medication risk for ICDs. Mesolimbic/D3 pharmacology is relevant but not a sufficient single-cause explanation.**
  - Placement: `FOLLOWUP`
  - Source: NICE NG71; PD ICD literature

### Q049

- `MODIFY` — FTD is autosomal dominant in 30–40%; C9orf72 most common. → **Family/genetic causes are important and C9orf72, MAPT and GRN are high-yield genes, but drop a fixed inheritance percentage and ‘most common’ across all populations.**
  - Placement: `FOLLOWUP`
  - Source: FTD genetics reviews
- `KEEP` — Do not offer AChEIs or memantine for FTD. **Approved:** Retain as current NICE guidance.
  - Placement: `TRAP`
  - Source: NICE NG97
- `MODIFY` — SSRIs/trazodone are preferred treatment for FTD compulsions/hyperorality. → **They may be used off-label for selected behavioural symptoms, with modest evidence; do not frame as established disease treatment.**
  - Placement: `FOLLOWUP`
  - Source: FTD clinical reviews

### Q050

- `MODIFY` — CADASIL anterior temporal/external-capsule MRI lesions are pathognomonic. → **These locations are characteristic and can strongly support suspicion, but they are not pathognomonic; diagnosis integrates phenotype/family history and NOTCH3 testing.**
  - Placement: `FOLLOWUP`
  - Source: CADASIL imaging/genetics literature
- `MODIFY` — All VCI requires aggressive BP/statin/antiplatelet treatment. → **Manage vascular risk and secondary stroke prevention according to standard cardiovascular/cerebrovascular indications; do not prescribe antiplatelet/statin solely because cognitive impairment is labelled vascular.**
  - Placement: `BOARD_FACT`
  - Source: NICE NG97; vascular prevention guidelines
- `KEEP` — AChEI/memantine are not routine for pure vascular dementia; consider when comorbid AD/PDD/DLB suspected. **Approved:** Retain.
  - Placement: `TRAP`
  - Source: NICE NG97

### Q051

- `DROP` — Antipsychotics in dementia increase stroke ~3× and mortality 1.5–1.7×. — **Do not freeze the old Oxford risk multipliers. Retain that cerebrovascular events and mortality are increased and discuss individual risk.**
  - Placement: `BOARD_FACT`
  - Source: NICE NG97; regulatory warnings
- `MODIFY` — Risperidone 0.25–1 mg for ≤6–12 weeks is the licensed BPSD rule. → **Current European/NICE licensing anchor: risperidone may be used up to 6 weeks for persistent aggression in moderate-to-severe Alzheimer dementia unresponsive to non-pharmacological approaches when there is risk of harm. Dose follows SmPC; do not generalise 6–12 weeks to all BPSD.**
  - Placement: `BOARD_FACT`
  - Source: NICE NG97; EMA/Risperdal referral
- `KEEP` — Reassess antipsychotic need at least every 6 weeks and use lowest effective dose/shortest time. **Approved:** Retain as current NICE principle.
  - Placement: `BOARD_FACT`
  - Source: NICE NG97
- `DROP` — About 70% of BPSD resolves with non-pharmacological management. — **No stable universal response percentage; keep non-pharmacological/environmental interventions first.**
  - Placement: `BOARD_FACT`
  - Source: NICE NG97
- `MODIFY` — Trazodone/SSRIs/memantine are standard non-antipsychotic options for agitation. → **Treat causes and use syndrome-specific evidence; some agents may be considered for selected symptoms, but there is no one general medication ladder for BPSD.**
  - Placement: `FOLLOWUP`
  - Source: NICE NG97; BPSD reviews

### Q052

- `MODIFY` — Diogenes syndrome is a clinical triad of squalor + self-neglect + no shame/refusal. → **Use ‘severe self-neglect/squalor’ as the current problem presentation. ‘Diogenes syndrome’ is historical/descriptive, heterogeneous and not a single diagnosis.**
  - Placement: `HISTORICAL`
  - Source: Current geriatric/self-neglect practice
- `KEEP` — Common drivers include dementia/frontal dysfunction, depression, psychosis, substance use, hoarding and delirium. **Approved:** Retain as differential contributors.
  - Placement: `BOARD_FACT`
  - Source: Q052–Q058 current packet
- `MODIFY` — Judicial support/Civil Code automatically authorises intervention when severe self-neglect exists. → **Capacity/refusal and judicial-support mechanisms are separate legal questions. Severe self-neglect alone does not create a general power for non-urgent forced social intervention and is not an independent Art 95 involuntary-admission criterion.**
  - Placement: `TRAP`
  - Source: Law 3418/2005; Law 2071/1992; Civil Code judicial support

### Q053

- `KEEP` — Rapid/subacute psychiatric-neurological deterioration with seizures/catatonia/cognitive decline/movements/autonomic instability should trigger AE work-up. **Approved:** Retain.
  - Placement: `MODEL`
  - Source: AE best-practice recommendations JNNP 2021
- `MODIFY` — CSF anti-GluN1 is ‘superior’ to serum and extreme delta brush occurs in ~30%. → **Test both serum and CSF. CSF is particularly important/sensitive-specific for NMDAR antibodies, while some antibodies such as LGI1 may be more sensitive in serum. Extreme delta brush is characteristic but uncommon and not required; drop a fixed percentage.**
  - Placement: `BOARD_FACT`
  - Source: Abboud et al., JNNP 2021
- `MODIFY` — First-line AE therapy is methylprednisolone 1 g/day ×5 plus IVIG/PLEX. → **High-dose IV corticosteroids, IVIG and/or plasma exchange are first-line immunotherapies; exact combinations/durations depend on severity and specialist protocol. Do not freeze one mandatory regimen.**
  - Placement: `BOARD_FACT`
  - Source: Abboud et al., JNNP 2021
- `MODIFY` — LGI1 faciobrachial dystonic seizures are pathognomonic and hyponatraemia is refractory. → **FBDS are highly characteristic of LGI1 encephalitis and hyponatraemia is common; neither wording should be absolute.**
  - Placement: `FOLLOWUP`
  - Source: AE/LGI1 consensus literature

### Q054

- `MODIFY` — PIP has a fixed 12–72 h lucid interval. → **The lucid interval remains high-yield, but describe it as hours to several days, with psychosis generally beginning within a week after seizure cluster; no single interval is universally required.**
  - Placement: `BOARD_FACT`
  - Source: Contemporary epilepsy-psychosis reviews
- `MODIFY` — Geschwind syndrome tetrad is a current epilepsy syndrome. → **Retain only as HISTORICAL_EXAM_FACT/contested personality description; do not present as established contemporary nosology.**
  - Placement: `HISTORICAL`
  - Source: Historical epilepsy psychopathology; modern reviews
- `MODIFY` — Levetiracetam psychiatric adverse effects occur in ~10–15%. → **Retain irritability/aggression, depression/anxiety and occasional psychotic symptoms as recognised adverse effects; drop a single prevalence number.**
  - Placement: `BOARD_FACT`
  - Source: Current levetiracetam SmPC
- `KEEP` — Topiramate can cause cognitive/word-finding problems; medication review matters in psychiatric change. **Approved:** Retain qualitatively.
  - Placement: `FOLLOWUP`
  - Source: Current ASM SmPCs

### Q055

- `DROP` — PTA duration categories mild <24 h, moderate 1–7 d, severe >7 d are universal and PTA is the single most reliable outcome predictor. — **PTA remains an important severity/prognostic marker, but contemporary TBI severity systems combine PTA with GCS, LOC and imaging and use differing thresholds. Drop the universal table/superlative.**
  - Placement: `BOARD_FACT`
  - Source: INCOG 2.0 PTA Guideline 2023
- `KEEP` — Orbitofrontal/dorsolateral/ACC injury patterns map to disinhibition/executive dysfunction/apathy. **Approved:** Retain as useful neuropsychiatric associations, not deterministic lesion rules.
  - Placement: `FOLLOWUP`
  - Source: Neuropsychiatry/TBI literature
- `KEEP` — Acute PTA/confusional agitation should be managed primarily with environmental/rehabilitative strategies. **Approved:** Retain.
  - Placement: `MODEL`
  - Source: INCOG 2.0

### Q056

- `KEEP` — Liaison psychiatry should clarify referral question and integrate medical disease, treatment, psychiatric history, behaviour and social context. **Approved:** Retain.
  - Placement: `MODEL`
  - Source: Current liaison psychiatry practice
- `MODIFY` — Proactive liaison significantly reduces LOS and readmission in high-risk units. → **Proactive/integrated liaison models may improve efficiency and some outcomes, but effects vary by service design and population; not a universal board fact.**
  - Placement: `FOLLOWUP`
  - Source: Liaison service evaluations

### Q057

- `KEEP` — Apathy is reduced motivation/goal-directed activity, usually without pervasive sadness/guilt/hopelessness/suicidality. **Approved:** Retain as a discriminator while recognising overlap/anhedonia.
  - Placement: `BOARD_FACT`
  - Source: 2018 apathy consensus; Q052–Q058 current packet
- `MODIFY` — Apathy is specifically an ACC/ventral-striatal dopamine disorder. → **Frontal-subcortical/ACC–ventral striatal circuitry is implicated, but apathy is a multidimensional syndrome across disorders; do not reduce it to one neurotransmitter/circuit.**
  - Placement: `FOLLOWUP`
  - Source: Apathy consensus/reviews
- `DROP` — SSRIs do not treat apathy and pro-dopaminergic drugs or AChEIs are preferred. — **Treatment is cause-specific. SSRIs may contribute to emotional blunting/apathy-like symptoms in some patients, but there is no universal pro-dopaminergic/AChEI treatment rule.**
  - Placement: `TRAP`
  - Source: Apathy treatment literature

### Q058

- `MODIFY` — CBS requires preserved insight, normal cognition, no auditory hallucinations/delusions/parkinsonism. → **CBS is recurrent visual hallucinations associated with significant visual impairment, usually with preserved or developing insight. Partial/fluctuating insight can occur. Cognitive/neurological comorbidity should prompt careful differential diagnosis rather than automatically excluding CBS.**
  - Placement: `BOARD_FACT`
  - Source: Ophthalmology/CBS reviews 2022–26
- `MODIFY` — CBS hallucinations are necessarily Lilliputian/faces/geometric patterns. → **They are commonly complex/formed but can vary; phenomenology is supportive, not diagnostic.**
  - Placement: `FOLLOWUP`
  - Source: CBS reviews
- `KEEP` — Reassurance/education and optimisation of vision are treatment backbone; routine antipsychotics are not indicated. **Approved:** Retain.
  - Placement: `MODEL`
  - Source: Ophthalmology/CBS reviews

### Q059

- `KEEP` — DSM adult ADHD uses ≥5 symptoms in either domain and some symptoms before age 12, with impairment in multiple settings. **Approved:** Retain as DSM-specific scaffold.
  - Placement: `BOARD_FACT`
  - Source: DSM-5-TR; NICE NG87
- `MODIFY` — Documented childhood onset is required. → **A childhood diagnosis, school records or parental collateral are not mandatory. A credible developmental history supporting symptoms before 12 is required; absent collateral increases uncertainty rather than automatically excluding ADHD.**
  - Placement: `TRAP`
  - Source: NICE NG87/QS39; DSM-5-TR
- `KEEP` — ADHD is developmental/trait-like whereas bipolar disorder is episodic. **Approved:** Retain as high-yield discriminator, without claiming ADHD symptoms are literally unchanging across contexts.
  - Placement: `BOARD_FACT`
  - Source: NICE NG87; diagnostic principles

### Q060

- `KEEP` — Autism diagnosis uses social-communication/social-interaction domain plus restricted/repetitive/sensory domain with developmental onset. **Approved:** Retain.
  - Placement: `BOARD_FACT`
  - Source: DSM-5-TR; ICD-11; NICE CG142
- `MODIFY` — ADOS-2/ADI-R are diagnostic instruments and sensory criteria prove adult autism. → **Structured instruments can support assessment but no scale/instrument independently establishes or excludes autism; developmental history and clinical synthesis remain central.**
  - Placement: `TRAP`
  - Source: NICE CG142
- `MODIFY` — Masking is common in adult females and causes autistic burnout/late diagnosis. → **Camouflaging can contribute to under-recognition, including in some women and adults, but occurs across genders and is not a diagnostic criterion. ‘Autistic burnout’ is a useful lived-experience/research construct but not a formal diagnostic requirement.**
  - Placement: `FOLLOWUP`
  - Source: Adult-autism camouflaging reviews

### Q061

- `KEEP` — Current ID diagnosis requires intellectual + adaptive-functioning impairment with developmental onset; severity is not rigid IQ bins. **Approved:** Retain.
  - Placement: `BOARD_FACT`
  - Source: ICD-11; DSM-5-TR
- `KEEP` — New aggression/insomnia in minimally verbal ID requires medical/pain/medication causes first. **Approved:** Retain; avoid diagnostic overshadowing.
  - Placement: `MODEL`
  - Source: NICE NG11
- `MODIFY` — Trisomy 21 gives virtually universal Alzheimer neuropathology by age 40. → **APP triplication explains very high age-related AD neuropathology/risk in Down syndrome, but the exact age/universality claim is not needed and can mislead clinically. Keep qualitative.**
  - Placement: `FOLLOWUP`
  - Source: Down syndrome–AD literature

### Q062

- `DROP` — AN diagnosis requires BMI <18.5 and DSM severity is the diagnostic threshold. — **Current AN diagnosis should not be reduced to a fixed BMI. Low weight relative to context, restriction/behaviour preventing weight restoration and weight/shape psychopathology are central; amenorrhoea is not required.**
  - Placement: `TRAP`
  - Source: DSM-5-TR; ICD-11; NICE NG69
- `MODIFY` — BMI severity categories are mandatory board facts. → **DSM includes BMI-based adult severity specifiers, but they are not diagnostic thresholds and clinical severity can diverge from BMI; if retained, label DSM specifiers only.**
  - Placement: `FOLLOWUP`
  - Source: DSM-5-TR
- `KEEP` — Adult AN treatment = nutritional rehabilitation + ED-focused psychotherapy; medication is non-primary. **Approved:** Retain.
  - Placement: `MODEL`
  - Source: NICE NG69
- `MODIFY` — Low-dose olanzapine is an evidence-based standard adjunct for core AN. → **Olanzapine may be considered off-label in selected patients; it is not a primary treatment for AN and should not displace nutritional/psychological treatment.**
  - Placement: `FOLLOWUP`
  - Source: Current AN treatment evidence
- `KEEP` — ARFID mechanisms and absence of weight/shape psychopathology. **Approved:** Retain.
  - Placement: `BOARD_FACT`
  - Source: DSM-5-TR; ICD-11

### Q063

- `MODIFY` — MEED admission criteria are BMI <13, HR <40, SBP <90, temp <35.5, postural drop >20, SUSS <2. → **MEED uses multidomain traffic-light risk, not a single admission checklist. BMI <13, waking pulse <40, temperature <35.5°C and glucose <3.0 mmol/L are useful red examples; admission depends on overall physiological decline and ability to monitor/refeed safely.**
  - Placement: `BOARD_FACT`
  - Source: RCPsych MEED 2022; NICE NG69
- `KEEP` — Refeeding can cause phosphate, potassium and magnesium shifts with cardiac/neurological/organ complications. **Approved:** Retain at high level.
  - Placement: `BOARD_FACT`
  - Source: MEED 2022
- `DROP` — Start all high-risk refeeding at 20–30 kcal/kg/day or 1000–1200 kcal/day and check electrolytes daily for 7–14 days. — **Current practice is risk-stratified and increasingly avoids prolonged underfeeding. Exact starting energy and laboratory frequency depend on severity, setting and local protocol; teach monitored, assertive refeeding rather than one universal schedule.**
  - Placement: `TRAP`
  - Source: MEED 2022; contemporary refeeding evidence
- `KEEP` — Thiamine and close phosphate/K/Mg/glucose/fluid monitoring are core high-risk refeeding principles. **Approved:** Retain; prophylaxis/replacement follows risk and local protocol.
  - Placement: `BOARD_FACT`
  - Source: MEED 2022

### Q064

- `KEEP` — DSM BN frequency ≥1/week for 3 months. **Approved:** Retain as DSM-specific scaffold.
  - Placement: `BOARD_FACT`
  - Source: DSM-5-TR
- `MODIFY` — Normal/elevated BMI is what distinguishes BN from AN binge-purge subtype. → **People with BN are often not significantly underweight, but diagnosis depends on whether AN low-weight architecture is met, not a single BMI boundary.**
  - Placement: `TRAP`
  - Source: DSM-5-TR; ICD-11
- `KEEP` — Fluoxetine 60 mg/day is a current licensed adult BN medication fact. **Approved:** Retain as an adjunct to psychotherapy, not sole treatment.
  - Placement: `BOARD_FACT`
  - Source: Current fluoxetine SmPC
- `KEEP` — Bupropion is contraindicated in patients with current or prior anorexia/bulimia in relevant product information because of seizure risk. **Approved:** Retain as a prescribing safety fact, with jurisdiction/product labelling acknowledged.
  - Placement: `FOLLOWUP`
  - Source: Current bupropion SmPC

### Q065

- `KEEP` — Chronic insomnia diagnostic anchor ≥3 nights/week for ≥3 months with adequate opportunity and daytime impairment. **Approved:** Retain as DSM/ICSD-compatible.
  - Placement: `BOARD_FACT`
  - Source: DSM-5-TR/ICSD-3; AASM
- `MODIFY` — DORAs such as daridorexant/ lemborexant avoid tolerance, dependence and muscle relaxation. → **Daridorexant is EU-authorised for adult insomnia of at least 3 months with daytime impact. DORAs have a different adverse-effect profile from benzodiazepines, but do not claim zero tolerance/dependence or no impairment. Lemborexant should not be presented as an EU option without current licensing verification.**
  - Placement: `FOLLOWUP`
  - Source: EMA Quviviq EPAR; NICE TA922
- `KEEP` — CBT-I is preferred first-line long-term treatment; sleep hygiene alone is insufficient. **Approved:** Retain, while recognising medication can be used when CBT-I is unavailable/unsuitable or according to individual circumstances.
  - Placement: `MODEL`
  - Source: AASM; NICE TA922

### Q066

- `MODIFY` — Narcolepsy type 1 is defined by the classic tetrad and CSF orexin <110 pg/mL/HLA-DQB1*06:02. → **EDS is required; cataplexy and/or hypocretin deficiency distinguish NT1 from NT2 under current sleep classification. The classic tetrad is not required in every patient. HLA-DQB1*06:02 is associated but insufficiently specific for diagnosis; exact CSF threshold is a specialist follow-up, not necessary board core.**
  - Placement: `BOARD_FACT`
  - Source: ICSD-3/AASM narcolepsy criteria
- `KEEP` — MSLT mean sleep latency ≤8 min with ≥2 SOREMPs following appropriate overnight PSG is a diagnostic anchor. **Approved:** Retain with caveats about adequate sleep, medication washout and circadian confounding.
  - Placement: `FOLLOWUP`
  - Source: ICSD-3/AASM
- `KEEP` — RBD = dream enactment + REM without atonia; injury prevention first; melatonin/clonazepam are conditional options. **Approved:** Retain; no neuroprotective therapy is established.
  - Placement: `BOARD_FACT`
  - Source: AASM RBD Guideline 2023

### Q067

- `MODIFY` — Normal adult sleep is N1 5%, N2 45–50%, N3 15–20%, REM 20–25%, 90–110-min cycles and 4–6 cycles. → **DROP_NUMBER_KEEP_QUALITATIVE for core: stage proportions and cycle length vary with age, night and scoring context. If used, present only as approximate classic sleep-physiology teaching, not diagnostic truth.**
  - Placement: `HISTORICAL`
  - Source: AASM sleep physiology/textbook sources
- `KEEP` — N1 theta; N2 spindles/K-complexes; N3 high-amplitude slow delta; REM low-voltage mixed-frequency EEG with atonia. **Approved:** Retain as classic board physiology.
  - Placement: `BOARD_FACT`
  - Source: AASM sleep staging; standard sleep medicine
- `MODIFY` — N3 is strictly 0.5–2 Hz >75 μV; depression REM latency <60–65 min is diagnostic. → **Frequency/amplitude conventions are classic scoring facts and may be retained only as technical follow-up. Shortened REM latency, increased REM density and reduced slow-wave sleep are classic group-level depression associations, not diagnostic tests; drop the fixed <60–65-min rule.**
  - Placement: `HISTORICAL`
  - Source: Sleep medicine/descriptive biological psychiatry

### Q068

- `KEEP` — ICD-11 PD: mild/moderate/severe + five trait domains + optional borderline pattern qualifier. **Approved:** Retain as major current update.
  - Placement: `BOARD_FACT`
  - Source: ICD-11 personality-disorder framework
- `MODIFY` — OCPD is ego-syntonic whereas OCD is ego-dystonic. → **Retain as a useful tendency, not the sole discriminator; OCPD/anankastic traits are pervasive perfectionism/control/rigidity, while OCD requires obsessions/compulsions.**
  - Placement: `FOLLOWUP`
  - Source: DSM-5-TR/ICD-11 descriptive framework
- `KEEP` — Avoidant PD is pervasive self/interpersonal style versus SAD centred on scrutiny/evaluation. **Approved:** Retain; overlap is common.
  - Placement: `FOLLOWUP`
  - Source: DSM-5-TR

### Q069

- `KEEP` — Structured psychotherapy is primary BPD treatment; DBT/MBT and other specialist therapies are evidence-based; medication does not treat core BPD. **Approved:** Retain; avoid long-term polypharmacy.
  - Placement: `BOARD_FACT`
  - Source: NICE CG78/QS88
- `DROP` — ~85% remit by 10 years and lifetime suicide 5–10%. — **These are cohort-dependent and not needed as current board anchors; retain that symptomatic remission is common over time while functional recovery may lag and suicide risk is clinically important.**
  - Placement: `FOLLOWUP`
  - Source: Longitudinal BPD cohorts
- `MODIFY` — BPD mood shifts are hours/interpersonal; bipolar episodes are days-weeks/autonomous. → **Retain as a pattern discriminator but do not diagnose solely by duration: examine episodicity, biological activation, baseline change, interpersonal reactivity and longitudinal personality pattern.**
  - Placement: `TRAP`
  - Source: Current BPD/bipolar differential reviews

### Q070

- `MODIFY` — PCL-R ≥30 defines psychopathy and 20–30% of ASPD prisoners are psychopathic. → **PCL-R is a specialist forensic measure; cut-offs vary by jurisdiction/research context and psychopathy is not an independent DSM/ICD diagnosis. Drop the prevalence figure/cutoff from general board core.**
  - Placement: `FOLLOWUP`
  - Source: Hare PCL-R literature; DSM/ICD
- `DROP` — PCL-R is the strongest known predictor of violent recidivism. — **Avoid the superlative. Structured risk assessment combines multiple static/dynamic factors and tools; PCL-R is not a stand-alone universal recidivism test.**
  - Placement: `TRAP`
  - Source: Forensic risk-assessment literature
- `KEEP` — Psychopathy includes interpersonal/affective callous-manipulative traits beyond antisocial behaviour. **Approved:** Retain conceptually.
  - Placement: `BOARD_FACT`
  - Source: Forensic psychiatry literature

### Q071

- `MODIFY` — SSRIs cause sexual dysfunction specifically through 5-HT2A; switch to bupropion/mirtazapine or add PDE5 inhibitor. → **SSRI sexual dysfunction is multifactorial and drug-specific; review cause/dose, alternatives and patient priorities. PDE5 inhibitors are established for erectile dysfunction when appropriate. Bupropion is not a routine EU antidepressant option in all jurisdictions.**
  - Placement: `BOARD_FACT`
  - Source: Current antidepressant SmPCs; EMA sildenafil
- `KEEP` — Prolactin-raising antipsychotics can cause hypogonadism/sexual dysfunction. **Approved:** Retain.
  - Placement: `BOARD_FACT`
  - Source: Antipsychotic SmPCs
- `DROP` — IELT <1 minute and dapoxetine are essential general sexual-dysfunction board anchors. — **This is a specialist definition/treatment detail for lifelong premature ejaculation and is not necessary for the broad sexual-dysfunction question.**
  - Placement: `FOLLOWUP`
  - Source: Sexual medicine guidelines

### Q072

- `MODIFY` — Paraphilic disorder = atypical interest plus distress/impairment OR harm/nonconsent. → **Use current ICD-11 nuance: consensual atypical interests are not disorders; disorder may involve non-consenting persons, marked distress not solely due to rejection, or significant risk of injury/death depending category.**
  - Placement: `BOARD_FACT`
  - Source: ICD-11 paraphilic-disorder framework
- `MODIFY` — GnRH agonists eliminate deviant sexual arousal by reducing testosterone to castrate levels. → **GnRH analogues markedly suppress gonadal testosterone and sexual drive and may be used in selected high-risk cases under specialist monitoring; ‘eliminate’ is too absolute and treatment is risk/consent/legal-context dependent.**
  - Placement: `FOLLOWUP`
  - Source: WFSBP paraphilic-disorder guideline
- `KEEP` — SSRIs and antiandrogen/GnRH strategies are selected specialist options alongside psychotherapy/risk management. **Approved:** Retain at high level.
  - Placement: `MODEL`
  - Source: WFSBP; forensic sexology guidance

### Q073

- `KEEP` — ICD-11 moved gender incongruence out of mental disorders into conditions related to sexual health. **Approved:** Retain; gender diversity itself is not psychopathology.
  - Placement: `BOARD_FACT`
  - Source: WHO ICD-11
- `MODIFY` — WPATH requires multidisciplinary assessment, fertility counselling, social transition and medical interventions. → **Use an affirming, non-pathologising, individualised assessment of goals, comorbidity, capacity and support. Fertility counselling is relevant before treatments that may impair fertility, but not every adult requires the same multidisciplinary pathway or interventions.**
  - Placement: `MODEL`
  - Source: WPATH SOC8; WHO ICD-11
- `UNRESOLVED` — Greek adult gender-service/legal pathway as a national board fact. — **Do not invent a uniform Greek referral or reimbursement pathway without dedicated current official verification.**
  - Placement: `FOLLOWUP`
  - Source: No clean national pathway verified

### Q074

- `MODIFY` — Steady state is exactly 4–5 half-lives/97%. → **Teach steady state after several elimination half-lives, commonly around 4–5 as a pharmacokinetic rule of thumb; active metabolites/non-linear kinetics can alter this.**
  - Placement: `BOARD_FACT`
  - Source: Clinical pharmacology
- `DROP` — Phase I is impaired by ageing/liver disease while Phase II is preserved. — **This is an oversimplification. Hepatic impairment and age effects are drug- and pathway-specific; use product-specific dosing and organ-function principles.**
  - Placement: `TRAP`
  - Source: Clinical pharmacology/SmPCs
- `KEEP` — Partial agonist/inverse agonist/PAM definitions. **Approved:** Retain stable pharmacodynamic definitions at concise level.
  - Placement: `FOLLOWUP`
  - Source: Clinical pharmacology
- `KEEP` — Routine pharmacogenomic panels are not required for psychotropic selection. **Approved:** Retain; gene–drug guidance is selected, not universal.
  - Placement: `TRAP`
  - Source: Major guideline/regulatory positions; CPIC drug-specific guidance

### Q075

- `DROP` — Fluvoxamine increases clozapine/olanzapine 5–10× and fluoxetine/paroxetine double TCA/risperidone. — **Keep the CYP1A2/CYP2D6 inhibition principle but drop fixed fold-changes; magnitude depends on substrate, dose, genotype, smoking and co-medication.**
  - Placement: `FOLLOWUP`
  - Source: Current SmPCs/interactions
- `KEEP` — Irreversible MAOI + serotonergic antidepressant interaction can cause severe serotonin toxicity. **Approved:** Retain.
  - Placement: `BOARD_FACT`
  - Source: Current MAOI/SSRI SmPCs
- `MODIFY` — All irreversible MAOI switches require 14 days, except 5 weeks after fluoxetine. → **Direction matters: current fluoxetine SmPC requires at least 5 weeks after fluoxetine before an irreversible MAOI, and at least 2 weeks after an irreversible MAOI before fluoxetine. Other antidepressant/MAOI intervals are product-specific.**
  - Placement: `BOARD_FACT`
  - Source: Current fluoxetine/MAOI SmPCs
- `KEEP` — Benzodiazepine+opioid/alcohol respiratory depression; lithium+NSAID/ACEi/ARB/diuretic; valproate-lamotrigine; additive QT; SSRI/SNRI bleeding interactions. **Approved:** Retain at principle level; no automatic PPI rule.
  - Placement: `BOARD_FACT`
  - Source: SmPCs; NICE; prescribing guidance

### Q076

- `MODIFY` — SGAs work through D2+5-HT2A antagonism and therefore universally have lower EPS. → **Mechanisms are heterogeneous: many SGAs antagonise D2/5-HT2A, while partial agonists differ. Lower EPS liability is drug- and dose-specific, not a class guarantee.**
  - Placement: `BOARD_FACT`
  - Source: Antipsychotic pharmacology/SmPCs
- `KEEP` — Clozapine/olanzapine high metabolic; risperidone/paliperidone/amisulpride prolactin; potent D2 blockade EPS. **Approved:** Retain as robust relative tendencies, not a rigid ranking table.
  - Placement: `BOARD_FACT`
  - Source: NICE CG178; SmPCs
- `DROP` — Cariprazine/aripiprazole D3 affinity improves negative symptoms and cognition as a mechanism fact. — **Partial D2/D3 agonist pharmacology is real, but a direct receptor-to-cognitive-benefit claim is overconfident.**
  - Placement: `FOLLOWUP`
  - Source: SmPCs; antipsychotic trials
- `KEEP` — LAIs are appropriate by preference or when avoiding covert/non-adherence is a priority. **Approved:** Retain.
  - Placement: `BOARD_FACT`
  - Source: NICE CG178

### Q077

- `KEEP` — Akathisia = subjective inner restlessness + observable motor restlessness; dose reduction/switch and propranolol are key. **Approved:** Retain.
  - Placement: `BOARD_FACT`
  - Source: Current EPS consensus/reviews
- `MODIFY` — Anticholinergics are always ineffective in akathisia and always contraindicated in TD. → **Anticholinergics are not reliable routine treatment for pure akathisia and may worsen TD; they may be useful when concomitant drug-induced parkinsonism exists. Avoid absolute wording.**
  - Placement: `TRAP`
  - Source: EPS guidance
- `MODIFY` — Valbenazine is the routine European VMAT2 inhibitor. → **EU-wide marketing authorisation for deutetrabenazine (Austedo) for moderate-to-severe adult TD was granted in January 2026. Greek routine availability/reimbursement remains unverified. Do not imply US valbenazine availability in Greece.**
  - Placement: `FOLLOWUP`
  - Source: EMA Austedo EPAR 2026
- `UNRESOLVED` — Routine Greek access to deutetrabenazine for TD. — **EMA authorisation does not prove Greek market/reimbursement availability.**
  - Placement: `FOLLOWUP`
  - Source: Greek access not verified

### Q078

- `MODIFY` — Metabolic monitoring: weight baseline/6wk/12wk/annual; BP/glucose/lipids baseline/12wk/1y/annual. → **Use current NICE schizophrenia schedule: baseline weight/waist/pulse/BP/glucose-or-HbA1c/lipids/prolactin; weight weekly for 6 weeks, then 12 weeks, 1 year, annually; waist annually; pulse/BP/glucose/lipids at 12 weeks, 1 year, annually.**
  - Placement: `BOARD_FACT`
  - Source: NICE CG178
- `KEEP` — Baseline ECG is indication/risk/SmPC/inpatient dependent, not required for every outpatient. **Approved:** Retain.
  - Placement: `TRAP`
  - Source: NICE CG178/CG185
- `MODIFY` — Normal QTc sex thresholds, 440–500 borderline, >500 or Δ>60 mandates medication change. → **QTc >500 ms is a robust high-risk threshold prompting urgent review of drugs/electrolytes/cardiac risk and usually change of the offending agent. Sex-specific ‘normal’ values and Δ60 ms are useful cardiology heuristics but need not be universal psychiatry-board thresholds.**
  - Placement: `BOARD_FACT`
  - Source: Cardiac safety guidance; SmPCs
- `MODIFY` — Troponin/CRP clozapine myocarditis monitoring is mandatory everywhere. → **Widely used specialist protocols support early troponin/CRP surveillance, but exact schedules are local/specialist rather than universal legal requirements.**
  - Placement: `FOLLOWUP`
  - Source: Clozapine myocarditis protocols

### Q079

- `KEEP` — Core antidepressant mechanisms: SSRI=SERT; SNRI=SERT/NET; mirtazapine alpha2 antagonism with 5-HT2/3 and H1 antagonism; trazodone 5-HT2A antagonism/SERT inhibition. **Approved:** Retain selectively where it helps distinguish effects; do not require a mechanism for every named drug.
  - Placement: `BOARD_FACT`
  - Source: Current SmPCs/pharmacology
- `DROP` — Venlafaxine is purely serotonergic <150 mg and recruits NET ≥150–225 mg as an exact threshold. — **Noradrenergic contribution increases with dose, but there is no clinically sharp transporter threshold suitable as a board rule.**
  - Placement: `FOLLOWUP`
  - Source: Venlafaxine pharmacology
- `MODIFY` — Bupropion is a standard antidepressant selection option in European practice. → **Bupropion is widely used as an antidepressant in some jurisdictions, but current UK/EU product licensing is not uniform (e.g. UK Zyban is smoking-cessation). Do not make it a routine European first-line option without jurisdiction context.**
  - Placement: `FOLLOWUP`
  - Source: Current national SmPC/licensing
- `KEEP` — Antidepressant selection should be individualised by prior response, comorbidity, sleep/appetite, pain, sexual effects, cardiac/overdose risk, interactions and preference. **Approved:** Retain.
  - Placement: `MODEL`
  - Source: NICE NG222

### Q080

- `MODIFY` — All patients starting SSRI/SNRI need baseline/early sodium monitoring. → **Hyponatraemia/SIADH risk is increased particularly in older adults, low body weight, diuretic use and other risk states. Measure sodium when clinically indicated/risk-based; do not mandate universal testing.**
  - Placement: `FOLLOWUP`
  - Source: SmPCs/medicines-safety guidance
- `KEEP` — Paroxetine/venlafaxine have greater withdrawal liability; fluoxetine lower due long half-life. **Approved:** Retain qualitatively; taper individually.
  - Placement: `BOARD_FACT`
  - Source: NICE NG222
- `KEEP` — Fluoxetine → irreversible MAOI requires at least 5 weeks. **Approved:** Retain exact safety interval.
  - Placement: `BOARD_FACT`
  - Source: Current fluoxetine SmPC
- `DROP` — SSRI+NSAID/anticoagulant raises GI bleed 3–6× and therefore co-prescribe PPI. — **Retain increased bleeding risk and individual GI-risk assessment; drop the fixed multiplier and automatic gastroprotection.**
  - Placement: `TRAP`
  - Source: SmPCs; gastroprotection guidance

### Q081

- `KEEP` — Lithium maintenance 0.6–0.8 mmol/L; consider 0.8–1.0 in selected relapse/persistent-symptom cases; 12-h level. **Approved:** Retain as NICE board anchors.
  - Placement: `BOARD_FACT`
  - Source: NICE CG185/QS95
- `MODIFY` — Acute mania target 0.8–1.0 mmol/L is universal. → **Acute target ranges are product/formulary-specific and should be titrated to current guidance, response and toxicity risk; do not teach one universal acute range.**
  - Placement: `FOLLOWUP`
  - Source: Lithium SmPC/specialist guidance
- `KEEP` — Lithium level q3 months first year; then q6 months or q3 months in higher-risk groups; renal/thyroid/calcium at least q6 months. **Approved:** Retain as NICE monitoring schedule.
  - Placement: `BOARD_FACT`
  - Source: NICE CG185; NICE NG222
- `DROP` — Lithium toxicity = >1.2 mild, >2 severe; dialyse >4 or >2.5 with renal failure/neurotoxicity. — **Do not map clinical toxicity to one serum ladder; toxicity can occur at therapeutic levels. For dialysis, use EXTRIP integrated criteria (level, renal function, symptoms, expected clearance) rather than a single cut-off.**
  - Placement: `TRAP`
  - Source: EXTRIP lithium recommendations
- `KEEP` — EXTRIP: ECTR recommended with impaired kidney function and Li >4.0 mEq/L or decreased consciousness/seizures/life-threatening dysrhythmias regardless of level; suggested if >5.0, significant confusion, or expected >36 h to <1.0. **Approved:** Retain as specialist/toxicology FOLLOWUP, explicitly as EXTRIP criteria rather than a bedside single-number rule.
  - Placement: `FOLLOWUP`
  - Source: EXTRIP
- `KEEP` — Gastroenteritis/dehydration + NSAID: temporarily withhold lithium and urgently assess hydration, renal function/electrolytes and level when toxicity suspected. **Approved:** Retain; emergency referral depends on neurological symptoms, significant dehydration/renal impairment, arrhythmia/seizure or clinical toxicity.
  - Placement: `MODEL`
  - Source: NICE/SPS lithium monitoring

### Q082

- `KEEP` — Valproate baseline/ongoing monitoring includes weight/BMI, FBC and LFTs; repeat at 6 months then annually when stable. **Approved:** Retain as NICE-specific operational monitoring.
  - Placement: `BOARD_FACT`
  - Source: NICE CG185
- `KEEP` — Valproate reproductive restrictions for pregnancy/women and new male precautions. **Approved:** Retain exact regulatory structure; do not simplify to ‘banned in all women’.
  - Placement: `BOARD_FACT`
  - Source: EMA valproate referral; EMA 2024/2026 male precaution wording
- `MODIFY` — Valproate mechanism includes GABA-T inhibition, sodium/T-type calcium block and HDAC inhibition as established antimanic mechanism. → **Valproate has multiple molecular effects, including increased GABAergic signalling and ion-channel effects; HDAC inhibition is mechanistic research, not necessary clinical board truth.**
  - Placement: `FOLLOWUP`
  - Source: Valproate pharmacology/SmPC
- `KEEP` — Hyperammonaemic encephalopathy can occur with normal transaminases. **Approved:** Retain; check ammonia in compatible unexplained encephalopathy and stop/treat valproate appropriately with specialist/toxicology input.
  - Placement: `FOLLOWUP`
  - Source: Valproate SmPC/toxicology

### Q083

- `KEEP` — Lamotrigine is primarily a bipolar-depression maintenance/prevention agent and lacks meaningful acute antimanic efficacy. **Approved:** Retain.
  - Placement: `BOARD_FACT`
  - Source: NICE CG185; lamotrigine SmPC
- `MODIFY` — Valproate doubles lamotrigine level so simply halve starting dose; carbamazepine halves it. → **Valproate inhibits lamotrigine glucuronidation and inducers increase clearance. Follow the exact SmPC titration schedule rather than applying a universal percentage dose rule.**
  - Placement: `BOARD_FACT`
  - Source: Current lamotrigine SmPC
- `MODIFY` — After >3–5 days interruption, restart from 25 mg and full retitration. → **Current SmPC principle: if the interval since stopping exceeds approximately five lamotrigine half-lives, restart according to the initial escalation schedule. The calendar time depends on interacting drugs; do not freeze 3–5 days.**
  - Placement: `BOARD_FACT`
  - Source: Current lamotrigine SmPC
- `KEEP` — Combined estrogen-containing contraception can approximately double lamotrigine clearance; pregnancy can lower concentrations and postpartum levels rebound. **Approved:** Retain as interaction/PK follow-up; dose/level management is individualized.
  - Placement: `FOLLOWUP`
  - Source: Lamotrigine SmPC

### Q084

- `MODIFY` — Benzodiazepines have a universal maximum prescribing duration of 2–4 weeks. → **2–4 weeks is a useful short-term prescribing/licensing heuristic for many anxiety/insomnia indications, not a statutory universal maximum. Longer use requires explicit indication, review and dependence planning.**
  - Placement: `BOARD_FACT`
  - Source: NICE/SmPC prescribing guidance
- `KEEP` — Dependence/tolerance, withdrawal seizures/delirium, falls/cognitive effects and opioid/alcohol respiratory depression are key risks. **Approved:** Retain.
  - Placement: `BOARD_FACT`
  - Source: Regulatory warnings; ASAM 2025
- `MODIFY` — Z-drugs are alpha1-selective and therefore avoid benzodiazepine dependence problems. → **Z-drugs also act at benzodiazepine-sensitive GABA-A receptors and still carry tolerance, dependence, impairment and complex-sleep-behaviour risks; do not imply safety exemption.**
  - Placement: `FOLLOWUP`
  - Source: Z-drug SmPCs/regulatory warnings

### Q085

- `KEEP` — Adult NICE sequence: lisdexamfetamine or methylphenidate first-line; atomoxetine after intolerance/nonresponse to both. **Approved:** Retain as NICE-specific board fact.
  - Placement: `BOARD_FACT`
  - Source: NICE NG87
- `KEEP` — Baseline weight, pulse/BP and cardiovascular/substance-diversion history; ECG only when indicated; pulse/BP before/after dose changes and every 6 months. **Approved:** Retain NICE schedule.
  - Placement: `BOARD_FACT`
  - Source: NICE NG87
- `MODIFY` — Active or previous psychosis/SUD is an absolute stimulant contraindication. → **During an acute psychotic/manic episode, stop ADHD medication and reconsider after resolution. A history of psychosis or SUD requires specialist risk assessment, long-acting formulations/diversion controls and monitoring, not automatic permanent stimulant exclusion.**
  - Placement: `TRAP`
  - Source: NICE NG87
- `KEEP` — Methylphenidate blocks DAT/NET; lisdexamfetamine is a dexamfetamine prodrug; atomoxetine inhibits NET. **Approved:** Retain one-line mechanisms.
  - Placement: `BOARD_FACT`
  - Source: Current SmPCs
- `DROP` — Atomoxetine has zero abuse liability and lisdexamfetamine’s RBC cleavage prevents intranasal/parenteral abuse. — **Both formulations have lower/divergent misuse characteristics than immediate-release amphetamine, but ‘zero’ or ‘prevents’ are overstatements.**
  - Placement: `FOLLOWUP`
  - Source: SmPCs/pharmacology

### Q086

- `MODIFY` — Lithium causes Ebstein anomaly at 1–2/1000; SSRIs PPHN ~3/1000 and neonatal adaptation 20–30%; valproate exact percentages should all be memorised. → **Use principle-level counselling. Lithium is associated with a small increased cardiac-malformation risk, much smaller than historic teaching implied. SSRIs may carry a small absolute PPHN risk and transient neonatal adaptation effects. Keep valproate’s regulatory risk figures only because they underpin EU restrictions; drop the other exact perinatal percentages from core.**
  - Placement: `BOARD_FACT`
  - Source: NICE CG192; current perinatal reviews; EMA valproate
- `MODIFY` — Pregnancy GFR rises 30–50%, therefore automatically increase lithium/lamotrigine and reduce during labour. → **Pregnancy changes lithium and lamotrigine pharmacokinetics, often lowering concentrations; monitor clinically/with TDM when indicated. Dose adjustment around delivery is individualized and guideline-specific, not automatic.**
  - Placement: `FOLLOWUP`
  - Source: Perinatal prescribing guidance; SmPCs
- `MODIFY` — Sertraline/paroxetine RID <5% are universally preferred; lithium RID >20% means breastfeeding is contraindicated. → **Breastfeeding decisions are drug-, infant- and monitoring-specific. Sertraline is commonly preferred because infant exposure is low. Lithium can enter breast milk substantially and requires specialist risk assessment/infant monitoring if considered; do not use one RID cut-off as an absolute rule.**
  - Placement: `FOLLOWUP`
  - Source: LactMed/perinatal guidelines; SmPCs

### Q087

- `MODIFY` — Clonus is the single most sensitive and specific sign of serotonin syndrome. → **Clonus and hyperreflexia are especially discriminating neuromuscular signs and central to Hunter-type criteria, but avoid a universal ‘single most sensitive/specific’ claim.**
  - Placement: `BOARD_FACT`
  - Source: Serotonin-toxicity diagnostic literature
- `MODIFY` — SS begins <24 h while NMS evolves over days/weeks; pupils/GI pattern is decisive. → **Serotonin toxicity usually develops rapidly after serotonergic exposure/change, often within hours; NMS usually develops over 1–3 days after dopamine blockade/withdrawal of dopaminergic drugs. Neuromuscular pattern is more useful than rigid timing or pupil/GI rules.**
  - Placement: `BOARD_FACT`
  - Source: Current NMS/serotonin syndrome reviews
- `MODIFY` — Cyproheptadine is the antidote for SS; bromocriptine+dantrolene are antidotes for NMS. → **Immediate drug cessation and supportive critical care are foundational. Cyproheptadine is an adjunct in selected serotonin toxicity with limited high-quality evidence. Bromocriptine/amantadine/dantrolene and ECT are severity-dependent NMS options, not mandatory antidotes.**
  - Placement: `TRAP`
  - Source: BAP NMS guidance; serotonin-toxicity reviews

### Q088

- `KEEP` — TCA QRS widening reflects fast sodium-channel blockade and QRS >100 ms is a useful major-toxicity/seizure-risk anchor. **Approved:** Retain as a practical toxicology board threshold, recognising some poison centres use 110–120 ms for bicarbonate treatment protocols.
  - Placement: `BOARD_FACT`
  - Source: Evidence-based poison-centre guideline; current poison-centre protocols
- `MODIFY` — QRS >160 ms and terminal R in aVR >3 mm are mandatory intervention thresholds. → **These are classic prognostic ECG markers, useful as examiner follow-up. Sodium bicarbonate treatment is driven by QRS widening/significant sodium-channel cardiotoxicity, hypotension, ventricular dysrhythmia and often seizures—not by one secondary ECG sign.**
  - Placement: `FOLLOWUP`
  - Source: TCA toxicology guidance
- `KEEP` — IV sodium bicarbonate is first-line for significant TCA sodium-channel cardiotoxicity; titrate to QRS narrowing/clinical stability and mild alkalinaemia. **Approved:** Retain; pH around 7.50–7.55 is a common poison-centre target, but exact bolus/infusion protocols are local and toxicity consultation is appropriate.
  - Placement: `BOARD_FACT`
  - Source: Current poison-centre guidance
- `KEEP` — Avoid class Ia/Ic sodium-channel blocking antiarrhythmics and avoid physostigmine in cardiotoxic TCA overdose. **Approved:** Retain as toxicology safety principle.
  - Placement: `TRAP`
  - Source: TCA toxicology guidance

### Q089

- `MODIFY` — An adequate ECT seizure must last ≥25–30 s. → **Do not teach a minimum seizure-duration number as the criterion of adequate ECT; seizure quality, EEG morphology and clinical response are more important and technique-specific.**
  - Placement: `TRAP`
  - Source: Modern ECT guidelines
- `MODIFY` — Right unilateral ultrabrief always minimises memory; bilateral always faster/more effective. → **Right unilateral high-dose/ultrabrief strategies generally reduce cognitive burden; bilateral/bitemporal often has faster or higher acute efficacy at a cost of greater cognitive effects. Technique is individualised.**
  - Placement: `BOARD_FACT`
  - Source: Modern ECT guidelines
- `MODIFY` — Benzodiazepines/anticonvulsants must be held and lithium must be held around ECT. → **Review medicines that raise seizure threshold or increase delirium risk. Dose reduction/withholding is individualised with anaesthesia/ECT team; these are not universal ‘must hold’ rules.**
  - Placement: `FOLLOWUP`
  - Source: Modern ECT medication guidance
- `UNRESOLVED` — Greek ECT-specific authorisation procedure for incapacitous/emergency non-consensual ECT. — **Capacitous adults ordinarily require informed consent and involuntary admission does not itself authorise ECT. The exact ECT-specific Greek court/prosecutor/guardian procedure was not cleanly verified and must remain unresolved rather than importing UK law.**
  - Placement: `TRAP`
  - Source: Law 3418/2005 general consent law; Q074–Q089 current packet
- `KEEP` — rTMS is an established depression treatment without general anaesthesia; seizure risk is low; ECT remains preferred when rapid high-probability response is needed in severe psychotic/catatonic illness. **Approved:** Retain at high level.
  - Placement: `FOLLOWUP`
  - Source: NICE HTG396; ECT guidelines

### Q090

- `KEEP` — CBT remains structured, collaborative, formulation-based and goal-oriented with BA, exposure, cognitive restructuring and behavioural experiments. **Approved:** No consequential correction required; retain.
  - Placement: `BOARD_FACT`
  - Source: NICE disorder-specific CBT guidance
- `MODIFY` — Every CBT answer should add third-wave therapies/ACT for modernity. → **Do not add ACT merely for novelty. MBCT is worth mentioning where guideline-supported (notably depression relapse prevention); supported digital CBT is a delivery mode in selected indications.**
  - Placement: `FOLLOWUP`
  - Source: NICE NG222

### Q091

- `MODIFY` — Projective identification means the patient projects affect into the clinician and thereby induces congruent staff emotion as objective evidence. → **Retain projective identification as a psychodynamic formulation concept; clinician reactions are hypotheses to reflect on and check against context/supervision, not objective truth about the patient.**
  - Placement: `BOARD_FACT`
  - Source: Contemporary psychodynamic practice
- `KEEP` — Team splitting is managed by shared formulation, communication, supervision and consistent boundaries. **Approved:** Retain.
  - Placement: `MODEL`
  - Source: Contemporary personality-disorder/team practice
- `KEEP` — Supportive therapy prioritises stabilisation/coping/function; exploratory work needs sufficient stability/reflective capacity/alliance. **Approved:** Retain.
  - Placement: `FOLLOWUP`
  - Source: Psychotherapy practice

### Q092

- `KEEP` — IPT uses grief, role disputes, role transitions and interpersonal difficulties as core problem areas. **Approved:** Retain.
  - Placement: `BOARD_FACT`
  - Source: IPT manuals; NICE depression guidance
- `MODIFY` — IPT is always 12–16 sessions in three fixed phases and assigns a ‘sick role’. → **12–16 sessions and three phases describe the classic manual, but adaptations vary. Keep as typical historical/manual structure rather than a universal treatment duration.**
  - Placement: `FOLLOWUP`
  - Source: IPT manuals/guidance

### Q093

- `DROP` — Bipolar group psychoeducation reduces relapse 30–40% over 5 years and schizophrenia family psychoeducation reduces relapse up to 50%. — **Effect sizes vary by trial/population; retain that structured psychoeducation/family intervention can reduce relapse and improve coping/adherence without fixed percentages.**
  - Placement: `FOLLOWUP`
  - Source: NICE CG185; NICE CG178; psychotherapy trials
- `KEEP` — Family intervention should be offered in schizophrenia/bipolar contexts when relevant, not described as mandatory. **Approved:** Retain.
  - Placement: `TRAP`
  - Source: NICE CG178/CG185
- `KEEP` — Psychoeducation includes illness understanding, shared decisions, relapse signatures and relapse-prevention planning. **Approved:** Retain.
  - Placement: `MODEL`
  - Source: NICE guidance

### Q094

- `KEEP` — DLPFC-executive, orbitofrontal-disinhibition/social judgement, ACC-motivation/apathy, amygdala-salience/fear, hippocampus-memory/context. **Approved:** Retain as high-yield associations, not deterministic one-region rules.
  - Placement: `BOARD_FACT`
  - Source: Stable neuropsychiatry
- `MODIFY` — Papez circuit is specifically the episodic-memory consolidation loop that should be mandatory board content. → **The circuit is historically/anatomically useful, but modern memory biology is broader; retain only as optional neuroanatomy follow-up if exam relevance warrants.**
  - Placement: `HISTORICAL`
  - Source: Neuroanatomy history/current systems neuroscience

### Q095

- `KEEP` — Four classic dopamine pathways and clinical correlates. **Approved:** Retain; add caveat that schizophrenia is not ‘too much dopamine everywhere’.
  - Placement: `BOARD_FACT`
  - Source: Stable psychopharmacology
- `MODIFY` — 65–70% D2 occupancy is efficacy and >80% is EPS/prolactin. → **Retain only as the classic PET heuristic, with drug/individual/partial-agonist caveats; not a treatment target measured in routine care.**
  - Placement: `FOLLOWUP`
  - Source: PET occupancy literature

### Q096

- `DROP` — Exact schizophrenia familial-risk table and heritability hierarchy (bipolar 70–85, schizophrenia 70–80, autism 80–90, ADHD 75–80, depression 35–40). — **These are population/study-dependent and invite false individual prediction. Retain high familial/polygenic loading, common small-effect variants, rare larger-effect variants and cross-disorder pleiotropy.**
  - Placement: `BOARD_FACT`
  - Source: ISPG genetic-testing statement; psychiatric genomics
- `DROP` — PRS explains 7–10% variance in schizophrenia and has low PPV. — **Drop the changing variance number. Retain that current psychiatric PRS are research tools and are not routine stand-alone diagnostic/prognostic tests.**
  - Placement: `TRAP`
  - Source: ISPG statements

### Q097

- `KEEP` — ARR, NNT/NNH and likelihood-ratio formulas. **Approved:** Retain as stable EBM calculations, with confidence intervals and absolute effects emphasised.
  - Placement: `BOARD_FACT`
  - Source: Evidence-based medicine standards
- `MODIFY` — Any test >90% sensitivity/specificity has PPV <10% in low-prevalence conditions. → **PPV depends mathematically on prevalence and test characteristics; use this as a conceptual example, not a fixed numeric rule.**
  - Placement: `FOLLOWUP`
  - Source: Diagnostic-test mathematics
- `KEEP` — Preregistration/protocol concordance is a modern appraisal point. **Approved:** Retain.
  - Placement: `BOARD_FACT`
  - Source: CONSORT/trial-reporting standards

### Q098

- `KEEP` — Greek confidentiality: Law 3418/2005 Art 13 + Penal Code Art 371; health-data processing under GDPR/Law 4624/2019. **Approved:** Retain.
  - Placement: `BOARD_FACT`
  - Source: Law 3418/2005 Art 13; Penal Code Art 371; Law 4624/2019
- `MODIFY` — Confidentiality can be broken under Penal Code Arts 25 and 32 to notify police and intended victim of imminent homicide. → **Article 13 itself allows disclosure for a legal duty, a justified substantial public/third-party interest that cannot otherwise be protected, and necessity/defence. Penal Code Art 25 is necessity that removes unlawfulness; Art 32 concerns necessity affecting imputability and should not be used as the primary confidentiality basis.**
  - Placement: `BOARD_FACT`
  - Source: Law 3418/2005 Art 13; Penal Code Art 25
- `KEEP` — Penal Code Art 232 creates a specific duty to report to authorities a reliably known planned/ongoing felony while prevention is still possible. **Approved:** Retain with statutory qualifications. This is not a general Tarasoff duty.
  - Placement: `FOLLOWUP`
  - Source: Penal Code Art 232
- `UNRESOLVED` — Greek law creates a categorical duty to warn the intended victim personally. — **No specific Tarasoff-style general Greek duty to warn was verified. Use proportionate disclosure to the appropriate protective recipient under the actual legal basis; direct victim warning depends on circumstances and legal advice.**
  - Placement: `TRAP`
  - Source: No specific Greek statute identified
- `KEEP` — Relatives have no automatic right to a competent living adult’s psychiatric information; confidentiality continues after death. **Approved:** Retain; note separate statutory record-access rights may exist for heirs after death.
  - Placement: `FOLLOWUP`
  - Source: Law 3418/2005 Arts 13–14
- `MODIFY` — Law 3500/2006 child-abuse reporting can be cited in its original form as a generic child-abuse duty. → **Use the current amended domestic-violence rule: Art 23 Law 3500/2006, amended by Law 5090/2024 and further Law 5172/2025, imposes immediate reporting duties on doctors/professionals for indications of domestic-violence offences against minors (and specified objective findings in adults). State the scope accurately; do not generalise it to every conceivable form of child maltreatment without checking the applicable reporting provision.**
  - Placement: `FOLLOWUP`
  - Source: Law 3500/2006 Art 23 as amended; Hellenic Police current guidance

### Q099

- `KEEP` — Penal Code Art 34: lack of cognitive OR volitional capacity due qualifying mental/intellectual disorder or disturbance of consciousness at offence time excludes imputability. **Approved:** Retain exact legal structure.
  - Placement: `BOARD_FACT`
  - Source: Greek Penal Code Art 34; official disability portal/current codification
- `KEEP` — Penal Code Art 36: substantially reduced, not absent, capacity leads to reduced punishment. **Approved:** Retain.
  - Placement: `BOARD_FACT`
  - Source: Greek Penal Code Art 36
- `MODIFY` — Art 34 automatically means acquittal plus Art 69 forensic hospitalisation. → **Diagnosis/Art 34 finding and subsequent safety measures are separate judicial decisions with their own statutory criteria. Do not imply automatic forensic hospitalisation.**
  - Placement: `TRAP`
  - Source: Greek Penal Code Arts 34,69; current forensic law
- `KEEP` — Diagnosis alone never determines criminal irresponsibility; assessment is retrospective and offence-specific. **Approved:** Retain; distinguish from current capacity, dangerousness/risk and fitness to participate.
  - Placement: `MODEL`
  - Source: Greek Penal Code Arts 34,36; forensic psychiatry

### Q100

- `MODIFY` — Greek community structures should be called KoKEPSY as the generic adult Community Mental Health Centre. → **Use current adult term Κέντρο Ψυχικής Υγείας (ΚΨΥ) for community mental-health centres; distinguish child/adolescent/community structures by their official names rather than using KoKEPSY generically.**
  - Placement: `BOARD_FACT`
  - Source: Ministry of Health/current service naming
- `KEEP` — Law 5129/2024 established the Εθνικό Δίκτυο Υπηρεσιών Ψυχικής Υγείας with seven Πε.Δ.Υ.Ψ.Υ. **Approved:** Retain; the network formally began operation in 2025 and integrates hospital/community/addiction service architecture.
  - Placement: `BOARD_FACT`
  - Source: Law 5129/2024; Ministry of Health 2024–25
- `KEEP` — Community care includes multidisciplinary continuity, crisis/home care, rehabilitation, supported housing/employment, family/physical-health/substance care, early intervention and recovery orientation. **Approved:** Retain as principles; do not bury answer in organisational bureaucracy.
  - Placement: `MODEL`
  - Source: WHO community mental-health principles; NICE psychosis guidance
- `KEEP` — IPS is evidence-based supported employment for severe mental illness. **Approved:** Retain only as an examiner follow-up, not mandatory core content.
  - Placement: `FOLLOWUP`
  - Source: NICE CG178; IPS evidence


## 4. Numerical claims master table

Only numbers that remain sufficiently stable, operational and sourceable are approved below. Their presence in this table does not mean they belong in the spoken model answer.

| Q | Claim | Approved number/range | Qualification | Source |
|---|---|---:|---|---|
| Q005 | NICE aftercare | Within 48 h | Only when ongoing safety concerns after self-harm | NICE NG225 1.10.2 |
| Q005 | Self-harm psychological intervention | Typically 4–10 sessions | Tailored CBT-informed/problem-solving intervention; not a mandatory fixed course | NICE NG225 1.11 |
| Q007 | Post-rapid-tranquillisation observations | At least hourly; every 15 min in specified high-risk states | NICE-specific monitoring; q15 min if sedated/asleep, intoxicated, pre-existing physical illness, harm from restrictive intervention, or BNF max exceeded | NICE NG10 1.4.45 |
| Q009 | Temporary examination detention | Maximum 48 h | Only when prior examination was impossible/refused; not max involuntary-admission duration | Law 2071/1992 Art 96 |
| Q009 | Prosecutor filing / court / summons | 3 days / 10 days / ≥48 h | Current procedural timetable; court designation updated by CPC | Law 2071/1992 Art 96 |
| Q009 | Involuntary admission duration/review | Ordinary max 6 months; report after first 3 months | Ends earlier when criteria cease; exceptional extension has separate conditions | Law 2071/1992 Art 99 |
| Q010 | Catatonia sign threshold | ≥3 signs | Current DSM-5-TR/ICD-11-compatible threshold | DSM-5-TR; ICD-11 |
| Q010 | BFCRS | 14 screening items / 23 total items | Rating instrument, not statutory diagnostic criterion | Bush–Francis; BAP 2023 |
| Q010 | Lorazepam challenge | 1–2 mg IV/IM or 2 mg PO | Reassess promptly; response supports but does not prove diagnosis | BAP 2023 |
| Q010 | Malignant catatonia lorazepam/ECT | 8 mg/day start, titrate to max 24 mg/day; ECT after 48–72 h if partial/no response | BAP malignant-catatonia recommendation only; not universal for non-malignant catatonia | BAP 2023 |
| Q010 | NMS antipsychotic restart | ≥2 weeks after resolution | BAP recommendation, not legal mandate | BAP 2023 |
| Q012 | Schizophrenia duration | DSM: active-phase ≈1 month and continuous disturbance ≥6 months; ICD-11: ≥1 month syndrome without DSM 6-month rule | System-specific; do not merge criteria | DSM-5-TR; ICD-11 |
| Q013 | Schizoaffective DSM psychosis–mood separation | ≥2 weeks psychosis without major mood episode | DSM-specific; ICD-11 architecture differs | DSM-5-TR |
| Q013 | DSM psychotic-disorder duration hierarchy | Brief <1 month; schizophreniform 1–6 months; schizophrenia ≥6 months continuous disturbance | DSM-specific | DSM-5-TR |
| Q016 | Adequate antipsychotic trial | Usually 4–6 weeks at effective therapeutic dose | Reassess adherence/diagnosis/tolerability; not automatic dose escalation | NICE CG178 |
| Q018 | TRRIP minimum adequate trials | ≥2 different antipsychotics; ≥6 weeks each at therapeutic dose | TRRIP consensus; ≥600 mg CPZ equivalent is fallback benchmark where product target unclear | TRRIP consensus |
| Q018 | TRRIP adherence | ≥80% prescribed doses over required trial period | Operational research/consensus criterion; real-world assessment triangulates adherence | TRRIP consensus |
| Q019 | Clozapine ANC initiation | ≥1500/mm³ general; ≥1000/mm³ confirmed BEN | Current EU update | EMA/PRAC 2025 |
| Q019 | Clozapine ANC frequency | Weekly first 18 wk; monthly next 34 wk; q12wk after year 1 if no neutropenia; annual after 2 years if none | Current EU 2025 update; mild neutropenia → monthly | EMA/PRAC 2025 |
| Q019 | Clozapine TDM adequacy | ≥350 ng/mL trough | Useful threshold for establishing adequate clozapine exposure/nonresponse; not a universal target for every patient | TRRIP/clozapine TDM |
| Q019 | Clozapine interruption |  >48 h | Requires low-dose restart/re-titration per current SmPC | Current clozapine SmPC |
| Q020 | DSM major depressive episode | ≥5/9 symptoms for ≥2 weeks, including ≥1 core symptom | DSM-specific; do not reproduce full proprietary criteria | DSM-5-TR |
| Q020 | PMDD confirmation | Prospective daily ratings across ≥2 symptomatic cycles | DSM-specific | DSM-5-TR |
| Q023 | DSM mania/hypomania | Mania ≥7 days or any duration if hospitalisation required; hypomania ≥4 days | DSM-specific; ICD wording differs | DSM-5-TR |
| Q023 | Rapid cycling | ≥4 mood episodes in 12 months | DSM specifier | DSM-5-TR |
| Q024 | Valproate male reproductive precaution | Contraception consideration and no sperm donation during treatment and for ≥3 months after stopping | Precautionary EU regulation based on potential paternal risk signal | EMA PRAC/CMDh 2024; product wording 2026 |
| Q024 | Valproate pregnancy counselling | Major malformation risk ≈10–11%; developmental problems reported up to ~30–40% | Retain only as official regulatory counselling anchors; not generic population facts | EMA valproate referral/product information |
| Q026 | Lithium maintenance | 0.6–0.8 mmol/L | Standard NICE maintenance target | NICE CG185/QS95 |
| Q026 | Lithium selected higher maintenance | 0.8–1.0 mmol/L | Consider for relapse on lithium or persistent subthreshold symptoms with impairment | NICE CG185 |
| Q026 | Lithium sampling | ~12 h post-dose | Standard trough timing | NICE CG185/NG222 |
| Q027 | Postpartum psychosis incidence | ≈1–2 per 1,000 births | Approximate epidemiological follow-up, not model-answer requirement | Major postpartum psychosis reviews |
| Q028 | DSM panic/agoraphobia timing | Panic: ≥1 month concern/behavioural change; agoraphobia: ≥6 months and ≥2 situation domains | DSM-specific | DSM-5-TR |
| Q029 | DSM GAD | ≥6 months; ≥3 associated symptoms in adults | DSM-specific; ICD-11 uses ‘several months’ | DSM-5-TR; ICD-11 |
| Q031 | OCD SSRI escalation | Consider dose increase after 4–6 weeks at standard dose if tolerated; allow a sufficiently long overall trial, often up to 12 weeks | Dose increases must follow SmPC; not routine supra-licensed dosing | NICE CG31 |
| Q033 | DSM acute stress disorder | 3 days–1 month | Persisting symptoms >1 month require PTSD reassessment; not automatic conversion | DSM-5-TR |
| Q033 | DSM adjustment disorder | Onset within 3 months; usually resolves within 6 months after stressor/consequences end | DSM-specific; ICD-11 timing differs | DSM-5-TR |
| Q037 | DSM SUD severity | 2–3 mild; 4–5 moderate; ≥6 severe | DSM-specific | DSM-5-TR |
| Q038 | Suspected Wernicke thiamine | IV 300–500 mg three times daily for 3–5 days | If symptoms persist, further IV 300–500 mg daily for 3–5 days/while improving; correct magnesium | UK alcohol treatment guideline 2025/26 |
| Q043 | Benzodiazepine taper starting pace | ~5–10% every 2–4 weeks; generally not >25% every 2 weeks | Individualise and slow/pause as needed | ASAM Joint Guideline 2025 |
| Q044 | DSM gambling disorder | ≥4 of 9 criteria over 12 months | DSM-specific | DSM-5-TR |
| Q045 | 4AT | Score ≥4 | Possible delirium/cognitive impairment; prompts clinical assessment, not diagnosis | 4AT; NICE CG103 |
| Q045 | Short-term haloperidol in delirium | Usually ≤1 week | Lowest clinically appropriate dose after de-escalation/non-drug measures fail; PD/DLB contraindications | NICE CG103; MHRA |
| Q048 | DLB/PDD convention | 1-year rule | Operational classification convention, not biological boundary | DLB Consortium 2017 |
| Q051 | Risperidone BPSD licensing | Up to 6 weeks | Persistent aggression in moderate-to-severe AD after non-drug failure when risk of harm | NICE NG97; European product information |
| Q051 | BPSD antipsychotic review | At least every 6 weeks | Stop if no ongoing benefit | NICE NG97 |
| Q059 | DSM adult ADHD | ≥5 symptoms in a domain; some symptoms before age 12 | Childhood diagnosis/documents not required; multiple-setting impairment needed | DSM-5-TR; NICE NG87 |
| Q063 | MEED red examples | BMI <13 kg/m²; waking pulse <40/min; temperature <35.5°C; glucose <3.0 mmol/L | Examples within multidomain risk assessment; not stand-alone admission rules | RCPsych MEED 2022 |
| Q064 | DSM bulimia frequency | ≥1/week for 3 months | DSM-specific | DSM-5-TR |
| Q064 | Fluoxetine for adult BN | 60 mg/day | Licensed adjunct to psychotherapy in current SmPC | Current fluoxetine SmPC |
| Q065 | Chronic insomnia | ≥3 nights/week for ≥3 months | DSM/ICSD/NICE-compatible; daytime impairment/adequate opportunity required | NICE TA922; DSM/ICSD |
| Q066 | Narcolepsy MSLT | Mean sleep latency ≤8 min + ≥2 SOREMPs | Requires valid overnight PSG/preparation and specialist interpretation | ICSD/AASM |
| Q075 | Fluoxetine → irreversible MAOI | ≥5 weeks | Exact product safety interval | Current fluoxetine SmPC |
| Q075 | Irreversible MAOI → fluoxetine | ≥2 weeks | Exact fluoxetine product safety interval | Current fluoxetine SmPC |
| Q078 | Antipsychotic weight monitoring | Weekly first 6 weeks, then 12 weeks, 1 year, annually | NICE schizophrenia schedule | NICE CG178 |
| Q078 | Antipsychotic BP/glucose/lipids | 12 weeks, 1 year, annually after baseline | NICE schizophrenia schedule | NICE CG178 |
| Q078 | QTc high-risk threshold | >500 ms | Urgent review of drug/electrolyte/cardiac risk; usually change offending agent where feasible | Cardiac safety guidance |
| Q080 | Fluoxetine → irreversible MAOI | ≥5 weeks | Same safety anchor as Q075 | Current fluoxetine SmPC |
| Q081 | Lithium monitoring | Level q3mo first year; q6mo thereafter or q3mo if higher risk; renal/thyroid/calcium at least q6mo | NICE schedule | NICE CG185/NG222 |
| Q081 | EXTRIP dialysis | Recommend if impaired kidney function + Li >4.0 mEq/L or severe neuro/cardiac features regardless of level; suggest >5.0, confusion, or expected >36 h to <1.0 | Specialist toxicology criteria; not a single-number rule | EXTRIP |
| Q082 | Valproate routine stable monitoring | FBC/LFT/weight at 6 months then annually | NICE-specific | NICE CG185 |
| Q083 | Lamotrigine restart | If interruption exceeds ~5 half-lives | Restart initial escalation; calendar days depend on interacting drugs | SmPC |
| Q083 | Ethinylestradiol/levonorgestrel effect on lamotrigine | ~2-fold increase in clearance | Follow levels/clinical response when starting/stopping | Current lamotrigine SmPC |
| Q085 | Adult ADHD stimulant trials before atomoxetine | Separate ~6-week adequate trials of lisdexamfetamine and methylphenidate | NICE-specific sequence | NICE NG87 |
| Q085 | ADHD BP/pulse follow-up | Before/after each dose change and every 6 months | NICE schedule | NICE NG87 |
| Q088 | TCA QRS risk anchor | >100 ms | Useful major-toxicity/seizure-risk marker; some poison protocols treat at 110–120 ms | Poison-centre/toxicology guidance |
| Q088 | TCA bicarbonate alkalinaemia target | ~pH 7.50–7.55 | Common poison-centre endpoint alongside QRS narrowing/clinical stability | Poison-centre guidance |

## 5. Drug-mechanism master table

| Q | Drug/class | Approved one-line mechanism | Qualification |
|---|---|---|---|
| Q029 | Pregabalin | Binds α2δ subunit of voltage-gated calcium channels, reducing excitatory transmitter release | Useful high-level mechanism; treatment positioning remains guideline-specific |
| Q029 | Buspirone | 5-HT1A partial agonist | Useful follow-up; not a universal first-line GAD drug |
| Q039 | Naltrexone | Opioid-receptor antagonist, mainly μ-receptor clinically | Blocks opioid effects; avoid initiation in current opioid dependence/use |
| Q039 | Disulfiram | Inhibits aldehyde dehydrogenase, causing acetaldehyde accumulation with alcohol | Aversive-treatment mechanism |
| Q039 | Acamprosate | Modulates glutamatergic/GABAergic signalling; precise mechanism not fully settled | Do not call it a single-receptor NMDA antagonist |
| Q040 | Buprenorphine | High-affinity partial μ-opioid agonist | Can precipitate withdrawal if given before sufficient withdrawal from full agonist |
| Q040 | Naloxone | Competitive opioid-receptor antagonist | Emergency reversal; product/route dosing varies |
| Q042 | Cocaine | Blocks monoamine reuptake transporters, especially DAT/NET/SERT | High-level stimulant mechanism |
| Q042 | Amphetamine/dexamfetamine | Promotes monoamine release/reverse transport and influences VMAT2 | High-level stimulant mechanism |
| Q047 | Donepezil/galantamine | Reversible acetylcholinesterase inhibition | Symptomatic AD therapy |
| Q047 | Rivastigmine | Acetylcholinesterase and butyrylcholinesterase inhibition | Symptomatic dementia therapy |
| Q047 | Memantine | Uncompetitive NMDA-receptor antagonist | Symptomatic dementia therapy |
| Q064 | Fluoxetine | SERT inhibition (SSRI) | Medication adjunct in adult bulimia nervosa |
| Q065 | Daridorexant | Dual orexin OX1/OX2 receptor antagonist | Promotes sleep by reducing wake drive |
| Q071 | PDE5 inhibitors | Inhibit phosphodiesterase-5, augmenting NO–cGMP signalling in erectile tissue | Use where erectile dysfunction is appropriate target |
| Q075 | Valproate–lamotrigine interaction | Valproate inhibits lamotrigine glucuronidation | Raises lamotrigine exposure/rash risk; follow SmPC titration |
| Q075 | Smoking–clozapine/olanzapine | Tobacco-smoke PAHs induce CYP1A2 | Nicotine/NRT do not reproduce induction |
| Q076 | Many SGAs | D2 and 5-HT2A antagonism is common but not universal | Class is mechanistically heterogeneous |
| Q076 | Aripiprazole-type agents | D2-family partial agonism rather than pure antagonism | Useful class distinction; do not infer guaranteed cognitive benefit |
| Q079 | SSRIs | Serotonin-transporter inhibition | Core class mechanism |
| Q079 | SNRIs | Serotonin- and noradrenaline-transporter inhibition | Degree of NET engagement varies by agent/dose |
| Q079 | Mirtazapine | Presynaptic α2 antagonism plus 5-HT2/5-HT3 and H1 antagonism | Explains sedative/appetite and lower serotonergic GI/sexual profile tendencies |
| Q079 | Trazodone | 5-HT2A antagonism with serotonin-reuptake inhibition; H1/α1 effects contribute at common doses | Avoid oversimplified one-target claims |
| Q083 | Lamotrigine | Use-dependent voltage-gated sodium-channel effects and reduced glutamate release are principal pharmacologic descriptions | Clinical role matters more than a single molecular mechanism |
| Q084 | Benzodiazepines | Positive allosteric modulators at GABA-A benzodiazepine sites, increasing GABA-mediated channel opening frequency | Dependence/respiratory-depression interactions are clinically more important |
| Q084 | Z-drugs | Positive allosteric modulation at benzodiazepine-sensitive GABA-A receptors with subtype preference | Do not claim dependence exemption |
| Q085 | Methylphenidate | DAT and NET reuptake inhibition | Adult ADHD |
| Q085 | Lisdexamfetamine | Prodrug converted to dexamfetamine; increases catecholamine release/reverse transport | Lower tampering attractiveness than immediate-release amphetamine does not mean zero abuse risk |
| Q085 | Atomoxetine | Selective noradrenaline-transporter inhibition | Non-stimulant ADHD option |
| Q087 | Cyproheptadine | 5-HT2A antagonism | Adjunct in selected serotonin toxicity; supportive care remains primary |
| Q087 | Bromocriptine | Dopamine agonism | Selected NMS option, not universal antidote |
| Q087 | Dantrolene | RYR1-mediated skeletal-muscle calcium-release inhibition | Selected severe NMS option |
| Q088 | Sodium bicarbonate in TCA toxicity | Raises extracellular sodium and alkalinises serum, reducing fast sodium-channel cardiotoxicity | Treats QRS widening/hypotension/dysrhythmia |

## 6. Emergency-dose master table

Only four exact/current dose anchors survive as broadly useful. Rapid-tranquillisation milligram doses are **not** listed as NICE doses because NG10 names regimens but not the exact mg doses; a current BNF/SmPC/local formulary is required for those.

| Q | Emergency | Approved dose/route | Timing/repeat/escalation | Caveat/source |
|---|---|---|---|---|
| Q010 | Lorazepam challenge | 1–2 mg IV/IM or 2 mg PO | Reassess promptly (route-dependent, minutes); response supports diagnosis | BAP Catatonia Guideline 2023 |
| Q010 | Malignant catatonia lorazepam | Start 8 mg/day PO/IM/IV, titrate by response/tolerability to max 24 mg/day | If partial/no response within 48–72 h, BAP recommends bilateral ECT | BAP 2023 |
| Q038 | Suspected Wernicke encephalopathy thiamine | IV 300–500 mg three times daily | 3–5 days; if symptoms persist, 300–500 mg IV daily for further 3–5 days/while improving; correct Mg | UK alcohol-treatment guideline 2025/26 |
| Q088 | TCA sodium bicarbonate | Common current poison-centre protocol: ~1 mmol/kg IV bolus, repeat every few minutes according to response | Titrate to QRS narrowing/haemodynamic stability and mild alkalinaemia; protocols vary; obtain toxicology advice | Current poison-centre guidance |

## 7. Monitoring/threshold master table

| Q | Item | Approved threshold/interval | Meaning/action | Source |
|---|---|---|---|---|
| Q007 | Rapid tranquillisation observations | At least hourly; q15 min in NICE high-risk criteria | Monitoring interval | NICE NG10 |
| Q009 | Temporary evaluation detention | 48 h maximum | Legal procedural limit, not clinical monitoring | Law 2071/1992 |
| Q019 | Clozapine baseline ANC | ≥1500/mm³ general; ≥1000/mm³ BEN | Initiation threshold | EMA/PRAC 2025 |
| Q019 | Clozapine ANC frequency | Weekly 18 wk → monthly next 34 wk → q12wk after 1 y if no neutropenia → annual after 2 y if none | Current EU monitoring schedule | EMA/PRAC 2025 |
| Q019 | Clozapine adequacy TDM | ≥350 ng/mL trough | Useful exposure benchmark, not universal target | TRRIP/TDM consensus |
| Q019 | Clozapine restart | Interruption >48 h | Low-dose restart/re-titration | Current SmPC |
| Q026/Q081 | Lithium maintenance | 0.6–0.8 mmol/L | Standard maintenance range | NICE CG185/QS95 |
| Q026/Q081 | Selected higher lithium maintenance | 0.8–1.0 mmol/L | Selected relapse/persistent symptoms | NICE CG185 |
| Q081 | Lithium sample timing | ~12 h post-dose | Trough timing | NICE |
| Q081 | Lithium routine monitoring | q3mo first year; q6mo after, or q3mo higher risk; renal/thyroid/calcium q6mo | Ongoing monitoring | NICE |
| Q081 | EXTRIP ECTR recommendation | Impaired renal function + Li >4.0 mEq/L OR decreased consciousness/seizures/life-threatening dysrhythmias regardless level | Specialist toxicology indication | EXTRIP |
| Q081 | EXTRIP ECTR suggestion | >5.0 mEq/L, confusion, or expected >36 h to <1.0 | Specialist toxicology suggestion, not stand-alone bedside rule | EXTRIP |
| Q082 | Valproate stable monitoring | FBC/LFT/weight at 6 months then annually | NICE stable-treatment monitoring | NICE CG185 |
| Q083 | Lamotrigine interruption | ~5 half-lives | Restart initial escalation; half-life changes with interacting drugs | SmPC |
| Q085 | ADHD cardiovascular follow-up | Pulse/BP before/after dose changes and every 6 months | NICE monitoring | NICE NG87 |
| Q045 | 4AT | ≥4 | Possible delirium/cognitive impairment; not diagnosis | 4AT/NICE |
| Q051 | Dementia antipsychotic review | At least every 6 weeks | Stop if no ongoing benefit | NICE NG97 |
| Q063 | MEED red examples | BMI <13; pulse <40; T <35.5°C; glucose <3.0 mmol/L | Risk indicators, not stand-alone admission criteria | MEED 2022 |
| Q078 | Antipsychotic weight | Weekly 6 wk, 12 wk, 1 y, annually | NICE schizophrenia monitoring | NICE CG178 |
| Q078 | Antipsychotic waist | Annually after baseline | NICE schizophrenia monitoring | NICE CG178 |
| Q078 | Antipsychotic BP/pulse/glucose/lipids | 12 wk, 1 y, annually after baseline | NICE schizophrenia monitoring | NICE CG178 |
| Q078 | QTc | >500 ms | High-risk threshold for urgent review/change and correction of reversible factors | Cardiac safety guidance |
| Q088 | TCA QRS | >100 ms | Major sodium-channel-toxicity/seizure-risk anchor; treatment thresholds vary 100–120 ms by protocol | Poison-centre guidance |
| Q088 | TCA alkalinaemia target | ~7.50–7.55 | Common bicarbonate endpoint; avoid overshoot | Poison-centre guidance |

## 8. Epidemiology/prognosis master table

| Q | Proposed claim | Decision | Publication instruction |
|---|---|---|---|
| Q004 | Suicide-tool PPV <5% | DROP_NUMBER_KEEP_QUALITATIVE | NICE explicitly rejects predictive use/risk stratification; no need one PPV. |
| Q005 | Prior attempt = 15–30×; highest risk 3–12 months | DROP_NUMBER_KEEP_QUALITATIVE | Prior attempt/early post-discharge period are major risk markers; exact multiplier/window heterogeneous. |
| Q006 | SMI victims 3–5× more likely than perpetrators | DROP_NUMBER_KEEP_QUALITATIVE | Retain victimisation burden and weak explanatory role of diagnosis alone. |
| Q011 | FEP response 70–80%; half-dose rule | DROP_NUMBER_KEEP_QUALITATIVE | Use lower end licensed range and titrate individually. |
| Q011 | Cannabis psychosis 2–5×; onset 2.7 y earlier | DROP_NUMBER_KEEP_QUALITATIVE | Retain dose-response/high-potency association. |
| Q012 | Schizophrenia prevalence/incidence/sex/onset fixed set | MODIFY | Use only broad prevalence around ~0.5–1% if needed; onset earlier/incidence modestly higher in men. |
| Q015 | 20/40/40 schizophrenia outcome distribution | DROP_NUMBER_KEEP_QUALITATIVE | Outcome distributions depend on era/cohort/endpoint. |
| Q015 | SMR 2.5–3, life expectancy −15–20, suicide 4.9% | MODIFY | Retain major mortality/life-expectancy/suicide gap; optional broad 10–20-y life-expectancy loss follow-up. |
| Q017 | Relapse off 70–80% vs on 20–30% | DROP_NUMBER_KEEP_QUALITATIVE | Maintenance reduces relapse; absolute rates heterogeneous. |
| Q018 | TRS prevalence 20–30% | MODIFY | Substantial minority; number optional. |
| Q021 | Depression recurrence 50/70/90 | DROP_NUMBER_KEEP_QUALITATIVE | Risk rises with prior episodes/residual symptoms. |
| Q023 | Bipolar prevalence, sex, FDR risk, heritability set | DROP_NUMBER_KEEP_QUALITATIVE | Highly familial/polygenic; estimates vary. |
| Q024 | Valproate pregnancy risks | KEEP_REGULATORY | ≈10–11% major malformations; developmental problems up to ~30–40% are official counselling figures. |
| Q026 | Lithium suicide reduction 60–80% | DROP_NUMBER_KEEP_QUALITATIVE | Evidence supports suicide/self-harm reduction; effect size unstable. |
| Q026 | Psychoeducation relapse reduction 30–40% | DROP_NUMBER_KEEP_QUALITATIVE | Benefit varies. |
| Q027 | Postpartum psychosis incidence | KEEP_APPROX | ≈1–2/1000 births is a defensible broad anchor. |
| Q027 | Bipolar PPP 25–50%; recurrence 50–60% | DROP_NUMBER_KEEP_QUALITATIVE | High risk but strongly history/treatment dependent. |
| Q027 | Blues 50–80%; PPD 10–15% | DROP_NUMBER_KEEP_QUALITATIVE | Low-value prevalence anchors. |
| Q045 | Delirium subtype 50/25/25; hypoactive worst mortality | DROP_NUMBER_KEEP_QUALITATIVE | Hypoactive common/under-recognised. |
| Q048 | DLB neuroleptic mortality 2–3× | DROP_NUMBER_KEEP_QUALITATIVE | Severe sensitivity/safety risk remains. |
| Q048 | Dopamine-agonist ICD 15–20% | DROP_NUMBER_KEEP_QUALITATIVE | Major medication risk; prevalence depends exposure/population. |
| Q049 | FTD genetic 30–40% | DROP_NUMBER_KEEP_QUALITATIVE | Family/genetic disease important; specific genes follow-up. |
| Q051 | BPSD AP stroke 3×/mortality 1.5–1.7× | DROP_NUMBER_KEEP_QUALITATIVE | Regulatory risk remains; no frozen multiplier. |
| Q051 | Nonpharm BPSD response 70% | DROP_NUMBER_KEEP_QUALITATIVE | Nonpharm first; no universal response % |
| Q054 | Levetiracetam behavioural AE 10–15% | DROP_NUMBER_KEEP_QUALITATIVE | Recognised adverse effects; frequency varies. |
| Q061 | Down syndrome AD neuropathology virtually universal by 40 | DROP_NUMBER_KEEP_QUALITATIVE | Very high age-related AD pathology/risk; exact age not needed. |
| Q069 | BPD 10-y remission 85%; suicide 5–10% | DROP_NUMBER_KEEP_QUALITATIVE | Remission often occurs; function may lag; suicide risk important. |
| Q070 | Psychopathy/PCL-R prevalence and cutoff | DROP_NUMBER_KEEP_QUALITATIVE | Specialist forensic construct; jurisdiction-dependent thresholds. |
| Q096 | Familial recurrence and heritability tables | DROP_NUMBER_KEEP_QUALITATIVE | Population estimates should not be individual predictions. |
| Q096 | PRS explains 7–10% variance | DROP_NUMBER_KEEP_QUALITATIVE | Changing research metric; not routine clinical test. |

## 9. Historical exam-fact table

| Q | Classic material | Decision | Current-use qualification |
|---|---|---|---|
| Q001 | Jaspers: Verstehen vs Erklären | RETAIN | Classic conceptual psychopathology; not current diagnostic criterion. |
| Q002 | Jaspers’ delusion criteria | RETAIN_QUALIFIED | Classic criteria; literal falsity/impossibility is not a modern universal requirement. |
| Q002 | Wernicke overvalued idea | RETAIN | Useful historical descriptive distinction. |
| Q002 | Primary vs secondary delusions; delusional perception/mood/intuition | RETAIN | Classic Jaspersian phenomenology; not ICD/DSM criterion set. |
| Q012 | Schneiderian first-rank symptoms | RETAIN | Exam recognition only; non-pathognomonic. |
| Q012 | Paranoid/hebephrenic/catatonic/undifferentiated/residual schizophrenia subtypes | RETAIN | Historical DSM-IV/ICD-10/Kraepelinian taxonomy; removed from current DSM/ICD. |
| Q035 | Somatization disorder/hypochondriasis/pain disorder old taxonomy | RETAIN | Historical context; current DSM/ICD architecture differs. |
| Q052 | ‘Diogenes syndrome’ | RETAIN_QUALIFIED | Historical/descriptive label for severe self-neglect/squalor; not a single current diagnosis. |
| Q054 | Geschwind syndrome | RETAIN_CONTESTED | Historical/controversial TLE personality construct; do not present as current nosology. |
| Q067 | Classic sleep percentages and depression PSG signature | RETAIN_QUALIFIED | Physiology/exam associations, not diagnostic facts; avoid rigid percentages/REM-latency cutoff. |
| Q094 | Papez circuit | OPTIONAL_HISTORICAL | Anatomically/historically useful, but not a complete modern memory/emotion network model. |

## 10. Greek legal corrections

These are jurisdiction-specific. They must not be silently replaced with UK/US capacity, Mental Health Act, Tarasoff or forensic doctrines.

| Q | Claim/domain | Decision | Current Greek formulation |
|---|---|---|---|
| Q008 | Law 3418/2005 Arts 11–12 | KEEP | Information + consent basis; mental disorder/involuntary status does not automatically remove consent rights. |
| Q008 | Substitute consent | MODIFY | Appointed judicial supporter if legally empowered; otherwise statute says οικείοι. Do not invent spouse→parent→child→sibling hierarchy. |
| Q008 | Emergency exception | KEEP | Art 12(3): urgent care when appropriate consent cannot be obtained; attempted suicide separately included. |
| Q009 | Law 2071/1992 Art 95 routes | KEEP | Route I and alternative Route II remain current. |
| Q009 | 48h/3d/10d/48h summons/3mo/6mo | KEEP | Statutory procedural anchors; interpret each in correct procedural context. |
| Q009 | Court designation | MODIFY | Current first-instance competence is Μονομελές Πρωτοδικείο; legacy Law 2071 text still names Πολυμελές. |
| Q009 | Transport statute | MODIFY | Correct law is 4931/2022 Art 59 inserting 96A—not Law 4999/2022. EKAB coordinates; mixed clinical/police initial team, community-unit vehicle onward, police accompaniment exceptional. |
| Q009/Q100 | Law 5129/2024 | KEEP_QUALIFIED | Service/network reorganisation; did not replace core Art 95 involuntary criteria. |
| Q052 | Self-neglect and coercion | MODIFY | Self-neglect/squalor alone is not an independent involuntary-admission criterion and does not create a general forced-social-care power. |
| Q073 | Greek gender pathway | UNRESOLVED | No uniform national service/referral/reimbursement rule verified for insertion. |
| Q089 | ECT without capacity/consent | UNRESOLVED | Capacitous adult consent and admission≠ECT authorisation are clear; ECT-specific Greek authorisation pathway in incapacity/emergency remains unresolved. |
| Q098 | Medical confidentiality Art 13 | KEEP | Continuing duty; exceptions for legal duty, justified substantial interest, necessity/defence, valid consent. |
| Q098 | Penal Code Art 371 | KEEP | Professional-secrecy offence; defence/justification for duty/substantial interest. |
| Q098 | Threat disclosure basis | MODIFY | Use Medical Code Art 13 and Penal Code Art 25; Art 32 is not the primary confidentiality justification. |
| Q098 | Planned felony reporting | KEEP | Penal Code Art 232: timely report to authority of reliably known planned/ongoing felony while prevention remains possible, subject to statutory conditions. |
| Q098 | Tarasoff-style direct duty to warn victim | UNRESOLVED | No general Greek Tarasoff statute verified; do not claim one. |
| Q098 | Domestic-violence reporting | MODIFY | Art 23 Law 3500/2006 must be cited as currently amended (5090/2024 and 5172/2025), including professional duties regarding indications in minors. |
| Q099 | Penal Code Art 34 | KEEP | Cognitive OR volitional incapacity at offence time due qualifying condition. |
| Q099 | Penal Code Art 36 | KEEP | Substantially reduced capacity → reduced punishment; not absence of responsibility. |
| Q099 | Art 69 safety measure automaticity | MODIFY | Any forensic safety measure is a separate judicial decision with their own statutory criteria. Do not imply automatic forensic hospitalisation. |
| Q100 | EDYPSY/PEDYPSY | KEEP | Law 5129/2024 created national network and seven regional networks. |
| Q100 | Adult CMHC naming | MODIFY | Use Κέντρο Ψυχικής Υγείας (ΚΨΥ); do not use KoKEPSY generically for adult community centres. |

## 11. Research gaps remaining

| Priority | Q | Gap | Instruction |
|---|---|---|---|
| HIGH | Q089 | Greek ECT-specific procedure for incapacitous or emergency non-consensual ECT | General consent/involuntary-admission law is clear; no clean ECT-specific court/prosecutor/guardian/second-opinion rule verified. Do not import UK law. |
| MEDIUM | Q007 | National Greek acute-agitation formulary/protocol availability for IM olanzapine, aripiprazole and zuclopenthixol acetate | Hospital/local availability may differ; no national protocol verified. |
| MEDIUM | Q073 | Current national Greek adult gender-incongruence service/referral/reimbursement pathway | Do not invent a uniform pathway. |
| LOW | Q077 | Routine Greek availability/reimbursement of deutetrabenazine after 2026 EU authorisation | EU authorisation is verified; Greek access/reimbursement not. |
| LOW | Q098 | Whether a particular imminent-threat scenario creates a direct duty to warn the intended victim rather than reporting to authorities/other protective disclosure | No general Tarasoff rule verified; case-specific Greek legal advice may be required. |

## 12. Writer directives

1. Do not require a numerical anchor in every question. Add a number only when it materially discriminates diagnosis, treatment, safety, monitoring, legal procedure or a genuinely stable epidemiological fact.
2. Never convert a screening score into a diagnosis. 4AT, MoCA, MMSE, BFCRS, BVC, CIWA-Ar, COWS and similar tools must be labelled by purpose and limitation.
3. Use `DROP_NUMBER_KEEP_QUALITATIVE` whenever the direction of effect is robust but the magnitude is heterogeneous: suicide multipliers, violence/victimisation ratios, relapse rates, heritability tables and long-term outcome distributions.
4. Distinguish classification systems whenever a duration/count is system-specific. DSM timing must never be presented as ICD-11 timing by default.
5. Historical psychopathology must be visibly labelled `HISTORICAL_EXAM_FACT`; it must never be phrased as a current DSM-5-TR/ICD-11 criterion.
6. Never use `pathognomonic`, `mandatory`, `always`, `never`, `gold standard`, `strongest predictor` or `contraindicated` unless the cited current authority genuinely supports that scope.
7. For guidelines, use their actual verb: `offer`, `consider`, `do not offer`, `avoid`, `monitor`, `review`. Do not upgrade `consider` to `must`.
8. Do not attribute doses to a guideline that only names a regimen. For rapid tranquillisation, NICE NG10 supplies regimen choices and monitoring; exact milligram doses require a current BNF/SmPC/local-formulary source.
9. Catatonia: retain ≥3 signs and the lorazepam challenge. Restrict the 8→24 mg/day and 48–72 h ECT rule specifically to BAP malignant-catatonia recommendations. NMS drugs are severity-dependent options, not mandatory antidotes.
10. Schizophrenia: keep DSM-versus-ICD duration distinctions; drop rigid prevalence/sex/onset sets, 70–80% FEP response, a 50% dose rule and fixed three-bin outcome distributions.
11. TRS: distinguish TRRIP from NICE. TRRIP requires two adequate ≥6-week trials but not one SGA; NICE’s clozapine pathway specifies at least one failed non-clozapine SGA.
12. Clozapine: use the current EU 2025 ANC schedule. Treat ≥350 ng/mL as an exposure/adequacy benchmark, not a universal therapeutic border; avoid deterministic 600/1000 ng/mL toxicity rules.
13. Clozapine smoking/infection: teach the mechanisms—smoke PAHs induce CYP1A2; inflammation can suppress CYP1A2—and use TDM/clinical response rather than a fixed percentage dose change.
14. Depression/bipolar recurrence and lithium suicide-prevention effects should remain qualitative unless an exact current regulatory/guideline number is needed.
15. Valproate: reproduce current EU reproductive restrictions accurately, including PPP conditions for women and the 3-month male contraception/sperm-donation precautions; do not simplify to ‘banned in all women’.
16. Do not list lurasidone/cariprazine as routine EU bipolar-depression licensed options merely because international trials/guidelines support efficacy; distinguish evidence, licence and guideline jurisdiction.
17. OCD: use licensed SmPC dose escalation. Do not teach routine supra-licensed escitalopram 40 mg or a rule requiring 12 weeks at maximum dose.
18. Alcohol withdrawal: present timing as approximate overlapping windows; use current Wernicke IV thiamine 300–500 mg TID guidance and never delay emergency glucose for hypoglycaemia.
19. Buprenorphine: teach high-affinity partial μ-agonism and precipitated withdrawal. Do not freeze COWS 8–12 across all opioids/fentanyl contexts.
20. Functional seizures: never use a normal interictal/post-event EEG as the diagnostic rule. Use positive semiology and, when needed, video-EEG capture of a typical event without ictal epileptiform activity.
21. Dementia scales are screening aids, not diagnostic thresholds. A normal score does not exclude dementia; structural imaging and biomarkers support subtype/etiology in context.
22. Anti-amyloid therapy: keep EU eligibility and ARIA-monitoring rules treatment-specific. Do not generalise APOE testing/MRI schedules to all Alzheimer diagnosis.
23. MEED: use selected red examples only within multidomain risk formulation. Do not turn BMI <13 or HR <40 into independent admission rules and do not impose one universal refeeding calorie schedule.
24. Personality disorder: current ICD-11 severity + five trait domains + borderline qualifier supersedes categorical ICD-10 teaching in the current-practice layer.
25. Lithium: retain 0.6–0.8 mmol/L maintenance, selected 0.8–1.0, 12-h sampling and NICE monitoring. Never teach haemodialysis as `dialyse above X`; use EXTRIP integrated criteria.
26. Lamotrigine: after interruption beyond about five half-lives, restart the initial escalation. Do not translate this into a fixed 3–5-day rule because half-life changes with interacting drugs.
27. TCA overdose: QRS >100 ms is a useful toxicity anchor; sodium bicarbonate follows significant sodium-channel cardiotoxicity/haemodynamic compromise and poison-centre protocol. Secondary aVR metrics belong in follow-up, not model answer.
28. ECT: do not use seizure duration ≥25–30 s as an adequacy criterion or absolute contraindication lists. Greek ECT-specific incapacity/emergency authorisation remains unresolved.
29. Greek law: cite statutes exactly. Correct involuntary transport to Law 4931/2022 Art 59; retain the Monomeles/legacy-text mismatch; use Law 3418/2005 Art 13 and Penal Code Arts 232/371 for confidentiality; never import UK MCA/MHA or Tarasoff.
30. Greek criminal/community systems: diagnosis never equals criminal irresponsibility—use Penal Code Arts 34/36 retrospectively and offence-specifically; use Ε.Δ.Υ.Ψ.Υ./seven Πε.Δ.Υ.Ψ.Υ. and ΚΨΥ under the post-2024 system without bureaucratic overgrowth.


### Verification metrics

- Candidate claim units adjudicated: **349**
- `KEEP`: **152**
- `MODIFY`: **161**
- `DROP`: **31**
- `UNRESOLVED`: **5**
- Approved numerical anchors/rows: **66**
- Approved drug/class mechanism rows: **33**
- Approved emergency-dose anchors: **4**
- Approved monitoring/threshold rows: **24**
- Historical exam facts retained/qualified: **11**
- Greek legal/system claims modified in the compact legal table: **8**

**Status: `FULL_ENRICHMENT_VERIFICATION_READY`.**
