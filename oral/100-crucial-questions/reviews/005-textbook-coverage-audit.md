# Attempt 005 — Textbook Coverage Audit (read-only)

Status: one-off audit deliverable. Does not modify `attempts/005.md`, `internal/core-coverage.yml`, `internal/question-design.md`, `internal/attempt-maps/005.yml`, or `internal/source-register.md`. Recommendations only.

## 1. Executive conclusion

`core-coverage.yml` is already a mature, well-hierarchised canonical map — it already contains essentially every topic this brief asked me to specifically re-check (Parkinson's disease psychiatry, TBI, vascular dementia, gender dysphoria, PMDD, sleep/circadian physiology, neuroanatomy, core psychodynamic concepts, nicotine, other personality disorders, OCD-related disorders, BED/ARFID, rTMS, professional boundaries, negative/cognitive symptoms of schizophrenia). The independent textbook-derived domain map built from Oxford Shorter 7th, Oxford New 3rd, Kaplan Synopsis 2021 and DSM-5-TR converges strongly with this existing structure — no missing CORE domain was found.

The residual problems are narrow and mostly about **weighting inside Attempt 005**, not about the coverage bank's architecture: a small number of IMPORTANT-tier units that are canonically present but never surface as a visible question or follow-up (negative/cognitive schizophrenia symptoms, non-dementia Parkinson's-disease psychiatric syndromes, other personality disorders, OCD-related disorders, rTMS), one main question that is arguably overweighted relative to its clinical importance (carbamazepine, Q84), two follow-ups that duplicate their own parent question's necessary content (31a, 92a) and one that duplicates another question's follow-up (41a vs 11a). One small canonical gap was found in `core-coverage.yml` itself: intimate-partner/domestic violence has no coverage unit.

Attempt 005 is judged **structurally near-final**; the fixes below are targeted, not systemic.

## 2. Sources actually inspected

| Source | Edition/Year | Classification | What was used |
|---|---|---|---|
| Oxford Shorter Textbook of Psychiatry | 7th ed. (2018 printing, 2017 copyright) | BROAD, priority 1 | Full table of contents (26 chapters) extracted via `pdftotext -layout`; used as primary breadth/weighting reference |
| Oxford New Textbook of Psychiatry | 3rd ed. (2020) | BROAD, priority 2 | Full table of contents (~140+ numbered chapters across sections) extracted; used to check granular/contemporary topics (hoarding, BDD, gender dysphoria, functional neurological disorder, factitious/malingering, domestic violence, refugee mental health, chronic pain/fibromyalgia interface, neuroimaging/connectome, brain stimulation) |
| Kaplan & Sadock's Synopsis of Psychiatry | 2021 | BROAD, priority 3 | Full table of contents including sub-sections (e.g. 2.1–2.17, 4.1–4.13, 21.1–21.11) extracted; used as the most systematically organised cross-check of disease/treatment granularity |
| DSM-5-TR | 2022 | DIAGNOSTIC, priority 5 | Front-matter classification/section listing extracted (Sections I–III, diagnostic chapter list) for diagnostic-domain completeness only, not text detail |

Kaplan & Sadock's Comprehensive Textbook was **not opened** — the three broad sources above converged clearly enough that the "unresolved gap" trigger for the comprehensive text was never reached. No psychopharmacology-specialist source (Maudsley, Stahl, Carlat, etc.) was opened; none of the discrepancies found required dose/monitoring-level verification. No linear reading was performed on any source; only TOC/front-matter extraction via `pdftotext -layout`, targeted `grep` over the extracted text, and page-range extraction.

## 3. Coverage-bank findings (`core-coverage.yml`)

| Topic/domain | Current status | Textbook signal | Recommendation | Priority |
|---|---|---|---|---|
| Non-dementia Parkinson's-disease psychiatric syndromes (depression/anxiety/apathy, PD psychosis drug choice, dopamine-agonist impulse-control disorders) | Present as `neuropsychiatry.parkinson` (IMPORTANT); essentials already name "psychosis and medication-related behavioural syndromes" | All three broad sources treat PD's cognitive/dementia dimension (DLB/PDD) as a distinct chapter from PD's broader psychiatric complications (mood, psychosis, ICDs from dopaminergic drugs) — the two are not interchangeable content | GOOD_AS_IS in the coverage bank itself; the gap is in Attempt 005's sampling (see §4) | A (attempt-level) |
| Intimate partner / domestic violence | **Absent** — no coverage unit anywhere in `core-coverage.yml` | Oxford New has a dedicated chapter ("Domestic violence and abuse and mental..."); a strong resident is expected to screen for and respond to IPV as part of risk/safeguarding practice | Add a compact SUPPORTING/IMPORTANT unit under `risk` or `legal_ethics` domain (screening, safety planning, overlap with forensic/safeguarding); does not need a dedicated main question — can be represented as answer-coverage within Q6 (violence risk assessment) | B |
| Elimination disorders (enuresis/encopresis) | Absent | DSM-5-TR and Kaplan list it as its own chapter, but it is low-yield for a senior-resident oral board relative to everything else competing for space | No action — correctly excluded under the inclusion rule | — (confirmatory, not a gap) |
| Obesity / chronic pain–fibromyalgia psychiatric interface | Absent | Oxford New devotes chapters to both, but both are SUPPORTING-tier for a psychiatry board (medical/psychosomatic-medicine adjacent) | Optional light SUPPORTING mention only if the bank is later enriched; not urgent | C |
| Refugee / mass-trauma-exposed populations, cultural formulation | Present only generically via `systems.public_cultural_digital` (SUPPORTING) | Oxford New gives this real chapter weight, but Greek-board relevance is lower than the domains already CORE | GOOD_AS_IS | — |
| Negative and cognitive symptoms of schizophrenia | Present as `schizophrenia.negative_cognitive` (IMPORTANT) | Consistently treated as a distinct clinically important dimension in all three broad sources (functional-outcome relevance, limited pharmacological treatment, differential from depression/EPS/environmental deprivation) | Bank content is adequate; Attempt 005 under-samples it (see §4) | A (attempt-level) |
| OCD-related disorders (BDD, hoarding, trichotillomania/excoriation) | Present as `ocd.related` (IMPORTANT) | Oxford New gives BDD and hoarding disorder their own chapters; Kaplan groups them under "Obsessive-Compulsive and Related Disorders" | Bank adequate; Attempt 005 under-samples (see §4) | B (attempt-level) |
| Other personality disorders (paranoid/schizoid/avoidant/dependent/OCPD) | Present as `personality.other` (IMPORTANT) | Standard content in all sources | Bank adequate; Attempt 005 has zero sampling (see §4) | B (attempt-level) |
| rTMS/other neuromodulation | Present as `biological.rtms_other` (IMPORTANT) | Oxford New has a chapter on the development of brain stimulation; increasingly examinable given growing clinical use | Bank adequate; Attempt 005 has zero sampling (see §4) | B (attempt-level) |
| Gender dysphoria / gender-identity-related care | Present as `gender.dysphoria_care` (IMPORTANT) | DSM-5-TR and Kaplan give it a full chapter; Oxford New gives it a dedicated chapter (Ch.116) | Bank adequate; Attempt 005 has **zero** sampling — no main question, no follow-up (see §4) | A (attempt-level) |

## 4. Attempt 005 main-question audit

Only questions with a plausible non-KEEP disposition are listed.

| Q | Current wording (abridged) | Issue | Recommended disposition |
|---|---|---|---|
| Q84 | "How do you use carbamazepine safely in psychiatric practice?" | `psychopharm.carbamazepine` is IMPORTANT (not CORE); carbamazepine is a third-line mood stabiliser with narrow current psychiatric use. Devoting a full main-question slot to it — the same weight as lithium (Q81) or valproate (Q82) — is disproportionate given several IMPORTANT/undersampled topics (see §3, §6) currently get zero main-question or follow-up representation | MERGE/DEMOTE: fold into Q82/Q83 answer-coverage (enzyme induction, limited indications, monitoring) or reduce to a short follow-up on Q82; free the main slot |

No other main question was judged REPLACE/MERGE/DEMOTE-worthy. The remaining 99 questions each test one coherent entity/comparison/drug/emergency and do not obviously duplicate another question's necessary content.

## 5. Follow-up audit

Only problematic follow-ups are listed; all others reviewed were judged genuine and are not repeated here.

| Follow-up | Test result | Classification |
|---|---|---|
| 31a (OCD: poor-insight obsession vs delusion) | If Q31 ("diagnose and treat OCD") is answered well, insight specifiers are already part of the diagnostic-criteria discussion; this follow-up also substantially duplicates Q2's delusion/overvalued-idea/obsession framework | DEMOTE_TO_INTERNAL_COVERAGE |
| 41a (cannabis use changing FEP formulation) | Near-duplicate of 11a, which already tests exactly "when does cannabis use point to substance-induced psychosis vs an emerging primary psychotic disorder" in the first-episode-psychosis context | DEMOTE_TO_INTERNAL_COVERAGE (redundant with 11a; delete rather than merge) |
| 92a (when countertransference is useful vs misleading) | If Q92 ("what are transference/countertransference, and **why are they clinically important**") is answered well, the useful-vs-misleading distinction is inherent to explaining clinical importance | DEMOTE_TO_INTERNAL_COVERAGE |

All other reviewed follow-ups (10a, 11a, 19a, 36a, 38a, 48a, 58a, 59a, 60a, 61a, 67a, 71a, 77a, 81a, 82a, 83a, 86a, 90a, 98a) are GENUINE_FOLLOW_UP — each tests a complication, special circumstance, discrimination, or mechanistic depth point that would not already be answered by a strong response to its parent question.

## 6. Missing/underrepresented psychiatry (ranked strongest to weakest)

1. **Gender dysphoria / gender-identity-related psychiatric care** — canonically IMPORTANT, currently zero visible representation in Attempt 005 (no main question, no follow-up), despite dedicated chapters in DSM-5-TR, Kaplan and Oxford New.
2. **Negative and cognitive symptoms of schizophrenia** — high functional-outcome relevance and a classic discrimination target (vs depression, EPS-induced bradykinesia, environmental deprivation); currently invisible beyond passing mention inside Q12's psychopathology description.
3. **Parkinson's disease psychiatric syndromes outside dementia** (PD psychosis drug choice, dopamine-agonist impulse-control disorders) — Q48 only tests the DLB/PDD dementia comparison, not this distinct and high-stakes prescribing topic.
4. **Other personality disorders** (paranoid, schizoid, avoidant, dependent, OCPD) — entirely unsampled; Q70/71/72 cover only the general concept, BPD and ASPD/psychopathy.
5. **OCD-related disorders** (BDD, hoarding) — entirely unsampled despite dedicated textbook chapters and clear differential-diagnosis value.
6. **rTMS/other neuromodulation** — entirely unsampled; increasingly examinable as clinical use grows.
7. **Intimate partner/domestic violence** — genuine gap in `core-coverage.yml` itself (not just Attempt 005); lower urgency than the six items above since it is not currently even a canonical unit.
8. **Professional boundaries** and **nicotine/tobacco dependence** — both canonically IMPORTANT and unsampled, but both are lower-stakes/lower-yield than items 1–6 and can reasonably remain answer-coverage-only.

## 7. Main-question domain allocation vs textbook emphasis

Attempt 005's per-section main-question counts (I–X, 100 total) were compared qualitatively against the relative chapter/section weight in Oxford Shorter (26 chapters), Kaplan Synopsis (35 chapters plus dense sub-sections) and Oxford New (~140+ chapters). No obvious distortion was found:

- Psychopharmacology + biological treatments (16 main questions) is proportionate to the very high density of distinct psychopharm sub-topics in all three sources (Kaplan alone gives psychopharmacology 11 numbered sub-sections), and matches `source-register.md`'s own note that Greek oral boards weight psychopharmacology heavily.
- Developmental/eating/sleep/personality/sexual psychiatry (18 main + 4 follow-ups across five different domains) is proportionate to the combined textbook space these domains occupy; not bloated.
- Foundational science/evidence/ethics/forensic/systems (7 main questions) is *not* over- or under-weighted relative to Oxford Shorter's own two dedicated chapters (Aetiology; Evidence-based approaches) plus ethics/forensic/service chapters — and Greek oral exams are known to test neuroanatomy/neurotransmitter-pathway questions recurrently, which this section already accommodates via Q94–96.
- No section shows the classic distortion patterns this step was designed to catch (excess foundational science crowding out clinical material, excessive personality/developmental material, thin psychopharmacology, or missing common clinical entities). The only concrete miscalibration found is the single-question weighting issue already flagged for carbamazepine (§4).

## 8. Candidate swaps for Attempt 006 (max 10)

1. REMOVE Q84 (carbamazepine, standalone main question) → ADD new main question on gender dysphoria / gender-identity-related psychiatric care → rationale: carbamazepine is IMPORTANT-tier/third-line and adequately foldable into Q82/Q83 answer-coverage; gender-identity care is IMPORTANT-tier and currently has zero visible representation.
2. DEMOTE follow-up 31a → fold into Q2/Q31 internal answer-coverage (no replacement needed) → rationale: duplicates Q2's delusion/overvalued-idea/obsession framework and Q31's own diagnostic-criteria content.
3. DEMOTE follow-up 41a → delete as duplicate of 11a (no replacement needed) → rationale: both test cannabis use altering the diagnostic formulation of first-episode psychosis.
4. PROMOTE `schizophrenia.negative_cognitive` → add as a genuine follow-up to Q17 (maintenance/rehabilitation) → rationale: high-yield discrimination (negative symptoms vs depression/EPS/deprivation) with real functional-outcome stakes, currently invisible.
5. PROMOTE `neuropsychiatry.parkinson`'s non-dementia content → add as a genuine follow-up to Q48, alongside or replacing 48a's narrow DLB-antipsychotic-sensitivity scope with a slightly broader PD-psychosis/dopamine-agonist-ICD framing → rationale: distinct high-stakes prescribing topic from the DLB/PDD dementia comparison Q48 currently tests.
6. PROMOTE `personality.other` → add as a genuine follow-up to Q70 (personality disorder general) → rationale: paranoid/schizoid/avoidant/dependent/OCPD patterns are entirely unsampled and low-cost to add as a follow-up.
7. PROMOTE `ocd.related` → add as a genuine follow-up to Q31 (OCD) → rationale: BDD/hoarding differential value, entirely unsampled, no main-slot cost.
8. PROMOTE `biological.rtms_other` → add as a genuine follow-up to Q90 (ECT) → rationale: contemporary neuromodulation increasingly examinable; natural pairing with ECT indications/limitations.
9. ADD new `core-coverage.yml` unit for intimate-partner/domestic violence (canonical-bank-level change, out of scope for this audit to implement) → represent via Q6 (violence risk assessment) answer-coverage, no new main slot needed → rationale: genuine gap in the canonical bank itself, not merely in Attempt 005's sampling.
10. DEMOTE follow-up 92a → fold into Q92 internal answer-coverage (no replacement needed) → rationale: "useful vs misleading" is inherent to explaining countertransference's clinical importance, which Q92 already asks for directly.

## 9. Final recommendation

**Structurally near-final.** The canonical coverage bank (`core-coverage.yml`) is already mature and converges with an independently built textbook domain map across Oxford Shorter 7th, Oxford New 3rd, Kaplan Synopsis 2021 and DSM-5-TR — no CORE-tier domain is missing, and nearly every topic this brief flagged as a suspected weak point (Parkinson's, TBI, vascular dementia, gender dysphoria, PMDD, sleep/circadian physiology, neuroanatomy, psychodynamic concepts, nicotine, other personality disorders, OCD-related disorders, BED/ARFID, rTMS, professional boundaries, negative/cognitive schizophrenia symptoms) is already present in the bank at an appropriate priority tier. The only genuine bank-level gap found is intimate-partner/domestic violence. Attempt 005's own architecture is sound and its domain allocation is not visibly distorted relative to textbook emphasis. The concrete work before Attempt 006 is narrow: one overweighted main question (carbamazepine) to demote/merge, one clearly valuable replacement main question (gender-identity care) to add, four to five cheap follow-up additions (negative/cognitive schizophrenia symptoms, PD psychiatric syndromes, other personality disorders, OCD-related disorders, rTMS), and three follow-up redundancies (31a, 41a, 92a) to tidy up.