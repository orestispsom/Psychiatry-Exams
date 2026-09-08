# C1 Foundations — evidence verification log

Status: **REVIEWABLE DRAFT — verification support for Stage 1B manuscript**  
Verified: **2026-09-09**  
Governing outline: `C1-FOUNDATIONS-OUTLINE.md` on `main` after PR #7  
Source manuscript basis: *Master Psychopharm.pdf*, source PDF pp. 4–19 plus CYP/interactions material on pp. 514–515.

## Purpose

This file records the external checks used while rewriting C1. It is not a bibliography for every stable pharmacology statement. The source PDF remains the starting material, but claims that are regulatory, dose-specific, pharmacogenomic, interaction-sensitive, or otherwise consequential are checked against current authoritative sources before being carried forward.

The rewrite deliberately corrects or removes several absolute statements in the source rather than preserving them merely because they appeared in the PDF.

## Evidence hierarchy used

1. Current prescribing / regulatory information when a claim concerns licensed administration, contraindications, or interaction dose modification.
2. CPIC when a claim concerns interpretation of available pharmacogenetic results.
3. Consensus / specialty guidance for TDM.
4. Primary clinical pharmacology studies when an important practical rule is not expressed with sufficient precision in labeling.
5. Stable standard pharmacology for equations and receptor/signaling concepts.

---

## V1 — Ziprasidone food effect

**Manuscript use:** C1.1 and application case.

**Verified conclusion:** oral ziprasidone should be taken with food. FDA labeling states that food increases absorption up to approximately two-fold. A randomized crossover study found that a meal of **at least 500 kcal**, regardless of fat content, produced more reliable exposure; 250-kcal meals produced substantially lower exposure.

**Sources:**
- FDA / DailyMed-equivalent labeling: GEODON prescribing information, administration with food; absorption increased up to two-fold.
- Gandelman K et al. *J Clin Psychiatry*. 2009;70(1):58–62. PMID 19026256. https://pubmed.ncbi.nlm.nih.gov/19026256/

**Editorial correction from source:** retain the 500-kcal practical rule, but do not state that a fatty meal is required. Fat content was not the determinant in the crossover study.

---

## V2 — Lurasidone food requirement

**Manuscript use:** C1.1 and application case.

**Verified conclusion:** lurasidone should be taken with food containing **at least 350 kcal**; food substantially increases absorption.

**Source:** current DailyMed lurasidone labeling. https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=083a1a52-5a13-4e28-8ef2-127ac4ce5b2d

**Editorial correction from source:** keep the 350-kcal threshold as a label-level rule. Do not generalize it to other antipsychotics.

---

## V3 — Xanomeline/trospium (COBENFY) prandial rule

**Manuscript use:** C1.1 as an example of an exposure rule that can mimic non-response if ignored.

**Verified conclusion:** administer COBENFY **at least 1 hour before a meal or at least 2 hours after a meal**.

**Source:** current DailyMed COBENFY labeling. https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8f0e73bf-6025-44f6-ab64-0983322de0df

**Editorial correction from source:** use the label instruction rather than an unqualified statement that “food cuts trospium 70%.” The clinical instruction is what belongs in Foundations; quantitative component PK belongs in the drug profile if needed.

---

## V4 — Clozapine, tobacco smoke, CYP1A2, and inhibitor/inducer changes

**Manuscript use:** C1.10–C1.13.

**Verified conclusions:**
- Tobacco smoke is a CYP1A2 inducer and can reduce clozapine exposure.
- When a CYP1A2 inducer such as tobacco smoke is discontinued, clozapine exposure can rise; current labeling instructs clinicians to **consider reducing the clozapine dose** and monitor for adverse reactions.
- Current U.S. clozapine labeling specifies reducing clozapine to **one-third of the dose** when coadministered with a strong CYP1A2 inhibitor such as fluvoxamine or ciprofloxacin.
- The label does not support a universal fixed percentage reduction for smoking cessation; dose change should be individualized with clinical assessment and, where available, TDM.

**Source:** current DailyMed clozapine labeling, revised 4/2026. https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=883b5d43-0339-7dc1-f775-93791fb9b978

**Editorial corrections from source:**
- remove “levels double” as a universal law;
- remove a universal “reduce by 30–50%” directive from Foundations;
- retain the clinically crucial fact that **combustion products, not nicotine itself, drive CYP1A2 induction**;
- place exact clozapine management in the clozapine monograph / interaction protocol, with Foundations teaching the mechanism.

---

## V5 — Lurasidone and CYP3A4

**Manuscript use:** C1.10–C1.13.

**Verified conclusions:**
- Concomitant use of lurasidone with a **strong CYP3A4 inhibitor** is contraindicated / should not be used.
- Concomitant use with a **strong CYP3A4 inducer** is also contraindicated / should not be used.
- With a moderate CYP3A4 inhibitor, labeling gives a dose-reduction strategy.

**Source:** current DailyMed lurasidone labeling. https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=083a1a52-5a13-4e28-8ef2-127ac4ce5b2d

**Editorial use:** this becomes the cleanest C1 example of why “substrate + strong inhibitor/inducer” must be recognized before titrating a psychiatric drug.

---

## V6 — CPIC serotonin-reuptake inhibitor pharmacogenomics

**Manuscript use:** C1.11.

**Verified conclusions:**
- CPIC 2023 gives CYP2C19-guided recommendations for citalopram, escitalopram, and sertraline, and CYP2D6-guided recommendations for selected other SRIs.
- For **CYP2C19 poor metabolizers** taking citalopram/escitalopram, CPIC recommends considering an alternative not predominantly metabolized by CYP2C19 or, if used, a lower starting dose, slower titration, and approximately **50% lower maintenance dose** than in normal metabolizers. For citalopram, FDA labeling limits the adult dose to 20 mg/day in CYP2C19 poor metabolizers because of QT risk.
- For **sertraline CYP2C19 poor metabolizers**, CPIC similarly supports a lower start, slower titration, and approximately 50% lower standard maintenance dose, or an appropriate alternative.
- For **sertraline CYP2C19 ultrarapid/rapid metabolizers**, CPIC does **not** recommend a routine dose increase at initiation.
- CPIC explicitly distinguishes actionable metabolism genes from pharmacodynamic genes for which evidence does not support clinical prescribing use (e.g. SLC6A4 and HTR2A in this guideline).

**Source:** Bousman CA et al. CPIC guideline for serotonin reuptake inhibitor antidepressants. *Clin Pharmacol Ther*. 2023;114(1):51–68. https://files.cpicpgx.org/data/guideline/publication/serotonin_reuptake_inhibitor_antidepressants/2023/37032427.pdf

**Editorial correction from source:** delete the source PDF’s blanket “CYP2D6 poor metabolizer = reduce all drugs by 50–75%” model. PGx recommendations are **drug- and pathway-specific**.

---

## V7 — CPIC tricyclic antidepressants

**Manuscript use:** C1.11 as an example; exact TCA instructions are deferred to C3.

**Verified conclusion:** CPIC provides genotype-guided TCA selection/dosing recommendations for CYP2D6 and CYP2C19. These are drug/class specific and are strengthened by TDM rather than reducible to a universal phenotype percentage rule.

**Source:** Hicks JK et al. CPIC guideline for CYP2D6/CYP2C19 and TCAs, 2016 update. *Clin Pharmacol Ther*. 2017;102(1):37–44. https://files.cpicpgx.org/data/guideline/publication/TCA/2016/TCA_2016.pdf

---

## V8 — HLA-B*15:02 / HLA-A*31:01 with carbamazepine and oxcarbazepine

**Manuscript use:** C1.11 and application case.

**Verified conclusions:**
- HLA-B*15:02 is strongly associated with carbamazepine- and oxcarbazepine-induced SJS/TEN.
- In a **carbamazepine-naïve HLA-B*15:02-positive** patient, CPIC recommends avoiding carbamazepine; for an **oxcarbazepine-naïve HLA-B*15:02-positive** patient, CPIC recommends not using oxcarbazepine.
- HLA-A*31:01 is associated with a broader range of carbamazepine hypersensitivity reactions. In a **carbamazepine-naïve HLA-A*31:01-positive** patient, CPIC recommends avoiding carbamazepine when alternatives are available.
- Allele frequencies vary by ancestry, but self-reported ethnicity alone is an imperfect proxy; genotype, when available, should drive interpretation.

**Source:** Phillips EJ et al. CPIC guideline for HLA genotype and carbamazepine/oxcarbazepine, 2017 update. https://files.cpicpgx.org/data/guideline/publication/carbamazepine/2017/CPIC_HLA_CBZ_OXC.pdf

**Editorial correction from source:** remove simplified “Asian screening” as the governing rule and replace it with a genotype-centered explanation plus local/regulatory testing guidance.

---

## V9 — Therapeutic drug monitoring (TDM)

**Manuscript use:** dedicated C1.4 page.

**Verified conclusion:** TDM is established for selected psychotropics and is especially useful for non-response, suspected nonadherence, adverse effects at usual doses, suspected interactions, and suspected pharmacokinetic abnormalities. Interpretation requires standardized sampling and clinical context.

**Source:** Hiemke C et al. Consensus Guidelines for Therapeutic Drug Monitoring in Neuropsychopharmacology: Update 2017. *Pharmacopsychiatry*. 2018. PMID 28910830. https://pubmed.ncbi.nlm.nih.gov/28910830/

**Editorial correction from source:** the phrase “never draw before five half-lives” is too absolute. Routine steady-state TDM usually aims for a stable concentration at a defined sampling time, but urgent toxicity, suspected overdose, adherence questions, and some dose-adjustment decisions may require earlier measurements.

---

## V10 — Lithium and dialyzability

**Manuscript use:** C1.3 only as a mechanistic example. Exact toxicity thresholds are moved out of Foundations.

**Verified conclusion:** lithium is highly dialyzable and intermittent hemodialysis is the preferred extracorporeal modality when EXTRIP criteria for severe poisoning are met. Thresholds depend on renal function and clinical status, not concentration alone.

**Source:** EXTRIP Workgroup lithium recommendations. https://www.extrip-workgroup.org/lithium

**Editorial correction from source:** delete the source PDF’s simplified rule “>4.0 mEq/L regardless of symptoms” and “>2.5 mEq/L with severe neurotoxicity” from C1. EXTRIP recommendations are more conditional. The full toxicity algorithm belongs in the lithium / toxicology sections.

---

## Stable foundational corrections applied without a dynamic guideline dependency

These are standard pharmacology corrections made while converting the source material into clinically defensible teaching text:

- **Five half-lives** represents ~96.9% approach to a new steady state (or elimination of the removable parent-drug amount) under simple first-order kinetics; it is not “complete washout.”
- The usual `t½ = 0.693 × Vd / CL` relation assumes first-order elimination and a simplified distribution model; it is not universally valid for nonlinear kinetics, multi-compartment behavior, depot formulations, or active metabolites.
- Oral bioavailability should be written with dose correction when oral and IV doses differ: `F = (AUC_oral × Dose_IV) / (AUC_IV × Dose_oral)`.
- `Vd = amount of drug in the body / plasma concentration`; `Dose/C0` is an IV-bolus approximation, not a universal definition.
- **Potency, affinity, efficacy, and clinical effectiveness are different constructs.** Milligram dose does not rank therapeutic effectiveness.
- Partial agonism cannot be safely taught as a universal fixed percentage of “full signaling.” Net effect depends on intrinsic efficacy, receptor density/reserve, endogenous agonist tone, concentration, and signaling context.
- Quaternary ammonium structure usually **reduces passive CNS penetration**; “100% excluded from the BBB” is an overstatement.
- BBB penetration is multi-determinant. There is no universal clinical rule that a CNS drug must have one specific logP or molecular-weight cutoff.
- Phase-II conjugation is not categorically “preserved” in every patient with cirrhosis. Organ impairment effects are pathway- and severity-dependent and belong in C7.
- CYP inhibition can emerge quickly; enzyme induction requires altered protein expression and generally develops/resolves more slowly. Exact onset/offset is inducer-, enzyme-, dose-, and patient-specific.
- CYP2D6 phenotype can be **phenoconverted** by strong inhibitors; genotype is not the sole determinant of functional exposure.
- The source’s “higher-dose mirtazapine is reliably less sedating” claim is not retained in C1 because the clinical dose–sedation relationship is insufficiently robust for a foundational law.
- The source’s mechanistic statements that antidepressant efficacy *requires* hippocampal neurogenesis, or that one BDNF/mTOR pathway fully explains response, are reframed as supported mechanistic models rather than established singular causes.

---

## Claims intentionally deferred to later chapters

The following may be clinically valid in context but are **not** frozen in C1 because they require drug-/indication-specific verification:

- D2 occupancy thresholds and pathway-specific antipsychotic effects → C2.
- Exact clozapine smoking-cessation dose adjustment and TDM strategy → C2 / C8.
- Ketamine/esketamine mechanistic and dosing detail → C3.
- Lithium TDM ranges, toxicity levels, and dialysis algorithm → C4 / C6 or C7 as finally structured.
- Lamotrigine–valproate and estrogen/UGT dose schedules → C4 / C7.
- Benzodiazepine receptor-subunit and tapering rules → C5 / C8.
- Buprenorphine induction / precipitated-withdrawal thresholds → C6 / C8.
- Renal/hepatic dose adjustments and “LOT” benzodiazepine decisions → C7.
- Hyperbolic tapering and receptor-discontinuity switch rules → C8.

## Evidence status

This verification log supports the **C1 manuscript draft only**. It does not validate later drug monographs or protocols. Any dynamic source cited here should be rechecked at publication QA if the final guide is released substantially later or if labeling/guidelines change.