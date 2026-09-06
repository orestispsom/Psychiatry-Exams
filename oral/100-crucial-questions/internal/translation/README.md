# Translation guides — which one is authoritative

Read this before using any file in this directory.

## Current layering

| File | State | Where | Role |
|---|---|---|---|
| `Translation-guide-v4.md` | intact, 57,942 B | **branch `greek-v5-scale`** | **Current house language authority.** Start here. |
| `Translation-guide-v2.md` | intact, 21,725 B | `main` | Underlying terminology index — 265 rows, 21 sections. Still valid except where v4 supersedes it. |
| `Translation-guide-v3.md` | **corrupt** | `main` | Historical only. Do not use. |

`Greek-v5-scale-doctrine.md` (in `../editorial/`, also on `greek-v5-scale`) carries the founder-approved v5 scale doctrine that v4 draws on.

## v4 is not on `main`

The current authority lives on the unmerged branch `greek-v5-scale`, which is 228 commits ahead of `main`. This file exists so that anyone working from `main` can find out that v4 exists rather than defaulting to v2 or, worse, to the corrupt v3.

To read it without checking out the branch:

```bash
git show origin/greek-v5-scale:oral/100-crucial-questions/internal/translation/Translation-guide-v4.md
```

Whether v4 should be merged or copied onto `main` is an open decision. This pointer is deliberately the smallest possible fix: it avoids a second copy of an authority that is still evolving on its branch.

## `Translation-guide-v3.md` is corrupt

15,009 bytes, valid UTF-8 for only the first 7,501; the remainder is binary garbage, with the break falling mid-row inside the "Σαλάτα λέξεων / Word salad" entry.

It was committed already corrupt in `75df5d9` on 2026-08-20. No intact revision exists in this repository's history, and `Translation-guide-v3.docx` is likewise unrecoverable — it has no zip end-of-central-directory record. `Psych` holds a byte-identical damaged copy at `docs/Psychiatry-Translation-Guide-v3.md`.

**Nothing was lost.** v3 was a reformatting of v2, which is intact here, and v4 supersedes both. v4 §13 already records v3 as "historical; encoding-corrupted in repository representation".

The file is retained as provenance. It should not be used, and its apparent completeness is misleading — a repository audit in September 2026 read the corrupt file, did not check its siblings, and wrongly concluded that half the bilingual terminology had been destroyed.

## Using the guides

v4 is a **language authority, not a clinical-content authority**. It governs how an already verified English or semantic claim is rendered in Greek. It must never be used to change diagnostic criteria, duration thresholds, doses, monitoring schedules, treatment sequencing, recommendation strength, causal claims, licensing status, Greek law or article numbers, or source-specific uncertainty.

v4 §1 sets out the supersession hierarchy for language decisions; §10 is the regression watchlist of forms that must not reappear; §11 is the REVIEW_ONLY queue of terms that must not be promoted to house forms without adjudication.

## Related

`mental-health-core` mirrors 56 of these terms — only those its own concepts name — copied verbatim with v4 attributed. It is a mirror, not an authority: https://github.com/orestispsom/mental-health-core/blob/main/terminology/en-el.yaml
