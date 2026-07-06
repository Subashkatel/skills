---
name: planning-implementations
description: "Creates reviewable implementation plans after recon or research. Use before costly architecture, GPU, QPU, QEC, decoder, or scientific-code edits."
---

# Planning Implementations

## Purpose

Create a plan that is useful to review before work starts. Lead with decisions most likely to change, not mechanical steps.

## Workflow

1. Confirm the goal, scope, and non-goals.
2. Summarize evidence from recon, research, or unknown mapping.
3. Lead with change-sensitive decisions:
   - Architecture: module boundaries, APIs, data models, ownership, dependencies.
   - GPU: data layout, kernel decomposition, precision, benchmark protocol, portability.
   - Quantum/QEC: code/noise/decoder assumptions, circuit IR, schedules, metrics.
4. Propose the implementation sequence.
5. Define tests, benchmarks, simulations, and review checkpoints.
6. Identify rollback or conservative alternatives.
7. State when to pause for user input.

## Output

Use `templates/implementation-plan.md`. Keep it reviewable. Avoid drowning the user in mechanical edits that are unlikely to change.

## Minimization gate

Before committing to an expensive implementation path, invoke or apply `approximating-changes`. Lead the plan with decisions that could shrink or remove the work: not doing it, doing it once, doing it fewer times, using an explicit error-bounded approximation, using a lookup table, using a FIFO, or constraining the problem.
