---
name: reviewing-research
description: "Synthesizes papers, docs, APIs, and benchmarks into grounded assumptions, equations, limitations, implementation notes, and open questions."
---

# Reviewing Research

## Purpose

Convert research papers, specifications, and technical documentation into implementable knowledge. The output should separate what the source actually says from interpretation or design choices.

## Source-first workflow

1. Identify the research question or implementation goal.
2. Read the relevant source sections before summarizing.
3. Extract:
   - Main claims.
   - Assumptions and scope.
   - Definitions and notation.
   - Algorithms or protocols.
   - Complexity/performance claims.
   - Experimental setup.
   - Limitations and failure modes.
4. Build an implementation map:
   - Inputs and outputs.
   - Data structures.
   - Pseudocode.
   - Required libraries/tools.
   - Tests or reproduction steps.
5. Track confidence and conflicts between sources.
6. Provide citations or exact source references when the environment supports them.

## Domain emphasis

GPU docs: extract hardware assumptions, API version, profiler metrics, and tuning prerequisites.

Quantum architecture: extract layers, timing/control assumptions, hardware abstraction, IR semantics, and compiler/runtime boundaries.

QEC papers: extract code construction, noise model, decoder, metrics, threshold/logical-error claims, and reproducibility details.

## Output

Use `templates/research-implementation-brief.md`. Avoid turning a paper into vague advice; produce implementable structure and explicit uncertainty.
