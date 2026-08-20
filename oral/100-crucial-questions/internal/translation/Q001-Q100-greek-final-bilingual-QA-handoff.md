# Q001–Q100 Greek Final Bilingual QA Handoff

**Product:** *The 100 Crucial Questions in Psychiatry*  
**Purpose:** independent second-pass bilingual QA handoff for final Greek PDF production  
**Date:** 2026-08-20

## Canonical production inputs checked

- English v2 corpus: `oral/100-crucial-questions/answers/revision-v2/`
- Greek translated v2 corpus: `oral/100-crucial-questions/answers/revision-v2-el/`
- Translation terminology master actually used by the translation run: `oral/100-crucial-questions/internal/translation/Translation-guide-v2.md`
- Existing translation QA report: `oral/100-crucial-questions/internal/translation/Q001-Q100-greek-translation-QA.md`
- Greek translation commit: `ab617961440309f7f32677c56122b3f525215c03`

A later-named `Translation-guide-v3.md` also exists in the repository. It predates the Greek translation commit, but the completed translation run explicitly used v2 as its canonical terminology master. In the current GitHub connector representation, v3 becomes encoding-corrupted after part of the psychopathology section, so it is **not treated as a safe production authority for this already-translated corpus** without a separate repair/adjudication pass. The final PDF should therefore continue to use the Greek `revision-v2-el` corpus rather than attempting an automatic v3 terminology substitution.

## QA conclusion

The Greek corpus is **structurally complete and production-usable**. The existing translation run reports 100/100 English files and 100/100 Greek files with one-to-one section parity. Independent second-pass review of representative high-risk material found preserved clinical meaning, numerical anchors, legal chronology and board-answer architecture.

Representative files rechecked directly against their English v2 counterparts or governing terminology included:

- Q001 — initial psychiatric assessment / MSE / formulation terminology
- Q009 — Greek involuntary admission procedure and deadlines
- Q067 — sleep stages / EEG physiology
- Q079 — antidepressant selection and pharmacological mechanisms
- Q094 — frontal-subcortical / limbic circuitry
- Q095 — dopamine pathways and D2 clinical implications

No semantic reversal, omitted section, altered dose/threshold, or mistranslated legal deadline was identified in those checks.

## Source-file changes made in this QA pass

**None.**

No file under `oral/100-crucial-questions/answers/revision-v2-el/` was changed during this second-pass QA. Therefore this QA pass by itself does **not** trigger a Greek PDF rebuild if the current renderer is already using the canonical `revision-v2-el` files.

## Important correction to the earlier translation QA report

The existing `Q001-Q100-greek-translation-QA.md` contains an inaccurate shorthand in section 4, item 12, for Q009. It states:

> `3μηνη διάρκεια, 6μηνη παράταση`

That is **not** the wording of the canonical Greek Q009 source. Q009 correctly states that involuntary hospitalisation should end once the criteria cease to apply, that the ordinary statutory maximum is **6 months**, and that there is a reporting/review safeguard after the first **3 months**, with exceptional conditions for extension.

For final editorial work, follow **Q009 itself**, not that shorthand line in the older QA report.

The earlier QA report also contains a minor conclusion typo where `revision-v2-el` is rendered without the initial `r`; this is metadata only and does not affect the translated corpus.

## Terminology / register watchlist for human final edit

These are **non-blocking editorial watch items**, not authorised automatic replacements:

1. **Q094/Q095 — `salience`** is rendered with forms based on `προεξοχή` (for example `συναισθηματική προεξοχή`, `προεξοχή κινήτρου`). The meaning is preserved, but this is an English-derived technical rendering that may sound less natural than alternative Greek psychiatric/neuroscience phrasing. Do not change it casually because no replacement has been formally adjudicated in the v2 terminology guide; simply flag it for human stylistic review.
2. **English technical parentheticals** such as `sleep spindles`, `K-complexes`, `frontostriatal`, `incentive salience`, receptor/transporter abbreviations and named psychotherapies are intentionally retained where they improve board recognition. The final editor should not strip them globally.
3. **`formulation`** is intentionally retained in parentheses after `διατύπωση περίπτωσης` in selected places; this is useful for exam recognition and should not be removed mechanically.
4. Preserve the established distinctions from the terminology master: `πίεση λόγου` ≠ `λογόρροια`; `ανακοπή σκέψης`; `χαλάρωση συνειρμών` ≠ `εκτροχιασμός`; `υπερλεπτομερειακή σκέψη` ≠ `εφαπτομενικότητα`; `εναισθησία` ≠ `κρίση` ≠ decision-specific capacity; `ψευδαίσθηση` ≠ `παραίσθηση`.
5. Do not replace `ηχολαλία`, `ηχοπραξία`, `πενία λόγου`, `εμπροσθόδρομη αμνησία`, or `οπισθόδρομη αμνησία` with alternative spellings during layout cleanup.

## Final-editor PDF handoff

If Greek PDF manufacture has already started, use the following as the fast-path rule:

### No rebuild required from this QA pass

Because no Greek source question file was modified here, a PDF generated from the current `revision-v2-el` corpus remains aligned with the content reviewed in this pass.

### If the editor performs a later textual change

Rebuild only after checking `git diff` for changes under:

`oral/100-crucial-questions/answers/revision-v2-el/`

A change to this QA handoff or to internal translation documentation alone does not require re-rendering the book.

### Production source of truth

For the current Greek book:

`oral/100-crucial-questions/answers/revision-v2-el/Q001.md` through `Q100.md`

Do not build the PDF from the old English corpus, old `final/` corpus, translation research packets, or the terminology-guide files themselves.

## Final status

**BILINGUAL_QA_PASS — PRODUCTION_USABLE**

- Greek source files changed in this pass: **0**
- Confirmed rebuild-triggering changes: **0**
- Critical translation blockers found: **0**
- Metadata/documentation correction identified: **1** (Q009 shorthand in prior QA report)
- Non-blocking human linguistic watch items: **5**

The next meaningful gate is visual/layout QA of the generated Greek PDF, with special attention to Greek line wrapping, table overflow, mixed Greek/English abbreviations, legal numerals, units, and preservation of bold emphasis.