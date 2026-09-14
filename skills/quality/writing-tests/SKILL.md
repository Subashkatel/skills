---
name: writing-tests
description: "Write behavior tests, and run a test-first loop when chosen, for real contracts. Not for prose or formatting changes."
---

# Writing Tests

A good test fails when real behavior breaks and survives refactors that preserve
the contract. The first section designs the test. The second runs the test-first
loop when that is the chosen approach. Later sections hold the clocked RTL
protocol rules and the scientific evidence rules.

## Designing a behavior test

1. Name the plausible wrong implementation a new test catches that existing tests miss. Prefer a property or metamorphic check when it captures the law. Write one tracer test at a time. Assert the contract, see it fail when possible, make the code earn green, then choose the next test from what you learned.
2. Use the focused runner, then required repository gates. Broaden or repeat checks when changes, failures, or unresolved risk justify it.
3. Assert observable behavior through the outermost practical surface: return values, persisted state, command output, CPU/GPU oracle comparison, circuit output, syndrome stream, detector model, logical outcome, or benchmark metric.
4. Control variables: seed, data size, device, precision mode, noise model, circuit, decoder, and configuration unless that variable is the subject.
5. Treat stochastic claims statistically. Use repeated seeds, bands, confidence intervals, and recorded random seeds.
6. Mock at edges: network, clock, filesystem, GPU availability, external service, hardware backend, or config lookup. Avoid mocking internal collaborators when an observable layer can exercise them.
7. Falsify important regression tests against the original defect or a controlled mutation in an isolated copy. Confirm the expected failure and preserve the working tree.
8. Promote useful probes. Delete scratch probes after use or turn them into durable tests when they guard real behavior.

Use `references/scientific-test-checklist.md` for the domain checks in detail.

### What not to assert

- Type guarantees the compiler already enforces.
- Internal helper calls when public behavior is observable.
- Collection sizes without checking canonical values.
- Current constants, config values, or measured baselines unless they are the contract.
- Single lucky samples for stochastic behavior.

### Red test triage

When a test fails after a change, check whether the test pinned deleted semantics, an uncontrolled variable leaked in, a stochastic margin is too tight, or the code is actually wrong. Probe before tuning constants.

### Test readability

Tests must be as readable as production code. Name fixtures, seeds, tolerances, detector IDs, launch configurations, backend targets, and expected values by role. Avoid copy-pasted setup blocks; create a shared fixture only when it represents a real repeated test concept.

## Test-first loop

Use this section when test-first work is requested or is the chosen approach for
a real behavior change. A typo, prose edit, or formatting-only change does not
need a new behavior test. The loop is one small step at a time.

1. State the smallest behavior or bug contract to pin.
2. Write or modify one readable behavior test through the public surface when practical.
3. Run the narrowest relevant command and record red. If red cannot be produced because the harness is absent, behavior already exists, or hardware is unavailable, record why.
4. Implement the minimum readable change needed for green. Do not add unrelated cleanup, broad abstractions, feature flags, or speculative flexibility.
5. Run the narrow test until green, then the nearest broader gate.
6. Refactor only the touched scope with `writing-readable-code`; rerun affected tests.
7. Record the meaningful red and green evidence and limitations in the existing task record or final report. Do not create state files solely for a small regression. `templates/tdd-record.json` and `scripts/validate_tests_json.py` cover the record format and its check.

### Loop quality rules

- Tests verify contracts, not implementation details.
- A regression test written after the fix should be falsified once when practical.
- Do not delete, weaken, skip, or repin tests just to get green.
- If a test seems wrong, prove the contract changed and record the reason.
- If no contract exists, ask or create a characterization test before changing behavior.

### When a pure test-first loop does not fit

For exploratory research, hardware bring-up, unknown scientific behavior, or performance discovery, first create an oracle, invariant, characterization test, or experiment record. Do not claim test-first completion until there is a repeatable check.

The loop is done when red was attempted and explained, green was proven with commands, refactoring preserved green, and evidence was recorded.

## Clocked RTL protocols

Compile every conditional testbench variant, including negative monitor modes, before expensive builds. A passing positive variant does not establish that the negative mode elaborates; keep these checks in the permitted compute environment.

Drive stimulus away from the sampling edge to avoid testbench races. Check valid and payload at the acceptance edge before nonblocking updates. After any stalled cycle, require valid and unchanged payload on the next edge even when ready becomes high. Reject unknown control values and unknown payload whenever valid is asserted, including stalled cycles. Falsify the monitor with a result that changes only on stall release.

## Scientific adaptations

GPU: use a CPU or analytic oracle before optimization; record tolerance, synchronization, device, compiler flags, warmup, repetitions, and profiler evidence.

QPU: prefer simulator checks before hardware claims; record backend target, transpilation path, shots, qubit and bit ordering, and uncertainty.

QEC and decoders: pin stabilizers, logical observables, detector model assumptions, syndrome schedule, detector ordering, decoder predictions, seeds, shots, and confidence intervals.

Architecture: add characterization, contract, migration, or integration tests around behavior that must not change before refactoring boundaries.

## State integration

Record the evidence in the existing task record or report; update the plan only when results change it. Load a supporting skill only for a test-design or scientific-evidence question this skill does not answer.

For decsim tests, read the active worktree's `STYLE.md`: assertions for maintained
internal invariants do not need dedicated tests, and unreachable invalid states
are not new requirements. Keep meaningful values in the test and histories in
reports. Preserve required regression coverage when pruning duplicate tests.
