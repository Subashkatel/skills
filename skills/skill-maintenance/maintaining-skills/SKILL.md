---
name: maintaining-skills
description: "Author, audit, and evaluate agent skills in a skill pack. Not for using a skill on a normal task."
---

# Maintaining Skills

A skill supplies task-specific knowledge the agent would otherwise lack. Keep
constraints and useful evidence, and remove instructions that add no value.
Three sections: author a skill, audit one, evaluate one. Enter at the section
the work needs.

## 1. Author

1. **Define the job.** Name the concrete behavior the skill should change and the failure it prevents.
2. **Write the trigger first.** The description is what the agent sees before loading the skill. Name the actual task and a useful exclusion in as few words as possible. Avoid keyword lists and broad activation language.
3. **Keep essential guidance.** State constraints, decision points, and completion criteria. Prescribe order only where there is a dependency or demonstrated failure; avoid generic coaching and elaborate itineraries.
4. **Use progressive disclosure.** Keep `SKILL.md` short. Move long examples, schemas, provider notes, rubrics, and templates into support files the skill explicitly names when needed. Start from `templates/skill-skeleton.md`.
5. **Prefer durable principles.** Avoid current file paths, line numbers, constants, one bug's play-by-play, or implementation mechanics unless the skill is a navigation runbook.
6. **Name completion criteria.** Each workflow should make it clear when the step and whole skill are done.
7. **Add eval cases.** Include realistic positive cases, a near-miss that must not trigger, and a boundary case. Preserve substantive regression cases; do not test exact wording or mandatory skill chains.
8. **Validate the change.** Check metadata and support links, then evaluate the affected behavior. Distinguish structural checks, manual review, and actual fresh-agent runs.

### Description checklist

- States what the skill does.
- States when to use it.
- Includes boundaries so it does not overtrigger.
- Uses the same words users and other skills will say.
- Stays concise enough to survive description truncation.

### Failure smells

- Premature completion: the skill stops before its promised artifact exists.
- Stage compression: multiple workflow stages are waved through in one response.
- Duplication: the same rule appears in several places.
- Sediment: old cautions and workarounds remain after the model or workflow no longer needs them.
- War story: a one-off incident is written as a reusable rule with stale specifics.
- No-op: the line says what the model already does.
- Overtrigger: the description makes the skill fire for tasks that do not need it.

A skill is authored well when its description triggers correctly, the body is short enough to read in one pass, support files are loaded only when useful, evals cover realistic cases, and a fresh agent can follow it without knowing why it was written.

## 2. Audit

Review skills as operational instructions. A good skill should trigger at the
right time, load concise guidance, point to useful support files, and avoid
stale or unsafe prompting patterns. `references/audit-rubric.md` holds the
rubric; use `templates/skill-audit-report.md` only when a saved report is useful
and allowed.

1. Validate frontmatter:
   - Name is lowercase letters, numbers, and hyphens.
   - Description says what the skill does and when to use it.
   - Description names the actual task, with no broad keyword triggers or redundant urgency.
2. Check SKILL.md body:
   - Concise enough for its purpose; the 500-line structural cap is not a target.
   - Clear workflow.
   - No over-prescriptive or outdated anti-laziness instructions.
   - No instructions asking the model to expose hidden reasoning.
   - No broad tool permissions unless justified.
3. Check progressive disclosure:
   - Support files are useful.
   - References are one level deep.
   - Scripts solve concrete tasks, state coverage limits, and have safe error handling.
   - References do not reintroduce conflicting defaults, unavailable-file claims, or mandatory reading stacks.
4. Check domain fit:
   - Architecture skills produce decisions and tradeoffs.
   - GPU skills require profiling and correctness evidence.
   - Quantum and QEC skills require assumptions, algebra, simulator or decoder config, and uncertainty labels.
5. Check evals:
   - Positive cases, near-misses, and consequential boundaries.
   - Expected behavior is testable.
6. Report changed scope, preserved constraints, checks actually run, and remaining limits.

### Cross-agent audit

When auditing skills intended for both Claude Code and Codex, check that the core workflow is model-agnostic, platform-specific session variables are paired with equivalents, and side-effecting startup or git-note behavior is safe, local, and append-only by default.

### Script

`scripts/validate_skill_pack.py` performs structural checks on a skill pack: frontmatter, name and directory agreement, description length and shape, body line cap, discouraged phrases, eval presence, and support-file nesting depth. It is a structural check, not a behavior evaluation.

## 3. Evaluate

Treat a skill like a function under test. Feed it realistic inputs in a clean
room, judge artifacts against a bar, and let the gaps drive edits.

### Required inputs

Find these in the request and skill package; draft missing cases and criteria when the intended behavior is clear. Ask only for a consequential ambiguity that the evidence cannot resolve:

- Target skill: an actual `SKILL.md`.
- Golden cases: concrete inputs the skill might receive.
- Bar per case: what a good artifact achieves and what smells make it bad.

### Evaluation workflow

1. **Read first principles.** Identify what the skill promises and what behavior it should change.
2. **Classify the eval.** Judgment evals use a qualitative bar; conformance evals require exact criteria. Do not turn a judgment skill into an answer checklist.
3. **Run blind.** Use one fresh, context-free run per case. The runner sees only the input and the instruction to use the target skill, not the expected result or bar.
4. **Judge separately.** A separate judge sees the artifact, the bar, and the skill's first principles. The judge cites evidence from the artifact for each verdict.
5. **Account for variance.** Re-run important or borderline cases multiple times and report pass rate or failure pattern.
6. **Diagnose defects.** Map misses to authoring failures: vague done condition, missing rule, premature completion, overtrigger, undertrigger, duplication, sediment, no-op, or bad case.
7. **Revise with restraint.** Fix the named defect using the author section above; do not add bulk unrelated to the observed failure.
8. **Check regressions.** Re-run affected cases and selection boundaries. Repeat expensive or stochastic runs only when failures or variance warrant it.

### Evaluation rules

- Blindness is essential. Leaking expected outputs teaches to the test.
- Grade against the bar, not against another artifact.
- A bad golden case is a finding, not a reason to warp the skill.
- Keep eval artifacts and reports in a temporary or clearly named eval folder, not mixed into product code.

Produce a report with case-by-case verdicts, pass rates, cited gaps, defect diagnosis, edits made or proposed, and re-eval results, using `templates/skill-eval-report.md`. The evaluation is done when every case either clears its bar with repeatable evidence or has a clearly named reason the skill or case cannot support it.

## Model migration

Audit one demonstrated gap at a time: shorten triggers, route optional references,
remove duplicated instructions, and clarify completion within existing authorization.
Preserve domain invariants, owner preferences, and necessary interface contracts.
Keep shared instructions model-agnostic and retain guidance that another supported
agent still needs. Review symlink targets and divergent clones before editing.
Do not edit reference repositories, manifests, or user configuration during a
skills-only task. Commit skill changes locally without attribution trailers;
never push or merge without approval.

Migration rationale: [OpenAI, Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra).
The last pack-wide audit is recorded in `references/astra-audit-2026-09-14.md`.
