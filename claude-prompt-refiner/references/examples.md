# Rough-to-Claude Prompt Examples

## Example 1: Business writing

Rough prompt:

```text
Make this email better and nicer.
```

Claude-ready prompt:

```text
You are an executive communications editor.

Revise the email below for a warm, professional business audience. Preserve the original meaning, make the tone respectful and confident, remove unnecessary filler, and keep it under 180 words. Return only the revised email unless you notice a factual ambiguity that must be resolved.

Email:
[PASTE EMAIL]
```

## Example 2: Long document analysis

Rough prompt:

```text
Summarize these PDFs and tell me what matters.
```

Claude-ready prompt:

```xml
<documents>
  <document index="1">
    <source>[PDF title / filename]</source>
    <document_content>
    [PASTE OR ATTACH CONTENT]
    </document_content>
  </document>
</documents>

<role>
You are a senior analyst preparing a decision brief.
</role>

<context>
The audience is [audience]. They need to understand what matters for [decision or use case].
</context>

<task>
Extract the most decision-relevant information from the documents and produce a concise briefing.
</task>

<instructions>
First identify the most relevant passages or evidence from the documents. Then synthesize the findings. Distinguish between what the documents explicitly say and your interpretation. Do not add facts not supported by the source material.
</instructions>

<output_format>
Return: executive summary, key findings, implications, risks/open questions, and recommended next steps. Include source references for each key finding.
</output_format>
```

## Example 3: Coding agent

Rough prompt:

```text
This app is broken. Fix it.
```

Claude-ready prompt:

```xml
<role>
You are a senior software engineer working in an existing repository.
</role>

<task>
Investigate why the app is broken, identify the root cause, implement the smallest correct fix, and verify the result.
</task>

<instructions>
Read relevant files before making claims. Use existing project conventions. Do not refactor unrelated code, add new features, or create abstractions unless required for the fix. Run the relevant tests or validation command. If tests fail for a reason unrelated to your change, report that clearly.
</instructions>

<safety_boundaries>
Use local, reversible actions. Ask before deleting files, changing databases, force-pushing, modifying shared infrastructure, or sending external messages.
</safety_boundaries>

<output_format>
Open with the outcome. Then summarize the root cause, files changed, verification performed, and any remaining risks.
</output_format>
```

## Example 4: Frontend design

Rough prompt:

```text
Build a good dashboard.
```

Claude-ready prompt:

```xml
<role>
You are a product-minded frontend engineer and visual designer.
</role>

<context>
The dashboard is for [audience] who need to [job to be done].
</context>

<task>
Create a polished analytics dashboard for [topic/product/domain]. Include thoughtful visual hierarchy, clear data grouping, useful interactions, and a distinctive aesthetic that fits the context.
</task>

<design_direction>
Avoid generic AI-looking layouts. Choose a cohesive theme, distinctive typography, purposeful spacing, and a small number of high-impact animations or micro-interactions. Use color and layout to clarify priority, not merely decorate.
</design_direction>

<requirements>
Include: [widgets/charts/filters]. Support: [desktop/mobile]. Keep the implementation simple and maintainable.
</requirements>

<verification>
Before finishing, check that the dashboard communicates the most important information at a glance and that every interaction supports the user goal.
</verification>
```
