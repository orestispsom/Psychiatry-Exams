# Greek v4 structural/editorial completion

Status: **WRITER COMPLETE — READY FOR FINAL ADJUDICATION**

Corpus: `oral/100-crucial-questions/answers/revision-v4-el/Q001.md` … `Q100.md`

This report closes the Greek v4 Writer task. It does **not** promote v4 to production and does **not** build the PDF.

## 1. Batch commit lineage

1. Q001–Q010 — `7a0201e7359fa2002ae48efa27e5198db85a9d00`
2. Q011–Q019 — `8218e59341119e70eb4797e110f619270c032c2b`
3. Q020–Q027 — `d062114a134d44873bc82a895356d3c650846fbe`
4. Q028–Q036 — `6dcc32a8acafa29e377da1b1f754c0b16abd0711`
5. Q037–Q044 — `ca78337c2d08ba6454630d544838643e4a8e7a7b`
6. Q045–Q058 — `1864b65a46f7494009fa6de6fca0cbf38bdf3d05`
7. Q059–Q073 — `829c436b415fe3ac5a7a3957bcd23e7ef210e7ce`
8. Q074–Q083 — `cc96ccd30d708a21e14d9f20a41dda67c15f6a78`
9. Q084–Q089 — `8eb197dee9cf843b03b5bdb3aee77cd594abd849`
10. Q090–Q100 — `4ad68a9dbcb5ff7521d29ad0f95a46cc0fa22e75`

## 2. Final editorial/QA commits

- Q074–Q083 Greek-prose cleanup — `0af1437ed4dc7754a5f23b51abd0cdcec4279f8c`
- Q037–Q044 Greek-prose cleanup — `49e9b34eb6e40fc4b0c28b6f23d5dea5190289ea`
- Q045–Q058 Greek-prose cleanup — `e613f5bc649b1015f1cee278f608cd738d17aba4`
- Q059–Q073 first Greek-prose cleanup — `a243e6d090ed5b21ae2eb5e9de9c703b9eb42dc9`
- Q059–Q073 final acronym/instrument + Greek-prose pass — `b3c6bf7bf36b077b22aef4cc92835b8bae03f08c`
- Q084–Q100 final acronym + Greek-prose pass — `2beac384dced9a68c440c4452d2fb38a8f7e4a44`

Two transient repository-history commits created and immediately removed a temporary placeholder during tool switching; they make no surviving tree change and are not part of the manuscript or QA lineage.

## 3. Corpus completion

- Main question files present: **100/100**
- Recall Axis (`## Άξονας ανάκλησης`): **100/100**
- Model Oral Answer (`## Πρότυπη προφορική απάντηση`): **100/100**
- Basic Exam Points (`## Βασικά σημεία για τις εξετάσεις`): **100/100**
- Traps (`## Συχνές παγίδες / παγίδες εξεταστή`): **100/100**
- v3 overwritten: **0 files**
- v4 automatically promoted to production: **No**
- PDF built: **No**

## 4. Diagnostic criteria / operational visibility

Explicit diagnostic criteria/checklist/table structures added where the answer itself invokes an operational denominator: **4 principal structures**.

- Q010 — catatonia: the ≥3-sign threshold exposes the 12 signs being counted.
- Q012 — schizophrenia: DSM-5-TR 2/5 and ICD-11 2/7 sets are visible separately.
- Q013 — schizoaffective disorder: DSM-5-TR versus ICD-11 logic is separated in a compact comparison structure.
- Q020 — depressive episode: ICD-11 ≥5/10 exposes the 10 counted symptoms.

Other named clusters/triads are stated with their components when invoked rather than left as unexplained labels.

## 5. Acronym QA

Outcome: **PASS after final cleanup**.

Non-obvious instruments and specialist abbreviations are expanded locally at first use within their own question. High-value examples include BVC, DASA-IV, BFCRS, CIWA-Ar, 4AT, CAM-ICU, ICDSC, AQ, ADOS, CAT-Q, MEED, PSG, MSLT, RBD, PCL-R, CBT-I, CBT-ED, MANTRA, SSCM, DBT, MBT, PICO, NNT/NNH and PRS.

Standard diagnostic/manual abbreviations may remain after local contextual introduction where their meaning is clear. The final Q059–Q073 and Q084–Q100 passes specifically targeted remaining unexplained specialist abbreviations.

## 6. AI-language / Greek-language cleanup

Outcome: **PASS**.

The final corpus was edited to remove or reduce:

- sentence-level Greek/English hybrid prose when established Greek terminology exists;
- repeated generated constructions and redundant closing summaries;
- writer-facing or process-facing statements inside learner text;
- unexplained English instrument names/acronyms;
- unnecessary guideline/source narration.

International drug names, diagnostic-manual names and specialist test names are retained where they genuinely improve board retrieval, but they are embedded in natural Greek prose.

The later batches required additional cleanup because their first Writer pass retained excessive English syntax. Those defects were corrected in the QA commits listed above without reopening the approved factual briefs.

## 7. Major source upgrades that changed v3 content

The complete detail is recorded in `Greek-v4-source-use-ledger.md`. The most consequential upgrades are:

- Current Greek consent/involuntary-care law replaces imported UK framing where applicable.
- DSM-5-TR and ICD-11 diagnostic systems are separated rather than blended.
- Current ICD-11 operational schizophrenia and depressive-episode denominators are made visible.
- Current psychosis/TRS/clozapine sequencing and 2025 European clozapine monitoring are retained.
- Depression treatment is no longer represented as a rigid severity ladder; TRD is separated from pseudoresistance/DTD.
- Current bipolar I/II architecture, antidepressant-emergent episode logic and valproate reproductive restrictions are incorporated.
- Panic disorder/agoraphobia, GAD duration, PTSD/CPTSD, acute stress and FND are updated to current DSM/ICD distinctions.
- Wernicke treatment, OAT-centred opioid treatment, Greek naloxone access, stimulant beta-blocker nuance and individualized benzodiazepine tapering are updated.
- Delirium uses current 4AT/CAM-ICU/ICDSC roles; dementia material includes restricted anti-amyloid treatment and updated DLB/RBD architecture.
- ADHD onset, intellectual-disability severity, anorexia criteria, MEED/refeeding, ICD-11 dimensional personality classification and sexual/gender-health placement are updated.
- Psychopharmacology incorporates current lithium monitoring/targets, valproate reproductive rules, lamotrigine interactions, MAOI washouts and emergency toxicology anchors.
- Greek confidentiality/criminal-responsibility/service-organisation answers use current verified Greek legal/service architecture.

## 8. Unresolved source conflicts / bounded uncertainties

No unresolved point was filled by invention. Remaining items for final adjudication are:

1. **Greek ECT-specific authorization procedure:** the current official procedure when a patient lacks decision-making capacity or urgent non-consensual ECT is contemplated remains unverified. Q089 states the verified general consent principles and explicitly leaves the special procedure unresolved.
2. **Greek routine availability/reimbursement of selected newer medicines/interventions:** EU authorisation was not converted into a Greek access claim where access was not verified (examples include esketamine, zuranolone, deutetrabenazine and anti-amyloid treatments).
3. **Acute behavioural disturbance:** routine Greek national availability/protocol status of some alternative parenteral agents remains unresolved.
4. **Greek community mental-health reform:** the verified 2026 top-level Ε.Δ.Υ.Ψ.Υ./Πε.Δ.Υ.Ψ.Υ. architecture is stated, without claiming that every legacy local term or operational arrangement has disappeared.

These are adjudication items rather than Writer-stage reasons to fabricate or broaden claims.

## 9. Recommendation

**Proceed to final adjudication.**

The manuscript is structurally complete, source-enhanced and suitable to enter the final factual/editorial adjudication pass. PDF manufacture should occur **after** that adjudication, with particular attention to Q089’s unresolved Greek ECT authorization pathway and the bounded Greek-access caveats for newer treatments.

Writer status: `GREEK_V4_WRITER_COMPLETE`
