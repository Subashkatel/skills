---
name: verifying-scientific-code
description: "Verify numerical, performance, QPU, or QEC claims with oracles, uncertainty, and repeated runs. Not for routine software checks."
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
7. Produce a short verification report that leads with the outcome and then gives evidence. Use `templates/verification-report.md` and `templates/verification-matrix.md`; `reference/verification-checklist.md` holds the detailed checks and `scripts/compare_numeric_csv.py` compares numeric result files.

## Domain checks

GPU: CPU/GPU comparison, tolerance, warmups, synchronization, repeated timings, profiler output, memory layout, occupancy tradeoffs, and floating-point non-associativity.

QPU: backend target, transpilation path, qubit/bit ordering, shot counts, simulator or hardware evidence, queue/runtime metadata, and statistical uncertainty.

QEC: stabilizer commutation, logical operator checks, syndrome schedule, detector error model assumptions, noise model, decoder configuration, shots, seeds, confidence intervals, logical error metrics, and threshold evidence.

QEC decoders: detector ordering, edge-weight convention, boundary handling, batch versus single-shot agreement, logical-observable prediction, latency, memory, and confidence intervals.

Architecture: scenario checks against quality attributes, migration safety, compatibility assumptions, and regression tests for runtime paths.

## Adversarial verification

For high-risk claims, use a task harness as described below, or `using-peer-agents`. Give verifiers the spec, rubric, and evidence, not the desired conclusion.

For a consequential derivation, give each nontrivial claim an ID, assumptions,
dependencies, evidence, and status. Expand disputed steps instead of repeatedly
asking for a verdict on the whole argument. Verify that the theorem, test, or
formal statement still expresses the original scientific claim; a passing check
can certify the wrong statement. Label sketches, unchecked axioms, and proof
placeholders explicitly. Independent reviews can share errors, so agreement is
not a substitute for a counterexample search or an external check.

## Task harnesses for repeated runs

Use a harness when one context window is risky: flaky tests, large refactors, deep verification, rule adherence, root-cause investigation, broad research, skill evals, or parallel GPU/QPU/QEC experiments. Do not use one for simple single-file edits or routine questions.

A harness is a temporary workflow with roles, state, verification, stop conditions, and a budget. It can use Claude Code workflows, Codex tasks, peer agents, shell scripts, or manual focused passes depending on the available tool harness. See `reference/harness-patterns.md`, and use `templates/harness-plan.md` and `templates/harness-result.md` when a written harness record is useful.

### Harness contract

Before running, define:

1. Goal and non-goals.
2. State store: `agent-state.json`, spec README, `tests.json`, or `harness-runs/<name>/`.
3. Work units: files, tests, hypotheses, slices, rules, claims, seeds, or benchmark cases.
4. Agent roles: classifier, worker, verifier, synthesizer, or judge.
5. Isolation: worktrees, read-only reviews, sandbox limits, and who may edit.
6. Verification rubric and evidence required.
7. Completion condition tied to the requested contract. A budget limit stops execution but does not establish completion.
8. Honor user-specified budgets and resource limits. Do not invent a token limit or require one before useful work.

### Harness patterns

- **Classify and act:** classify files, failures, rules, or claims, then route each class to the right check.
- **Fan out and synthesize:** split independent units, run them in clean contexts, then merge structured results.
- **Adversarial verification:** assign a separate verifier to challenge each worker result against a rubric.
- **Generate and filter:** create many hypotheses or designs, dedupe, test, and keep only the strongest.
- **Tournament:** compare alternatives pairwise when relative judgment is more reliable than absolute scoring.
- **Loop until done:** continue until the stop condition is met, not until a fixed number of passes finishes.

### Harness uses and safety

For rule adherence, create one verifier per important rule in `AGENTS.md` or the active spec. For flaky tests, run independent hypothesis agents over logs, code paths, seeds, and environment. For QEC/GPU/QPU experiments, split by seed ranges, devices, distances, noise models, circuits, or benchmarks only when they do not share mutable state.

Keep run evidence in the existing task record or an allowed temporary directory. Use a separate harness folder only when multiple runs need it; do not duplicate the current plan.

Quarantine untrusted inputs: agents that read public issues, web pages, logs, or generated content should not take high-privilege actions. The orchestrator owns edits, commits, destructive commands, and final claims.

A harness is done when sub-results are synthesized, verifier disagreements are resolved or recorded, evidence is attached, state files are updated, and the final answer distinguishes verified findings from open risks.

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
