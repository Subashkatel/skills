# Classical Architecture Checklist

## Before proposing

- Which files and tests were inspected?
- What concepts currently own state and behavior?
- What change is expensive or likely to recur?
- What quality attributes matter most?

## Boundary questions

- Does this boundary protect a real difference in change rate?
- Does it make data flow easier to see?
- Does it reduce duplication without hiding semantics?
- Does it have a clear test seam?
- Can the simpler direct version work first?

## Readability questions

- Are names domain-specific and non-abbreviated?
- Does each meaningful line do one thing?
- Are intermediate values named to explain intent?
- Are comments short and focused on non-obvious invariants?
- Did the refactor reduce copy-paste instead of spreading it?

## Evidence

- Behavior tests or golden cases.
- Numerical tolerance checks.
- Performance baselines if performance-sensitive.
- Migration or rollback path.
- ADR for durable decisions.
