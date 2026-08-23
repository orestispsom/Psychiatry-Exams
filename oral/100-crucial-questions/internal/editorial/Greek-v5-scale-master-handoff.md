# Greek v5 scale-up — master Writer handoff

Status: **READY FOR SCALE-UP WRITER**

Repository: `orestispsom/Psychiatry-Exams`

Calibration branch: `greek-v5-pilot`

Target scale-up branch: `greek-v5-scale`

## 1. Mission

Produce the complete Greek-first v5 corpus for **The 100 Crucial Questions in Psychiatry**.

The eight-question calibration pilot is complete and founder-reviewed. The remaining task is to apply that final doctrine consistently to the other 92 questions without sacrificing factual fidelity.

This is primarily an **editorial rewrite/manufacture task**, not a new broad research project.

The central object is the `## Πρότυπη προφορική απάντηση`. It must sound like a strong Greek psychiatry specialist candidate answering the examiner directly.

Accuracy remains prior to style.

## 2. Controlling documents — read before writing anything

Read these completely, in this order:

1. `oral/100-crucial-questions/internal/editorial/Greek-v5-scale-doctrine.md`
2. `oral/100-crucial-questions/internal/editorial/Greek-v5-pilot-scoring-rubric.md`
3. the eight founder-approved calibration answers under:
   `oral/100-crucial-questions/answers/revision-v5-pilot-el/`
4. this handoff.

The founder-approved scale doctrine controls stylistic and oral-answer decisions.

The updated scoring rubric contains hard gates. A high numerical score cannot rescue an answer that fails clinical sequence, read-aloud naturalness or source fidelity.

The pre-founder `Greek-v5-pilot-independent-adjudication.md` remains useful only as a factual/source audit trail. Its old stylistic scores are **not** controlling.

## 3. Output location

Do not overwrite final v4 or the pilot directory.

Create the complete v5 working corpus under:

`oral/100-crucial-questions/answers/revision-v5-el/`

The directory must ultimately contain **Q001.md through Q100.md**.

### Locked pilot questions

For these eight questions, copy the current founder-approved files from `revision-v5-pilot-el/` **verbatim** into `revision-v5-el/`:

- Q001
- Q012
- Q019
- Q020
- Q038
- Q045
- Q090
- Q098

Do not rewrite, polish, normalize or silently “improve” them during scale-up.

They are the stylistic calibration set.

Create also:

`oral/100-crucial-questions/internal/editorial/Greek-v5-scale-writer-report.md`

Do not create a PDF and do not promote files to `final-v5-el/` in this task.

## 4. Source hierarchy

### 4.1 Approved question/batch briefs control learner-facing factual content

Use the corresponding approved brief under:

`oral/100-crucial-questions/answers/briefs/`

Current batch briefs are:

- `Q001-Q010-batch.md`
- `Q011-Q019-batch.md`
- `Q020-Q027-batch.md`
- `Q028-Q036-batch.md`
- `Q037-Q044-batch.md`
- `Q045-Q051-batch.md`
- `Q052-Q058-batch.md`
- `Q059-Q073-batch.md`
- `Q074-Q089-batch.md`
- `Q090-Q100-batch.md`

Use question-specific approved files such as `Q012.yml` where they exist and are relevant.

### 4.2 Current-verification layer controls vulnerable current claims

Use:

`oral/100-crucial-questions/internal/revision/Q001-Q100-board-depth-current-verification.md`

and the approved source-use/adjudication material already present in the repository when the brief points to it.

For diagnosis, preserve verified DSM-5-TR / ICD-11 distinctions.

For treatment, psychopharmacology, monitoring, drug safety/licensing, Greek law and other time-sensitive claims, the approved current-verification layer overrides historical exam shorthand.

### 4.3 Final v4 is a completeness backstop, not a writing template

Use:

`oral/100-crucial-questions/answers/final-v4-el/`

only to check that important already-adjudicated material has not been accidentally lost.

Do **not** preserve v4 wording, paragraph order, opening sentences or architecture merely because they already exist.

### 4.4 Do not launch broad new research

This scale-up task is source-locked to the approved repository layer.

If a consequential ambiguity cannot be resolved from the approved material:

- do not guess;
- preserve the safest already-adjudicated formulation where possible;
- record `SOURCE_QUERY` in the Writer report;
- continue with the remaining questions rather than stopping the entire manufacture run.

Do not change a threshold, dose, duration, legal article, monitoring schedule, indication, contraindication, recommendation strength or causal claim without approved source support.

## 5. The production method for every non-pilot question

For each question, perform this sequence:

### Step 1 — Read the question literally

Identify exactly what the examiner asks and in what order.

Examples:

- `κλινική εικόνα, διάγνωση και διαφορική διάγνωση` → clinical picture → diagnosis → differential;
- `αναγνωρίζετε, αξιολογείτε και αντιμετωπίζετε` → recognition → assessment → management;
- `τι είναι ... και πώς χρησιμοποιείται` → definition/model → use/applications.

Clinical safety may justify an earlier emergency point, but editorial convenience does not.

### Step 2 — Extract verified content backstage

Read the approved brief/current-verification material and identify:

- required clinical content;
- exact criteria/thresholds/durations;
- current-vs-historical distinctions;
- high-value board facts;
- likely examiner traps;
- any source-sensitive wording.

This is a backstage content map only.

### Step 3 — Design the clinical discourse architecture

Decide how a psychiatrist would naturally answer the examiner.

Do **not** mechanically convert outline labels into prose.

A backstage label such as `setting`, `monitoring`, `severity`, `differential`, `first decision`, `next step` or `framework` is not automatically a learner-facing sentence.

Clinical causality must be preserved: evidence/assessment should precede the decision that follows from it.

### Step 4 — Write the model oral answer from scratch in Greek

Write as if composing directly in Greek, not translating English sentence-by-sentence.

The answer should normally be speakable in roughly **2–4 minutes**, with asymmetry when the subject genuinely requires it.

Use first-person clinical verbs when they express real clinical action: `ελέγχω`, `αναζητώ`, `εκτιμώ`, `ρωτώ`, `χορηγώ`, `αποκλείω`.

Do not use first-person narration merely to announce the structure of the answer.

### Step 5 — Add operational material where it genuinely improves retrieval

Use lists/tables/checklists selectively for:

- counted diagnostic criteria;
- monitoring schedules;
- emergency drug regimens;
- compact comparisons;
- legal rule/exception structures;
- short instruments whose components are high-yield.

Operational material supports the clinical answer; it does not automatically become the answer's architecture.

### Step 6 — Completeness check against v4

Only after the new Greek-first answer exists, compare it against final v4.

Recover any important verified fact that was accidentally omitted, but integrate it according to the v5 clinical architecture rather than copying the old paragraph.

### Step 7 — Read-aloud QA

Read the model answer literally as viva speech.

For every sentence ask:

1. Would a strong Greek psychiatrist plausibly say this aloud to an examiner?
2. Does it add psychiatric information, prioritisation or reasoning?
3. Does it follow clinically from what precedes it?
4. Is the Greek ordinary professional Greek rather than a possible translation?
5. Is it answering the examiner rather than narrating the production of the answer?

Rewrite or delete sentences that fail.

## 6. Hard oral-language rules

The following are hard revision triggers when they function as editorial narration rather than clinical content:

- `Η πρώτη απόφαση είναι...`
- `Το επόμενο βήμα είναι...`
- `Η προσέγγιση οργανώνεται...`
- `Στην εξέταση θέλω να δείξω...`
- `Για τις εξετάσεις πρέπει...`
- `Η πρακτική απάντηση είναι...`
- generic concluding paragraphs that merely restate the answer.

Do not write circular definitions such as:

`Η Χ διαταραχή είναι Χ διαταραχή...`

If the question asks for clinical picture, begin with clinical picture rather than forcing taxonomy.

Prefer established Greek clinical terminology over grammatically possible calques.

Founder-calibrated examples include:

- `πληροφορίες από το περιβάλλον`, not `ετεροαναφορικές πληροφορίες`;
- `υπερδραστηριότητα του αυτόνομου νευρικού συστήματος` where appropriate;
- `ψυχοκινητική διέγερση`;
- `ασφάλεια`;
- ordinary phrases such as `υπόθεση εργασίας` rather than coined abstract compounds.

## 7. Clinical-domain rules

### Diagnostic / phenomenology questions

Default:

1. clinical picture/syndrome;
2. severity/red flags where relevant;
3. diagnosis and criteria;
4. differential;
5. selected discriminators/follow-ups.

Do not let DSM/ICD mechanics displace phenomenology unless criteria are explicitly the question.

Keep DSM-5-TR and ICD-11 separate where they differ.

A central denominator such as `5/10`, `2/5` or `2/7` must have its counted items visible nearby.

### Assessment questions

Follow real clinical assessment order and do not assume the diagnosis/syndrome before it has been established.

When collateral is relevant, prefer natural wording such as `πληροφορίες από το περιβάλλον`, then specify family/carers/staff/records as appropriate.

### Emergency questions

Follow real clinical priorities:

1. identify syndrome/emergency;
2. current severity and immediate threats;
3. risk factors/causes that change risk;
4. core treatment/support;
5. disposition/escalation as a consequence of the assessment;
6. major complications in separate short subsections where useful.

Do not confuse **current severity** with **predictors of severe/complicated course**.

### Psychopharmacology questions

Use question-specific logic. Do not impose one universal drug template.

Where natural, the clozapine pilot supports:

- pharmacological identity;
- useful mechanism;
- indications/place in treatment;
- major dangers/adverse effects;
- monitoring/practical pharmacokinetics.

Do not drown the oral answer in receptor trivia or monitoring tables before explaining the drug.

### Psychotherapy questions

Do not produce generic therapy essays.

For CBT-like questions, use the calibrated logic:

- what it is;
- model/formulation;
- collaborative process;
- techniques linked to mechanisms/problems;
- selected applications;
- between-session work/relapse prevention.

### Law / ethics questions

Precision can require more technical prose.

Do not over-colloquialise legal material at the expense of accuracy.

Keep the main oral core focused on governing duty/principle → scope → exceptions/legal basis → practical handling/documentation.

## 8. Learner-facing file structure

Each question should contain, as appropriate:

- question heading;
- `## Άξονας ανάκλησης`;
- `## Πρότυπη προφορική απάντηση`;
- `## Βασικά σημεία για τις εξετάσεις`;
- `## Συχνές παγίδες / παγίδες εξεταστή`.

Examiner follow-ups and `Απάντηση εξετάσεων έναντι τρέχουσας πρακτικής` are optional.

Include them only when they add real viva value or clarify a genuine historical/current discrepancy.

### Recall Axis

Usually 5–7 terse anchors.

It reconstructs the answer but is **not** prose to be spoken.

Do not allow its headings to leak mechanically into paragraph openings.

### Basic Exam Points

Usually 4–6 high-value facts: thresholds, durations, discriminators, monitoring rules, high-stakes exceptions.

Do not merely repeat the model oral answer sentence-for-sentence.

### Traps

Usually 4–6 plausible errors a competent candidate might make.

No filler and no trivial negatives.

## 9. Acronyms, instruments and named clusters

Expand non-obvious acronyms/instruments at or before first visual use in each standalone question.

Named triads/tetrads/clusters should state their components immediately when invoked.

Short instruments may receive a concise component summary when this materially aids recall; full manuals do not belong in the spoken core unless specifically asked.

A screening instrument must never be presented as if it were the diagnosis.

## 10. Fidelity gate

Automatic factual fail if an unsupported change is made to:

- diagnostic threshold;
- symptom denominator;
- duration;
- dose/regimen;
- concentration;
- monitoring schedule;
- indication/licensing;
- contraindication;
- Greek legal article/rule;
- recommendation strength;
- causal strength.

Do not strengthen `may/consider` into `must/indicated`.

Do not turn association into causation.

When uncertain, preserve the approved formulation and record `SOURCE_QUERY`.

## 11. Hard QA gate before a question can pass

Before assigning any numerical rubric score, all of the following must be YES:

- Does the answer follow the question's requested order unless safety/clinical logic clearly overrides it?
- Does each major transition follow actual clinical reasoning rather than editorial outline order?
- Does the opening answer the examiner directly?
- Does every paragraph survive the read-aloud viva test?
- Has outline narration been removed?
- Is the Greek natural contemporary psychiatric/medical Greek?
- Are clinically distinct domains kept distinct when useful?
- Are operational criteria/scales subordinate to the clinical answer?
- Are all consequential claims source-faithful?
- Has final v4 been checked for accidental omissions only after the new answer was drafted?

If any answer is NO, the question is **not ready to score** and must be revised.

Only after the hard gates pass, apply:

`Greek-v5-pilot-scoring-rubric.md`

## 12. Manufacture batches

Complete all batches without waiting for founder approval between them.

The existing approved brief remains the factual source even when a source batch is split into smaller manufacture batches.

| Manufacture batch | Questions to rewrite | Approved source brief |
|---|---|---|
| V5-A | Q002–Q010 | Q001-Q010-batch.md |
| V5-B | Q011, Q013–Q018 | Q011-Q019-batch.md |
| V5-C | Q021–Q027 | Q020-Q027-batch.md |
| V5-D | Q028–Q036 | Q028-Q036-batch.md |
| V5-E | Q037, Q039–Q044 | Q037-Q044-batch.md |
| V5-F | Q046–Q051 | Q045-Q051-batch.md |
| V5-G | Q052–Q058 | Q052-Q058-batch.md |
| V5-H | Q059–Q066 | Q059-Q073-batch.md |
| V5-I | Q067–Q073 | Q059-Q073-batch.md |
| V5-J | Q074–Q081 | Q074-Q089-batch.md |
| V5-K | Q082–Q089 | Q074-Q089-batch.md |
| V5-L | Q091–Q097, Q099–Q100 | Q090-Q100-batch.md |

Total rewritten: **92 questions**.

Plus the 8 locked pilot files copied verbatim = **100-question v5 working corpus**.

## 13. Git workflow

1. Start from the current founder-reviewed `greek-v5-pilot` HEAD.
2. Create/switch to branch `greek-v5-scale`.
3. Create `answers/revision-v5-el/`.
4. Copy the eight locked pilot files verbatim.
5. Complete V5-A through V5-L in order.
6. Commit after each manufacture batch.
7. Do not wait for approval between batches.
8. Do not merge into `main` or any v4 branch.
9. Keep the working tree clean after each commit.

Suggested commit pattern:

`editorial: Greek v5 scale batch A Q002-Q010`

through:

`editorial: Greek v5 scale batch L Q091-Q100`

The locked-pilot copy may be included in the first setup commit or V5-A commit, but record it clearly in the report.

## 14. Mandatory corpus-level QA after V5-L

After all 100 files exist:

### Completeness

- exactly Q001–Q100 present;
- no missing numbers;
- no accidental duplicate question files;
- eight pilot questions byte-for-byte/content-identical to the founder-approved pilot versions.

### Language/cadence sweep

Search the corpus for repeated/generated constructions, including:

- `Η πρώτη απόφαση είναι`
- `Το επόμενο βήμα`
- `Η προσέγγιση οργανώνεται`
- `Στην εξέταση θέλω`
- `Για τις εξετάσεις πρέπει`
- `Η πρακτική απάντηση`
- repeated `δεν είναι απλώς ... αλλά ...`
- repeated generic summary endings.

A search hit is not automatically wrong; inspect it in context.

### Terminology sweep

Check for recurrent known calques and inconsistent Greek terminology.

Do not perform blind global replacements where context matters.

### Operational sweep

Check:

- denominators have counted items nearby;
- acronyms expanded locally;
- triads/clusters stated;
- monitoring schedules remain exact;
- current/historical distinctions remain labelled;
- legal and pharmacological numbers have not drifted.

### Oral-usability sampling

Re-read at least one answer from every manufacture batch aloud from beginning to end, plus all eight calibration questions.

If sampled answers reveal a systematic defect, inspect the whole relevant batch before declaring completion.

## 15. Writer report

Create `Greek-v5-scale-writer-report.md` containing:

- branch and starting commit;
- 100/100 completion count;
- confirmation that eight pilot questions were copied unchanged;
- commit SHA for each V5-A through V5-L batch;
- source brief used for each batch;
- `SOURCE_QUERY` list, if any;
- summary of major structural rewrites by batch;
- hard-gate QA result for every question;
- rubric self-score for every question **only after** hard gates pass;
- corpus-level cadence/terminology/operational QA findings;
- statement that the corpus is ready for independent adjudication, but **not publication-ready**.

## 16. Stop conditions

Do not stop for ordinary editorial uncertainty; make the best source-faithful Greek-first decision and continue.

Do not stop between manufacture batches for approval.

Do not guess consequential facts.

A `SOURCE_QUERY` does not block progress on unrelated questions.

If a file cannot be safely written without inventing a consequential fact, preserve the safest approved content, flag the exact issue in the report, and continue.

## 17. Completion response

Return:

- target branch;
- 100/100 file count;
- 92 rewritten + 8 locked-copy count;
- V5-A through V5-L commit SHAs;
- `SOURCE_QUERY` count and list;
- corpus-level QA result;
- final status exactly:

`GREEK_V5_SCALE_WRITER_COMPLETE`
