# skills

Portable AI agent skills for Codex and Claude.

## Included skills

- `claude-prompt-refiner`: turns rough prompts into structured, Claude-ready prompt packages.

## Add another skill

Create a new folder at the repository root:

```text
your-skill-name/
  SKILL.md
```

Keep the folder name lowercase hyphen-case. Put detailed examples, templates, and larger docs in `references/`, reusable scripts in `scripts/`, and output assets in `assets/`.

## Repository layout

```text
claude-prompt-refiner/
  SKILL.md
  agents/openai.yaml
  references/
    examples.md
    prompt-template.md
scripts/
  install-local.sh
```

The canonical skill package is `claude-prompt-refiner/`. Its `SKILL.md` uses only shared frontmatter fields so it remains compatible with Codex and Claude.

## Install locally

Run:

```bash
scripts/install-local.sh
```

That symlinks every skill folder in this repository into:

- Codex: `$HOME/.agents/skills/<skill-name>`
- Claude: `$HOME/.claude/skills/<skill-name>`

Restart Codex after installing. Claude Code usually detects edits to existing skill files live.

The installer will not overwrite an existing real directory. It also refuses to replace a symlink that points somewhere else unless you run:

```bash
scripts/install-local.sh --force
```

## Project use

Claude Code discovers project skills from `.claude/skills/`. Codex discovers repository skills from `.agents/skills/`.

This repository keeps canonical skill packages at the repository root and ignores project symlinks for portability. A fresh clone will not expose project skills until you run the local installer above or create local project symlinks:

```bash
mkdir -p .agents/skills
mkdir -p .claude/skills
for skill in */; do
  test -f "$skill/SKILL.md" || continue
  name="$(basename "$skill")"
  ln -sfn "../../$name" ".agents/skills/$name"
  ln -sfn "../../$name" ".claude/skills/$name"
done
```

The symlinks are ignored in git because the canonical package already lives at the repository root.

## Codex install from GitHub

After pushing this repo, install the skill from:

```text
Subashkatel/skills
claude-prompt-refiner
```
