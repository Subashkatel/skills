---
name: refactoring-cleanly
description: "Refactors by moving ownership to one clear concept, removing copy-paste and compatibility sediment, and preserving behavior. Use for cleanup or redesign."
---

# Refactoring Cleanly

Replace the old shape with the simpler shape the codebase would want if it were designed today.

## Workflow

1. **Name the duplicated concept.** Examples: state machine, projection, buffer layout, memory allocator, kernel contract, decoder interface, detector model, noise schema, circuit IR, backend target, test oracle, or data contract.
2. **Find every owner and consumer.** Search before building. Wrappers, copied structs, pass-local constants, aliases, and temporary branches are sediment until proven otherwise.
3. **Pick the natural owner.** Choose the module or layer that should own the concept from scratch.
4. **Move consumers to the owner.** Prefer direct consumption of the canonical primitive over adapters. External boundaries may keep adapters; internal dev scaffolding usually should not.
5. **Delete or collapse stale paths in the same pass when safe.** If a bridge is necessary, name it as transitional and give it a removal condition.
6. **Verify through consumers.** Prove the surfaces that used to diverge now exercise the same source of truth.
7. **Record the invariant.** Update the active spec, ADR, or memory note with the concept owner and the reason.

## Rules

- Do not preserve unshipped compatibility by default.
- Do not size the refactor by line count alone. Agentic edits make large ownership moves cheap; judge by end-state clarity and verification cost.
- A checker that re-derives a value the code already computes can drift. Prefer exporting the owner’s computed value into verifiers when the goal is to verify what was actually produced.
- Symmetric placeholders hide orientation, coordinate, and ordering bugs. Re-verify with asymmetric or hostile fixtures before accepting the refactor.
- Reuse is not automatic. Existing code may be wrong or genuinely different. The point is to decide after inspection, not duplicate in ignorance.
- If the refactor widens into unrelated behavior, slice it: land the shared contract first, then port consumers in reviewable passes.

## Domain notes

- GPU: one owner for memory layout, stride, alignment, work partitioning, timing, and device capability decisions.
- Quantum architecture: one owner for circuit IR semantics, backend target constraints, scheduling assumptions, and calibration/timing data.
- QEC: one owner for detector semantics, logical observable definitions, noise model schema, and decoder interpretation.

## Done

The refactor is done when there is one named owner, obsolete paths are removed or have explicit removal conditions, consumers verify the same contract, and the invariant is recorded.

## Readable refactoring rules

When the user asks for a refactor, apply `writing-readable-code` to the target scope as part of the refactor. Rename abbreviated variables, split dense expressions into named intermediate values, remove accidental copy-paste, and keep comments/docstrings short and useful. Do not preserve an unclear name merely because the old code used it unless it is public API or a documented external contract; if a public name must remain, introduce a clearer internal name at the boundary.
