#!/usr/bin/env python3
from __future__ import annotations
import json
import sys
from pathlib import Path

VALID = {"not-run", "red", "green", "pass", "fail", "skipped", "blocked"}


def main() -> int:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "tests.json")
    if not path.exists():
        print(f"missing {path}")
        return 2
    data = json.loads(path.read_text())
    tests = data.get("tests", []) if isinstance(data, dict) else []
    errors: list[str] = []
    if not isinstance(tests, list):
        errors.append("tests must be a list")
    for index, test in enumerate(tests if isinstance(tests, list) else []):
        if not isinstance(test, dict):
            errors.append(f"tests[{index}] is not an object")
            continue
        if not test.get("name"):
            errors.append(f"tests[{index}] has no name")
        if not test.get("contract") and not test.get("purpose"):
            errors.append(f"tests[{index}] needs contract or purpose")
        if not test.get("command"):
            errors.append(f"tests[{index}] has no command")
        for phase in ("red", "green", "refactor", "final_gate"):
            value = test.get(phase)
            if isinstance(value, dict):
                status = value.get("status", "not-run")
            else:
                status = value or "not-run"
            if status not in VALID:
                errors.append(f"tests[{index}].{phase} has invalid status {status!r}")
    if errors:
        print("tests.json check failed")
        for error in errors:
            print(f"- {error}")
        return 1
    print("tests.json check passed")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
