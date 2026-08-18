# Internal architecture — 100 Crucial Questions

This directory contains the control system behind the visible 100-question attempts and their eventual model answers.

## Authority order

1. `core-coverage.yml` — canonical, question-independent psychiatry coverage map. This defines the important knowledge that must be preserved across revisions.
2. `adult-board-scope.yml` — exam-scope overlay for Greek Adult Psychiatry specialist certification. It determines which canonical topics deserve scarce visible main-question space without deleting broader psychiatry knowledge.
3. `question-design.md` — rules for constructing main questions, genuine examiner follow-ups, hidden answer coverage and board-fact use.
4. `attempt-maps/<attempt>.yml` — disposable maps showing how a specific visible attempt samples the canonical coverage and where coverage is partial or distributed.
5. `answer-coverage/<attempt>.yml` — hidden authoring specifications defining the minimum clinical/conceptual territory an excellent answer to each visible question must cover.
6. `board-fact-anchors.yml` — high-yield exact-recall, criterion/timing, classic-distinction and drug-specific board facts that must be retrievable within the 100 answer packages. These anchors do not create new main questions and require source verification before final answers are written.
7. `answer-production/` — production governance: evidence workflow, dossier schema, answer archetypes and bounded agent prompts. This controls how research becomes a final model answer.
8. `source-register.md` — record of sources actually reviewed and the scope in which they were used.
9. `core-coverage-candidates.yml` — staging area for possible additions to the canonical bank that require deliberate review before promotion.

The corresponding working files for final answers live under `../answers/`.

## Core principle

The coverage map does **not** exist to justify the current 100 questions. The 100 questions exist to test a high-value subset/organisation of the canonical coverage map.

The Adult Psychiatry scope overlay may demote broader psychiatry topics from visible main-question status without deleting them from canonical knowledge.

Question numbers may change freely. Stable coverage IDs should change only when the underlying psychiatry concept itself needs to be reorganised.

## Board-sufficiency architecture

The intended final learning package for each of the 100 questions has four learner-facing knowledge layers, with a fifth source-control layer behind them:

1. **Oral core** — a coherent approximately 2–5 minute senior-resident answer.
2. **Must-not-miss answer coverage** — differentials, red flags, treatment sequencing, monitoring, special situations and other clinically important content.
3. **Board-fact anchors** — exact criteria/durations, classic distinctions, key calculations/numerical anchors and specific high-yield drug facts that can be tested in MCQs or short oral probes.
4. **Examiner pivots** — only genuine follow-up questions that meaningfully change or deepen the task.
5. **Canonical question dossier** — hidden claim-level provenance and adjudication controlling what the writer is allowed to say.

The board-sufficiency target is not literal memorisation of 100 scripts. It is that a candidate who genuinely understands, can reproduce and can apply the first four layers across the 100 questions should possess a preparation set plausibly sufficient for a general Greek Adult Psychiatry specialist-certification examination. The dossier exists to make those layers accurate and source-controlled. No finite bank guarantees an exam outcome.

## Model-answer production rule

Research, source extraction, adjudication and writing are separate stages.

The final writer receives an **approved dossier**, not raw textbooks and not an open research brief. It may compose and optimise oral delivery, but it may not introduce unsupported facts, new treatment recommendations, numerical claims or unadjudicated source reconciliation.

The full workflow is defined in `answer-production/README.md`.

## Visible versus hidden coverage

A clinically important topic does not require its own main question. It can be protected through:

- a numbered main question;
- a genuine examiner follow-up;
- distributed hidden answer coverage across one or more questions;
- a board-fact anchor;
- or, for lower-priority material, canonical coverage without a visible prompt.

Follow-ups must not be used merely as answer-outline bullets.

## Board-fact rule

`board-fact-anchors.yml` protects facts that are too precise or narrow to deserve main-question space but are still plausible board probes.

- It should remain compact and high-yield.
- It stores what must be recalled; potentially unstable exact answers are verified when final answer packages are produced.
- Diagnostic/classification facts use the designated exam source and must be labelled when current classification differs.
- Doses, serum levels, monitoring schedules, interactions, pregnancy restrictions and licensing require current authoritative prescribing/regulatory verification.
- Historical/legacy facts may remain only when clearly labelled as exam-specific or historical.
- A board fact never upgrades itself into a main question merely because it is easy to test.

## Answer-coverage inheritance

When a new attempt preserves the same main-question spine and only changes visible follow-ups or minor wording, its `answer-coverage/<attempt>.yml` may inherit the previous attempt rather than duplicating the entire specification.

When most semantic questions are retained but numbering changes because a small number of slots are reallocated, inheritance is also permitted if the new file contains an explicit old→new semantic migration map and self-contained coverage blocks for every genuinely new question.

The inheriting file must state:

- the parent answer-coverage file;
- any old→new question migration when numbering changed;
- any changed or additional requirements;
- any changed visible sampling;
- whether inherited requirements remain unchanged.

Do not use inheritance when the majority of main-question scopes change or when the migration would be ambiguous; in that case create a full self-contained answer-coverage specification.

## Jurisdiction rule

Diagnosis and clinical science may use international authoritative sources. Law, consent, involuntary care, confidentiality, safeguarding and forensic procedure must use the current Greek framework. Treatment evidence may be international, but licensing, regulation and availability must be checked for Greece/EU where relevant. Service-model answers must not silently default to UK or US structures.

## Growth rule

Enrich `core-coverage.yml` when source review reveals a meaningful senior-resident knowledge gap. Do not expand it merely to capture every detail in a textbook, guideline or classification system.

The intended endpoint is a compact but increasingly robust map of the most crucial psychiatry knowledge, not an encyclopaedia.
