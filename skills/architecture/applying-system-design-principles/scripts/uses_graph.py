"""Print a package's 'uses' graph, its cycles, and its levels.

Usage: python uses_graph.py <path to the top package directory>

The relation is Parnas 1972's "uses": package A uses package B when a
module of A imports a module of B. Cycles are listed; when there are
none, each package's level is the longest path below it, so level 0
packages depend on nothing inside the top package.
"""
import collections
import pathlib
import re
import sys

root = pathlib.Path(sys.argv[1]).resolve()
top = root.name
edges = collections.defaultdict(set)
pattern = re.compile(
    r"^\s*(?:from|import)\s+" + re.escape(top) + r"\.([A-Za-z_][A-Za-z0-9_]*)",
    re.M,
)
for path in root.rglob("*.py"):
    if "__pycache__" in path.parts:
        continue
    source = path.relative_to(root).parts[0]
    if source.endswith(".py"):
        source = source[:-3]
    for match in pattern.finditer(path.read_text(errors="ignore")):
        target = match.group(1)
        if target != source:
            edges[source].add(target)

nodes = sorted(set(edges) | {t for s in edges for t in edges[s]})
color = {}
cycles = []


def visit(node, stack):
    color[node] = 1
    stack.append(node)
    for nxt in sorted(edges.get(node, ())):
        if color.get(nxt) == 1:
            cycles.append(stack[stack.index(nxt):] + [nxt])
        elif nxt not in color:
            visit(nxt, stack)
    stack.pop()
    color[node] = 2


for node in nodes:
    if node not in color:
        visit(node, [])
for node in nodes:
    print(f"{node:24s} -> {' '.join(sorted(edges.get(node, ())))}")
print("cycles:", len(cycles))
for cycle in cycles:
    print("  ", " -> ".join(cycle))
if cycles:
    sys.exit(1)
level = {}


def level_of(node):
    if node in level:
        return level[node]
    below = [level_of(n) for n in edges.get(node, ())]
    level[node] = 1 + max(below, default=-1)
    return level[node]


for node in nodes:
    level_of(node)
grouped = collections.defaultdict(list)
for node, lv in level.items():
    grouped[lv].append(node)
for lv in sorted(grouped):
    print("level", lv, sorted(grouped[lv]))
