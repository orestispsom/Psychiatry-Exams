# Model-Answer Production System

Status: governing internal workflow for producing the final answers to **The 100 Crucial Questions in Psychiatry**.

## 1. Production objective

Each final question package should be capable of functioning as part of a plausible **board-sufficiency set for Greek Adult Psychiatry specialist certification**.

The aim is not to produce 100 polished essays. The aim is to produce 100 compact learning packages from which a candidate can:

- give a coherent senior-resident oral answer;
- survive predictable examiner interruptions and adjacent questions;
- retrieve exact high-yield board facts when required;
- distinguish exam-source truth from current clinical practice;
- reason through unfamiliar but related clinical scenarios.

The central production rule is:

> **Research, adjudication and writing are separate tasks. The writer does not decide what is true.**

No model answer should be drafted directly from general model memory or from a pile of textbooks without an approved question dossier.

---

## 2. Final learner-facing answer package

Each finished question should contain up to five components.

### A. Recall spine

A compact 4–7-part conceptual sequence that shows how to organise the answer mentally.

Example form:

`Recognise → diagnose/exclude mimics → assess risk → treat acute illness → plan maintenance/monitoring`

This is a retrieval aid, not an answer outline with every detail.

### B. Model oral answer

The main spoken answer.

Requirements:

- sounds like a strong senior psychiatry resident speaking to an examiner;
- answers the question immediately;
- first 2–4 sentences contain the skeleton of the whole answer, so the answer remains useful if interrupted early;
- expands naturally rather than reading like a checklist;
- usually supports approximately 2–5 minutes of speech, but length follows the question rather than a quota;
- integrates diagnosis, differential, risk, treatment and monitoring only where they belong naturally;
- does not include citations in the spoken prose unless the final publication format specifically requires them.

### C. Must-know board facts

A compact block containing only exact or classic facts that are genuinely worth retrieving separately:

- criteria/duration thresholds;
- classic distinctions;
- key calculations or epidemiological anchors;
- high-yield drug-specific facts;
- monitoring/timing anchors;
- historical exam facts where still relevant.

These facts are sourced from `../board-fact-anchors.yml` and must pass their stated verification gate before publication.

### D. Examiner follow-ups

Only the genuine pivots already approved in the visible question set, each with a concise answer.

A follow-up answer should usually be much shorter than the main answer and should directly answer the altered clinical problem.

### E. Exam answer vs current practice

Shown **only when a meaningful difference exists**.

Preferred format:

- **Exam answer:** what the designated exam source/edition expects.
- **Current practice:** what current authoritative guidance/classification/regulation supports.
- **Practical conclusion:** what the candidate should say or how to frame the discrepancy.

Do not manufacture this section when there is no genuine conflict.

---

## 3. Fractal oral-answer principle

Every model answer should work at three depths without being written three times.

### First 20–30 seconds

The opening should establish:

- what the condition/problem is;
- the organising framework;
- the most important clinical priority.

If the examiner interrupts here, the candidate should already sound oriented and safe.

### Approximately 2 minutes

The answer should cover the core diagnostic/clinical/treatment territory required for a competent pass.

### Approximately 4–5 minutes

If allowed to continue, the candidate should naturally add the discriminating material expected of an excellent candidate: difficult differentials, sequencing, resistance, monitoring, complications, special circumstances or mechanistic depth.

This should be achieved through paragraph ordering, not by publishing three redundant answer versions.

---

## 4. Mandatory production stages

No stage should silently perform the role of a later stage.

### Stage 0 — Question framing

Inputs:

- current visible question (`attempts/011.md` or successor);
- canonical coverage IDs;
- current answer-coverage specification;
- board-fact anchors;
- Greek oral-bank mappings;
- Adult Psychiatry and Greek-jurisdiction rules.

Output:

- question target;
- answer archetype;
- likely oral length class;
- required claims/questions for research;
- known exam-source/current-practice sensitivity.

No prose answer is written.

### Stage 1 — Independent contemporary research

Purpose:

Establish what a well-prepared contemporary adult psychiatrist should know **before anchoring to the 2017 exam textbook**.

The research lead should identify:

- current diagnostic framework where relevant;
- current treatment sequence and resistance/next-step logic;
- high-stakes differential diagnoses and red flags;
- monitoring and major adverse effects;
- special populations/contraindications where material;
- important areas of uncertainty or disagreement;
- exact claims requiring authoritative verification.

Source hierarchy follows the project rules:

- diagnosis: DSM-5-TR / ICD-11 as appropriate;
- treatment: current major guidelines → prescribing/regulatory sources → systematic reviews/meta-analyses → major trials → authoritative textbooks;
- psychopharmacology: current prescribing/regulatory sources and Maudsley-level references for doses, interactions, monitoring, pregnancy and licensing;
- Greek law/regulation: current official Greek sources;
- stable mechanisms/foundations: authoritative psychiatry/neuroscience texts.

Output is a structured research packet, **not a model answer**.

### Stage 2 — Official exam-source extraction: Oxford Shorter 7th ed. (2017)

This is the first local-textbook pass and has special status.

The local-source agent must determine:

- exact relevant chapter/section/pages;
- how Oxford organises the topic;
- what Oxford appears to expect an examination candidate to know;
- terminology, classic distinctions and characteristic teaching points;
- exam-relevant facts absent from the contemporary research packet;
- statements that appear outdated, ambiguous or materially different from current practice.

The agent must not silently modernise Oxford and must not write the final answer.

### Stage 3 — Targeted local-textbook triangulation

Only after Oxford has been extracted.

Use other local books selectively to answer unresolved questions, not to perform indiscriminate parallel summaries.

Suggested roles:

- **Oxford New Textbook of Psychiatry 3rd ed.** — depth, modern specialist framing, neuropsychiatry and broader conceptual triangulation;
- **Kaplan & Sadock's Synopsis 2021** — classic examination distinctions and broad cross-check;
- **Comprehensive Textbook** — only when a substantive point remains unresolved;
- **Maudsley 15th / current prescribing references** — psychopharmacology, monitoring, interactions and special populations;
- **Stahl / Prescriber's Guide / Practical Psychopharmacology** — mechanisms and practical drug differentiation where useful;
- specialist books (e.g. clozapine, adult autism) only for questions where they materially improve the dossier.

Stop when the information required by the dossier has converged. More sources are not automatically better.

### Stage 4 — Dossier synthesis and adjudication

All source packets are converted into one **canonical question dossier** using `dossier-schema.yml`.

This is the truth-resolution stage.

Every consequential claim should be assigned one of:

- `APPROVED_EXAM_AND_CURRENT`
- `APPROVED_EXAM_ONLY`
- `APPROVED_CURRENT_ONLY`
- `APPROVED_WITH_EXAM_CURRENT_SPLIT`
- `CONTESTED_BUT_INCLUDE`
- `EXCLUDE`
- `UNRESOLVED_BLOCK`

A claim with `UNRESOLVED_BLOCK` prevents final writing.

Adjudication explicitly decides:

- which facts belong in the spoken core;
- which belong only in board facts;
- which are current-practice notes;
- which are exam-specific/historical;
- which details are deliberately omitted because their cognitive burden exceeds their value.

### Stage 5 — Dedicated writer

The writer receives only:

- the approved dossier;
- the answer-archetype rules;
- the fixed final-output template.

The writer must **not** browse, research, reinterpret source conflicts, add remembered facts, or expand scope.

Its job is composition:

- convert the approved spine into natural oral prose;
- optimise ordering and retrieval;
- maintain advanced but speakable language;
- preserve necessary technical terminology;
- ensure the opening functions as the short answer and later paragraphs deepen it;
- keep board facts and examiner pivots separate where required.

### Stage 6 — Independent factual/source QA

A verifier checks the written answer against the dossier and underlying sources.

It must test:

- every consequential factual claim is authorised by the dossier;
- Oxford exam-source content has not been lost or distorted;
- current treatment/prescribing claims are current and correctly sourced;
- exam/current disagreements are represented accurately;
- Greek jurisdiction has not drifted into UK/US law or service assumptions;
- assigned board-fact anchors are present and verified;
- no unsupported detail was introduced by the writer.

QA does not rewrite for style except to identify problems.

### Stage 7 — Oral red-team QA

A separate pass tests the answer as an examination performance.

Questions:

- Does the first 20–30 seconds establish command of the topic?
- Can it be spoken without sounding like a paper?
- Is the hierarchy obvious when heard rather than read?
- Are dangerous misses or obvious examiner traps covered?
- Does unnecessary detail crowd out high-value material?
- If interrupted at several points, can the candidate still pivot intelligently?
- Would an examiner asking an adjacent version of the question expose a gap?

The red team proposes **targeted edits only**. It does not reopen the entire evidence synthesis without cause.

### Stage 8 — Final approval and freeze

The final package is frozen only when:

- dossier status = `APPROVED_FOR_WRITING` then `ANSWER_VERIFIED`;
- no unresolved claims remain;
- all assigned must-cover items can be pointed to in the answer;
- all assigned board facts can be pointed to in the board-fact block;
- all visible examiner follow-ups have answers;
- source QA and oral QA both pass.

---

## 5. Claim-level provenance rule

The dossier should distinguish **claims** from **sources**.

A source citation alone does not prove that every statement around it is supported.

Consequential claims should have stable local IDs such as:

- `C_DIAG_01`
- `C_DIFF_03`
- `C_TX_04`
- `C_MON_02`
- `C_EXAM_01`

Each claim records:

- concise proposition;
- importance;
- exam/current status;
- source references;
- adjudication state;
- destination: spoken core / extension / board fact / follow-up / exclude.

This makes hallucinated or writer-added facts detectable.

---

## 6. Source-role matrix

| Claim type | Exam-source authority | Current authority | Typical supplementary role |
|---|---|---|---|
| Diagnostic criteria/classification | Oxford Shorter for exam framing | DSM-5-TR / ICD-11 | New Oxford/Kaplan for explanation |
| Treatment sequencing | Oxford Shorter for exam framing | Current major guideline | New Oxford / major evidence |
| Psychopharmacology dose/monitoring/interactions | Oxford as exam context only | Current Maudsley/prescribing/regulatory source | Stahl for mechanism/practical differentiation |
| Mechanism/neurobiology | Oxford Shorter | Current authoritative reviews/texts when needed | New Oxford/Stahl |
| Epidemiology/prognosis | Oxford when clearly exam-specific | Current high-quality evidence when consequential | Kaplan/New Oxford |
| Psychotherapy | Oxford exam framing | Current guideline/evidence where material | specialist/manual sources selectively |
| Law/consent/forensic/service | Oxford foreign material is non-authoritative for Greece | Current official Greek sources | comparative foreign material only if explicitly labelled |

When exam and current sources conflict, **do not average them**.

---

## 7. Answer-length classes

Length is assigned in the dossier before writing.

- `COMPACT`: approximately 90–150 seconds; sharply bounded concepts/comparisons.
- `STANDARD`: approximately 150–240 seconds; most disorders and treatment questions.
- `MAJOR`: approximately 240–330 seconds; broad/high-frequency topics such as schizophrenia, delirium, lithium or ECT when needed.

These are oral targets, not hard word counts. Clarity and sufficiency override duration.

Follow-up answers should usually be 20–90 seconds depending on complexity.

---

## 8. Pilot before scale

Do **not** manufacture all 100 until the complete workflow has been tested on heterogeneous questions.

Recommended pilot:

1. **Q12 — Schizophrenia diagnosis**: diagnostic/classification + psychopathology + exam-history stress test.
2. **Q21 — Major depressive episode treatment**: current guideline vs exam-source synthesis.
3. **Q45 — Delirium**: organic/emergency reasoning and differential diagnosis.
4. **Q81 — Lithium**: dense psychopharmacology, exact facts and monitoring verification.
5. **Q90 or Q91 — CBT or transference/countertransference**: psychotherapy/conceptual writing test.

After the five pilots:

- compare consistency;
- measure answer length and oral usability;
- identify dossier fields that were unused or missing;
- decide whether the recall spine and board-fact block improve learning;
- freeze the writer specification;
- only then batch-produce the remaining answers.

---

## 9. Batch strategy after pilot

Research and local extraction may be batched by coherent domain, usually 3–8 questions at a time.

Examples:

- schizophrenia Q11–19;
- mood Q20–27;
- psychopharmacology in smaller drug-focused batches;
- neurocognitive Q45–58.

**Final writing remains question-by-question from approved dossiers.**

This preserves consistency without allowing batch synthesis to blur the centre of gravity of individual questions.

---

## 10. Stop / escalation rules

Stop final production when:

- Oxford and current authoritative sources materially conflict and no adjudication exists;
- exact psychopharmacology or legal information has not been verified;
- a local-textbook claim cannot be traced to the cited page/section;
- a source appears to be from the wrong edition;
- a supposedly Adult Psychiatry answer drifts materially into Child and Adolescent Psychiatry;
- a Greek-law question is being answered from a foreign legal framework;
- the writer introduces an unsupported claim;
- the answer becomes comprehensive at the cost of oral usability.

A qualified unresolved note is preferable to an invented resolution.
