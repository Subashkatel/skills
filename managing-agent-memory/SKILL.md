---
name: managing-agent-memory
description: "Creates and curates durable agent memory: reusable lessons, repo notes, state links, evidence, stale-memory cleanup, and session mining."
---

# Managing Agent Memory

Use this skill for durable memory that should improve future sessions. Do not use it for current status; use `maintaining-agent-state` and `tracking-work-state` for active work.

## Memory layers

- `agent-state.json`: current truth for the active task.
- `progress.md`: human-readable current progress.
- `implementation-notes.md`: decisions, deviations, blockers, and handoff.
- `tests.json`: test and TDD evidence.
- `performance-log.md`: GPU, runtime, and benchmark evidence.
- `qec-experiments.json`: QEC, decoder, noise, seed, and simulation evidence.
- `git notes --ref=context`: commit-bound rationale and evidence.
- `agent-memory/lessons/`: reusable lessons that survive across sessions.

## Create or update durable memory when

The lesson is reusable, non-obvious, evidence-backed, and likely to prevent a future mistake. Good lessons include user preferences, project conventions, detector ordering rules, decoder weight conventions, hardware constraints, benchmark findings, architecture invariants, and confirmed debugging approaches.

Do not save secrets, raw chat summaries, vague todos, restatements of diffs, guesses, stale speculation, or private hidden-reasoning text.

## Workflow

1. Decide whether this is active state, commit memory, or durable lesson memory.
2. Search existing lessons before creating a new one.
3. Verify the lesson against files, commands, commits, test output, benchmarks, simulations, or source documents.
4. Write one lesson per file using `templates/lesson.md`.
5. Add revalidation guidance: when to trust it, when to re-check it, and what would invalidate it.
6. Update or delete stale lessons instead of duplicating them.
7. Mention the memory file or git note only when it affected the decision.

## Session mining

When the user asks to improve rules from past failures, use `running-task-harnesses`: mine sessions or review comments, cluster recurring corrections, adversarially verify whether each rule would have prevented a real mistake, then distill survivors into `AGENTS.md`, `CLAUDE.md`, or lessons.

## Done

Memory is done when a future agent can load the relevant note, understand the correction, see evidence, know the revalidation condition, and avoid duplicating or trusting stale information.
