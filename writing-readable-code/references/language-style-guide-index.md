# Language style-guide index

Use repository-local style first. When the project does not define style, pick the language-specific guide that matches the codebase and toolchain. For languages not listed here, search the current language documentation or the awesome-guidelines index before broad edits.

## Recommended defaults

- Python: Python Guide, Google Python Style Guide, PEP 8, PEP 257.
- C++ / CUDA host code: project style, then Google C++ Style Guide or C++ Core Guidelines; for LLVM-like projects, use LLVM Coding Standards.
- CUDA/HIP kernels: project kernel style plus readable host/device naming. Spell out `thread_index`, `block_index`, `element_index`, `row_index`, `column_index`, `shared_memory_tile`, and `launch_configuration` unless a local convention says otherwise.
- C: project style, Linux/GNU/Mozilla style only when that matches the repository.
- Rust: Rust API Guidelines and `rustfmt` conventions.
- Go: Effective Go, Go Code Review Comments, and `gofmt`.
- Java: Google Java Style Guide unless the repo has another convention.
- TypeScript/JavaScript: project ESLint/Prettier rules first, then Google or Airbnb style only when compatible with the repo.
- Shell: ShellCheck guidance plus project conventions.
- SQL: project SQL formatter/style, then a clear SQL style guide.

## Cross-language readability contract

- Names should be readable in a code review without a glossary.
- The length of a name should grow with its scope and ambiguity.
- One declaration per line when declarations are not trivial.
- One meaningful action per line when expression nesting obscures intent.
- Avoid magic constants; name them by role and unit.
- Keep scopes small and initialize values close to use.
- Prefer fewer abstractions with better names over many thin wrappers.
- Do not invent a new local style in one file.
