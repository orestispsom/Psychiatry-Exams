# Q12 Contemporary Research Handoff — Schizophrenia Clinical Picture & Diagnosis

Status: READY_FOR_RESEARCH
Pilot: 1 of 5
Question source: Attempt 011
Output destination: `oral/100-crucial-questions/answers/source-packets/Q012-contemporary.md`

## Mission

Build the independent **current-authoritative research packet** for:

> **Q12. Describe the clinical picture and diagnosis of schizophrenia.**

This is the contemporary-evidence stream of the model-answer pipeline. It must be completed **independently of the prescribed Oxford Shorter 2017 textbook/local-library extraction** so that later adjudication can compare modern clinical truth with exam-source framing without anchoring contamination.

You are not writing the model answer.

## Repository orientation — read these first

1. `oral/100-crucial-questions/attempts/011.md` — current visible question set; Q12 is the target.
2. `oral/100-crucial-questions/internal/answer-coverage/007.yml` — Q12's inherited hidden coverage requirements.
3. `oral/100-crucial-questions/internal/board-fact-anchors.yml` — identify anchors mapped to Q12.
4. `oral/100-crucial-questions/reviews/010-greek-oral-129-mapping-audit.md` — use the Q12-related mapping as exam-priority context only; do not treat old oral answers as current authority.
5. `oral/100-crucial-questions/internal/source-register.md` — project source hierarchy and exam/current discipline.
6. `oral/100-crucial-questions/internal/answer-production/README.md`
7. `oral/100-crucial-questions/internal/answer-production/agent-prompts.md` — follow **A. Contemporary Research Lead**.
8. `oral/100-crucial-questions/internal/answer-production/dossier-schema.yml` — understand the later claim-level handoff, but do not instantiate the final dossier yourself.

## Q12 inherited must-cover territory

The research packet must resolve the contemporary clinical basis for:

- positive symptoms;
- negative symptoms;
- disorganisation/formal thought disorder;
- cognitive symptoms/dysfunction;
- affective symptoms commonly relevant to schizophrenia presentations;
- perceptual abnormalities relevant to schizophrenia;
- current diagnostic framework and longitudinal requirements;
- functional impairment/course elements relevant to diagnosis;
- required exclusion of mood disorders, substances/medications and medical/neurological causes;
- the contemporary diagnostic significance and limitations of Schneider first-rank symptoms;
- the role and limitations of symptom dimensions versus obsolete subtype thinking;
- important diagnostic boundaries that a senior Adult Psychiatry candidate should understand without turning Q12 into the separate differential question Q13.

Do not drift into detailed acute treatment, maintenance treatment, TRS or clozapine. Those belong to other main questions.

## Board-fact anchors relevant to this research

At minimum, inspect and prepare evidence for the following anchors where mapped to Q12:

- `bf.psychosis.schneider_first_rank`
- `bf.psychosis.schizophrenia_dsm_icd`
- `bf.psychosis.duration_boundaries` insofar as needed to define schizophrenia's diagnostic boundary
- `bf.psychosis.cognitive_profile`

For exact DSM-5-TR material: use an official/authoritative DSM-5-TR source if actually accessible. If the exact proprietary criterion text cannot be verified from an authoritative accessible source, **do not substitute a secondary website and pretend it is DSM authority**. Mark the exact criterion/wording as requiring local DSM/exam-source verification in the later local-source stream.

For ICD-11: prefer WHO's official ICD-11 materials.

## Contemporary research questions to answer

### A. Syndrome / phenomenology

1. What symptom domains best organise schizophrenia clinically today?
2. Which positive, negative, disorganised, cognitive and affective phenomena are most diagnostically/clinically important?
3. Which features are characteristic but not specific?
4. How should formal thought disorder and hallucinations be described without relying on historically overprivileged signs?
5. What is the current understanding of primary versus secondary negative symptoms insofar as diagnosis/phenomenology requires it?

### B. Diagnosis

1. What does DSM-5-TR currently require for schizophrenia diagnosis at a conceptual level and, where authoritatively verifiable, at exact criterion/duration level?
2. What does ICD-11 currently require, and how does its diagnostic framing differ materially from DSM-5-TR?
3. What longitudinal/functional information is essential rather than relying on a cross-sectional MSE?
4. What exclusions are mandatory before diagnosing schizophrenia?
5. Which psychotic-spectrum boundaries belong naturally in a Q12 answer, versus being deferred to Q13?

### C. Historical/classic examination concepts

1. What are Schneider first-rank symptoms?
2. What is their contemporary diagnostic status/specificity?
3. What happened to classical schizophrenia subtypes in modern classification?
4. Are there other classic terms/concepts a modern senior psychiatrist should recognise even if they no longer determine diagnosis?

### D. Cognitive symptoms

1. Which cognitive domains are reproducibly impaired in schizophrenia?
2. Are cognitive deficits part of formal diagnostic criteria?
3. At what stage of illness can they be present?
4. What level of quantitative statement, if any, is sufficiently robust to become a board fact rather than trivia?

### E. Update-sensitive areas likely to matter when compared later with Oxford Shorter 2017

Identify, without consulting Oxford for this task:

- DSM-5-TR versus current ICD-11 framing;
- the current status of first-rank symptoms;
- dimensional description versus historical subtype language;
- any modern terminology changes that could create an exam/current distinction.

Do not speculate about what Oxford says. Merely flag the contemporary position that will need comparison.

## Source hierarchy for this task

Use current authoritative/primary sources wherever practical.

Priority:

1. DSM-5-TR / official APA materials for DSM claims.
2. WHO ICD-11 official classification/clinical descriptions for ICD claims.
3. Current major schizophrenia guidelines where they inform diagnostic assessment rather than treatment.
4. High-quality systematic reviews/meta-analyses or major consensus/research papers for questions such as cognitive impairment, negative symptoms or first-rank symptom validity.
5. Authoritative current textbooks/reviews only where primary/official sources do not adequately resolve a stable foundational point.

Do not use generic clinical websites, exam-prep websites, Wikipedia, commercial summaries or unsourced search snippets as authorities for consequential claims.

## Required deliverable

Create/update exactly:

`oral/100-crucial-questions/answers/source-packets/Q012-contemporary.md`

Use this structure:

```markdown
# Q12 Contemporary Research Packet — Schizophrenia Clinical Picture & Diagnosis

## 1. Question target

## 2. Proposed answer spine

## 3. Current-authoritative claim table
| Claim ID | Proposition | Importance | Authority/source | Evidence status | Destination suggestion |

## 4. Dangerous misses / examiner traps

## 5. Exact facts requiring later verification

## 6. Likely 2017-vs-current comparison points

## 7. Coverage trace
- Q12 hidden coverage item → supporting claim IDs
- Q12 board-fact anchor → supporting claim IDs / verification status

## 8. Sources actually inspected

## 9. Unresolved items / blocks
```

### Claim discipline

Use stable IDs such as:

- `Q12_CUR_DIAG_01`
- `Q12_CUR_PHEN_01`
- `Q12_CUR_COG_01`
- `Q12_CUR_HIST_01`

Every consequential statement that could enter the eventual model answer must be represented by a claim ID and cited to a genuinely supporting source.

Evidence status:

- `ESTABLISHED`
- `GUIDELINE_RECOMMENDATION`
- `SUPPORTED`
- `EMERGING`
- `CONTESTED`
- `HISTORICAL_ONLY`

Destination suggestion:

- `SPOKEN_CORE`
- `MUST_COVER_EXTENSION`
- `BOARD_FACT`
- `FOLLOWUP`
- `EXAM_CURRENT_NOTE`

## Hard exclusions

- Do not read or summarise Oxford Shorter 2017 for this task.
- Do not inspect local textbooks to answer the question; Claude/local-source extraction will do that independently.
- Do not use the old model answers in `orestispsom/Psych/src/data/oral.js` as factual authority.
- Do not write the final oral answer.
- Do not research detailed treatment beyond what is necessary to define/exclude diagnoses.
- Do not invent exact criteria, percentages, durations or historical claims.
- Do not collapse DSM-5-TR and ICD-11 into a synthetic hybrid criterion set.
- If an authoritative source is unavailable, mark the claim unresolved rather than weakening the source standard.

## Completion gate

Mark the packet `READY_FOR_ADJUDICATION` only if:

- every inherited Q12 must-cover item has current-source support or an explicit unresolved flag;
- every relevant board-fact anchor has either authoritative support or an explicit local/exam-source verification dependency;
- DSM and ICD claims are kept distinct;
- historical concepts are labelled as such;
- no treatment or unrelated psychosis material has bloated the packet;
- all sources actually inspected are listed.
