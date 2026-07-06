---
name: engineering-qec
description: "Designs, implements, reviews, and verifies QEC systems: codes, stabilizers, syndrome schedules, detector error models, logical observables, and simulations."
---

# Engineering QEC

## Purpose

Help the coding agent work carefully on quantum error correction. The focus is on explicit assumptions, algebraic checks, simulator/decoder configuration, and honest interpretation of evidence.

## QEC workflow

1. Specify the task type: code design, circuit construction, decoder implementation, simulation, threshold study, architecture integration, or paper reproduction.
2. Record the code definition:
   - Code family and parameters.
   - Stabilizer or gauge generators.
   - Boundaries and distance.
   - Logical operators.
   - Syndrome extraction schedule.
3. Verify algebra before simulation:
   - Stabilizers commute.
   - Logical operators commute with stabilizers and anticommute with their paired logicals.
   - Claimed distance or detectable errors are either proved, computed, or marked as an assumption.
4. Specify the noise model:
   - Circuit-level or phenomenological.
   - Measurement errors and correlated errors.
   - Pauli/stabilizer assumptions or non-Pauli limitations.
5. Configure the decoder:
   - MWPM, union-find, belief propagation, tensor/network, neural, custom, or exact small-code decoder.
   - Graphlike detector-error-model assumptions if using matching.
   - Weights and boundaries.
6. Define metrics:
   - Logical error rate, failure probability, threshold crossing, decoding time, memory, and confidence intervals.
7. Run or propose reproducible experiments with seeds, shots, and result schema.
8. Interpret results conservatively. Do not claim threshold or below-threshold behavior without evidence across distances and uncertainty estimates.

## Tools and handoffs

- Use Stim for stabilizer-circuit and detector-error-model work when available.
- Use PyMatching for MWPM-style decoding when applicable.
- Use `engineering-qec-decoders` for decoder implementation, decoder benchmarking, logical-observable prediction, and syndrome-to-logical pipelines.
- Use `verifying-scientific-code` for experiment rigor and reproducibility.
- Use `modeling-quantum-architectures` when QEC must integrate into a control/runtime architecture.
- Use `programming-qpus` when QEC circuits are intended for QPU execution or hardware runtime jobs.

## Output

Use `templates/qec-experiment-report.md` for experiments and `templates/qec-design-review.md` for design reviews.

## QEC simplification gate

Before optimizing a QEC simulator, decoder, or syndrome pipeline, apply `approximating-changes`. Any approximation must preserve detector semantics, logical observables, noise-model assumptions, and reported logical-error evidence.

## QEC readability rules

QEC code must spell out detector, syndrome, logical-observable, noise-model, and decoder roles. Prefer `detector_error_model`, `logical_observable_index`, `syndrome_round_index`, `physical_qubit_index`, `stabilizer_generator`, and `decoder_graph` over short names unless directly matching a paper equation in a tiny scope. Add comments for qubit order, detector indexing, coordinate frames, and approximation/error-budget assumptions.
