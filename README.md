# skills

AI agent skills for Codex and Claude.

## Included skills

This repository currently contains 36 skills:

- Core workflow: `mapping-unknowns`, `recon-codebases`, `orchestrating-skills`, `approximating-changes`
- Architecture/spec work: `designing-architectures`, `designing-classical-architectures`, `planning-implementations`, `slicing-specs`, `implementing-specs`, `closing-specs`
- Quantum systems: `programming-qpus`, `modeling-quantum-architectures`, `engineering-qec`, `engineering-qec-decoders`
- GPU and visual output: `programming-gpus`, `debugging-gpu-renderers`, `reviewing-rendered-output`
- Quality, testing, and state: `writing-readable-code`, `practicing-tdd`, `writing-behavior-tests`, `refactoring-cleanly`, `verifying-scientific-code`, `tracking-work-state`, `recording-repo-memory`, `maintaining-agent-state`, `managing-agent-memory`, `running-task-harnesses`
- Research and docs: `reviewing-research`, `writing-durable-docs`, `explaining-changes`, `refining-prompts`, `claude-prompt-refiner`
- Skill maintenance: `auditing-skills`, `authoring-agent-skills`, `evaluating-agent-skills`, `using-peer-agents`

## Add another skill

Create a new folder at the repository root:

```text
your-skill-name/
  SKILL.md
```

Keep the folder name lowercase hyphen-case. Put detailed examples, templates, and larger docs in `references/`, reusable skill helpers in the skill's own `scripts/`, and output assets in `assets/`.

## Repository layout

```text
claude-prompt-refiner/
  SKILL.md
  agents/openai.yaml
  references/
    examples.md
    prompt-template.md
programming-gpus/
  SKILL.md
  agents/openai.yaml
  scripts/
  reference/
  templates/
  evals/
practicing-tdd/
  SKILL.md
  agents/openai.yaml
  scripts/
  templates/
  evals/
```

Each root-level directory containing `SKILL.md` is a canonical skill package. Skill frontmatter uses shared fields so packages remain compatible with Codex and Claude. Codex-specific UI metadata lives in `agents/openai.yaml`.

## Use Locally

Each root-level skill directory can be copied or symlinked into the standard skill location for the tool you use:

- Codex: `$HOME/.agents/skills/<skill-name>`
- Claude: `$HOME/.claude/skills/<skill-name>`

Restart Codex after adding new skills. Claude Code usually detects edits to existing skill files live.

## Codex install from GitHub

After pushing this repo, install an individual skill from:

```text
Subashkatel/skills
<skill-name>
```
