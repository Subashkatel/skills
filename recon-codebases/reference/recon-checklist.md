# Recon checklist

## General
- Repository root and package boundaries.
- Build/test commands.
- Entry points and public APIs.
- Configuration and environment assumptions.
- Tests and fixtures.
- Existing documentation.

## Architecture
- Domain model and ownership boundaries.
- Runtime paths and failure paths.
- Deployment and persistence assumptions.
- ADRs or design notes.

## GPU
- Kernels and launch sites.
- Host/device transfer paths.
- Memory layout and strides.
- Precision and tolerances.
- Benchmark/profiling scripts.

## Quantum/QEC
- Circuit/code construction.
- Stabilizers/gauge operators.
- Noise model.
- Decoder and detector error model.
- Logical observables.
- Experiment seeds, shots, and aggregation.
