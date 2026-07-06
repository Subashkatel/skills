#!/usr/bin/env bash
set -euo pipefail

cache="${AGENT_SESSION_ID_CACHE:-/tmp/.agent-chat-id}"
agent="AGENT"
id=""

if [ -n "${CODEX_THREAD_ID:-}" ]; then
  agent="CODEX"
  id="$CODEX_THREAD_ID"
elif [ -n "${CLAUDE_SESSION_ID:-}" ]; then
  agent="CLAUDE"
  id="$CLAUDE_SESSION_ID"
elif [ -f /tmp/.codex-chat-id ] && [ -s /tmp/.codex-chat-id ]; then
  agent="CODEX"
  id="$(cat /tmp/.codex-chat-id)"
else
  project_key="$(pwd | sed 's#/#-#g')"
  latest=""
  if [ -d "$HOME/.codex/projects/$project_key" ]; then
    latest="$(ls -t "$HOME/.codex/projects/$project_key"/*.jsonl 2>/dev/null | head -n 1 || true)"
  fi
  if [ -n "$latest" ]; then
    agent="CODEX"
    id="$(basename "$latest" .jsonl)"
  else
    repo_name="$(basename "$(pwd)")"
    if [ -z "$repo_name" ] || [ "$repo_name" = "/" ]; then repo_name="session"; fi
    id="$repo_name-$(date -u +%Y%m%dT%H%M%SZ)"
  fi
fi

printf '%s\n' "$id" > "$cache"
printf '%s:%s\n' "$agent" "$id"
