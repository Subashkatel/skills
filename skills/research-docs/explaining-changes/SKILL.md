---
name: explaining-changes
description: "Write a reviewer handoff for substantial technical changes, connecting behavior, rationale, and validation."
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
6. Give reviewer guidance when useful. Include a quiz only if the user requests one.

## Domain outputs

Architecture: decisions, tradeoffs, migration risk, affected modules.

GPU: baseline, profiler evidence, optimization, speedup, correctness tolerance, remaining bottleneck.

Quantum/QEC: code/noise/decoder assumptions, logical observables, results, confidence, and limitations.

## Templates

Use `templates/reviewer-package.md` for a substantial handoff; use `templates/quiz.md` only for a requested comprehension exercise. Keep ordinary summaries short and use no em dashes.
