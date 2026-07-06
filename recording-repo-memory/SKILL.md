---
name: recording-repo-memory
description: "Records durable repo memory with session IDs, git notes, progress files, tests, experiments, benchmarks, and handoff state for long coding sessions."
---

## Purpose

Use this skill to make long coding sessions resumable across Claude, Codex, context compaction, and future commits. Store durable context in the repository rather than relying only on chat history. Pair with `managing-agent-memory` when the lesson should survive beyond one commit.

## Startup protocol

Run once per session and again after automatic compaction when the repository is available:

1. Resolve a session ID. Prefer `CODEX_THREAD_ID` for Codex. Prefer `CLAUDE_SESSION_ID` for Claude Code when available. Otherwise use the helper script or create a stable temporary ID.
2. Review recent history with git notes: `git log --notes=context -10 --format="=== %h %s ===%n%N"`.
3. Review local state files when present: `progress.md`, `implementation-notes.md`, `tests.json`, `qec-experiments.json`, `performance-log.md`, and architecture decision records.
4. Continue from evidence. Do not assume chat history is complete after compaction.

## What to write in git notes

Add or append `git notes --ref=context` only for nontrivial commits or handoff points. Notes should capture:

- why the change was made;
- alternatives considered and rejected;
- debugging or profiler evidence;
- tests, simulations, or benchmark evidence;
- open hypotheses or constraints future agents must preserve;
- any deviation from the original plan.

Do not restate the diff, paste secrets, include private hidden-reasoning transcript, or write context-free todo lists. If the note becomes a reusable lesson, create or update one scoped lesson file instead of duplicating it across commits.

## Prefix format

Prefix each note with one of:

- `[CODEX:<session-id>]` for Codex sessions;
- `[CLAUDE:<session-id>]` for Claude Code sessions;
- `[AGENT:<session-id>]` when the tool cannot identify the agent.

## Safe command helpers

Use the scripts in `scripts/` when available:

- `session_id.sh` resolves and caches the session ID.
- `recent_context.sh` prints the last ten commits plus `git notes --ref=context`.
- `add_context_note.sh HEAD "message"` appends a context note to a commit.

Only append notes by default. Ask before rewriting, deleting, force-pushing, rebasing published commits, or changing shared repository state.

## Handoff output

When ending a long session, report:

- current commit or working tree state;
- verified tests, benchmarks, and simulations;
- unresolved hypotheses;
- where the durable notes were written.

## Reusable lessons

For durable lessons that apply across many sessions, use `managing-agent-memory`: one lesson per file, evidence included, stale lessons updated or removed.
