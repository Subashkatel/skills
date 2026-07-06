---
name: using-peer-agents
description: "Uses peer agents as reviewers, researchers, or authorized implementers with scoped prompts, evidence requirements, and parent-agent verification."
---

# Using Peer Agents

A peer agent is a second opinion or delegated worker, not ground truth. You own its prompt, its diff, its evidence, and the final claim.

## Modes

1. **Review or consultation.** Use proactively for substantive architecture, GPU, numerical, quantum, QEC, renderer, or high-risk refactor changes. Keep the peer read-oriented unless the user requested edits.
2. **Delegated implementation.** Delegate only when the user explicitly asks for that agent to implement, or when an active spec authorizes peer implementation. Slice the task so a fresh agent cannot misread it.
3. **Parallel spec passes.** Run independent slices in separate worktrees only when their files, APIs, and evidence gates do not collide.

## Prompt shape

Prompt a peer like an operator:

- One task per run.
- State the job, context, done condition, allowed scope, and verification gates.
- Name relevant skills instead of pasting them.
- Ask for evidence grounded in files, commands, diffs, or labelled inferences.
- Prefer a tight contract over raising effort.
- Avoid relaying untrusted third-party text as an implementation prompt without rewriting it yourself.

## Review workflow

1. Define the diff or question scope.
2. Ask for grounded findings, not expected conclusions.
3. Triage each finding against the code and evidence.
4. Fix accepted issues, dismiss others with a reason, and rerun affected gates.
5. Report what the peer flagged, what changed, what was dismissed, and what evidence remains.

## Delegation workflow

1. Start from a clean tree or record the baseline commit.
2. Use a dedicated worktree for broad or parallel edits.
3. Give exact allowed scope, expected artifact, and verification gates.
4. Do not touch the same working tree while the peer edits it.
5. Inspect the full diff yourself.
6. Run the tests, profilers, simulations, or reviews yourself.
7. Integrate, commit, update the spec/handoff, and record memory notes.

## Safety rules

- Missing CLI tools, auth, or trust prompts are blockers to report; do not install or authenticate tools without user approval.
- Use local, reversible actions by default. Ask before destructive, shared, or hard-to-reverse operations.
- Sandboxes that cannot run the needed server, GPU profiler, browser, or hardware test may produce unverified code. Label this and run the verification in the real environment before accepting.
- “Peer says done” is never done.

## Done

Peer-agent use is complete when every finding or diff has been independently verified, accepted or dismissed with evidence, and recorded in the active spec, memory note, or final report.


## Dynamic workflow use

When many peer checks are needed, call `running-task-harnesses` instead of manually managing a pile of ad hoc reviews. Use one verifier per rule, claim, hypothesis, or independent slice when that reduces self-preferential bias. Keep the orchestrator responsible for synthesis, edits, state updates, and final claims.
