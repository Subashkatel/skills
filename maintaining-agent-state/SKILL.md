---
name: maintaining-agent-state
description: "Maintains active execution state: current goal, plan, todo list, blockers, evidence, tests, next action, and resume status for long coding work."
---

# Maintaining Agent State

Use this skill when work spans many steps, tools, agents, context compaction, or sessions. Active state answers: what is the goal, what is happening now, what remains, what is blocked, and what evidence supports progress claims.

## Files

Use `agent-state.json` as the canonical current state for long tasks. Use `progress.md` for human-readable notes, `implementation-notes.md` for decisions and deviations, `tests.json` for test evidence, and domain logs for GPU, QPU, QEC, decoder, or benchmark evidence.

## Startup and resume

1. Read `AGENTS.md` or `CLAUDE.md`, then relevant local state files.
2. Check `git status`, recent commits, and `git log --notes=context -10` when available.
3. Load only relevant lessons from `agent-memory/lessons/`.
4. Reconcile state against the real repository. If memory says one thing and files say another, trust the files and update memory.
5. Before editing, write or refresh `agent-state.json` with the current goal, scope, plan, next action, blockers, tests, and evidence ledger.

## Update cadence

Update active state at task start, after any plan change, after each red/green/refactor cycle, after each implemented slice, after a failed command that changes direction, before context compaction, and before the final response.

## State rules

- Every open task needs an owner, next action, and verification gate.
- Every done claim needs an evidence pointer: command, file, commit, profiler output, simulation result, or cited source.
- Keep one current plan. Move stale play-by-play into notes or delete it.
- Record assumptions and unknowns separately from verified facts.
- Do not store secrets, private hidden-reasoning text, vague reminders, or raw chat transcripts.
- If the task is complete, mark remaining work empty and record final evidence.

## Fresh-agent test

State is good when a fresh agent can read `AGENTS.md`, `agent-state.json`, `tests.json`, the relevant spec, and git notes, then choose the same next action without conversation history.

## Templates and checks

Start from `templates/agent-state.json`. Run `scripts/check_agent_state.py` with `agent-state.json` when available before handoff or after compaction.
