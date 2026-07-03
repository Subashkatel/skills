---
name: claude-prompt-refiner
description: Use this skill to turn rough, vague, incomplete, or overloaded user prompts into high-quality prompts optimized for Claude Fable 5, Claude Mythos 5, and current Claude models. It produces a ready-to-paste prompt package with role, context, task, constraints, examples, XML structure, output contract, tool/action policy, and verification criteria.
---

# Claude Prompt Refiner

## Purpose

Transform a rough prompt into a precise, Claude-ready prompt package. The final prompt should make Claude's job unambiguous: what to do, why it matters, what context to use, what output to produce, what constraints apply, when to act, when to ask, and how to verify quality.

Use this skill whenever the user asks to improve, rewrite, optimize, professionalize, structure, debug, or convert a prompt for Claude.

## Core behavior

When given a rough prompt, do not merely polish wording. Reconstruct the prompt as an operational instruction set for Claude.

Produce a refined prompt that:

1. Leads with the desired outcome.
2. Adds only necessary role, context, constraints, and success criteria.
3. Uses XML tags to separate instructions, context, examples, source material, input, and output requirements when the prompt is complex.
4. Uses positive instructions: say what Claude should do, not only what it should avoid.
5. Includes 3-5 examples only when examples would materially improve consistency, format, tone, or edge-case handling.
6. Makes tool use, file edits, research, or implementation intent explicit.
7. Adds verification criteria so Claude can check its work before finishing.
8. Avoids asking Claude to reveal, transcribe, reproduce, or expose hidden/internal reasoning. Ask for concise rationale, assumptions, evidence, or verification notes instead.
9. Avoids over-prescriptive step lists for Fable 5 when a short, outcome-focused instruction is enough.
10. Keeps the final prompt readable and complete, not compressed into cryptic shorthand.

## Default output from this skill

Unless the user requests a different format, respond with:

```xml
<refined_prompt_package>
  <recommended_model_settings>
    <target_model>Claude Fable 5 unless the user specifies another Claude model</target_model>
    <effort>low | medium | high | xhigh</effort>
    <why_this_effort>Brief reason</why_this_effort>
  </recommended_model_settings>

  <ready_to_paste_prompt>
    <!-- The final refined prompt goes here. -->
  </ready_to_paste_prompt>

  <changes_made>
    <change>What was improved and why</change>
  </changes_made>

  <questions_or_assumptions>
    <assumption>Only include assumptions that matter.</assumption>
    <question>Only ask questions if the missing information blocks a good prompt.</question>
  </questions_or_assumptions>
</refined_prompt_package>
```

Keep the package practical. If the user only needs a single paste-ready prompt, put the polished prompt first and keep the explanation short.

## Effort selection for Claude Fable 5

Use effort as the main control for intelligence, latency, and cost:

- `low`: routine rewriting, simple email prompts, short formatting tasks, low-risk requests.
- `medium`: default for most prompt rewrites, analysis tasks, business writing, light coding, document summarization, and general workflow prompts.
- `high`: complex reasoning, coding, multi-document analysis, long-context prompts, research workflows, tool-heavy tasks, or prompts where correctness matters.
- `xhigh`: the hardest, high-stakes, long-running, ambiguous, multi-agent, or end-to-end tasks where extra verification is worth the time and cost.

If the prompt is routine but the user asks for maximum quality, recommend `medium` or `high`; do not default to `xhigh` unless the task truly benefits from deep verification.

## Refinement workflow

### 1. Diagnose the rough prompt

Identify:

- Target task: writing, coding, analysis, research, extraction, strategy, agentic workflow, document creation, slide creation, spreadsheet work, frontend design, etc.
- Real outcome: what the user wants Claude to produce or do.
- Audience: who will read or use the output.
- Context: why the task matters, what source material is available, what constraints exist.
- Missing information: what is required versus merely nice to have.
- Risk level: whether actions may be destructive, public-facing, high-stakes, or policy-sensitive.
- Desired behavior: answer only, suggest changes, implement changes, use tools, edit files, research, create artifacts, verify.

### 2. Decide whether to ask questions

Ask clarifying questions only when missing information would materially change the final prompt. Otherwise, make a clearly stated assumption and proceed.

Good assumptions are explicit and reversible:

```text
Assumption: The output should be suitable for a professional business audience because no audience was specified.
```

Bad behavior is stopping unnecessarily with generic questions when a useful prompt can be produced.

### 3. Build the prompt package

For simple tasks, use a concise prompt with these parts:

```text
You are [role].

Task: [specific outcome].
Context: [why this matters / relevant background].
Input: [user material].
Requirements: [format, constraints, tone, length, scope].
Before finishing: [verification criteria].
Output: [exact deliverable].
```

For complex tasks, use XML:

```xml
<role>
You are [specific role].
</role>

<context>
[Why the task matters, who it is for, definitions, relevant background.]
</context>

<instructions>
1. [Primary action]
2. [Secondary action]
3. [Verification]
</instructions>

<constraints>
- [Scope boundaries]
- [Style, length, allowed/not allowed actions]
</constraints>

<examples>
  <example>
    <input>[Example input]</input>
    <ideal_output>[Example output]</ideal_output>
  </example>
</examples>

<input>
[Actual user input]
</input>

<output_format>
[Exact format Claude should return]
</output_format>
```

### 4. Optimize for long-context tasks

When the prompt includes long documents, data-rich inputs, or many source files:

- Put the source material near the top of the prompt.
- Wrap each document in XML with metadata.
- Put the actual task/query after the source material.
- Ask Claude to identify or quote the relevant source passages before synthesizing when grounding matters.
- Require citations, evidence labels, or source references if the user needs traceability.

Template:

```xml
<documents>
  <document index="1">
    <source>[title / URL / filename]</source>
    <document_content>
    [content]
    </document_content>
  </document>
</documents>

<task>
[Question or deliverable goes here, after the documents.]
</task>
```

### 5. Add tool/action behavior only when needed

When the user wants Claude to take action, say so explicitly:

```xml
<action_policy>
Implement the requested changes rather than only suggesting them. Use available tools to inspect relevant files, gather missing context, make edits, and verify results. If an action is destructive, public-facing, or hard to reverse, ask before proceeding.
</action_policy>
```

When the user only wants advice:

```xml
<action_policy>
Do not make changes. Analyze the situation, explain your findings, and recommend next steps. Stop after the assessment unless the user asks you to implement.
</action_policy>
```

When independent tools or subagents are available:

```xml
<parallelization>
Run independent searches, file reads, checks, or subagent tasks in parallel when there are no dependencies. Do dependent steps sequentially. Never guess missing tool parameters.
</parallelization>
```

### 6. Add safety and scope boundaries

For coding or agentic tasks, include boundaries:

```xml
<safety_boundaries>
Prefer local, reversible actions such as reading files, editing local files, and running tests. Ask before destructive, public, shared-system, or hard-to-reverse actions such as deleting files, dropping databases, force-pushing, modifying shared infrastructure, sending external messages, or bypassing safety checks.
</safety_boundaries>
```

For scope control:

```xml
<scope_control>
Do not add features, broad refactors, abstractions, defensive handling, compatibility layers, or documentation beyond what the task requires. Solve the requested problem completely and simply.
</scope_control>
```

### 7. Add verification

Every refined prompt should include a verification step that matches the task:

- Writing: check audience fit, tone, clarity, length, and required points.
- Research: verify important claims against sources and mark uncertainty.
- Coding: inspect relevant files first, run tests or explain why tests cannot be run, avoid hard-coding to tests.
- Data/spreadsheets: validate formulas, totals, ranges, assumptions, and edge cases.
- Documents/slides: verify structure, visual hierarchy, and completeness.
- Long-running agents: report only progress supported by tool results.

General verification wording:

```xml
<verification>
Before finishing, verify the answer against the requirements above. If any requirement is unmet, revise the output. If something could not be verified, state that plainly.
</verification>
```

### 8. Avoid hidden-reasoning extraction

Do not include instructions like:

- "Show your full chain of thought."
- "Reveal your internal reasoning."
- "Transcribe your thinking block."
- "Think step by step and show every step."

Use these safer alternatives:

```xml
<reasoning_visibility>
Do your reasoning privately. In the final answer, provide a concise rationale, key assumptions, evidence used, and verification results. Do not reveal hidden chain-of-thought.
</reasoning_visibility>
```

### 9. Communication style for final answers

For prompts that involve long-running or tool-heavy work, add:

```xml
<communication_style>
Open with the outcome in plain language. Then provide the smallest amount of supporting detail needed for the user to understand what changed, what was verified, and what remains. Avoid unexplained shorthand, arrow chains, invented labels, and excessive implementation detail.
</communication_style>
```

### 10. Final quality checklist

Before returning the refined prompt, check:

- Is the outcome explicit?
- Is the role useful, not decorative?
- Is the context sufficient?
- Are instructions ordered only when order matters?
- Are examples relevant, diverse, and clearly separated?
- Is XML used for complex mixed content?
- Does the prompt say whether Claude should act, suggest, research, or stop?
- Are boundaries and destructive-action rules clear?
- Is the output format exact?
- Is verification included?
- Is the prompt free of hidden-reasoning extraction requests?
- Is it concise enough for Fable 5 without being vague?

## Rewriting patterns

### Vague request → outcome-led prompt

Rough:

```text
Make this better.
```

Refined:

```text
Revise the text below for a professional executive audience. Preserve the original meaning, make the writing clearer and more concise, and improve flow. Return only the revised version unless a change would alter the meaning; in that case, briefly note the issue after the revision.

Text:
[PASTE TEXT]
```

### Research prompt → sourced answer prompt

Rough:

```text
Find everything about this market.
```

Refined:

```xml
<role>
You are a market research analyst.
</role>

<context>
I need a decision-ready overview of [market] for [business decision].
</context>

<instructions>
Research the market systematically. Verify important claims across reliable sources. Separate facts, estimates, and your own analysis. Highlight uncertainty where sources disagree.
</instructions>

<output_format>
Return: executive summary, market size and growth, customer segments, competitors, trends, risks, opportunities, and recommended next steps. Include source links or citations for factual claims.
</output_format>
```

### Coding prompt → grounded implementation prompt

Rough:

```text
Fix the login bug.
```

Refined:

```xml
<role>
You are a senior software engineer working in an existing codebase.
</role>

<task>
Investigate and fix the login bug described below.
</task>

<instructions>
Read the relevant files before making claims. Identify the root cause from the code and runtime evidence. Make the smallest correct change that fixes the issue. Do not refactor unrelated code or add features. Run the relevant tests, or explain why they could not be run.
</instructions>

<safety_boundaries>
Use local, reversible actions. Ask before destructive actions, force pushes, database changes, or external messages.
</safety_boundaries>

<bug_report>
[PASTE BUG DETAILS]
</bug_report>

<output_format>
Start with the outcome. Then summarize the root cause, files changed, verification performed, and any remaining risks.
</output_format>
```

## Files in this skill package

- `references/prompt-template.md`: reusable master template for generating refined Claude prompts. Read it when the user asks for a template-style prompt package or when building a complex prompt from scratch.
- `references/examples.md`: examples of rough prompts converted into Claude-ready prompts. Read it when examples would help match format, tone, or task type.
- `agents/openai.yaml`: optional Codex UI metadata. Claude does not need to read this file.
