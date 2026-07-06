---
name: tracking-work-state
description: "Tracks active work state in agent-state, progress notes, tests, deviations, benchmarks, QEC experiments, and handoff records."
---

# Tracking Work State

Use this skill to keep long technical work recoverable. State files are the handoff between planning, implementation, verification, and future sessions.

## State files

Use only what the task needs:

- `agent-state.json`: canonical current goal, plan, next action, blockers, evidence, and resume status.
- `progress.md`: concise human-readable status.
- `implementation-notes.md`: decisions, deviations, blockers, and handoff.
- `tests.json`: planned, red, green, skipped, blocked, benchmark, and simulation evidence.
- `performance-log.md`: GPU, runtime, profiler, and benchmark results.
- `qec-experiments.json`: QEC code, decoder, noise, distance, seed, shot, and result grid.
- `architecture-decisions.md`: ADR index and revisit triggers.

## Workflow

1. Initialize or refresh `agent-state.json` for long work.
2. Write the current goal, scope, non-goals, plan, next action, blockers, and verification gates.
3. Log deviations when implementation discovers a new unknown or invalidates the plan.
4. Record evidence, not intentions. For TDD, record red, green, refactor, and final gate results.
5. For GPU work, record hardware/software, command, metric, benchmark statistics, and profiler summary.
6. For QPU work, record backend target, simulator or hardware, transpilation path, shots, bit ordering, and uncertainty.
7. For QEC and decoders, record code, noise model, syndrome schedule, detector mapping, decoder, distance, shots, seeds, logical outcomes, and confidence intervals.
8. Before ending, update state files and state what is verified, unverified, blocked, and next.

## Consistency checks

- If a task is not complete or blocked, `agent-state.json` must name a next action.
- If a test or benchmark is claimed, `tests.json` or the verification report must contain the command and result.
- If a plan changes, `implementation-notes.md` must record the deviation and reason.
- If a commit carries important rationale, add a `git notes --ref=context` note with `recording-repo-memory`.

## Templates

Use files in `templates/` as starting points. Use `maintaining-agent-state` for the active-state schema and validation script.
