---
name: writing-readable-code
description: "Enforces clean readable code for new work and refactors: descriptive names, no abbreviations, one clear action per line, useful comments, and low bloat."
---

# Writing Readable Code

Use this skill whenever you write, edit, review, or refactor code. The goal is code that a careful reader can understand without decoding abbreviations, hidden side effects, clever expression chains, or copy-pasted variants.

## Readability contract

1. **Every line does one clear thing.** Avoid dense lines that call multiple functions, index into the result, transform it again, and branch on it. Split them into named intermediate values.
2. **Use intermediate variables as documentation.** Prefer `window_manager = self.window_manager`, `decoded_observable_count = len(decoded_observables)`, and `syndrome_column = syndrome_matrix[:, detector_index]` over abbreviation or expression nesting.
3. **No unexplained abbreviations.** Names must say what the thing is or does. Avoid `c`, `cnt`, `cou`, `wm`, `cfg`, `arr`, `buf`, `tmp`, `res`, `val`, `obj`, `ctx`, and similar shortcuts unless the project has a strong local convention and the scope is tiny. When in doubt, spell it out.
4. **Names reflect role, not vague type.** Prefer `detector_error_probability`, `logical_observable_index`, `window_manager`, `sample_count`, and `launch_configuration` over `data`, `item`, `manager`, `dict`, or `result` when the role is known.
5. **No copy-paste blocks.** If two blocks are the same concept, create one clear owner. If they differ in meaningful scientific semantics, keep them separate and name the distinction explicitly.
6. **Comments explain why, not what.** Add short comments or docstrings for invariants, units, coordinate frames, memory layout, numerical tolerance, noise model, decoder assumption, QPU backend constraint, hardware constraint, or non-obvious performance tradeoff. Do not narrate obvious syntax.
7. **Prefer simple control flow.** Use guard clauses, small scopes, and named predicates. Avoid deeply nested conditionals, multi-purpose variables, and clever one-liners.
8. **Refactoring must follow the same contract.** When asked to refactor existing code, improve names, break dense expressions, remove copy-paste, and preserve behavior with tests. Do not make unrelated style sweeps unless requested.

## Language guide policy

- **Project style wins first.** Read local `AGENTS.md`, `CLAUDE.md`, README, formatter config, lint config, and nearby code before choosing style.
- **Python:** follow the Python Guide, Google Python Style Guide, PEP 8, and PEP 257. Use `references/python-readable-code.md` when writing or reviewing Python.
- **C, C++, CUDA, HIP, SYCL, Triton, Rust, Go, Java, TypeScript, shell, or other languages:** use `references/language-style-guide-index.md` to pick the appropriate official or widely accepted style guide. If internet access is available and the project does not define a style, consult the current guide before making broad edits.
- **Scientific notation exception:** Short names such as `x`, `y`, `z`, `i`, `j`, `k`, `m`, `n`, or `p` are acceptable only for standard mathematical notation, tiny loop scopes, paper-matching formulas, or conventional GPU indices. Prefer descriptive variants like `row_index`, `sample_index`, `thread_index_x`, `qubit_count`, and `detector_count` when the value survives beyond a few lines.

## Workflow

1. **Inspect conventions.** Identify the language, nearby naming style, formatter, linter, test style, and domain notation.
2. **Write the boring version first.** Implement the smallest correct change with clear names and simple control flow before optimizing or abstracting.
3. **Extract intent from expressions.** Replace dense expressions with intermediate values whose names explain the computation.
4. **Name all domain facts.** In GPU/QEC/quantum code, spell out memory layout, qubit order, detector index, logical observable, precision mode, tolerance, launch configuration, and noise assumptions.
5. **Comment only non-obvious intent.** Add a short inline comment or docstring where a reader would otherwise ask “why is this safe?” or “what invariant is assumed?”
6. **Run the readability pass.** Review the changed diff for abbreviation, nested expression chains, duplicate blocks, needless abstraction, hidden state changes, and comments that restate syntax.
7. **Verify behavior.** Run the relevant tests, static checks, formatter, and scientific verification gates. Read the diff after formatting; formatters do not guarantee readability.

## Before and after examples

Bad:

```python
wm = self.window_manager
c = len(wm.active_windows())
return self.metrics.update(wm.active_windows()[self.pick(wm)])
```

Better:

```python
window_manager = self.window_manager
active_windows = window_manager.active_windows()
selected_window_index = self.pick_window_index(active_windows)
selected_window = active_windows[selected_window_index]

return self.metrics.update(selected_window)
```

Bad:

```python
if self.decoder.graph().nodes()[self.map(dets)[0]].p < tol:
    return True
```

Better:

```python
detector_ids = self.map_detectors_to_ids(detectors)
first_detector_id = detector_ids[0]
decoder_graph = self.decoder.graph()
first_detector_node = decoder_graph.nodes()[first_detector_id]

return first_detector_node.error_probability < tolerance
```

Bad comment:

```python
# Increment count.
count += 1
```

Better comment:

```python
# We count only accepted samples so the Wilson interval matches the decoder input.
accepted_sample_count += 1
```

## Performance-sensitive scientific code

Readability is still required in hot paths. If a dense construct is necessary for performance, isolate it, measure it, and add a short comment explaining the tradeoff. Prefer a clear reference implementation plus optimized implementation when GPU, SIMD, numerical, or decoder code becomes intentionally low-level.

## Done

The code is done only when it is correct, verified, minimal, and readable. A reviewer should be able to identify the purpose of each variable, understand each nontrivial line, and see why comments/docstrings exist.
