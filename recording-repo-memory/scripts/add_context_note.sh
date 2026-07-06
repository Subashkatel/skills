#!/usr/bin/env bash
set -euo pipefail

if ! git rev-parse --git-dir >/dev/null 2>&1; then
  echo "Not inside a git repository." >&2
  exit 1
fi

commit="${1:-HEAD}"
shift || true
message="${*:-}"
if [ -z "$message" ]; then
  echo "Usage: add_context_note.sh [commit] <message>" >&2
  exit 2
fi

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
session="$($script_dir/session_id.sh)"
agent="${session%%:*}"
id="${session#*:}"

git notes --ref=context append -m "[$agent:$id] $message" "$commit"
echo "Appended context note to $commit with [$agent:$id]."
