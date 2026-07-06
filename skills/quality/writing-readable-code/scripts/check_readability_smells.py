#!/usr/bin/env python3
"""Heuristic readability-smell scanner for Python files.

This script is intentionally conservative. It cannot decide style for you; it only
flags names and expression shapes that deserve a human review.
"""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path

ALLOWED_SHORT_NAMES = {
    "_",
    "__",
    "e",
    "i",
    "j",
    "k",
    "m",
    "n",
    "p",
    "q",
    "x",
    "y",
    "z",
}
SUSPICIOUS_ABBREVIATIONS = {
    "arr",
    "buf",
    "cfg",
    "cnt",
    "ctx",
    "cur",
    "dst",
    "idx",
    "obj",
    "prev",
    "res",
    "src",
    "tmp",
    "val",
    "wm",
}


def iter_python_files(paths: list[str]) -> list[Path]:
    files: list[Path] = []
    for raw_path in paths:
        path = Path(raw_path)
        if path.is_dir():
            files.extend(sorted(path.rglob("*.py")))
        elif path.suffix == ".py":
            files.append(path)
    return files


class ReadabilityVisitor(ast.NodeVisitor):
    def __init__(self, path: Path) -> None:
        self.path = path
        self.issues: list[tuple[int, str]] = []

    def check_name(self, name: str, line_number: int, role: str) -> None:
        if len(name) <= 2 and name not in ALLOWED_SHORT_NAMES:
            self.issues.append((line_number, f"short {role} name `{name}`"))
        if name in SUSPICIOUS_ABBREVIATIONS:
            self.issues.append((line_number, f"abbreviated {role} name `{name}`"))

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:  # noqa: N802
        if len(node.name) <= 2:
            self.issues.append((node.lineno, f"short function name `{node.name}`"))
        for argument in node.args.args + node.args.kwonlyargs:
            self.check_name(argument.arg, argument.lineno, "argument")
        if node.args.vararg:
            self.check_name(node.args.vararg.arg, node.args.vararg.lineno, "vararg")
        if node.args.kwarg:
            self.check_name(node.args.kwarg.arg, node.args.kwarg.lineno, "kwarg")
        self.generic_visit(node)

    visit_AsyncFunctionDef = visit_FunctionDef

    def visit_Name(self, node: ast.Name) -> None:  # noqa: N802
        if isinstance(node.ctx, ast.Store):
            self.check_name(node.id, node.lineno, "assigned variable")
        self.generic_visit(node)


def count_nested_calls(line: str) -> int:
    return len(re.findall(r"\w+\s*\(", line))


def scan_file(path: Path) -> list[tuple[int, str]]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    issues: list[tuple[int, str]] = []

    try:
        tree = ast.parse(text, filename=str(path))
    except SyntaxError as error:
        return [(error.lineno or 0, f"syntax error: {error.msg}")]

    visitor = ReadabilityVisitor(path)
    visitor.visit(tree)
    issues.extend(visitor.issues)

    for line_number, line in enumerate(text.splitlines(), start=1):
        stripped_line = line.strip()
        if not stripped_line or stripped_line.startswith("#"):
            continue
        if ";" in stripped_line and not stripped_line.startswith("for "):
            issues.append((line_number, "multiple statements may be on one line"))
        if count_nested_calls(stripped_line) >= 3 and ("[" in stripped_line or "." in stripped_line):
            issues.append((line_number, "dense expression with several calls/indexes"))

    return sorted(set(issues))


def main(argv: list[str]) -> int:
    if not argv:
        print("usage: check_readability_smells.py <file-or-directory> [...]", file=sys.stderr)
        return 2

    any_issue = False
    for path in iter_python_files(argv):
        issues = scan_file(path)
        for line_number, message in issues:
            print(f"{path}:{line_number}: {message}")
            any_issue = True
    return 1 if any_issue else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
