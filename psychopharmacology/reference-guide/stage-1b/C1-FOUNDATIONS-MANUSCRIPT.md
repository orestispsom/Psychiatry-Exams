# C1 — Foundations & General Principles of Psychopharmacology

Status: **REVIEWABLE DRAFT — clinical/editorial content, not design-frozen**  
Working allocation: **13 pages**  
Hard editorial ceiling: **14 pages**  
Source basis: *Master Psychopharm.pdf*, source PDF pp. 4–19, with selected CYP/interactions material from pp. 514–515.  
Verification support: [`C1-EVIDENCE-LOG.md`](C1-EVIDENCE-LOG.md).

## Editorial purpose

This chapter is the reusable pharmacology layer for the rest of the guide. It should answer one question repeatedly:

**What pharmacological principle changes what I prescribe, how I dose it, what I monitor, or how I interpret an unexpected response?**

It is not a condensed neuroscience textbook. Detailed drug-specific thresholds, toxicity algorithms, switching schedules, and indication-specific receptor explanations belong in later chapters and should cross-reference this foundation rather than be repeated here.

---

# C1.1 — ADME, bioavailability, formulation and food

## The clinical sequence

A prescribed dose does not equal an effective exposure. Before calling a medication ineffective, separate the sequence:

**Dose administered → dose absorbed → systemic exposure → tissue/CNS exposure → target engagement → clinical effect.**

Failure at any upstream step can mimic pharmacodynamic treatment resistance.

## Absorption: how much gets in, and how fast

**Bioavailability (`F`)** is the fraction of an administered dose that reaches the systemic circulation unchanged. For an oral drug, incomplete absorption and first-pass metabolism can both reduce systemic exposure.

When oral and intravenous doses differ:

`F = (AUC_oral × Dose_IV) / (AUC_IV × Dose_oral)`

- **AUC** reflects total systemic exposure over time.
- **Cmax** is the observed peak concentration.
- **Tmax** is the time to that peak.

These variables answer different clinical questions. Two formulations can produce similar AUC but different Cmax/Tmax, changing onset, sedation, abuse liability, or peak-related adverse effects.

### Clinical rule

When apparent non-response is unexpected, check **administration conditions and formulation** before escalating the dose.

| Exposure problem | What it changes | Typical clinical consequence |
|---|---|---|
| Missed food requirement | Bioavailability | Apparent non-response / erratic exposure |
| Food must be avoided | Absorption or component exposure | Adverse effects or altered efficacy if taken incorrectly |
| Extended-release formulation altered/crushed | Release rate and Cmax | Peak toxicity or loss of intended duration |
| Malabsorption / severe GI disease | Fraction absorbed | Unpredictable exposure |
| Enzyme/transporter interaction in gut | Presystemic exposure | Higher or lower AUC before hepatic clearance is considered |

## Three psychopharmacology food rules worth remembering

These are examples of **administration-dependent exposure**, not universal class rules.

- **Ziprasidone:** take with food. A clinical pharmacology study found that a meal of at least **500 kcal** produced substantially more reliable exposure than fasting or a 250-kcal meal; fat content was not the determining factor. [V1]
- **Lurasidone:** take with food containing at least **350 kcal**; current labeling explicitly states that food substantially increases absorption. [V2]
- **Xanomeline/trospium (COBENFY):** administer at least **1 hour before** or **2 hours after** a meal. [V3]

The practical point is larger than memorizing three numbers: a drug can look ineffective because the **prescription is correct but the administration is pharmacokinetically wrong**.

## Distribution: where the drug goes after absorption

**Apparent volume of distribution (`Vd`)** relates the amount of drug in the body to its measured plasma concentration:

`Vd = amount of drug in body / plasma concentration`

A large Vd usually indicates extensive distribution outside the vascular compartment. It does not mean there is literally that volume of fluid in the body.

Distribution is influenced by:

- lipophilicity and tissue affinity;
- plasma-protein binding;
- ionization at physiological pH;
- tissue perfusion;
- transporter activity;
- body composition.

### Protein binding: avoid the displacement reflex

Only unbound drug is immediately available for diffusion, metabolism, and filtration. However, a transient rise in free fraction from protein-binding displacement does **not automatically produce sustained toxicity**: for many drugs, increased free drug is also cleared more rapidly until a new equilibrium is reached.

Protein binding matters most when combined with other factors such as:

- narrow therapeutic index;
- high extraction or altered clearance;
- severe hypoalbuminemia;
- renal failure with altered binding;
- nonlinear binding;
- a measured **total** concentration that no longer represents the active free concentration well.

Do not infer toxicity from “high protein binding” alone.

## Metabolism and elimination: preview

Systemic exposure falls through metabolism and excretion. The central quantitative relationship is:

`Clearance (CL) = volume of plasma effectively cleared of drug per unit time`

Total clearance is the sum of relevant routes, most often hepatic metabolism and renal excretion. The later C1 metabolism section separates CYP metabolism, conjugation, inhibition, induction, and pharmacogenomics.

### Bedside checkpoint

Before increasing a dose for apparent failure, ask:

1. Is the patient taking the intended formulation?
2. Are food requirements being followed?
3. Is absorption plausible?
4. Has an inhibitor or inducer changed exposure?
5. Has renal/hepatic function changed?
6. Is the measured concentration interpretable?
7. Only then: is target-level pharmacodynamic failure likely?

---

# C1.2 — Half-life, accumulation, loading and washout

## Half-life connects distribution and clearance

For drugs with approximately first-order elimination in a simplified one-compartment model:

`t½ = 0.693 × Vd / CL`

Half-life therefore becomes longer when distribution volume increases or clearance decreases. In real psychopharmacology, measured terminal half-life may also reflect multi-compartment redistribution, active metabolites, depot release, or nonlinear kinetics.

## The five-half-life heuristic — useful, not absolute

After a constant dosing regimen is started or changed, a first-order system approaches its new steady state exponentially:

| Elapsed half-lives | Approximate fraction of new steady state reached |
|---:|---:|
| 1 | 50% |
| 2 | 75% |
| 3 | 87.5% |
| 4 | 93.75% |
| 5 | 96.9% |

The same mathematics describes the decline of a parent drug after discontinuation under simple first-order conditions.

### Correct interpretation

**Five half-lives means “close to steady state / mostly eliminated,” not “complete washout.”** [stable correction]

The heuristic becomes unreliable when any of the following dominate:

- active metabolites with longer half-lives;
- nonlinear or saturable clearance;
- depot / long-acting formulations;
- enterohepatic recycling;
- irreversible or slowly reversible target effects;
- time-dependent enzyme induction/inhibition;
- organ failure changing clearance during the interval;
- very large tissue stores or multicompartment redistribution.

This distinction is critical in switching. Pharmacokinetic disappearance and pharmacodynamic recovery are not the same event.

## Loading dose versus maintenance dose

A **loading dose** is intended to achieve a target concentration more rapidly:

`Loading dose ≈ Target concentration × Vd / F`

A **maintenance dose** replaces drug eliminated during the dosing interval:

`Maintenance dose per interval ≈ Target concentration × CL × dosing interval / F`

These equations are conceptual tools, not automatic psychiatric prescriptions. They clarify why:

- loading dose depends mainly on **distribution**;
- maintenance requirement depends mainly on **clearance**;
- increasing the dose does not change the time constant of a linear first-order system;
- a loading dose can reach a plasma target quickly but does not accelerate every downstream receptor or clinical adaptation.

## Why “steady state” matters clinically

A concentration obtained before the regimen has approached steady state can be misleading if interpreted as though it were stable. The usual response to an unexpectedly low early level should not be reflexive dose escalation.

However, “wait five half-lives before measuring anything” is also wrong. Earlier measurement may be appropriate for:

- suspected toxicity or overdose;
- suspected nonadherence;
- a potentially dangerous interaction;
- renal/hepatic deterioration;
- a drug with a protocol-defined early level;
- urgent clinical deterioration in which concentration data may change management.

**Timing is part of the laboratory result.** A drug level without the dose, last-dose time, sampling time, formulation, and recent dose changes is incomplete information.

---

# C1.3 — Linear and nonlinear kinetics, clearance and dialyzability

## First-order kinetics: the usual model

With **first-order elimination**, a roughly constant fraction of the drug is eliminated per unit time across the clinically relevant range.

Consequences:

- half-life is approximately constant;
- exposure often changes proportionally with dose;
- doubling a maintenance dose tends to produce an approximately proportional change in steady-state concentration, if other variables remain stable.

This model is useful for many psychotropics, but it is a model rather than a guarantee.

## Capacity-limited kinetics: when dose and concentration separate

Enzymatic elimination can be described by Michaelis-Menten behavior:

`Rate of elimination = Vmax × C / (Km + C)`

At concentrations well below `Km`, elimination behaves approximately first order. As the responsible pathway approaches saturation, increases in dose can produce **disproportionately large increases in concentration**. At concentrations far above `Km`, elimination approaches a fixed amount per unit time.

### Prototype: phenytoin

Phenytoin is the classic clinically important example. Near the therapeutic range, relatively small dose increases can produce unexpectedly large concentration changes. This is why dose adjustment is made cautiously and should be guided by concentration, clinical state, albumin/free concentration where relevant, and the specific clinical context.

Do not generalize phenytoin’s kinetics to all antiseizure medications or psychotropics.

## Clearance is not the same as amount excreted

A patient can excrete a large amount of drug yet have low clearance if the concentration is also high. Conversely, a drug can have efficient clearance but a long half-life if its distribution volume is extremely large.

Think in linked variables:

**Dose → concentration → Vd + CL → half-life → accumulation → clinical exposure.**

## Dialyzability: a distribution problem as much as a kidney problem

Extracorporeal removal is favored when a toxin is:

- present substantially in the vascular compartment;
- relatively low in Vd;
- not extensively protein-bound, or has a meaningful free fraction;
- small enough for the membrane modality;
- water soluble;
- not cleared rapidly enough endogenously in the clinical situation.

Many lipophilic psychotropics with large Vd and extensive tissue binding are poor dialysis targets because little of the total body burden is accessible in plasma at any one time.

### Lithium: the important exception

Lithium is a small, water-soluble ion with no clinically meaningful protein binding and is highly dialyzable. EXTRIP recommends extracorporeal treatment in defined severe-poisoning scenarios, with hemodialysis the preferred modality. [V10]

**Do not memorize a single serum lithium number as the dialysis rule.** Renal function, neurologic/cardiac severity, concentration, chronicity and projected clearance all matter. Exact criteria belong in the lithium/toxicology section.

## Clinical retrieval rule

In overdose, ask three questions before assuming dialysis will help:

1. **Where is the drug?** Plasma versus tissue distribution.
2. **How bound is it?** Free versus protein/tissue-bound fraction.
3. **Can the extracorporeal method remove it faster than the patient can?**

---

# C1.4 — Therapeutic drug monitoring as a prescribing tool

## TDM is exposure measurement, not a substitute for clinical assessment

**Therapeutic drug monitoring (TDM)** combines a measured drug concentration with the timing and clinical context needed to interpret that concentration.

The strongest use case is not “a number exists.” It is that the number answers a clinically relevant uncertainty.

TDM is particularly useful when there is:

- non-response despite an apparently adequate dose;
- suspected nonadherence;
- unexpected adverse effects at a usual dose;
- a narrow therapeutic window;
- a suspected pharmacokinetic interaction;
- unusual metabolism or known pharmacogenomic variation;
- major change in renal/hepatic function;
- a major change in smoking status for a CYP1A2-sensitive drug;
- pregnancy, aging or another state that may materially alter exposure;
- a need to establish the individual patient’s effective concentration for future comparison. [V9]

## A valid sample has four parts

Before interpreting a level, document:

1. **Regimen** — drug, formulation, dose, dosing interval.
2. **Last dose** — date/time and whether it was actually taken.
3. **Sample time** — date/time and relation to the dosing interval.
4. **Exposure modifiers** — recent dose change, interacting drugs, smoking status, renal/hepatic change, acute inflammation/illness where relevant.

Without these, a “high” or “low” concentration may be uninterpretable.

## Steady-state sampling

For routine maintenance TDM, sample after the regimen has had enough time to approach a stable exposure and at a standardized point in the dosing interval—commonly a trough or guideline-defined sampling window.

Do not apply this rigidly to emergencies. Suspected poisoning, severe adverse effects, a dangerous interaction, or abrupt organ-function change may justify measurement before steady state. [V9]

## Therapeutic reference range versus dose-related reference range

These answer different questions.

- A **therapeutic reference range** is a population-based concentration range associated with a favorable probability of response/tolerability for a defined use.
- A **dose-related reference range** estimates the concentration expected from a given dose in a typical population and can help identify unusual clearance or nonadherence even when no strong therapeutic range exists.

Neither defines a magic boundary between “works” and “does not work.” Individual patients can respond outside population ranges or experience toxicity within them.

## When total concentration can mislead

Total concentration may diverge from active unbound exposure when protein binding is altered. Consider whether a free concentration or a corrected interpretation is needed in states such as severe hypoalbuminemia, renal failure, or strongly concentration-dependent protein binding.

This is drug-specific; do not apply a generic correction formula across psychotropics.

## Drugs for which TDM matters most

The guide will provide drug-specific procedures later, but the high-yield groups include:

- **lithium**;
- **clozapine**;
- **tricyclic antidepressants**;
- selected **mood stabilizers / antiseizure medications**;
- selected additional antipsychotics/antidepressants when exposure uncertainty is clinically important. [V9]

## The TDM reasoning loop

**Clinical question → correctly timed sample → interpret with dose + modifiers → decide whether the problem is adherence, exposure, sensitivity or pharmacodynamic failure → intervene → recheck after the new state is interpretable.**

A concentration is most valuable when it prevents an incorrect story about the patient.

---

# C1.5 — Receptor pharmacology that changes clinical care

## Keep four terms separate

### Affinity

How strongly a ligand binds a target. Lower `Ki` or `Kd` generally indicates higher affinity under the assay conditions.

### Potency

The concentration or dose required to produce a defined effect. `EC50` is the concentration producing 50% of a measured maximal effect in that experimental system.

### Efficacy / intrinsic activity

The degree to which a bound ligand activates or suppresses receptor signaling.

### Clinical effectiveness

What happens to the patient. It depends on far more than receptor potency: exposure, target engagement, pathway, illness biology, tolerability, adherence, comorbidity and evidence for the indication.

**Milligram dose does not rank clinical strength.** A low-milligram drug is not inherently “stronger” or more effective than a high-milligram drug.

## Agonist spectrum

| Ligand behavior | Core pharmacology | Clinical interpretation |
|---|---|---|
| Full agonist | Produces high receptor-system activation when sufficiently occupying the target | Can reproduce or exceed endogenous signaling depending on system |
| Partial agonist | Produces less maximal signaling than a full agonist in the same system | Can increase signaling where endogenous tone is low yet reduce net signaling when it competitively replaces a higher-efficacy agonist |
| Neutral antagonist | Occupies receptor without changing constitutive activity; blocks agonist access | Reduces signaling driven by endogenous/exogenous agonists |
| Inverse agonist | Reduces constitutive receptor activity below baseline | Relevant only where constitutive activity is pharmacologically meaningful |

Do not teach partial agonists as a universal fixed percentage of “full” signaling. Apparent efficacy depends on receptor density/reserve, endogenous ligand tone, concentration, cellular coupling, and the assay/tissue involved.

## Orthosteric and allosteric sites

- **Orthosteric ligands** bind the primary endogenous-ligand site.
- **Allosteric modulators** bind a distinct site and alter the receptor’s response to the orthosteric ligand.
- A **positive allosteric modulator (PAM)** enhances response.
- A **negative allosteric modulator (NAM)** reduces response.

Benzodiazepines are the clinically familiar example of GABA-A PAMs. The detailed GABA-A subunit pharmacology belongs in C5.

## Receptor reserve and tissue context

Maximal effect can occur before every receptor is occupied if downstream signaling has amplification or receptor reserve. The amount of reserve varies by receptor, tissue and disease state.

This is why receptor occupancy cannot be converted into a universal “percentage blocked = percentage clinical effect” rule.

## Affinity does not equal adverse-effect probability by itself

An adverse effect requires enough **in-vivo exposure at the relevant compartment** to occupy the target. A receptor-affinity table becomes clinically useful only when integrated with:

- free concentration;
- dose;
- active metabolites;
- CNS penetration;
- competing endogenous ligand;
- receptor density;
- patient susceptibility.

The later drug profiles should therefore translate receptor pharmacology into **clinical consequences**, not display affinity values without context.

---

# C1.6 — Clinically useful receptor map

The purpose of this map is recognition. Detailed disease-specific pathway teaching appears in later chapters.

| Receptor / system | Coupling | High-yield physiological role | What matters clinically in psychopharmacology |
|---|---|---|---|
| **D1-like: D1, D5** | Gs/Golf | Facilitates cAMP-dependent signaling in cortical/striatal circuits | Dopaminergic activation; detailed pathway roles deferred to C2 |
| **D2-like: D2, D3, D4** | Gi/o | Reduces cAMP; presynaptic/postsynaptic inhibitory signaling | Core antipsychotic / partial-agonist targets; prolactin/EPS/pathway effects in C2 |
| **5-HT1A** | Gi/o | Autoreceptor and postsynaptic modulation | SSRI adaptation; buspirone and multimodal antidepressant effects |
| **5-HT2A** | Gq | Cortical/striatal serotonergic signaling | Antagonism/inverse agonism relevant to antipsychotics; agonism relevant to psychedelics |
| **5-HT2C** | Gq | Appetite and monoamine modulation | Antagonism can contribute to appetite/weight liability in susceptible drugs |
| **5-HT3** | Ligand-gated cation channel | Vagal/area-postrema and GI signaling | Antagonism reduces nausea; one of the few ionotropic serotonin receptors |
| **5-HT4/6/7** | Gs | CNS/GI/circadian/cognitive signaling | Drug-specific modulatory targets; avoid inferring clinical benefit from affinity alone |
| **α1 adrenergic** | Gq | Vascular smooth-muscle tone | Antagonism → orthostatic hypotension, dizziness; priapism risk in some agents |
| **α2 adrenergic** | Gi/o | Presynaptic reduction of NE release / sympathetic tone | Agonists such as clonidine/guanfacine reduce sympathetic output; antagonist effects are drug-specific |
| **β adrenergic** | Gs | Cardiac/peripheral sympathetic signaling | β-blockade can reduce tremor and peripheral autonomic symptoms |
| **H1 histamine** | Gq | Wakefulness and appetite regulation | Antagonism commonly contributes to sedation and weight/appetite liability |
| **M1 muscarinic** | Gq | Cortical/hippocampal cholinergic signaling | Antagonism contributes to cognitive impairment and anticholinergic burden |
| **M2/M4 muscarinic** | Gi/o | Cardiac/presynaptic cholinergic modulation; striatal signaling | M4 pharmacology is relevant to newer muscarinic psychosis strategies; detail in C2 |
| **M3 muscarinic** | Gq | Peripheral glandular/smooth-muscle/metabolic signaling | Antagonism contributes to dry mouth, constipation, urinary effects and may add metabolic burden |
| **GABA-A** | Ligand-gated Cl⁻ channel | Fast inhibitory transmission | PAMs produce anxiolytic, sedative, anticonvulsant effects; dependence/tolerance in C5/C8 |
| **GABA-B** | Gi/o | Slow inhibitory signaling | Baclofen and presynaptic inhibition; later SUD/neuro material |
| **NMDA** | Glutamate-gated cation channel, voltage dependent | Plasticity, learning, excitatory transmission | Antagonism relevant to ketamine/dextromethorphan and toxicity; detailed mechanisms in C3/C6 |
| **AMPA** | Glutamate-gated cation channel | Fast excitatory transmission | Important downstream component of plasticity models; not a stand-alone clinical selection marker in most psychiatry |
| **Nicotinic ACh** | Ligand-gated cation channel | Attention, autonomic and reward circuitry | Nicotine dependence and varenicline pharmacology in C6 |
| **μ-opioid** | Gi/o | Analgesia, reward, respiratory control | Agonism/partial agonism central to opioid use treatment and overdose; C6/C8 |

## Retrieval shortcuts

When an adverse effect appears, the fastest receptor hypotheses are often:

- **sedation / appetite:** H1;
- **orthostasis:** α1;
- **dry mouth, constipation, urinary retention, delirium:** muscarinic blockade;
- **EPS / prolactin:** D2 pathway effects;
- **sexual dysfunction, nausea, activation:** serotonergic effects are usually multi-receptor and transporter dependent rather than reducible to one receptor;
- **respiratory depression / opioid toxidrome:** μ-opioid agonism, usually compounded by other CNS depressants.

These are starting hypotheses, not diagnostic proofs.

---

# C1.7 — Signal transduction, adaptation and receptor regulation

## Three GPCR families cover much of psychopharmacology

### Gs — increase cAMP signaling

Typical sequence:

**Receptor → Gs → adenylyl cyclase ↑ → cAMP ↑ → PKA activation → phosphorylation / transcriptional effects.**

Examples include D1-like dopamine receptors, β-adrenergic receptors, and 5-HT4/6/7.

### Gi/o — reduce cAMP and inhibit release/excitability

Typical sequence:

**Receptor → Gi/o → adenylyl cyclase ↓ → cAMP ↓**, with βγ subunits also able to open GIRK potassium channels and inhibit voltage-gated calcium channels.

Examples include D2-like receptors, 5-HT1A, α2 adrenergic, M2/M4 and μ-opioid receptors.

### Gq/11 — mobilize intracellular calcium and activate PKC

Typical sequence:

**Receptor → Gq/11 → phospholipase C → IP3 + DAG → intracellular Ca²⁺ release + PKC activation.**

Examples include 5-HT2A/2C, α1 adrenergic, H1, and M1/M3/M5 receptors.

## Immediate signaling versus adaptation

Psychotropic effects occur on different timescales:

- **milliseconds–seconds:** ion-channel opening/closure, membrane excitability;
- **seconds–minutes:** second-messenger and kinase changes;
- **hours–days:** receptor phosphorylation, trafficking, gene-expression changes;
- **days–weeks:** network adaptation, altered receptor density/coupling, synaptic remodeling and learned behavioral effects.

Target engagement can therefore be immediate while clinical benefit, tolerance, withdrawal, or relapse risk evolves much later.

## Desensitization and downregulation

Repeated agonist stimulation can reduce receptor responsiveness through mechanisms such as phosphorylation, β-arrestin recruitment, uncoupling, internalization, or altered receptor expression.

Clinically this contributes to phenomena including:

- tolerance;
- tachyphylaxis in some systems;
- reduced responsiveness during chronic agonist exposure.

Do not assume every tolerance syndrome is receptor downregulation; pharmacokinetic tolerance, learning, disease progression and behavioral adaptation can also contribute.

## Upregulation and supersensitivity

Chronic receptor blockade can produce compensatory increases in receptor number or signaling sensitivity in some systems. Abrupt removal of the blocker may then expose a system whose responsiveness has adapted to chronic antagonism.

This provides a pharmacological framework for some rebound and withdrawal phenomena, but it does **not** create a universal taper duration.

Exact switching and tapering decisions belong in C8, where half-life, receptor profile, prior exposure, relapse risk and available formulations are integrated.

## Clinical rule

**A drug can leave plasma before the system it changed has returned to baseline.**

This is the bridge between pharmacokinetics and deprescribing.

---

# C1.8 — Neuroplasticity: delayed and rapid treatment effects

## Target engagement and clinical response operate on different clocks

The source chapter correctly emphasizes a major psychopharmacology principle: many drug targets are engaged quickly, while clinical change can take longer.

The error is turning one proposed molecular cascade into the sole explanation.

### What is established

- Monoamine-transporter inhibition occurs much earlier than the full antidepressant response in many patients.
- Clinical improvement is variable: some symptoms may change early, while full response often develops over subsequent weeks.
- Repeated treatment changes receptor sensitivity, network activity and gene expression over time.

### What is strongly supported but not a single proven causal chain

Neurotrophic and synaptic-plasticity pathways—including BDNF/TrkB-related signaling, stress-related synaptic remodeling and changes in network connectivity—are implicated in antidepressant response.

These mechanisms should be taught as a **multilevel model**, not as “monoamines rise in an hour, then one required BDNF/neurogenesis pathway produces response at exactly 2–4 weeks.”

## A clinically useful time-course model

| Time scale | Pharmacology | Clinical interpretation |
|---|---|---|
| Minutes–hours | Transporter/receptor occupancy, acute neurotransmitter changes | Side effects or acute subjective effects may occur before therapeutic response |
| Days | Autoreceptor and network adaptation begins | Early symptom shifts may appear; lack of full response is not yet definitive failure |
| Weeks | Continued circuit adaptation, learning/environmental interaction, downstream transcriptional/plasticity changes | Full therapeutic effect becomes more assessable |
| Months+ | Maintenance of network/behavioral change; illness-course effects | Relapse prevention, adherence and long-term tolerability become dominant |

The table is a reasoning model, not a fixed timetable for every antidepressant or patient.

## Rapid-acting treatments prove that “antidepressants require weeks” is not a pharmacological law

Ketamine/esketamine and neuroactive-steroid treatments can produce clinically meaningful effects on a faster time scale than conventional monoaminergic antidepressants in appropriate indications.

Their existence reinforces two principles:

1. clinical response latency is mechanism-dependent;
2. “delayed response” should not be explained solely by drug accumulation to steady state.

Detailed ketamine/esketamine, dextromethorphan-bupropion and neurosteroid mechanisms belong in C3.

## Mechanism certainty labels for the rest of the guide

When presenting mechanisms, distinguish:

- **Established target:** directly demonstrated pharmacological action.
- **Supported clinical mechanism:** plausible mechanism with convergent human/experimental evidence.
- **Mechanistic model:** useful explanatory framework that is not proven as the sole cause of clinical response.
- **Emerging/contested:** promising but insufficient to present as settled.

This prevents molecular elegance from being mistaken for clinical certainty.

---

# C1.9 — Blood–brain barrier and CNS exposure

## The BBB is a selective interface, not a simple wall

The blood–brain barrier is formed primarily by specialized cerebral microvascular endothelial cells with tight junctions, supported by pericytes, astrocytic end-feet and the broader neurovascular unit.

For a psychotropic to produce a central effect, systemic exposure is necessary but not sufficient. The drug must achieve adequate **unbound concentration at the CNS target**.

## Passive CNS penetration is multi-determinant

Passive transcellular diffusion is generally favored by:

- adequate lipophilicity;
- lower polarity / hydrogen-bond burden;
- a meaningful unionized fraction at physiological pH;
- smaller molecular size;
- low enough protein/tissue sequestration to leave an available free fraction.

There is **no universal clinical logP or molecular-weight cutoff** that determines whether a psychiatric drug crosses the BBB. Medicinal-chemistry heuristics are useful in drug development but should not be converted into rigid bedside laws.

## Ionization: why permanent charge matters

Weak acids/bases can exist as mixtures of charged and uncharged forms depending on pKa and pH. The unionized fraction generally crosses lipid membranes more readily.

**Quaternary ammonium compounds** carry a permanent positive charge, which markedly reduces passive CNS penetration compared with structurally similar tertiary amines.

Clinical implication:

- tertiary antimuscarinics more readily produce central cognitive/anticholinergic effects;
- quaternary agents such as **trospium** and **glycopyrrolate** generally have much lower CNS penetration.

Do not state that they are “100% excluded”: low penetration is the clinically defensible principle.

## Efflux transporters

**P-glycoprotein (P-gp/ABCB1)** is an ATP-dependent efflux transporter expressed at the luminal blood–brain barrier and in other tissues. It can reduce tissue exposure to susceptible substrates.

Important caveat: being a P-gp substrate does not automatically mean that a clinically important CNS interaction will occur. Transporter contribution depends on the specific drug, competing pathways, dose, transporter expression and the magnitude of inhibition/induction.

Use transporter data when they explain a known clinical interaction; do not make them a universal prescribing rule.

## Circumventricular organs

Selected brain regions, including the area postrema, have relatively fenestrated capillaries and can detect circulating substances without the same BBB restrictions as most brain parenchyma. This helps explain why some peripheral drugs/toxins can trigger centrally coordinated responses such as vomiting despite limited global CNS penetration.

## Clinical reasoning sequence

When plasma exposure seems adequate but CNS effect is unexpectedly low or high, consider:

1. active metabolite exposure;
2. free versus total concentration;
3. BBB penetration and ionization;
4. transporter effects;
5. receptor affinity/occupancy;
6. target/pathway sensitivity.

---

# C1.10 — Metabolism, CYP enzymes, conjugation and environmental modifiers

## Phase I and Phase II are pathways, not a severity ranking

### Phase I

Includes oxidation, reduction and hydrolysis. Cytochrome P450 enzymes are major contributors to oxidative metabolism for many psychotropics.

### Phase II

Includes conjugation reactions such as glucuronidation, sulfation and acetylation, which often increase polarity and facilitate elimination.

Do not teach “Phase II is preserved in cirrhosis” as an absolute rule. Relative preservation can occur for some pathways, but severe liver disease can affect multiple metabolic processes. Drug-specific organ-impairment guidance belongs in C7.

## Substrate, inhibitor, inducer: three different roles

- **Substrate:** the enzyme metabolizes the drug.
- **Inhibitor:** reduces enzyme activity and may increase exposure to susceptible substrates.
- **Inducer:** increases enzyme/transporter expression or activity and may reduce exposure to susceptible substrates.

A drug can occupy more than one role across different enzymes.

## Inhibition versus induction timing

**Inhibition** can become relevant quickly because existing enzyme activity is blocked. The exact onset tracks inhibitor concentration and mechanism.

**Induction** generally evolves more slowly because new protein expression must develop. Offset can also persist after the inducer is stopped while enzyme expression returns toward baseline.

Do not memorize one universal “7–14 day” induction rule. Timing varies by enzyme, inducer, dose and patient.

## High-yield psychopharmacology metabolism map

This is a recognition table. Drug-specific management belongs in the monographs.

| Pathway | Important psychiatric substrates/examples | Important inhibitors/examples | Important inducers/examples | High-yield use |
|---|---|---|---|---|
| **CYP1A2** | Clozapine, olanzapine; contributes to several antidepressants | Fluvoxamine, ciprofloxacin | **Combustible tobacco smoke**; some broader enzyme inducers | Smoking change + clozapine/olanzapine exposure |
| **CYP2D6** | Aripiprazole, risperidone, atomoxetine, many TCAs; contributes to several antidepressants | Fluoxetine, paroxetine, bupropion, quinidine | No clinically established induction comparable to CYP1A2/3A4 | Genotype + inhibitor phenoconversion |
| **CYP2C19** | Citalopram, escitalopram, diazepam; important contribution to sertraline | Fluvoxamine, omeprazole/esomeprazole, fluconazole | Carbamazepine, rifampin and other broad inducers | PGx for selected SSRIs; PPI interactions |
| **CYP2C9** | Phenytoin; several non-psychiatric drugs | Fluconazole, amiodarone and others | Carbamazepine, rifampin | Phenytoin variability / interactions |
| **CYP3A4/5** | Lurasidone, quetiapine, aripiprazole, alprazolam, midazolam and many others | Strong azoles, clarithromycin, ritonavir/cobicistat; grapefruit affects intestinal CYP3A | Carbamazepine, phenytoin, rifampin, St John’s wort | Large interaction burden; some combinations contraindicated |
| **UGT / glucuronidation** | Lamotrigine and many non-CYP substrates | Valproate can inhibit lamotrigine glucuronidation | Estrogen-containing contraceptives increase lamotrigine clearance; broad inducers may contribute | Reminder that “no CYP metabolism” does not mean “no interaction” |

## Tobacco smoke is not nicotine

Combustion-derived polycyclic aromatic hydrocarbons induce CYP1A2. Nicotine itself is not the driver of this interaction.

Therefore, switching from cigarettes to nicotine replacement can remove smoke-related induction even though nicotine exposure continues.

For **clozapine**, current labeling warns that stopping a CYP1A2 inducer such as tobacco smoke can increase clozapine exposure and advises considering dose reduction with monitoring. [V4]

The exact adjustment is patient-specific; Foundations should teach the mechanism, while C2 provides the clozapine-specific management algorithm.

## Drug inflammation interaction: a future-proof caution

Acute systemic inflammation can reduce activity of some CYP pathways, including CYP1A2, in clinically important circumstances. In a clozapine patient who becomes acutely ill, a rising concentration may reflect more than adherence or dose.

This is a reason to use TDM and clinical context, not a reason to apply an unverified universal correction factor.

---

# C1.11 — Pharmacogenomics and HLA: use results precisely

## Genotype is one contributor to phenotype

Pharmacogenomics can explain part of the interindividual variation in exposure, efficacy and adverse effects. The clinically important distinction is:

**Genotype-predicted phenotype ≠ guaranteed real-time enzyme activity.**

A genetically normal metabolizer can functionally behave like a poor metabolizer when a strong inhibitor is present—**phenoconversion**. Age, organ function, inflammation and interacting drugs can further alter exposure.

## CPIC tells you how to use a result

CPIC guidelines are primarily designed to answer:

**“If this genotype result is already available, how should it inform prescribing?”**

They are not a universal mandate that every patient must undergo every pharmacogenetic test. [V6]

Testing indications and reimbursement vary by drug, regulator, population and jurisdiction.

## CYP2C19 and serotonin-reuptake inhibitors

CPIC 2023 provides clinically actionable recommendations for citalopram, escitalopram and sertraline based on CYP2C19 phenotype. [V6]

### Citalopram / escitalopram

For a **CYP2C19 poor metabolizer**:

- consider an alternative antidepressant not predominantly metabolized by CYP2C19; or
- if citalopram/escitalopram is clinically appropriate, use a lower starting dose, slower titration and approximately 50% lower standard maintenance dose than in normal metabolizers.

For **citalopram**, the FDA adult maximum is 20 mg/day in CYP2C19 poor metabolizers because of QT-prolongation risk. [V6]

For CYP2C19 ultrarapid metabolizers, citalopram/escitalopram exposure may be reduced; CPIC favors an appropriate alternative not extensively metabolized by CYP2C19 rather than simply assuming a large dose increase.

### Sertraline

For a **CYP2C19 poor metabolizer**, CPIC supports a lower starting dose, slower titration and approximately 50% lower standard maintenance dose, or an appropriate alternative.

For CYP2C19 rapid/ultrarapid metabolizers, CPIC does not recommend routine increased starting dosing of sertraline. [V6]

## CYP2D6: avoid the universal-percentage mistake

CYP2D6 is important for multiple psychotropics, but there is no defensible rule that every poor metabolizer should receive the same percentage dose reduction.

Examples with formal guidance include:

- selected TCAs (CYP2D6/CYP2C19); [V7]
- atomoxetine (CYP2D6);
- selected serotonin-reuptake inhibitors;
- several non-psychiatric prodrugs and interacting medications.

For each drug, follow the relevant label/CPIC recommendation rather than extrapolating from another substrate.

## HLA and severe cutaneous adverse reactions

### HLA-B*15:02

Strongly associated with carbamazepine- and oxcarbazepine-induced SJS/TEN.

- If **HLA-B*15:02 positive and carbamazepine-naïve**, avoid carbamazepine unless an exceptional benefit-risk rationale overrides.
- If **HLA-B*15:02 positive and oxcarbazepine-naïve**, CPIC recommends not using oxcarbazepine. [V8]

### HLA-A*31:01

Associated with a broader spectrum of carbamazepine hypersensitivity reactions, including maculopapular eruption, DRESS and SJS/TEN.

In a **carbamazepine-naïve HLA-A*31:01-positive** patient, CPIC recommends avoiding carbamazepine when clinically appropriate alternatives are available. [V8]

## Ancestry is a risk clue, not a genotype

Allele frequencies differ by ancestry, but self-reported ethnicity is an imperfect surrogate for carrier status. When a genotype is available, interpret the genotype itself.

Testing policy should follow current regulatory/local guidance rather than a simplistic “test all Asian patients / no one else” rule.

## What not to do with commercial PGx panels

Do not treat color-coded combinatorial reports as direct substitutes for drug-specific evidence. Ask:

1. Which gene–drug pair is driving the recommendation?
2. Is there CPIC/regulatory guidance for that pair?
3. Is the predicted phenotype being phenoconverted by current inhibitors/inducers?
4. Does the recommendation match the drug’s actual metabolic pathways?
5. Would TDM answer the clinical question more directly?

---

# C1.12 — Drug-interaction reasoning: a reusable clinical algorithm

## Start with the victim drug

When a new medication, smoking change, organ-function change or supplement is introduced, identify the **victim drug** whose exposure or pharmacodynamic risk may change.

Ask:

1. What is its major clearance pathway?
2. Is it a narrow-therapeutic-index or concentration-sensitive drug?
3. Is the new factor an inhibitor, inducer, substrate competitor, absorption modifier or pharmacodynamic co-toxin?
4. How quickly will the interaction start?
5. What happens when the interacting factor is later stopped?

The last question prevents many delayed toxicities.

## Pharmacokinetic interactions: exposure changes

### Inhibitor added

Typical direction for an active parent drug:

**Clearance ↓ → AUC/concentration ↑ → adverse effects/toxicity may increase.**

### Inducer added

Typical direction:

**Clearance ↑ → AUC/concentration ↓ → loss of efficacy/withdrawal may occur.**

### Inhibitor/inducer removed

The direction reverses. A patient who was stable because the dose had been adapted to an inducer may become toxic when the inducer disappears.

### Prodrug exception

For a drug requiring metabolic activation, enzyme inhibition can **reduce formation of the active metabolite** rather than simply increasing therapeutic effect. This is why the label “CYP inhibitor” is not enough; know whether the parent drug or metabolite is the clinically active moiety.

## Pharmacodynamic interactions: exposure can be unchanged while risk rises

High-yield additive risk patterns include:

| Shared liability | Common combinations that amplify it | Clinical concern |
|---|---|---|
| CNS / respiratory depression | Opioid + benzodiazepine + alcohol/other sedatives | Somnolence, aspiration, respiratory depression |
| Anticholinergic burden | Clozapine/low-potency antipsychotic + sedating antihistamine + antimuscarinic | Ileus, urinary retention, delirium, cognitive impairment |
| QT prolongation | Multiple QT-active drugs + electrolyte disturbance / bradycardia | Torsades risk in susceptible patients |
| Serotonergic excess | Multiple serotonergic mechanisms, especially with MAO inhibition | Serotonin toxicity |
| Orthostasis | α1-blocking psychotropics + antihypertensives/dehydration | Falls, syncope |
| Seizure threshold reduction | Multiple proconvulsant drugs + withdrawal/intoxication states | Seizure risk |
| Bleeding | SRI + anticoagulant/antiplatelet/NSAID | Increased bleeding risk |

Exact combinations and thresholds belong in drug-specific sections.

## Four interaction patterns to recognize immediately

### 1. Clozapine + strong CYP1A2 inhibitor

Current U.S. labeling specifies reducing clozapine to one-third of the dose when a strong CYP1A2 inhibitor such as fluvoxamine or ciprofloxacin is coadministered. [V4]

The principle: a large exposure shift can occur without any change in the clozapine prescription itself.

### 2. Smoking cessation in a clozapine patient

Removing tobacco-smoke induction can increase clozapine exposure. Reassess clinically, use TDM where available, and adjust according to the drug-specific protocol rather than applying a fixed universal percentage. [V4]

### 3. Lurasidone + strong CYP3A4 inhibitor/inducer

Current labeling states that lurasidone should not be used with strong CYP3A4 inhibitors such as clarithromycin/ketoconazole/ritonavir or strong CYP3A4 inducers such as rifampin/carbamazepine. [V5]

The principle: some interactions are **avoid/contraindicated**, not “monitor and increase the dose.”

### 4. Lamotrigine without CYP metabolism

Lamotrigine demonstrates why “not a CYP substrate” does not mean “interaction-free.” Valproate inhibits its glucuronidation, while estrogen-containing contraceptives can increase clearance. Exact dose schedules belong in C4/C7.

## Interaction-checker discipline

An interaction database is a detection system, not the clinical decision.

For every alert, determine:

- mechanism;
- expected direction and magnitude;
- clinical evidence;
- patient susceptibility;
- whether management is avoid, substitute, adjust, monitor, or ignore;
- what must happen when the interacting drug is stopped.

This is the difference between **polypharmacy recognition** and **polypharmacy panic**.

---

# C1.13 — Mechanism-to-bedside application matrix

The aim is rapid retrieval: identify the pharmacological law, then make the immediate clinical decision. These are teaching cases, not substitutes for the detailed protocols later in the guide.

| Clinical situation | Mechanism | Immediate interpretation / action |
|---|---|---|
| **1. Ziprasidone appears ineffective despite adherence; patient takes each dose with coffee and a small snack.** | Food-dependent bioavailability | Before escalating, correct administration. A meal of at least ~500 kcal gives more reliable exposure; fat content itself is not the key variable. [V1] |
| **2. A routine TDM level is drawn soon after a major dose change, before the new regimen could plausibly approach steady state, and is interpreted as “too low.”** | Exponential accumulation | Do not reflexively chase the early number. Recheck at the appropriate standardized time unless toxicity/urgency requires earlier measurement. Record dose and sample timing. [V9] |
| **3. A patient on stable phenytoin has a modest dose increase followed by a disproportionately large concentration rise and ataxia.** | Saturable / capacity-limited elimination | Hold/reduce as clinically indicated, reassess concentration and contributing factors, and make future dose changes cautiously. Do not assume dose-concentration proportionality near saturation. |
| **4. A stable clozapine patient stops smoking after hospital admission and develops increasing sedation.** | Loss of CYP1A2 induction from tobacco smoke | Treat smoking change as a major exposure change: assess for toxicity, obtain TDM when available, and apply clozapine-specific dose adjustment. Nicotine replacement does not recreate smoke induction. [V4] |
| **5. HLA-B*15:02 is positive before first carbamazepine prescription.** | Genetic risk of severe cutaneous hypersensitivity | Avoid carbamazepine in the drug-naïve patient; HLA-B*15:02 also changes oxcarbazepine selection. Use an appropriate alternative. [V8] |
| **6. A patient on lurasidone is prescribed clarithromycin.** | Strong CYP3A4 inhibition markedly increases lurasidone exposure | Do not simply “monitor.” Current labeling says the combination should not be used; choose an alternative antimicrobial or antipsychotic strategy. [V5] |
| **7. A CYP2C19 poor metabolizer is prescribed citalopram at a routine high maintenance dose.** | Reduced CYP2C19 clearance | Reassess drug/dose. CPIC supports an alternative or lower start/slower titration/≈50% lower maintenance; FDA limits adult citalopram to 20 mg/day in CYP2C19 poor metabolizers. [V6] |
| **8. An older patient develops cognitive toxicity from a centrally penetrating antimuscarinic; a peripheral antimuscarinic effect is still needed.** | BBB penetration and permanent charge | Consider whether a lower-CNS-penetrating quaternary agent is pharmacologically suitable. “Lower CNS penetration” is the correct principle—not “zero brain entry.” |

## Final C1 synthesis

When something unexpected happens in psychopharmacology, locate the problem at the correct layer:

**Administration → absorption → distribution → clearance → measured exposure → CNS access → receptor engagement → signaling/adaptation → clinical effect.**

Then ask what changed.

- If the dose is unchanged but exposure changed, look for **food, adherence, smoking, interactions, organ function, genetics or formulation**.
- If exposure is appropriate but effect is wrong, look at **target, pathway, diagnosis, illness biology and patient susceptibility**.
- If the drug has been stopped but symptoms emerge later, remember that **pharmacodynamic adaptation can outlast plasma elimination**.
- If a mechanism is attractive but not proven, label it as a **model**, not a fact.

This framework is the common language for every later chapter.

---

# Cross-reference map for later chapters

- D2 occupancy, dopamine pathways, antipsychotic receptor profiles, clozapine interactions → **C2 Antipsychotics**.
- Antidepressant transporter pharmacology, ketamine/esketamine, serotonin toxicity, TCA/MAOI specifics → **C3 Antidepressants**.
- Lithium/valproate/lamotrigine PK, TDM, UGT interactions and bipolar-specific mechanisms → **C4 Bipolar / Mood Stabilizers**.
- GABA-A subunits, benzodiazepines, hypnotics, stimulant kinetics → **C5 Anxiety / Sleep / ADHD**.
- Opioid partial agonism, nicotine, toxicology, movement/catatonia rescue pharmacology → **C6 SUD / Movement / Catatonia**.
- Renal/hepatic impairment, dialysis details, pregnancy, geriatrics, perioperative and cardiac special situations → **C7 Special Populations / Neuro / Organ**.
- Receptor discontinuity, hyperbolic tapering, cross-titration and withdrawal protocols → **C8 Switching / Deprescribing**.

# Stage 1B editorial QA notes

The following source-PDF claims were intentionally **not** carried forward as foundational laws:

- “five half-lives = complete clearance”;
- fixed universal partial-agonist intrinsic efficacy percentages;
- universal 65–80% D2 occupancy thresholds in C1 (moved to C2 for contextual verification);
- fixed BBB rules such as `logP 1.5–3.0`, `MW <450`, or “quaternary = 100% excluded” as bedside absolutes;
- “Phase II metabolism is spared in cirrhosis” as an absolute statement;
- universal CYP2D6 poor-metabolizer percentage reductions;
- a universal 30–50% clozapine dose reduction whenever smoking stops;
- a single lithium concentration threshold as the dialysis rule;
- “higher-dose mirtazapine is reliably less sedating”;
- hippocampal neurogenesis / BDNF / mTOR as singular proven explanations of antidepressant efficacy;
- treatment instructions embedded in C1 that belong in drug-specific emergency/switching protocols.

These changes are deliberate corrections, not omissions.