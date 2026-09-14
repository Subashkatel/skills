---
name: assessing-changes
description: "Surface unresolved assumptions and simpler bounded alternatives before a costly change. Not for a typo or formatting edit."
---

# Assessing Changes

Two gates run before a costly design, experiment, or implementation. The first
asks what is still unknown. The second asks whether a smaller intervention
would do. Run the gate that the task needs; a small reversible edit needs
neither.

## Gate one: unknowns

Use this gate when unresolved assumptions could change the solution or the
validity of results. Resolve what the prompt and available evidence already
answer before asking. It is especially relevant for codebase refactors, GPU
kernels, quantum architecture, and QEC.

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

### Domain cues for unknowns

For GPU work, look for unknowns about hardware, memory layout, precision, problem size, benchmark protocol, profiler output, and portability.

For quantum and QEC work, look for unknowns about code family, distance, boundaries, stabilizers or gauge checks, noise model, decoder, syndrome schedule, logical observables, and target logical error rate.

For architecture work, look for unknowns about quality attributes, constraints, runtime paths, ownership, deployment, failure modes, and costly-to-change decisions.

## Gate two: approximation

Use this gate when a design or optimization has a meaningful complexity
tradeoff. Prefer the smallest correct intervention that preserves the required
semantics, evidence, and scientific constraints.

### Required first step

State the objective and the invariant that must not be broken. For scientific code, also state the allowed tolerance, error budget, resource budget, or proof obligation. If those are missing and the answer would change the architecture or validity of results, ask for them or propose conservative defaults and label them as assumptions.

### The approximation pass

Consider the applicable alternatives; this is a menu, not seven mandatory stages:

1. Can we not do this at all?
2. Can we do this only once?
3. Can we do this fewer times?
4. Can we approximate the result within an explicit, tested error budget?
5. Can we use a small lookup table?
6. Can we use a small FIFO or bounded buffer?
7. Can we constrain the problem further?

### Domain rules for approximation

- GPU and HPC: never claim a speedup without a baseline, repeated measurements, correctness comparison, and hardware or build context. Prefer removing transfers, reducing launches, improving locality, and constraining shapes before adding complex kernels.
- Numerical code: approximation is acceptable only with a named tolerance, representative adversarial cases, and a reference oracle or analytical bound.
- Quantum architecture: preserve circuit semantics, timing and control constraints, backend target assumptions, and resource accounting. Any approximation must state what layer it applies to.
- QEC: preserve stabilizer or gauge structure, logical observables, detector semantics, syndrome schedule assumptions, decoder inputs, and noise model. Do not trade correctness for speed without logical-error evidence.
- Architecture: avoid new abstractions until repeated use, clear ownership, or measurable complexity reduction justifies them.

## Output shape

Keep the main response actionable: goal, high-impact unknowns, recommended next
step, and assumptions. For a substantial approximation decision, summarize only
the applicable items:

- Verdict: do nothing, simplify, approximate, constrain, or proceed as planned.
- Recommended change: the smallest correct action.
- Rejected shortcuts: tempting alternatives that would break correctness, science, or maintainability.
- Evidence needed: tests, benchmarks, proofs, simulations, profiler output, or review questions.
- Follow-up note: what to record in implementation notes or git notes if the decision matters later.

## Support files

- `references/unknowns-taxonomy.md` for the unknowns categories in detail.
- `references/acton-approximator-scientific.md` for domain-specific approximation examples.
- `templates/unknowns-report.md` when the user needs a written unknowns artifact.
- `templates/approximation-review.md` for a saved design or review artifact.
