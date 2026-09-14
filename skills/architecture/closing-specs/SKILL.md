---
name: closing-specs
description: "Close a completed implementation spec into decisions, invariants, and evidence using the repository archive convention."
---

# Closing Specs

A live spec is a build plan. A closed spec is a rationale record. Closing preserves why the shipped system has this shape and points readers to the code for how it works.

## Workflow

1. **Confirm shipped state.** Verify that implementation landed, required tests/profilers/simulations/reviews are complete, and unresolved slices are either done or explicitly out of scope.
2. **Diff plan against reality.** Read the spec and the code that shipped. Record divergences: dropped slices, renamed seams, changed assumptions, failed approaches, altered metrics, and new invariants.
3. **Archive by convention.** Follow the repository's existing archive location; use `specs/done/` only if appropriate, and preserve working links.
4. **Rewrite the README.** Replace build order with present-tense rationale: purpose, constraints, core decisions, invariants, tradeoffs, dead ends, and pointers into code/tests/benchmarks.
5. **Preserve evidence.** Keep benchmark baselines, QEC experiment records, profiler outputs, reference circuits, figures, and other artifacts that define why the result was accepted.
6. **Cut sediment.** Remove stale next steps, slice-by-slice instructions, temporary prompts, and mechanics that the code already states better.
7. **Audit claims.** Check each claim against code, tests, benchmarks, or recorded evidence. Fix unsupported or stale statements before calling the spec closed.
8. **Link durable lessons.** Add a separate memory note only for reusable information not already captured by the closed spec.

## Closed spec should contain

- What shipped and what problem it solves.
- Why the design is shaped this way.
- Invariants the implementation must keep honoring.
- Greppable pointers to modules, tests, benchmarks, experiments, and papers.
- Dead ends and why they failed.
- Evidence provenance: what data, circuits, seeds, baselines, hardware, or profilers supported acceptance.

## Smell test

- If a paragraph restates what a function does, replace it with a pointer.
- If it says “will”, “next”, or “slice N”, it is still a plan.
- If a future expert would re-run a failed approach without this note, record the dead end.
- If a performance or logical-error claim lacks environment, command, seed, tolerance, or confidence context, it is not durable.

## Done

The spec is archived using the repository convention, reads as rationale and invariants, names the code and evidence that support it, and has no stale build-plan instructions.
