---
name: practicing-tdd
description: "Use a red-green-refactor loop when test-first development is requested or chosen for a behavior change."
---

# Practicing TDD

Use this skill when test-first work is requested or is the chosen approach for a real behavior change. A typo, prose edit, or formatting-only change does not need a new behavior test. TDD is one small loop at a time.

## Red-green-refactor loop

1. State the smallest behavior or bug contract to pin.
2. Write or modify one readable behavior test through the public surface when practical.
3. Run the narrowest relevant command and record red. If red cannot be produced because the harness is absent, behavior already exists, or hardware is unavailable, record why.
4. Implement the minimum readable change needed for green. Do not add unrelated cleanup, broad abstractions, feature flags, or speculative flexibility.
5. Run the narrow test until green, then the nearest broader gate.
6. Refactor only the touched scope with `writing-readable-code`; rerun affected tests.
7. Record the meaningful red/green evidence and limitations in the existing task record or final report. Do not create state files solely for a small regression.

## Test quality rules

- Tests verify contracts, not implementation details.
- A regression test written after the fix should be falsified once when practical.
- Do not delete, weaken, skip, or repin tests just to get green.
- If a test seems wrong, prove the contract changed and record the reason.
- If no contract exists, ask or create a characterization test before changing behavior.

## Scientific adaptations

GPU: use a CPU or analytic oracle before optimization; record tolerance, synchronization, device, compiler flags, warmup, repetitions, and profiler evidence.

QPU: prefer simulator checks before hardware claims; record backend target, transpilation path, shots, qubit/bit ordering, and uncertainty.

QEC and decoders: pin stabilizers, logical observables, detector model assumptions, syndrome schedule, detector ordering, decoder predictions, seeds, shots, and confidence intervals.

Architecture: add characterization, contract, migration, or integration tests around behavior that must not change before refactoring boundaries.

## When pure TDD does not fit

For exploratory research, hardware bring-up, unknown scientific behavior, or performance discovery, first create an oracle, invariant, characterization test, or experiment record. Do not claim TDD completion until there is a repeatable check.

## Done

Done means red was attempted and explained, green was proven with commands, refactoring preserved green, and evidence was recorded. Load a supporting skill only for a test-design or scientific-evidence question this loop does not answer.
