# Quantum architecture map

## Physical/device layer
Qubit modality, topology/connectivity, gate set, durations, error rates, measurement/reset behavior, calibration constraints.

## Control and timing layer
Pulse/control model, real-time classical feedback, timing granularity, acquisition alignment, latency constraints.

## Circuit/IR layer
Circuit representation, OpenQASM/QIR/stim/Qiskit/Cirq formats, supported operations, timing/pulse specificity, classical control.

## Compilation/transpilation layer
Layout, routing, basis translation, optimization, scheduling, target backend constraints.

## QEC/logical layer
Code family, distance, stabilizers/gauge checks, syndrome schedule, logical operators, logical gates, magic-state or lattice-surgery assumptions.

## Decoder/runtime layer
Syndrome ingestion, detector error model, decoder algorithm, latency, feedback action, result logging.

## Application/resource layer
Algorithm, logical resources, logical error budget, runtime budget, hardware footprint, verification plan.
