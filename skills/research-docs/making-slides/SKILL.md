---
name: making-slides
description: "Create or revise research slides and pptx decks using the owner's typography and one-idea layout. Excludes standalone plots."
---

# Making Slides

Produce decks that look like research-talk slides (Dally Hot Chips / BAICS
style), not consulting decks, and that hold up typographically.

## Before drawing anything

1. Use supplied examples when available. The original example decks and
   typography books are not on disk in the indexed collection; their distilled
   preferences survive in `references/typography.md` and the rules below.
2. Use traceable existing runs, supplied data, or cited source numbers. Run a
   new experiment only when the requested content needs it and resources are
   authorized. A font or layout fix does not require rerunning the science.
   Label a hypothetical example explicitly and never present it as measurement.
3. Use the owner palette (blue `#2a78d6`, aqua `#1baf7a`, yellow `#eda100`
   on white) consistently. A chart skill is optional when chart design needs it.
4. For a difficult layout decision, use `applying-design-principles` or its
   reference. Do not load a second skill solely because the output is visual.

## Layout rules (one idea per slide)

- Plain white background. One centered title set in LETTERSPACED CAPITALS
  at text weight (never bold; weight decreases as size increases). ONE
  focal element per slide (a diagram, a timeline, a breakdown).
- **Fill the frame by scale, not by count** (owner preference):
  size the focal element and the type so the slide is occupied; undersized
  content floating in empty space reads as accidental. Whitespace stays,
  but as deliberate composition around large content. Never add boxes,
  icons, or filler bullets to occupy space.
- One serif family throughout: name "Palatino Linotype" in the pptx
  (check availability; URW P052 is a possible Linux substitute). The typography must be
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

## Owner typography rules

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
- Prefer rendering the actual pptx for acceptance. A matplotlib mirror from
  one layout spec can provide fast draft previews, but cannot prove Office
  font substitution, line wrapping, or animation playback. Working pattern:
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

1. Render and inspect every changed slide and a whole-deck overview. Inspect
   every slide for a new deck or a change to shared layout or typography.
2. Hunt for: text overlapping boxes/lines, labels crossing markers,
   off-center bar labels, text overflowing its box or the page edge, sizes
   off the scale, em dashes, undersized content adrift in empty space.
3. Fix visual defects and re-render affected slides. Confirm the pptx opens
   and text remains editable. If only mirror previews are available, report
   that viewer-specific layout and playback remain unverified.

## Eval cases

- "Make 3 slides explaining the decoder pipeline with an example" → uses
  traceable results or runs a needed authorized experiment, builds editable
  pptx, and checks rendered slides.
- "The fonts on these slides are illegible, redo them" → switches raster
  text to native pptx text, applies the modular scale one step up,
  re-verifies renders.
- "There is a lot of negative space on these slides" → scales up type and
  the focal element per `applying-design-principles`; does not add filler.
- "Plot the benchmark results" (no slides requested) → does NOT trigger
  this skill; use dataviz alone.
