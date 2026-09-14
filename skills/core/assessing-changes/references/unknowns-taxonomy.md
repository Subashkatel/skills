# Unknowns taxonomy

## Known knowns
Facts explicitly provided by the user, repository, paper, logs, profiler output, or tool results.

## Known unknowns
Questions already visible to the user, such as “which decoder should we use?” or “is this kernel memory-bound?”

## Hidden knowns
Things the user may know but forgot to state: target GPU, tolerance, problem size, preferred backend, expected qubit modality, or deployment constraints.

## Unknown unknowns
Blindspots the user may not know to ask about. Examples: floating-point non-associativity in GPU reductions, decoder latency in a fault-tolerant architecture, syndrome schedule effects, measurement error assumptions, or architecture decisions hidden in existing tests.
