---
name: writing-behavior-tests
description: "Writes behavior tests that pin real contracts, invariants, tolerances, stochastic claims, QEC semantics, GPU behavior, and edge cases without overfitting."
---

# Writing Behavior Tests

A good test fails when real behavior breaks and survives refactors that preserve the contract.

## Workflow

1. Write one tracer test at a time. Assert the contract, see it fail when possible, make the code earn green, then choose the next test from what you learned.
2. Use the fastest focused runner first. Run broader suites as final gates.
3. Assert observable behavior through the outermost practical surface: return values, persisted state, command output, CPU/GPU oracle comparison, circuit output, syndrome stream, detector model, logical outcome, or benchmark metric.
4. Control variables: seed, data size, device, precision mode, noise model, circuit, decoder, and configuration unless that variable is the subject.
5. Treat stochastic claims statistically. Use repeated seeds, bands, confidence intervals, and recorded random seeds.
6. Mock at edges: network, clock, filesystem, GPU availability, external service, hardware backend, or config lookup. Avoid mocking internal collaborators when an observable layer can exercise them.
7. Falsify important tests. For a regression test written after a fix, break or revert the production path once and confirm red for the expected reason, then restore and confirm green.
8. Promote useful probes. Delete scratch probes after use or turn them into durable tests when they guard real behavior.

## What not to assert

- Type guarantees the compiler already enforces.
- Internal helper calls when public behavior is observable.
- Collection sizes without checking canonical values.
- Current constants, config values, or measured baselines unless they are the contract.
- Single lucky samples for stochastic behavior.

## Red test triage

When a test fails after a change, check whether the test pinned deleted semantics, an uncontrolled variable leaked in, a stochastic margin is too tight, or the code is actually wrong. Probe before tuning constants.

## Test readability

Tests must be as readable as production code. Name fixtures, seeds, tolerances, detector IDs, launch configurations, backend targets, and expected values by role. Avoid copy-pasted setup blocks; create a shared fixture only when it represents a real repeated test concept.

## State integration

For TDD, pair with `practicing-tdd`. Record red, green, refactor, final gate, seeds, tolerances, skipped checks, and blockers in `tests.json`. Update `agent-state.json` when test results change the plan.
