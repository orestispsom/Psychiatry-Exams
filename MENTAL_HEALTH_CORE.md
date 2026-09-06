# Canonical shared knowledge: `mental-health-core`

`https://github.com/orestispsom/mental-health-core` is the canonical layer for clinical concepts shared across this ecosystem. This document says what that means for this repository.

**Nothing here has moved, been rewritten, or been deleted.** The core owns concept identity and distinctions; this repository keeps everything it produces.

## What this repository consumes

Concept identity and definitions, safety-critical distinctions, English↔Greek terminology, and the epistemic and provenance vocabulary.

## What stays here

The 100-crucial-questions pipeline, exam framing and board conventions, source packets and verification records, Greek board-review modules, the drug-dossier schema and its dossiers, high-yield tables, and the publication tooling.

Exam convention in particular stays local by design — it is tied to a board, an edition and a year, and the core deliberately does not carry it. The rule separating the two is in the core as [`MHC-C-004`](https://github.com/orestispsom/mental-health-core/blob/main/concepts/exam-answer-vs-current-practice.md), which is `AGENTS.md` rule 2 generalised.

## What this repository contributed

The audit found this repository to be the richest source of clinical distinctions in the ecosystem. Three core concepts came from material here, including [`MHC-C-012`](https://github.com/orestispsom/mental-health-core/blob/main/concepts/obsession.md) — the rule that poor insight does not by itself convert an obsession into a delusion. That rule was written down in exactly one place and needed in at least three.

## An issue this repository should know about

`oral/100-crucial-questions/internal/translation/Translation-guide-v3.md` is **damaged**. It is 15,009 bytes, valid UTF-8 for only its first 7,501, and binary garbage thereafter. It was committed already corrupt in `75df5d9` on 2026-08-20 and no intact revision exists in this repository's history. `Psych` holds an identical damaged copy.

Roughly half the bilingual terminology authority is unrecoverable — thought content, perception, mood and affect, insight, psychopharmacology and neuroanatomy are all in the lost portion.

The 65 salvageable rows are preserved in the core at [`terminology/en-el.yaml`](https://github.com/orestispsom/mental-health-core/blob/main/terminology/en-el.yaml), every one flagged as recovered from a damaged source. **Nothing was reconstructed.**

The file has been left exactly as it is. Whether to mark it as damaged in place, and whether an intact original exists outside git, are founder decisions — see [`OPEN_QUESTIONS.md` Q1](https://github.com/orestispsom/mental-health-core/blob/main/docs/OPEN_QUESTIONS.md).

Note also that `glossary/` is currently a README with no entries. The core's terminology file is the nearest thing to the controlled glossary that README describes.

## How to use it

**Look up a concept.** Human: `concepts/<slug>.md` in the core. Machine: `index/concepts.json`, which is the whole core in one file. Search `aliases` too.

**Reference by `id`, not by name.** `MHC-C-###` is permanent. Slugs can change; old ones move to `aliases`.

**Add local interpretation as an overlay.** An overlay names the core concept and adds what the core does not own — audience language, exam framing, product claims, UI labels, market state. It may add. It may not restate, narrow, or contradict the core definition.

**Contribute improvements by pull request** against the core. Do not fork a definition locally. If you need to contradict the core, that is a conflict, not an overlay.

**Pin to a tag.** Current release: `v0.1.0`.

## Two things the core will not do

**It will not approve a clinical claim.** All 30 V0 concepts are `READY_FOR_FOUNDER_REVIEW`. Nothing has been clinically reviewed, so nothing in the core licenses a public clinical claim yet.

**It will not supply market evidence.** The core has no market fields and never will. Clinical plausibility is not demand, whitespace, or opportunity.

## Telling evidence from heuristic from hypothesis

Every concept carries three separate fields, which must not be collapsed:

| Field | Question |
|---|---|
| `epistemic_status` | What kind of knowledge is this? |
| `certainty` | How confident, within that kind? |
| `review.state` | Has a qualified human signed it off? |

The five epistemic values — `ESTABLISHED_EVIDENCE`, `SUPPORTED_CLINICAL_PRINCIPLE`, `EXPERT_PRACTICE`, `BTB_CLINICAL_HEURISTIC`, `SPECULATIVE` — are the ones already in use in `btb-intelligence`, adopted unchanged.

## Avoiding a second conflicting definition

Before defining a shared clinical term in this repository, search the core index including aliases.

- exists and is right → reference it;
- exists and is wrong → pull request against the core;
- exists but you need local framing → overlay;
- does not exist and two repositories need it → propose it;
- does not exist and only this repository needs it → keep it local.

## Reference

- Audit that produced this: [`docs/AUDIT-2026-09-06.md`](https://github.com/orestispsom/mental-health-core/blob/main/docs/AUDIT-2026-09-06.md)
- Ownership matrix: [`docs/OWNERSHIP_MATRIX.md`](https://github.com/orestispsom/mental-health-core/blob/main/docs/OWNERSHIP_MATRIX.md)
- Consuming guide: [`docs/CONSUMING.md`](https://github.com/orestispsom/mental-health-core/blob/main/docs/CONSUMING.md)
- Conflict rules: [`docs/SOURCE_PRECEDENCE.md`](https://github.com/orestispsom/mental-health-core/blob/main/docs/SOURCE_PRECEDENCE.md)
- Contributing: [`CONTRIBUTING.md`](https://github.com/orestispsom/mental-health-core/blob/main/CONTRIBUTING.md)
