---
name: keeping-work-records
description: "Keep a resumable task record, repository handoff notes, and durable lessons for long work. Not for a one-step task."
---

# Keeping Work Records

Three kinds of record, one skill. The task record holds what is true right now.
The repository handoff binds rationale to commits. Durable lessons survive the
task entirely. Decide which one a piece of information belongs to before writing
it anywhere.

## Files

Use only what the task needs:

- `agent-state.json`: canonical current goal, plan, next action, blockers, evidence, and resume status.
- `progress.md`: concise human-readable status.
- `implementation-notes.md`: decisions, deviations, blockers, and handoff.
- `tests.json`: planned, red, green, skipped, blocked, benchmark, and simulation evidence.
- `performance-log.md`: GPU, runtime, profiler, and benchmark results.
- `qec-experiments.json`: QEC code, decoder, noise, distance, seed, shot, and result grid.
- `architecture-decisions.md`: ADR index and revisit triggers.
- `git notes --ref=context`: commit-bound rationale and evidence.
- `agent-memory/lessons/`: reusable lessons that survive across sessions.

Reuse one existing task record, such as a spec handoff or `agent-state.json`.
Create companion logs only when they hold evidence the main record cannot
usefully contain. A request limited to code or skills does not authorize
unrelated state files; use permitted temporary storage when needed. Templates
for each file live in `templates/`; `references/state-management-policy.md` and
`references/memory-policy.md` hold the policies in detail.

## 1. The task record: start, update, resume

Use this section when work spans many steps, tools, agents, context compaction,
or sessions. Active state answers: what is the goal, what is happening now, what
remains, what is blocked, and what evidence supports progress claims.

### Startup and resume

1. Read `AGENTS.md` or `CLAUDE.md`, then relevant local state files.
2. Check `git status`, recent commits, and `git log --notes=context -10` when available.
3. Load only relevant lessons from `agent-memory/lessons/`.
4. Reconcile state against the real repository. If memory says one thing and files say another, trust the files and update memory.
5. Reconcile the current record with the goal, scope, next action, blockers, and evidence; do not initialize a second competing plan.

### Schema and check

When creating or replacing `agent-state.json`, follow `templates/agent-state.json` exactly and run `scripts/check_agent_state.py`. Plan statuses are `pending`, `in-progress`, `blocked`, `done`, or `skipped`; the checker requires `current_status`, `current_action`, and each step's `description`. An existing spec handoff does not need conversion.

### Update cadence and content

Update at meaningful milestones, changes of direction, and handoff or compaction boundaries. Avoid rewriting state after every routine command.

1. Write the current goal, scope, non-goals, plan, next action, blockers, and verification gates.
2. Log deviations when implementation discovers a new unknown or invalidates the plan.
3. Record evidence, not intentions. For a test-first loop, record red, green, refactor, and final gate results.
4. For GPU work, record hardware and software, command, metric, benchmark statistics, and profiler summary.
5. For QPU work, record backend target, simulator or hardware, transpilation path, shots, bit ordering, and uncertainty.
6. For QEC and decoders, record code, noise model, syndrome schedule, detector mapping, decoder, distance, shots, seeds, logical outcomes, and confidence intervals.
7. Before ending, update state files and state what is verified, unverified, blocked, and next.

### State rules

- Every open task needs an owner, next action, and verification gate.
- Every done claim needs an evidence pointer: command, file, commit, profiler output, simulation result, or cited source.
- Keep one current plan. Move stale play-by-play into notes or delete it.
- Record assumptions and unknowns separately from verified facts.
- Do not store secrets, private hidden-reasoning text, vague reminders, or raw chat transcripts.
- If the task is complete, mark remaining work empty and record final evidence.

### Consistency checks

- If a task is not complete or blocked, the current task record must name a next action.
- If a test or benchmark is claimed, `tests.json` or the verification report must contain the command and result.
- If a plan changes, the current task record must record the material deviation and reason.
- If a commit carries important rationale, retain it in the existing record or write a commit note as described below.

### Fresh-agent test

State is good when a fresh agent can read the current task record and its relevant evidence links, then choose the same next action without conversation history.

## 2. The repository handoff and git notes

Use this section to make long coding sessions resumable across Claude, Codex,
context compaction, and future commits. Store durable context in the repository
rather than relying only on chat history. `references/git-notes-memory.md` holds
the detail.

### Session identity

1. Resolve a session ID. Prefer `CODEX_THREAD_ID` for Codex. Prefer `CLAUDE_SESSION_ID` for Claude Code when available. If neither exists, omit the identifier unless the repository requires one; no startup file is needed just to obtain it.
2. Review recent history with git notes: `git log --notes=context -10 --format="=== %h %s ===%n%N"`.
3. Review local state files when present: `progress.md`, `implementation-notes.md`, `tests.json`, `qec-experiments.json`, `performance-log.md`, and architecture decision records.
4. Continue from evidence. Do not assume chat history is complete after compaction.

Prefix each note with one of:

- `[CODEX:<session-id>]` for Codex sessions;
- `[CLAUDE:<session-id>]` for Claude Code sessions;
- `[AGENT:<session-id>]` when the tool cannot identify the agent.

### What to write in git notes

Add or append `git notes --ref=context` only for nontrivial commits or handoff points, using `templates/context-note.md`. Notes should capture:

- why the change was made;
- alternatives considered and rejected;
- debugging or profiler evidence;
- tests, simulations, or benchmark evidence;
- open hypotheses or constraints future agents must preserve;
- any deviation from the original plan.

Do not restate the diff, paste secrets, include private hidden-reasoning transcript, or write context-free todo lists. If the note becomes a reusable lesson, create or update one scoped lesson file instead of duplicating it across commits.

### Safe command helpers

Use the scripts in `scripts/` when available:

- `session_id.sh` resolves and caches the session ID.
- `recent_context.sh` prints the last ten commits plus `git notes --ref=context`.
- `add_context_note.sh HEAD "message"` appends a context note to a commit.

Preserve existing notes and append only when useful and within the authorized scope. Commit coherent changes locally. Never push or merge without explicit user approval; do not infer permission for history rewriting. Keep owner commit messages free of attribution trailers.

### Handoff output

When ending a long session, report:

- current commit or working tree state;
- verified tests, benchmarks, and simulations;
- unresolved hypotheses;
- where the durable notes were written.

## 3. Durable lessons

Use this section for memory that should improve future sessions. Do not use it
for current status; that belongs in the task record above.

Create or update a durable lesson when it is reusable, non-obvious, evidence-backed, and likely to prevent a future mistake. Good lessons include user preferences, project conventions, detector ordering rules, decoder weight conventions, hardware constraints, benchmark findings, architecture invariants, and confirmed debugging approaches.

Do not save secrets, raw chat summaries, vague todos, restatements of diffs, guesses, stale speculation, or private hidden-reasoning text.

1. Decide whether this is active state, commit memory, or durable lesson memory.
2. Search existing lessons before creating a new one.
3. Verify the lesson against files, commands, commits, test output, benchmarks, simulations, or source documents.
4. Write one lesson per file using `templates/lesson.md`.
5. Add revalidation guidance: when to trust it, when to re-check it, and what would invalidate it.
6. Update or delete stale lessons instead of duplicating them.
7. Mention the memory file or git note only when it affected the decision.

### Session mining

When many past failures need systematic comparison, use the task harness section of `verifying-scientific-code`: mine sessions or review comments, cluster recurring corrections, adversarially verify whether each rule would have prevented a real mistake, then distill survivors into the user-authorized skill or memory location. Do not widen the permitted file scope.

## Done

Records are done when a future agent can load the relevant note, understand the
correction, see evidence, know the revalidation condition, and avoid duplicating
or trusting stale information.
