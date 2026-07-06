#!/usr/bin/env python3
"""Run a benchmark command multiple times and report wall-time statistics.

This is a generic harness. For kernel timings, prefer in-program GPU event timing
or profiler output; this script is useful for end-to-end measurements.
"""
from __future__ import annotations
import argparse, statistics, subprocess, time


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('-n', '--repeats', type=int, default=10)
    ap.add_argument('--warmup', type=int, default=1)
    ap.add_argument('command', nargs=argparse.REMAINDER)
    args = ap.parse_args()
    if args.command and args.command[0] == '--':
        args.command = args.command[1:]
    if not args.command:
        raise SystemExit('provide a command after --, e.g. python repeat_command.py -- ./bench')
    for _ in range(args.warmup):
        subprocess.run(args.command, check=True)
    times = []
    for _ in range(args.repeats):
        t0 = time.perf_counter()
        subprocess.run(args.command, check=True)
        times.append(time.perf_counter() - t0)
    print({'repeats': args.repeats, 'min_s': min(times), 'median_s': statistics.median(times), 'max_s': max(times)})
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
