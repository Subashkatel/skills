---
name: reviewing-research
description: "Read papers or technical sources to assess a claim, reproduce a method, or inform an implementation."
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
6. Cite title/version and the exact supporting section or page. Preserve units, conditions, and distinctions between measurement, proxy, proposal, and implementation. Treat missing corpus evidence as a search limit.

## Domain emphasis

GPU docs: extract hardware assumptions, API version, profiler metrics, and tuning prerequisites.

Quantum architecture: extract layers, timing/control assumptions, hardware abstraction, IR semantics, and compiler/runtime boundaries.

QEC papers: extract code construction, noise model, decoder, metrics, threshold/logical-error claims, and reproducibility details.

## Output

Use `templates/research-implementation-brief.md`. Avoid turning a paper into vague advice; produce implementable structure and explicit uncertainty.

## Source routes

For decsim or the owner's architecture study, use
`references/owner-source-index.md` to find the relevant local source. For
calibration, uncertainty, or validation claims, use the
[scientific credibility reference](../../quality/verifying-scientific-code/references/source-credibility.md).
The index is navigation, not a reading checklist or proof of a claim.
