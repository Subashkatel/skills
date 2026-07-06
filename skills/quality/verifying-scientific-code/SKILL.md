---
name: verifying-scientific-code
description: "Verifies scientific code with tests, numerical tolerances, invariants, reproducibility, benchmarks, profiling, statistics, and evidence reports."
---

# Verifying Scientific Code

Use this skill whenever correctness, performance, numerical accuracy, hardware validity, or scientific interpretation matters. The output is evidence, not confidence language.

## Workflow

1. State the claim to verify.
2. Choose evidence: tests, reference implementation, invariants, algebra checks, benchmark/profiler output, simulator or hardware runs, confidence intervals, or source citations.
3. Run checks or provide exact commands when tools are unavailable.
4. Separate verified facts, failed checks, plausible hypotheses, skipped checks, and unverified assumptions.
5. Record reproducibility: command, seed, hardware, backend target, dependency versions, compiler flags, data, precision, simulator, and environment.
6. Update `tests.json`, `agent-state.json`, and domain logs when the verification result changes status or plan.
7. Produce a short verification report that leads with the outcome and then gives evidence.

## Domain checks

GPU: CPU/GPU comparison, tolerance, warmups, synchronization, repeated timings, profiler output, memory layout, occupancy tradeoffs, and floating-point non-associativity.

QPU: backend target, transpilation path, qubit/bit ordering, shot counts, simulator or hardware evidence, queue/runtime metadata, and statistical uncertainty.

QEC: stabilizer commutation, logical operator checks, syndrome schedule, detector error model assumptions, noise model, decoder configuration, shots, seeds, confidence intervals, logical error metrics, and threshold evidence.

QEC decoders: detector ordering, edge-weight convention, boundary handling, batch versus single-shot agreement, logical-observable prediction, latency, memory, and confidence intervals.

Architecture: scenario checks against quality attributes, migration safety, compatibility assumptions, and regression tests for runtime paths.

## Adversarial verification

For high-risk claims, pair with `running-task-harnesses` or `using-peer-agents`. Give verifiers the spec, rubric, and evidence, not the desired conclusion.

## Approximation evidence

If a change uses approximation, lookup tables, bounded buffers, or narrower constraints, verify the declared error budget or invariant directly. Distinguish exact equivalence, tolerance-bounded agreement, statistical confidence, and unverified assumptions.

## Readability gate

Changed code is not verified if it is hard to audit. Check for unexplained abbreviations, dense expressions, copy-paste blocks, unclear comments, and unnecessary abstractions. Record any justified tradeoff.
