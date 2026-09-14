---
name: authoring-agent-skills
description: "Create or revise a skill with a specific trigger, essential guidance, supporting resources, and behavior cases."
---

# Authoring Agent Skills

A skill supplies task-specific knowledge the agent would otherwise lack. Keep constraints and useful evidence, and remove instructions that add no value.

## Workflow

1. **Define the job.** Name the concrete behavior the skill should change and the failure it prevents.
2. **Write the trigger first.** The description is what the agent sees before loading the skill. Name the actual task and a useful exclusion in as few words as possible. Avoid keyword lists and broad activation language.
3. **Keep essential guidance.** State constraints, decision points, and completion criteria. Prescribe order only where there is a dependency or demonstrated failure; avoid generic coaching and elaborate itineraries.
4. **Use progressive disclosure.** Keep `SKILL.md` short. Move long examples, schemas, provider notes, rubrics, and templates into support files the skill explicitly names when needed.
5. **Prefer durable principles.** Avoid current file paths, line numbers, constants, one bug’s play-by-play, or implementation mechanics unless the skill is a navigation runbook.
6. **Name completion criteria.** Each workflow should make it clear when the step and whole skill are done.
7. **Add eval cases.** Include realistic positive cases, a near-miss that must not trigger, and a boundary case. Preserve substantive regression cases; do not test exact wording or mandatory skill chains.
8. **Validate the change.** Check metadata and support links, then evaluate the affected behavior. Distinguish structural checks, manual review, and actual fresh-agent runs.

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

## Model migration

Audit one demonstrated gap at a time: shorten triggers, route optional references,
remove duplicated instructions, and clarify completion within existing authorization.
Preserve domain invariants, owner preferences, and necessary interface contracts.
Keep shared instructions model-agnostic and retain guidance that another supported
agent still needs. Review symlink targets and divergent clones before editing.
Do not edit reference repositories, manifests, or user configuration during a
skills-only task. Commit skill changes locally; never push or merge without approval.

Migration rationale: [OpenAI, Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra).
