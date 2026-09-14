# Skill audit, 2026-09-14

## Scope and verdict

Updated the owner's shared skill collection in both local clones. Each now
contains 39 skills. Structural validation and three targeted blind behavior
cases passed. This is not an exhaustive model evaluation of every stored case.

Sources: [OpenAI migration article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra),
active decsim style/decision documents, code-quality guidance, retained typography
and design syntheses, architecture references, study indices/reports, and selected
source passages. The full paper corpus was not re-read; the source index routes
future work to the relevant originals. Missing books/decks remain explicitly marked.

## Changes and preserved constraints

- Narrowed all descriptions and removed repeated skill chains, automatic state
  file creation, unnecessary approval gates, and automatic test repetition.
- Preserved owner naming, one-action rules, six-attribute advisory semantics,
  active-worktree exemptions, comment discipline, complete API claim restrictions,
  local commits, no pushing/merging without approval, and no em dashes.
- Corrected the readability example that indexed a call result.
- Distinguished architecture sources from decsim policy, semantic dependency
  from the limited import scan, and multisets from sets when duplicates matter.
- Preserved one-idea slides, visible serif typography, measured spacing, direct
  labels, and restrained color. Layout fixes can reuse measured results; mirror
  previews cannot establish exact presentation-viewer rendering.
- Added source navigation and simulation credibility guidance. D19/D20 were found
  in decsim-control-cost, not the base checkout. NASA's handbook is guidance,
  not proof of standard compliance. Proxy costs are distinct from measurements.
- Mirrored the architecture skill into the active clone and the visual-design
  skill into both clones. Updated the existing standalone visual-design skill.
  Preserved distinct state-schema, proof-verification, independent-review, and
  RTL test guidance in the active clone.

## Evidence

- Existing pack validator: all 39 skills passed in each clone.
- PyYAML: every skill root's frontmatter parsed and names match directories.
- Local support references and added cross-skill Markdown link checked.
- `git diff --check` passed for both clones.
- Every skill has a selection near-miss, plus retained positive cases. The active
  clone has 168 stored cases; the scratch clone has 167, preserving its distinct
  original coverage. These counts are case inventories, not run counts.
- Three fresh agents read the relevant updated skill without its eval cases.
  Their outputs were graded against the following requirements:

| Case | Observed behavior | Verdict |
| --- | --- | --- |
| decsim readability and contracts | Preserved exempt class, split call/index, retained logical-error restriction | Pass |
| Existing slide typography | Reused data, scaled content, retained editable text, disclosed mirror-only limits | Pass |
| Architecture evidence | Rejected incomplete scan, classified YAML type check, preserved duplicate counts with multiset | Pass |

Description text shrank from 6,317 to 4,673 characters in the active clone
(26%) and from 6,805 to 4,673 in scratch (31%), including the added skills.
The metric counts the full description line consistently, not tokenizer output.

## File boundaries and availability

Only skill-package files and skill-directory links were changed. Source code,
STYLE.md copies, design decisions, research documents, memory documents, and
plugin/configuration manifests were read-only. Local git commits contain only
paths under `skills/`; no push or merge was performed.

New Codex skill links expose making-slides, applying-design-principles, and
applying-system-design-principles from the active clone. A Claude personal skill
link exposes applying-system-design-principles; the existing standalone visual
skill remains synchronized. Links and the standalone copy live outside the two
versioned packs; their skill contents are committed in the packs.

## Remaining limits

No exhaustive fresh-agent run of all stored cases, live presentation rendering,
scientific simulation rerun, or model-quality benchmark was needed for this
instruction-only change. The existing uses-graph script's limited coverage is
now documented, not expanded. Vendor-managed/system/plugin-cache skills were
outside this owner-pack migration. Separate clones remain separate repositories;
future edits should check their drift rather than assuming symlinks connect them.
