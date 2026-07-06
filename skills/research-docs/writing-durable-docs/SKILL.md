---
name: writing-durable-docs
description: "Writes durable docs that explain why systems exist, invariants, design decisions, and where to look, without mirroring code that will rot."
---

# Writing Durable Docs

A doc should hold what code cannot: why a thing exists, what must stay true, and where to look. The code, tests, and git history hold changing inventories.

## Workflow

1. **Ask the governing question.** Could the reader get this faster and more reliably by reading code, tests, schema, or command help? If yes, point there instead of copying it.
2. **Keep the durable layer.** Preserve purpose, principles, invariants, non-obvious constraints, dead ends, platform quirks, and pointers to source-of-truth files.
3. **Shed rotting detail.** Remove file inventories, command matrices, helper rosters, exact constants, line numbers, changelog narration, and duplicated explanations.
4. **Create one home per fact.** Pick the canonical doc or code owner and make other docs link to it.
5. **Use examples as touchstones.** One concrete example can ground a principle; exhaustive examples usually rot.
6. **Read as a stranger.** After editing, a reader with no chat history should understand why the system is shaped this way and where to verify mechanics.

## Scientific documentation rules

- For GPU docs, record device assumptions, benchmarking methodology, invariants, and where performance evidence lives. Do not copy current profiler tables unless the doc is an evidence report.
- For quantum architecture docs, record layer boundaries, target constraints, timing/control assumptions, and where compiler/runtime contracts live.
- For QEC docs, record code family, detector/logical semantics, noise assumptions, decoder choices, and experiment provenance. Do not duplicate simulator internals.
- For architecture docs, emphasize ownership and tradeoffs, not file-by-file implementation narration.

## Done

The doc is done when every surviving line is a why, invariant, caution, or pointer; repeated facts have one home; and no sentence races the code for source-of-truth status.
