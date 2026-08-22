# Greek v5 pilot — Independent adjudication

Date: 2026-08-22
Branch: `greek-v5-pilot`
Scope: Q001, Q012, Q019, Q020, Q038, Q045, Q090, Q098 only.

The eight v5 pilot answers were read and provisionally graded before the Writer report was consulted. The Writer report was then used only as an audit trail. Scores below are the independent adjudicator's scores for the adjudicated files after the three minor wording corrections recorded below.

## 1. Executive decision

**SCALE_V5**

The pilot clears the quantitative and qualitative gate. Mean score is **95.4/100**, the lowest score is **93/100**, there is **no automatic factual fail**, no question retains a conspicuous AI-slop cap, and v5 is materially preferable to v4 overall. The main improvement is not extra content but better Greek-first retrieval architecture: operational criteria are visible where they matter, acronyms are locally expanded, emergency and legal sequences are easier to reconstruct, and the prose is less dependent on English-shaped shorthand.

Three learner-facing sentences required minor editorial correction. None changed a clinical, diagnostic, monitoring or legal claim.

## 2. Score table

| Q | Human-authored Greek /20 | Model oral answer /15 | Retrieval architecture /15 | Diagnostic/operational visibility /10 | Acronyms/instruments/technical terms /8 | Recall Axis /8 | Basic Exam Points /8 | Traps /8 | Follow-ups / exam-current /4 | Source fidelity /4 | Total /100 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Q001 | 18 | 14 | 14 | 9 | 8 | 8 | 7 | 8 | 4 | 4 | **94** |
| Q012 | 18 | 14 | 14 | 10 | 8 | 8 | 7 | 8 | 4 | 4 | **95** |
| Q019 | 17 | 13 | 15 | 10 | 8 | 8 | 8 | 8 | 4 | 4 | **95** |
| Q020 | 18 | 14 | 14 | 10 | 8 | 8 | 8 | 8 | 4 | 4 | **96** |
| Q038 | 18 | 14 | 15 | 10 | 8 | 8 | 8 | 8 | 4 | 4 | **97** |
| Q045 | 18 | 14 | 15 | 10 | 8 | 8 | 8 | 8 | 4 | 4 | **97** |
| Q090 | 18 | 14 | 13 | 9 | 8 | 8 | 7 | 8 | 4 | 4 | **93** |
| Q098 | 18 | 14 | 15 | 10 | 8 | 8 | 8 | 8 | 4 | 4 | **96** |

**Mean:** 95.4/100  
**Lowest:** 93/100 (Q090)  
**Acceptance gate:** **PASS** — mean ≥90; no question <86; no automatic factual fail; no conspicuous AI-slop cap; v5 materially preferable to v4 overall.

## 3. Per-question judgement

### Q001 — 94/100

**Disposition:** `ACCEPT_WITH_MINOR_EDITS`  
**v4 → v5:** `V5_MATERIALLY_BETTER`

**Strongest positive:** The answer now follows the actual clinical sequence — safety → history → collateral → MSE → physical/neurological assessment → risk/capacity → synthesis — and externalises the MSE domains into a usable recall structure. It also avoids making the old `4Ps` shorthand carry retrieval burden.

**Strongest defect:** The final sentence used the abstract/calqued `υποθεσιοκεντρική`, which is grammatically possible but not how an experienced Greek psychiatrist is likely to phrase the point orally.

**Edit made:** `Η εκτίμηση παραμένει υποθεσιοκεντρική...` → `Η αρχική διατύπωση είναι υπόθεση εργασίας...`.

**Automatic-fail check:** clear. No source-process language, denominator problem, unexplained specialist acronym, unsupported numerical/legal change, DSM/ICD blending, recommendation-strength drift or causal strengthening.

### Q012 — 95/100

**Disposition:** `ACCEPT_WITH_MINOR_EDITS`  
**v4 → v5:** `V5_SLIGHTLY_BETTER`

**Strongest positive:** Syndrome-first organisation is excellent, primary versus secondary negative symptoms are more clinically legible than in v4, and DSM-5-TR and ICD-11 are kept in separate operational blocks with each denominator adjacent to its counted items.

**Strongest defect:** The model answer briefly spoke about what the candidate should do `Για τις εξετάσεις`, rather than simply giving the answer. That is learner-facing exam meta-language inside text intended to be spoken.

**Edit made:** `Για τις εξετάσεις χρειάζεται να κρατώ χωριστά...` → `Τα δύο σύγχρονα συστήματα ταξινόμησης πρέπει να διακρίνονται καθαρά.`

**Automatic-fail check:** clear. Both central denominators have their component sets. DSM and ICD are not blended. The exact ICD-11 2/7 structure initially required a provenance check because `Q012.yml` cautions against making exact enumeration central without later verification; however, `Greek-v4-source-use-ledger.md` explicitly records the Q012 2/7 structure as adjudicated with no blocking conflict, and `Greek-v4-final-adjudication.md` confirms preservation of the separate operational structures. No `SOURCE_QUERY` is therefore required.

### Q019 — 95/100

**Disposition:** `ACCEPT`  
**v4 → v5:** `V5_MATERIALLY_BETTER`

**Strongest positive:** This is the strongest high-stakes medication architecture in the pilot: indication → ANC eligibility/monitoring → myocarditis/GI hypomotility → TDM/smoking/infection → interruption/restart. The ANC table and local expansion of ANC/TDM materially reduce retrieval friction versus v4.

**Strongest defect:** The spoken core is information-dense. A candidate who attempted to recite every monitoring and toxicity detail would run long; the table should function as retrieval support rather than material to verbalise line by line.

**Edit made:** none.

**Automatic-fail check:** clear. Start/stop ANC thresholds, the 2025 European schedule, ≥350 ng/mL exposure anchor and >2-day restart rule all match the approved Q011–Q019/current-verification layer. No unsupported dose, threshold or recommendation strengthening identified.

### Q020 — 96/100

**Disposition:** `ACCEPT_WITH_MINOR_EDITS`  
**v4 → v5:** `V5_SLIGHTLY_BETTER`

**Strongest positive:** The full current ICD-11 ten-item set is placed immediately after the 5/10 rule, suicidality and psychosis are prioritised before classification, and DSM terminology is explicitly kept separate. The PMDD/PME follow-up is concise and operational.

**Strongest defect:** The opening originally said `Στην εξέταση θέλω να δείξω...`, which is candidate meta-commentary rather than natural oral clinical reasoning.

**Edit made:** replaced that sentence with `Στην αξιολόγηση αποτυπώνω τη συνολική φαινομενολογία, τη βαρύτητα και τη διάρκεια και αποκλείω διπολικότητα ή δευτεροπαθή αιτία.`

**Automatic-fail check:** clear. The 5/10 denominator has all ten components. DSM/ICD terminology is separated. The two-cycle PMDD confirmation rule is explicitly supported by the approved Q020 brief and global current-verification ledger.

### Q038 — 97/100

**Disposition:** `ACCEPT`  
**v4 → v5:** `V5_MATERIALLY_BETTER`

**Strongest positive:** The emergency sequence is unusually good: severity/setting is decided before medication detail, CIWA-Ar is correctly demoted to an adjunct, and Wernicke recognition plus treatment are visible rather than buried in a follow-up. The full triad is named without requiring the full triad for diagnosis.

**Strongest defect:** There is unavoidable numerical density in the Wernicke subsection, but here the numbers are high-stakes and source-supported rather than decorative.

**Edit made:** none.

**Automatic-fail check:** clear. CIWA-Ar is expanded and its limitations are stated. The IV thiamine 300–500 mg three-times-daily 3–5-day regimen, continuation rule, magnesium point and no-delay-of-emergency-glucose wording match the approved source layer.

### Q045 — 97/100

**Disposition:** `ACCEPT`  
**v4 → v5:** `V5_MATERIALLY_BETTER`

**Strongest positive:** The answer makes the central syndrome, hypoactive subtype, cause search and treatment hierarchy immediately reconstructable. `4AT ≥4` is explicitly framed as possible delirium/cognitive impairment requiring clinical assessment, not a diagnosis.

**Strongest defect:** The antipsychotic paragraph is necessarily guideline-like and slightly less conversational than the opening, but the recommendation strength is appropriately bounded.

**Edit made:** none.

**Automatic-fail check:** clear. 4AT, CAM-ICU and ICDSC are locally expanded; tool roles are not conflated; haloperidol wording preserves the approved `consider only`/shortest-duration position and current Parkinson/DLB contraindication.

### Q090 — 93/100

**Disposition:** `ACCEPT`  
**v4 → v5:** `V5_SLIGHTLY_BETTER`

**Strongest positive:** Formulation and collaborative empiricism genuinely organise the answer; the technique examples are disorder-linked rather than presented as a generic psychotherapy catalogue. The retrieval spine is conceptually coherent.

**Strongest defect:** This remains the most expository answer in the pilot. It is natural enough to pass, but its middle paragraphs are denser and more polished than a typical spontaneous viva answer, and the retrieval architecture cannot be improved much further without making psychotherapy sound artificially algorithmic.

**Edit made:** none. Further compression would risk losing the formulation-first logic.

**Automatic-fail check:** clear. CBT and MBCT are expanded locally; no unsupported treatment hierarchy, causal claim or current-practice strengthening is introduced.

### Q098 — 96/100

**Disposition:** `ACCEPT`  
**v4 → v5:** `V5_MATERIALLY_BETTER`

**Strongest positive:** Greek law is genuinely the organising frame rather than a translated UK/US confidentiality answer. The disclosure table, minimum-necessary principle and Article 232/Tarasoff boundary make the legal reasoning substantially easier to retrieve than v4.

**Strongest defect:** Legal Greek is inevitably more formal than the rest of the pilot, and the candidate must resist reciting the table as a statute list. The model answer nevertheless remains clinically organised rather than bureaucratic.

**Edit made:** none.

**Automatic-fail check:** clear. Articles 13, 371 and 232 match the approved Greek-law layer. The answer does not invent a general Tarasoff duty and does not overstate direct victim warning. GDPR is expanded locally. No unsupported legal article or recommendation-strength change identified.

## 4. Cross-pilot language findings

### Greek strengths

- The v5 answers are composed primarily through Greek clinical syntax rather than English sentence skeletons with Greek vocabulary inserted.
- First-person clinical verbs (`ελέγχω`, `αναζητώ`, `εκτιμώ`, `κλείνω με σύνθεση`) work well when they express actual sequence rather than rhetorical performance.
- Technical English is mostly retained only where it has retrieval value: validated instrument names, international acronyms, `asociality`, CYP1A2, DSM/ICD labels.
- Lists and tables are used for things that are genuinely counted or operational; prose carries interpretation and prioritisation.

### Remaining calques / over-polish

- Abstract nominal formulations remain the main residual risk. `υποθεσιοκεντρική` in Q001 was the clearest example and was removed.
- Phrases that describe how to answer an exam rather than answering it can slip into the model oral answer. Q012 and Q020 each contained one such sentence and were corrected.
- High-stakes pharmacology and law naturally push the prose toward formal register. The solution is not colloquialisation; it is short clauses, explicit sequencing and avoidance of unnecessary nominalisations.

### AI-cadence patterns

No conspicuous repeated AI cadence remains. There is no corpus-wide dependence on `δεν είναι απλώς... αλλά...`, `όχι μόνο... αλλά...`, repeated three-part mini-conclusions or generic summary endings. Several answers still use contrastive sentences, but they are content-bearing and not mechanically repeated.

### Terminology

- Local acronym expansion is substantially better than v4, especially Q019, Q038 and Q045.
- DSM/ICD labels are used as system labels rather than blended Greek diagnostic shorthand.
- Historical terms (Schneider, old schizophrenia subtypes, ICD-10 depression hierarchy) are clearly marked as historical/exam material rather than current truth.

### Structural / retrieval findings

The main v5 gain is **externalisation of operational material**. Criteria, monitoring schedules, causes and named clusters are visible at the point of use. This is especially successful in Q012, Q019, Q020, Q038 and Q045. Q090 correctly remains more prose-driven because forcing a checklist architecture onto psychotherapy would reduce fidelity and oral naturalness.

## 5. Factual/source fidelity

**Consequential corrections made during adjudication:** none. The three learner-facing edits were wording-only.

**Source ambiguities resolved without new research:**

- **Q012 ICD-11 2/7 enumeration:** `Q012.yml` contains an earlier caution against central exact enumeration unless later verification existed. Later repository governance resolves this: `Greek-v4-source-use-ledger.md` explicitly records the 2/7 structure as adjudicated and states no blocking conflict, while `Greek-v4-final-adjudication.md` preserves the separate DSM/ICD operational structures. The v5 content therefore remains source-supported within the approved repository layer.

**SOURCE_QUERY:** **0**.

No unresolved consequential claim in the eight files requires guessing or a new broad research pass.

## 6. Scaling recommendation

**Recommendation: freeze the v5 doctrine for manufacture, with three small editorial rules made explicit. A second calibration pilot is not required.**

1. **Model oral answers must never narrate the exam-writing task.** Remove phrases such as `για τις εξετάσεις χρειάζεται...` or `στην εξέταση θέλω να δείξω...`; state the clinical distinction directly.
2. **Prefer ordinary Greek clinical phrasing over coined abstract compounds.** If a concept can be expressed as `υπόθεση εργασίας`, do not choose a more synthetic term such as `υποθεσιοκεντρική` merely for concision.
3. **Do not penalise necessary asymmetry.** Tables/lists belong where a denominator, monitoring schedule, emergency sequence or legal boundary must be retrieved; psychotherapy and formulation questions may remain more prose-led if forced symmetry would make them less natural.

These are refinements to the existing v5 doctrine, not a change of direction. The pilot demonstrates that Greek-first rewriting can materially improve naturalness, oral usability and retrieval without sacrificing the factual controls established in v4.