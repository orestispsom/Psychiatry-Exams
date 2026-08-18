# Attempt 010 — Adult Psychiatry Board-Sufficiency Audit

Status: internal review. No question-bank changes made by this audit.

## Executive conclusion

Attempt 010 is close to a defensible **oral-viva sufficiency set** for the Greek Adult Psychiatry specialist examination. Its strongest feature is that the high-risk/high-frequency adult domains are represented repeatedly and from several angles: psychosis, mood disorders, suicide/risk, delirium/neurocognitive disorders, psychopharmacology, ECT, substance use, old-age/neuropsychiatry, psychotherapy, Greek law/ethics and foundational science.

However, the stronger project goal — that mastery of the 100 questions should probably suffice for the **whole board-certification examination**, including the written MCQ component — is not yet secured by question selection alone. The remaining weakness is mainly an **answer-architecture problem**, not a missing-100-topics problem. A candidate can give an excellent 2–5 minute oral answer while still missing exact diagnostic durations, classic examiner distinctions, key numerical/monitoring anchors, individual-drug facts and legacy/current classification points that can be tested directly in MCQs or short oral probes.

Therefore: **do not substantially reallocate the 100 mains yet. Build a verified board-fact/exam-anchor layer underneath them, and make a small number of visible/follow-up corrections where the current prompt does not naturally protect high-yield Greek oral material.**

## Sources used for this audit

- `attempts/010.md`
- `internal/core-coverage.yml`
- `internal/adult-board-scope.yml`
- `internal/attempt-maps/010.yml`
- `internal/answer-coverage/010.yml`
- `orestispsom/Psych/src/data/oral.js` — curated probability-weighted Greek oral-topic bank
- `orestispsom/Psych/src/data/oralCore.js` — secondary source for viva cadence and challenge structure
- `orestispsom/Psych/ORAL_QUALITY_AUDIT.md` — confirms all 129 curated oral answers and their topic distribution
- `orestispsom/Psych/MCQ_QUALITY_AUDIT.md` — confirms broad MCQ-bank content and typical precision requirements
- `orestispsom/Psych/src/data/sos.js` — high-yield exact criteria/duration/monitoring anchors; must be re-verified before final answer use
- `orestispsom/Psych/src/data/highYieldPsychiatryTables.js` — secondary gap/recognition check

## 1. Sufficiency strengths

### A. Core adult clinical psychiatry is heavily protected

A candidate mastering 010 should be difficult to expose on the major adult-board domains:

- psychosis/FEP/schizophrenia/TRS/clozapine;
- depression, bipolar disorder, mania, TRD and perinatal psychiatry;
- suicide, violence, agitation, catatonia and emergency syndromes;
- panic, GAD, social anxiety, OCD, PTSD and functional/somatic presentations;
- alcohol, opioids, cannabis, stimulants and benzodiazepine dependence;
- delirium, dementia, BPSD, Parkinson psychiatry, epilepsy, liaison and old-age presentations;
- adult ADHD, adult autism and intellectual disability;
- eating disorders and sleep;
- personality disorders;
- antipsychotics, antidepressants, lithium, valproate, lamotrigine, benzodiazepines, pregnancy psychopharmacology, NMS/serotonin syndrome, overdose and ECT;
- CBT, psychodynamic concepts, IPT and psychoeducation;
- Greek involuntary care, consent, confidentiality and forensic psychiatry.

This is consistent with the current curated Greek oral bank, whose strongest repeated areas include schizophrenia/psychoses, delirium, mood/suicide, psychopharmacology, anxiety/trauma, substances, neurocognitive/Parkinson syndromes, biological treatments, psychotherapy/ethics, sleep, autism, genetics and personality disorders.

### B. Examiner-style Greek probes are now unusually well represented

010 explicitly protects several themes that would be easy to miss in a generic textbook-derived list but are present in the Greek oral material:

- DUP/prognosis/negative symptoms and cognition in schizophrenia;
- clozapine;
- apathy versus depression;
- Charles Bonnet syndrome;
- Parkinson psychosis and dopamine-agonist behavioural syndromes;
- sleep stages/EEG and depression-related sleep changes;
- psychotropic interactions;
- psychoeducation;
- Greek involuntary care/confidentiality/forensic framing.

### C. Adult scope is now appropriate

Removing general child assessment, ODD/conduct disorder, adolescent depression and Tourette from dedicated main slots was correct for this project. Adult ADHD/autism/intellectual disability retain developmental history where diagnostically necessary without turning the guide into a Child and Adolescent Psychiatry syllabus.

## 2. Board-sufficiency vulnerabilities that could still expose a candidate

### A — High priority: exact diagnostic and factual anchors are not yet systematically bound to the 100

This is the largest remaining architectural weakness.

The Greek oral and MCQ banks contain direct questions on exact or semi-exact facts such as:

- schizophrenia duration/classification distinctions and historical first-rank symptoms;
- brief psychotic/schizophreniform timing;
- mania/hypomania and depressive-episode duration;
- ASD/PTSD/adjustment timing;
- ADHD onset/symptom thresholds;
- bulimia/BED frequency thresholds;
- lithium levels, sampling timing, toxicity and monitoring;
- valproate levels/risk;
- lamotrigine titration/interactions;
- clozapine interruption, blood monitoring and key thresholds;
- sleep EEG characteristics;
- NNT and diagnostic-test metrics.

`core-coverage.yml` deliberately avoids exact numbers, which is correct. But the sufficiency goal requires a second layer.

**Recommendation:** create `internal/board-fact-anchors.yml`, mapped to stable coverage IDs and/or the current attempt, containing only high-value recall facts that are plausibly board-tested. These facts must be source-tagged and re-verified before final publication. This should not become an encyclopedia.

### A — High priority: suicide knowledge is slightly too narrow in visible 010

Q4 tests suicidal intent/immediate risk. Q5 tests recurrence prevention after an attempt. The curated Greek oral bank also directly asks:

- major suicide risk factors;
- sex differences in suicidality;
- differences in suicide risk/profile across schizophrenia and depression.

A candidate could master Q4 and Q5 as currently worded while still not rehearsing these direct factual probes.

**Recommendation:** preserve Q4/Q5 separation, but add one genuine follow-up under Q5 such as:

`Which factors most strongly increase suicide risk, and how does risk differ across major psychiatric disorders?`

Sex/age patterns can remain hidden answer/fact-anchor coverage rather than another visible follow-up.

### A — High priority: individual psychopharmacology facts need deliberate protection

The current psychopharmacology main-question allocation is strong, but the Greek oral bank asks highly specific subtopics: trazodone mechanism/priapism, SSRI differences, hyponatraemia, CYP/interactions, lithium toxicity/dialysis, clozapine practicalities, etc.

A broad answer to “choose an antidepressant” or “major antidepressant adverse effects” does not necessarily force recall of these exam probes.

**Recommendation:** do not create more psychopharmacology mains. Instead, the board-fact layer and answer coverage should explicitly assign a small set of exemplar-drug facts to Q75/Q79/Q80/Q81/Q82/Q83/Q89.

### A — High priority: adult safeguarding / domestic violence must not disappear

The Adult Psychiatry scope correctly removed child safeguarding as a dedicated child-psychiatry main. But an adult psychiatrist still needs competence when:

- an adult patient has dependent children;
- domestic/intimate-partner violence is disclosed;
- perinatal illness creates infant risk;
- confidentiality competes with safeguarding duties.

`risk.intimate_partner_violence` is still only a candidate, despite meeting the project's meaningful-gap test.

**Recommendation:** promote intimate-partner/domestic violence to canonical `IMPORTANT` coverage, without adding a main question. Protect it across Q1/Q4/Q6/Q27/Q98 answer coverage. Protect child/dependent safeguarding similarly under Q27/Q98 and relevant adult-risk answers.

## 3. Medium-priority gaps: answer coverage rather than new mains

These areas can still be tested directly but do not justify disturbing the 100-slot allocation:

- Schneider first-rank symptoms and current/historical DSM–ICD classification distinctions;
- brief psychotic and delusional disorders within psychosis differential;
- mixed features and rapid cycling in bipolar disorder;
- sex differences, cognition and physical-health mortality in schizophrenia;
- LAIs, adherence and expressed emotion/family intervention;
- melancholic, atypical, psychotic, seasonal and persistent depressive patterns;
- specific phobia/performance anxiety;
- BDD, trichotillomania and excoriation disorder;
- complex PTSD/prolonged grief at overview level;
- toxicology-test interpretation and stimulant mechanisms;
- pseudodementia/depression versus neurocognitive disorder;
- NREM parasomnias, sleep architecture and melatonin/phototherapy principles;
- paranoid, schizoid, dependent and OCPD patterns;
- defence mechanisms and psychodynamic formulation;
- antipsychotic class/mechanism distinctions and representative receptor profiles;
- carbamazepine;
- other psychotropic overdoses;
- NNT/NNH and diagnostic-test metrics;
- current Greek professional/safeguarding duties.

The correct response is **not** 20 more follow-ups. These should be distributed through hidden answer specifications and the board-fact layer.

## 4. Main-question allocation challenge

No main question currently looks so wasteful that it must be removed to make the set pass-sufficient.

The lower-yield or more debatable mains are:

- autoimmune encephalitis;
- TBI psychiatric sequelae;
- gender dysphoria;
- paraphilic disorder.

However, each represents legitimate specialist knowledge, and there is currently no clearly missing adult CORE domain that should replace one of them. Charles Bonnet syndrome is formally SUPPORTING in the canonical bank but has direct Greek oral-bank support, so its visible promotion is justified by the exam-specific hierarchy.

Therefore the default should be **slot freeze** unless a future Greek-exam source identifies a materially stronger missing adult topic.

## 5. Internal-logic issue discovered

Q57 (apathy versus depression) is now a visible adult-board question with direct Greek oral support, but there is no dedicated stable canonical coverage ID for apathy. It is currently mapped indirectly to `depression.mdd` and `neuroscience.neuroanatomy`.

That is conceptually untidy and makes future audits less reliable.

**Recommendation:** add a compact canonical unit such as `neuropsychiatry.apathy` (IMPORTANT), covering:

- reduced motivation/goal-directed behaviour;
- distinction from depressed mood/anhedonia, negative symptoms and medication effects;
- frontal-subcortical/neurodegenerative contexts;
- treatment directed at underlying cause.

## 6. Oral sufficiency versus whole-exam sufficiency

### Oral viva

If the eventual answers are genuinely senior-resident level, include the hidden answer-coverage requirements, and the candidate can handle the visible follow-ups, Attempt 010 is **probably close to sufficient as a core oral-preparation set**.

### Whole certification exam (oral + MCQ)

The same 100 can plausibly serve as the core preparation set, but only if each answer package contains more than the spoken model answer. It should eventually have four layers:

1. **Oral core** — coherent 2–5 minute answer.
2. **Must-not-miss clinical coverage** — differentials, red flags, sequencing, monitoring, special situations.
3. **Board-fact anchors** — exact criteria/durations/key numbers/classic distinctions/specific high-yield drug facts.
4. **Examiner pivots** — a small number of genuine follow-ups/scenarios.

This architecture allows the learner to memorise/understand 100 coherent topics while still being protected against MCQ precision and short factual viva probes.

## 7. Recommended next actions before writing model answers

### Strongly recommended

1. Keep the 100 main slots provisionally frozen.
2. Add one suicide-risk-factor/disorder-pattern follow-up or equivalent explicit answer requirement.
3. Create a compact verified `board-fact-anchors.yml` sourced initially from the Greek oral bank + SOS/MCQ material, with current verification gates.
4. Promote `risk.intimate_partner_violence` to canonical IMPORTANT answer coverage, not a main.
5. Add `neuropsychiatry.apathy` as a stable canonical IMPORTANT unit.
6. Audit every 010 question against the Greek 129-question bank and mark each old oral item as `COVERED_DIRECTLY`, `COVERED_WITHIN_ANSWER`, `FACT_ANCHOR`, or `LOWER_PRIORITY_NOT_FORCED`.

### Not recommended

- another wholesale rewrite of the 100;
- adding dozens of visible follow-ups;
- expanding the canonical bank into textbook-level completeness;
- assuming that a polished oral answer automatically covers MCQ-level factual precision.

## Final judgement

**Attempt 010 is very close to the right 100-question architecture for Greek Adult Psychiatry.**

The residual risk is no longer primarily “we forgot a major psychiatric section.” The residual risk is that the eventual answers could be too elegant and conceptual, leaving the candidate vulnerable to the exact, old-school, drug-specific and criterion-specific questions that Greek oral and MCQ materials demonstrably contain.

The next engineering problem is therefore to make the **100 answers deep enough to be board-sufficient without making the visible 100 questions bloated.**