---
name: designing-architectures
description: "Designs scientific system architecture across classical, GPU, QPU, quantum runtime, QEC, and decoder layers. Use for boundaries, ADRs, tradeoffs, and runtime views."
---

# Designing Architectures

## Purpose

Help the coding agent act as a careful software/systems architect for scientific and infrastructure-heavy code. The goal is not to draw a generic diagram; it is to expose decisions, constraints, tradeoffs, and verification paths.

## Architecture workflow

1. Ground the work in codebase recon or source material when available.
2. Define architecture drivers:
   - Functional goals.
   - Quality attributes: correctness, performance, scalability, maintainability, reproducibility, portability, observability, and safety.
   - Constraints: hardware, languages, data models, dependencies, deployment, team norms.
3. Describe views only as needed:
   - Context and external interfaces.
   - Building-block/module view.
   - Runtime/data-flow view.
   - Deployment/hardware view.
   - Crosscutting concepts such as error handling, configuration, logging, experiment state, memory ownership, and numerical policy.
4. Identify architecture decisions that are costly to change. Use ADRs for these.
5. Analyze tradeoffs and risks with concrete scenarios.
6. Produce an implementation plan only after decisions likely to change have been surfaced.

## Domain-specific architecture questions

GPU architecture: where data lives, when transfers happen, whether ownership is host/device/unified, how kernels compose, how benchmarks run, and whether CUDA/HIP/SYCL/Triton portability matters.

Quantum architecture: where circuits, IR, transpilation, hardware targets, calibration/timing, QEC schedules, decoder latency, logical resources, and experiment results live.

QEC architecture: how code definitions, syndrome extraction schedules, detector error models, decoders, simulation campaigns, and result aggregation are separated.

## Outputs

Use `designing-classical-architectures` when the task is specifically about non-quantum software boundaries, APIs, state ownership, runtime services, or maintainability. Use:

- `templates/adr.md` for decisions.
- `templates/architecture-review.md` for review.
- `templates/architecture-plan.md` for proposed changes.

Be explicit about assumptions, rejected alternatives, risks, and validation.

## Simplification check

Before introducing a new abstraction, service boundary, data model, or subsystem, apply `approximating-changes`. Prefer no new layer, one-time setup, tighter constraints, or a bounded buffer when that solves the current problem with less long-term surface area.
