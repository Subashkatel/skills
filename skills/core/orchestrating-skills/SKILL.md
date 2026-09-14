---
name: orchestrating-skills
description: "Select a small set of skills for a task spanning multiple scientific workflows. Skip routine single-workflow tasks."
---

# Orchestrating Skills

## Purpose

Choose the right skills and order for complex work. Do not load every skill. Pick the smallest sequence that reduces risk. Choose according to the next unresolved task, not a fixed chain.

## Select by the next unresolved job

| Need | Primary skill |
| --- | --- |
| Unfamiliar code path | `recon-codebases` |
| Material unknowns | `mapping-unknowns` |
| Paper or specification claim | `reviewing-research` |
| Software ownership and interfaces | `designing-classical-architectures` |
| Cross-layer system tradeoffs | `designing-architectures` or `modeling-quantum-architectures` |
| GPU kernel or transfer | `programming-gpus` |
| QPU circuit or job | `programming-qpus` |
| QEC code or syndrome schedule | `engineering-qec` |
| Decoder semantics or performance | `engineering-qec-decoders` |
| Multi-slice implementation | `slicing-specs` or `implementing-specs`, according to phase |

Load the chosen skill when its guidance is needed. Add another only when the
next job crosses its boundary; the table is not a reading sequence.

## Supporting work

- Use `writing-readable-code` for the owner's code conventions.
- Use `approximating-changes` for a real complexity or error-budget decision.
- Use `writing-behavior-tests` for test design, `verifying-scientific-code`
  for scientific claims, and `reviewing-rendered-output` for visual acceptance.
- Keep one existing task record for long work. `maintaining-agent-state`
  initializes or reconciles it; `tracking-work-state` updates it. Durable
  lessons and commit notes have separate purposes and are optional.
- Use `running-task-harnesses` only when repeated runs need coordination.
  Delegate only independent work permitted by the session's agent policy.
- Use `closing-specs` when archiving is part of completion and
  `explaining-changes` when a substantial reviewer handoff is useful.

## Completion

Complete the requested artifact and its applicable acceptance checks. Continue
through routine reversible work already authorized by the task. Stop for an
unresolved user-only decision, an actual external blocker, or user interruption.
Do not introduce extra approvals, reports, or files solely to satisfy a route.
