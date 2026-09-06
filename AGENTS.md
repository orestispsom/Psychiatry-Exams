# Psychiatry Study — Agent Rules

## Ecosystem process governance

For multi-agent and cross-repository coordination, follow `orestispsom/mental-health-core/docs/ECOSYSTEM_GOVERNANCE.md`. It governs sync, task claims, explicit supersession, semantic merge preflight, and version-bound validation; this file remains authoritative for psychiatry-study and exam-specific rules.

1. Accuracy over fluency. Never invent psychiatric facts, criteria, doses, statistics, citations, quotations, page numbers, or guideline recommendations. If uncertain, verify or state uncertainty.
2. Separate exam truth from current clinical truth. Exam questions prioritize designated exam sources/editions; current clinical questions prioritize current authoritative guidance. If they conflict, label **Exam answer** vs **Current practice**.
3. Source hierarchy depends on the claim: diagnosis → DSM-5-TR/ICD-11; treatment → current major guidelines → prescribing/regulatory sources → systematic reviews/meta-analyses → major trials → authoritative textbooks; law/regulation → current official sources, prioritizing Greek authorities where relevant.
4. Psychopharmacology: verify doses, interactions, contraindications, monitoring, pregnancy and licensing from current authoritative sources.
5. Browse/retrieve whenever recency could matter: guidelines, drug safety/licensing, legislation, new treatments, epidemiology, standards, or recent research. Stable foundational textbook facts do not require browsing.
6. Prefer primary/authoritative sources. A citation must actually support its claim; inspect the underlying guideline/paper when exact recommendations, numbers, or conclusions matter.
7. Source-locked requests stay source-locked. If asked to work from a supplied source, use it as the authority and do not silently supplement missing material.
8. Handle disagreement explicitly: identify the disagreement, relevant dates/versions, applicable authority, and practical/exam conclusion. Do not average incompatible answers.
9. Distinguish evidence strength when relevant: established, supported, emerging, contested, historical, or exam-specific. Do not convert association into causation or hypotheses into established mechanisms.
10. Study material should optimize retrieval and discrimination: differentials, timelines, red flags, treatment sequencing, monitoring, adverse effects, common traps, and meaningful exceptions over low-value detail.
11. Assume advanced psychiatric knowledge. Use precise terminology, lead with the answer, and keep outputs information-dense.
12. For consequential or uncertain claims, verification beats memory. A qualified “not verified” is preferable to a confident approximation.
13. `orestispsom/Psych` is the canonical continuously updated exam-prep app and production dataset. Use its current files when app/exam-bank state matters; do not let this library silently fork canonical production data.
14. Priority when rules conflict: accuracy → source fidelity → safety → exam/current distinction → understanding → exam utility → brevity.
15. For the commercial/product role of `oral/100-crucial-questions`, consult `oral/100-crucial-questions/internal/2026-08-26-hustling-portfolio-context.md` only when the task concerns publication prioritization, product strategy, reuse/licensing, or cross-project sequencing. That context must never override manuscript/source locks, psychiatric editorial decisions, audit findings, or publication QA.

## Reusable knowledge asset detection

The protocol is canonical in [`mental-health-core/docs/REUSE_CANDIDATE_PROTOCOL.md`](https://github.com/orestispsom/mental-health-core/blob/main/docs/REUSE_CANDIDATE_PROTOCOL.md). Follow it there — the callout format and all eight rules live in one place, so they stop drifting between repositories.

Only the local specifics are recorded here.

**What counts as a candidate in this repository:** strong differential frameworks, decision or monitoring algorithms, comparison tables, memorable synthetic cases, difficult concepts explained unusually clearly, common-clinician traps, patient or family explanations, clinician teaching material, clinical-AI test cases, and clinician-workflow insights.

**Where a candidate could go:** professional education · clinician resource or product · article or website · patient/family handoff · clinical-AI evaluation · software workflow.

**Local emphasis:** During board preparation the default is **note for later** unless a one-to-five-minute capture also improves learning and retrieval.
