---
name: implementing-specs
description: "Implements an existing scientific spec slice by slice with verification, cleanup, state updates, and handoff notes. Use for multi-pass specs under specs/."
---

# Implementing Specs

Build the active spec to completion one reviewable pass at a time. The spec is the source of truth, but the code is allowed to teach you that the spec needs to be resliced.

## Workflow

1. **Load the map.** Read the repo instructions, spec README, active slice, evidence ledger, and current handoff. Load domain skills named by the spec.
2. **Reconcile with reality.** Inspect current code and tests before editing. If the slice preserves a duplicated owner, dev-only shim, obsolete path, or weak wrapper, update the plan toward the cleaner architecture.
3. **Pick the next pass.** A pass is usually one slice, one vertical checkpoint, one benchmark gate, one QEC experiment, or one architecture correction. Independent passes may run in parallel through peer agents or worktrees when their files and seams do not collide.
4. **Implement narrowly.** Keep the diff scoped to the contract. No drive-by cleanup, feature creep, or speculative compatibility layers.
5. **Verify the contract.** Run the focused tests, numerical checks, profiler runs, QEC simulations, or architecture review named by the slice. Never weaken a gate to claim progress.
6. **Clean the pass.** Review `git status` and `git diff` path by path. Delete scratch probes, stray outputs, debug scripts, and logs unless they are promoted into spec evidence or real tests.
7. **Run quality gates.** Use `refactoring-cleanly`, `writing-behavior-tests`, and `verifying-scientific-code` where they apply. Fix accepted findings in the same pass.
8. **Record state.** Update the spec README handoff, slice status, evidence ledger, and `recording-repo-memory` notes when the pass changes rationale, assumptions, or next steps.
9. **Commit clean checkpoints when working in a repo.** A green commit is a checkpoint, not a reason to hand back if slices remain.
10. **Continue or stop honestly.** Continue while there is non-blocked work. Stop only for user-only decisions, irreducible red gates, destructive actions, missing credentials/assets the user must supply, or explicit user interruption.

## Maintenance checkpoints

Run a maintenance checkpoint after red gates, every few slice commits, after compaction/resume, when the handoff contradicts the graph, or when the prompt/spec becomes hard to scan. A checkpoint should shorten handoff, correct statuses, delete stale TODOs, reslice overloaded work, and collapse scaffolding that no longer owns a contract.

## Scientific rules

- GPU passes must include correctness and performance evidence when they claim speed or kernel correctness.
- QEC passes must preserve detector semantics, logical observables, noise assumptions, and decoder interpretation unless the spec explicitly changes them.
- Numerical passes must state whether evidence is deterministic, tolerance-bounded, or statistical.
- Architecture passes must leave one owner per concept.
- A pass is not done because an agent says it is done; it is done when diff, tests, evidence, and handoff agree.

## Done

The implementation is done when every slice and global TODO is closed, required gates are green or honestly documented as accepted limitations, evidence is recorded, handoff has no remaining pickup point, and `closing-specs` has archived the spec into durable rationale.

## Readability gate

Every implementation pass must run a readability review before final verification. Use `writing-readable-code` to check changed code for abbreviations, dense expression chains, vague names, copy-paste blocks, over-abstraction, missing domain comments, and comments that restate obvious syntax. A slice is not complete just because tests pass; it must also be readable in the touched scope.
