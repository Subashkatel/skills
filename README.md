# skills

AI agent skills for Codex and Claude.

This repository contains 24 skills organized by domain under `skills/<category>/<skill-name>/`.

## Layout

```text
skills/
  core/
    assessing-changes/
      SKILL.md
      agents/openai.yaml
      evals/evals.json
  gpu/
    programming-gpus/
      SKILL.md
      scripts/
      reference/
      templates/
  memory/
    keeping-work-records/
      SKILL.md
      references/
      scripts/
      templates/
.claude-plugin/
  plugin.json
  marketplace.json
```

Each skill package contains its own `SKILL.md` and optional support files. Codex UI metadata lives in `agents/openai.yaml`.

Do not load every skill. Pick the smallest set that reduces risk for the job in
front of you, chosen from the descriptions below, and add another only when the
next job crosses its boundary.

## Skills

### Core

- [`assessing-changes`](skills/core/assessing-changes/SKILL.md): unknowns and simpler alternatives before a costly change.
- [`recon-codebases`](skills/core/recon-codebases/SKILL.md): inspect a repository before making claims or edits.

### Architecture

- [`applying-system-design-principles`](skills/architecture/applying-system-design-principles/SKILL.md): module boundaries and plug-in contracts against the design principles.
- [`designing-architectures`](skills/architecture/designing-architectures/SKILL.md): cross-layer boundaries plus classical ownership and data flow.
- [`working-with-specs`](skills/architecture/working-with-specs/SKILL.md): plan, slice, implement and close a multi-pass spec.

### Quantum Systems

- [`programming-qpus`](skills/quantum-systems/programming-qpus/SKILL.md): QPU programs, transpilation, shots and runtime jobs.
- [`modeling-quantum-architectures`](skills/quantum-systems/modeling-quantum-architectures/SKILL.md): the quantum stack from hardware to application.
- [`engineering-qec`](skills/quantum-systems/engineering-qec/SKILL.md): codes, stabilizers, schedules, detector models and simulations.
- [`engineering-qec-decoders`](skills/quantum-systems/engineering-qec-decoders/SKILL.md): decoder design, semantics and benchmarks.

### GPU

- [`programming-gpus`](skills/gpu/programming-gpus/SKILL.md): kernels, data movement and renderer debugging with measurements.
- [`reviewing-rendered-output`](skills/gpu/reviewing-rendered-output/SKILL.md): accept plots, diagrams and images on visual evidence.

### Quality

- [`writing-readable-code`](skills/quality/writing-readable-code/SKILL.md): the owner's naming, one-action, comment and simplicity rules.
- [`writing-tests`](skills/quality/writing-tests/SKILL.md): behavior tests and the test-first loop.
- [`refactoring-cleanly`](skills/quality/refactoring-cleanly/SKILL.md): one owner per concept, no compatibility sediment.
- [`verifying-scientific-code`](skills/quality/verifying-scientific-code/SKILL.md): evidence, uncertainty and repeated-run harnesses.

### Memory

- [`keeping-work-records`](skills/memory/keeping-work-records/SKILL.md): task record, repository handoff and durable lessons.

### Research And Docs

- [`reviewing-research`](skills/research-docs/reviewing-research/SKILL.md): papers and benchmarks into grounded assumptions.
- [`writing-durable-docs`](skills/research-docs/writing-durable-docs/SKILL.md): why a system exists, and its invariants.
- [`explaining-changes`](skills/research-docs/explaining-changes/SKILL.md): reviewer-ready summaries, evidence and risks.
- [`refining-prompts`](skills/research-docs/refining-prompts/SKILL.md): rough prompts into agent prompts, Claude included.
- [`making-slides`](skills/research-docs/making-slides/SKILL.md): the owner's slide style and typography.
- [`applying-design-principles`](skills/research-docs/applying-design-principles/SKILL.md): hierarchy, spacing and emphasis in figures and decks.

### Skill Maintenance

- [`maintaining-skills`](skills/skill-maintenance/maintaining-skills/SKILL.md): author, audit and evaluate the skills in this pack.
- [`using-peer-agents`](skills/skill-maintenance/using-peer-agents/SKILL.md): scope and verify delegated agent work.

## Use Locally

Copy or symlink any `skills/<category>/<skill-name>/` folder into the standard skill location for your tool:

- Codex: `${CODEX_HOME:-$HOME/.codex}/skills/<skill-name>`
- Claude: `$HOME/.claude/skills/<skill-name>`

Restart Codex after adding new skills. Claude Code usually detects edits to existing skill files live.

## Claude Plugin Install (recommended)

The repo is an installable Claude Code plugin. On any machine, run:

```sh
claude plugin marketplace add Subashkatel/skills
claude plugin install skills@skills
```

This installs all 24 skills at user scope, so they are available in every project. Pull the latest skills after editing this repo with:

```sh
claude plugin update skills@skills
```

Plugin metadata lives in `.claude-plugin/plugin.json` (indexes all skill package paths); `.claude-plugin/marketplace.json` makes the repo installable as a marketplace.

## Codex Install From GitHub

Install individual skills from this repo by using the nested path, for example:

```text
Subashkatel/skills
skills/gpu/programming-gpus
```
