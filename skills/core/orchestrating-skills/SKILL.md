---
name: orchestrating-skills
description: "Chooses and sequences skills for long scientific coding work across recon, architecture, GPU, QPU, quantum, QEC, decoder, implementation, and verification."
---

# Orchestrating Skills

## Purpose

Choose the right skills and order for complex work. Do not load every skill. Pick the smallest sequence that reduces risk. For large work, prefer a factory loop: map unknowns, slice a living spec, implement verified slices, close the spec into durable rationale.

## Default sequences

### Architecture refactor
`mapping-unknowns` → `recon-codebases` → `designing-classical-architectures` or `designing-architectures` → `refactoring-cleanly` → `slicing-specs` for large work → `implementing-specs` → `verifying-scientific-code` → `closing-specs` → `explaining-changes`

### GPU optimization
`mapping-unknowns` → `recon-codebases` → `programming-gpus` → `writing-behavior-tests` → `slicing-specs` for multi-pass work → `implementing-specs` → `verifying-scientific-code` → `explaining-changes`

### Quantum architecture
`mapping-unknowns` → `reviewing-research` or `recon-codebases` → `modeling-quantum-architectures` → `designing-classical-architectures` for runtime/software boundaries → `planning-implementations` → `verifying-scientific-code`

### QEC implementation or experiment
`mapping-unknowns` → `reviewing-research` or `recon-codebases` → `engineering-qec` → `engineering-qec-decoders` if decoder behavior matters → `writing-behavior-tests` → `slicing-specs` → `implementing-specs` → `verifying-scientific-code` → `closing-specs` → `explaining-changes`

### GPU-accelerated QEC decoder
`mapping-unknowns` → `reviewing-research` → `recon-codebases` → `engineering-qec` → `engineering-qec-decoders` → `programming-gpus` → `designing-classical-architectures` → `slicing-specs` → `implementing-specs` → `writing-readable-code` → `verifying-scientific-code` → `closing-specs` → `explaining-changes`

### QPU programming
`mapping-unknowns` → `reviewing-research` or `recon-codebases` → `programming-qpus` → `modeling-quantum-architectures` if backend/runtime layers matter → `writing-behavior-tests` → `verifying-scientific-code` → `explaining-changes`

### QEC decoder implementation
`mapping-unknowns` → `reviewing-research` or `recon-codebases` → `engineering-qec` → `engineering-qec-decoders` → `designing-classical-architectures` for integration → `programming-gpus` only if accelerating → `writing-behavior-tests` → `verifying-scientific-code` → `closing-specs` → `explaining-changes`

## Orchestration rules

- Start with unknowns if the task is ambiguous.
- Start with recon if codebase truth matters.
- Start with research if paper/spec truth matters.
- Use only one primary domain skill at a time unless the task truly spans domains. Treat `programming-qpus`, `engineering-qec-decoders`, and `designing-classical-architectures` as primary domain skills when the work is specifically about QPU execution, decoder behavior, or classical software structure.
- Always include `maintaining-agent-state` for long work and verification for code, performance, math, quantum, or QEC claims.
- Produce an orchestration plan using `templates/orchestration-plan.md` for long tasks.
- Use `slicing-specs` when the implementation cannot be safely reviewed as one pass.
- Use `using-peer-agents` for independent review or explicitly authorized delegated implementation.
- Use `reviewing-rendered-output` or `debugging-gpu-renderers` only when visual/rendered artifacts matter.

## Scientific coding default sequence

For long scientific coding work, prefer this sequence: `recording-repo-memory` startup, `maintaining-agent-state`, `mapping-unknowns`, `recon-codebases` or `reviewing-research`, domain skill, `approximating-changes`, `planning-implementations`, implementation with `tracking-work-state`, `verifying-scientific-code`, final `approximating-changes` review, then `explaining-changes`.

## Factory loop

For long scientific coding work, prefer: `recording-repo-memory` startup, `maintaining-agent-state`, `mapping-unknowns`, `recon-codebases` or `reviewing-research`, domain skill, `approximating-changes`, `slicing-specs`, `implementing-specs`, `writing-behavior-tests`, `verifying-scientific-code`, `closing-specs`, and `explaining-changes`.

## Readable-code route

For any sequence that writes or refactors code, insert `writing-readable-code` after implementation and before final verification. For readability-focused refactors, use `recon-codebases` → `writing-readable-code` → `refactoring-cleanly` only if the readability problem is also an ownership/abstraction problem → `writing-behavior-tests` or existing tests → `verifying-scientific-code`.

Default long-run route: `recording-repo-memory` startup → `maintaining-agent-state` → `mapping-unknowns` → `recon-codebases` or `reviewing-research` → domain skill such as `designing-classical-architectures`, `programming-gpus`, `programming-qpus`, `modeling-quantum-architectures`, `engineering-qec`, or `engineering-qec-decoders` → `approximating-changes` → `slicing-specs` → `implementing-specs` → `writing-readable-code` → `writing-behavior-tests` → `verifying-scientific-code` → `closing-specs` → `explaining-changes`.


## Dynamic harness route

Use `running-task-harnesses` when a task is large, flaky, adversarial, parallel, or vulnerable to goal drift: deep verification, rule adherence, root-cause investigation, broad refactors, or skill evals. Keep a state store, explicit budget, verifier roles, and stop condition. Do not use a harness for routine single-file edits.
