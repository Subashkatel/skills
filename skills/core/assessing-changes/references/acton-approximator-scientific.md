# Scientific Acton Approximator Reference

The goal is not to make approximate code look exact. The goal is to remove unnecessary work, constrain the problem, or approximate only when the user has an explicit scientific or engineering tolerance.

## Question interpretations

### Can we not do this at all?
Use when a feature, refactor, abstraction, extra kernel, extra simulator path, or additional decoder option is not needed for the current result. In scientific code, deleting work is safest when tests and benchmarks prove unchanged outputs.

### Can we do this only once?
Look for repeated setup, repeated data transfer, repeated circuit compilation, repeated syndrome graph construction, repeated memory allocation, repeated code generation, repeated file parsing, and repeated calibration lookup.

### Can we do this fewer times?
Batch work, fuse loops where it helps locality, cache immutable transforms, reuse decoder graphs, amortize host-device synchronization, or reduce expensive cross-layer calls.

### Can we approximate the result within an explicit error budget?
Require an error budget, an oracle or analytical bound, representative inputs, and a failure policy. In QEC, the approximation must be checked against logical error rates, threshold behavior, detector semantics, or decoder accuracy as appropriate.

### Can we use a small lookup table?
Good for small finite domains, precomputed schedules, bit masks, Pauli multiplication tables, stabilizer indexing, interpolation grids, and quantized constants. Require bounds on table size, cache behavior, and invalidation.

### Can we use a small FIFO?
Good for bounded streams, recent syndromes, rolling windows, event queues, pipeline buffers, and limited backpressure. Require capacity, overflow behavior, and latency implications.

### Can we constrain the problem further?
Prefer explicit constraints over implicit complexity: fixed dtype, fixed layout, bounded distance, fixed lattice geometry, fixed noise channel, static shapes, no dynamic allocation in kernels, or a smaller backend target.

## Red flags

Reject an approximation if it changes physical assumptions, hides numerical drift, invalidates benchmarks, makes a simulator disagree with the paper being reproduced, changes logical observables, breaks determinism required by tests, or makes performance claims without measurement.
