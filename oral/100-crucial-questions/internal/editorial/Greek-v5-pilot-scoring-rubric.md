# Greek v5 pilot — scoring rubric

Purpose: final editorial calibration for the Greek-first rewrite pilot. This rubric is intentionally stricter than ordinary medical-content QA. A clinically correct answer can still score poorly if it reads like generated text, hides operational criteria in prose, or introduces unexplained technical shorthand.

## Global rule

Score each pilot question out of 100, then convert to /10. The target for scale-up is **≥90/100 overall**, with **no category below 8/10 equivalent** and no automatic-fail defect.

### Automatic major deductions / caps

- Obvious AI-generated cadence or stock contrast language repeated across the answer: major deduction. If conspicuous enough that a reader would identify the prose as AI-shaped, the question cannot score above **84/100** until rewritten.
- Learner-facing process language (for example, instructions to the writer, source-workflow narration, “for this answer I do not need to list…”, or similar): **automatic revision required**.
- Numerical diagnostic denominator without the counted items when the denominator is educationally central (for example 5/10, 2/5, 4/9): **automatic revision required**.
- Non-obvious acronym/instrument appearing before local expansion in that question: deduction; repeated instances are a major defect.
- Change in dose, threshold, duration, legal article, recommendation strength or causal strength without source justification: **automatic factual fail**.
- Greek that is grammatically correct but plainly calqued from English is still a language defect.

## 1. Human-authored Greek and absence of AI slop — 20 points

Evaluate:
- natural contemporary Greek medical prose;
- sentence rhythm and variation;
- absence of repetitive “δεν είναι απλώς…”, “όχι μόνο… αλλά…”, “το βασικό είναι…”, “η πρακτική απάντηση…”, “συνοπτικά…” templates;
- absence of redundant concluding restatements;
- no writer-facing/meta prose;
- no unnecessary English-Greek hybrid syntax;
- terminology sounds like Greek psychiatry, not translated English.

## 2. Model oral answer — 15 points

Evaluate whether `## Πρότυπη προφορική απάντηση`:
- could genuinely be spoken by a strong specialist candidate;
- has a clear opening orientation and clinical sequence;
- prioritises rather than encyclopaedically dumps facts;
- uses prose for reasoning and synthesis;
- delegates enumerations to bullets/tables when appropriate;
- avoids padding and repeated conclusions;
- generally fits a 2–4 minute oral response unless the topic inherently requires more.

## 3. Retrieval architecture / structure — 15 points

Evaluate:
- information is placed where it is easiest to retrieve;
- criteria are lists/checklists rather than buried prose;
- comparisons use tables when this materially improves discrimination;
- emergency/treatment sequences are visibly ordered;
- headings are meaningful rather than decorative;
- the answer is neither a wall of prose nor an indiscriminate bullet list.

## 4. Diagnostic / operational visibility — 10 points

Where relevant:
- explicit counted criteria are shown;
- duration, exclusion and impairment rules are visible;
- DSM-5-TR and ICD-11 are kept separate;
- named triads/tetrads/clusters immediately state their components;
- the learner never has to infer what a denominator refers to.

If the question is not primarily diagnostic, score instead on visibility of the relevant operational sequence (monitoring, emergency actions, legal procedure, etc.).

## 5. Acronyms, instruments and technical terms — 8 points

- Every non-obvious acronym/instrument is expanded before or at first visual occurrence within the question, including the Recall Axis.
- Do not assume prior questions were read.
- Common terms such as DSM-5-TR, ICD-11, MRI, EEG, SSRI may remain abbreviated when unambiguous.
- Technical English may remain parenthetically when it improves recognition, but Greek should carry the prose.

## 6. Recall Axis — 8 points

`## Άξονας ανάκλησης` should:
- reconstruct the answer;
- usually contain 5–7 terse anchors;
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
- avoid trivial negative statements.

## 9. Examiner follow-ups / exam-vs-current distinction — 4 points

- Follow-ups should test a natural viva probe and add depth rather than duplicate the answer.
- Exam-vs-current sections should appear only when there is a real discrepancy or historically important distinction.
- Do not force either section into every question.

## 10. Source fidelity and clinical precision — 4 points

- Preserve verified meaning and uncertainty.
- Do not strengthen `may/consider` into `must/indicated`.
- Do not convert association into causation.
- Preserve doses, durations, thresholds, legal citations and regulatory boundaries.

## Pilot acceptance gate

Before scaling v5 beyond the pilot:

1. Each of Q001, Q012, Q019, Q020, Q038, Q045, Q090 and Q098 must be graded using this rubric.
2. Mean score must be **≥90/100**.
3. No question may be below **86/100**.
4. No automatic factual fail may remain.
5. No conspicuous AI-slop cap may remain.
6. Founder review should confirm that the prose feels materially more human, natural and teachable than final v4.
