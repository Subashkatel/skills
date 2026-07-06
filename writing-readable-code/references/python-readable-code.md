# Python readable-code reference

Use this reference when writing or refactoring Python.

## Source hierarchy

1. Repository-local style and formatter/linter configuration.
2. Python Guide: emphasizes readability, explicit code, one statement per line, and Pythonic idioms.
3. Google Python Style Guide: naming, comments, docstrings, import layout, line length, and maintainability.
4. PEP 8 and PEP 257 for baseline Python conventions.

## Practical rules

- Prefer explicit parameters, explicit return values, and straightforward control flow.
- Put one statement per line. Split complex conditions into named booleans.
- Use descriptive names and avoid deleting letters inside words.
- Use `snake_case` for functions, methods, variables, and parameters; `ClassName` for classes; `UPPER_SNAKE_CASE` for constants unless the project differs.
- Use docstrings for public modules, classes, functions, and methods when the signature/name is not enough. Keep one-line docstrings short.
- Use comments for tricky intent, invariants, and why something is safe; do not describe obvious Python syntax.
- Keep imports at the top, grouped and sorted according to the project’s style.
- Favor named intermediate values over expression chains.
- Prefer standard tools already configured in the project: `ruff`, `black`, `pyright`, `mypy`, `pylint`, `pycodestyle`, or project-specific checks.

## Naming examples

Use `count`, not `c`; `window_manager`, not `wm`; `configuration`, not `cfg`; `detector_error_probability`, not `p` unless the code is a direct transcription of a paper equation and the scope is tiny.

## Comments and docstrings

A comment or docstring should answer at least one of these questions:

- What contract does this function expose?
- What unit, coordinate frame, precision, noise model, or ordering is assumed?
- Why is this branch safe?
- Why is this implementation intentionally different from the obvious one?
- What external behavior must remain stable?

Delete comments that only restate the next line.
