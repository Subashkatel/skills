---
name: maintaining-agent-state
description: "Initialize or reconcile a resumable task record for long work, handoff, or context recovery."
---

# Maintaining Agent State

Use this skill when work spans many steps, tools, agents, context compaction, or sessions. Active state answers: what is the goal, what is happening now, what remains, what is blocked, and what evidence supports progress claims.

## Files

Reuse one existing task record, such as a spec handoff or `agent-state.json`. Create companion logs only when they hold evidence the main record cannot usefully contain. A request limited to code or skills does not authorize unrelated state files; use permitted temporary storage when needed.

When creating or replacing `agent-state.json`, follow `templates/agent-state.json` exactly and run `scripts/check_agent_state.py`. Plan statuses are `pending`, `in-progress`, `blocked`, `done`, or `skipped`; the checker requires `current_status`, `current_action`, and each step's `description`.

## Startup and resume

1. Read `AGENTS.md` or `CLAUDE.md`, then relevant local state files.
2. Check `git status`, recent commits, and `git log --notes=context -10` when available.
3. Load only relevant lessons from `agent-memory/lessons/`.
4. Reconcile state against the real repository. If memory says one thing and files say another, trust the files and update memory.
5. Reconcile the current record with the goal, scope, next action, blockers, and evidence; do not initialize a second competing plan.

## Update cadence

Update at meaningful milestones, changes of direction, and handoff or compaction boundaries. Avoid rewriting state after every routine command.

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
