#!/usr/bin/env python3
"""Probe common GPU development tools without requiring CUDA/ROCm Python packages."""
from __future__ import annotations
import shutil, subprocess

COMMANDS = [
    ['nvidia-smi'],
    ['nvcc', '--version'],
    ['ncu', '--version'],
    ['nsys', '--version'],
    ['rocminfo'],
    ['rocm-smi'],
    ['hipcc', '--version'],
    ['rocprofv3', '--version'],
]

def main() -> int:
    for cmd in COMMANDS:
        exe = shutil.which(cmd[0])
        print(f"\n## {' '.join(cmd)}")
        if not exe:
            print('not found')
            continue
        try:
            out = subprocess.run(cmd, text=True, capture_output=True, timeout=10)
            print(out.stdout.strip() or out.stderr.strip() or f'exit code {out.returncode}')
        except Exception as e:
            print(f'error: {e}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
