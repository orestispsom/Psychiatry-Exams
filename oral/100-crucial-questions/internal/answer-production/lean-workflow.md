# Lean Model-Answer Production Workflow

Status: **CURRENT DEFAULT** as of 2026-08-18.

This supersedes the earlier multi-agent, multi-textbook workflow as the routine production method. The earlier files remain useful as reference/escalation procedures, but they are not required for every question.

## Core idea

A high-quality answer usually does **not** need independent reconstruction from five books plus a literature review.

For the private Greek Adult Psychiatry board-preparation master:

> **Start from one strong exam source, then verify only the claims most likely to be wrong, outdated, unsafe or exam-sensitive.**

The prescribed **Shorter Oxford Textbook of Psychiatry, 7th edition / 2017 exam edition** is the default content backbone unless a question clearly requires a more appropriate primary authority.

## The four-step routine

### Step 1 — Base source extraction

Default source: **Oxford Shorter 2017**.

Extract only what is needed for the question:
- the natural answer structure;
- core clinical facts;
- classic examination points;
- any exact facts or wording that appear especially exam-relevant;
- source pages/sections.

Target output: a compact source packet, usually about 500–1200 words.

Do **not** routinely open New Oxford, Kaplan, Comprehensive, Maudsley or Stahl at this stage.

### Step 2 — Targeted verification delta

Perform only the verification needed to put the Oxford-based answer in good standing.

Typical checks:

- **diagnosis/classification:** DSM-5-TR and/or ICD-11 for exact current criteria or changed classification;
- **treatment:** current major guideline only where Oxford 2017 may be outdated;
- **psychopharmacology:** current prescribing/regulatory source for dose, monitoring, interactions, pregnancy, toxicity or licensing;
- **law/forensic/confidentiality:** current official Greek source;
- **unstable factual claim:** one strong current source if the number/fact matters;
- **historical exam fact:** retain as exam-specific if useful, but label it.

For a stable descriptive question, this may be only 2–5 checks.

Do not perform a broad literature review unless the question genuinely needs one.

### Step 3 — Compact answer brief

The coordinator combines the base-source packet and verification delta into one short `answer brief` using `answer-brief-schema.yml`.

The brief decides:
- answer spine;
- must-cover material;
- verified corrections/updates to Oxford;
- exact board facts;
- any genuine exam-vs-current difference;
- exclusions;
- provenance/copyright flags where needed.

The brief should normally be 1–3 pages, not a claim-level evidence database.

Use the full `dossier-schema.yml` only for questions with substantial conflict, high-risk prescribing/legal content, or unusually complex evidence.

### Step 4 — Write + final check

A dedicated writer receives the approved answer brief and writes the learner-facing package.

Then the coordinator performs one integrated final check for:
- fidelity to the brief;
- factual accuracy of the verified/update-sensitive claims;
- oral usability;
- missing board facts/follow-ups;
- exam/current separation;
- Greek applicability where relevant.

A separate Source-QA agent and Oral-Red-Team agent are **optional escalation tools**, not mandatory stages for every question.

## Source hierarchy by question type

### Stable disorder / psychopathology / descriptive question

1. Oxford Shorter 2017 — base
2. DSM-5-TR / ICD-11 — targeted current classification check
3. One additional authoritative source only if a material gap remains

### Treatment question

1. Oxford Shorter 2017 — exam framing/base
2. Current major guideline — treatment delta
3. Prescribing/regulatory source only for exact drug safety details that enter the answer

### Drug question

1. Oxford Shorter 2017 — exam framing
2. Current Maudsley/prescribing/regulatory source — authoritative practical details
3. Stahl only if mechanism/exam differentiation genuinely adds value

### Law / ethics / forensic / service question

1. Oxford only for general psychiatric framing where useful
2. Current official Greek law/authority — actual answer authority

### Foundational stable question

1. One authoritative textbook/source may be sufficient
2. Verify only disputed or exam-specific facts

## Supplementary-textbook escalation rule

Open another local textbook **only** when at least one of these is true:

- Oxford is genuinely insufficient for a must-cover item;
- Oxford is ambiguous;
- a current-source conflict needs explanation;
- the Greek oral bank signals a classic point Oxford does not adequately cover;
- the question is a specialist drug/therapy topic for which another local source is clearly superior.

Do not open another textbook merely to confirm material already adequately supported.

## Research-GPT rule

The Research GPT is no longer asked to independently rebuild every question from scratch.

Default request:

> Given the Oxford-derived base packet, perform only the current-authoritative verification delta needed for this question. Verify the listed update-sensitive claims and identify any important current correction or omission. Do not broaden the topic.

Deep research is reserved for:
- genuinely contested questions;
- rapidly changing treatment;
- high-risk psychopharmacology;
- major guideline changes;
- law/regulation;
- places where Oxford and current authority materially conflict.

## Claude/local-agent rule

Claude should be used primarily as a **targeted local source retriever**, not as a broad textbook synthesis agent.

Default local task:
- locate the Oxford section;
- read the relevant pages;
- produce a compact paraphrased extraction with page references;
- stop.

If exact DSM/local-source verification is required, add only that second source.

Do not make Claude read the entire project architecture. Each task should receive a compact work order containing only:
- question;
- 5–10 must-cover bullets;
- board facts needing local verification;
- source(s) allowed;
- output path/format.

### Batch efficiency

When several questions share one Oxford chapter, extract the chapter **once** and create a chapter map. Then produce small question-specific extracts from that map.

For example, Q11–Q19 should not cause nine fresh searches of the same schizophrenia chapter.

## QA tiers

### Routine QA
Performed by coordinator in one pass.

### Enhanced QA
Use a separate verifier only for:
- current prescribing/monitoring/toxicity;
- pregnancy;
- emergency treatment;
- Greek law/forensic questions;
- major exam-current conflict;
- answers that fail the first integrated QA pass.

## Commercial provenance

Commercialization does not change the study workflow.

Retain:
- source/page provenance;
- flags for close paraphrase/direct quotation/proprietary text.

The later commercial manuscript will be rewritten and cleared separately.

## Practical production target

Routine question:

`Oxford extract → 2–5 targeted current checks → compact answer brief → writer → coordinator QA`

The expected intellectual work should be measured in **minutes per question after source reuse**, not a 15–30 minute independent research project for each of 100 questions.

## Escalation principle

If the lean process reveals uncertainty, escalate that claim or question. Do not pre-emptively apply the maximal process to everything.

**Accuracy is maintained by targeted verification, not by source-count.**
