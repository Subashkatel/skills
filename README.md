# skills

AI agent skills for Codex and Claude.

This repository contains 36 skills organized by domain under `skills/<category>/<skill-name>/`.

## Layout

```text
skills/
  core/
    mapping-unknowns/
      SKILL.md
      agents/openai.yaml
      evals/evals.json
  gpu/
    programming-gpus/
      SKILL.md
      scripts/
      reference/
      templates/
  prompts/
    claude-prompt-refiner/
      SKILL.md
      references/
.claude-plugin/
  plugin.json
```

Each skill package contains its own `SKILL.md` and optional support files. Codex UI metadata lives in `agents/openai.yaml`.

## Skills

### Core

- [`mapping-unknowns`](skills/core/mapping-unknowns/SKILL.md)
- [`recon-codebases`](skills/core/recon-codebases/SKILL.md)
- [`orchestrating-skills`](skills/core/orchestrating-skills/SKILL.md)
- [`approximating-changes`](skills/core/approximating-changes/SKILL.md)

### Architecture

- [`designing-architectures`](skills/architecture/designing-architectures/SKILL.md)
- [`designing-classical-architectures`](skills/architecture/designing-classical-architectures/SKILL.md)
- [`planning-implementations`](skills/architecture/planning-implementations/SKILL.md)
- [`slicing-specs`](skills/architecture/slicing-specs/SKILL.md)
- [`implementing-specs`](skills/architecture/implementing-specs/SKILL.md)
- [`closing-specs`](skills/architecture/closing-specs/SKILL.md)

### Quantum Systems

- [`programming-qpus`](skills/quantum-systems/programming-qpus/SKILL.md)
- [`modeling-quantum-architectures`](skills/quantum-systems/modeling-quantum-architectures/SKILL.md)
- [`engineering-qec`](skills/quantum-systems/engineering-qec/SKILL.md)
- [`engineering-qec-decoders`](skills/quantum-systems/engineering-qec-decoders/SKILL.md)

### GPU

- [`programming-gpus`](skills/gpu/programming-gpus/SKILL.md)
- [`debugging-gpu-renderers`](skills/gpu/debugging-gpu-renderers/SKILL.md)
- [`reviewing-rendered-output`](skills/gpu/reviewing-rendered-output/SKILL.md)

### Quality

- [`writing-readable-code`](skills/quality/writing-readable-code/SKILL.md)
- [`practicing-tdd`](skills/quality/practicing-tdd/SKILL.md)
- [`writing-behavior-tests`](skills/quality/writing-behavior-tests/SKILL.md)
- [`refactoring-cleanly`](skills/quality/refactoring-cleanly/SKILL.md)
- [`verifying-scientific-code`](skills/quality/verifying-scientific-code/SKILL.md)

### Memory And Testing

- [`tracking-work-state`](skills/memory-testing/tracking-work-state/SKILL.md)
- [`recording-repo-memory`](skills/memory-testing/recording-repo-memory/SKILL.md)
- [`maintaining-agent-state`](skills/memory-testing/maintaining-agent-state/SKILL.md)
- [`managing-agent-memory`](skills/memory-testing/managing-agent-memory/SKILL.md)
- [`running-task-harnesses`](skills/memory-testing/running-task-harnesses/SKILL.md)

### Research And Docs

- [`reviewing-research`](skills/research-docs/reviewing-research/SKILL.md)
- [`writing-durable-docs`](skills/research-docs/writing-durable-docs/SKILL.md)
- [`explaining-changes`](skills/research-docs/explaining-changes/SKILL.md)
- [`refining-prompts`](skills/research-docs/refining-prompts/SKILL.md)

### Skill Maintenance

- [`auditing-skills`](skills/skill-maintenance/auditing-skills/SKILL.md)
- [`authoring-agent-skills`](skills/skill-maintenance/authoring-agent-skills/SKILL.md)
- [`evaluating-agent-skills`](skills/skill-maintenance/evaluating-agent-skills/SKILL.md)
- [`using-peer-agents`](skills/skill-maintenance/using-peer-agents/SKILL.md)

### Prompts

- [`claude-prompt-refiner`](skills/prompts/claude-prompt-refiner/SKILL.md)

## Use Locally

Copy or symlink any `skills/<category>/<skill-name>/` folder into the standard skill location for your tool:

- Codex: `$HOME/.agents/skills/<skill-name>`
- Claude: `$HOME/.claude/skills/<skill-name>`

Restart Codex after adding new skills. Claude Code usually detects edits to existing skill files live.

## Claude Plugin

Claude plugin metadata lives in `.claude-plugin/plugin.json` and indexes all skill package paths.

## Codex Install From GitHub

Install individual skills from this repo by using the nested path, for example:

```text
Subashkatel/skills
skills/gpu/programming-gpus
```
