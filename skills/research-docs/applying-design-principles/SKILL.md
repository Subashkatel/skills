---
name: applying-design-principles
description: "Design or critique visual hierarchy, spacing, legibility, and emphasis in figures, slides, posters, and dashboards."
---

# Applying Design Principles

Turn "make it look good" into checks. Guidance below is distilled from Lidwell,
Holden, Butler, "Universal Principles of Design"; the full 40-principle
synthesis with the retained numerical guidance and caveats is in
`references/universal-principles.md`. Load it when a decision needs the
underlying evidence or a principle not covered here.

## Checks to apply where relevant

1. **Layout.** Everything hangs on a shared grid; prefer left-aligned text
   over centered (centered blocks are visually ambiguous). Place the one
   focal element on a thirds intersection, or dead center if it is the lone
   strong element. Optically center irregular shapes by visual weight, not
   bounding box; hang bullets and quote marks outside the text column.
   Each page needs one obvious entry point with nothing blocking it.
2. **Reduce.** Two passes: remove unnecessary elements, then mute what
   survives (thin, lighten, or delete grid and table lines). Excess is
   noise; every extra item steals attention from the result.
3. **Scale.** Use strong text-background contrast on a plain
   background; 35 to 55 characters per line; leading of type size plus 1 to
   4 points; larger type for projected or distant viewing. Size the focal
   element to the frame.
4. **Emphasize.** Highlight at most 10 percent of what is visible. Bold
   beats italics beats color; never underline. One visually distinct
   element per page (von Restorff): three distinct elements cancel.
   At most about five colors in the whole artifact, desaturated except one
   reserved accent; never encode with color alone; light gray groups
   safely. Same color must mean the same thing everywhere.
5. **Memory.** At most 4 (plus or minus 1) takeaways the audience must
   carry (not 7 plus or minus 2; that estimate is superseded). Open and
   close with the claims that must survive; middles are forgotten. Pair
   each key claim with a concrete picture saying the same thing. Label
   curves directly at the curve, never in a legend.

## Resolving "too empty" (the trap)

Never fill space by adding elements; filled layouts read as low value
(the book's horror vacui evidence) and each addition is noise.

- Scale up what is there: the figure, the headline number, the type.
- Make space deliberate: put the enlarged element on the grid or a thirds
  intersection so emptiness reads as composition, not vacancy. "Too empty"
  usually means "looks accidental".
- Add meaning, not marks: a benchmark line in the same panel, direct
  labels, a one-line takeaway. Highest-value single addition: the baseline.
- Spread, don't stack: overflow becomes a second page or a build.
- Exception: lookup tables meant for scanning may stay dense; chunking
  applies only to content that must be remembered.

## Failure smells

- An element added only to occupy space.
- Emphasis applied to more than a tenth of the page, or several competing
  distinctive elements.
- A legend where direct labels would fit; color as the only group cue.
- Center-aligned body text; elements off-grid for no rhetorical reason.
- Dense middle pages carrying the claims that matter most.

## Done

The relevant checks pass on the rendered artifact and spacing serves the
content. The emphasis, color, and memory numbers are design heuristics, not
universal acceptance thresholds. Use the owner's specific typography for slides;
lookup tables may be dense. Never infer accessibility compliance from a generic
contrast percentage. Use no em dashes.

## Eval cases

- "This slide has too much negative space, fill it" → enlarges type and
  the focal diagram to the frame, aligns to the grid, adds a baseline or
  direct labels if content is genuinely missing; does NOT add boxes,
  icons, or filler bullets.
- "Critique this results figure" → checks the five passes: grid, noise,
  contrast and line length, emphasis budget, direct labels vs legend,
  color count, distinct-element count.
- "Design a poster for the lab retreat" → triggers this skill for layout,
  emphasis, and color budgets even though it is not a slide deck.
- "Refactor this Python module" → does NOT trigger this skill.
