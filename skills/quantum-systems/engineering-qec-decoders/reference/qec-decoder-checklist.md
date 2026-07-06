# QEC Decoder Checklist

## Contract

- Input type: raw measurements, detector events, syndrome bits, erasures, soft information, or detector error model samples.
- Output type: correction, residual error estimate, logical prediction, confidence, or runtime feedback decision.
- Code family, distance, rounds, boundaries, and logical observables.
- Bit ordering and detector ordering.

## Semantic checks

- Stabilizer or parity-check convention.
- Detector index and time-round convention.
- Boundary and virtual node convention.
- Logical observable index convention.
- Weight calculation from error probabilities.
- Graphlike assumption for MWPM.
- Batch path equals single-shot path on fixed samples.

## Evidence

- Small-code exhaustive oracle or reference decoder.
- Stim or PyMatching comparison when applicable.
- Logical-observable correctness tests.
- Performance benchmark with batch size and hardware.
- Statistical confidence for logical failure estimates.

## Common failure modes

- Matching a syndrome but predicting the wrong logical observable.
- Off-by-one detector time indexing.
- Reversed bitstrings from measurement output.
- Fusing boundaries incorrectly.
- Using probability weights with the wrong log-odds convention.
- Benchmarking Python overhead instead of decoder work.
- Treating a neural or heuristic decoder as exact.
