---
name: claude-prompt-refiner
description: "Refines rough, vague, incomplete, or overloaded prompts into clear Claude-ready prompt packages with role, context, task, constraints, examples, output format, tool policy, and verification criteria."
---

# Claude Prompt Refiner

Use this skill when the user asks to improve, rewrite, optimize, professionalize, structure, debug, or convert a prompt for Claude.

## Core behavior

Turn the rough prompt into an operational instruction set, not a polished paraphrase.

Produce a refined prompt that:

- Opens with the desired outcome.
- Adds only useful role, context, constraints, source material, and success criteria.
- Uses XML tags when the prompt mixes instructions, documents, examples, or output contracts.
- States whether Claude should answer, research, edit files, use tools, or stop after analysis.
- Includes examples only when they improve format, tone, or edge-case handling.
- Uses positive instructions and clear boundaries.
- Asks Claude to reason privately and report concise rationale, assumptions, evidence, and verification notes.
- Ends with a concrete output contract and verification step.

## Workflow

1. Diagnose the real task: writing, coding, research, extraction, strategy, documents, slides, spreadsheets, frontend design, or agentic work.
2. Identify audience, source material, action level, missing information, risk, and desired output.
3. Ask questions only when missing information materially changes the prompt. Otherwise state reversible assumptions.
4. Choose a concise text prompt for simple tasks and XML for complex mixed-content tasks.
5. Add safety boundaries for destructive, public, shared-system, or hard-to-reverse actions.
6. Add verification criteria that match the domain.

## Default output

Unless the user requests another format, return:

```xml
<refined_prompt_package>
  <recommended_model_settings>
    <target_model>Claude model specified by the user, or the user's default Claude model</target_model>
    <effort>low | medium | high | xhigh</effort>
    <why_this_effort>Brief reason</why_this_effort>
  </recommended_model_settings>

  <ready_to_paste_prompt>
    <!-- Final refined prompt. -->
  </ready_to_paste_prompt>

  <changes_made>
    <change>What improved and why</change>
  </changes_made>

  <questions_or_assumptions>
    <assumption>Only include material assumptions.</assumption>
    <question>Only include blockers.</question>
  </questions_or_assumptions>
</refined_prompt_package>
```

For users who only need a paste-ready prompt, put the prompt first and keep explanation short.

## Effort guidance

- `low`: routine rewriting, simple emails, formatting, low-risk tasks.
- `medium`: default for prompt rewrites, analysis, business writing, light coding, and summaries.
- `high`: complex reasoning, coding, long-context analysis, research, tool-heavy tasks, or correctness-sensitive work.
- `xhigh`: high-stakes, ambiguous, multi-agent, long-running, or end-to-end tasks where extra verification is worth the cost.

## Prompt skeletons

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

## Support files

- `references/prompt-template.md`: read when building a complex prompt package from scratch.
- `references/examples.md`: read when examples would help match format, tone, or task type.
- `agents/openai.yaml`: Codex UI metadata. Claude does not need to read this file.
