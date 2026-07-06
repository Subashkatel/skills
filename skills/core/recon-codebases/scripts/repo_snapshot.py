#!/usr/bin/env python3
"""Create a compact repository snapshot for Claude Code recon.

Usage:
  python repo_snapshot.py [root] [--max-files 500]
"""
from __future__ import annotations
import argparse, os
from pathlib import Path

SKIP_DIRS = {'.git', '.hg', '.svn', '__pycache__', '.pytest_cache', '.mypy_cache', '.ruff_cache', 'node_modules', 'dist', 'build', 'target', '.venv', 'venv', '.tox', '.idea', '.vscode'}
INTERESTING = {'.py','.rs','.cpp','.cc','.c','.cu','.cuh','.hip','.h','.hpp','.md','.toml','.yaml','.yml','.json','.cmake','.txt','.qasm','.stim','.dem'}

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('root', nargs='?', default='.')
    ap.add_argument('--max-files', type=int, default=500)
    args = ap.parse_args()
    root = Path(args.root).resolve()
    count = 0
    print(f"# Repository snapshot: {root}")
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in sorted(dirnames) if d not in SKIP_DIRS]
        rel_dir = Path(dirpath).relative_to(root)
        depth = 0 if str(rel_dir) == '.' else len(rel_dir.parts)
        if depth > 4:
            dirnames[:] = []
            continue
        for fn in sorted(filenames):
            p = Path(dirpath) / fn
            if p.suffix.lower() not in INTERESTING and fn not in {'Makefile','Dockerfile','CMakeLists.txt'}:
                continue
            try:
                size = p.stat().st_size
            except OSError:
                continue
            print(f"{p.relative_to(root)}\t{size} bytes")
            count += 1
            if count >= args.max_files:
                print(f"# stopped at --max-files={args.max_files}")
                return 0
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
