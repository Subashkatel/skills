---
name: approximating-changes
description: "Assess simpler or bounded approximations when a proposed design or optimization adds complexity."
---

## Purpose

Use this skill when a design or optimization has a meaningful complexity tradeoff. Prefer the smallest correct intervention that preserves the required semantics, evidence, and scientific constraints.

## Required first step

State the objective and the invariant that must not be broken. For scientific code, also state the allowed tolerance, error budget, resource budget, or proof obligation. If those are missing and the answer would change the architecture or validity of results, ask for them or propose conservative defaults and label them as assumptions.

## The approximation pass

Consider the applicable alternatives; this is a menu, not seven mandatory stages:

1. Can we not do this at all?
2. Can we do this only once?
3. Can we do this fewer times?
4. Can we approximate the result within an explicit, tested error budget?
5. Can we use a small lookup table?
6. Can we use a small FIFO or bounded buffer?
7. Can we constrain the problem further?

## Domain rules

- GPU and HPC: never claim a speedup without a baseline, repeated measurements, correctness comparison, and hardware/build context. Prefer removing transfers, reducing launches, improving locality, and constraining shapes before adding complex kernels.
- Numerical code: approximation is acceptable only with a named tolerance, representative adversarial cases, and a reference oracle or analytical bound.
- Quantum architecture: preserve circuit semantics, timing/control constraints, backend target assumptions, and resource accounting. Any approximation must state what layer it applies to.
- QEC: preserve stabilizer or gauge structure, logical observables, detector semantics, syndrome schedule assumptions, decoder inputs, and noise model. Do not trade correctness for speed without logical-error evidence.
- Architecture: avoid new abstractions until repeated use, clear ownership, or measurable complexity reduction justifies them.

## Output format

For a substantial decision, summarize only the applicable items:

- Verdict: do nothing, simplify, approximate, constrain, or proceed as planned.
- Recommended change: the smallest correct action.
- Rejected shortcuts: tempting alternatives that would break correctness, science, or maintainability.
- Evidence needed: tests, benchmarks, proofs, simulations, profiler output, or review questions.
- Follow-up note: what to record in implementation notes or git notes if the decision matters later.

## Additional resources

- See `reference/acton-approximator-scientific.md` for domain-specific examples.
- Use `templates/approximation-review.md` for a saved design or review artifact.
