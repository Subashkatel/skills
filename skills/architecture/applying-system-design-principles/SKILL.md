---
name: applying-system-design-principles
description: "Review module boundaries, plug-in contracts, dependency levels, or unstable interfaces against system-design principles."
---

# Applying System Design Principles

## Purpose

Turn "is this a good abstraction?" into checks that run on the tree
and findings that cite a source. Each principle in
`reference/principles.md` has a quote, its line in the source text,
and one check. Findings are recorded under the principle that caught
them, so the reason survives the fix.

## Scope

Review the affected boundaries and the principles that bear on the requested
change. Use `reference/principles.md` for source passages. Treat the checks as
design heuristics unless local policy makes them requirements. In decsim, read
the active worktree's `STYLE.md` and relevant decisions; their scope is local.

## Workflow

1. **Write the changeability list (Parnas).** List the decisions the
   system exists to vary (what an experiment sweeps, what a user
   swaps). For each, name the one module that knows it. A decision two
   modules know is a leak: cite both sites. Done when every decision
   has exactly one owner or a finding.
2. **Build the uses graph (Parnas, Dijkstra).** Run
   `scripts/uses_graph.py <package root>`. This script scans absolute imports only; it misses relative imports
   and isolated nodes and is a proxy for semantic dependency, not a proof.
   Inspect omitted dependencies before drawing conclusions. If the design
   requires layers, check cycles and whether lower layers run independently. A package holding both a leaf and a top (a names module and
   a wiring module) is the usual cause of a cycle: split it.
3. **Grep for recognition by class (gem5 port API).** Search every
   component for `isinstance(`, `type(...) is`, `__class__` against
   classes from another package or from a plug-in table. Classify hits against the plug-in contract and local exemptions.
   A branch that must change for each new plug-in may expose hidden policy;
   use a port fact when that is the real missing contract.
4. **Inspect affected cross-boundary imports.** Port (abstract interface),
   record (behaviour-free data), or reach-in (another component's live
   object or internal types). Reach-ins that expose private implementation are findings; shared records
   move to the shared records place; internal types stay home.
5. **Check the interfaces' promises (Parnas, Lampson, Hyrum).** No
   method or golden compares an order the design does not promise
   (compare multisets when duplicates matter, sets only when they do not). Check real consumers and promised extension points. Stable interfaces
   may evolve; apply a design-note requirement only where local policy calls
   for one. Tests pin promises,
   never incidental ticks, strings or orders.
6. **Mark the local-versus-remote line (Waldo).** For a boundary that changes latency, memory access, partial failure,
   or concurrency, name which differences the model includes and which it
   excludes. Express retry semantics when applicable; a modeled unit is
   not automatically a distributed failure domain.
7. **Separate essential from accidental (Brooks).** Make relevant states and transitions understandable. A phase record
   is one option, not a universal representation. Judge roots, classes, and
   wrappers by the responsibility and complexity they hide, not size alone.
8. **Record.** One table: finding, principle, site, size of fix,
   ranked by which promise it breaks. Record it once in the requested review or design note, with a source
   locator and a clear distinction between the source and its application.

## Decision points

- If the system has no plug-in tables, step 3 still applies to any
  `isinstance` on a sibling package's classes.
- If the graph has cycles, fix them before judging levels; levels are
  undefined on a cyclic graph.
- If a golden or characterization test fails without a code change,
  suspect step 5 before suspecting the code.

## Failure smells

- A design preference presented as a theorem from a source; separate evidence
  from local policy and professional judgment.
- An alias, wrapper, or second path that hides a duplicate owner rather than
  serving a required boundary.
- A new concept introduced to satisfy a check (the checks ask for
  fewer concepts, never more).
- The changeability list written from the code instead of from the
  system's purpose.

## Done

The relevant principles and changed boundaries have evidence-backed verdicts.
Required local checks pass, tool coverage limits are stated, and remaining
findings are ranked. A targeted review does not require a whole-tree audit.

## Support files

- `reference/principles.md`: the principles, quotes, line citations,
  source locations and how to fetch them.
- `scripts/uses_graph.py`: the package uses graph, cycles and levels.
