#!/usr/bin/env python3
"""Validate a minimal QEC experiment result JSON schema.

Expected top-level keys:
  code, noise_model, decoder, distances, physical_error_rates, shots, results
"""
from __future__ import annotations
import argparse, json, sys

REQUIRED = {'code', 'noise_model', 'decoder', 'distances', 'physical_error_rates', 'shots', 'results'}

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('json_file')
    args = ap.parse_args()
    data = json.load(open(args.json_file, encoding='utf-8'))
    missing = sorted(REQUIRED - set(data))
    if missing:
        print('missing keys:', ', '.join(missing))
        return 1
    if not isinstance(data['results'], list):
        print('results must be a list')
        return 1
    for i, row in enumerate(data['results']):
        for key in ['distance', 'p', 'shots', 'failures']:
            if key not in row:
                print(f'results[{i}] missing {key}')
                return 1
    print('QEC experiment schema looks valid')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
