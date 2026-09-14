# decsim style and contract checks

Read `STYLE.md` in the active decsim worktree. Resolve it from that worktree,
not a fixed checkout path. Read `docs/explanation/decisions.md` for a modeling
or architecture change, and use `tools/check.sh` for the configured checks.
These rules are decsim-specific. The local files remain authoritative.

## One action and meaningful size

- A line calls one function, performs one arithmetic step, or makes one decision.
  Attribute/index walks on named values are fine; split a call result before
  indexing, accessing an attribute, or calling another method on it.
- Split nested calls, computations in arguments, inline conditionals, calls in
  f-strings, and mixed or long Boolean expressions as the checker requires.
- The built-ins allowed inside arguments or f-strings are defined in local
  `STYLE.md`. Read that list instead of assuming all pure helpers are exempt.
  A simple predicate may remain in a condition when hoisting gives no honest name.
- Six constructor attributes and 40 function lines are review reports, not hard
  failures in the inspected version. Split by responsibility, never to game a cap.
  Deeper-than-two block nesting is a failure. Recheck the active checker version.
- The named wide-class exemptions live in `STYLE.md`, which the checker reads.
  Preserve their rationale and avoid copying a stale class list into this skill.
- A measured hot-path exception needs the local rule's evidence and explanation.
  Readability growth is acceptable; extra concepts need a real responsibility.

## Names, comments, and boundaries

- Use full words, action names, and explicit units/counts. The local acronym list
  is narrow. Mathematical short names need the paper and equation in the
  function's docstring; tiny scope alone does not grant an exception in decsim.
- Comments state a present-tense invariant and consequence, source, or design
  reason. Keep finding IDs, dates, review rounds, defect stories, and report
  references out of production and test code. Put history in reports/commits.
- Keep API contracts complete: units, errors, lifecycle, scope and claim limits
  must survive pruning. A short comment preference does not justify deleting them.
- External invalid inputs raise `ValueError`; caller contract violations that
  risk a silent wrong result raise `RuntimeError`; internal maintained invariants
  use assertions. Do not add checks or tests for unreachable internal inputs.
- Renames migrate callers together, without compatibility aliases. Preserve
  research baselines whose purpose is documented even if usage counts are small.
- Apply the active Python/version/import rules and local formatter/linter config.

## Structure, verification, and commits

- Components own state and settings and talk through named ports. Shared records
  have one owner; observers use callbacks. Enforce the local dependency and
  plug-in recognition checks without turning them into universal language rules.
- Test public laws with real referents when available. Goldens characterize
  behavior and can pin bugs; a source-backed correction determines the law.
- A worktree has its own rules and code. Verify the imported `decsim.__file__`
  points there before accepting results from another checkout's interpreter.
- Follow local commit evidence requirements, including size and gate timing
  where required. Keep each commit focused on one defect or coherent behavior.
  Commit locally, without attribution trailers; never push or merge without approval.
