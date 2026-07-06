---
name: authoring-agent-skills
description: "Creates or revises agent skills with concise triggers, operational steps, support-file boundaries, and eval cases. Use when adding or pruning skills for Claude Code or Codex."
---

# Authoring Agent Skills

A skill is operational memory for an agent. It should make the agent take a better process every time it triggers.

## Workflow

1. **Define the job.** Name the concrete behavior the skill should change and the failure it prevents.
2. **Write the trigger first.** The description is what the agent sees before loading the skill. Front-load use cases, boundaries, and domain words that should trigger it.
3. **Keep the body procedural.** Use steps, decision points, checks, failure smells, and done conditions. Avoid essays and generic advice.
4. **Use progressive disclosure.** Keep `SKILL.md` short. Move long examples, schemas, provider notes, rubrics, and templates into support files the skill explicitly names when needed.
5. **Prefer durable principles.** Avoid current file paths, line numbers, constants, one bug’s play-by-play, or implementation mechanics unless the skill is a navigation runbook.
6. **Name completion criteria.** Each workflow should make it clear when the step and whole skill are done.
7. **Add eval cases.** Include at least three realistic inputs that test when the skill should trigger and what good behavior means.
8. **Validate structure.** Run the pack validator, then read the skill as a fresh agent with no conversation history.

## Description checklist

- States what the skill does.
- States when to use it.
- Includes boundaries so it does not overtrigger.
- Uses the same words users and other skills will say.
- Stays concise enough to survive description truncation.

## Failure smells

- Premature completion: the skill stops before its promised artifact exists.
- Stage compression: multiple workflow stages are waved through in one response.
- Duplication: the same rule appears in several places.
- Sediment: old cautions and workarounds remain after the model or workflow no longer needs them.
- War story: a one-off incident is written as a reusable rule with stale specifics.
- No-op: the line says what the model already does.
- Overtrigger: the description makes the skill fire for tasks that do not need it.

## Done

The skill is done when its description triggers correctly, the body is short enough to read in one pass, support files are loaded only when useful, evals cover realistic cases, and a fresh agent can follow it without knowing why it was written.
