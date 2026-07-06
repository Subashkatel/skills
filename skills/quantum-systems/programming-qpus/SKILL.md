---
name: programming-qpus
description: "Guides QPU programming and hybrid execution with Qiskit, Cirq, CUDA-Q, OpenQASM, QIR, backend targets, transpilation, shots, and runtime jobs."
---

# Programming QPUs

## Purpose

Help the agent write, review, or refactor QPU-facing code without confusing abstract algorithms, simulator behavior, and hardware execution. The goal is clear, verified quantum programs with explicit qubit order, measurement semantics, backend target assumptions, and result interpretation.

Use this skill for QPU programming, quantum SDK code, circuit generation, transpilation, quantum runtime jobs, OpenQASM/QIR handling, hybrid quantum-classical loops, and hardware-aware execution paths. For fault-tolerant or syndrome-extraction work, pair this with `engineering-qec` and `engineering-qec-decoders`.

## QPU programming workflow

1. **Identify the execution target.** State whether the code targets an exact simulator, noisy simulator, local sampler, remote QPU, quantum runtime service, or compiler/intermediate representation.
2. **Read local examples first.** Inspect repository code, build scripts, notebooks, and tests before choosing a style or SDK pattern.
3. **Define the program contract.** Record qubit register order, classical register order, parameters, measurement map, shot count, seeds if available, expected result schema, and whether mid-circuit measurements or resets are allowed.
4. **Check backend constraints.** Capture native gate set, connectivity, measurement/reset behavior, timing requirements, control-flow support, and whether circuits must be ISA-compliant after transpilation.
5. **Separate logical intent from hardware lowering.** Keep algorithm construction, transpilation/target selection, job submission, and result post-processing in separate named steps or functions unless the task is tiny.
6. **Verify with the cheapest trustworthy oracle.** Use known analytical results, exact statevector/unitary checks on small circuits, simulator snapshots, reference circuits, or cross-SDK comparison before relying on hardware samples.
7. **Preserve statistical meaning.** When using shots, report counts, confidence intervals or uncertainty where relevant, seed policy, and whether observed differences are statistically meaningful.
8. **Document hardware assumptions.** Do not claim a result is hardware-valid unless the job, backend, transpilation settings, and measurement interpretation support that claim.

## Hybrid and runtime rules

- Keep quantum program construction deterministic when possible; isolate stochastic sampling and hardware queue effects.
- Name job identifiers, backend names, shot counts, and result fields explicitly.
- Do not silently change qubit endianness, bitstring ordering, classical register layout, or measurement basis.
- For variational loops, separate parameter binding, execution, objective computation, optimizer state, and stopping criteria.
- For runtime services, distinguish local validation from submitted jobs and returned hardware results.
- For QEC circuits, do not treat raw measurement strings, detector events, syndromes, and logical-observable flips as interchangeable.

## QPU code readability rules

Use `writing-readable-code` with this skill. Prefer names such as `logical_qubit_register`, `physical_qubit_index`, `measurement_bit_index`, `backend_target`, `transpiled_circuit`, `runtime_job_identifier`, `shot_count`, and `measurement_counts`. Avoid `qc`, `qr`, `cr`, `circ`, `res`, and `job` outside very small examples or direct library tutorial snippets. Use short inline comments for endianness, bit order, coordinate frames, timing assumptions, and hardware limitations.

## Handoffs

- Use `modeling-quantum-architectures` for layer boundaries, compiler/runtime architecture, control timing, and QEC integration.
- Use `engineering-qec` when the QPU program performs syndrome extraction, logical operations, or fault-tolerant schedules.
- Use `engineering-qec-decoders` when measurement output feeds a decoder or detector error model.
- Use `verifying-scientific-code` for simulator/hardware evidence, numerical tolerances, and statistical claims.
- Use `programming-gpus` when the QPU workflow includes GPU-accelerated simulation or decoder kernels.

## Output

For nontrivial work, produce a short QPU program review with:

- Target stack and backend assumptions.
- Program contract and qubit/bit ordering.
- Transpilation or lowering path.
- Verification evidence.
- Remaining hardware or statistical uncertainty.
