# 100 Crucial Questions — Internal Source Register

Status: living provenance record for coverage design. This file records what has been reviewed and how each source may influence the guide.

## Source hierarchy for this project

### A. Greek board-exam specific material — highest exam-specific value

**Source:** `orestispsom/Psych` repository

Role:
- canonical, continuously updated source for the psychiatry board-exam app;
- oral-question bank and oral-simulator material;
- actual / recalled exam questions and examiner-associated themes where provenance exists;
- existing question-answer audit material.

Use:
- verify that known Greek oral-exam themes are represented in the 100-question architecture;
- identify recurrent examiner probes and high-yield discriminations;
- distinguish genuine past-exam material from generated practice material wherever provenance permits.

Do not:
- copy old answers uncritically into the final guide;
- treat older treatment, dose, legal or monitoring statements as automatically current.

### B. Crash Course Psychiatry, 5th ed. (2019) — broad clinical coverage check

**Scope reviewed for this project:** textbook content through PDF page 268 only. Material after that point is self-assessment / answer material and is excluded from the current coverage audit.

Important structural observations used:
- substantial emphasis on presenting complaints and clinical syndromes rather than only disease chapters;
- distinct coverage of suicide/self-harm, cognition, substances, psychosis, mania, depression, anxiety, OCD, stress reactions, somatic presentations, eating disorders, personality, neurodevelopment, sleep, psychosexual disorders, reproductive psychiatry, child/adolescent psychiatry, old-age psychiatry and forensic psychiatry;
- separate foundational sections on assessment, pharmacological/ECT treatment, psychological therapy, law and service provision.

Role:
- detect major clinical domains accidentally omitted from the 100;
- compare relative breadth and granularity across psychiatric domains;
- identify topics that deserve at least internal coverage even when they do not merit a main question.

Limitations:
- undergraduate / junior-doctor orientation rather than specialist-board depth;
- 2019 edition, so treatment, classification, law and prescribing details may be outdated;
- UK-centred legal/service material does not define Greek current practice;
- child/adolescent chapters must not be allowed to inflate main-question allocation for an Adult Psychiatry certification examination.

### C. Attempt 005 local textbook coverage audit — broad specialist-level triangulation

**Audit file:** `oral/100-crucial-questions/reviews/005-textbook-coverage-audit.md`

**Sources actually inspected:**
- Oxford Shorter Textbook of Psychiatry, 7th ed. (2017 copyright; 2018 printing);
- Oxford New Textbook of Psychiatry, 3rd ed. (2020);
- Kaplan & Sadock's Synopsis of Psychiatry (2021);
- DSM-5-TR (2022) classification/diagnostic chapter structure.

Method:
- local-file, read-only audit performed by Claude;
- TOC/front-matter extraction, targeted text search and selected page-range retrieval rather than linear reading;
- compared an independently derived textbook domain map with `internal/core-coverage.yml` and Attempt 005.

Main findings accepted as coverage signals:
- no missing CORE domain identified in the canonical coverage bank;
- Attempt 005 broadly proportionate across major textbook domains;
- carbamazepine likely over-weighted as a standalone main question;
- gender dysphoria / gender-identity-related psychiatric care under-sampled in Attempt 005;
- negative/cognitive schizophrenia symptoms, non-dementia Parkinson psychiatry, OCD-related disorders, other personality disorders and rTMS deserve deliberate sampling review;
- intimate-partner/domestic violence identified as a candidate gap in the canonical bank.

Limitations:
- this was a coverage/weighting audit, not treatment-guideline verification;
- textbook chapter prominence does not automatically determine Greek oral-exam weighting;
- findings should influence the canonical bank only when they pass the project's independent inclusion rule.

### D. Current Greek legal, ethical and service-system applicability audit

**Audit file:** `oral/100-crucial-questions/reviews/008-greece-applicability-audit.md`

Sources checked included current Greek medical-ethics, involuntary-care, penal-law, child-protection and mental-health-service materials.

Role:
- prevent UK, US or other foreign legal/service frameworks from being silently imported into Greek specialist-board answers;
- identify which clinically universal questions require Greek-law or Greek-system verification when answers are written;
- distinguish international clinical evidence from national law, regulation, licensing and service organisation.

Main implications:
- involuntary care must be answered from current Greek law;
- informed consent should use Greek law rather than treating a foreign capacity test as statute;
- safeguarding/reporting must use current Greek duties/pathways when relevant;
- ECT without valid consent is legally sensitive and must not import UK Mental Health Act or US substitute-consent rules;
- confidentiality must use the Greek Code of Medical Ethics; Tarasoff-style duty-to-warn language is not assumed to be Greek law;
- criminal responsibility must use Greek concepts and current Greek Penal Code rather than foreign tests;
- community-care answers may use universal recovery principles, but concrete service-organisation claims should describe the current Greek system rather than defaulting to NHS or US models.

### E. Greek oral-question phrasing and Adult Psychiatry scope audit

**Audit file:** `oral/100-crucial-questions/reviews/009-greek-oral-phrasing-adult-scope-audit.md`

**Sources inspected:**
- `orestispsom/Psych/src/data/oral.js`
- `orestispsom/Psych/src/data/oralCore.js`
- `orestispsom/Psych/ORAL_QUALITY_AUDIT.md`

Role:
- calibrate visible question wording to the cadence of the Greek oral examination;
- distinguish the curated Greek oral bank from broader simulator-generated coverage;
- enforce that the target certification is **Adult Psychiatry**, not Child and Adolescent Psychiatry.

Observed viva cadence:
- short direct prompts such as `Ποια ...;`, `Πώς ...;`, `Τι είναι ...;`, `Τι ξέρετε για ...;`, `Περιγράψτε ...`;
- brief vignettes followed by `Πώς θα τον/την προσεγγίσετε;`;
- a broad but coherent anchor followed by short examiner probes rather than a written syllabus-style headline.

Adult-scope findings:
- the curated 129-question oral bank is overwhelmingly Adult Psychiatry;
- autism has a dedicated curated oral block;
- the broader `oralCore.js` simulator additionally includes ADHD, autism and Tourette, but simulator breadth is not by itself authority for Adult Psychiatry main-slot allocation;
- dedicated main questions on general child/adolescent assessment, child-only disruptive disorders and adolescent depression were not supported strongly enough to justify scarce Adult Psychiatry slots.

Reallocation accepted for Attempt 010:
- remove dedicated main slots for general child assessment, child abuse/neglect as a child-psychiatry topic, Tourette/tics, ODD/conduct disorder and adolescent depression;
- retain ADHD, autism and intellectual disability with explicit **adult** framing;
- use the five freed slots for sleep stages/EEG, apathy versus depression, Charles Bonnet syndrome, psychoeducation and clinically important psychotropic interactions.

### F. Current major examination / curriculum frameworks — secondary completeness check

Role:
- check for broad specialty domains that neither the Greek oral bank nor a single textbook may emphasize;
- identify expected specialist knowledge categories such as special populations, forensic psychiatry, neuroscience, evidence appraisal and systems of care.

Use cautiously:
- these frameworks do not determine the exact weighting of the Greek oral boards;
- they should not force low-value curriculum headings into the 100 main questions.

### G. Future source categories

To add as reviewed in greater depth where needed:
- DSM-5-TR / ICD-11 for diagnosis and classification;
- Maudsley Prescribing Guidelines 15th for psychopharmacology;
- Stahl for mechanisms / psychopharmacology framing where appropriate;
- current authoritative treatment guidelines;
- further current Greek legal / regulatory sources as answers are written;
- recovered English–Greek psychiatry and neuroanatomy terminology guide.

## Coverage-review rule

Every source review should record:

- source and edition/version;
- pages / chapters / file scope actually examined;
- what it contributes: exam provenance, clinical coverage, diagnostic authority, treatment authority, terminology, law, etc.;
- important new topics or weighting changes identified;
- conflicts with existing guide assumptions;
- whether the finding affects MAIN questions, FOLLOW_UP prompts, ANSWER_COVERAGE only, or no change.

## Current design implications already established

- The target exam is Greek **Adult Psychiatry** specialist certification.
- Clinical entities and presentations should dominate the 100.
- Questions should sound like viva prompts, not polished written curriculum headings.
- Suicide requires both acute risk-assessment competence and broader suicide knowledge.
- Psychopharmacology requires substantial independent space, especially clozapine, lithium, valproate, antipsychotic adverse effects, clinically important interactions, major toxicity syndromes and ECT.
- Adult neurodevelopmental psychiatry remains represented through adult ADHD, adult autism and adult intellectual-disability assessment.
- Child/adolescent-only material remains in canonical/supporting coverage but should not displace stronger Adult Psychiatry topics without direct exam evidence.
- Reproductive psychiatry, sleep, eating disorders, old-age psychiatry, liaison and forensic psychiatry must not disappear through over-compression.
- Basic science and service topics should remain represented but should not displace higher-value clinical questions merely to mirror a curriculum table of contents.
- Source-derived candidate gaps should be staged and reviewed against the canonical inclusion rule before being promoted into `core-coverage.yml`.
- Law, consent, involuntary care, confidentiality, safeguarding and forensic rules are jurisdiction-specific and must use current Greek sources.
- International treatment evidence may be used, but Greek/EU licensing, regulation and actual service availability must be checked where relevant.
- Foreign service structures or legal doctrines may be discussed only as explicitly labelled comparisons, never as the default Greek answer.
