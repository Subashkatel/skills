# Claude Prompt Refiner Template

Use this template when converting a rough prompt into a Claude-ready prompt.

```xml
<role>
You are [specific expert role that genuinely helps the task].
</role>

<context>
[Explain the situation, audience, goal, why the task matters, and any background Claude needs.]
</context>

<source_material>
[Place documents, data, files, examples, or user-provided material here. For long context, put this before the task.]
</source_material>

<task>
[State the exact outcome Claude must produce or action Claude must take.]
</task>

<instructions>
1. [Step only if order matters.]
2. [Step only if order matters.]
3. [Add grounding, verification, or tool-use behavior.]
</instructions>

<constraints>
- [Scope boundaries]
- [Length]
- [Tone]
- [Allowed / disallowed actions]
- [No hidden chain-of-thought extraction]
</constraints>

<examples>
  <example>
    <input>[example input]</input>
    <ideal_output>[example output]</ideal_output>
  </example>
</examples>

<action_policy>
[Choose one: answer only / suggest only / implement changes / research with citations / use tools / ask before risky actions.]
</action_policy>

<verification>
Before finishing, check the output against the task, constraints, and success criteria. If any part is missing, revise it. State anything that could not be verified.
</verification>

<output_format>
[Exact structure Claude should return.]
</output_format>
```

## Minimal version

```text
You are [role].

Task: [specific outcome].
Context: [why it matters / audience / background].
Input: [material].
Requirements: [constraints, tone, format, scope].
Before finishing: verify [criteria].
Output: [exact deliverable].
```
