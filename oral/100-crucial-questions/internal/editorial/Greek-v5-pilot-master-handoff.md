# Greek v5 pilot — master Writer handoff

Status: **READY FOR FRESH WRITER CHAT**

Branch: `greek-v5-pilot`

Repository: `orestispsom/Psychiatry-Exams`

## 1. Purpose

Create a deliberately small, high-quality **Greek-first v5 calibration set** before any further 100-question manufacture.

The problem being solved is no longer mainly factual completeness. Final v4 is strong clinically, but residual defects remain in:

- translated-English Greek;
- repetitive AI-shaped sentence cadence;
- uneven information architecture;
- criteria/monitoring information sometimes being placed in prose when a checklist or table would retrieve better;
- non-obvious acronyms appearing before local explanation;
- answers that are correct but do not yet sound as if originally written by an experienced Greek psychiatrist for an oral board examination.

This pilot must demonstrate a materially better editorial standard before v5 is scaled.

## 2. Pilot questions

Rewrite only these eight questions:

- **Q001** — initial psychiatric assessment
- **Q012** — clinical picture and diagnosis of schizophrenia
- **Q019** — clozapine
- **Q020** — depressive episode / major depression diagnosis and differential
- **Q038** — alcohol withdrawal
- **Q045** — delirium
- **Q090** — CBT
- **Q098** — medical confidentiality in Greece

These were selected because they stress different answer archetypes: assessment, diagnosis, psychopharmacology/monitoring, operational diagnostic criteria, emergency/addictions, liaison/emergency medicine, psychotherapy and Greek law.

Do **not** rewrite Q002–Q011, Q013–Q018 or any other non-pilot question in this task.

## 3. Output

Do not overwrite final v4.

Create:

`oral/100-crucial-questions/answers/revision-v5-pilot-el/Q001.md`

`Q012.md`

`Q019.md`

`Q020.md`

`Q038.md`

`Q045.md`

`Q090.md`

`Q098.md`

Also create:

`oral/100-crucial-questions/internal/editorial/Greek-v5-pilot-writer-report.md`

No PDF in this task.

## 4. Source hierarchy — crucial change from previous versions

### 4.1 Final v4 is a reference, not scripture

Use:

`oral/100-crucial-questions/answers/final-v4-el/`

as:

- a completeness check;
- a record of already adjudicated material;
- a source of useful board facts and prior decisions.

Do **not** preserve its wording, paragraph order or structure merely because it is current final v4.

If a substantially better Greek-first structure expresses the same verified content more clearly, rewrite from scratch.

### 4.2 Approved factual/verification layer controls consequential claims

Use the relevant approved batch briefs and current-verification material in the repository, especially:

- `oral/100-crucial-questions/answers/briefs/Q001-Q010-batch.md`
- `oral/100-crucial-questions/answers/briefs/Q011-Q019-batch.md`
- `oral/100-crucial-questions/answers/briefs/Q020-Q027-batch.md`
- `oral/100-crucial-questions/answers/briefs/Q037-Q044-batch.md`
- `oral/100-crucial-questions/answers/briefs/Q045-Q051-batch.md`
- `oral/100-crucial-questions/answers/briefs/Q090-Q100-batch.md`
- `oral/100-crucial-questions/internal/revision/Q001-Q100-board-depth-current-verification.md`
- the final v4 source-use ledger and adjudication report under `internal/editorial/`.

For diagnosis, preserve system-specific DSM-5-TR / ICD-11 distinctions already verified in the approved layer.

For treatment, psychopharmacology, monitoring, current regulation and Greek law, the verified/current layer overrides older exam shorthand.

### 4.3 Greek exam/base-source language

When the repository provides source-locked Greek exam/base material from the prescribed Greek Shorter Oxford or other designated exam sources, use it to anchor established Greek psychiatric terminology and classic exam framing.

Do not invent Greek textbook wording or quotations if the source is not actually accessible.

### 4.4 Do not launch a new broad research project

This is an editorial calibration task, not another comprehensive evidence review.

If a consequential factual ambiguity cannot be resolved from the approved repository layer, do not guess. Mark it in the Writer report as `SOURCE_QUERY` and preserve the safest already-adjudicated formulation.

## 5. Greek-first writing principle

Do not translate sentence-by-sentence from English.

For each question:

1. Determine the verified clinical meaning and the exam objective.
2. Decide the best oral-answer architecture in Greek.
3. Write the answer in natural Greek as if composing it originally.
4. Use v4 only afterwards as a completeness check.
5. Re-check factual anchors against the approved source layer.

The finished answer should sound like a senior Greek psychiatrist teaching a strong resident, not like a translated guideline summary.

## 6. Hard anti-AI rule

Obvious AI-shaped language is heavily penalised.

Aggressively scrutinise repeated patterns such as:

- `δεν είναι απλώς ... αλλά ...`
- `όχι μόνο ... αλλά ...`
- `το βασικό είναι ...`
- `το κρίσιμο σημείο είναι ...`
- `η πρακτική απάντηση είναι ...`
- `η συνοπτική απάντηση ...`
- repeated `δεν ...· ...` contrast constructions;
- generic final paragraphs that merely restate the answer;
- unnecessary narration about what the candidate “would not” say;
- writer/source-process language.

These constructions are not banned individually. Repetitive generated cadence is the defect.

Prefer direct clinical Greek.

Example principle:

Instead of constructing a paragraph around “X is not merely Y; rather it is Z”, usually state Z directly and then add the relevant limitation only if it teaches something.

## 7. Acronym and named-instrument rule

A non-obvious acronym or instrument must be expanded **before or at its first visual occurrence within that question**, including the Recall Axis.

Do not rely on an expansion later in the model answer.

Examples relevant to the pilot include:

- absolute neutrophil count / ANC;
- therapeutic drug monitoring / TDM;
- CIWA-Ar;
- BFCRS if retained in Q012-related material (do not add it unless relevant);
- 4 'A's Test / 4AT;
- CAM-ICU / ICDSC;
- any specialist legal/clinical abbreviation not obvious to a reader opening that question directly.

Common diagnostic/manual abbreviations such as DSM-5-TR and ICD-11 may remain abbreviated.

## 8. Named triad / cluster rule

If the prose invokes a classic triad, tetrad, diagnostic cluster or numbered set, state the components immediately.

Example for Wernicke:

`κλασική τριάδα (μεταβολή νοητικής κατάστασης + οφθαλμοκινητικές διαταραχές + αταξία)`

Do not force the learner to recall what an unnamed “classic triad” contains.

## 9. Diagnostic denominator rule

If the answer states a central operational count such as `≥5/10`, `≥2/5`, `≥2/7`, etc., show the actual counted items nearby as a numbered list, checklist or compact table.

Do not bury a criteria denominator in prose.

Keep DSM-5-TR and ICD-11 structures separate.

## 10. Answer architecture is question-specific

Do not impose one universal template beyond the required core sections.

### Q001 — assessment archetype

Preferred sequence:

1. immediate safety / medical urgency;
2. presenting problem and longitudinal history;
3. collateral information;
4. mental-state examination;
5. physical/neurological assessment and targeted investigations;
6. explicit risk/capacity where relevant;
7. differential + formulation + plan.

A compact visible list of MSE domains and/or formulation scaffold is preferable to burying all domains in prose.

### Q012 — diagnostic archetype

Preferred sequence:

1. syndrome domains and clinical picture;
2. visible DSM-5-TR operational criteria;
3. visible ICD-11 operational criteria;
4. duration/functional requirements;
5. differential diagnosis;
6. primary vs secondary negative symptoms;
7. classic historical psychopathology clearly labelled historical.

Use a table only if it improves DSM/ICD discrimination more than two separate compact lists.

### Q019 — drug/monitoring archetype

Preferred sequence:

1. indications and where clozapine sits in treatment sequencing;
2. baseline/start eligibility if relevant;
3. **visible ANC monitoring schedule**;
4. major life-threatening risks;
5. common/important adverse effects;
6. TDM, smoking, infection and interactions;
7. interruption/restart rule;
8. focused examiner follow-up.

A compact monitoring table is encouraged if clearer than prose.

The Recall Axis must not begin with unexplained `ANC` or `TDM`.

### Q020 — diagnostic archetype

Preferred sequence:

1. clinical depressive syndrome organised for oral recall;
2. psychosis/suicidality/severity;
3. explicit current ICD-11 counted symptom set where the 5/10 denominator is used;
4. DSM terminology distinguished rather than blended;
5. bipolar screen and differential diagnosis.

Do not say 5/10 without showing the 10.

### Q038 — emergency/addictions archetype

Preferred sequence:

1. recognition and severity/risk of complicated withdrawal;
2. appropriate setting;
3. benzodiazepine strategy;
4. locally expanded CIWA-Ar and its limitations;
5. thiamine/medical support;
6. seizure/delirium escalation;
7. Wernicke section with the **classic triad stated explicitly** and the verified parenteral thiamine regimen.

### Q045 — delirium archetype

Preferred sequence:

1. core syndrome: acute/subacute, fluctuating attention/awareness;
2. subtypes and high-risk hypoactive presentation;
3. causes + collateral baseline;
4. detection tools, with names expanded locally;
5. treat cause + non-pharmacological bundle;
6. limited role and safety constraints of antipsychotics.

A brief “cause search” checklist may retrieve better than a long cause paragraph.

### Q090 — psychotherapy archetype

Preferred sequence:

1. what CBT is in clinically meaningful terms;
2. formulation/model;
3. therapeutic process / collaborative empiricism;
4. disorder-specific techniques;
5. between-session work and relapse prevention;
6. selected psychiatric applications/limits.

Avoid generic psychotherapy prose and “CBT = positive thinking” straw-man cadence in the main answer. Keep the oral answer compact and specific.

### Q098 — Greek law archetype

Preferred sequence:

1. general duty of confidentiality and principal Greek legal basis;
2. what information is protected;
3. lawful/ethical exceptions and minimum-necessary disclosure;
4. relevant reporting duties and their limits;
5. imminent-risk/protective disclosure boundary without importing a US/UK Tarasoff rule;
6. documentation and practical handling;
7. traps.

Use a compact rule/exception table if it improves legal retrieval.

## 11. Required learner-facing structure

Each pilot file should contain, as appropriate:

- question heading;
- `## Άξονας ανάκλησης`;
- `## Πρότυπη προφορική απάντηση`;
- `## Βασικά σημεία για τις εξετάσεις`;
- `## Συχνές παγίδες / παγίδες εξεταστή`.

Examiner follow-ups and exam-vs-current sections are optional and should appear only when they genuinely improve viva preparation.

## 12. Recall Axis standard

Usually 5–7 terse cues.

It should allow reconstruction of the answer.

Avoid:

- mini-paragraphs;
- unexplained acronyms;
- generic items that do not discriminate sequence or content.

## 13. Model oral answer standard

This remains the central object.

It should sound natural aloud and usually fit roughly 2–4 minutes.

Use prose for reasoning and synthesis.

Use lists/tables where the examiner expects enumeration or where retrieval is clearly improved.

Do not convert the entire model answer into bullet points.

## 14. Board facts and traps

`Βασικά σημεία για τις εξετάσεις`:

- usually 4–6 strong points;
- thresholds, durations, discriminators, monitoring and high-value exceptions;
- avoid duplicating the oral answer sentence-for-sentence.

`Συχνές παγίδες / παγίδες εξεταστή`:

- usually 4–6 plausible errors;
- discriminate DSM/ICD, current/historical, diagnosis/treatment, monitoring or legal boundaries;
- no filler.

## 15. Language standard

Prefer established Greek psychiatric/medical terminology.

International technical names can remain parenthetically at first use when recognition is useful, but Greek should carry the sentence.

Avoid unnecessary English such as `standard care`, `setting`, `follow-up`, `cut-off`, `on/off`, `switch`, `taper`, etc. when natural Greek exists.

Do not over-Hellenise internationally conventional drug names or validated instrument names.

## 16. Fidelity gate

Do not change without approved source support:

- diagnosis thresholds;
- symptom denominators;
- durations;
- doses;
- concentrations;
- monitoring schedules;
- indications/licensing;
- contraindications;
- Greek law/article numbers;
- recommendation strength;
- causal strength.

Do not turn `may/consider` into `must/indicated`.

Do not turn association into causation.

## 17. Mandatory Writer self-QA

Before completion, compare each v5 pilot file against:

1. its approved factual brief/current-verification material;
2. final v4 for completeness;
3. the scoring rubric:
   `oral/100-crucial-questions/internal/editorial/Greek-v5-pilot-scoring-rubric.md`.

For each question explicitly check:

- natural Greek;
- AI cadence;
- oral usability;
- retrieval structure;
- criteria/operational visibility;
- acronym first-use expansion;
- named clusters explained;
- Recall Axis quality;
- Board Facts quality;
- Traps quality;
- no content drift.

## 18. Writer report

Create `Greek-v5-pilot-writer-report.md` containing:

- eight files completed;
- source files used for each question;
- structural changes made from v4;
- criteria/checklists/tables introduced;
- acronyms/instruments expanded;
- any `SOURCE_QUERY` items;
- any deliberate decision to retain English terminology and why;
- self-assessed score for each question using the v5 rubric;
- statement on whether the pilot is ready for independent adjudication.

Do not claim publication readiness. The next stage is independent grading/adjudication.

## 19. Git workflow

Work only on branch `greek-v5-pilot`.

Commit in two calibration batches:

- **Pilot A:** Q001, Q012, Q019, Q020
- **Pilot B:** Q038, Q045, Q090, Q098 + Writer report

Do not wait for founder approval between Pilot A and Pilot B.

Do not merge to `greek-v4-final` or `main`.

## 20. Completion status

Return:

- Pilot A commit SHA;
- Pilot B commit SHA;
- eight-question completion count;
- any `SOURCE_QUERY` items;
- self-QA summary;
- final status exactly:

`GREEK_V5_PILOT_WRITER_COMPLETE`
