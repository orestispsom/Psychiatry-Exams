# Translation guides — which one is authoritative

Read this before using any file in this directory.

| File | State | Role |
|---|---|---|
| `Translation-guide-v4.md` | intact, 57,942 B | **Current house language authority.** Start here. |
| `Translation-guide-v2.md` | intact, 21,725 B | Underlying terminology index — 265 rows, 21 sections. Still valid except where v4 supersedes it. |
| `Translation-guide-v3.md` | **corrupt** | Historical only. Do not use. |

`Greek-v5-scale-doctrine.md` in `../editorial/` carries the founder-approved v5 scale doctrine that v4 draws on.

## `Translation-guide-v3.md` is corrupt

15,009 bytes, valid UTF-8 for only the first 7,501; the remainder is binary garbage, with the break falling mid-row inside the "Σαλάτα λέξεων / Word salad" entry.

It was committed already corrupt in `75df5d9` on 2026-08-20. No intact revision exists in this repository's history, and `Translation-guide-v3.docx` is likewise unrecoverable — it has no zip end-of-central-directory record. `Psych` holds a byte-identical damaged copy at `docs/Psychiatry-Translation-Guide-v3.md`.

**Nothing was lost.** v3 was a reformatting of v2, which is intact here, and v4 supersedes both. v4 §13 already records v3 as "historical; encoding-corrupted in repository representation".

The file is retained as provenance. It should not be used, and its apparent completeness is misleading — a repository audit in September 2026 read the corrupt file, did not check its siblings, and wrongly concluded that half the bilingual terminology had been destroyed.

Whether to mark the file in place or remove it is still open.

## Using the guides

v4 is a **language authority, not a clinical-content authority**. It governs how an already verified English or semantic claim is rendered in Greek. It must never be used to change diagnostic criteria, duration thresholds, doses, monitoring schedules, treatment sequencing, recommendation strength, causal claims, licensing status, Greek law or article numbers, or source-specific uncertainty.

- §1 — supersession hierarchy for language decisions
- §3 — frozen core psychopathology terminology
- §4 — founder-locked natural clinical Greek
- §10 — regression watchlist: forms that must not reappear
- §11 — REVIEW_ONLY queue: terms that must not be promoted without adjudication

## Related

`mental-health-core` mirrors 56 of these terms — only those its own concepts name — copied verbatim with v4 attributed. It is a mirror, not an authority: https://github.com/orestispsom/mental-health-core/blob/main/terminology/en-el.yaml
