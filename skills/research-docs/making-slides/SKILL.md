---
name: making-slides
description: Build presentation slides (pptx decks, talk figures) in the owner's preferred style; minimal one-idea-per-slide layout with Bringhurst/Proportional Web typography, native vector pptx text, and numbers taken from real runs. Use whenever asked to create, redo, or fix slides, a deck, a presentation, or talk figures. Not for papers, posters, or web dashboards.
---

# Making Slides

Produce decks that look like research-talk slides (Dally Hot Chips / BAICS
style), not consulting decks, and that hold up typographically.

## Before drawing anything

1. If example decks or style PDFs exist in the workspace (filenames like
   "slide example ..."), read them first and match them.
2. Get the numbers from a real run of the system being presented: run the
   simulator/experiment, capture the trace, and use only values you
   observed. Never invent illustrative numbers.
3. If a `dataviz` skill is available, load it before any chart/timeline
   slide; either way use the validated palette (blue `#2a78d6`, aqua
   `#1baf7a`, yellow `#eda100` on white) in fixed slot order.
4. For layout, emphasis, and white-space decisions, load
   `applying-design-principles` (the Universal Principles of Design
   synthesis); it governs when space is composition and when it is vacancy.

## Layout rules (one idea per slide)

- Plain white background. One centered title set in LETTERSPACED CAPITALS
  at text weight (never bold; weight decreases as size increases). ONE
  focal element per slide (a diagram, a timeline, a breakdown).
- **Fill the frame by scale, not by count** (owner feedback 2026-07-12):
  size the focal element and the type so the slide is occupied; undersized
  content floating in empty space reads as accidental. Whitespace stays,
  but as deliberate composition around large content. Never add boxes,
  icons, or filler bullets to occupy space.
- One serif family throughout: name "Palatino Linotype" in the pptx
  (Office has it; Linux substitutes URW P052). The typography must be
  VISIBLE; a generic sans deck that merely follows the rules numerically
  reads as "plain" and gets rejected.
- Italic serif for commentary, captions, and takeaway lines; bold reserved
  for direct labels and headline numbers.
- No kickers, footers, logos, stat-tile grids, or legend chrome. A small
  muted provenance line (the exact reproduction command) is allowed. A
  neutral paper-tint panel (`#f1f0ec`) may group text content; it is not a
  data color.
- Annotate numbers directly on the diagram (Dally's "$10M-50M GPU Time"
  pattern): latencies under arrows, timestamps beside events, direct
  labels on bars.
- Component boxes: flat solid fills, short names, one-line sublabels.
  Colored marks carry identity; text stays in ink (`#0b0b0b` / gray
  `#52514e`). Never color a text label when a colored mark already
  identifies it.

## Typography rules (non-negotiable)

- Compose on a modular scale; never use off-scale sizes. Root scale (13.33
  by 7.5 in pages): 10.5, 12, 13.5, 15, 18, 24, 30, 36 pt. For projected
  decks the owner prefers one step up: 12.5, 14, 16, 18, 21.5, 27 pt
  (owner feedback 2026-07-12, after Lidwell's Legibility: larger type for
  low-resolution/distant viewing).
- Leading 1.2; add vertical space in measured intervals; don't cram (never
  line-spacing ≈ 1.0).
- One hierarchy parameter changes at a time (size OR weight, not
  size+weight+color).
- **No em dashes anywhere** (owner rule): not in slide text, captions,
  notes, code comments, or filenames. Use a comma, colon, period, or
  middot (·) instead. En dash between digits for ranges (8.750–14.750) is
  still correct; × for dimensions; letterspace any all-caps strings 5-10%.
- Full distilled rules with citations: read `references/typography.md`.

## Build pipeline

- Write native pptx text and shapes with python-pptx (vector text: crisp
  and editable; never raster text through PIL/matplotlib into the deck).
- Mirror the same layout calls to matplotlib to render preview PNGs, from
  one layout spec, so previews match the deck. Working pattern:
  `references/build-pattern.md`; a runnable self-contained example ships
  with this skill at `scripts/example_builder.py`
  (`python example_builder.py out.pptx preview_dir`; deps:
  `pip install python-pptx matplotlib`).
- Keep a monotonic z-order in the matplotlib mirror so paint order matches
  pptx.
- Animated GIFs (e.g. an engine/algorithm explainer) may embed via
  `shapes.add_picture`; they play in slideshow mode. Mirror one hold frame
  into the preview.

## Visual QA (required before declaring done)

1. Render preview PNGs and actually read every slide image.
2. Hunt for: text overlapping boxes/lines, labels crossing markers,
   off-center bar labels, text overflowing its box or the page edge, sizes
   off the scale, em dashes, undersized content adrift in empty space.
3. Fix and re-render until a pass is clean. A deck is done only when every
   preview has been viewed clean and the pptx opens with the expected
   slide/shape counts.

## Eval cases

- "Make 3 slides explaining the decoder pipeline with an example" → runs
  the simulator for real numbers, builds pptx via the dual-backend
  pattern, QAs previews.
- "The fonts on these slides are illegible, redo them" → switches raster
  text to native pptx text, applies the modular scale one step up,
  re-verifies renders.
- "There is a lot of negative space on these slides" → scales up type and
  the focal element per `applying-design-principles`; does not add filler.
- "Plot the benchmark results" (no slides requested) → does NOT trigger
  this skill; use dataviz alone.
