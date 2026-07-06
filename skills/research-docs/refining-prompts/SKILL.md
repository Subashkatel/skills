---
name: refining-prompts
description: "Turns rough prompts into clear agent prompts for Claude Code, Codex, or similar coding agents with context, constraints, unknowns, and verification criteria."
---

# Refining Prompts

## Purpose

Turn rough prompts into precise prompts for Claude Code, Codex, or another coding agent. The output should help the agent act like a careful technical collaborator, not a generic assistant.

## Process

1. Identify the real deliverable: architecture review, code edit, kernel optimization, QEC experiment, research synthesis, verification, or explanation.
2. Add the reason for the request so the target agent can connect details to intent.
3. Add domain constraints:
   - Architecture: quality attributes, scope, constraints, ADR needs.
   - GPU: target hardware, programming stack, precision, data layout, benchmark protocol.
   - Quantum architecture: layer, hardware assumptions, circuit IR, ISA, transpilation, decoder latency.
   - QEC: code family, distance, schedule, noise model, decoder, metrics.
4. Add an unknowns step before implementation when ambiguity could change the solution.
5. Require evidence: files read, tests, profiler output, algebra checks, simulations, citations, or benchmark logs.
6. Specify whether the target agent should only advise, inspect files, edit code, or run experiments.
7. Avoid instructions that request hidden reasoning. Ask for concise rationale, assumptions, checks, and evidence instead.

## Output

Use `templates/refined-prompt-package.md`. Include:

- Recommended skills.
- Recommended effort level or working mode.
- Final prompt.
- Assumptions.
- Questions only if the prompt cannot be made safe without answers.
