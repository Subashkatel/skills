# Architecture checklist

## Core views
- Context and scope.
- Building-block/module structure.
- Runtime/data-flow scenarios.
- Deployment/hardware mapping.
- Crosscutting concepts.
- Architecture decisions.
- Quality requirements.
- Risks and technical debt.

## Scientific-code additions
- Reproducibility and random seeds.
- Numerical precision policy.
- Experiment metadata and provenance.
- Performance benchmark protocol.
- Separation of model, solver/decoder, simulator, analysis, and visualization/reporting.

## GPU additions
- Host/device ownership.
- Transfer boundaries.
- Kernel launch orchestration.
- Vendor portability layer.
- Profiling/benchmark harness.

## Quantum/QEC additions
- Circuit representation and transformations.
- Hardware target and ISA constraints.
- Stabilizer/code representation.
- Noise model and syndrome schedule.
- Decoder integration and latency path.
- Logical observables and result aggregation.
