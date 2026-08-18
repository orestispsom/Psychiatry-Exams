# 100 Crucial Questions — Internal Question Design Doctrine

Status: living internal standard. This file governs future attempts of the 100-question guide. It is not learner-facing content.

## 1. Three distinct layers

Every topic must be handled through three separate layers:

1. **Main question** — the visible oral-board question.
2. **Examiner follow-up** — an optional visible probe that genuinely changes or deepens the task.
3. **Internal answer-coverage checklist** — hidden authoring metadata ensuring that the eventual model answer is complete.

Do not use follow-ups as a substitute for an answer outline.

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

The internal checklist records what an excellent model answer must cover. It is **not** visible as a/b/c questions unless a specific item qualifies as a genuine examiner follow-up.

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

## 7. Coverage without question inflation

A topic can be covered in one of four ways:

- **MAIN** — deserves one of the 100 numbered questions.
- **FOLLOW_UP** — important examiner probe linked to a main question.
- **ANSWER_COVERAGE** — must appear in the eventual model answer but does not deserve a visible prompt.
- **DEFERRED** — valid psychiatry knowledge but below the threshold for this guide.

A topic is not automatically promoted to MAIN merely because a textbook gives it a heading.

## 8. Source and exam discipline

- The current `Psych` repository is the canonical live source for the Greek board-exam app and oral-question bank.
- Actual / recalled Greek oral-exam material should strongly influence coverage and examiner-probe design.
- Core textbooks and curricula are coverage checks, not automatic generators of main questions.
- Current treatment, prescribing, regulation and law must be re-verified when answers are eventually written.
- Exam-specific historical material must be distinguished from current clinical practice when they differ.

## 9. Numbering is disposable; topic identity is stable

Attempt question numbers (`004 Q19`, `005 Q22`, etc.) are temporary.

The internal coverage ledger uses stable topic IDs so a topic can move between MAIN, FOLLOW_UP and ANSWER_COVERAGE without losing provenance or review history.

## 10. Final quality test for every visible prompt

Before accepting a main question or follow-up, ask:

- Is the target clear without reading hidden notes?
- Does it test one coherent thing?
- Could an examiner realistically ask it in this form?
- Does it discriminate a competent candidate from an excellent senior resident?
- Is it duplicating what another question necessarily covers?
- Is a supposed follow-up actually just part of the complete parent answer?
- Would removing it create a meaningful knowledge gap?

If the prompt fails these tests, rewrite, demote, merge or delete it.
