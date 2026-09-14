---
name: refining-prompts
description: "Rewrite a rough prompt for a coding agent or for Claude, with scope and completion criteria. Not for executing a clear task."
---

# Refining Prompts

Turn rough prompts into precise prompts for Claude Code, Codex, or another
coding agent. The output should help the agent act like a careful technical
collaborator, not a generic assistant, and it should be an operational
instruction set, not a polished paraphrase.

## Process

1. Identify the real deliverable: architecture review, code edit, kernel optimization, QEC experiment, research synthesis, verification, or explanation.
2. Add the reason for the request so the target agent can connect details to intent.
3. Add domain constraints:
   - Architecture: quality attributes, scope, constraints, ADR needs.
   - GPU: target hardware, programming stack, precision, data layout, benchmark protocol.
   - Quantum architecture: layer, hardware assumptions, circuit IR, ISA, transpilation, decoder latency.
   - QEC: code family, distance, schedule, noise model, decoder, metrics.
4. Add an unknowns step before implementation when ambiguity could change the solution.
5. Require evidence: files read, tests, profiler output, algebra checks, simulations, citations, or benchmark logs.
6. Specify whether the target agent should only advise, inspect files, edit code, or run experiments.
7. Preserve the user's chosen model, authorization, and completion boundary. Do not add mandatory document stacks or stop-for-review gates. Avoid instructions that request hidden reasoning. Ask for concise rationale, assumptions, checks, and evidence instead.

## Output

Return the paste-ready prompt first. Use `templates/refined-prompt-package.md` only when a full package is requested. Include only useful items:

- Recommended skills.
- Model or effort settings only if requested and supported by the target environment.
- Final prompt.
- Assumptions.
- Questions only if the prompt cannot be made safe without answers.

`reference/prompt-refinement-playbook.md` holds the longer playbook.

## Prompts written for Claude

Use this section when the user asks to improve, rewrite, optimize,
professionalize, structure, debug, or convert a prompt explicitly for Claude.

Produce a refined prompt that:

- Opens with the desired outcome.
- Adds only useful role, context, constraints, source material, and success criteria.
- Uses XML tags when the prompt mixes instructions, documents, examples, or output contracts.
- States whether Claude should answer, research, edit files, use tools, or stop after analysis.
- Includes examples only when they improve format, tone, or edge-case handling.
- Uses positive instructions and clear boundaries.
- Asks Claude to reason privately and report concise rationale, assumptions, evidence, and verification notes.
- Ends with a concrete output contract and verification step.

### Claude workflow

1. Diagnose the real task: writing, coding, research, extraction, strategy, documents, slides, spreadsheets, frontend design, or agentic work.
2. Identify audience, source material, action level, missing information, risk, and desired output.
3. Ask questions only when missing information materially changes the prompt. Otherwise state reversible assumptions.
4. Choose a concise text prompt for simple tasks and XML for complex mixed-content tasks.
5. Add safety boundaries for destructive, public, shared-system, or hard-to-reverse actions.
6. Add verification criteria that match the domain.

Return the ready-to-paste prompt first, with only material assumptions
afterward. Use `reference/prompt-template.md` for an explicitly requested full
package and `reference/examples.md` when examples would help match format, tone,
or task type. Preserve the requested model and effort. Suggest settings only
when asked and when supported by the target interface; do not invent
cross-provider effort names. Define completion through the requested artifact
and useful checks. Do not add mandatory document stacks, generic role play, or
extra approval gates. Existing authorization remains valid throughout the work.

### Prompt skeletons

Simple prompt:

```text
You are [role].

Task: [specific outcome].
Context: [audience, goal, background].
Input: [material].
Requirements: [constraints, tone, format, scope].
Before finishing: verify [criteria].
Output: [exact deliverable].
```

Complex prompt:

```xml
<role>[Specific useful role]</role>
<context>[Audience, goal, background, definitions]</context>
<source_material>[Documents, data, examples, or user material]</source_material>
<task>[Exact outcome or action]</task>
<instructions>[Ordered steps only when order matters]</instructions>
<constraints>[Scope, style, length, allowed and disallowed actions]</constraints>
<action_policy>[Answer only, suggest only, implement, research, use tools, ask before risky actions]</action_policy>
<verification>[Checks Claude should perform before finalizing]</verification>
<output_format>[Exact structure to return]</output_format>
```

`agents/openai.yaml` is Codex UI metadata. Claude does not need to read it.
