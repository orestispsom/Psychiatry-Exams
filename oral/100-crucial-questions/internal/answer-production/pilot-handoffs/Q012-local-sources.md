# Q12 Local Source / Exam-Source Handoff — Schizophrenia Clinical Picture & Diagnosis

Status: READY_FOR_LOCAL_EXTRACTION
Pilot: 1 of 5
Question source: Attempt 011
Output destination: `oral/100-crucial-questions/answers/source-packets/Q012-local.md`

## Mission

Build the **exam-source and local-textbook packet** for:

> **Q12. Describe the clinical picture and diagnosis of schizophrenia.**

This is the local-source stream of the model-answer pipeline. Its first duty is to reconstruct what the prescribed **Shorter Oxford Textbook of Psychiatry, 7th edition / 2017 exam edition** expects a Greek Adult Psychiatry specialist candidate to know. It then uses the user's other local textbooks selectively to supplement, clarify or challenge that framing.

You are **not writing the model answer**.

## Local library

Expected local psychiatry library root:

`C:\Users\orest\OneDrive\Υπολογιστής\Ψυχιατρικη\Books`

Do not alter, rename, move or annotate source books.

If the exact Shorter Oxford 7th edition / 2017 exam source cannot be positively identified, stop and report `BLOCKED_EXAM_SOURCE_IDENTITY` rather than substituting another Oxford edition.

## Repository orientation — read these first

Read only the following project files before local textbook extraction:

1. `oral/100-crucial-questions/attempts/011.md` — Q12 is the target.
2. `oral/100-crucial-questions/internal/answer-coverage/007.yml` — Q12 inherited hidden coverage.
3. `oral/100-crucial-questions/internal/board-fact-anchors.yml` — Q12 board-fact anchors.
4. `oral/100-crucial-questions/reviews/010-greek-oral-129-mapping-audit.md` — Q12-related Greek oral priority only; do not use old oral answers as factual authority.
5. `oral/100-crucial-questions/internal/source-register.md`.
6. `oral/100-crucial-questions/internal/answer-production/README.md`.
7. `oral/100-crucial-questions/internal/answer-production/agent-prompts.md` — follow **B. Local Textbook / Exam-Source Agent**.

### Important independence rule

**Do not read `answers/source-packets/Q012-contemporary.md` yet.**

Complete the Oxford-first extraction and your initial targeted local-book synthesis before opening the contemporary packet. This protects independent exam-source reconstruction from anchoring on the modern research stream.

After the independent local extraction is complete, you may read `Q012-contemporary.md` for the final comparison phase described below.

## Required Q12 territory

Resolve the local-source basis for:

- characteristic clinical picture of schizophrenia;
- positive symptoms;
- negative symptoms;
- disorganisation and formal thought disorder;
- hallucinations/perceptual phenomena;
- cognitive symptoms/dysfunction;
- affective and psychomotor/catatonic phenomena insofar as relevant to the syndrome;
- diagnosis as a longitudinal clinical diagnosis rather than a cross-sectional psychosis label;
- diagnostic duration and functional requirements in the prescribed exam framework;
- required exclusions and major diagnostic boundaries, without turning Q12 into the separate Q13 differential question;
- Schneider first-rank symptoms: exact exam-source list/framing and their diagnostic importance in the prescribed textbook;
- historical schizophrenia subtypes and whether/how Oxford 2017 still discusses them;
- terminology or classic distinctions likely to be expected in a Greek oral examination.

Do **not** drift into acute treatment, maintenance, treatment resistance or clozapine except where a source passage is necessary to clarify diagnosis/phenomenology.

## Board-fact anchors to resolve locally

At minimum:

- `bf.psychosis.schneider_first_rank`
- `bf.psychosis.schizophrenia_dsm_icd`
- `bf.psychosis.duration_boundaries` insofar as it defines schizophrenia boundaries
- `bf.psychosis.cognitive_profile`

Also resolve the current Research GPT's explicit local dependency:

- **exact DSM-5-TR schizophrenia criteria** from the user's authorised local DSM-5-TR copy, including active-phase threshold, mandatory core symptoms, duration, functional impairment, mood exclusion, substance/medical exclusion and developmental-disorder clause.

Do not rely on memory for the DSM criterion set.

## Source order — mandatory

### PHASE 1 — Oxford Shorter 2017, blind extraction

Open **only the prescribed Shorter Oxford 7th / 2017 exam edition** initially.

Use TOC/index/search to identify all directly relevant sections. Read enough surrounding text to understand the actual teaching structure.

Record:

1. exact book identity/edition;
2. chapter and section titles;
3. printed page numbers; if useful, PDF page numbers separately;
4. Oxford's natural organisation of the clinical picture;
5. Oxford's diagnostic/classification framework;
6. terminology and classic distinctions;
7. first-rank symptoms and their status;
8. subtype language/classification;
9. cognitive/negative/disorganisation material;
10. facts likely to be directly examinable;
11. any statement that appears potentially edition-bound or dated — **without modernising it yet**.

Create an internal working note before reading any other source. This need not be committed separately, but the final packet must make clear which findings came from this blind Oxford phase.

### PHASE 2 — Local DSM-5-TR, targeted authoritative diagnostic extraction

Open the user's local DSM-5-TR.

Retrieve and verify the exact schizophrenia diagnostic criteria relevant to the board-fact layer. Record exact section/page references where recoverable.

Also note only those DSM-5-TR classification changes/material directly useful to Q12, such as current subtype handling and the status of historically privileged psychotic symptoms.

Do not turn this into a full schizophrenia-spectrum chapter summary.

### PHASE 3 — Targeted supplementary local textbooks

Open additional books **only when they answer an identified Q12 need**.

Preferred order for Q12:

1. **New Oxford Textbook of Psychiatry, 3rd ed. (2020)** — specialist-level modern phenomenology/classification depth.
2. **Kaplan & Sadock's Synopsis of Psychiatry (2021)** — classic descriptive psychopathology/exam distinctions if useful.
3. **Kaplan Comprehensive** — only if a material diagnostic/phenomenological issue remains unresolved after Shorter Oxford + New Oxford + Synopsis.
4. Other specialist books only if directly necessary.

For Q12, do not open Maudsley/Stahl merely because they are in the library; this is not a treatment/psychopharmacology question.

Stop supplementary searching when the local sources converge and no important Q12 issue remains unresolved.

### PHASE 4 — Contemporary packet comparison, only after Phases 1–3

Now read:

`oral/100-crucial-questions/answers/source-packets/Q012-contemporary.md`

Do **not** re-research the web.

Use it only to identify:

- convergence with Oxford/local sources;
- exam-source material that is historical or differently framed today;
- current material missing from Oxford 2017;
- explicit conflicts requiring later adjudication;
- contemporary claims whose exact wording/criterion can now be resolved from the local DSM-5-TR;
- remaining unresolved dependencies, especially anything requiring WHO ICD-11 primary text rather than a local book.

Do not adjudicate the final answer yourself. Report the conflict; the coordinator/adjudicator decides what is spoken as exam answer versus current-practice note.

## Q12-specific questions to answer

### A. Oxford examination framing

1. How does Oxford 2017 organise the syndrome clinically?
2. Which symptoms/signs receive the greatest diagnostic emphasis?
3. What does it say about positive, negative, disorganised, cognitive, affective and catatonic phenomena?
4. How does it describe formal thought disorder?
5. How does it describe hallucinations and delusional/passivity phenomena?
6. What does it say about Schneider first-rank symptoms and their specificity/status?
7. Which duration/functional/classification rules does it teach for schizophrenia?
8. Does it compare DSM and ICD explicitly? If so, record the exact exam-relevant differences it teaches.
9. Which historical subtypes does it retain/discuss, and in what role?
10. What would a candidate relying on Oxford 2017 likely be expected to volunteer orally?

### B. DSM-5-TR exact criteria

Resolve from the local authorised DSM-5-TR:

- exact active-phase symptom number/threshold;
- mandatory core symptom requirement;
- duration language;
- functional impairment requirement;
- mood/schizoaffective exclusion;
- substance/medical exclusion;
- autism/developmental-disorder clause;
- current subtype/specifier approach relevant to Q12.

Paraphrase in the packet unless a very short exact phrase is essential. Do not reproduce long copyrighted criterion text verbatim.

### C. Supplementary textbook value

For each supplementary source actually opened:

- what did it add beyond Oxford?
- did it materially change the proposed answer structure?
- did it clarify a classic examiner distinction?
- did it reveal that an Oxford 2017 framing is now historical/edition-specific?

### D. Comparison with current research

After independent extraction, compare against `Q012-contemporary.md` specifically for:

- DSM-5-TR criterion details unavailable to the Research GPT;
- ICD-10-era versus ICD-11-era schizophrenia framing;
- first-rank symptoms;
- classical subtypes;
- cognitive symptoms;
- formal thought disorder;
- functional impairment;
- duration boundaries;
- any modern dimensional terminology absent from Oxford 2017.

## Required deliverable

Create exactly:

`oral/100-crucial-questions/answers/source-packets/Q012-local.md`

Use this structure:

```markdown
# Q12 Local Source Packet — Schizophrenia Clinical Picture & Diagnosis

## 1. Source identities verified

## 2. Oxford Shorter 2017 — blind exam-source extraction
### Sections/pages inspected
### Oxford's answer architecture
### Clinical picture / psychopathology
### Diagnosis / classification
### Classic examination concepts
### Potentially edition-bound points

## 3. Local DSM-5-TR — exact diagnostic verification

## 4. Targeted supplementary local-textbook findings
### [Book actually opened]
- reason opened
- sections/pages
- material addition/clarification/conflict

## 5. Local-source comparison table
| Claim/topic | Oxford Shorter 2017 | DSM-5-TR / supplementary source | Relationship |

Relationship values:
- CONVERGENT
- MORE_DETAIL_ONLY
- DIFFERENT_FRAMING
- POSSIBLE_CONFLICT
- OUTDATED_EXAM_SOURCE_SIGNAL
- UNRESOLVED

## 6. Exam-source facts/terminology to preserve

## 7. Post-extraction comparison with contemporary packet
| Topic/claim | Local/exam-source finding | Contemporary packet finding | Adjudication issue |

## 8. Board-fact anchor trace
- anchor → local source/page → status

## 9. Sources actually inspected

## 10. Unresolved items / blocks

## 11. Extraction-efficiency report
- books opened
- books deliberately not opened
- searches/sections used
- where further reading would have had low marginal value
```

## Hard rules

- **Do not write the final model answer.**
- Oxford Shorter 2017 must be examined before any other textbook.
- Do not read the contemporary packet before completing Phases 1–3.
- Do not use web/general knowledge to correct or supplement local sources.
- Do not use old `Psych` oral answers as factual authority.
- Do not invent page numbers.
- Do not treat a keyword hit as support without reading surrounding context.
- Do not silently replace Oxford 2017 with DSM-5-TR/current knowledge; report differences explicitly.
- Do not mechanically read every book in the library.
- Do not open treatment-heavy psychopharmacology texts unless the diagnostic task genuinely requires them.
- Prefer native text extraction/search; OCR only if unavoidable.
- Keep this Adult Psychiatry focused.
- Do not modify any file except the specified output packet.

## Efficiency rule for scale

This pilot should be thorough enough to establish the method, but retrieval must model a workflow that can scale to 100 questions:

- use targeted TOC/index/text search, not linear reading;
- Oxford first, then only books with a stated information need;
- stop when sources converge;
- report low-yield books that were deliberately not opened;
- avoid duplicating material already securely established by Oxford/local DSM unless a comparison question requires it.

## Completion gate

Return `READY_FOR_ADJUDICATION` only if:

- Oxford Shorter 2017 identity is verified;
- relevant Oxford sections/pages were actually read;
- exact DSM-5-TR Q12 criteria were locally verified or explicitly blocked;
- every Q12 board-fact anchor has local-source evidence or a stated unresolved dependency;
- supplementary books were used selectively, not mechanically;
- the contemporary packet was consulted only after independent local extraction;
- all important exam/current differences are explicit;
- no final-answer prose was written;
- output file was committed and re-fetched/verified.
