# Greek manuscript cumulative language QA — master control file

## Purpose

This is the **single cumulative control file** for all post-translation Greek-language QA of *The 100 Crucial Questions in Psychiatry*.

Repository: `orestispsom/Psychiatry-Exams`

Greek manuscript:
`oral/100-crucial-questions/answers/revision-v2-el/Q001.md` … `Q100.md`

English semantic authority:
`oral/100-crucial-questions/answers/revision-v2/Q001.md` … `Q100.md`

Translation/terminology workspace:
`oral/100-crucial-questions/internal/translation/`

This file exists so that repeated audit passes remain **cumulative rather than episodic**. New audits may discover additional defects, but they must not lose, overwrite, silently reverse, or repeatedly reopen settled decisions from earlier passes.

---

# 1. Core operating rules

1. **English v2 controls meaning.** Greek may be made more natural, technically correct, and idiomatic, but psychiatric content must not be added, removed, softened, strengthened, or factually rewritten unless a separate content-revision task explicitly authorises it.
2. **Current Greek `main` controls state.** Before editing, sync and inspect the actual current file. If an issue listed here has already been corrected, mark it `ALREADY_FIXED`; do not re-edit merely to satisfy old wording.
3. **No mechanical search-and-replace across semantic terms.** Context decides the Greek rendering.
4. **Apply automatically only HIGH-confidence linguistic corrections.** Ambiguous terminology goes to `REVIEW_ONLY` with the English source phrase and surrounding sentence.
5. **Settled terminology is frozen.** A future pass may check for regression, but must not reopen a settled family without new evidence of an actual error.
6. **Every audit is cumulative.** A new pass adds new candidates to this master and preserves all unresolved candidates from previous passes.
7. **Every CLI correction run produces a ledger.** For each candidate use one status: `APPLIED`, `ALREADY_FIXED`, `NOT_FOUND`, `REVIEW_ONLY`, `REJECTED`, or `REGRESSION_FIXED`.
8. **Do not rebuild the publication PDF from a stale corpus.** Rebuild only after all HIGH-confidence source corrections in the current cumulative queue have been resolved.

---

# 2. Existing translation QA assets

The translation directory already contains the following working history and authorities:

- `Q001-Q100-greek-translation-QA.md`
- `Q001-Q100-greek-final-bilingual-QA-handoff.md`
- `Greek-manuscript-salience-correction-handoff.md`
- `Greek-manuscript-salience-correction-completion.md`
- `Greek-manuscript-second-language-audit-handoff.md`
- `Greek-manuscript-second-language-audit-results.md`
- `Greek-manuscript-third-language-audit-handoff.md`
- `Greek-manuscript-fourth-language-audit-handoff.md`
- `Translation-guide-v2.md`
- `Translation-guide-v2-writer-brief.md`
- `Translation-guide-v3.md`
- `Translation-guide-neuroscience-addendum.md`
- `Translation-guide-audit.md`
- `Translation-guide-current-research.md`

Do not delete these historical files. They preserve provenance. This master file is the **forward control surface**, not a replacement for the detailed evidence in those documents.

---

# 3. Settled / frozen correction families

## 3.1 Salience family — CLOSED

Status: **CLOSED / DO NOT REOPEN ROUTINELY**.

The dedicated salience correction has been applied. The bad literal mapping `salience → προεξοχή` is not an acceptable house translation.

Contextual house logic already established:

- aberrant salience → `παθολογική απόδοση σημασίας`
- affective/emotional salience → `συναισθηματική σημασιοδότηση` / `απόδοση συναισθηματικής σημασίας`
- incentive salience → `κινητροδοτική σημασία`
- salience of stimuli → `απόδοση σημασίας στα ερεθίσματα`
- symptom prominence/salience → `κυριαρχία`, `προεξάρχουσα παρουσία`, or another natural symptom-prominence form

Future passes may only fix **regressions or unrelated grammar on the same lines**.

## 3.2 Confirmed neuroscience/anatomy corrections — CLOSED unless regression

Current settled forms include:

- `φυματοχοανική οδός` for tuberoinfundibular pathway
- `πρόσθιος φλοιός του προσαγωγίου (ACC)` for anterior cingulate cortex
- `κοιλιοέσω προμετωπιαίος φλοιός` for ventromedial prefrontal cortex
- Q12 symptom wording using natural `κυριαρχία ... συμπτωμάτων` and `γνωστική δυσλειτουργία`, rather than calqued `προεξοχή` / `γνωστική αναπηρία`

Commit evidence for the applied neuroscience/psychiatric terminology corrections includes:

- `7a537d4f5ca6295ef119db6bed2ca94e4bd439f5`
- `8ddd9ea6f843513557b9f15cb0a1d4507f4fbe19`

---

# 4. Cumulative unresolved / pending correction families

These must remain in the queue until a CLI run records a final status against the current Greek corpus. Do not assume an old handoff has been executed merely because the handoff file exists.

## 4.1 General English-calque families from the third audit

Audit the full corpus and compare with English v2 before applying.

### `high-yield → υψηλής απόδοσης`

`υψηλής απόδοσης` is generally wrong when English means high-yield in an educational/exam sense.

Use contextually natural Greek such as:

- `ιδιαίτερα σημαντικό εξεταστικό σημείο`
- `υψηλής εξεταστικής αξίας`
- `ιδιαίτερα χρήσιμο παράδειγμα για τις εξετάσεις`
- `σημαντική διαφορική διάγνωση`

Do not alter literal performance/yield contexts where `απόδοση` is genuinely correct.

### `collateral history/information → παράπλευρο ιστορικό / παράπλευρες πληροφορίες`

Preferred psychiatric Greek:

- `ετεροαναφορικές πληροφορίες`
- `ετεροαναφορικό ιστορικό`
- `πληροφορίες από τρίτους/οικείους`

Choose according to sentence and register.

### Clinical `baseline → γραμμή βάσης`

Prefer context-specific Greek such as:

- `προηγούμενο επίπεδο λειτουργικότητας`
- `συνήθες επίπεδο λειτουργικότητας`
- `προϋπάρχον γνωστικό επίπεδο`
- `αρχικές τιμές` for actual measured baseline laboratory/physiological values

Do not ban `γραμμή βάσης` outside clinical prose if it is genuinely appropriate, but it should not be the default rendering.

### `engagement → θεραπευτική σύνδεση`

Distinguish:

- therapeutic alliance/engagement → `θεραπευτική συνεργασία`, `θεραπευτική σχέση`
- engagement with services → `σύνδεση με τις υπηρεσίες`, `διατήρηση επαφής με τις υπηρεσίες`, depending meaning

### `cross-situational → διακαταστασιακό`

For adult ADHD, prefer natural Greek explaining the criterion:

`παρουσία των συμπτωμάτων σε περισσότερα από ένα περιβάλλοντα/πλαίσια`.

### `treatment-emergent → αναδυόμενος από θεραπεία`

Avoid literal `αναδυόμενος` where unnatural. Use according to meaning:

- `που εμφανίστηκε μετά την έναρξη της θεραπείας`
- `που εμφανίστηκε κατά τη θεραπεία`
- `ανεπιθύμητες ενέργειες σχετιζόμενες με τη θεραπεία`

### Q45 specific known defects

- `μετανασθητική ανάνηψη` → compare English; expected `μετεγχειρητική ανάνηψη` / post-anaesthetic recovery wording
- `προσυμπτωματικός έλεγχος` for delirium screening → `ανίχνευση ντελίριου` / `έλεγχος ανίχνευσης`

### `pathway → μονοπάτι`

Do **not** blanket-replace. Biological signalling pathways may legitimately be `μονοπάτια`.

Where English means a care/treatment pathway, prefer:

- `θεραπευτική διαδρομή`
- `θεραπευτική ακολουθία`
- `αλγόριθμος αντιμετώπισης`
- `πορεία φροντίδας`

according to context.

---

## 4.2 Pharmacology/regulatory and technical-Greek families from the fourth audit

### `φαρμακοειδικός` for drug-specific / product-specific

Do not retain the neologism `φαρμακοειδικός`.

Preferred forms:

- `διαφέρει ανάλογα με το συγκεκριμένο φάρμακο`
- `εξαρτάται από το συγκεκριμένο φάρμακο`
- `ειδικός για το συγκεκριμένο σκεύασμα/προϊόν`

Known targets include Q71, Q75 and Q76, plus corpus-wide inflections of `φαρμακοειδ-`.

### `patient-specific → ασθενοκεντρικός`

`ασθενοκεντρικός` means patient-centred, not patient-specific.

Where English says patient-specific, use natural phrasing such as:

`εξαρτάται από τα χαρακτηριστικά του συγκεκριμένου ασθενούς`.

Preserve genuine uses of patient-centred care.

### SmPC / SPC terminology

When the source means **Summary of Product Characteristics**, the house form is:

`Περίληψη Χαρακτηριστικών του Προϊόντος (ΠΧΠ/SmPC)`.

Do not call the SmPC `φύλλο οδηγιών`, which implies the patient information leaflet.

Audit `SPC`, `SmPC`, `φύλλο οδηγιών`, `πληροφορίες προϊόντος`, and equivalent wording in Q007/Q019/Q075/Q078 and corpus-wide.

### Q074 technical pharmacology

Known high-confidence targets:

- `φαινόμενο όγκο κατανομής` → `φαινομενικό όγκο κατανομής`
- `πρωτοταγή θέση του αγωνιστή` → preferably `κύρια θέση πρόσδεσης του αγωνιστή`; `ορθοστερική θέση πρόσδεσης` only if terminology authority supports it
- review `απο-επαγωγή` → likely `άρση της ενζυμικής επαγωγής`

### Q085 medication diversion

Do not use `διασπορά` for prescription medication diversion.

Preferred first explicit rendering:

`παράνομη διάθεση της συνταγογραφούμενης αγωγής σε τρίτους (diversion)`

Then shorter `παράνομη διάθεση` where clear.

### Q089 ECT terminology

Known targets:

- `παθολογική/αναισθησιολογική εκτίμηση` → `ιατρική και αναισθησιολογική εκτίμηση`
- `γνωστικό φορτίο` → `γνωστική επιβάρυνση`

Do not alter the underlying ECT recommendations.

### Q093 shared decision-making / relapse signature

Avoid calqued:

- `συν-απόφαση`
- `υπογραφή υποτροπής`

Preferred:

- `από κοινού λήψη αποφάσεων` or `συνεργατική λήψη αποφάσεων`
- `ατομικό πρότυπο πρώιμων προειδοποιητικών σημείων υποτροπής`

The relapse-signature issue also applies outside Q093, including Q017 where present.

### Q097 evidence-language calque

`συνολικό σώμα των επιστημονικών τεκμηρίων` → prefer `σύνολο της διαθέσιμης επιστημονικής τεκμηρίωσης`.

Do not automatically replace potentially established statistical terms such as the current rendering of pre-test probability unless terminology is independently confirmed.

### Q007 postictal and incident-review wording

Known targets:

- `μετακρίσιμη κατάσταση` → `μετακριτική κατάσταση`
- `Παρατηρήσεις ανά δεκαπεντάλεπτο` → natural `παρακολούθηση ανά 15 λεπτά` / `έλεγχος ανά 15 λεπτά`
- `τι εκδήλωσε τη διέγερση` → `τι πυροδότησε/προκάλεσε τη διέγερση`

### Q039 precipitated withdrawal and awkward patient phrasing

Audit against English v2 for natural Greek. Do not use literal constructions that imply the withdrawal is merely `εκλυόμενη` without conveying that opioid antagonism **precipitates** an acute withdrawal syndrome. Prefer an established natural phrase such as `προκληθείσα οξεία στέρηση` if confirmed in context.

Also remove constructions such as `εξατομικευμένο ασθενή`; the treatment is individualised, not the patient.

---

# 5. Audit strategy from this point onward

Repeated whole-corpus keyword scans are useful but insufficient. From here, use **two complementary modes**.

## Mode A — lexical/systematic sweeps across all Q001–Q100

Each pass selects a semantic family and runs corpus-wide search, always checking English v2 before changing.

Recommended remaining systematic lenses:

1. **Anglicised adjective/noun formations** — literal compounds, English suffix logic, unnatural Greek neologisms.
2. **Clinical-service language** — pathway, engagement, follow-up, outreach, recovery, care plan, crisis plan, adherence/concordance.
3. **Psychopharmacology/regulatory language** — SmPC, licensed/authorised, treatment-emergent, product-specific, formulation, exposure, washout, titration, augmentation, switching.
4. **Psychotherapy language** — formulation, enactment, projective identification, collaborative empiricism, behavioural experiment, inhibitory learning, role transition/dispute, therapeutic frame.
5. **Research/statistics language** — effect size, confidence interval, pre-test probability, likelihood ratio, attrition, allocation concealment, generalisability, body of evidence.
6. **Neurology/sleep/neuropsychology** — postictal/interictal, recovery room, executive dysfunction, set-shifting, sleep-stage terminology, cognitive domains.
7. **Law/services Greek register** — ensure legal terms remain official Greek rather than translated-back English legal language.
8. **Abbreviations/parenthetical English** — consistent first-use expansion, Greek term + English acronym only when it genuinely aids exam retrieval.

## Mode B — deep bilingual sequential read

After the broad lexical sweeps, perform a **line-by-line Greek ↔ English read in five blocks of 20 questions**:

- Deep Read A: Q001–Q020
- Deep Read B: Q021–Q040
- Deep Read C: Q041–Q060
- Deep Read D: Q061–Q080
- Deep Read E: Q081–Q100

For each sentence, ask:

1. Does the Greek preserve the English meaning exactly?
2. Would a Greek psychiatrist naturally say/write this?
3. Is the technical term established or merely morphologically translated?
4. Has an English abstract noun been turned into unnatural Greek nominal prose?
5. Is an English adjective better rendered as a Greek clause?
6. Has the translation accidentally changed the clinical subject, agency, causality, certainty, temporality, or scope?
7. Is the terminology consistent with earlier corrected questions?

This deep-read phase is more likely to find defects that no `rg` keyword can predict.

---

# 6. Recommended cadence

Do **not** keep generating disconnected handoff files indefinitely.

Recommended workflow for every further audit turn:

1. Read this master first.
2. Inspect current `main` and latest translation/fix commits.
3. Audit using one clearly different lens or one 20-question deep-read block.
4. Add only genuinely new findings to this master under a dated/pass-labelled section.
5. Do not remove unresolved findings from earlier passes.
6. Produce a short delta handoff only if a CLI needs immediate execution instructions.
7. CLI runs the **master + latest delta**, not a chain of old handoffs.
8. CLI records all outcomes in one cumulative results ledger:
   `oral/100-crucial-questions/internal/translation/Greek-manuscript-cumulative-language-QA-results.md`
9. After source corrections, CLI commits/pushes and re-reads from `origin/main`.
10. Only after the cumulative HIGH-confidence queue is empty should Final rebuild/freeze the Greek PDF.

This prevents stale instructions, duplicate edits and regression.

---

# 7. Stop condition

Continue iterative language audits while each materially different pass is still finding multiple substantive defects.

Move to final freeze when all of the following are true:

- two consecutive **different** audit lenses find no new HIGH-confidence systematic error family;
- the five 20-question bilingual deep-read blocks are complete;
- all cumulative HIGH-confidence items are `APPLIED` or `ALREADY_FIXED`;
- `REVIEW_ONLY` items have been explicitly adjudicated or accepted as intentional;
- corpus-wide regression searches for previously banned calques are clean;
- Greek PDF is rebuilt from the corrected Markdown;
- PDF text extraction/visual QA shows no truncation, broken characters, duplicated text, incorrect line wrapping around units/English acronyms, or stale pre-correction content.

Do not use a fixed number of passes as the stop rule. Use diminishing discovery plus completion of the sequential bilingual read.

---

# 8. Current repository-state note at creation of this master

At the time this file was created (20 Aug 2026), the most recent visible manuscript terminology-fix commits were:

- `7a537d4f5ca6295ef119db6bed2ca94e4bd439f5` — salience/symptom-prominence correction
- `8ddd9ea6f843513557b9f15cb0a1d4507f4fbe19` — Greek psychiatric/neuroscience terminology corrections

The third- and fourth-audit handoff files were present, but no later manuscript-fix commit was visible after the fourth handoff. A future CLI must therefore **inspect current `main` rather than assuming those handoffs were executed**.

---

# 9. Required CLI completion format

For each cumulative correction run, report:

- files inspected
- files changed
- count `APPLIED`
- count `ALREADY_FIXED`
- count `REVIEW_ONLY`
- count `REJECTED`
- count `NOT_FOUND`
- any regressions discovered
- manuscript commit SHA
- PDF rebuilt: YES/NO and output path if YES
- remote re-read verification: PASS/FAIL

When the current cumulative queue is fully resolved, return:

`GREEK_CUMULATIVE_LANGUAGE_QA_CURRENT_PASS_READY`

Do **not** claim the manuscript is globally final until the stop condition in section 7 is satisfied.
