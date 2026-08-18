# Attempt 009 — Greek Oral-Phrasing and Adult-Board Scope Audit

Status: source-locked review against the current `orestispsom/Psych` oral-exam files. No external curriculum was used to infer phrasing.

## 1. Sources inspected

- `orestispsom/Psych/src/data/oral.js`
- `orestispsom/Psych/src/data/oralCore.js`
- `orestispsom/Psych/ORAL_QUALITY_AUDIT.md`

`oral.js` / `ORAL_QUALITY_AUDIT.md` are treated as stronger evidence for the curated Greek oral bank and topic weighting. `oralCore.js` is useful for viva cadence and realistic examiner follow-ups, but it is a broader simulator and must not independently determine Adult Psychiatry board allocation.

## 2. Observed Greek viva question style

The dominant forms are short and direct:

- `Ποια ...;` → `What are ...?`
- `Πώς ...;` / `Πώς θα ...;` → `How do you ...? / How would you ...?`
- `Τι είναι ...;` → `What is ...?`
- `Τι ξέρετε για ...;` → `What do you know about ...?`
- `Περιγράψτε ...` → `Describe ...`
- brief clinical vignette followed by `Πώς θα τον/την προσεγγίσετε;` → `How would you approach this patient?`

The source bank frequently uses one broad but clinically coherent anchor followed by short examiner probes. It is less likely than Attempt 009 to use polished written-exam phrasing such as `How should X be organised?`, `What are the leading models and what are their strengths and limitations?`, or long compound prompts with several qualifications in the headline.

## 3. Phrasing doctrine for the next attempt

- Keep English-first, but use Greek oral-exam cadence.
- Prefer one short sentence.
- Prefer `Describe`, `What is/are`, `How do you`, `When do you`, `How would you approach this patient?`.
- Use a short clinical vignette when the source bank naturally tests a presentation or management decision.
- Allow a clinically coherent broad anchor when that matches the viva style, but do not reintroduce the old problem of answer-outline subquestions.
- Keep genuine follow-ups short. The examiner should sound as if they are interrupting and probing, not reading a written syllabus.
- Avoid unnecessary phrases such as `in psychiatric practice`, `for an individual patient`, `clinically important`, or `associated mental-health concerns` when the target is already obvious.
- Avoid academic-review wording when a direct oral formulation works better.

## 4. Examples of source cadence

Representative forms in the current Greek files include:

- `Ποια η ντοπαμινεργική και ποια η γλουταμινεργική υπόθεση για τη σχιζοφρένεια; Πώς αντιστοιχούν στα συμπτώματα;`
- `Ποια τα αρνητικά συμπτώματα; Πώς τα θεραπεύετε;`
- `Ποια η διαφοροδιάγνωση Alzheimer – Lewy Body – μετωποκροταφικής άνοιας;`
- `Τι είναι η CBT; Ποιες οι εφαρμογές της;`
- `Τι είναι η μεταβίβαση και η αντιμεταβίβαση;`
- `Ποια τα στάδια ύπνου; Ποιο το ΗΕΓ κάθε σταδίου;`
- `Νέος 23 ετών ... Πώς θα τον προσεγγίσετε διαγνωστικά και θεραπευτικά;`
- `Μιλήστε μου για την κλοζαπίνη: ενδείξεις, πλεονεκτήματα, κίνδυνοι και παρακολούθηση.`

The intended adaptation is not literal translation of these items. It is to reproduce their concise examiner cadence while preserving the independently designed 100-question coverage architecture.

## 5. Adult Psychiatry scope finding

Attempt 009 still over-allocates main slots to child/adolescent-only material.

The curated 129-question oral bank audited in `ORAL_QUALITY_AUDIT.md` is overwhelmingly Adult Psychiatry. Its developmental material contains a dedicated autism block, while `oralCore.js` adds ADHD, autism and Tourette as broader simulator anchors. The current curated bank does not provide comparable support for dedicated main questions on:

- general child/adolescent psychiatric assessment;
- child abuse/neglect as a standalone child-psychiatry topic;
- ODD versus conduct disorder;
- adolescent major depression.

These remain legitimate psychiatry knowledge but should not displace adult-board questions.

## 6. Adult-board reallocation recommended

Remove from dedicated main-question allocation:

- general child/adolescent assessment;
- child abuse/neglect;
- Tourette/tic disorders as a standalone main;
- ODD/conduct disorder;
- adolescent depression.

Retain, but explicitly adult-frame:

- ADHD;
- autism;
- intellectual developmental disorder.

Use the five freed slots for adult topics directly represented in the Greek oral material and currently under-sampled:

1. sleep stages / REM-NREM / EEG findings;
2. apathy versus depression;
3. Charles Bonnet syndrome;
4. psychoeducation;
5. clinically important psychotropic drug interactions.

## 7. Final recommendation

Create Attempt 010 as an Adult Psychiatry / Greek-viva phrasing pass.

- Keep 100 main questions.
- Preserve the substance of the near-final clinical architecture.
- Replace five child/adolescent-only main slots with the five adult topics above.
- Rephrase the whole bank toward concise oral-board cadence.
- Preserve child/adolescent material in internal coverage rather than deleting it from the broader psychiatry knowledge bank.
