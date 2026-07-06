---
name: recon-codebases
description: "Inspects repositories before codebase claims or edits. Use when work depends on existing files, tests, build scripts, APIs, architecture, or conventions."
---

# Recon Codebases

## Rule

Do not make confident claims about code that has not been inspected. Before architecture, performance, or QEC implementation work, gather a map of the relevant files, tests, build commands, data flows, and conventions.

## Recon workflow

1. Identify the requested change or question.
2. Locate relevant files using directory listing, search, imports, tests, build scripts, and docs.
3. Read the files that determine behavior, not only files whose names look relevant.
4. Map:
   - Entry points.
   - Core modules and ownership boundaries.
   - Runtime/data flow.
   - Test coverage and missing tests.
   - Build, benchmark, and experiment scripts.
   - Existing architecture decisions and conventions.
5. For GPU code, also map kernels, launch sites, memory allocation/transfer sites, precision handling, and profiling tools.
6. For quantum/QEC code, also map circuit construction, stabilizer/code definitions, noise models, decoder configuration, simulation loops, metrics, seeds, and result aggregation.
7. Produce a grounded recon report before proposing changes.

## Output

Use `templates/recon-report.md` for substantial recon. Reference exact files and evidence. Mark inferred items as inferred.

## Utility

`scripts/repo_snapshot.py` can summarize a repository tree while excluding common build and dependency directories.
