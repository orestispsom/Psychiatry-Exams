# Greek v5 — scoring rubric

Purpose: editorial calibration for Greek-first board-review answers. This rubric is intentionally stricter than ordinary medical-content QA. A clinically correct answer can still fail if it reads like generated text, follows an editorial outline rather than clinical reasoning, hides operational information in prose, or introduces unexplained technical shorthand.

This version incorporates the founder sentence-level review of the eight-question v5 pilot and supersedes the original pilot-only interpretation of the rubric.

## Global rule

Score each question out of 100. Target for scale-up is **≥90/100**, with **no category below the equivalent of 8/10** and no automatic-fail or automatic-revision defect.

A high numerical score does **not** override the hard gates below.

## Hard gates / automatic revision

The following defects require revision before a question can be accepted:

- **Editorial-outline language leaking into the spoken answer.** Internal headings such as `setting`, `severity`, `monitoring`, `differential`, `first decision`, `next step` or similar may organise drafting, but must not become learner-facing sentences unless that wording is itself natural clinical speech.
- **Clinical sequence failure.** Decisions must arise from the information that clinically produces them. For example, severity/risk assessment leads to disposition; the answer must not announce disposition as an abstract first decision before establishing what is being assessed.
- **Question-order failure.** When the examiner asks several things explicitly — e.g. clinical picture → diagnosis → differential, or recognise → assess → manage — the model answer should normally follow that order unless there is a clear clinical reason not to.
- **Read-aloud failure.** If a sentence is unlikely to be said by a strong Greek specialist candidate, or adds only rhetorical/architectural narration rather than psychiatric information, it must be deleted or rewritten.
- Learner-facing source/writer/exam-production narration such as `για τις εξετάσεις πρέπει να...`, `στην απάντηση θα...`, `η πρώτη απόφαση είναι...` when used only to narrate structure: **automatic revision required**.
- Numerical diagnostic denominator without the counted items when the denominator is educationally central: **automatic revision required**.
- Change in dose, threshold, duration, legal article, recommendation strength or causal strength without source justification: **automatic factual fail**.

### Major deductions / caps

- Obvious AI-generated cadence or stock contrast language repeated across the answer: major deduction. If conspicuous enough that a reader would identify the prose as AI-shaped, the question cannot score above **84/100** until rewritten.
- Non-obvious acronym or instrument appearing before local expansion: deduction; repeated instances are a major defect.
- Greek that is grammatically correct but plainly calqued from English is a language defect even when medically intelligible.
- Abstract nominalisations or coined compounds should be penalised when ordinary Greek clinical phrasing would be clearer.

## 1. Human-authored Greek and absence of AI slop — 20 points

Evaluate:

- natural contemporary Greek medical prose;
- wording an experienced Greek psychiatrist would plausibly use aloud;
- established Greek psychiatric/medical terminology rather than literal English calques;
- sentence rhythm and variation;
- absence of repetitive `δεν είναι απλώς... αλλά...`, `όχι μόνο... αλλά...`, `το βασικό είναι...`, `η πρακτική απάντηση...`, `συνοπτικά...` templates;
- absence of redundant concluding restatements;
- no writer-facing, source-facing or exam-performance meta prose;
- no unnecessary English-Greek hybrid syntax;
- preference for ordinary clinical expressions over unnecessarily abstract constructions.

### Read-aloud test

For every paragraph, ask:

1. Would a strong specialist candidate actually say this to an examiner?
2. Does each sentence add clinical information, prioritisation or reasoning?
3. If the sentence were removed, would any useful psychiatric content be lost?

If the answer to 1 is no, or to 2 and 3 is no, revise it.

## 2. Model oral answer — 15 points

Evaluate whether `## Πρότυπη προφορική απάντηση`:

- directly answers the examiner's wording from the opening sentence;
- follows the natural clinical logic of the subject rather than the Writer's production outline;
- follows the explicit order of a multi-part question when appropriate;
- could genuinely be spoken by a strong specialist candidate;
- prioritises rather than encyclopaedically dumps facts;
- uses prose for reasoning and synthesis;
- delegates enumeration to bullets/tables only when retrieval is genuinely improved;
- avoids padding, rhetorical scaffolding and repeated conclusions;
- generally fits roughly 2–4 minutes unless the topic inherently requires more.

### Clinical-discourse test

The answer must distinguish **information architecture** from **clinical discourse architecture**.

An internal outline may be:

`recognition → severity → setting → medication`

but spoken clinical reasoning may need to be:

`recognise the syndrome → assess current severity and predictors of complications → treatment → decide the safe level of care from that assessment`.

Do not convert outline labels mechanically into sentences or paragraph openings.

## 3. Retrieval architecture / structure — 15 points

Evaluate:

- information is placed where it is easiest to retrieve **without distorting clinical logic**;
- structure reflects the question's actual task;
- criteria are lists/checklists rather than buried prose when counting is important;
- comparisons use tables only when they materially improve discrimination;
- emergency/treatment sequences are visibly ordered when the sequence itself is clinically real;
- headings are meaningful rather than decorative;
- the answer is neither a wall of prose nor an indiscriminate bullet list.

**Important:** visible structure is not automatically good structure. A neat sequence that a clinician would not naturally reason through should lose points.

## 4. Diagnostic / operational visibility — 10 points

Where relevant:

- explicit counted criteria are shown;
- duration, exclusion and impairment rules are visible;
- DSM-5-TR and ICD-11 are kept separate;
- named triads/tetrads/clusters immediately state their components;
- the learner never has to infer what a denominator refers to.

If the question is not primarily diagnostic, score instead on visibility of the relevant operational sequence: monitoring, emergency actions, legal procedure, treatment escalation, etc.

Operational detail should remain **subordinate to the clinical answer**. Do not let a scale, table or protocol become the organising principle of the entire viva response unless the question specifically asks for it.

## 5. Acronyms, instruments and technical terms — 8 points

- Every non-obvious acronym/instrument is expanded before or at first visual occurrence within the question, including the Recall Axis.
- Do not assume prior questions were read.
- Common terms such as DSM-5-TR, ICD-11, MRI, EEG and SSRI may remain abbreviated when unambiguous.
- Technical English may remain parenthetically when it improves recognition, but Greek should carry the sentence.
- When a short instrument has unusually high retrieval value, its components may be shown compactly; do not reproduce an entire manual unnecessarily.

## 6. Recall Axis — 8 points

`## Άξονας ανάκλησης` should:

- reconstruct the answer;
- usually contain 5–7 terse anchors;
- reflect the **final spoken clinical order**, not the Writer's backstage production plan;
- avoid mini-paragraphs;
- avoid unexplained acronyms;
- emphasise discriminators, sequence and high-value recall rather than generic headings.

## 7. Basic Exam Points — 8 points

`## Βασικά σημεία για τις εξετάσεις` should:

- contain genuinely memorizable board facts;
- avoid merely repeating the model answer;
- foreground thresholds, timelines, discriminators, monitoring rules and clinically important exceptions;
- usually contain about 4–6 strong points rather than filler.

## 8. Traps — 8 points

`## Συχνές παγίδες / παγίδες εξεταστή` should:

- target plausible errors made by competent candidates;
- discriminate current vs historical rules where useful;
- include common DSM/ICD, diagnostic, treatment, legal or monitoring confusions;
- include clinically meaningful sequence errors where relevant;
- avoid trivial negative statements.

## 9. Examiner follow-ups / exam-vs-current distinction — 4 points

- Follow-ups should test a natural viva probe and add depth rather than duplicate the answer.
- Exam-vs-current sections should appear only when there is a real discrepancy or historically important distinction.
- Do not force either section into every question.
- A separate high-yield subtopic may be used when it prevents the main answer becoming overloaded, as with Wernicke encephalopathy within alcohol-withdrawal teaching.

## 10. Source fidelity and clinical precision — 4 points

- Preserve verified meaning and uncertainty.
- Do not strengthen `may/consider` into `must/indicated`.
- Do not convert association into causation.
- Preserve doses, durations, thresholds, legal citations and regulatory boundaries.
- Editorial naturalisation must never silently alter a consequential clinical claim.

## Mandatory final QA before acceptance

Before a question is accepted, the reviewer must perform all of the following:

1. **Question-match check:** Does the answer respond in the same conceptual order as the examiner's actual question?
2. **Clinical-causality check:** Does each decision follow from the assessment that justifies it?
3. **Read-aloud check:** Would the wording sound natural from a Greek psychiatrist in an oral exam?
4. **Sentence-necessity check:** Does every sentence add useful psychiatric content or reasoning?
5. **Terminology check:** Are the Greek terms actually used clinically, rather than merely possible translations?
6. **Operational check:** Are important criteria/scales/doses visible without taking over the answer?
7. **Source-fidelity check:** Are consequential numbers and recommendations still supported by the approved source layer?

A question that fails checks 1–4 cannot receive an acceptance score even if its factual content is correct.

## Scale-up acceptance gate

Before a batch is accepted:

1. Every question must be graded using this rubric.
2. Mean score must be **≥90/100**.
3. No question may be below **86/100**.
4. No automatic factual fail may remain.
5. No conspicuous AI-slop cap may remain.
6. No clinical-sequence or read-aloud hard-gate failure may remain.
7. Founder-approved pilot answers are the stylistic calibration set for scale-up.
8. Independent scoring is provisional until founder review has confirmed the calibration standard; independent adjudication must not declare scale-up final solely from numerical scores.
