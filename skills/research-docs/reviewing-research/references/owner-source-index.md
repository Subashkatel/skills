# Owner research sources, navigation only

Use this index for decsim architecture, decoder research, or validation work.
It records the owner's collection as inspected on 2026-09-14; verify availability
and revision before citing. These files are references, not permission to edit
their repositories. Read the relevant passage, not the entire collection.

Collection root: `/scratch/gpfs/MARTONOSI/sk2415/qlx-qec-sandbox`.
Paths below are relative to that root unless specified otherwise.

| Question | Start here | Source to verify |
| --- | --- | --- |
| Style/checker behavior | Active decsim worktree `STYLE.md` | Its `tools/check_one_action.py` and `tools/check.sh` |
| Modeling decisions | Active worktree `docs/explanation/decisions.md` | The cited paper, implementation, and section |
| Comments and contract completeness | `tmp/research_agent_prompts/common/code-quality.md` | Comments section and `common/rubrics/code-quality.md` |
| Abstraction and dependencies | `docs/rewrite/design_audit/notes/17_architecture_principles.md` | `tmp/papers/architecture/` |
| Classical scheduling, queues, ownership | Relevant decision or study report | `tmp/papers/txt/`, named below |
| QEC and decoder evidence | `tmp/architecture-study/owner_review/README.md` | `owner_review/papers/`, `tmp/papers/txt/`, and rendered `owner_review/figures/paper_pages/` |
| Vendor architecture | `tmp/architecture-study/owner_review/papers/vendors/SOURCES.md` and `R3_vendor_architectures.md` in the study directory | The named vendor file and hardware generation |
| Control-hop costs | `tmp/architecture-study/R11_control_hop_costs.md`, `D5_control_hop.md` | Cited measurement; distinguish a proxy from the measured quantity |
| System placement and proposal | Design-audit notes 07, 30, 32, 33, 34, 35 | Use the actual filenames in `docs/rewrite/design_audit/notes/` |
| Simulation credibility | `NASA-HDBK-7009B_Final 02-03-2026.pdf` | Handbook sections and intended use; it is not NASA-STD-7009B |
| Owner intent | `Decoder Switching Ideas.pdf`, `decsim draft.pdf` | Draft text, distinguished from measured or implemented claims |
| Backline | `resources/backline-whitepaper.pdf`, `resources/2609.09270v1.pdf` | Document title, version, path and measured setup |

## Worktrees and changing decisions

Use `git worktree list` and resolve the target checkout before applying rules.
The inspected base decsim had D1-D18; `decsim-control-cost` had D19 (control
message distance) and D20 (central or per-chip dispatch). Other worktrees had
fewer decisions. Do not synthesize missing decisions or import another tree's
rules silently. Each worktree's `STYLE.md` is its own authority.

## Architecture and classical text routes

The architecture corpus contains Parnas, Dijkstra, Lampson, Conway, Brooks,
gem5, Hyrum, Foote/Yoder, and Waldo in extracted text. Ousterhout CS190 notes
and a talk are present, as is Saltzer chapter 1; these are not the full books.

For classical referents, use the cited file in `tmp/papers/txt/`:

- Work distribution: `cilk5-pldi1998.txt`, `blumofe-leiserson-workstealing.txt`,
  `lea-forkjoin-2000.txt`, `starpu_ccpe2011.txt`, `realm_pact2014.txt`,
  `legion_sc2012.txt`, `omp_exec.txt`, `cuda_guide.txt`.
- Queues and synchronization: `brun_garcia_2000_md1k.txt`,
  `mellor-crummey-scott-tocs1991.txt`, `tomasulo-1967.txt`, `cfs.txt`, `eevdf.txt`.
- Transport and energy: `am-isca92.txt`, `kalia_atc16_rdma.txt`,
  `chu_zerocopy_1996.txt`, `zerocopy_atc12.txt`, `dally_towles_dac2001.txt`,
  `horowitz_isscc2014.txt`, `backline-whitepaper.txt`.
- Frame and feedback: `riesebos_dac2017.txt`, `ionq_ecdsa_2026.txt`,
  `quant-ph_0110143.txt`, plus the QEC study's paper index.

Other listed papers and source files are found through the decision's citation
or the study index. A filename list is navigation evidence, not proof its contents
were verified. Never turn a numerical example into a universal hardware constant.

## Typography and visual sources

The original Bringhurst, Wickstrom, Lidwell books and Judy Fan/Dally example decks
were removed from the indexed collection. Their surviving syntheses live in the
`making-slides/references/typography.md`, `making-slides/references/build-pattern.md`,
and `applying-design-principles/references/universal-principles.md` skill packages.
Use them as distilled owner preferences; do not claim to have read unavailable originals.
