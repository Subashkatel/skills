---
name: engineering-qec-decoders
description: "Designs, implements, reviews, and benchmarks QEC decoders: MWPM, union-find, belief propagation, neural/custom decoders, detector events, and logical predictions."
---

# Engineering QEC Decoders

## Purpose

Help the agent work on the decoder layer of quantum error correction with explicit semantics and evidence. The decoder contract is not just an algorithm name; it is the mapping from detector events or syndromes to corrections, logical-observable predictions, confidence, and latency under a stated noise model.

Use this skill when implementing, refactoring, optimizing, benchmarking, or reviewing a QEC decoder, decoder graph, detector error model, matching setup, union-find or belief-propagation path, neural decoder, threshold experiment, or QEC runtime feedback loop.

## Decoder workflow

1. **Define the decoder contract.** State the input format, output format, code family, distance, rounds, boundary conventions, logical observables, and whether output is a correction, a residual error, or a logical prediction.
2. **Identify the model source.** Use a parity-check matrix, Tanner graph, stabilizer table, circuit sampler, Stim detector error model, Qiskit QEC object, or paper definition. Do not mix these without an explicit conversion step.
3. **Check semantics before optimizing.** Verify syndrome parity, detector indices, time offsets, boundary nodes, edge weights, erasure handling, and logical-observable indices.
4. **Choose the decoder honestly.** Record whether it is MWPM, union-find, belief propagation, ordered-statistics postprocessing, tensor/network, neural, exact small-code, or custom. State the assumptions that make it valid.
5. **Build a correctness oracle.** For small cases, compare with exhaustive decoding, analytical examples, known reference data, Stim/PyMatching behavior, or a slower clear implementation.
6. **Test logical outcomes.** Check that predicted logical observables match the actual logical frame changes, not only that the syndrome is matched.
7. **Benchmark with reproducibility.** Record hardware, software versions, seed policy, batch size, shots, distances, rounds, noise model, wall time, memory, and latency distribution.
8. **Interpret results conservatively.** Do not claim a threshold, decoder superiority, or production readiness without multi-distance evidence and uncertainty estimates.

## Decoder implementation rules

- Keep detector generation, graph construction, weight assignment, decoding, and logical-observable evaluation as separate named stages.
- Prefer a clear reference decoder or small-code oracle before an optimized decoder.
- If a decoder is approximate, learned, heuristic, or GPU-accelerated, state the failure modes and validation budget.
- For matching, verify that the detector error model is graphlike enough for the chosen matching formulation.
- For batch decoding, test that batched and single-shot paths agree on a fixed sample set.
- For runtime feedback, separate correctness latency from queueing, data transfer, and post-processing latency.

## QEC decoder readability rules

Use `writing-readable-code` with this skill. Prefer names such as `detector_event_matrix`, `syndrome_bit_index`, `decoder_graph`, `edge_error_probability`, `edge_weight`, `boundary_detector_index`, `predicted_logical_observables`, `actual_logical_observables`, `logical_failure_count`, `decoder_latency_seconds`, and `shot_count`. Avoid names like `s`, `e`, `p`, `w`, `m`, `pred`, and `obs` except in tiny scopes directly matching a displayed equation.

## Handoffs

- Use `engineering-qec` for code definitions, stabilizers, syndrome extraction schedules, and logical operators.
- Use `programming-qpus` when decoder inputs come from QPU measurement results or runtime jobs.
- Use `programming-gpus` when implementing decoder kernels or accelerating batch decoding.
- Use `verifying-scientific-code` for experiment rigor, confidence intervals, and reproducibility.
- Use `designing-classical-architectures` when the decoder must fit into a larger service, simulator, or runtime architecture.

## Output

For nontrivial decoder work, produce a decoder design or benchmark report with:

- Contract and conventions.
- Model source and conversions.
- Decoder choice and assumptions.
- Correctness oracle and tests.
- Performance evidence.
- Risks, approximations, and open hypotheses.
