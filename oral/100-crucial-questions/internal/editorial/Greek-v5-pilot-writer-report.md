# Greek v5 pilot — Writer report

Branch: `greek-v5-pilot`

Status: **WRITER COMPLETE — READY FOR INDEPENDENT ADJUDICATION**

This report covers only the eight defined Greek-first v5 pilot questions. It does not claim publication readiness.

## Completed files

1. `answers/revision-v5-pilot-el/Q001.md`
2. `answers/revision-v5-pilot-el/Q012.md`
3. `answers/revision-v5-pilot-el/Q019.md`
4. `answers/revision-v5-pilot-el/Q020.md`
5. `answers/revision-v5-pilot-el/Q038.md`
6. `answers/revision-v5-pilot-el/Q045.md`
7. `answers/revision-v5-pilot-el/Q090.md`
8. `answers/revision-v5-pilot-el/Q098.md`

Completion: **8/8**.

## Source layer used

All questions were checked against:

- `internal/revision/Q001-Q100-board-depth-current-verification.md`;
- the corresponding file in `answers/final-v4-el/` as a completeness backstop;
- `internal/editorial/Greek-v4-source-use-ledger.md`;
- `internal/editorial/Greek-v4-final-adjudication.md`;
- `internal/editorial/Greek-v5-pilot-scoring-rubric.md`.

Question-specific approved factual briefs:

| Question | Approved brief used |
|---|---|
| Q001 | `answers/briefs/Q001-Q010-batch.md` |
| Q012 | `answers/briefs/Q012.yml` |
| Q019 | `answers/briefs/Q011-Q019-batch.md` |
| Q020 | `answers/briefs/Q020-Q027-batch.md` |
| Q038 | `answers/briefs/Q037-Q044-batch.md` |
| Q045 | `answers/briefs/Q045-Q051-batch.md` |
| Q090 | `answers/briefs/Q090-Q100-batch.md` |
| Q098 | `answers/briefs/Q090-Q100-batch.md` |

No new broad research was performed.

## Structural changes from final v4

| Question | Main v5 structural change |
|---|---|
| Q001 | Rebuilt around the actual clinical sequence: urgency → history → collateral → mental state → physical/neurological assessment → risk/capacity → synthesis. The mental-state domains are now a visible checklist rather than embedded prose. |
| Q012 | Rewritten as a syndrome-first answer, then two separate operational blocks for DSM-5-TR and ICD-11. Primary/secondary negative symptoms and historical Schneider/subtype material are more clearly separated. |
| Q019 | Drug-sequencing answer reorganised around indication, ANC eligibility/monitoring, life-threatening toxicities, exposure modifiers and restart safety. The ANC schedule is now a compact table. |
| Q020 | Clinical depressive syndrome precedes classification. The current ICD-11 5/10 denominator is immediately followed by the full ten-item numbered set; DSM terminology is kept separate. |
| Q038 | Emergency sequence made explicit: recognition/severity → setting → benzodiazepine strategy → scale limitations → medical support → escalation. Wernicke is a defined emergency subsection with the triad stated and the current IV regimen visible. |
| Q045 | Delirium answer now centres attention/awareness and cause-finding. A brief cause-search checklist replaces a long cause paragraph; detection tools and antipsychotic limits are separated. |
| Q090 | Rewritten around formulation, collaborative empiricism and disorder-specific technique selection rather than a generic psychotherapy description. |
| Q098 | Greek statutory rule comes first. A rule/exception table makes lawful disclosure boundaries retrievable; the violence-threat section explicitly separates Article 232 reporting from any Tarasoff-style assumption. |

## Criteria, checklists and tables introduced

- **Q001:** visible mental-state examination checklist.
- **Q012:** numbered DSM-5-TR 2/5 set and numbered ICD-11 2/7 set, each adjacent to its denominator and duration rule.
- **Q019:** European ANC monitoring table; start and stop thresholds kept outside the table to avoid conflating routine monitoring with action thresholds.
- **Q020:** full numbered ICD-11 ten-symptom set immediately after the 5/10 rule.
- **Q038:** explicit Wernicke triad and ordered parenteral thiamine regimen.
- **Q045:** compact cause-search checklist; 4AT role and threshold separated from diagnosis.
- **Q090:** no table added; prose is more useful for formulation and therapeutic process, with techniques enumerated only where retrieval benefits.
- **Q098:** compact confidentiality rule/exception table.

## Acronyms, instruments and retained technical English

Local first-use expansion was checked within each question, including the Recall Axis where relevant.

- **Q019:** absolute neutrophil count (ANC); therapeutic drug monitoring (TDM). `CYP1A2` and `Duffy-null` retained as internationally conventional pharmacogenetic/pharmacokinetic technical terms.
- **Q020:** premenstrual dysphoric disorder (PMDD) expanded in the follow-up heading before subsequent abbreviation.
- **Q038:** Clinical Institute Withdrawal Assessment for Alcohol, Revised (CIWA-Ar), with Greek explanatory gloss.
- **Q045:** 4 ‘A’s Test (4AT); Confusion Assessment Method for the Intensive Care Unit (CAM-ICU); Intensive Care Delirium Screening Checklist (ICDSC).
- **Q090:** Cognitive Behavioral Therapy (CBT); Mindfulness-Based Cognitive Therapy (MBCT). English acronyms retained because they are the internationally recognised therapy labels.
- **Q098:** General Data Protection Regulation (GDPR). `Tarasoff` retained because it names the specific foreign legal doctrine that must not be imported into Greek law.
- **Q012:** `asociality` retained parenthetically once because it is a current negative-symptom consensus term; Greek wording carries the sentence.

## SOURCE_QUERY

**None.**

No consequential ambiguity required a new source query. Existing bounded uncertainties were preserved rather than expanded. In particular, Q098 retains the verified position that no general Greek Tarasoff-style duty was established and does not invent a universal direct-warning rule.

## Mandatory self-QA checklist

| Question | Natural Greek | AI cadence | Oral usability | Retrieval structure | Operational visibility | First-use expansion | Named clusters | Recall Axis | Board facts | Traps | Content drift |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Q001 | PASS | PASS | PASS | PASS | PASS | PASS | N/A | PASS | PASS | PASS | PASS |
| Q012 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| Q019 | PASS | PASS | PASS | PASS | PASS | PASS | N/A | PASS | PASS | PASS | PASS |
| Q020 | PASS | PASS | PASS | PASS | PASS | PASS | N/A | PASS | PASS | PASS | PASS |
| Q038 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| Q045 | PASS | PASS | PASS | PASS | PASS | PASS | N/A | PASS | PASS | PASS | PASS |
| Q090 | PASS | PASS | PASS | PASS | PASS | PASS | N/A | PASS | PASS | PASS | PASS |
| Q098 | PASS | PASS | PASS | PASS | PASS | PASS | N/A | PASS | PASS | PASS | PASS |

Specific anti-AI pass: repeated stock constructions such as `δεν είναι απλώς… αλλά…`, `όχι μόνο… αλλά…`, `η πρακτική απάντηση…` and generic concluding summaries were removed or avoided. No learner-facing source/workflow narration remains.

## Rubric self-scores

Columns follow the v5 rubric in order: human-authored Greek /20; model oral answer /15; retrieval architecture /15; operational visibility /10; acronyms/technical terms /8; Recall Axis /8; board facts /8; traps /8; follow-ups or exam/current handling /4; source fidelity /4.

| Question | Greek | Oral | Retrieval | Operational | Terms | Recall | Board | Traps | Follow-up | Fidelity | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Q001 | 18 | 14 | 14 | 9 | 8 | 8 | 7 | 7 | 4 | 4 | **93/100** |
| Q012 | 18 | 14 | 14 | 10 | 8 | 8 | 7 | 7 | 4 | 4 | **94/100** |
| Q019 | 18 | 14 | 15 | 10 | 8 | 8 | 8 | 7 | 4 | 4 | **96/100** |
| Q020 | 18 | 14 | 15 | 10 | 8 | 8 | 8 | 7 | 4 | 4 | **96/100** |
| Q038 | 18 | 14 | 14 | 10 | 8 | 8 | 7 | 8 | 4 | 4 | **95/100** |
| Q045 | 18 | 14 | 15 | 10 | 8 | 8 | 7 | 7 | 4 | 4 | **95/100** |
| Q090 | 19 | 15 | 13 | 9 | 8 | 8 | 7 | 7 | 4 | 4 | **94/100** |
| Q098 | 18 | 14 | 15 | 10 | 8 | 8 | 8 | 8 | 4 | 4 | **97/100** |

Mean self-score: **95.0/100**. Lowest question: **93/100**. No rubric category falls below the ≥8/10-equivalent threshold. No automatic factual fail or conspicuous AI-cadence cap was identified in the final self-pass.

## Readiness statement

The eight-question pilot is **ready for independent grading/adjudication** against `Greek-v5-pilot-scoring-rubric.md`. It is not declared publication-ready; independent adjudication and founder review remain the next gate.