---
name: modeling-quantum-architectures
description: "Models quantum architecture across hardware, control, circuit IR, transpilation, runtime, QEC, decoder, and application layers."
---

# Modeling Quantum Architectures

## Purpose

Help the coding agent reason about quantum architecture as a layered system, not as isolated circuits. Use this when decisions span hardware constraints, control timing, circuit representations, transpilation, QEC schedules, decoders, and logical resources.

## Layered workflow

1. State the architecture level being discussed:
   - Physical qubit modality and device topology.
   - Control/timing/calibration layer.
   - Circuit or pulse representation.
   - Compiler/transpiler and hardware target.
   - QEC/logical layer.
   - Decoder/runtime feedback layer.
   - Application/resource-estimation layer.
2. Gather assumptions:
   - Gate set, connectivity, durations, error rates, measurement/reset behavior.
   - Classical feedback and timing constraints.
   - Circuit IR format and transformations.
   - QEC code and syndrome schedule if fault tolerance is involved.
3. Map data/control flow from logical intent to hardware execution and back through measurement/decoder feedback.
4. Identify bottlenecks and risks:
   - Routing overhead.
   - Decoder latency.
   - Measurement/reset cadence.
   - Calibration drift.
   - Error model mismatch.
   - Classical/quantum interface constraints.
5. Produce an architecture artifact using `templates/quantum-architecture-review.md` or an ADR.

## Guardrails

- Do not fabricate current hardware capabilities, error rates, thresholds, or roadmaps.
- Mark preprint-derived or vendor-specific claims clearly.
- When source docs or papers are provided, extract assumptions before proposing architecture.
- For implementation tasks, hand off to `programming-qpus`, `engineering-qec`, `engineering-qec-decoders`, `programming-gpus`, `designing-classical-architectures`, or `designing-architectures` as appropriate.

## Quantum architecture readability rules

Architecture code and docs must use names that reveal the layer and contract: physical qubit, logical qubit, control pulse, backend target, circuit instruction, transpiler pass, runtime job, syndrome schedule, decoder latency, and logical-resource estimate. Avoid generic adapters and managers unless the specific role is named at the boundary.
