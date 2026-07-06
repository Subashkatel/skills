#!/usr/bin/env bash
set -euo pipefail

if ! git rev-parse --git-dir >/dev/null 2>&1; then
  echo "Not inside a git repository."
  exit 0
fi

if git show-ref --verify --quiet refs/notes/context; then
  git log --notes=context -10 --format=$'=== %h %s ===%n%N'
else
  git log -10 --format='=== %h %s ==='
fi
