---
name: designing-classical-architectures
description: "Designs maintainable classical software architecture for simulators, compilers, runtimes, QEC tools, decoders, services, and experiment pipelines."
---

# Designing Classical Architectures

## Purpose

Help the agent design ordinary software architecture well: clear ownership, simple data flow, explicit interfaces, minimal abstraction, and evidence-backed tradeoffs. Use this for classical architecture inside quantum projects too: simulators, QEC decoder services, compiler passes, experiment runners, result stores, GPU orchestration, and numerical libraries.

This skill is separate from `modeling-quantum-architectures`. Use this skill for the classical code structure that supports the quantum or scientific work.

## Classical architecture workflow

1. **Inspect before proposing.** Read relevant files, tests, build scripts, and local patterns before making architecture claims.
2. **Name the architecture drivers.** State correctness, performance, maintainability, reproducibility, portability, observability, safety, and team constraints that matter for this task.
3. **Define ownership.** Each concept should have one clear owner: configuration, experiment state, decoder graph, device buffer, transpilation target, result schema, benchmark record, or runtime job.
4. **Choose boundaries by change pressure.** Separate modules where requirements, data models, performance characteristics, or verification methods change independently.
5. **Prefer boring interfaces.** Use explicit functions and data structures before new frameworks, plugins, inheritance trees, or generic managers.
6. **Make data flow visible.** Show where data is created, transformed, validated, stored, and passed across CPU, GPU, QPU, decoder, and reporting boundaries.
7. **Preserve behavior.** Pair refactors with behavior tests, golden cases, numerical tolerances, or benchmark baselines.
8. **Record decisions.** Use an ADR for choices that will be expensive to change.

## Anti-bloat rules

- Do not add layers to prepare for hypothetical future requirements.
- Do not introduce an adapter, manager, registry, factory, or base class unless it removes real duplication or protects a real boundary.
- Do not create configuration knobs for values that are not expected to vary.
- Do not convert straightforward code into a framework.
- Collapse copy-pasted concepts into one owner, but do not merge semantically different paths just because they look similar.

## Scientific architecture checks

- Numerical code: define tolerance policy, precision policy, and reference oracle ownership.
- GPU code: define host/device ownership, transfer points, stream/synchronization policy, and benchmark path.
- QPU code: define circuit construction, transpilation, job execution, and result interpretation boundaries.
- QEC code: define code definition, syndrome schedule, detector error model, decoder, logical analysis, and experiment aggregation boundaries.
- Research code: separate paper-derived assumptions from implementation choices and measured evidence.

## Readability rules

Use `writing-readable-code` with this skill. Architecture code should use names that reveal domain ownership and intent. Prefer `decoder_experiment_runner`, `detector_event_batch`, `hardware_backend_target`, `benchmark_result_store`, and `simulation_configuration` over vague names like `manager`, `handler`, `processor`, `utils`, `data`, or `result` when the exact role is known.

## Handoffs

- Use `designing-architectures` when the task needs a broader system review across classical, GPU, quantum, and QEC layers.
- Use `refactoring-cleanly` when existing code has duplicated concepts, stale wrappers, or compatibility sediment.
- Use `slicing-specs` when the architecture change is too large for one pass.
- Use `verifying-scientific-code` for correctness and evidence.

## Output

For nontrivial architecture work, produce:

- Current architecture summary grounded in inspected files.
- Proposed boundaries and ownership.
- Rejected alternatives.
- Migration plan with small safe steps.
- Verification plan.
- ADR if the decision is durable.
