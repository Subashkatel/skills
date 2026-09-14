---
name: verifying-scientific-code
description: "Verify numerical, performance, QPU, or QEC claims with appropriate oracles, uncertainty, and reproducible evidence."
---

# Verifying Scientific Code

Use this skill to substantiate a scientific or hardware claim whose validity needs more than routine software checks. The output is evidence, not confidence language.

## Workflow

1. State the claim to verify.
2. Choose evidence: tests, reference implementation, invariants, algebra checks, benchmark/profiler output, simulator or hardware runs, confidence intervals, or source citations.
3. Run checks or provide exact commands when tools are unavailable.
4. Separate verified facts, failed checks, plausible hypotheses, skipped checks, and unverified assumptions.
5. Record reproducibility: command, seed, hardware, backend target, dependency versions, compiler flags, data, precision, simulator, and environment. For Slurm, keep launch scripts on a shared filesystem and verify headers, libraries, and ABI inside the compute allocation; login-node availability is not evidence of compute-node availability.
6. Record results in the existing evidence ledger; update task status when the outcome changes the plan. Do not require parallel state files.
7. Produce a short verification report that leads with the outcome and then gives evidence.

## Domain checks

GPU: CPU/GPU comparison, tolerance, warmups, synchronization, repeated timings, profiler output, memory layout, occupancy tradeoffs, and floating-point non-associativity.

QPU: backend target, transpilation path, qubit/bit ordering, shot counts, simulator or hardware evidence, queue/runtime metadata, and statistical uncertainty.

QEC: stabilizer commutation, logical operator checks, syndrome schedule, detector error model assumptions, noise model, decoder configuration, shots, seeds, confidence intervals, logical error metrics, and threshold evidence.

QEC decoders: detector ordering, edge-weight convention, boundary handling, batch versus single-shot agreement, logical-observable prediction, latency, memory, and confidence intervals.

Architecture: scenario checks against quality attributes, migration safety, compatibility assumptions, and regression tests for runtime paths.

## Adversarial verification

For high-risk claims, pair with `running-task-harnesses` or `using-peer-agents`. Give verifiers the spec, rubric, and evidence, not the desired conclusion.

For a consequential derivation, give each nontrivial claim an ID, assumptions,
dependencies, evidence, and status. Expand disputed steps instead of repeatedly
asking for a verdict on the whole argument. Verify that the theorem, test, or
formal statement still expresses the original scientific claim; a passing check
can certify the wrong statement. Label sketches, unchecked axioms, and proof
placeholders explicitly. Independent reviews can share errors, so agreement is
not a substitute for a counterexample search or an external check.

## Approximation evidence

If a change uses approximation, lookup tables, bounded buffers, or narrower constraints, verify the declared error budget or invariant directly. Distinguish exact equivalence, tolerance-bounded agreement, statistical confidence, and unverified assumptions.

## Readability gate

Changed code is not verified if it is hard to audit. Check for unexplained abbreviations, dense expressions, copy-paste blocks, unclear comments, and unnecessary abstractions. Record any justified tradeoff.

## Model and source credibility

For simulation validation or source-derived cost models, read
`references/source-credibility.md`. Define intended use; distinguish verification
from empirical validation, measured values from surrogates, and timing-model
results from logical-error evidence. Use the `reviewing-research` source index
for the owner's local corpus. No checklist by itself establishes NASA compliance.
