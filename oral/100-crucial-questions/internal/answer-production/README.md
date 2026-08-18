# Model-Answer Production System

Status: governing internal workflow for **The 100 Crucial Questions in Psychiatry**.

## Governing rule

Routine production now follows the lean workflow in `lean-workflow.md`.

The project still separates source extraction, verification and writing, but it does **not** require a multi-agent literature review and multi-textbook triangulation for every question.

> **One strong base source + targeted verification is the default. Escalate only when uncertainty, safety, law, treatment volatility or source conflict justifies it.**

The prescribed **Shorter Oxford Textbook of Psychiatry, 7th edition / 2017 exam edition** is the default base source for the private Greek Adult Psychiatry board-preparation master.

## Routine production path

### 1. Oxford base extraction

Retrieve only the relevant section/pages and produce a compact paraphrased source packet containing:
- natural answer structure;
- core clinical/exam points;
- classic distinctions;
- exact facts that need checking;
- page provenance.

Do not routinely open supplementary textbooks.

### 2. Targeted current verification

Verify only update-sensitive or exact claims needed for accuracy:
- DSM-5-TR / ICD-11 for diagnosis/classification;
- current guideline for treatment where Oxford may be outdated;
- current prescribing/regulatory source for dose, monitoring, interactions, pregnancy, toxicity or licensing;
- current official Greek source for law/forensic/confidentiality/service rules;
- one strong current source for any consequential unstable fact.

A stable descriptive question may need only 2–5 current checks.

### 3. Compact answer brief

Use `answer-brief-schema.yml` to combine the Oxford base and verification delta.

The answer brief records:
- recall spine;
- must-cover content;
- verified updates/corrections;
- board facts;
- genuine exam-vs-current differences;
- follow-ups;
- deliberate exclusions;
- lightweight commercial provenance flags.

Use the older full `dossier-schema.yml` only when a question has substantial conflict or unusually high-risk/complex evidence.

### 4. Dedicated writer

The writer receives the approved answer brief and creates the learner-facing package in original wording.

The writer does not independently research, invent exact facts or resolve source conflicts.

### 5. Coordinator QA

One integrated coordinator pass checks:
- fidelity to the brief;
- correctness of verified/update-sensitive claims;
- oral usability and hierarchy;
- missing board facts/follow-ups;
- exam/current distinction;
- Greek applicability where relevant.

Separate source-QA and oral-red-team agents are optional escalation tools, not routine requirements.

## Final learner-facing package

Each answer may contain:

1. **Recall spine** — 4–7 retrieval concepts.
2. **Model oral answer** — fractal spoken answer: strong opening, competent ~2-minute core, deeper material if allowed to continue.
3. **Must-know board facts** — exact criteria/durations/classic facts/drug or monitoring anchors worth separate recall.
4. **Examiner follow-ups** — only genuine approved pivots.
5. **Exam answer vs current practice** — only when a meaningful discrepancy exists.

## Source escalation

Open a supplementary local textbook only when:
- Oxford cannot cover a required item;
- Oxford is ambiguous;
- a current-source conflict needs explanation;
- the Greek oral bank signals a classic point Oxford does not adequately cover;
- another text is clearly the appropriate specialist authority for the question.

Examples:
- Maudsley for psychopharmacology practicalities;
- Stahl for selected mechanisms;
- New Oxford/Kaplan only when they materially resolve a gap.

Source count is not a quality metric.

## Efficiency and batching

Questions sharing an Oxford chapter should use one chapter map rather than repeated fresh retrieval.

Examples:
- Q11–19 schizophrenia/psychosis;
- Q20–27 mood/perinatal;
- Q45–58 neurocognitive/neuropsychiatry.

Current research should likewise reuse already inspected domain authorities and perform only question-specific delta checks.

## Enhanced verification triggers

Use the more intensive/full dossier workflow only for:
- psychopharmacology dose/monitoring/toxicity/interactions;
- pregnancy/reproductive safety;
- emergency treatment;
- current treatment algorithms/resistance when materially changed since 2017;
- Greek law/forensic/confidentiality;
- rapidly changing interventions;
- substantial Oxford-vs-current disagreement;
- contested evidence central to the answer.

## Accuracy rule

Efficiency means eliminating duplication, not weakening authority.

Never save time by:
- using generic websites instead of DSM/ICD/guidelines/regulators where those authorities are required;
- copying old `Psych` answers as factual authority;
- guessing an exact criterion, dose, level, legal rule or monitoring schedule;
- allowing the writer to fill unresolved gaps from memory.

## Commercialization

The private study master remains optimized for exam preparation and must not be slowed by commercial clearance.

Retain source/page provenance and obvious source-expression flags during production. The eventual commercial manuscript will be a separate, originally written derivative subjected to a dedicated copyright/licensing/provenance pass.

## Legacy workflow files

The detailed `dossier-schema.yml`, multi-agent prompts and previous extensive workflow remain available for escalation and auditing. They are **not the default checklist for every question**.

Current default: `lean-workflow.md` + `answer-brief-schema.yml`.
