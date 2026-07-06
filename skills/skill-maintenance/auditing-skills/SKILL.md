---
name: auditing-skills
description: "Audits agent skills for trigger quality, YAML validity, progressive disclosure, safety, concision, and scientific-domain usefulness. Use when reviewing or migrating SKILL.md files."
---

# Auditing Skills

## Purpose

Review skills as operational instructions. A good skill should trigger at the right time, load concise guidance, point to useful support files, and avoid stale or unsafe prompting patterns.

## Audit workflow

1. Validate frontmatter:
   - Name is lowercase letters/numbers/hyphens.
   - Description says what the skill does and when to use it.
   - Description is specific and not vague.
2. Check SKILL.md body:
   - Under 500 lines.
   - Clear workflow.
   - No over-prescriptive or outdated anti-laziness instructions.
   - No instructions asking the model to expose hidden reasoning.
   - No broad tool permissions unless justified.
3. Check progressive disclosure:
   - Support files are useful.
   - References are one level deep.
   - Scripts solve concrete tasks and have safe error handling.
4. Check domain fit:
   - Architecture skills produce decisions and tradeoffs.
   - GPU skills require profiling and correctness evidence.
   - Quantum/QEC skills require assumptions, algebra, simulator/decoder config, and uncertainty labels.
5. Check evals:
   - At least three realistic prompts.
   - Expected behavior is testable.
6. Produce an audit report using `templates/skill-audit-report.md`.

## Script

`scripts/validate_skill_pack.py` performs structural checks on a skill pack.

## Cross-agent audit

When auditing skills intended for both Claude Code and Codex, check that the core workflow is model-agnostic, that Claude-specific session variables are paired with Codex equivalents, and that side-effecting startup or git-note behavior is safe, local, and append-only by default.
