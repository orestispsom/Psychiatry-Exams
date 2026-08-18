# Model-Answer Production System

Status: governing workflow for **The 100 Crucial Questions in Psychiatry**.

## Objective

Produce 100 high-yield Greek **Adult Psychiatry** board-preparation packages that are accurate, memorable and genuinely usable in an oral examination.

The unit of production is **not a literature review**. It is a short oral answer package.

Default learner-facing target:

- model oral answer: roughly **1–2 pages**, usually about **350–700 words**;
- spoken duration: usually **2–4 minutes**, up to about 5 minutes for major topics;
- compact recall spine;
- compact board facts;
- only genuine examiner follow-ups;
- brief current-update/exam-current note only when needed.

## Governing principle

> **Do only enough research to make the short final answer accurate, current where necessary, and safe for the exam.**

More source retrieval is not automatically better.

The detailed routine is in `lean-workflow.md` and supersedes the older maximal multi-agent workflow as the default.

## Default pipeline

### 1. Tiny question brief

Define:

- what is being asked;
- 4–8 must-cover items;
- board facts/follow-ups;
- likely update-sensitive points.

### 2. Oxford exam-base extraction

The prescribed **Shorter Oxford Textbook of Psychiatry, 7th ed. / 2017 exam edition** is usually the starting study source.

Extract only the relevant pages and answer skeleton. Do not summarise whole chapters when the final answer is 1–2 pages.

### 3. Targeted current verification

Check only claims that matter and may have changed.

Typical authorities:

- **WHO ICD-11** for current international diagnostic/classification framing when adequate;
- **DSM-5-TR selectively**, when a DSM-specific distinction is genuinely useful for private exam study or a DSM/ICD comparison matters;
- current major guideline for treatment;
- current prescribing/regulatory authority for doses, monitoring, interactions, pregnancy, toxicity and licensing;
- current official Greek authority for law, ethics, involuntary care, confidentiality, forensic rules and system-specific claims;
- one strong current review/paper for a consequential uncertain scientific point.

DSM is **not** the universal organising baseline and its criterion text should not be reproduced in final learner-facing prose.

### 4. Compact answer brief

Use `answer-brief-schema.yml`.

Combine the exam base + only the current corrections/additions needed for the final answer.

The brief should contain only what the writer needs.

### 5. Dedicated writer

Writer receives only the approved brief.

Writer produces an original, spoken, hierarchical answer. The writer does not browse or add new facts.

### 6. One integrated coordinator QA

Check:

- oral length and usability;
- must-cover completeness;
- current/high-risk facts;
- board facts/follow-ups;
- exam/current distinction;
- Greek applicability;
- unsupported additions;
- unnecessary detail.

Separate QA agents are escalation tools, not mandatory for every question.

## Source-count rule

For most stable questions, **Oxford + a few current checks is enough**.

A second local textbook is opened only when it will plausibly change what the candidate should say.

For treatment/drug/legal questions, a more appropriate current authority may carry more weight than Oxford for the relevant claim.

## DSM / ICD / commercialization rule

The personal study master may consult all appropriate sources, including DSM-5-TR.

However:

- do not design every answer around DSM criteria;
- prefer syndrome-based original clinical explanation;
- use WHO ICD-11 and other publicly referenceable authorities where they adequately support current classification;
- use DSM selectively for exam-relevant distinctions/cross-checks;
- do not reproduce DSM criterion wording in the commercial derivative;
- retain internal provenance and create the commercial manuscript later as a separate original derivative.

See `commercialization-policy.md`.

## Escalation

Use the older full dossier / multi-source workflow only when:

- sources materially conflict;
- a high-risk drug/legal point remains unresolved;
- the question itself concerns contested evidence;
- routine QA finds a substantive problem.

## Scaling

When several questions share a source chapter/domain:

- map the source once;
- reuse the verified source map;
- retrieve only the question-specific delta;
- still write each answer separately.

The project should scale through **source reuse and selective verification**, not through 100 independent deep-research jobs.

## Final stop rule

Stop retrieval when further reading is unlikely to change the 1–2 page oral answer, its board-fact block, or a genuine examiner follow-up.

That is the operational definition of “enough research” for this project.
