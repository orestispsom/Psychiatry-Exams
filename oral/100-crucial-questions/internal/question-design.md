# 100 Crucial Questions — Internal Question Design Doctrine

Status: living internal standard. This file governs future attempts of the 100-question guide. It is not learner-facing content.

## 1. Four distinct layers

The project has four separate layers:

1. **Canonical psychiatry coverage** — `core-coverage.yml`; question-independent knowledge that a well-prepared senior psychiatry resident should possess.
2. **Main question** — the visible oral-board question used to sample part of that coverage.
3. **Examiner follow-up** — an optional visible probe that genuinely changes or deepens the task.
4. **Internal answer-coverage checklist** — hidden authoring metadata ensuring that the eventual model answer to a particular question is complete.

Do not use follow-ups as a substitute for an answer outline, and do not reshape the canonical coverage map merely to fit a particular question attempt.

## 2. Main-question rule

A main question should usually test exactly one of the following:

- one clinical entity;
- one clinical presentation;
- one drug or coherent drug class;
- one intervention;
- one emergency or high-risk syndrome;
- one sharply defined comparison or discrimination problem;
- one bounded foundational concept with clear psychiatric relevance.

The question should have one centre of gravity and support a coherent approximately 2–5 minute senior-resident oral answer.

### Preferred forms

- `How do you diagnose and manage obsessive-compulsive disorder?`
- `A young adult presents with first-episode psychosis. How do you assess and manage them?`
- `How do you use lithium safely and effectively in psychiatric practice?`
- `How do delirium and dementia differ clinically?`

### Avoid

- vague headings such as `What should a psychiatrist know about X?` when X contains several independent topics;
- questions that are merely textbook chapter titles;
- headlines that enumerate diagnosis + epidemiology + mechanisms + treatment + prognosis unless those elements form one genuinely coherent clinical task;
- omnibus questions containing several independent disorders simply to preserve coverage.

## 3. Follow-up rule

**Zero follow-ups is the default.**

A follow-up is justified only when a candidate could answer the parent question very well and the examiner could still reasonably use the follow-up to test something meaningfully new.

Permitted follow-up functions:

1. **Discrimination** — distinguish the parent entity from a difficult mimic or adjacent diagnosis.
2. **Complication / deterioration** — the clinical state changes or a high-stakes complication appears.
3. **Treatment failure / next step** — an adequate first-line approach fails.
4. **Special circumstance** — pregnancy, older age, renal/hepatic disease, comorbidity, etc. materially changes management.
5. **Mechanistic / depth probe** — asks why a clinically important effect occurs or tests a known examiner-depth area.
6. **Examiner trap / exception** — a dangerous miss, contradiction, or finding that should force diagnostic reconsideration.

### Follow-up deletion test

Ask:

> If the candidate answered the main question perfectly, would this follow-up already have been answered?

If **yes**, the follow-up should normally be deleted and its content moved to the internal answer-coverage checklist.

## 4. Follow-up quantity

Target distribution for the final guide:

- approximately 50–60 main questions with no follow-up;
- approximately 25–30 with one follow-up;
- approximately 10–15 with two follow-ups;
- only a small number with three follow-ups.

There is no quota. Clinical logic overrides these targets.

## 5. Internal answer-coverage checklist

The internal checklist records what an excellent model answer to a specific visible question must cover. It is **not** the canonical psychiatry coverage bank and is **not** visible as a/b/c questions unless a specific item qualifies as a genuine examiner follow-up.

Typical checklist dimensions, used only when relevant:

- definition / diagnostic framework;
- characteristic psychopathology;
- differential diagnosis;
- red flags and dangerous alternatives;
- medical / neurological / substance exclusion;
- investigations;
- acute risk;
- indication for admission;
- first-line treatment;
- treatment sequencing;
- monitoring;
- adverse effects;
- treatment resistance / next steps;
- psychosocial treatment;
- prognosis / relapse prevention;
- special populations;
- clinically important mechanisms;
- exam-specific historical or conceptual points.

Do not mechanically apply every dimension to every topic.

## 6. Scenario rule

A clinical vignette should create a decision or diagnostic problem. Do not add a vignette merely to decorate a descriptive question.

Strong:

`A patient treated for schizophrenia remains psychotic despite two apparently adequate antipsychotic trials. How do you determine whether this is true treatment resistance?`

Weak:

`A patient with schizophrenia presents. Describe schizophrenia.`

## 7. Canonical coverage without question inflation

`core-coverage.yml` is the authority for what psychiatry knowledge the project must preserve. It is intentionally independent of the 100 visible questions.

A canonical coverage unit can ultimately be represented in the guide as:

- a **MAIN** question;
- a genuine **FOLLOW-UP**;
- required **ANSWER COVERAGE** within another question;
- or, for lower-priority material, no visible prompt at all.

The canonical bank therefore does not label topics as permanent MAIN/FOLLOW_UP items. Those are attempt-specific decisions.

A topic is not automatically promoted to a main question merely because a textbook gives it a heading, and a topic is not removed from canonical coverage merely because the current 100-question attempt has no dedicated prompt for it.

## 8. Source and exam discipline

- The current `Psych` repository is the canonical live source for the Greek board-exam app and oral-question bank.
- Actual / recalled Greek oral-exam material should strongly influence coverage and examiner-probe design.
- Core textbooks and curricula are coverage checks, not automatic generators of main questions.
- `source-register.md` records what sources have actually been audited and the scope in which they were used.
- Current treatment, prescribing, regulation and law must be re-verified when answers are eventually written.
- Exam-specific historical material must be distinguished from current clinical practice when they differ.

## 9. Stable coverage IDs; disposable question numbers

Attempt question numbers (`004 Q19`, `005 Q22`, etc.) are temporary.

Stable coverage IDs live only in `core-coverage.yml`.

Attempt-specific relationships belong in:

`internal/attempt-maps/<attempt>.yml`

These maps may say that a question samples one or more canonical coverage IDs, or that a visible follow-up is redundant. They must not redefine the underlying psychiatry knowledge map.

## 10. Growth discipline for the canonical coverage bank

The canonical bank should become richer over time, but not progressively encyclopaedic.

Add or expand a coverage unit when new source review shows that omission would create a meaningful senior-resident knowledge gap, especially in:

- diagnostic discrimination;
- dangerous alternative diagnoses;
- treatment sequencing;
- emergencies and red flags;
- monitoring and major adverse effects;
- treatment resistance;
- special populations;
- risk, capacity and law;
- recurrent board-exam material.

Do **not** expand the bank merely to capture:

- every rare syndrome;
- every DSM/ICD specifier;
- every possible adverse effect;
- exact doses or numerical thresholds better handled during verified answer writing;
- historical or mechanistic trivia with little clinical or examination value.

When in doubt, prefer a compact stable coverage unit with a few meaningful essentials over many tiny nodes.

## 11. Board-sufficiency criterion

The final 100-question set is intended to function as a **high-yield sufficiency set for Adult Psychiatry specialist-board preparation in Greece**.

The design target is stronger than simple curriculum representation:

> If a candidate genuinely understood, could explain, discriminate, and clinically apply the material required by all 100 questions and their internal answer-coverage specifications, that knowledge should probably be sufficient to pass a general Adult Psychiatry specialist board examination, while recognising that no finite question bank can guarantee examination outcome.

This requires the set collectively to provide:

- broad coverage of the major adult psychiatric disorders and presentations;
- adequate depth in high-frequency and high-risk topics rather than superficial mention;
- diagnostic criteria and clinically meaningful differentials;
- emergency psychiatry, suicide, violence, catatonia, delirium and other dangerous presentations;
- treatment sequencing, treatment resistance and next-step reasoning;
- psychopharmacology sufficient for safe specialist practice, including monitoring, interactions, major adverse effects and toxic syndromes;
- psychotherapy principles expected of a general adult psychiatrist;
- old-age, liaison, neuropsychiatric, substance-use, sleep, eating, personality and adult neurodevelopmental psychiatry at appropriate board depth;
- core psychopathology, neuroscience and evidence-appraisal knowledge that commonly supports oral examination questions;
- Greek law, ethics, forensic psychiatry and service-system knowledge where jurisdiction matters;
- enough cross-topic integration that the candidate can handle an unfamiliar vignette by reasoning from the mastered material rather than relying only on recognition of rehearsed wording.

### Sufficiency audit question

Before locking an attempt, ask:

> If the examiner deliberately avoided asking these exact 100 prompts but tested the same adult-psychiatry curriculum through adjacent cases, comparisons and follow-up questions, would mastery of our 100 answers still allow a strong candidate to reason their way to a passing response?

If **no**, the bank is not yet sufficient even if every major textbook chapter has nominal representation.

The project therefore optimises for **transferable board competence**, not memorisation of 100 scripts.

## 12. Final quality test for every visible prompt

Before accepting a main question or follow-up, ask:

- Is the target clear without reading hidden notes?
- Does it test one coherent thing?
- Could an examiner realistically ask it in this form?
- Does it discriminate a competent candidate from an excellent senior resident?
- Is it duplicating what another question necessarily covers?
- Is a supposed follow-up actually just part of the complete parent answer?
- Would removing it create a meaningful knowledge gap in the canonical coverage map?
- Does this prompt materially contribute to the board-sufficiency target, or is the slot better spent elsewhere?

If the prompt fails these tests, rewrite, demote, merge or delete it.
