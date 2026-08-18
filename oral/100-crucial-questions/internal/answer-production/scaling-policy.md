# Model-Answer Production — Scaling Policy

Status: active production rule after Q12 pilot timing review.

## Problem identified

The first contemporary Q12 research pass was intentionally exhaustive and took more than 15 minutes. That depth is useful for calibrating the pipeline, but repeating 100 independent literature-review-style searches would make production impractical and would duplicate the same source retrieval many times.

The production system must preserve source quality while reducing repeated work.

## Core scaling principle

**Research deeply once per domain/source family; research incrementally per question.**

Question dossiers remain separate, but source retrieval should be reused whenever several questions depend on the same authoritative material.

Do not perform 100 independent mini-systematic reviews.

## 1. Domain evidence packets

Create reusable contemporary evidence packets for coherent clusters of questions. A packet records authoritative sources, major current positions, stable claim IDs and update-sensitive issues shared by multiple questions.

Suggested clusters:

1. assessment / psychopathology / suicide / emergencies;
2. schizophrenia spectrum and psychosis;
3. depression / bipolar / perinatal psychiatry;
4. anxiety / OCD / trauma / dissociation / somatic presentations;
5. substance-use and addictive disorders;
6. delirium / neurocognitive / old-age / neuropsychiatry / liaison;
7. adult neurodevelopment / eating / sleep / personality / sexual psychiatry;
8. antipsychotic and antidepressant psychopharmacology;
9. mood stabilisers / ADHD medication / pregnancy / toxic syndromes / ECT;
10. psychotherapies;
11. neuroscience / evidence appraisal / ethics / forensic / systems.

Clusters may be split when source sets diverge substantially.

## 2. Three research-intensity tiers

### Tier A — full current verification

Use for claims where error or staleness could materially affect safety, law or treatment:

- psychopharmacology dose/monitoring/interactions/toxicity;
- pregnancy/reproductive safety;
- current treatment sequencing and treatment resistance;
- emergencies;
- law, consent, confidentiality and forensic rules;
- new or rapidly changing interventions;
- regulatory/licensing questions.

These questions may justify substantial dedicated research, but should still reuse domain sources already inspected.

### Tier B — focused authoritative update

Use for diagnosis, course, differential diagnosis and common clinical syndromes where current authority matters but the source set is relatively stable.

Typical method:

- reuse the domain packet;
- inspect the relevant DSM/ICD/guideline section;
- retrieve only question-specific supporting evidence;
- stop once answer-coverage and board-fact requirements are resolved.

Do not repeat broad searches already completed for adjacent questions.

### Tier C — stable foundational synthesis

Use for stable psychopathology, classic neuroanatomy, established psychotherapy concepts or other low-volatility foundational material.

Use authoritative textbooks/consensus sources already in the domain packet unless a specific claim is uncertain or contested. Web research is not mandatory merely for volume.

## 3. Batch source retrieval, separate question outputs

Research agents may receive a coherent batch of adjacent questions when the authoritative sources overlap heavily.

Example: Q11–Q19 schizophrenia/psychosis.

One retrieval pass may inspect:

- DSM-5-TR/APA schizophrenia-spectrum material;
- WHO ICD-11 primary psychotic disorders;
- current psychosis/schizophrenia guidelines;
- negative-symptom and cognition consensus evidence;
- FEP/course/TRS/clozapine sources where relevant.

The agent should then write **separate question source packets**, each containing only the claims required for that question.

Batch retrieval must not produce one giant undifferentiated research document.

## 4. Local-textbook scaling

The same principle applies to Claude/local sources.

When several questions occupy the same Oxford chapter:

1. inspect the chapter/index thoroughly once;
2. maintain a reusable internal chapter map of relevant sections/pages;
3. extract separate Q-specific packets from that map;
4. reopen sections only when the exact context needs checking;
5. do not re-search/re-read the same chapter from scratch for every question.

Oxford remains first in the local-source stream. Supplementary books remain targeted.

## 5. Source cache / reuse rule

If an authoritative source was already inspected for a domain packet or earlier question:

- reuse its verified bibliographic/source identity;
- reuse claims only when the cited section genuinely supports the new question;
- reopen the relevant section if the new claim is more specific than the previously recorded extraction;
- never infer support from source title alone.

A reused source does not require a new general web search.

## 6. Stop rule

Research stops when:

- every `must_cover` item has adequate authoritative support;
- every assigned board-fact anchor has a verification route;
- conflicts relevant to the final answer are identified;
- no unresolved high-priority claim remains;
- additional sources are adding detail rather than changing conclusions.

Do not continue merely to maximise citation count.

## 7. Pilot versus production depth

The first five heterogeneous pilot questions may receive greater scrutiny because they are validating the workflow itself.

After the pilot:

- freeze the source hierarchy and dossier/writer format;
- convert repeated source work into domain packets;
- use question-specific delta research;
- reserve exhaustive deep dives for Tier A/high-uncertainty claims.

## 8. Quality must not be traded for speed

Efficiency means avoiding duplicated retrieval, not weakening authority.

Never speed up by:

- relying on search snippets;
- replacing DSM/ICD/guidelines with generic clinical websites;
- copying old `Psych` answers as authority;
- skipping current verification of psychopharmacology/law/regulation;
- allowing the writer to fill research gaps from memory.

## Practical target

The production objective is that one substantial domain research pass should support multiple related questions. Per-question work should usually become targeted extraction/adjudication rather than a fresh literature review.

No fixed wall-clock guarantee is imposed because question complexity and source accessibility vary; production is judged by avoiding redundant work while preserving the project's accuracy gates.
