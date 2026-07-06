---
name: reviewing-rendered-output
description: "Reviews rendered scientific visuals, plots, circuit diagrams, QEC lattices, GPU images, and screenshots with visual evidence instead of vibes."
---

# Reviewing Rendered Output

Visual evidence is telemetry, not verdict. Decide what the artifact should show, then use crops, diffs, and neutral review to find where the output diverges.

## Workflow

1. **Define the target.** State what the image, plot, circuit diagram, simulation frame, or report should communicate. If the target is ambiguous or taste-driven, ask the user with the artifact in front of them.
2. **Confirm comparability.** Same viewport, seed, tick, camera, input data, fonts, device scale, render mode, and frozen time where applicable.
3. **Capture truthfully.** Use the current candidate artifact, not a stale baseline or report. Preserve full-frame context.
4. **Create crops.** Make tight crops or zoomed regions for small labels, symbols, overlaps, boundaries, depth/order issues, artifacts, plotted features, or QEC circuit details.
5. **Generate telemetry when useful.** Use side-by-side images, grayscale diffs, edge maps, luminance summaries, bounding boxes, content counts, or layout measurements to locate movement.
6. **Judge against the target.** The baseline can be wrong. Accept the candidate only if divergences move toward the stated requirement.
7. **Use a neutral second opinion for disputed or high-stakes visuals.** Give a peer only the images, crops, and neutral task; do not prime it with the expected defect.
8. **Record findings.** Put accepted visual evidence, rejected issues, and remaining limitations in the spec, report, or verification record.

## Scientific visual cases

- GPU renderer: inspect actual PNGs after shader, pass-order, depth, blend, camera, resource layout, or capability changes.
- Plots and reports: verify axes, units, legends, confidence bands, outliers, and whether the figure supports the claim.
- Quantum circuits: verify ordering, labels, measurement placement, timing annotations, and mapping to backend constraints.
- QEC artifacts: verify syndrome timelines, detector coordinates, logical observables, lattice boundaries, and decoder-path overlays.

## Rules

- Do not accept on a lower pixel distance alone or reject on a higher one alone.
- Metrics explain where images differ; requirements decide which image is better.
- A full screenshot can hide small defects. Crops are mandatory for small or subtle features.
- A passing neutral critique does not replace direct inspection or formal tests.
- If the visual is generated from stochastic or time-varying state, freeze seed/time or state why it cannot be frozen.

## Done

Rendered output is accepted when the target is explicit, comparability is controlled, key regions were inspected, evidence is recorded, and any remaining ambiguity is surfaced to the user rather than hidden behind metrics.
