# Model-Answer Production — Scaling Policy

Status: active. Read together with `lean-workflow.md`.

## Core principle

**Do not perform 100 independent research projects. Do not triangulate multiple textbooks by default.**

Routine production should be:

`Oxford base extract → targeted current verification → compact answer brief → writer → coordinator QA`

## 1. One primary source by default

For most Adult Psychiatry board questions, **Shorter Oxford Textbook of Psychiatry, 7th ed. / 2017 exam edition** is the base source.

The base source should normally provide most of the answer structure and stable clinical content.

Open another textbook only if Oxford is insufficient, ambiguous, materially outdated for the question, or another source is clearly the appropriate specialist authority.

## 2. Targeted verification, not independent reconstruction

Current research should verify only claims that are plausibly stale, exact, safety-sensitive or classification-sensitive.

Typical verification targets:
- DSM-5-TR / ICD-11 criteria;
- current treatment sequencing;
- psychopharmacology dose/monitoring/interactions/toxicity/pregnancy;
- Greek law and forensic rules;
- rapidly changing interventions;
- important epidemiological or factual anchors where exactness matters.

A stable descriptive question may need only 2–5 checks.

## 3. Batch local extraction by chapter

When multiple questions share one Oxford chapter:
- map the chapter once;
- retain section/page locations locally;
- produce question-specific extracts from that map;
- do not repeat full search/retrieval for each question.

Examples:
- Q11–19 psychosis/schizophrenia;
- Q20–27 mood/perinatal;
- Q45–58 neurocognitive/neuropsychiatry.

## 4. Batch current sources by domain

Keep authoritative sources already inspected for the domain and reuse them when they genuinely support adjacent questions.

Do not rerun broad web searches for the same DSM/ICD/guideline material.

## 5. Agent economy

### Claude/local agent
Use for targeted local source retrieval only. Give a compact work order, not the entire project architecture. Default to Oxford only; add a second source only when explicitly required.

### Research GPT
Use for the current-authoritative delta, not a full literature review. Deep research is an escalation path.

### Writer
Use one dedicated writer from approved answer briefs.

### QA
Coordinator performs routine QA. Separate QA agents are reserved for high-risk or failed cases.

### Codex
Do not spend scarce coding-agent tokens on psychiatric research/prose. Use later for deterministic automation if useful.

## 6. Stop rule

Stop source work when:
- the Oxford base adequately covers the stable answer;
- required update-sensitive claims are verified;
- board facts have authoritative support;
- any material conflict is identified;
- additional sources would add detail rather than change the answer.

## 7. Escalation triggers

Use the heavier workflow only for:
- prescribing/monitoring/toxicity;
- pregnancy;
- emergencies;
- Greek law/forensic/confidentiality;
- rapidly changing treatment;
- genuine exam-current conflict;
- contested evidence central to the question.

## Practical target

After source reuse is established, routine question preparation should be a **short targeted production task**, not a 15–30 minute independent deep-research exercise.

Quality comes from choosing the right authority and verifying the vulnerable claims, not from maximizing the number of books, papers or agents consulted.
