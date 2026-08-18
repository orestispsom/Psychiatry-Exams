# The 100 Crucial Questions in Psychiatry — Publication Production System

Status: LOCKED AFTER Q11 PILOT

Purpose: preserve a single coherent visual/publication system across all 100 question entries while allowing controlled content-driven variations.

## Authority split

- `answers/final/` is the learner-facing psychiatric content authority.
- The approved Q11 publication prototype is the visual/layout reference authority for the book system.
- Publication work must not silently change psychiatric meaning. Any content change discovered during layout must return to the editorial/content workflow for approval.

## Core production rule

Do **not** independently redesign each question.

Every subsequent question must be composed inside the Q11-derived publication system. New visual treatments are allowed only when the content genuinely requires a new component (for example a table, algorithm, figure, graph, dense board-fact block or exam/current distinction).

A later global pass is for consistency cleanup and polish, not for redesigning the book from scratch.

## Page architecture

1. Each main question begins on a new page.
2. A question entry may occupy one or more pages.
3. The next main question must never begin on the previous question’s final page.
4. Typography must not be compressed merely to force an entry onto one page.
5. The model oral answer is the central reading element.
6. Recall spine, board facts, examiner follow-ups, traps and exam/current distinctions use restrained, repeatable hierarchy.
7. Avoid worksheet, dashboard, slide-deck or card-stack aesthetics.
8. A4 is the primary production size for the first edition. Other paper sizes are derivative outputs, not separate design systems.

## Component policy

Standard components:
- Question heading
- Recall spine
- Model oral answer
- Must-know board facts, when present
- Examiner follow-ups, when present
- Common/examiner traps, when present
- Exam answer vs current practice, when present

Optional components may be introduced only when they materially improve learning or retrieval:
- Tables
- Algorithms / flowcharts
- Diagrams
- Graphs
- Comparison matrices

Optional components must inherit the same typography, spacing, rule weights, visual restraint and publication character as the Q11 system. They must not become isolated mini-designs.

## Visual consistency rule

The exact visual tokens — fonts, sizes, margins, leading, spacing, rule weights, colour values, header/footer treatment and other measurements — should be transcribed from the approved Q11 prototype into a dedicated design-spec file before large-scale production. Until that transcription exists, no later question should invent a competing visual system.

## Scaling workflow

1. Q11 serves as the approved prototype.
2. Compose the next representative batch inside the same system.
3. Introduce new component types only when first required by actual content.
4. Review the first multi-question batch together for visual consistency.
5. Freeze any newly validated component patterns into the design specification.
6. Continue production in batches.
7. Perform periodic consistency audits.
8. At full-manuscript stage, perform one global polish/QA pass without reopening approved content or redesigning the visual language.

## Review gates

### Per-question production check
- starts on a new page;
- approved final text used;
- no silent psychiatric rewriting;
- hierarchy matches Q11 system;
- no unnecessary visual component introduced;
- overflow/page breaks are deliberate;
- answer remains comfortable to read aloud and scan for retrieval.

### Batch consistency check
After each practical batch, inspect pages side-by-side for:
- title hierarchy;
- recall-spine treatment;
- body measure/leading;
- vertical rhythm;
- follow-up treatment;
- board-fact treatment;
- traps treatment;
- page-number/header/footer consistency;
- excessive density or empty space;
- inconsistent use of boxes, rules, tables or colour.

### Print checks
Printing is a validation tool, not a mandatory step for every question.

Print representative pages when a new layout condition appears, especially:
- simple one-page entry;
- multi-page entry;
- dense pharmacology entry;
- entry with follow-up;
- entry with table/algorithm/figure;
- entry with exam/current distinction.

Check actual print readability, contrast, line length, type size, whitespace, page turns and visual weight.

## Change control

A departure from the Q11 system is justified only if:
- the existing system cannot express the content clearly;
- the new treatment improves retrieval or understanding;
- it can become a reusable component rather than a one-off decoration.

If approved, document the new component in the publication design specification and reuse it consistently thereafter.

## Anti-patterns

Do not:
- design 100 visually independent question pages;
- postpone all consistency work until the end;
- shrink text to preserve arbitrary page counts;
- add decorative tables/graphs that duplicate prose;
- allow one question to look visually special without a content reason;
- perform a final-stage wholesale redesign unless the pilot system has demonstrably failed.

## Current next step

Capture the exact visual measurements/tokens from the approved Q11 PDF into a dedicated `DESIGN_SPEC.md`, then use Q12–Q19 as the first real multi-question consistency test.