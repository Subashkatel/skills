---
name: recon-codebases
description: "Inspect unfamiliar code paths and conventions needed to answer a repository question or make a change."
---

# Recon Codebases

## Rule

Do not make confident claims about code that has not been inspected. Before architecture, performance, or QEC implementation work, gather a map of the relevant files, tests, build commands, data flows, and conventions.

## Recon workflow

1. Identify the requested change or question.
2. Locate relevant files using directory listing, search, imports, tests, build scripts, and docs.
3. Read the files that determine behavior, not only files whose names look relevant.
4. Map only the parts needed for this question or change:
   - Entry points.
   - Core modules and ownership boundaries.
   - Runtime/data flow.
   - Test coverage and missing tests.
   - Build, benchmark, and experiment scripts.
   - Existing architecture decisions and conventions.
5. For GPU code, also map kernels, launch sites, memory allocation/transfer sites, precision handling, and profiling tools.
6. For quantum/QEC code, also map circuit construction, stabilizer/code definitions, noise models, decoder configuration, simulation loops, metrics, seeds, and result aggregation.
7. Stop inspection when the relevant behavior, constraints, and verification path are clear. Use a report for substantial recon; a small fix needs only its local context.

## Output

Use `templates/recon-report.md` for substantial recon. Reference exact files and evidence. Mark inferred items as inferred.

## Utility

`scripts/repo_snapshot.py` can summarize a repository tree while excluding common build and dependency directories.
