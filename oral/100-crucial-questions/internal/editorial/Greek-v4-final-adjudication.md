# Greek v4 final adjudication

Date: 2026-08-21
Branch: `greek-v4-final`
Final learner-facing corpus: `oral/100-crucial-questions/answers/final-v4-el/Q001.md`–`Q100.md`

## Baseline and manuscript state

- Writer-complete baseline commit: `5df4981d6a8cba5be569c7944cc7421f4bd59526`.
- Byte-identical final-corpus seed: `cbfb8900275b3fc29d82de2beae74e8a83aefcb1` (`final v4 seed corpus from writer baseline`).
- Final learner-facing manuscript head before this report: `0abd6bfbbc9d772cc6472f6d9d429982f0544661`.
- The Writer corpus was preserved; all final adjudication changes were made only in `answers/final-v4-el/` on `greek-v4-final`.

## Final adjudication commits

- `5ca63598…` — first targeted adjudication corrections, including current Greek system wording and removal of internal verification/process language.
- `ecec57fa…` — perinatal/anxiety/trauma/dissociation Greek-language normalization.
- `ab6718f4…` — substance-use, delirium and cognitive-assessment language normalization.
- `01a4d49f…` — neuropsychiatry and psychopharmacology language normalization.
- `dde5a258…` — Q022 TRD access/wording adjudication.
- `3f70b392…` — Q023 bipolar wording normalization without altering DSM/ICD duration distinctions.
- `0abd6bfb…` — Q019 clozapine terminology cleanup; WBC retained as standard shorthand by editorial decision.

## Consequential current-practice adjudication

### Greek systems and law

- Q040 was corrected so that the current 2026 umbrella organisation is **ΕΟΠΑΕ**, rather than presenting ΟΚΑΝΑ as the current umbrella body.
- Q100 retains the current statutory architecture of the **Εθνικό Δίκτυο Υπηρεσιών Ψυχικής Υγείας (Ε.Δ.Υ.Ψ.Υ.)** and the seven **Περιφερειακά Δίκτυα Υπηρεσιών Ψυχικής Υγείας (Πε.Δ.Υ.Ψ.Υ.)**, while avoiding the claim that every legacy local term or arrangement has already disappeared in implementation.
- Q089 preserves the verified Greek informed-consent boundary: a capacitous adult ordinarily requires prior informed consent, and involuntary admission does not itself authorise ECT. No foreign substitute-consent mechanism was imported. A distinct Greek ECT-specific court/prosecutor/second-opinion pathway for incapacity or urgent non-consensual ECT was not established from authoritative material, so the final answer does not invent one.
- Q098 retains the Greek confidentiality framework without creating a general Greek Tarasoff-style duty that was not established.

### Regulatory/current-treatment checks

- EU authorisation and indication statements were checked for the current newer agents/interventions carried into the manuscript, including lecanemab, donanemab, zuranolone and deutetrabenazine.
- European authorisation is not treated as proof of routine Greek availability, reimbursement or local formulary access.
- Q022 preserves the distinction between EU authorisation of intranasal esketamine and Greek routine access/reimbursement.
- Q047 preserves the restricted early-Alzheimer anti-amyloid framework and ARIA/MRI safety logic without presenting these agents as treatment for all Alzheimer disease.
- Q019 preserves the current European ANC-based clozapine monitoring architecture, clinically important myocarditis/gastrointestinal hypomotility risks, smoking/infection CYP1A2 effects, TDM use and >48-hour restart rule.

## Structural QA

Final-corpus requirements remain intact across Q001–Q100:

- question heading;
- `## Άξονας ανάκλησης`;
- `## Πρότυπη προφορική απάντηση`;
- `## Βασικά σημεία για τις εξετάσεις`;
- `## Συχνές παγίδες / παγίδες εξεταστή`;
- assigned examiner follow-ups and exam/current distinctions where relevant.

The final directory is intended to contain exactly the 100 learner-facing question files Q001–Q100. Each main question remains a separate Markdown file, preserving the downstream one-question/new-page packaging model.

## Diagnostic and high-yield operational QA

Explicit operational structures were preserved where they materially aid board recall, including:

- Q010: catatonia DSM symptom denominator;
- Q012: separate DSM-5-TR and ICD-11 schizophrenia operational structures;
- Q013: schizoaffective DSM/ICD comparison;
- Q020: ICD-11 depressive-episode symptom structure;
- Q023: DSM mania/hypomania durations explicitly separated from ICD-11 wording;
- Q045: delirium detection-tool roles;
- Q048: four current DLB core clinical features and the operational one-year DLB/PDD rule;
- Q059: ADHD developmental-onset anchor;
- Q063: MEED-based eating-disorder medical-risk framing;
- Q068: current ICD-11 dimensional personality architecture.

## Acronym and terminology QA

Non-obvious specialist scales/tools and technical targets are expanded locally where needed. Final adjudication specifically corrected missed expansions or overly hybrid wording around COWS, MCI/APOE/AChE, VMAT2 and other specialist terminology. Standard psychiatry/medicine abbreviations and internationally conventional labels may remain where they improve retrieval (for example DSM, ICD, EEG, MRI, SSRI, ANC, WBC, TDM, CYP1A2).

## Greek-language QA

A whole-corpus editorial sweep identified residual sentence-level Greek/English hybrid prose in the Writer-complete manuscript. These were normalized in the final branch while preserving clinical content, thresholds and treatment sequencing. English remains only where it functions as a conventional technical name, acronym, drug name, validated instrument name or useful parenthetical original term.

Internal production language such as references to briefs, source packets, verification workflow or "documented here" was removed from learner-facing prose. Where uncertainty is itself clinically important, it is expressed as a bounded clinical/legal statement rather than as a production note.

## Material source upgrades retained from v4

The final corpus preserves the major contemporary upgrades introduced during the v4 evidence/editorial pipeline, including:

- Greek informed-consent and involuntary-admission law;
- DSM-5-TR/ICD-11 psychosis distinctions;
- current European clozapine ANC monitoring;
- ICD-11 depressive-episode structure;
- reproductive valproate restrictions;
- panic disorder/agoraphobia separation;
- ICD-11 acute stress reaction and PTSD/CPTSD architecture;
- positive rule-in framing for functional neurological disorder;
- tobacco/CYP1A2 and opioid-use-disorder/naloxone updates;
- 4AT-era delirium practice;
- current anti-amyloid treatment/ARIA distinctions;
- DLB RBD core-feature and one-year-rule framing;
- ADHD onset before age 12;
- MEED eating-disorder medical-risk framework;
- ICD-11 dimensional personality disorder;
- current psychopharmacology monitoring/interactions across Q074–Q089;
- current Greek confidentiality, criminal-responsibility and community-service frameworks.

## Deliberately unresolved or bounded points

These are not Writer/final-stage blockers because the manuscript does not fabricate a resolution:

1. A distinct current Greek ECT-specific authorisation procedure for a patient lacking decision-making capacity or urgent non-consensual ECT was not established from authoritative material. The final answer states the verified legal boundary and avoids importing UK rules.
2. Routine Greek availability/reimbursement is not inferred solely from EU licensing for newer medicines/interventions where local access was not established.
3. Greek national availability/protocol status is not asserted for alternative parenteral behavioural-emergency agents where a uniform current national position was not established.
4. Current Greek community-service legislation is presented at the statutory top-level architecture without assuming that all local implementation and legacy terminology have already converged.

## Final adjudication conclusion

The Greek v4 corpus is clinically and editorially suitable to become the authoritative learner-facing source for downstream publication/layout work. No known unresolved item requires fabrication or further manuscript rewriting. Future legal/regulatory changes should be handled as dated maintenance updates rather than by reopening this completed editorial pass.
