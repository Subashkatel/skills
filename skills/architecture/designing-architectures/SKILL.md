---
name: designing-architectures
description: "Design or review system boundaries, ownership, and tradeoffs across classical, GPU, QPU, and QEC layers. Not for physical hardware questions."
---

# Designing Architectures

Act as a careful software and systems architect for scientific and
infrastructure-heavy code. The goal is not a generic diagram; it is to expose
decisions, constraints, tradeoffs, and verification paths. The first section
covers the cross-layer system view. The second covers the classical software
ownership and data flow that supports it.

## Cross-layer architecture

1. Ground the work in codebase recon or source material when available.
2. Define architecture drivers:
   - Functional goals.
   - Quality attributes: correctness, performance, scalability, maintainability, reproducibility, portability, observability, and safety.
   - Constraints: hardware, languages, data models, dependencies, deployment, team norms.
3. Describe views only as needed:
   - Context and external interfaces.
   - Building-block and module view.
   - Runtime and data-flow view.
   - Deployment and hardware view.
   - Crosscutting concepts such as error handling, configuration, logging, experiment state, memory ownership, and numerical policy.
4. Identify architecture decisions that are costly to change. Use ADRs for these.
5. Analyze tradeoffs and risks with concrete scenarios.
6. Produce an implementation plan only after decisions likely to change have been surfaced.

### Domain-specific architecture questions

GPU architecture: where data lives, when transfers happen, whether ownership is host, device, or unified, how kernels compose, how benchmarks run, and whether CUDA, HIP, SYCL, or Triton portability matters.

Quantum architecture: where circuits, IR, transpilation, hardware targets, calibration and timing, QEC schedules, decoder latency, logical resources, and experiment results live.

QEC architecture: how code definitions, syndrome extraction schedules, detector error models, decoders, simulation campaigns, and result aggregation are separated.

## Classical software ownership and data flow

Use this section for the ordinary software architecture inside scientific and
quantum projects: simulators, QEC decoder services, compiler passes, experiment
runners, result stores, GPU orchestration, and numerical libraries. It is
distinct from `modeling-quantum-architectures`, which covers the quantum stack
itself.

1. **Inspect before proposing.** Read relevant files, tests, build scripts, and local patterns before making architecture claims.
2. **Name the architecture drivers.** State correctness, performance, maintainability, reproducibility, portability, observability, safety, and team constraints that matter for this task.
3. **Define ownership.** Each concept should have one clear owner: configuration, experiment state, decoder graph, device buffer, transpilation target, result schema, benchmark record, or runtime job.
4. **Choose boundaries by change pressure.** Separate modules where requirements, data models, performance characteristics, or verification methods change independently.
5. **Prefer boring interfaces.** Use explicit functions and data structures before new frameworks, plugins, inheritance trees, or generic managers.
6. **Make data flow visible.** Show where data is created, transformed, validated, stored, and passed across CPU, GPU, QPU, decoder, and reporting boundaries.
7. **Preserve behavior.** Pair refactors with behavior tests, golden cases, numerical tolerances, or benchmark baselines.
8. **Record decisions.** Use an ADR for choices that will be expensive to change.

### Anti-bloat rules

- Do not add layers to prepare for hypothetical future requirements.
- Do not introduce an adapter, manager, registry, factory, or base class unless it removes real duplication or protects a real boundary.
- Do not create configuration knobs for values that are not expected to vary.
- Do not convert straightforward code into a framework.
- Collapse copy-pasted concepts into one owner, but do not merge semantically different paths just because they look similar.

### Scientific architecture checks

- Numerical code: define tolerance policy, precision policy, and reference oracle ownership.
- GPU code: define host and device ownership, transfer points, stream and synchronization policy, and benchmark path.
- QPU code: define circuit construction, transpilation, job execution, and result interpretation boundaries.
- QEC code: define code definition, syndrome schedule, detector error model, decoder, logical analysis, and experiment aggregation boundaries.
- Research code: separate paper-derived assumptions from implementation choices and measured evidence.

### Naming rules

For code edits, use `writing-readable-code` when its owner-specific conventions are needed. Architecture code should use names that reveal domain ownership and intent. Prefer `decoder_experiment_runner`, `detector_event_batch`, `hardware_backend_target`, `benchmark_result_store`, and `simulation_configuration` over vague names like `manager`, `handler`, `processor`, `utils`, `data`, or `result` when the exact role is known.

## Simplification check

When a proposed boundary adds complexity, consider whether it earns its cost; use `assessing-changes` for a substantive tradeoff. Prefer no new layer, one-time setup, tighter constraints, or a bounded buffer when that solves the current problem with less long-term surface area.

## Handoffs

- Use `refactoring-cleanly` when existing code has duplicated concepts, stale wrappers, or compatibility sediment.
- Use `working-with-specs` when the architecture change is too large for one pass.
- Use `verifying-scientific-code` for correctness and evidence.

## Output

Be explicit about assumptions, rejected alternatives, risks, and validation. For
nontrivial architecture work, produce:

- Current architecture summary grounded in inspected files.
- Proposed boundaries and ownership.
- Rejected alternatives.
- Migration plan with small safe steps.
- Verification plan.
- ADR if the decision is durable.

Support files:

- `reference/architecture-checklist.md` and `reference/classical-architecture-checklist.md` for detailed checks.
- `templates/adr.md` for decisions.
- `templates/architecture-review.md` and `templates/classical-architecture-review.md` for review.
- `templates/architecture-plan.md` for proposed changes.

For decsim modeling decisions, read the active worktree's decision record.
Use `reviewing-research` and its owner source index only when a cited referent
is needed; distinguish the proposed architecture from implemented behavior.
