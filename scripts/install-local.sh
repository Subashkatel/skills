#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
skills_dir="${repo_root}"

force=0
if [[ "${1:-}" == "--force" ]]; then
  force=1
elif [[ "$#" -gt 0 ]]; then
  echo "Usage: scripts/install-local.sh [--force]" >&2
  exit 2
fi

codex_skills_dir="${HOME}/.agents/skills"
claude_skills_dir="${HOME}/.claude/skills"

if [[ ! -d "${skills_dir}" ]]; then
  echo "Missing skills directory: ${skills_dir}" >&2
  exit 1
fi

install_link() {
  local source="$1"
  local dest="$2"
  local label="$3"

  if [[ -L "${dest}" ]]; then
    local current_target
    current_target="$(readlink "${dest}")"
    if [[ "${current_target}" == "${source}" ]]; then
      echo "  ${label}: ${dest} (already linked)"
      return 0
    fi
    if [[ "${force}" -ne 1 ]]; then
      echo "Skipping ${label}: symlink already points elsewhere: ${dest} -> ${current_target}" >&2
      echo "Use --force to replace that symlink." >&2
      return 1
    fi
    rm "${dest}"
  elif [[ -e "${dest}" ]]; then
    echo "Skipping ${label}: destination already exists and is not a symlink: ${dest}" >&2
    return 1
  fi

  ln -s "${source}" "${dest}"
  echo "  ${label}: ${dest}"
}

installed=0
required_failures=0
seen_skills=0
for skill_source in "${skills_dir}"/*; do
  [[ -d "${skill_source}" ]] || continue

  skill_name="$(basename "${skill_source}")"
  if [[ ! -f "${skill_source}/SKILL.md" ]]; then
    continue
  fi
  seen_skills=$((seen_skills + 1))

  codex_dest="${codex_skills_dir}/${skill_name}"
  claude_dest="${claude_skills_dir}/${skill_name}"

  mkdir -p "${codex_skills_dir}" "${claude_skills_dir}"

  echo "Installing ${skill_name}:"
  linked=0
  if install_link "${skill_source}" "${codex_dest}" "Codex"; then
    linked=1
  else
    required_failures=$((required_failures + 1))
  fi
  if install_link "${skill_source}" "${claude_dest}" "Claude"; then
    linked=1
  else
    required_failures=$((required_failures + 1))
  fi
  if [[ "${linked}" -eq 1 ]]; then
    installed=$((installed + 1))
  fi
done

if [[ "${seen_skills}" -eq 0 ]]; then
  echo "No skill directories found under ${skills_dir}." >&2
  exit 1
fi

if [[ "${installed}" -eq 0 ]]; then
  echo "No skills were linked successfully." >&2
  exit 1
fi

if [[ "${required_failures}" -gt 0 ]]; then
  echo "Completed with ${required_failures} skipped or failed required install target(s)." >&2
  exit 1
fi

echo "Restart Codex to pick up new skills. Claude Code usually detects SKILL.md edits live."
