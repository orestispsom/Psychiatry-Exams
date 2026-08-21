# Greek v4 Writer master handoff

Status: **READY FOR FRESH WRITER CHAT**

Repository: `orestispsom/Psychiatry-Exams`

Purpose: create the next Greek manuscript as a **source-enhanced structural/editorial rewrite**, not as a cosmetic rewrite of v3.

This file is intended to be the only startup handoff needed in a fresh Writer conversation.

---

## 1. Core editorial decision

`revision-v3-el` is **not an authority**. It is a useful draft containing substantial approved work, but the latest review exposed important omissions, retrieval failures, unexplained acronyms, structural weaknesses and residual AI-style prose.

Therefore Writer must not preserve v3 merely because text already exists there.

Use v3 as:
- a Greek-language draft;
- a record of already incorporated corrections;
- a source of useful phrasing and answer architecture when it survives scrutiny.

Do **not** use v3 as:
- the semantic authority;
- the final diagnostic authority;
- the final treatment authority;
- the final board-fact authority;
- a reason to preserve weak structure.

The task is to produce a better book, while preserving already verified facts unless stronger source authority requires correction.

---

## 2. Source hierarchy for v4

Different claims require different authorities. Do not use one source for everything.

### Tier A — Greek exam truth / exam framing

Use for what a Greek Adult Psychiatry candidate is expected to recognise, including classic psychopathology, traditional examiner pivots and board emphasis:

- prescribed **Shorter Oxford Textbook of Psychiatry, 7th edition (2017/2018 printing)**;
- Greek oral-exam material and examiner provenance from `orestispsom/Psych`;
- `oral/100-crucial-questions/internal/board-fact-anchors.yml`;
- `oral/100-crucial-questions/internal/question-design.md`;
- `oral/100-crucial-questions/internal/answer-production/answer-archetypes.md`;
- existing Oxford/base-source packets where present.

Old exam material controls **exam framing**, not current treatment, licensing or law.

### Tier B — already adjudicated current verification

This is the most important existing current-practice authority in the repository:

`oral/100-crucial-questions/internal/revision/Q001-Q100-board-depth-current-verification.md`

It adjudicates 349 consequential claim units and explicitly records KEEP / MODIFY / DROP / UNRESOLVED decisions.

**This document overrides v3 and the earlier enrichment audit whenever they conflict.**

Also use question-specific current-verification packets already present under:

`oral/100-crucial-questions/internal/answer-production/`

when they exist.

### Tier C — diagnosis / classification

Use current diagnostic manuals directly when an answer states operational diagnostic requirements or diagnostic counts:

1. **WHO ICD-11 Clinical Descriptions and Diagnostic Requirements (CDDR), 2024** — primary current ICD authority.
2. **DSM-5-TR, 2022** — DSM authority.

Do not merge their criteria into a hybrid system.

When they differ, label the system explicitly and present the distinction only when it improves the board answer.

### Tier D — psychopharmacology / prescribing

Use:

1. **The Maudsley Prescribing Guidelines in Psychiatry, 15th edition (2025)**;
2. official current **SmPC / EMA / Greek EOF** information for product-specific indications, contraindications, monitoring, restart rules and licensing;
3. the current-verification packet above;
4. **Stahl** for clinically useful mechanism explanations, not as the primary authority for licensing or regulatory detail.

For antidepressant / benzodiazepine / Z-drug discontinuation questions, add where accessible:

- **The Maudsley Deprescribing Guidelines: Antidepressants, Benzodiazepines, Gabapentinoids and Z-drugs (2024)**.

### Tier E — current treatment guidance

Use the current-verification packet first, then current authoritative guidance when more structure or exact sequencing is needed.

High-value source set includes, as applicable:

- NICE NG225 — Self-harm;
- NICE NG10 — Violence and aggression / rapid tranquillisation;
- NICE CG178 — Psychosis and schizophrenia;
- NICE NG222 — Depression in adults;
- NICE CG185 — Bipolar disorder;
- NICE CG31 — OCD;
- NICE CG159 — Social anxiety disorder;
- NICE CG113 — GAD and panic disorder;
- NICE NG69 — Eating disorders;
- NICE NG87 — ADHD;
- NICE NG97 — Dementia;
- relevant NICE substance-use guidance;
- BAP 2023 catatonia guideline where relevant;
- MEED for medical emergencies in eating disorders;
- EXTRIP for lithium poisoning;
- AASM / current specialist sleep guidance where the sleep questions require operational specialist detail;
- current specialist consensus only where the verification packet already establishes its role or where a genuine gap remains.

Do not turn the manuscript into a guideline collage. The purpose is to support a coherent viva answer.

### Tier F — Greek law / regulation / service organisation

Use current official Greek law and government/regulatory sources, plus the already verified legal packet.

Do not import UK/US legal rules into Greek answers.

### Tier G — stable specialist depth

For stable phenomenology, neurobiology, neuropsychiatry and broad clinical depth, the following remain useful triangulation sources:

- New Oxford Textbook of Psychiatry, 3rd ed. (2020);
- Kaplan & Sadock's Synopsis of Psychiatry (2021);
- Shorter Oxford 7th where exam-specific;
- Stahl for mechanisms.

These are secondary to current diagnostic/guideline/regulatory sources when recency matters.

---

## 3. New source additions recommended for this rewrite

The following should be treated as explicit additions/upgrades to the v4 source stack rather than merely future possibilities:

1. **WHO ICD-11 CDDR 2024**
   - especially important for Q20, Q23, Q28–Q36, Q37–Q44, Q59–Q73;
   - use to expose actual operational criteria when the text gives counts or thresholds.

2. **Maudsley Prescribing Guidelines 15th ed. 2025**
   - especially Q16–Q19, Q21–Q27, Q39–Q43, Q74–Q89;
   - do not use older Maudsley rules where the 15th edition or regulator has changed them.

3. **Maudsley Deprescribing Guidelines 2024**
   - particularly Q43, Q80 and Q84;
   - useful for avoiding simplistic fixed tapers and for describing withdrawal safely.

4. **Current NICE topic guidance**
   - use selectively by domain rather than loading every guideline into every question;
   - current-verification packets already identify many of the exact relevant documents.

5. **Current official EMA/SmPC/EOF material**
   - mandatory when product-specific monitoring, restarting, pregnancy/reproductive restrictions, authorisation or contraindications are stated.

6. **Current specialist sleep source**
   - AASM / ICSD framework where needed for Q65–Q67;
   - do not invent criteria if the relevant specialist source is unavailable.

If a proprietary/local source is unavailable to Writer, do **not** pretend it was consulted. Use the existing verified repository packet instead and flag a blocking source gap only if the missing source is necessary to resolve a consequential discrepancy.

---

## 4. Conflict rules

When sources disagree:

1. For **diagnosis**, ICD-11 CDDR and DSM-5-TR control their own systems.
2. For **current treatment**, current major guidelines outrank old textbooks.
3. For **drug licensing / monitoring / contraindications**, current regulatory / SmPC material outranks textbooks.
4. For **Greek law**, current Greek official sources control.
5. For **exam-specific historical teaching**, Shorter Oxford / Greek exam provenance may be retained as an explicitly labelled exam or historical fact.
6. Never average incompatible recommendations.
7. If exam truth and current practice differ materially, show the distinction explicitly and briefly.

---

## 5. Required output corpus

Do not overwrite v3.

Create:

`oral/100-crucial-questions/answers/revision-v4-el/Q001.md` … `Q100.md`

Also create:

`oral/100-crucial-questions/internal/editorial/Greek-v4-source-use-ledger.md`

The ledger should record, per question or coherent question group:
- principal exam/base source used;
- current diagnostic source used where relevant;
- current treatment/regulatory source used where relevant;
- whether the v3 wording was retained, rewritten or structurally replaced;
- any unresolved source conflict.

Do not clutter the learner-facing answers with citations or production-language provenance.

---

## 6. Batch plan

Work in these domain-coherent batches. Complete each batch, self-QA it, commit it, then continue without waiting for founder approval.

1. **Q001–Q010** — assessment, risk, emergencies, consent/involuntary care
2. **Q011–Q019** — psychosis and schizophrenia
3. **Q020–Q027** — depression, bipolar disorder, perinatal psychiatry
4. **Q028–Q036** — anxiety, OCD, trauma, dissociation, FND
5. **Q037–Q044** — substance-use and behavioural addictions
6. **Q045–Q058** — delirium, dementia, neuropsychiatry, liaison
7. **Q059–Q073** — neurodevelopmental, eating, sleep, personality, sexual/gender topics
8. **Q074–Q083** — core psychopharmacology through lamotrigine
9. **Q084–Q089** — benzodiazepines/hypnotics, ADHD medication, reproductive psychopharmacology, emergencies, ECT
10. **Q090–Q100** — psychotherapies, neuroscience/genetics, evidence appraisal, Greek law/services

Suggested commit pattern:

`editorial v4 batch 01 Q001-Q010`
...
`editorial v4 batch 10 Q090-Q100`

---

## 7. Required learner-facing architecture

The model oral answer remains central, but the book must stop forcing operational information into prose.

### Recall axis

Mandatory in all 100 questions.

Target 5–7 short retrieval cues. Avoid mini-paragraphs and unexplained acronyms.

### Model oral answer

Should sound like a strong Greek specialist candidate speaking to an examiner.

Use prose for:
- clinical reasoning;
- sequencing;
- explanation;
- synthesis.

Do not turn the whole answer into bullets.

### Diagnostic criteria visibility rule

Whenever the manuscript says:
- `5/10`;
- `5/9`;
- `4/9`;
- `≥5 symptoms`;
- `2–3 / 4–5 / ≥6 criteria`;
- `3 of 12 signs`;
- or another named operational threshold,

the learner must be able to see what is being counted.

Use a compact checklist, bullets or table.

Do not reproduce every criterion in every disorder merely because a manual contains it; apply this rule when the answer itself invokes the denominator or operational set.

### Acronym rule

Every non-obvious acronym / instrument must be expanded at first use **within each question**, even if it appeared earlier in the book.

Examples that need local expansion when used:
- ANC;
- BEN;
- CIWA-Ar;
- BFCRS;
- BVC;
- DASA-IV;
- 4AT;
- CAM-ICU;
- ICDSC;
- MEED;
- PCL-R;
- comparable specialist scales/tools.

Acronym expansion must not become a mini-lecture. State the full name, then use the acronym normally.

### Named cluster rule

If the text says classical triad/tetrad/cluster, name the components immediately.

Example: Wernicke classical triad should not be referred to without the three elements being visible.

### Basic exam points

Mandatory in all 100 questions.

Target approximately 4–6 genuinely examinable facts. Use these for exact criteria, durations, thresholds, monitoring and classic distinctions. Do not repeat the model answer mechanically.

### Traps

Mandatory in all 100 questions.

Target approximately 4–6 plausible examiner traps. They should discriminate good candidates from superficially prepared ones.

### Examiner follow-ups

Optional. Keep only if they add a genuine likely viva probe rather than repeat the parent answer.

### Exam answer vs current practice

Use only for a real conflict or meaningful historical/current distinction. Do not add this section merely to narrate that modern practice is “more nuanced.”

### Tables/checklists

Use selectively where they reduce cognitive load, especially:
- criteria sets;
- diagnostic comparisons;
- treatment sequences;
- monitoring schedules;
- adverse-effect comparisons;
- toxicology/emergency discriminations.

---

## 8. Anti-AI-slop standard

The v4 corpus must not sound generated.

Aggressively remove repetitive constructions and meta-writing such as:
- repeated `όχι απλώς ... αλλά ...`;
- repeated `το βασικό είναι` / `το κρίσιμο σημείο είναι`;
- `η πρακτική απάντηση είναι επομένως`;
- `η συνοπτική απάντηση είναι επομένως`;
- repeated `δεν πρέπει να παρουσιάζεται ως ...`;
- closing paragraphs that merely restate the previous answer;
- writer-facing statements such as `σε μια γενική προφορική απάντηση δεν χρειάζεται να...`;
- hybrid Greek/English sentences when established Greek exists.

These expressions are not mechanically banned; the problem is generated cadence and editorial residue.

Prefer direct, specific clinical prose.

---

## 9. Fidelity gates

Do not silently change:
- diagnosis;
- symptom counts;
- duration thresholds;
- doses;
- serum concentrations;
- monitoring schedules;
- treatment sequence;
- recommendation strength;
- causal strength;
- licensing status;
- Greek law or article numbers.

When a source update genuinely requires a change from v3, record it in the source-use ledger and make the corrected v4 statement.

Preserve the distinction between:
- `may consider` and `recommend/offer`;
- `associated with/implicated` and `causes`;
- `discriminating` and `specific`;
- `additive` and `synergistic`.

---

## 10. Mandatory batch QA

After each batch check:

1. all expected Q files exist;
2. Recall Axis exists;
3. Model Oral Answer exists;
4. Basic Exam Points exists;
5. Traps exists;
6. non-obvious acronyms are locally expanded;
7. operational denominators have visible criteria where relevant;
8. named triads/tetrads have visible components;
9. no obvious hybrid-English prose remains;
10. no unsupported factual additions were introduced;
11. no recommendation-strength or causal-strength drift occurred;
12. current verification decisions were respected;
13. source conflicts are logged;
14. the answer reads naturally aloud.

---

## 11. Final whole-corpus QA

After Q100:

- confirm 100/100 Recall Axes;
- confirm 100/100 Model Oral Answers;
- confirm 100/100 Basic Exam Points;
- confirm 100/100 Traps;
- scan for unexplained acronyms;
- scan for operational X/Y counts without nearby criteria structures;
- scan for unnamed classical triads/tetrads;
- scan for excessive repeated AI-style constructions;
- scan for untranslated / unnecessary English residue;
- compare consequential numbers, doses, law numbers and monitoring against the verified source layer;
- review the source-use ledger for unresolved conflicts.

Create completion report:

`oral/100-crucial-questions/internal/editorial/Greek-v4-structural-editorial-completion.md`

Include:
- batch commit SHAs;
- 100/100 completion;
- structural section counts;
- diagnostic checklist/table count;
- acronym QA outcome;
- AI-language cleanup summary;
- source upgrades that changed v3 content;
- unresolved source conflicts;
- recommendation whether v4 is ready for final adjudication/PDF manufacture.

Do not build the PDF in this task.
Do not overwrite v3.
Do not promote v4 to production automatically.

Final status:

`GREEK_V4_WRITER_COMPLETE`
