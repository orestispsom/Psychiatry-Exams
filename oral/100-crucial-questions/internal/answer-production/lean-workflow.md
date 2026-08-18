# Lean Model-Answer Production Workflow

Status: **CURRENT DEFAULT** as of 2026-08-18.

This is the governing routine for producing the 100 model answers. The project is building an oral-exam study resource, not 100 literature reviews.

## Governing constraint

The learner-facing **model oral answer should normally fit about 1–2 pages** and sound like something a strong senior Adult Psychiatry resident could actually say in a viva.

Typical spoken target:

- most questions: roughly 2–4 minutes;
- major questions: up to about 5 minutes when genuinely needed;
- follow-ups: usually 20–60 seconds.

The exact word count is secondary, but the model answer should usually remain roughly **350–700 words**, with exceptional major topics allowed somewhat more if oral usability is preserved.

The rest of the package — recall spine, board facts, examiner follow-ups, traps/current-update note — is compact and separate.

**Research depth must be proportional to this output.**

If a research detail is unlikely to enter the oral answer, board-fact block, examiner follow-up, or a clinically important current-update note, it normally does not deserve dedicated retrieval.

---

## Core source philosophy

### 1. Oxford Shorter 2017 is the exam-study backbone

For most questions, start with the prescribed **Shorter Oxford Textbook of Psychiatry, 7th edition / 2017 exam edition**.

Use it to establish:

- the natural oral-answer structure;
- the core clinical material;
- classic exam distinctions;
- the level of depth expected.

The goal is a compact extraction, not a chapter summary.

### 2. Current sources are a correction/verification layer

After the base is known, check only what is likely to have changed, be safety-critical, legally sensitive, or worth correcting.

Current verification is **not a second full reconstruction of the topic**.

### 3. DSM-5-TR is not the universal baseline

DSM-5-TR may be used for private study and targeted diagnostic verification when its distinctions matter, but it is **not the default organising source for every answer** and should not drive the structure of the commercial derivative.

For diagnosis/classification:

- use Oxford for exam framing;
- use **ICD-11 / WHO material preferentially as the current openly usable international classification reference where it adequately answers the question**;
- use DSM-5-TR selectively when a DSM-specific distinction is exam-relevant, clinically important, or needed to explain a DSM/ICD difference;
- avoid reproducing DSM criterion wording in learner-facing material.

The final answer should normally describe the clinical syndrome and diagnostic logic in original language rather than recite a proprietary criterion set.

### 4. One good source is often enough for stable material

Do not triangulate stable facts across several textbooks merely to increase confidence cosmetically.

Open another textbook only when there is a real unanswered question.

---

## The routine five-step production loop

### Step 0 — Tiny question brief

Before retrieval, define only:

- what the examiner is asking;
- 4–8 things the answer must cover;
- assigned board facts/follow-ups;
- what is plausibly update-sensitive.

Target: **100–250 words**.

No research essay and no final prose.

### Step 1 — Oxford base extraction

Local agent retrieves the directly relevant Oxford section/pages and returns:

1. answer skeleton;
2. core points;
3. classic exam facts;
4. any obviously dated or uncertain point;
5. exact pages/sections.

Target: **300–700 words per question**, often less after chapter reuse.

Default: **Oxford only.**

When several questions share a chapter, map the chapter once and reuse it rather than repeating extraction.

### Step 2 — Targeted current verification

Research GPT receives the question brief + Oxford extract and checks only the vulnerable points.

Typical routine question: **2–6 checks**.

Examples:

- changed classification → WHO ICD-11; DSM only if a material DSM distinction matters;
- treatment → one current major guideline;
- drug dose/monitoring/interactions/pregnancy → current prescribing/regulatory authority;
- Greek law/forensic/confidentiality → current official Greek source;
- a consequential epidemiological/mechanistic claim → one strong current source if necessary.

Output should be a **verification memo**, not a research packet:

- `KEEP` — Oxford/base is still suitable;
- `UPDATE` — replace/modify this point;
- `ADD` — one important current omission;
- `EXAM_CURRENT_SPLIT` — preserve an exam-specific distinction separately;
- `UNRESOLVED` — rare, requires escalation.

Target: **250–700 words**, preferably under 500 for routine questions.

Do not browse broadly once the vulnerable claims are resolved.

### Step 3 — Compact answer brief

Coordinator combines Oxford + verification delta into `answer-brief-schema.yml`.

The brief contains only what the writer needs:

- recall spine;
- 5–10 must-cover points;
- verified updates/corrections;
- board facts;
- follow-ups;
- deliberate exclusions;
- source/provenance notes.

Target: **roughly 500–1000 words total**, often less.

The full claim-level dossier is an **escalation format only** for genuinely complex/high-risk disputes.

### Step 4 — Dedicated writer

Writer receives **only the approved answer brief**.

Produces:

1. recall spine;
2. model oral answer;
3. must-know board facts;
4. approved examiner follow-ups;
5. a very short exam-vs-current note only if genuinely necessary.

The model answer must sound spoken, hierarchical and memorable. It is not required to demonstrate all research performed.

### Step 5 — One integrated QA pass

Coordinator checks:

- Does the answer actually answer the question?
- Is it orally plausible in 2–5 minutes?
- Are all must-cover items represented?
- Are exact/current/high-risk claims verified?
- Did the writer add unsupported facts?
- Is any exam/current discrepancy mishandled?
- Is Greek jurisdiction correct where relevant?
- Is anything included that does not earn its cognitive burden?

Separate source-QA or oral-red-team agents are used only when this pass finds a reason to escalate.

---

## Source selection by question type

### Descriptive disorder / psychopathology

Default:

1. Oxford Shorter 2017
2. 0–3 current checks, typically ICD-11/WHO or another authoritative current source
3. DSM only if a DSM-specific distinction materially matters

No routine second textbook.

### Treatment question

Default:

1. Oxford for exam framing
2. one current major guideline for the treatment delta
3. prescribing source only for exact drug details that will actually enter the answer

### Drug question

Default:

1. Oxford for exam framing if useful
2. one current practical prescribing authority as the main current source
3. regulator/product information for a specific safety/licensing issue if needed

Stahl/Maudsley/other texts are not automatically stacked together.

### Law / ethics / forensic

Current official Greek authority is primary for the actual rule. Oxford is optional background only.

### Stable foundational / psychotherapy concept

One authoritative source may be enough. Verify only disputed or source-sensitive claims.

---

## Supplementary textbook rule

**Do not routinely consult New Oxford, Kaplan, Comprehensive, Maudsley and Stahl after Oxford.**

A second local book is opened only if:

- Oxford does not answer a must-cover point;
- a specific current/exam conflict needs interpretation;
- the question is intrinsically better served by another specialist source;
- a known Greek oral-exam point is absent or unclear.

If the second source resolves the issue, stop.

---

## Research intensity

### Routine

Stable/descriptive material. Oxford + a few targeted checks.

### Enhanced

Treatment, psychopharmacology, emergencies, pregnancy, law, regulatory issues, genuinely changed classification.

Even here, research is claim-targeted rather than a mini-systematic review.

### Exceptional deep dive

Only when:

- authoritative sources materially disagree;
- a safety-critical point is unclear;
- the evidence itself is the subject of the question;
- the coordinator explicitly requests it.

The Q12 pilot-level 15+ minute independent literature review is **not** the routine template.

---

## Commercial-readiness principle

The study master remains exam-first, but the research architecture should make later commercialization easy.

Therefore:

- base the final prose on **original clinical synthesis**, not reproduction of Oxford or DSM structure/text;
- retain source/page provenance internally;
- prefer publicly referenceable/current sources such as WHO ICD-11, guidelines, official regulators and papers where they adequately support current claims;
- use DSM selectively for diagnostic cross-checking, not as the sole conceptual backbone;
- do not reproduce DSM criteria verbatim;
- commercial clearance remains a later separate pass and does not slow study production.

---

## Hard stop rule

Stop researching once all four are true:

1. the 4–8 must-cover items are adequately supported;
2. the few update-sensitive claims have been checked;
3. board facts have a verification route;
4. further retrieval is unlikely to change a 1–2 page oral answer.

This fourth rule is decisive.

> **If another source is unlikely to change what the candidate should actually say, do not open it.**

Accuracy comes from using the right source for the right claim, not from maximizing source count.