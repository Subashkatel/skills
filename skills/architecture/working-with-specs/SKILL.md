---
name: working-with-specs
description: "Plan, slice, implement, and close a multi-pass spec with verifiable gates. Not for a single small change."
---

# Working With Specs

One lifecycle in four sections: plan the work, slice it into contracts,
implement it pass by pass, and close it into rationale. Enter at the section the
work has reached. A typo, a one-line fix, or a single reversible edit needs none
of this.

## 1. Plan

Create a plan that is useful to review before work starts. Lead with decisions
most likely to change, not mechanical steps.

1. Confirm the goal, scope, and non-goals.
2. Summarize evidence from recon, research, or unknown mapping.
3. Lead with change-sensitive decisions:
   - Architecture: module boundaries, APIs, data models, ownership, dependencies.
   - GPU: data layout, kernel decomposition, precision, benchmark protocol, portability.
   - Quantum and QEC: code, noise, and decoder assumptions, circuit IR, schedules, metrics.
4. Propose the implementation sequence.
5. Define tests, benchmarks, simulations, and review checkpoints.
6. Identify rollback or conservative alternatives.
7. Name only unresolved decisions that require user input. An implementation request already authorizes routine, reversible steps within scope; a plan is not an extra approval gate.

Use `templates/implementation-plan.md` and `references/planning-checklist.md`.
Keep the plan reviewable. Avoid drowning the user in mechanical edits that are
unlikely to change.

### Minimization gate

For an expensive path with a real complexity tradeoff, use `assessing-changes` if needed. Lead the plan with decisions that could shrink or remove the work: not doing it, doing it once, doing it fewer times, using an explicit error-bounded approximation, using a lookup table, using a FIFO, or constraining the problem.

## 2. Slice

Turn a large technical goal into a ladder of small contracts. Each slice should
be independently understandable, implementable, and verifiable before the whole
system exists.

1. **Interrogate before slicing.** Combine `assessing-changes`, `recon-codebases`, and `reviewing-research` as needed. Ask one question at a time only when repo or source inspection cannot answer it.
2. **Name the scientific contract.** State the invariant, API seam, algorithmic property, benchmark target, numerical tolerance, decoder behavior, or hardware constraint the slice proves.
3. **Slice at seams.** Prefer module boundaries, typed interfaces, kernel or pass boundaries, test oracles, experiment harnesses, decoder interfaces, transpiler stages, and data contracts. A slice that needs unrelated systems to be accepted is too broad.
4. **Add a runnable artifact per slice.** Examples: focused unit test, benchmark harness, profiler trace, small kernel, QEC circuit or noise fixture, detector-error-model sample, simulator probe, reproducibility script, or architecture decision record.
5. **Resolve unsupported assumptions.** Add a research or replication spike only where existing evidence does not establish the needed contract.
6. **Draft more than once for high-risk work.** For major redesigns, ask independent agents or passes to propose slice graphs from the same brief, then synthesize. Agreement means stable ground; disagreement marks where to inspect harder.
7. **Run the minimization gate.** Use `assessing-changes` and `refactoring-cleanly` to remove fake flexibility, duplicated concepts, dev-only compatibility layers, or unneeded abstractions before freezing the spec.
8. **Materialize the spec.** Reuse the repository convention. If none exists, use `specs/<feature>/README.md` plus `specs/<feature>/slices/<nn>-<name>.md`. Keep evidence, fixtures, benchmark baselines, and references under the spec folder when they define acceptance. Use `templates/spec-readme.md` and `references/slice-template.md`.
9. **Write the handoff.** The README needs a current pickup point, dependency graph, global TODOs, verification gates, and a direct "Next Agent Prompt" a fresh agent can follow without chat history.

### Slice contract

Each slice file answers:

- What contract does this unlock?
- What is the seam and who owns it?
- What must stay unchanged?
- What evidence proves correctness?
- What benchmark, tolerance, stochastic confidence, or QEC logical-error metric applies?
- What human decision could change this slice?
- What later slice removes any temporary seam?

### Scientific slicing rules

- For GPU work, never treat speedup as done without a correctness oracle, baseline, profiler evidence, and repeatable measurement environment.
- For numerical work, state exact equality, tolerance-bounded agreement, or statistical confidence explicitly.
- For QEC work, slice detector semantics, logical observables, noise assumptions, decoder behavior, and threshold or logical-error evidence separately when any one could fail independently.
- For architecture work, slice concept ownership first, then consumers. Avoid building adapters around a duplicated concept.
- Reslicing is progress. When implementation exposes hidden variables, update the spec before widening the patch.

The spec is sliced well when a fresh agent can start with the README, pick the
same next slice, know the contracts and gates, and verify each slice without
relying on the original conversation.

## 3. Implement

Build the active spec to completion one reviewable pass at a time. The spec is
the source of truth, but the code is allowed to teach you that the spec needs to
be resliced.

1. **Load the map.** Read the repo instructions, spec README, active slice, evidence ledger, and current handoff. Load a named domain skill only when the active slice needs its guidance.
2. **Reconcile with reality.** Inspect current code and tests before editing. If the slice preserves a duplicated owner, dev-only shim, obsolete path, or weak wrapper, update the plan toward the cleaner architecture.
3. **Pick the next pass.** A pass is usually one slice, one vertical checkpoint, one benchmark gate, one QEC experiment, or one architecture correction. Delegate independent passes only under the session's agent policy and when their files and seams do not collide.
4. **Implement narrowly.** Keep the diff scoped to the contract. No drive-by cleanup, feature creep, or speculative compatibility layers.
5. **Verify the contract.** Run the focused tests, numerical checks, profiler runs, QEC simulations, or architecture review named by the slice. Never weaken a gate to claim progress.
6. **Clean the pass.** Review `git status` and `git diff` path by path. Remove only task-created scratch outputs that are no longer needed; preserve user files and useful evidence.
7. **Run quality gates.** Use `refactoring-cleanly`, `writing-tests`, and `verifying-scientific-code` where they apply. Fix accepted findings in the same pass.
8. **Record state.** Update the spec README handoff, slice status, evidence ledger, and the commit notes described in `keeping-work-records` when the pass changes rationale, assumptions, or next steps.
9. **Commit clean checkpoints when working in a repo.** A green commit is a checkpoint, not a reason to hand back if slices remain. Commit locally without attribution trailers; never push or merge without explicit user approval.
10. **Continue or stop honestly.** Continue while there is non-blocked work. Stop only for user-only decisions, irreducible red gates, destructive actions, missing credentials or assets the user must supply, or explicit user interruption.

Record each pass with `templates/pass-report.md` when a written record is useful.

### Maintenance checkpoints

Run a maintenance checkpoint after red gates, every few slice commits, after compaction or resume, when the handoff contradicts the graph, or when the prompt or spec becomes hard to scan. A checkpoint should shorten handoff, correct statuses, delete stale TODOs, reslice overloaded work, and collapse scaffolding that no longer owns a contract.

### Scientific rules for a pass

- GPU passes must include correctness and performance evidence when they claim speed or kernel correctness.
- QEC passes must preserve detector semantics, logical observables, noise assumptions, and decoder interpretation unless the spec explicitly changes them.
- Numerical passes must state whether evidence is deterministic, tolerance-bounded, or statistical.
- Architecture passes must leave one owner per concept.
- A pass is not done because an agent says it is done; it is done when diff, tests, evidence, and handoff agree.

### Readability gate

Every implementation pass must run a readability review before final verification. Use `writing-readable-code` to check changed code for abbreviations, dense expression chains, vague names, copy-paste blocks, over-abstraction, missing domain comments, and comments that restate obvious syntax. A slice is not complete just because tests pass; it must also be readable in the touched scope.

The implementation is done when every slice and global TODO is closed, required
gates are green or honestly documented as accepted limitations, evidence is
recorded, and the handoff has no required work remaining.

## 4. Close

A live spec is a build plan. A closed spec is a rationale record. Closing
preserves why the shipped system has this shape and points readers to the code
for how it works.

1. **Confirm shipped state.** Verify that implementation landed, required tests, profilers, simulations, and reviews are complete, and unresolved slices are either done or explicitly out of scope.
2. **Diff plan against reality.** Read the spec and the code that shipped. Record divergences: dropped slices, renamed seams, changed assumptions, failed approaches, altered metrics, and new invariants.
3. **Archive by convention.** Follow the repository's existing archive location; use `specs/done/` only if appropriate, and preserve working links.
4. **Rewrite the README.** Replace build order with present-tense rationale: purpose, constraints, core decisions, invariants, tradeoffs, dead ends, and pointers into code, tests, and benchmarks. Use `templates/closed-spec-readme.md`.
5. **Preserve evidence.** Keep benchmark baselines, QEC experiment records, profiler outputs, reference circuits, figures, and other artifacts that define why the result was accepted.
6. **Cut sediment.** Remove stale next steps, slice-by-slice instructions, temporary prompts, and mechanics that the code already states better.
7. **Audit claims.** Check each claim against code, tests, benchmarks, or recorded evidence. Fix unsupported or stale statements before calling the spec closed.
8. **Link durable lessons.** Add a separate memory note only for reusable information not already captured by the closed spec.

### A closed spec contains

- What shipped and what problem it solves.
- Why the design is shaped this way.
- Invariants the implementation must keep honoring.
- Greppable pointers to modules, tests, benchmarks, experiments, and papers.
- Dead ends and why they failed.
- Evidence provenance: what data, circuits, seeds, baselines, hardware, or profilers supported acceptance.

### Smell test

- If a paragraph restates what a function does, replace it with a pointer.
- If it says "will", "next", or "slice N", it is still a plan.
- If a future expert would re-run a failed approach without this note, record the dead end.
- If a performance or logical-error claim lacks environment, command, seed, tolerance, or confidence context, it is not durable.

The spec is closed when it is archived using the repository convention, reads as
rationale and invariants, names the code and evidence that support it, and has
no stale build-plan instructions.
