# Internal architecture — 100 Crucial Questions

This directory contains the control system behind the visible 100-question attempts.

## Authority order

1. `core-coverage.yml` — canonical, question-independent psychiatry coverage map. This defines the important knowledge that must be preserved across revisions.
2. `question-design.md` — rules for constructing main questions, genuine examiner follow-ups and hidden answer-coverage checklists.
3. `attempt-maps/<attempt>.yml` — disposable maps showing how a specific visible attempt samples the canonical coverage and where its structure should be revised.
4. `source-register.md` — record of sources actually reviewed and the scope in which they were used.

## Core principle

The coverage map does **not** exist to justify the current 100 questions. The 100 questions exist to test a high-value subset/organisation of the canonical coverage map.

Question numbers may change freely. Stable coverage IDs should change only when the underlying psychiatry concept itself needs to be reorganised.

## Growth rule

Enrich `core-coverage.yml` when source review reveals a meaningful senior-resident knowledge gap. Do not expand it merely to capture every detail in a textbook, guideline or classification system.

The intended endpoint is a compact but increasingly robust map of the most crucial psychiatry knowledge, not an encyclopaedia.
