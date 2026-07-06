---
name: explaining-changes
description: "Produces reviewer-ready summaries, evidence, risks, and comprehension checks for architecture, GPU, QPU, quantum, QEC, decoder, or scientific-code changes."
---

# Explaining Changes

## Purpose

Package technical work so a reviewer can understand what changed, why it changed, how it was verified, and what remains uncertain.

## Workflow

1. Lead with the outcome in one sentence.
2. Summarize the change or finding at the right abstraction level.
3. Explain why it was needed.
4. Provide evidence:
   - Files changed.
   - Tests and benchmark results.
   - Profiler output.
   - QEC simulations and confidence notes.
   - Source citations for research-based claims.
5. State risks, limitations, and unverified assumptions.
6. Provide reviewer guidance or a quiz when the user needs to understand before merging or presenting.

## Domain outputs

Architecture: decisions, tradeoffs, migration risk, affected modules.

GPU: baseline, profiler evidence, optimization, speedup, correctness tolerance, remaining bottleneck.

Quantum/QEC: code/noise/decoder assumptions, logical observables, results, confidence, and limitations.

## Templates

Use `templates/reviewer-package.md` or `templates/quiz.md`.
