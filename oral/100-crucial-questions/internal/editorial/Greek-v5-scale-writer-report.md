# Greek v5 Scale Writer Report

## Status

**PASS — Greek-first v5 scale manufacture and Writer QA complete.**

- Branch: `greek-v5-scale`
- Starting commit: `f11c08844fdfa3d0281238a70d9f680598761fc1`
- Pre-report QA head: `0ad8adf6c3691eabcf4784f260d6deaf89b3a805`
- Output directory: `oral/100-crucial-questions/answers/revision-v5-el/`
- Corpus completion: **100/100 questions (Q001–Q100)**
- PDF generation: **not performed**
- Promotion to `final-v5-el`: **not performed**

This report records Writer manufacture and self-QA only. It does not imply that all 100 questions have received founder line-level approval.

## Locked pilot identity

The eight founder-approved calibration questions were copied into the full v5 corpus without modification and were rechecked at final QA by Git blob SHA.

| Question | Locked/full-v5 blob SHA | Result |
|---|---|---|
| Q001 | `de5f0271b36125cc6f7026e61693ad2d493cd791` | identical |
| Q012 | `472fcbd382557e8dd578a35fa9dcb8c1c7744081` | identical |
| Q019 | `311ebabf804f208300a9ff19a55801735a1ece05` | identical |
| Q020 | `ff751312a5326bde0c86396fc0757dd452e255dd` | identical |
| Q038 | `da24bbda2be927cbcf47f86f87f4ea9a902d445b` | identical |
| Q045 | `a6fdc43455af20533be639b70370ebac4422b50f` | identical |
| Q090 | `af80f78f01d39cb92e17fee864de2a80a8787d70` | identical |
| Q098 | `64bfa6af58011d145dfdd8ad26efa88799378d6a` | identical |

## Manufacture batches

| Batch | Manufacture targets | Source brief | Manufacture commit |
|---|---|---|---|
| V5-A | Q002–Q010, with Q001 locked | `Q001-Q010-batch.md` | `532dbf41b22b5d4570435cbc64970b99ecb7a4ac` |
| V5-B | Q011–Q019, with Q012/Q019 locked | `Q011-Q019-batch.md` | `c92d484522ab9f9c926b4ebf1ef5d33ffa50c53e` |
| V5-C | Q021–Q027, with Q020 locked | `Q020-Q027-batch.md` | `43163d603abcbfd9fe35bbf487bd09f2e9eef67e` |
| V5-D | Q028–Q036 | `Q028-Q036-batch.md` | `8b53169431feb3d04cb65cf715d53d0afc5ae74e` |
| V5-E | Q037–Q044, with Q038 locked | `Q037-Q044-batch.md` | `e3db9f5b7812de9aeee7e4a16dbc5e3c8804f469` |
| V5-F | Q045–Q051, with Q045 locked | `Q045-Q051-batch.md` | `79821c80f31a660783946c89ba155fa294660844` |
| V5-G | Q052–Q058 | `Q052-Q058-batch.md` | `b22b2cc7fdea669a2e8355a048377c4039637278` |
| V5-H | Q059–Q066 | `Q059-Q066-batch.md` | `3cff24f48150074b99f32ec1d6f592e5439c2e7c` |
| V5-I | Q067–Q073 | `Q067-Q073-batch.md` | `fb8c926bdf0b1d5989f4f29d7a06a78afcc114a4` |
| V5-J | Q074–Q081 | `Q074-Q081-batch.md` | `ec23e833eabf525308953a2cc2fd5a1b575db958` |
| V5-K | Q082–Q089 | `Q082-Q089-batch.md` | `89b9046b985ea977573df5f4ee9e2f2c75c2d917` |
| V5-L | Q091–Q100, with Q090/Q098 locked | `Q090-Q100-batch.md` | `e61c8b832615853fcce46c366853c8a6159d7b1f` |

Greek-first drafting was performed from the approved source briefs. The corresponding v4 answer was opened only after the new draft existed and was used as an omission backstop rather than as a prose template.

## Corpus-level QA

### Mechanical integrity

- Confirmed exactly **100 answer files**, Q001 through Q100, in `revision-v5-el/`.
- No missing question number and no duplicate question path were found.
- All eight locked pilot questions remain byte-identical to the founder-approved calibration files.

### Required oral/read-aloud sampling

One representative answer from each manufacture batch was read literally as viva speech:

- V5-A: Q007
- V5-B: Q018
- V5-C: Q024
- V5-D: Q034
- V5-E: Q040
- V5-F: Q050
- V5-G: Q053
- V5-H: Q063
- V5-I: Q069
- V5-J: Q081
- V5-K: Q089
- V5-L: Q099

The eight locked calibration answers were also preserved as the founder-approved reference standard and revalidated by SHA at final QA.

### Systematic defect found and corrected

The first corpus-level read-aloud pass identified a systematic register defect in a subset of newly manufactured answers: valid clinical caveats were sometimes expressed as production narration, for example language about what the candidate should "present", "memorize", or include "in the oral answer".

Per the v5 doctrine, this triggered a branch-wide inspection rather than correction of sampled files only. Affected non-locked answers were revised so that the same factual caveats are now expressed as direct clinical statements. The cleanup also removed subtler source-process/exam-production wording such as `board fact`, references to an `approved material` layer, and answer-construction commentary when these appeared inside the spoken model answer.

A fresh branch-wide hard-language sweep after correction found no occurrences of the calibrated failure constructions in spoken-core prose, including:

- `Η πρώτη απόφαση είναι`
- `Το επόμενο βήμα είναι`
- `Η προσέγγιση οργανώνεται`
- `Στην εξέταση θέλω να δείξω`
- `Για τις εξετάσεις πρέπει`
- `Η πρακτική απάντηση είναι`
- `στην προφορική απάντηση`
- `Για προφορική εξέταση`
- `Δεν απομνημονεύω`
- `Δεν επινοώ`
- `εγκεκριμένο υλικό`
- `board fact`

Remaining explicit references to examination framing are confined to learner-facing sections such as `Βασικά σημεία για τις εξετάσεις`, `Πιθανή ερώτηση εξεταστή`, or `Απάντηση εξετάσεων έναντι τρέχουσας πρακτικής`, where they are intentional.

Corrected representative samples were re-read after the systematic cleanup (including Q007, Q018, Q034, Q040, Q053, Q069 and Q089) and passed the natural-spoken-Greek / clinical-causality test. Representatives not touched by the cleanup remained unchanged after their original pass.

### Terminology/style checks

- No learner-facing use of `ετεροαναφορικές πληροφορίες`; appropriate formulations use `πληροφορίες από το περιβάλλον` and name family/carers/staff/records where relevant.
- No recurrence of the alcohol-withdrawal wording defect `αυτόνομη υπερδραστηριότητα`; the clinical wording uses activation/overactivity of the autonomic nervous system in natural Greek.
- Question titles were checked during manufacture so answer rewriting did not silently redefine the examiner's question.
- Internal outline architecture was not treated as mandatory spoken paragraph narration.

## SOURCE_QUERY

Count: **2**

1. **Q089 — ECT and Greek law:** verify the specific contemporary Greek authorization procedure, if any, when a patient lacks capacity for ECT or when emergency non-consensual ECT is considered. The current approved source layer does not establish a specific court/prosecutor/judicial-guardian/independent-second-opinion mechanism. The learner-facing answer explicitly preserves this uncertainty and does not import the UK Mental Health Act.
2. **Q027 — zuranolone in Greece:** confirm current commercial availability and reimbursement status in Greece after European authorization in September 2025. The learner-facing answer states the EU authorization and 14-day oral course but explicitly says Greek commercial availability/reimbursement are not confirmed.

Neither unresolved query was filled by inference or invention.

## Final Writer result

- Greek-first v5 scale corpus: **100/100 complete**
- V5-A through V5-L: **complete and committed**
- Locked founder-approved questions: **8/8 byte-identical**
- Mechanical corpus QA: **PASS**
- Required read-aloud sampling: **PASS after systematic cleanup**
- Final hard-language sweep: **PASS**
- Unresolved consequential/source-sensitive ambiguities: **recorded above as SOURCE_QUERY rather than guessed**
- PDF generation/promotion: **not performed**

`GREEK_V5_SCALE_WRITER_COMPLETE`
