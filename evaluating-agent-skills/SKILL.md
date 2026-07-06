---
name: evaluating-agent-skills
description: "Evaluates skills with golden cases, blind fresh runs, separate judging, and gap-driven edits. Use when a skill overtriggers, undertriggers, or misses behavior."
---

# Evaluating Agent Skills

Treat a skill like a function under test. Feed it realistic inputs in a clean room, judge artifacts against a bar, and let the gaps drive edits.

## Required inputs

Stop and ask if any are missing:

- Target skill: an actual `SKILL.md`.
- Golden cases: concrete inputs the skill might receive.
- Bar per case: what a good artifact achieves and what smells make it bad.

## Workflow

1. **Read first principles.** Identify what the skill promises and what behavior it should change.
2. **Classify the eval.** Judgment evals use a qualitative bar; conformance evals require exact criteria. Do not turn a judgment skill into an answer checklist.
3. **Run blind.** Use one fresh, context-free run per case. The runner sees only the input and the instruction to use the target skill, not the expected result or bar.
4. **Judge separately.** A separate judge sees the artifact, the bar, and the skill’s first principles. The judge cites evidence from the artifact for each verdict.
5. **Account for variance.** Re-run important or borderline cases multiple times and report pass rate or failure pattern.
6. **Diagnose defects.** Map misses to authoring failures: vague done condition, missing rule, premature completion, overtrigger, undertrigger, duplication, sediment, no-op, or bad case.
7. **Revise with restraint.** Fix the named defect using `authoring-agent-skills`; do not add bulk unrelated to the observed failure.
8. **Re-evaluate all cases.** A fix can regress a previously passing case.

## Rules

- Blindness is essential. Leaking expected outputs teaches to the test.
- Grade against the bar, not against another artifact.
- A bad golden case is a finding, not a reason to warp the skill.
- Keep eval artifacts and reports in a temporary or clearly named eval folder, not mixed into product code.

## Output

Produce a report with case-by-case verdicts, pass rates, cited gaps, defect diagnosis, edits made or proposed, and re-eval results.

## Done

The evaluation is done when every case either clears its bar with repeatable evidence or has a clearly named reason the skill or case cannot support it.
