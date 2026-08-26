# English ↔ Greek Psychiatry Translation Guide v4

**Status:** CURRENT HOUSE LANGUAGE AUTHORITY  
**Scope:** Greek Adult Psychiatry board preparation, oral answers, clinical/MSE prose, psychopharmacology, psychotherapy, neuropsychiatry/neuroanatomy, and future educational-product translation.  
**Branch at construction:** `greek-v5-scale`  

This guide consolidates the durable language work produced across the original terminology guide, terminology research, the neuroscience addendum, the five bilingual deep-read audits, the applied v3/v4 editorial passes, and the founder-calibrated Greek-first v5 work.

It is a **language authority, not a psychiatric-content authority**. It governs how an already verified English/semantic claim should be rendered in Greek. It must never override DSM/ICD criteria, guideline recommendation strength, regulatory wording, doses, legal rules, numerical thresholds, or source-specific uncertainty.

Historical translation files remain in the repository for provenance. Where this guide conflicts with an older guide or audit, **v4 governs Greek house language**. `Translation-guide-v3.md` is retained as historical evidence but is not a safe working master because its repository text is encoding-corrupted.

---

## 1. Authority and provenance

V4 uses the following hierarchy for language decisions:

1. **V5 founder-approved calibration** — highest authority for learner-facing Greek clinical discourse.
2. **Applied v5/v4 manuscript language** — especially changes that survived later editorial review.
3. **Applied v3 cumulative language correction** — the consolidated output of the five bilingual deep reads and cumulative QA.
4. **Settled terminology research / v2 terminology guide / neuroscience addendum.**
5. **Historical or recognition-only terminology.**
6. **REVIEW_ONLY candidates** — never promote these to preferred terminology without adjudication.

A later version may supersede this hierarchy, but older wording must not silently re-enter the manuscript merely because it appears in an earlier guide.

### Important example of supersession

Earlier v3 work accepted `ετεροαναφορικές πληροφορίες` / `ετεροαναφορικό ιστορικό`. Founder-calibrated v5 subsequently preferred ordinary clinical Greek:

- **`πληροφορίες από το περιβάλλον του ασθενούς`**
- shorter **`πληροφορίες από το περιβάλλον`** where the referent is obvious
- specify the source when useful: `από συγγενείς`, `από φροντιστές`, `από το νοσηλευτικό προσωπικό`, `από προηγούμενες καταγραφές`

`ετεροαναφορικό ιστορικό` remains recognisable specialist shorthand, but it is **not the default learner-facing house form**.

---

# 2. Core Greek clinical-language doctrine

## 2.1 Translate clinical meaning, not English morphology

A grammatically possible Greek word is not automatically good psychiatric Greek. Prefer the expression a Greek psychiatrist would naturally use in a viva, ward discussion, clinical note, or teaching setting.

Examples:

- `agitated patient` → **`διεγερμένος ασθενής`**, not `διεγερτικός ασθενής`
- `abnormal vital signs` → **`παθολογικά ζωτικά σημεία`**, not `επηρεασμένα ζωτικά σημεία`
- `physical examination` → **`σωματική εξέταση`**, not `φυσική εξέταση`
- `trajectory` → **`πορεία`**, not `τροχιά` in ordinary clinical prose
- `impaired renal function` → **`νεφρική δυσλειτουργία`** / `διαταραγμένη νεφρική λειτουργία`, not `επηρεασμένη νεφρική λειτουργία`

## 2.2 Read-aloud rule

Every learner-facing sentence should survive this test:

1. Would a strong Greek psychiatrist plausibly say it aloud to an examiner?
2. Does it add psychiatric information, prioritisation, or clinical reasoning?
3. Is it ordinary professional Greek rather than a visible translation of English syntax?

If not, rewrite the sentence rather than searching for a one-word substitution.

## 2.3 Clinical discourse is not an outline read aloud

Internal headings such as `setting`, `severity`, `monitoring`, `framework`, `first decision`, `next step`, `pathway`, and `approach` must not be mechanically converted into spoken transitions.

Avoid generated scaffolding such as:

- `Η πρώτη απόφαση είναι...`
- `Το επόμενο βήμα είναι...`
- `Η προσέγγιση οργανώνεται...`
- `Στην εξέταση θέλω να δείξω...`
- `Για τις εξετάσεις πρέπει...`
- repetitive `Δεν είναι απλώς... αλλά...`
- generic closing sentences that merely repeat the preceding paragraph

State the clinical reasoning directly.

## 2.4 Clinical causality determines sentence order

The linguistic sequence should reflect the clinical sequence:

- severity/risk assessment → decision about level of care
- identification of cause → etiological treatment
- phenomenology → differential diagnosis
- formulation/mechanism → psychotherapy intervention
- indication + patient factors → medication choice/monitoring

Do not announce a disposition, setting, or intervention before stating the information that justifies it.

## 2.5 Prefer active clinical verbs over translated abstract nouns

Prefer:

- `εκτιμώ`
- `ρωτώ`
- `ελέγχω`
- `αποκλείω`
- `λαμβάνω πληροφορίες`
- `συνθέτω`
- `παρακολουθώ`
- `προσαρμόζω`
- `συζητώ με τον ασθενή`

rather than chains of nominalisations derived from English clinical prose.

Example:

- poor: `η υπευθυνότητα για την παρακολούθηση`
- preferred: **`ποιος αναλαμβάνει την ευθύνη για την παρακολούθηση`**

## 2.6 Preserve modality, evidence strength, causality, and scope

Translation must not strengthen or weaken the source.

Keep these distinctions explicit:

- `may/can be considered` ≠ `ενδείκνυται` / `επιβάλλεται`
- `appropriate / attractive option` ≠ automatically `θεραπεία εκλογής`
- `important` ≠ automatically `απαραίτητο`
- `prompt consideration` ≠ `επιβάλλει την έναρξη`
- `associated with / implicated` ≠ `προκαλεί` / `ενοχοποιείται`
- `discriminating` ≠ `specific`
- `additive` ≠ `synergistic`
- `not suitable` ≠ `not tolerated`

Do not add intensifiers such as `σημαντικά`, `πολύ`, `πλήρης`, `εξαιρετικά`, or `αποκλειστικά` unless the semantic source contains that strength.

## 2.7 Do not add Greek-only content while translating

Do not insert local examples, legal criteria, mechanisms, service types, or explanatory claims merely because they make the Greek sound complete. Translation/naturalisation preserves the source claim; content enrichment requires its own authority.

## 2.8 Distinct psychopathological constructs remain distinct

Never collapse two constructs merely because Greek shorthand sometimes does so. Important examples:

- mood ≠ affect
- pressured speech ≠ logorrhea ≠ rapid speech
- circumstantiality ≠ tangentiality ≠ overinclusive thinking
- confabulation ≠ pseudomnesia ≠ paramnesia
- inappropriate affect ≠ mood-incongruent affect
- ambitendency ≠ ambivalence
- insight ≠ judgment ≠ reality testing ≠ decision-specific capacity
- cognitive function ≠ depressive cognitions / content of thought

---

# 3. Core psychopathology terminology

The clean `Translation-guide-v2.md` remains the underlying full MSE/psychopathology index. All of its entries remain valid **unless explicitly superseded in v4**. The following are the principal frozen or high-value house decisions that must not regress.

| English | Preferred Greek | Accepted / recognition form | Avoid / distinction |
|---|---|---|---|
| Mental state examination (MSE) | **Εξέταση παρούσας ψυχικής κατάστασης** | Ψυχική κατάσταση | — |
| Delirium | **Ντελίριο** | Οξύ συγχυτικό σύνδρομο | Do not force a translated neologism. |
| Mood | **Διάθεση** | — | Do not use `συναίσθημα` as a blanket equivalent. |
| Affect | **Συναίσθημα** / **συναισθηματική έκφραση** | θυμικό (historical/broader) | Keep distinct from mood. |
| Restricted affect | **Περιορισμένο συναίσθημα** | περίσφιξη / περιεσφιγμένο συναίσθημα (recognition) | Not blunted/flat affect. |
| Blunted affect | **Αμβλύ συναίσθημα** / **συναισθηματική άμβλυνση** | — | — |
| Flat affect | **Επίπεδο συναίσθημα** / **συναισθηματική επιπέδωση** | — | — |
| Inappropriate affect | **Απρόσφορο συναίσθημα** | — | Not mood incongruence. |
| Mood-incongruent affect/content | **Ασύμφωνο με τη διάθεση** | μη σύντονο προς τη διάθεση | Not `απρόσφορο`. |
| Circumstantiality | **Υπερλεπτομερειακή σκέψη** / υπερλεπτομερειακός λόγος | παρεκβατικός / λεπτολογικός λόγος; περιστασιακότητα (recognition) | Endpoint is eventually reached. |
| Tangentiality | **Εφαπτομενικότητα** / εφαπτομενικός λόγος | — | Endpoint is not reached. |
| Overinclusive thinking | **Υπερπεριεκτική σκέψη** | υπερεγκλειστικότητα | Never use `υπερλεπτομερειακή σκέψη`. |
| Loosening of associations | **Χαλάρωση συνειρμών** | χάλαση συνειρμών | Related to but not identical with derailment. |
| Derailment | **Εκτροχιασμός** | εκτροχιασμός σκέψης/λόγου | — |
| Flight of ideas | **Ιδεοφυγή** | φυγή ιδεών | — |
| Racing thoughts | **Καλπασμός σκέψεων** / υποκειμενικό αίσθημα επιτάχυνσης σκέψης | καλπάζουσες σκέψεις | Distinct from flight of ideas. |
| Thought blocking | **Ανακοπή σκέψης** | — | Avoid `μπλοκάρισμα` as canonical form. |
| Perseveration | **Εμμένουσα απάντηση / εμμένουσα σκέψη** according to modality | — | Avoid bare `εμμονή`; not obsession. |
| Poverty of thought | **Πενία σκέψης** | ιδεοπενία / πτωχεία σκέψης | — |
| Poverty of speech | **Πενία λόγου** | πτωχεία λόγου | Not alogia. |
| Poverty of content of speech | **Πενία περιεχομένου του λόγου** | — | — |
| Alogia | **Αλογία** | — | Broader negative-symptom construct. |
| Clang associations | **Ηχητικοί συνειρμοί** | συνειρμοί κατ’ ομοηχία | Avoid `κλαγγικοί`. |
| Word salad | **Σαλάτα λέξεων** | λεκτική σαλάτα; σχιζοφασία (historical/broader) | Severe incoherence, not a disease entity. |
| Thought insertion | **Παρεμβολή ξένων σκέψεων / παρεμβολή σκέψης** | επιβολή σκέψης | Avoid `πρόσδοση`. |
| Thought withdrawal | **Απόσυρση της σκέψης** | υφαρπαγή / αφαίρεση σκέψης | — |
| Thought broadcasting | **Εκπομπή της σκέψης** | μετάδοση / διάδοση της σκέψης | — |
| Obsession | **Ιδεοληψία** | — | Not perseveration or rumination. |
| Rumination | **Ιδεομηρυκασμός** | μηρυκασμός | Not perseveration. |
| Delusional misidentification | **Παραληρητική παραγνώριση** | παραληρητικές ψευδοαναγνωρίσεις | Thought-content/delusional domain, not perception. |
| Confabulation | **Μυθοπλασία (μνημονική)** | descriptive: μυθοπλαστική συμπλήρωση μνημονικών κενών | Not pseudomnesia. |
| Pseudomnesia | **Ψευδομνησία** | ψευδής μνήμη | Not confabulation. |
| Paramnesia | **Παραμνησία** | — | Broader qualitative memory distortion. |
| Pseudohallucination | **Ψευδοψευδαίσθηση** | ψευδο-ψευδαίσθηση (source recognition) | Historical/contested; describe phenomenology rather than use as psychosis boundary. |
| Cenesthetic hallucination | **Κοιναισθητική ψευδαίσθηση** | — | Keep distinct from somatic/visceral. |
| Somatic hallucination | **Σωματική ψευδαίσθηση** | σωματοαισθητική ψευδαίσθηση | — |
| Visceral hallucination | **Σπλαγχνική ψευδαίσθηση** | — | — |
| Pressured speech | **Πίεση λόγου** | πίεση στην ομιλία | Not logorrhea. |
| Logorrhea | **Λογόρροια** | — | Not pressured speech. |
| Rapid speech | **Ταχεία ομιλία / αυξημένος ρυθμός ομιλίας** | ταχύς λόγος | `ταχυλαλία/ταχυφημία` mainly speech-pathology/cluttering contexts. |
| Aprosodia | **Απροσωδία** | — | Not dysprosodia. |
| Dysprosodia | **Δυσπροσωδία** | — | Not aprosodia. |
| Psychomotor agitation | **Ψυχοκινητική διέγερση** | — | — |
| Stupor | **Εμβροντησία** | κατατονικό stupor (recognition) | Historical but board-recognisable. |
| Posturing | **Κατατονική στάση / διατήρηση στάσης** | — | Distinct from catalepsy. |
| Catalepsy | **Καταληψία** | — | — |
| Waxy flexibility | **Κηρώδης ευκαμψία** | — | — |
| Ambitendency | **Κινητική αμφιταλάντευση (ambitendency)** | αμφιβουλησία / αμφιπραξία (historical recognition) | Never `αμφιθυμία` / `αμφισθένεια`. |
| Insight | **Εναισθησία** | — | Not judgment/capacity/reality testing. |
| Judgment | **Κρίση** | — | Not insight/capacity. |
| Reality testing | **Έλεγχος πραγματικότητας** | — | Not insight. |
| Decision-making capacity | **Ικανότητα λήψης συγκεκριμένης απόφασης** | ικανότητα για συναίνεση (context) | Decision-specific and jurisdiction-sensitive. |
| Informed consent | **Ενημερωμένη συναίνεση** | — | — |
| Disinhibition | **Άρση αναστολών** | αποαναστολή | — |
| Self-harm | **Αυτοτραυματισμός** | αυτοβλαπτική συμπεριφορά | Not automatically suicidal. |
| Risk formulation | **Διατύπωση / σύνθεση εκτίμησης κινδύνου** | — | Prefer formulation over categorical `risk level`. |
| Safety behaviours | **Συμπεριφορές ασφάλειας** | — | V4 applied form. |
| Dissociative phenomena | **Διασχιστικά φαινόμενα** | — | Avoid generic `αποσυνδετικά` when the psychopathological construct is meant. |

---

# 4. Founder-locked natural clinical Greek

These are not merely dictionary mappings. They represent later calibration of how psychiatric concepts should actually be expressed in Greek prose.

| English / concept | Preferred Greek | Superseded / avoid | Status / note |
|---|---|---|---|
| collateral information/history | **πληροφορίες από το περιβάλλον του ασθενούς**; specify source when useful | `παράπλευρες πληροφορίες`; default learner-facing `ετεροαναφορικές πληροφορίες` | **FOUNDER_LOCKED**. `ετεροαναφορικό ιστορικό` remains recognisable shorthand, not default prose. |
| autonomic hyperactivity | **υπερδραστηριότητα του αυτόνομου νευρικού συστήματος** | `αυτόνομη υπερδραστηριότητα` when it reads as a calque | **FOUNDER_LOCKED** |
| agitated state/patient | **ψυχοκινητική διέγερση**; `διεγερμένος ασθενής` | `διεγερτικός ασθενής` | **FOUNDER_LOCKED / APPLIED** |
| safety | **ασφάλεια** | awkward nominal protective-language calques | **FOUNDER_LOCKED** |
| hyperactive/hypoactive/mixed delirium | **υπερκινητικό / υποκινητικό / μικτό ντελίριο** | unnecessary invented alternatives | **FOUNDER_ACCEPTED** |
| working hypothesis | **υπόθεση εργασίας** | coined abstract compounds | **FOUNDER_EXAMPLE** |
| presenting complaint | **κύρια αιτία προσέλευσης**; `κύριο αίτημα/πρόβλημα` by context | `κύρια ενόχληση` | **APPLIED** |
| forensic history | **δικαστικό/ποινικό ιστορικό** where justice history is meant | `ιατροδικαστικό ιστορικό` | `ιατροδικαστικός` belongs to forensic-medicine context. |
| disposition | **απόφαση για το πλαίσιο της περαιτέρω φροντίδας** | `διευθέτηση` | Prefer explicit clinical action. |
| follow-up responsibility | **ποιος αναλαμβάνει την ευθύνη για την παρακολούθηση** | `η υπευθυνότητα για το follow-up` | Active clinical Greek. |
| earliest appropriate opportunity | **το συντομότερο δυνατό, όταν είναι κλινικά κατάλληλο** | `στην πρωιμότερη κατάλληλη ευκαιρία` | — |
| emergency | **ιατρικό/ψυχιατρικό επείγον** | `επείγουσα ανάγκη` where the noun means emergency | Contextual. |
| treatment at lower licensed range | **στο κατώτερο άκρο του εγκεκριμένου δοσολογικού εύρους** | translated `lower-end` constructions | — |
| low mood | **χαμηλή διάθεση** | `πεσμένη διάθεση` in formal learner-facing prose | — |
| libido | **σεξουαλική επιθυμία (libido)** on first use if useful | mixed `μειωμένη libido` | — |

---

# 5. High-value anti-calque translation memory

## 5.1 Educational and editorial English

| English | Preferred Greek strategy | Avoid |
|---|---|---|
| high-yield | Translate the actual function: **ιδιαίτερα σημαντικό εξεταστικό σημείο**, `υψηλής εξεταστικής αξίας`, `βασικό σημείο`, `σημαντική διαφορική διάγνωση` | automatic `υψηλής απόδοσης` |
| practical / operational | **πρακτικό**, `εφαρμόσιμο`, `λειτουργικό`, `ταξινομικό`, or rewrite the clause | automatic `επιχειρησιακό` |
| framework / architecture | **πλαίσιο**, `δομή`, `διαχρονική δομή`, `δομή κριτηρίων` according to meaning | literal `αρχιτεκτονική` in ordinary diagnostic prose |
| benchmark / anchor | **πρακτικό σημείο αναφοράς**, `λειτουργικό κριτήριο`, `συμβατικό σημείο αναφοράς` | inflate to `ορισμός` if source says anchor/benchmark |
| pathway (care/treatment) | **θεραπευτική ακολουθία**, `αλγόριθμος αντιμετώπισης`, `πορεία φροντίδας`, sometimes `θεραπευτική διαδρομή`; often rewrite as a verb | automatic `μονοπάτι` / `διαδρομή` |
| pathway (biological/signalling) | biological `οδός` / established pathway term | do not apply the care-pathway rule mechanically |
| standard of care | **καθιερωμένη πρακτική / πρότυπο φροντίδας** according to context | unnecessary English parenthesis when Greek is clear |
| practice-changing | **ικανός να μεταβάλει την κλινική πρακτική** | `ανατρεπτικός για την πρακτική` |

## 5.2 Patient history, course and clinical state

| English | Preferred Greek | Avoid / distinction |
|---|---|---|
| clinical baseline | **συνήθες/προηγούμενο επίπεδο λειτουργικότητας**, `προϋπάρχον γνωστικό επίπεδο`; for measurements **αρχικές τιμές** | default `γραμμή βάσης` / `βάση αναφοράς` |
| longitudinal course | **διαχρονική πορεία** / `διαχρονική εικόνα` | awkward `διαμήκης αρχιτεκτονική` |
| trajectory | **πορεία** | `τροχιά` in ordinary clinical prose |
| unfolds / emerges over time | **διαμορφώνεται**, `καθίσταται σαφέστερο`, `εμφανίζεται` | literal `ξεδιπλώνεται` |
| trait-like | **σταθερό, αναπτυξιακό και όχι επεισοδιακό πρότυπο** where that is the meaning | `χαρακτηρολογικό` if it falsely implies personality pathology |
| cross-situational | **παρουσία σε περισσότερα από ένα περιβάλλοντα/πλαίσια** | `διακαταστασιακό` |
| state effect | **επίδραση της τρέχουσας κλινικής κατάστασης** | `επεισοδιακή κατάσταση` as a pseudo-term |
| intercurrent illness | **οξεία συνυπάρχουσα / παρεμπίπτουσα νόσος**, often simply `οξεία νόσος` | `διατρέχουσα νόσος`; narrowing to `λοίμωξη` unless source says infection |
| spontaneous (clinical occurrence) | **αυτόματα εμφανιζόμενος**, `αυθόρμητος`, or explanatory phrase according to meaning | automatic `αυτόματος` |
| waking pulse | **σφυγμός κατά την εγρήγορση** | `σφυγμός ηρεμίας` if source specifically says waking |

## 5.3 Engagement, collaboration and service language

| English | Preferred Greek | Avoid / note |
|---|---|---|
| engagement — therapeutic | **θεραπευτική συνεργασία**, `θεραπευτική σχέση`, `διατήρηση θεραπευτικής επαφής` | generic `θεραπευτική σύνδεση` |
| engagement with services | **επαφή / σύνδεση με τις υπηρεσίες**, `διατήρηση επαφής με τις υπηρεσίες` | force `θεραπευτική συνεργασία` when the object is the service system |
| shared decision-making | **από κοινού λήψη αποφάσεων** / **συνεργατική λήψη αποφάσεων** | `συν-απόφαση`, `συν-διαμόρφωση απόφασης` |
| safeguarding | usually **προστασία** of the relevant vulnerable person/group | automatic abstract `διασφάλιση` |
| proactive | **ενεργά**, `συστηματικά`, `εκ των προτέρων` or a context-specific phrase | automatic `προληπτικός` |
| proactive liaison | **ενεργητική/συστηματική διασυνδετική προσέγγιση** or rewrite as active case-finding | `προληπτική διασυνδετική` unless prevention is actually meant |
| aftercare | **συνέχιση της φροντίδας / επανεκτίμηση και παρακολούθηση** | `μετανοσοκομειακή φροντίδα` if source is not limited to inpatient discharge |

## 5.4 Diagnosis and assessment language

| English | Preferred Greek | Avoid / distinction |
|---|---|---|
| screening | **ανίχνευση**, `έλεγχος ανίχνευσης`, `σύντομη αξιολόγηση`, context-dependent | automatic `προσυμπτωματικός έλεγχος`; use that only when genuinely presymptomatic |
| cognitive screening | **σύντομη γνωστική αξιολόγηση / εργαλεία ανίχνευσης γνωστικής διαταραχής** | `μέσα διαλογής` if unnatural |
| formal neuropsychological testing | **πλήρης / τυπική νευροψυχολογική αξιολόγηση** | `επίσημος νευροψυχολογικός έλεγχος` |
| rule-in diagnosis | **θετική διάγνωση που βασίζεται σε χαρακτηριστικά κλινικά σημεία** | `διάγνωση ένταξης` |
| qualifying trauma | **τραυματικό γεγονός που πληροί το σχετικό διαγνωστικό κριτήριο** | `κατάλληλο τραύμα` |
| scrutiny (social anxiety) | **υπό παρατήρηση, κριτική ή αρνητική αξιολόγηση** according to sentence | `εξονυχιστικός έλεγχος` |
| feared outcome | **φοβούμενη συνέπεια / φοβούμενη έκβαση** | `φοβικό αποτέλεσμα` |
| proportionate investigation | **παρακλινικός έλεγχος ανάλογος με την κλινική εικόνα** | `αναλογικός έλεγχος` |
| abnormal vital signs | **παθολογικά ζωτικά σημεία** | `επηρεασμένα ζωτικά σημεία` |
| perceptual modality | **αισθητηριακή τροπικότητα**; often simply `ακουστική/οπτική κ.λπ.` | `αισθητηριακή διατροπικότητα` |
| held with conviction | Recast actively: **το άτομο υποστηρίζει/πιστεύει... με ... βεβαιότητα** | `διακρατείται` / `διακρατούμενη πεποίθηση` |
| diagnostically privileged | **έχει ιδιαίτερη/προνομιακή διαγνωστική βαρύτητα** | `διαγνωστικά προνομιακό` |
| discriminating clue | **διαγνωστικά χρήσιμο / διακριτικό κλινικό στοιχείο** | strengthen to `ειδικό` unless specificity is actually claimed |

## 5.5 Risk and emergency language

| English | Preferred Greek | Avoid |
|---|---|---|
| situational context | **πλαίσιο της κατάστασης / συνθήκες του περιστατικού** | `περιστασιακό πλαίσιο` if it suggests occasional |
| dynamic risk drivers | **δυναμικοί παράγοντες που διαμορφώνουν/επηρεάζουν τον κίνδυνο** | mechanical `κινητήριοι παράγοντες` |
| operational management plan | **σαφές, πρακτικό και εφαρμόσιμο πλάνο διαχείρισης** | `επιχειρησιακό πλάνο` |
| escalated the patient | **οδήγησε σε κλιμάκωση της διέγερσης/επιθετικότητας** | transitive `κλιμάκωσε τον ασθενή` |
| de-escalates behaviour | **μειώνει / ηρεμεί τη συμπεριφορά** when that is the meaning | overuse `αποκλιμακώνει` as a literal verb |
| police conveyance | **μεταφορά από την αστυνομία / αστυνομική μεταφορά** | `μεταγωγή` unless custodial/legal context specifically requires it |
| aggressive supportive care | **άμεση και εντατική υποστηρικτική φροντίδα/αντιμετώπιση** | `επιθετική υποστηρικτική φροντίδα` |
| may resemble/mimic an emergency | **μπορεί να μιμείται / να προσομοιάζει / να συγχέεται με** | `υποδύεται` |

## 5.6 Substance-use and addiction language

| English | Preferred Greek | Avoid / distinction |
|---|---|---|
| intoxication — generic substance term | **τοξίκωση** | generic `μέθη` outside alcohol-specific context |
| polysubstance use | **πολλαπλή / ταυτόχρονη χρήση ουσιών** | `πολυτοξικομανία` |
| binge use | **επεισοδιακή βαριά / υπερβολική χρήση** | `κατάχρηση` as automatic equivalent |
| craving | **έντονη επιθυμία για χρήση (craving)** | — |
| withdrawal syndrome | **σύνδρομο στέρησης** | bare `στέρηση` when the syndrome is meant and ambiguity matters |
| precipitated withdrawal | **προκληθέν σύνδρομο στέρησης / προκληθείσα οξεία στέρηση** | `εκλυόμενη στέρηση` |
| sustained cessation | **διατηρούμενη αποχή / σταθερή διακοπή της χρήσης** | literal `παρατεταμένη διακοπή` when abstinence is meant |
| reserve medication for selected cases | **χρησιμοποιώ μόνο σε επιλεγμένες περιπτώσεις** | `διατηρώ το φάρμακο` |
| motivational work | **κινητοποιητικές παρεμβάσεις** | `συνεντευξιακή κινητοποίηση`; use `κινητοποιητική συνέντευξη` only for Motivational Interviewing |
| lapse | **μεμονωμένο επεισόδιο επαναχρήσης (lapse)** on first use when distinction matters | literal `ολίσθημα` as default house prose |
| diversion | **παράνομη διάθεση της συνταγογραφούμενης αγωγής σε τρίτους (diversion)**; later `παράνομη διάθεση` | `διασπορά` |
| take-home naloxone | **ναλοξόνη για κατ’ οίκον / κοινοτική χρήση** | `ναλοξόνη για το σπίτι` in formal prose |
| contingency management | **REVIEW_ONLY:** retain `contingency management` with concise explanatory Greek if no settled house term is available | do not promote `διαχείριση ενδεχομένων` merely because it is literal |

## 5.7 Psychopharmacology and regulatory language

| English | Preferred Greek | Avoid / distinction |
|---|---|---|
| Summary of Product Characteristics (SmPC) | **Περίληψη Χαρακτηριστικών του Προϊόντος (ΠΧΠ/SmPC)** | `φύλλο οδηγιών` (patient leaflet) |
| drug-specific / product-specific | **εξαρτάται από το συγκεκριμένο φάρμακο/προϊόν**, `διαφέρει ανάλογα με...`, `ειδικός για το συγκεκριμένο φάρμακο` | `φαρμακοειδικός` |
| patient-specific | **εξαρτάται από τα χαρακτηριστικά του συγκεκριμένου ασθενούς** | `ασθενοκεντρικός` unless patient-centred care is actually meant |
| treatment-emergent | **που εμφανίστηκε κατά τη θεραπεία / μετά την έναρξη της θεραπείας** | `αναδυόμενος από θεραπεία` |
| loading dose | **δόση φόρτισης** | `δόση εφόδου` |
| oral overlap | **παράλληλη από του στόματος αγωγή** | literal `από του στόματος επικάλυψη` |
| fixed-dose regimen | **προκαθορισμένο δοσολογικό σχήμα / σχήμα προκαθορισμένων δόσεων** | `σχήμα σταθερής δόσης` if it implies one unchanged dose |
| induction/initiation of treatment | **έναρξη της θεραπείας** | `εισαγωγή` when English means initiation |
| therapeutic drug monitoring (TDM) | **θεραπευτική παρακολούθηση συγκεντρώσεων/επιπέδων του φαρμάκου (TDM)** | vague `παρακολούθηση επιπέδων στο αίμα` when a specific drug is intended |
| apparent volume of distribution | **φαινομενικός όγκος κατανομής** | `φαινόμενος όγκος κατανομής` |
| primary agonist site | **κύρια θέση πρόσδεσης του αγωνιστή** | `πρωτοταγής θέση του αγωνιστή` |
| de-induction | **άρση της ενζυμικής επαγωγής** where that is the intended pharmacokinetic process | `απο-επαγωγή` |
| prolactin-sparing | **σχετικά μικρή επίδραση στην προλακτίνη / μικρότερη τάση αύξησης της προλακτίνης** | `προστατευτικό` unless actual protective mechanism is claimed |
| coercive option | **εξαναγκαστική επιλογή** | `κατασταλτική επιλογή` |
| additive effect | **αθροιστική επίδραση** | `συνεργική` unless synergy is explicitly claimed |
| subtype preference | **προτίμηση για ορισμένους υποτύπους υποδοχέων** | `υποτυπική εκλεκτικότητα` |
| deprescribing | Prefer speakable **σταδιακή μείωση και διακοπή της αγωγής**; `αποσυνταγογράφηση` remains context-dependent | `αποδέσμευση`, `αποκλιμάκωση` when medication discontinuation is meant |
| bolus | **εφάπαξ ενδοφλέβια δόση (bolus)** on first use | unnecessary mixed `bolus δόση` if Greek can be clear |
| ultrabrief pulse | **υπερβραχύς παλμός / στρατηγική υπερβραχέων παλμών** | `υπερβραχέα παλμικά κύματα` if not technically intended |
| medical + anaesthetic assessment | **ιατρική και αναισθησιολογική εκτίμηση** | `παθολογική/αναισθησιολογική εκτίμηση` |
| cognitive burden | **γνωστική επιβάρυνση** | `γνωστικό φορτίο` in clinical ECT context |
| breastfeeding | **θηλασμός** | `μητρικός θηλασμός` |
| breastfeeding decision is drug-specific | **οι αποφάσεις κατά τον θηλασμό είναι ειδικές για κάθε φάρμακο** | awkward `ο θηλασμός είναι φαρμακοειδικός` |
| women/girls able to become pregnant | **γυναίκες και κορίτσια με δυνατότητα κύησης** | collapse to a simple age category if source is capability-based |
| reproductive considerations | **ζητήματα αναπαραγωγικής υγείας / αναπαραγωγικού σχεδιασμού** | narrow automatically to `οικογενειακός προγραμματισμός` |
| intercurrent illness in drug safety | **οξεία νόσος / οξεία συνυπάρχουσα νόσηση** | narrowing to infection unless source does |

## 5.8 Psychotherapy language

| English | Preferred Greek | Avoid / note |
|---|---|---|
| CBT | **γνωσιακή-συμπεριφορική θεραπεία (CBT)** | keep acronym if useful for exam recognition |
| cognitive formulation / case formulation | **γνωσιακή διατύπωση / διατύπωση περίπτωσης** according to context | — |
| collaborative empiricism | **συνεργατικός εμπειρισμός** | — |
| behavioural activation | **συμπεριφορική ενεργοποίηση** | — |
| cognitive restructuring | **γνωσιακή αναδόμηση** | — |
| behavioural experiment | **συμπεριφορικό πείραμα** | hybrid English `behavioural experiment` |
| disorder-specific CBT | **CBT ειδικά σχεδιασμένη για τη συγκεκριμένη διαταραχή** / `ειδική για τη διαταραχή γνωσιακή-συμπεριφορική θεραπεία` | untranslated `disorder-specific CBT` |
| self-focused attention | **αυτοεστιασμένη προσοχή** | hyphenated `αυτο-εστιασμένη` as inconsistent house orthography |
| maintaining cycle | **φαύλος κύκλος που συντηρείται από...** | `συντηρητικός κύκλος` |
| graded situational exposure | **σταδιακή έκθεση σε φοβούμενες καταστάσεις** | `κλιμακούμενη καταστασιακή έκθεση` |
| sleep restriction / compression (CBT-I) | **περιορισμός / συμπίεση του χρόνου στο κρεβάτι** | `περιορισμός/συμπίεση του ύπνου` |
| reconstruct history | **ανασύνθεση του ιστορικού** | `αναδόμηση του ιστορικού` when English means reconstruct, not restructure |
| enactment | **REVIEW_ONLY**: candidate `εκδραμάτιση (enactment)`; safer explanatory form `αυτόματη αναπαραγωγή της σχεσιακής δυναμικής στη θεραπευτική σχέση` | do not mass-standardise without adjudication |
| manualised therapy | **δομημένη βάσει θεραπευτικού εγχειριδίου (manualised)** on first use if needed | `εγχειριδιοποιημένη` may be recognised but is heavy |

## 5.9 Neurology, sleep and neuropsychiatry

| English | Preferred Greek | Avoid / distinction |
|---|---|---|
| post-ictal | **μετακριτικός / μετακριτική κατάσταση** | `μετακρίσιμος` |
| seizure cluster | **συρροή επιληπτικών κρίσεων** | — |
| cerebrovascular | **εγκεφαλοαγγειακός** | `αγγειακός εγκεφαλικός` |
| formication | First use: **αίσθηση / απτική ψευδαισθητική εμπειρία ότι έντομα έρπουν πάνω ή κάτω από το δέρμα (formication)** | `μυρμηγκίαση` if that reduces the phenomenon to tingling/paraesthesia |
| spontaneous parkinsonism | **αυτόματα εμφανιζόμενος / αυθόρμητος παρκινσονισμός**, with context making non-drug-induced meaning clear | `αυτόματος παρκινσονισμός` |
| sleep attack | **αιφνίδιο / ακατανίκητο επεισόδιο ύπνου** | `επίθεση ύπνου` |
| dream enactment | **εκδραμάτιση των ονείρων / συμπεριφορική εκδραμάτιση ονείρων** | `δραματοποίηση ονείρων` |
| brief muscle twitches | **βραχείες μυϊκές συσπάσεις / τινάγματα** | `σπασμοί` when seizure meaning is not intended |
| poor initiation | **μειωμένη πρωτοβουλία / δυσκολία έναρξης δραστηριοτήτων** | `πενία έναρξης πράξεων` |
| goal-directed activity | **στοχοκατευθυνόμενη δραστηριότητα** | literal multiword English syntax |
| frailty | **ευπάθεια / γηριατρική ευπάθεια** | `ευθραυστότητα` in clinical prose |
| post-anaesthetic recovery | **μεταναισθητική ανάνηψη / ανάνηψη μετά από αναισθησία** | erroneous `μετανασθητική` |

## 5.10 Evidence, research and statistics

| English | Preferred Greek | Avoid / note |
|---|---|---|
| body of evidence | **σύνολο της διαθέσιμης επιστημονικής τεκμηρίωσης** | `σώμα τεκμηρίων` / `συνολικό σώμα...` |
| high-quality evidence | **τεκμηρίωση υψηλής ποιότητας** | `δεδομένα υψηλής τεκμηρίωσης` |
| effect size | **μέγεθος επίδρασης** | — |
| implicated | **εμπλέκεται**, `συσχετίζεται` according to source | `ενοχοποιείται` when that overstates causality |
| urbanicity | **αστικότητα (urbanicity)** | `αστικοποίηση`, which is urbanisation |
| urbanisation | **αστικοποίηση** | do not confuse with urbanicity |
| pre-test probability | **REVIEW_ONLY:** candidate `πιθανότητα πριν από τη δοκιμασία (pre-test probability)`; `προδιαγνωστική πιθανότητα` requires terminology support | do not create `προ-ελεγκτική πιθανότητα` by calque |

---

# 6. Salience and symptom prominence — CLOSED family

`Προεξοχή` is not the house translation of psychiatric/neuroscientific **salience**. Use the meaning-specific form.

| English | Preferred Greek | Avoid |
|---|---|---|
| aberrant salience | **παθολογική απόδοση σημασίας** | παρεκκλίνουσα/παθολογική `προεξοχή` |
| affective / emotional salience | **συναισθηματική σημασιοδότηση** / `απόδοση συναισθηματικής σημασίας` | συναισθηματική προεξοχή |
| incentive salience | **κινητροδοτική σημασία** | προεξοχή κινήτρου / κίνητρο-επαγόμενη προεξοχή |
| salience of stimuli | **απόδοση σημασίας στα ερεθίσματα** | προεξοχή ερεθισμάτων |
| symptom prominence | **κυριαρχία**, `προεξάρχουσα παρουσία`, `προεξάρχοντα συμπτώματα` | προεξοχή συμπτωμάτων |

The adjective `προεξάρχων/προεξάρχουσα` remains legitimate Greek when it genuinely means prominent/dominant.

---

# 7. Neuroscience and neuroanatomy — settled terms

These forms were explicitly adjudicated in the neuroscience addendum or later corpus QA and should be treated as frozen unless new authoritative Greek terminology requires revision.

| English | Preferred Greek | Accepted / note | Avoid |
|---|---|---|---|
| anterior cingulate cortex (ACC) | **πρόσθιος φλοιός του προσαγωγίου** | πρόσθια μοίρα της έλικας του προσαγωγίου when referring to the gyrus | `πρόσθιο περιγεγυρωμένο` |
| ventromedial prefrontal cortex (vmPFC) | **κοιλιοέσω προμετωπιαίος φλοιός** | κοιλιοέσω προμετωπιαίο σύστημα | `κοιλιοδιάμεσο` |
| dorsolateral prefrontal cortex (DLPFC) | **ραχιοπλάγιος προμετωπιαίος φλοιός** | ραχιοπλάγιο προμετωπιαίο κύκλωμα | — |
| orbitofrontal cortex (OFC) | **κογχομετωπιαίος φλοιός** | κογχομετωπιαίο σύστημα | — |
| ventral striatum | **κοιλιακό ραβδωτό** | — | — |
| nucleus accumbens | **επικλινής πυρήνας** | — | — |
| nigrostriatal pathway | **μελανοραβδωτή οδός** | — | — |
| mesolimbic pathway | **μεσομεταιχμιακή οδός** | — | — |
| mesocortical pathway | **μεσοφλοιώδης οδός** | — | — |
| tuberoinfundibular pathway | **φυματοχοανική οδός** | connects tuber cinereum with infundibular/pituitary stalk region | `σωληνοχοανοειδής` |
| limbic | **μεταιχμιακός** | — | `μεταταιχμιακός` |
| hippocampal | **ιπποκαμπικός** / `του ιπποκάμπου` | choose natural sentence | awkward `ιπποκάμπειος` where not established |
| working memory | **μνήμη εργασίας** | `εργαζόμενη μνήμη` accepted | — |
| set-shifting | **εναλλαγή γνωστικών συνόλων** | `νοητική ευελιξία` in explanatory prose | — |
| cognitive impairment | **γνωστική έκπτωση / γνωστική δυσλειτουργία** | choose according to context | `γνωστική αναπηρία` for ordinary acquired impairment |
| intellectual disability / disorder of intellectual development | **διαταραχή διανοητικής ανάπτυξης (νοητική αναπηρία)** | classification-sensitive | Do not use `αναπηρία` for every cognitive impairment. |

---

# 8. Applied v4/v5 phrase improvements worth preserving

These are sentence-level lessons that should remain searchable even when they are not universal dictionary entries.

| Earlier / translated form | Preferred direction | Why |
|---|---|---|
| `Safety behaviours` | **συμπεριφορές ασφάλειας** | Established CBT Greek; hybrid English removed. |
| `Behavioural experiments` | **συμπεριφορικά πειράματα** | Established CBT Greek. |
| `disorder-specific CBT` | **CBT ειδικά σχεδιασμένη για τη συγκεκριμένη διαταραχή** | Naturalises English compound. |
| `maternity blues` | **μελαγχολία της λοχείας** | Removes English residue. |
| `off-label` | **εκτός εγκεκριμένης ένδειξης** | Regulatory/clinical Greek. |
| `postpartum schizophrenia` | **επιλόχεια σχιζοφρένεια** when quoting/rejecting the misconception | Avoid unnecessary English in Greek prose. |
| `standard treatment` | **καθιερωμένη θεραπεία / συνήθης θεραπευτική πρακτική** according to meaning | Avoid hybrid English. |
| `personality pattern` | **πρότυπο προσωπικότητας** | Avoid hybrid English. |
| `preconception planning` | **προσυλληπτικός σχεδιασμός** | Not `προγεννητικός` planning before conception. |
| `mother-and-baby unit` | **μονάδα μητέρας-βρέφους (MBU)** | Meaning is mother + baby, not automatically neonate. |
| `cyclical on/off pattern` | **κυκλικό πρότυπο εμφάνισης και ύφεσης των συμπτωμάτων** | Avoid mechanical on/off language. |
| `symptom-free follicular phase` | **ωοθυλακική φάση με ελάχιστα ή καθόλου συμπτώματα** | Speakable clinical Greek. |
| `maintaining cycle` | **φαύλος κύκλος που συντηρείται από...** | `συντηρητικός κύκλος` is a false friend. |
| `challenging behaviour` | **συμπεριφορά που προκαλεί σοβαρές δυσκολίες / αποτελεί πρόκληση για τη φροντίδα** | `προκλητική` may mean provocative. |
| `sleep restriction/compression` | **περιορισμός/συμπίεση του χρόνου στο κρεβάτι** | Intervention targets time in bed. |
| `relapse signature` | **ατομικό πρότυπο πρώιμων προειδοποιητικών σημείων υποτροπής** | Avoid literal `υπογραφή υποτροπής`. |
| `medical assessment` | **ιατρική εκτίμηση** | Avoid wrong-specialty `παθολογική εκτίμηση`. |
| `organ impairment` | **δυσλειτουργία οργάνων** / explicit hepatic/renal dysfunction | `οργανική ανεπάρκεια` can mean something else. |
| `recidivism-related` | **σχετιζόμενο με υποτροπή στην παραβατική/εγκληματική συμπεριφορά** | Avoid ambiguity with psychiatric relapse. |
| `explain away / invalidate identity` | use direct Greek: **να αποδοθεί αυθαίρετα σε άλλους παράγοντες ή να αμφισβητηθεί/ακυρωθεί...** | Avoid translated idiom. |
| `family history informs risk` | **το οικογενειακό ιστορικό παρέχει πληροφορίες για τον κίνδυνο** | More natural than `πληροφορεί για`. |

---

# 9. Greek oral-board prose rules by question type

## Diagnostic questions

Default spoken order:

1. clinical picture / syndrome;
2. severity or red flags where relevant;
3. diagnosis and operational criteria;
4. differential diagnosis;
5. selected discriminators / follow-ups.

Phenomenology usually precedes manual mechanics unless the examiner specifically asks for criteria.

## Emergency questions

Default clinical logic:

1. recognise the syndrome/emergency;
2. establish current severity and immediate threats;
3. identify predictors/causes that alter risk;
4. initiate core treatment and supportive care;
5. determine disposition/escalation from the assessment;
6. separate major complications when it improves retrieval.

Do not treat `severity` and `risk of complicated course` as the same construct.

## Psychopharmacology questions

Use the sequence the question actually needs. A natural answer may move through:

- what the drug is;
- useful mechanism;
- place in treatment;
- major risks/adverse effects;
- monitoring/practical pharmacokinetics.

Do not let a monitoring checklist swallow the clinical answer. Do not claim mechanistic certainty the source does not support.

## Psychotherapy questions

For CBT, the v5 calibration supports:

1. definition/model;
2. formulation;
3. collaborative therapeutic process;
4. techniques linked to the problem/mechanism;
5. selected applications;
6. between-session work and relapse prevention.

Do not present a technique catalogue detached from formulation.

## Law / ethics questions

Technical Greek is acceptable when it carries necessary precision. Naturalisation must not erase legal boundaries. Typical sequence:

1. governing principle/duty;
2. scope;
3. exceptions/legal bases;
4. practical handling/documentation.

---

# 10. Rejected or superseded forms — regression watchlist

The following forms should trigger review if they reappear in learner-facing Greek in the same meaning.

- `υψηλής απόδοσης` for educational **high-yield**
- `παράπλευρες πληροφορίες` for collateral information
- default learner-facing `ετεροαναφορικές πληροφορίες` where natural `πληροφορίες από το περιβάλλον` is better
- `γραμμή βάσης` for ordinary clinical baseline
- `θεραπευτική σύνδεση` as a generic translation of engagement
- `διακαταστασιακό` for cross-situational
- `αναδυόμενος από θεραπεία` for treatment-emergent
- `μονοπάτι` for care/treatment pathway when a natural clinical clause is available
- `φαρμακοειδικός`
- `ασθενοκεντρικός` when English is patient-specific
- `διασπορά` for medication diversion
- `συν-απόφαση` / `συν-διαμόρφωση απόφασης`
- `υπογραφή υποτροπής`
- `επιθετική υποστηρικτική φροντίδα`
- `γνωστικό φορτίο` in the ECT/clinical burden sense
- `παθολογική εκτίμηση` when English means medical assessment
- `προσυμπτωματικός έλεγχος` where screening detects current disease/syndrome
- `αυτόματος` for spontaneous occurrence
- `προληπτικός` for proactive action when no preventive meaning exists
- `επιχειρησιακό` for ordinary clinical operational/practical language
- `ενοχοποιείται` when English merely says implicated/associated
- `διακρατείται` for a belief held with conviction
- `αρχιτεκτονική` for ordinary diagnostic framework
- `αστικοποίηση` for urbanicity
- `δόση εφόδου` for loading dose
- `δυσκολοκυβέρνητη ανησυχία`
- `συντηρητικός κύκλος` for maintaining cycle
- `εξονυχιστικός έλεγχος` for social scrutiny
- `κατάλληλο τραύμα` for qualifying trauma
- `διάγνωση ένταξης` for rule-in diagnosis
- generic `μέθη` for intoxication across substances
- `πολυτοξικομανία` for polysubstance use
- `εκλυόμενη στέρηση` for precipitated withdrawal
- `διαχείριση ενδεχομένων` as unverified contingency-management translation
- `μετανασθητική ανάνηψη`
- `φυσική εξέταση` for physical examination in medical Greek
- `αυτόματος παρκινσονισμός`
- `προληπτική διασυνδετική` for proactive liaison
- `ευθραυστότητα` for frailty
- `επίθεση ύπνου`
- `δραματοποίηση ονείρων`
- `αποσυνδετικά φαινόμενα` for dissociative psychopathology
- `φύλλο οδηγιών (SmPC)`
- `κατασταλτική επιλογή` for coercive option
- `συνεργική` when source says additive
- `μητρικός θηλασμός`
- `σώμα τεκμηρίων`

This is a **semantic regression list**, not a blind search-and-replace list. A listed Greek word may be correct in another meaning.

---

# 11. REVIEW_ONLY — unresolved terminology

Do not silently convert these into preferred house terms without a separate adjudication.

| English / concept | Current safe handling | Open issue |
|---|---|---|
| contingency management | retain English term with concise explanatory Greek if needed | No sufficiently established house Greek confirmed here. |
| uncompetitive antagonist | retain English qualifier `(uncompetitive)` alongside carefully worded Greek | Must distinguish from non-competitive antagonism. |
| deprescribing as a noun | prefer descriptive `σταδιακή μείωση και διακοπή της αγωγής` in spoken prose | Whether `αποσυνταγογράφηση` becomes canonical remains open. |
| enactment | `εκδραμάτιση (enactment)` is a candidate; explanatory relational wording is safe | Psychodynamic house term not fully adjudicated. |
| pre-test probability | `πιθανότητα πριν από τη δοκιμασία (pre-test probability)` is a safe explanatory form | Whether `προδιαγνωστική πιθανότητα` is preferred needs terminology support. |
| Gender Incongruence | retain classification label carefully and verify official/accepted Greek before global standardisation | `ασυμφωνία` vs other forms not settled here. |
| ICD-11 Dissociality | retain English in parentheses if needed | Greek trait-domain label requires global adjudication. |
| ICD-11 Anankastia | retain `Anankastia` in parentheses if needed | Greek canonical label requires global adjudication. |
| autism masking/camouflaging | define descriptively on first use | Avoid alternating `κάλυψη`, `απόκρυψη`, `καμουφλάζ` without a house rule. |
| visual-release phenomenon | explanatory Greek + English term if needed | `φαινόμενο οπτικής αποδέσμευσης` may be a calque. |
| insistence on sameness | describe clinically if needed | Do not freeze `επιμονή στην ομοιομορφία` without adjudication. |
| difficult-to-treat depression | `δυσθεράπευτη κατάθλιψη` is acceptable pending global choice | Keep separate from formally defined TRD. |

---

# 12. Usage protocol for future translation/editorial work

For every consequential English phrase:

1. Identify the **clinical construct**, not merely the English word.
2. Check the stable terminology table.
3. Check the anti-calque/translation-memory tables for context-sensitive families.
4. Check whether a later founder-approved rule supersedes an older term.
5. Preserve recommendation strength, causal strength, temporality, scope, and uncertainty exactly.
6. Prefer a natural Greek clause over an invented noun/adjective when Greek terminology is unstable.
7. Keep established English acronym/term in parentheses only when it materially aids exam recognition or prevents ambiguity.
8. Read the final sentence aloud.
9. If the Greek is consequential but uncertain, verify actual Greek professional usage rather than guessing.
10. Record genuinely new durable decisions in the next guide revision rather than leaving them buried only in manuscript commits.

### Never use this guide as a factual-update mechanism

A translation edit must not silently alter:

- diagnostic criteria or counts;
- duration thresholds;
- doses or serum concentrations;
- monitoring schedules;
- treatment sequencing;
- recommendation strength;
- causal claims;
- licensing status;
- Greek law/article numbers;
- source-specific uncertainty.

If the underlying psychiatric claim needs revision, handle that in the appropriate diagnostic/treatment/regulatory/legal evidence workflow first, then translate the verified claim.

---

# 13. Historical source map

V4 was reconstructed from the following repository evidence and should be read as their forward consolidation rather than a deletion of history:

- `Translation-guide-v2.md`
- `Translation-guide-v2-writer-brief.md`
- `Translation-guide-current-research.md`
- `Translation-guide-audit.md`
- `Translation-guide-neuroscience-addendum.md`
- `Translation-guide-v3.md` — historical; encoding-corrupted in repository representation
- `Greek-manuscript-cumulative-language-QA-master.md`
- `Greek-manuscript-deep-read-A-Q001-Q020.md`
- `Greek-manuscript-deep-read-B-Q021-Q040.md`
- `Greek-manuscript-deep-read-C-Q041-Q060.md`
- `Greek-manuscript-deep-read-D-Q061-Q080.md`
- `Greek-manuscript-deep-read-E-Q081-Q100.md`
- `Greek-manuscript-revision-v3-completion.md`
- `Greek-manuscript-salience-correction-completion.md`
- applied Greek v4 editorial/prose-cleanup work
- `Greek-v5-scale-doctrine.md` and its founder-approved calibration set

Older files remain useful for provenance, rejected alternatives, and reconstruction of why a decision was made. **For forward Greek language choices, start here.**
