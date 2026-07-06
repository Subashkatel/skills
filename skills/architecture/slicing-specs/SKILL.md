---
name: slicing-specs
description: "Breaks large scientific goals into independently verifiable specs and slices with contracts, evidence gates, and next-agent handoffs."
---

# Slicing Specs

Turn a large technical goal into a ladder of small contracts. Each slice should be independently understandable, implementable, and verifiable before the whole system exists.

## Workflow

1. **Interrogate before slicing.** Combine `mapping-unknowns`, `recon-codebases`, and `reviewing-research` as needed. Ask one question at a time only when repo or source inspection cannot answer it.
2. **Name the scientific contract.** State the invariant, API seam, algorithmic property, benchmark target, numerical tolerance, decoder behavior, or hardware constraint the slice proves.
3. **Slice at seams.** Prefer module boundaries, typed interfaces, kernel or pass boundaries, test oracles, experiment harnesses, decoder interfaces, transpiler stages, and data contracts. A slice that needs unrelated systems to be accepted is too broad.
4. **Add a runnable artifact per slice.** Examples: focused unit test, benchmark harness, profiler trace, small kernel, QEC circuit/noise fixture, detector-error-model sample, simulator probe, reproducibility script, or architecture decision record.
5. **Research the fog.** If a slice depends on a paper, vendor API, architecture standard, QEC construction, decoder, GPU feature, or reference implementation, add a research or replication spike before the implementation slice.
6. **Draft more than once for high-risk work.** For major redesigns, ask independent agents or passes to propose slice graphs from the same brief, then synthesize. Agreement means stable ground; disagreement marks where to inspect harder.
7. **Run the minimization gate.** Use `approximating-changes` and `refactoring-cleanly` to remove fake flexibility, duplicated concepts, dev-only compatibility layers, or unneeded abstractions before freezing the spec.
8. **Materialize the spec.** For multi-slice work, create `specs/<feature>/README.md` plus `specs/<feature>/slices/<nn>-<name>.md`. Keep evidence, fixtures, benchmark baselines, and references under the spec folder when they define acceptance.
9. **Write the handoff.** The README needs a current pickup point, dependency graph, global TODOs, verification gates, and a direct “Next Agent Prompt” a fresh agent can follow without chat history.

## Slice contract

Each slice file answers:

- What contract does this unlock?
- What is the seam and who owns it?
- What must stay unchanged?
- What evidence proves correctness?
- What benchmark, tolerance, stochastic confidence, or QEC logical-error metric applies?
- What human decision could change this slice?
- What later slice removes any temporary seam?

## Scientific slicing rules

- For GPU work, never treat speedup as done without a correctness oracle, baseline, profiler evidence, and repeatable measurement environment.
- For numerical work, state exact equality, tolerance-bounded agreement, or statistical confidence explicitly.
- For QEC work, slice detector semantics, logical observables, noise assumptions, decoder behavior, and threshold/logical-error evidence separately when any one could fail independently.
- For architecture work, slice concept ownership first, then consumers. Avoid building adapters around a duplicated concept.
- Reslicing is progress. When implementation exposes hidden variables, update the spec before widening the patch.

## Done

The spec is done when a fresh agent can start with the README, pick the same next slice, know the contracts and gates, and verify each slice without relying on the original conversation.
