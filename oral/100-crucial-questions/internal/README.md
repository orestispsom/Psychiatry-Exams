# Internal architecture — 100 Crucial Questions

This directory contains the control system behind the visible 100-question attempts.

## Authority order

1. `core-coverage.yml` — canonical, question-independent psychiatry coverage map. This defines the important knowledge that must be preserved across revisions.
2. `question-design.md` — rules for constructing main questions, genuine examiner follow-ups and hidden answer-coverage checklists.
3. `attempt-maps/<attempt>.yml` — disposable maps showing how a specific visible attempt samples the canonical coverage and where coverage is partial or distributed.
4. `answer-coverage/<attempt>.yml` — hidden authoring specifications defining the minimum territory an excellent answer to each visible question must cover.
5. `source-register.md` — record of sources actually reviewed and the scope in which they were used.
6. `core-coverage-candidates.yml` — staging area for possible additions to the canonical bank that require deliberate review before promotion.

## Core principle

The coverage map does **not** exist to justify the current 100 questions. The 100 questions exist to test a high-value subset/organisation of the canonical coverage map.

Question numbers may change freely. Stable coverage IDs should change only when the underlying psychiatry concept itself needs to be reorganised.

## Visible versus hidden coverage

A clinically important topic does not require its own main question. It can be protected through:

- a numbered main question;
- a genuine examiner follow-up;
- distributed hidden answer coverage across one or more questions;
- or, for lower-priority material, canonical coverage without a visible prompt.

Follow-ups must not be used merely as answer-outline bullets.

## Answer-coverage inheritance

When a new attempt preserves the same main-question spine and only changes visible follow-ups or minor wording, its `answer-coverage/<attempt>.yml` may inherit the previous attempt rather than duplicating the entire specification.

The inheriting file must state:

- the parent answer-coverage file;
- any changed or additional requirements;
- any changed visible sampling;
- whether inherited requirements remain unchanged.

Use inheritance only when it makes the control system simpler and unambiguous. If main-question scope changes materially, create a full self-contained answer-coverage specification instead.

## Growth rule

Enrich `core-coverage.yml` when source review reveals a meaningful senior-resident knowledge gap. Do not expand it merely to capture every detail in a textbook, guideline or classification system.

The intended endpoint is a compact but increasingly robust map of the most crucial psychiatry knowledge, not an encyclopaedia.
