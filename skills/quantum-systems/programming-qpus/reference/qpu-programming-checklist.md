# QPU Programming Checklist

## Contract

- Target stack and version.
- Simulator or hardware backend.
- Qubit order and classical bit order.
- Measurement basis and result schema.
- Shot count, seed policy, and run identifiers.
- Whether mid-circuit measurement, reset, feedback, pulses, or timing are used.

## Backend target

- Native gates or instruction set.
- Coupling graph or topology.
- Gate durations and error rates if available.
- Measurement and reset behavior.
- Classical feedback support and latency assumptions.
- Transpiler optimization level or pass manager.

## Verification

- Analytical small-case check.
- Simulator/reference comparison.
- Hardware-job evidence if claimed.
- Statistical uncertainty for sampled results.
- Reproducible command or notebook cell.

## Common failure modes

- Reversed bitstrings or endianness.
- Using simulator-only operations on hardware paths.
- Treating transpiled and untranspiled circuits as semantically identical without checks.
- Ignoring backend unsupported operations.
- Mixing raw measurement bits with detector events or logical observables.
- Reporting noisy hardware counts as exact probabilities.
