#!/usr/bin/env python3
from __future__ import annotations
import json
import sys
from pathlib import Path

REQUIRED = ["goal", "current_status", "current_action", "plan", "evidence", "tests"]
TERMINAL = {"complete", "blocked", "cancelled"}


def main() -> int:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "agent-state.json")
    if not path.exists():
        print(f"missing {path}")
        return 2
    data = json.loads(path.read_text())
    errors: list[str] = []
    for key in REQUIRED:
        if key not in data:
            errors.append(f"missing required key: {key}")
    status = str(data.get("current_status", "")).strip().lower()
    if not str(data.get("goal", "")).strip():
        errors.append("goal is empty")
    if status not in TERMINAL and not str(data.get("current_action", "")).strip():
        errors.append("current_action is empty while task is not terminal")
    plan = data.get("plan", [])
    if status not in TERMINAL and (not isinstance(plan, list) or not plan):
        errors.append("plan is empty while task is not terminal")
    for index, step in enumerate(plan if isinstance(plan, list) else []):
        if not isinstance(step, dict):
            errors.append(f"plan[{index}] is not an object")
            continue
        if not step.get("description"):
            errors.append(f"plan[{index}] has no description")
        if step.get("status") not in {"pending", "in-progress", "blocked", "done", "skipped"}:
            errors.append(f"plan[{index}] has invalid status")
        if step.get("status") in {"pending", "in-progress"} and not step.get("next_action"):
            errors.append(f"plan[{index}] needs next_action")
    evidence = data.get("evidence", [])
    for index, item in enumerate(evidence if isinstance(evidence, list) else []):
        if not isinstance(item, dict):
            errors.append(f"evidence[{index}] is not an object")
            continue
        if item.get("status") == "verified" and not item.get("location"):
            errors.append(f"verified evidence[{index}] needs location")
    if errors:
        print("agent-state check failed")
        for error in errors:
            print(f"- {error}")
        return 1
    print("agent-state check passed")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
