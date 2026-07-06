#!/usr/bin/env python3
"""Compare two numeric CSV files elementwise with tolerances.

No third-party dependencies. Non-numeric cells must match exactly.
"""
from __future__ import annotations
import argparse, csv, math


def try_float(x: str):
    try:
        return float(x)
    except ValueError:
        return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('expected')
    ap.add_argument('actual')
    ap.add_argument('--rtol', type=float, default=1e-6)
    ap.add_argument('--atol', type=float, default=1e-12)
    args = ap.parse_args()
    exp = list(csv.reader(open(args.expected, newline='', encoding='utf-8')))
    act = list(csv.reader(open(args.actual, newline='', encoding='utf-8')))
    if len(exp) != len(act):
        print(f'row count differs: {len(exp)} vs {len(act)}')
        return 1
    mismatches = 0
    for i, (erow, arow) in enumerate(zip(exp, act), start=1):
        if len(erow) != len(arow):
            print(f'row {i} length differs: {len(erow)} vs {len(arow)}')
            mismatches += 1
            continue
        for j, (e, a) in enumerate(zip(erow, arow), start=1):
            ef, af = try_float(e), try_float(a)
            if ef is not None and af is not None:
                if not math.isclose(ef, af, rel_tol=args.rtol, abs_tol=args.atol):
                    print(f'cell {i},{j}: {ef} != {af}')
                    mismatches += 1
            elif e != a:
                print(f'cell {i},{j}: {e!r} != {a!r}')
                mismatches += 1
    if mismatches:
        print(f'{mismatches} mismatches')
        return 1
    print('files match within tolerance')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
