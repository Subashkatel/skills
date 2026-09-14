---
name: mapping-unknowns
description: "Identify unresolved assumptions that could change a complex design, experiment, or implementation."
---

# Mapping Unknowns

## Use this skill when

Use this skill when unresolved assumptions could change the solution or validity of results. Resolve what the prompt and available evidence already answer before asking. It is especially relevant for codebase refactors, GPU kernels, quantum architecture, and QEC.

## Workflow

1. Restate the user's goal and current starting point.
2. Identify material uncertainty, using these categories only when useful:
   - Known knowns: explicit facts from the prompt, files, papers, or tool output.
   - Known unknowns: questions the user already knows are open.
   - Hidden knowns: assumptions the user may know but did not say, such as hardware, precision, expected scale, or preferred library.
   - Unknown unknowns: blindspots likely to matter in this domain.
3. Identify the highest-impact unknowns where the answer would change architecture, algorithm, kernel strategy, QEC assumptions, or validation plan.
4. Choose a next mode:
   - Ask one or two high-impact questions.
   - Inspect code or references.
   - Create a small technical prototype or experiment.
   - Draft a plan with explicit assumptions.
5. State a conservative default only when it is safe to proceed without the answer.

## Domain cues

For GPU work, look for unknowns about hardware, memory layout, precision, problem size, benchmark protocol, profiler output, and portability.

For quantum/QEC work, look for unknowns about code family, distance, boundaries, stabilizers/gauge checks, noise model, decoder, syndrome schedule, logical observables, and target logical error rate.

For architecture work, look for unknowns about quality attributes, constraints, runtime paths, ownership, deployment, failure modes, and costly-to-change decisions.

## Output shape

Use `templates/unknowns-report.md` when the user needs a written artifact. Keep the main response actionable: goal, high-impact unknowns, recommended next step, and assumptions.
