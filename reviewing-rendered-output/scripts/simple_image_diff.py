#!/usr/bin/env python3
"""Small dependency-light image diff helper.
Usage: python simple_image_diff.py reference.png candidate.png [out_diff.png]
Requires Pillow if diff image output is needed in most environments.
"""
from __future__ import annotations
import sys, math
from pathlib import Path
try:
    from PIL import Image, ImageChops, ImageStat
except Exception as exc:
    print(f"Pillow is required for this helper: {exc}", file=sys.stderr)
    sys.exit(2)

def main() -> int:
    if len(sys.argv) < 3:
        print("usage: simple_image_diff.py reference.png candidate.png [out_diff.png]", file=sys.stderr)
        return 2
    a = Image.open(sys.argv[1]).convert('L')
    b = Image.open(sys.argv[2]).convert('L')
    if a.size != b.size:
        print(f"size_mismatch reference={a.size} candidate={b.size}")
        return 1
    diff = ImageChops.difference(a, b)
    stat = ImageStat.Stat(diff)
    mae = stat.mean[0]
    rmse = math.sqrt(stat.mean[0] ** 2 + stat.var[0])
    hist = diff.histogram()
    total = a.size[0] * a.size[1]
    over32 = sum(hist[33:]) / total
    over64 = sum(hist[65:]) / total
    print(f"mae={mae:.4f}")
    print(f"rmse={rmse:.4f}")
    print(f"diff_ratio_gt32={over32:.6f}")
    print(f"diff_ratio_gt64={over64:.6f}")
    if len(sys.argv) >= 4:
        diff.save(sys.argv[3])
    return 0
if __name__ == '__main__':
    raise SystemExit(main())
