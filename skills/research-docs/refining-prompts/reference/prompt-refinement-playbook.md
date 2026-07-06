# Prompt refinement playbook

## Minimal technical prompt structure

```xml
<task>
What should the target agent do?
</task>

<context>
Why this matters, who will use it, and what constraints apply.
</context>

<sources>
Files, papers, logs, profiler outputs, or references the target agent must inspect.
</sources>

<requirements>
Functional, performance, correctness, architecture, and research requirements.
</requirements>

<verification>
How the target agent should prove the result is correct or be honest about uncertainty.
</verification>

<deliverable>
Exact output format and whether to edit files, propose a plan, or ask questions.
</deliverable>
```

## Domain-specific additions

GPU: target GPU, CUDA/HIP/SYCL/Triton version, data sizes, precision, baseline, profiler, tolerance.

QEC: code, distance, boundaries, schedule, noise model, decoder, logical observables, sampling shots, confidence interval.

Architecture: quality attributes, runtime scenarios, deployment, constraints, ADRs, non-goals.
