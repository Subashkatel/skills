---
name: auditing-skills
description: "Audit skill triggers, instructions, references, and evals for relevance, correctness, and unnecessary overhead."
---

# Auditing Skills

## Purpose

Review skills as operational instructions. A good skill should trigger at the right time, load concise guidance, point to useful support files, and avoid stale or unsafe prompting patterns.

## Audit workflow

1. Validate frontmatter:
   - Name is lowercase letters/numbers/hyphens.
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
   - Quantum/QEC skills require assumptions, algebra, simulator/decoder config, and uncertainty labels.
5. Check evals:
   - Positive cases, near-misses, and consequential boundaries.
   - Expected behavior is testable.
6. Report changed scope, preserved constraints, checks actually run, and remaining limits. Use `templates/skill-audit-report.md` only when a saved report is useful and allowed.

## Script

`scripts/validate_skill_pack.py` performs structural checks on a skill pack.

## Cross-agent audit

When auditing skills intended for both Claude Code and Codex, check that the core workflow is model-agnostic, platform-specific session variables are paired with equivalents, and side-effecting startup or git-note behavior is safe, local, and append-only by default.
