# Git Notes Memory Reference

Git notes are useful because they attach durable context to commits without changing the commit diff. Use them for rationale and evidence that future agents should see, not for generated summaries of the code itself.

## Good note

[CODEX:abc123] Chose a bounded syndrome FIFO instead of a global event list because detector events are consumed in time order and the benchmark showed allocator overhead dominating. Verified with qec-experiments.json case surface_d5_p001 and tests/test_decoder_fifo.py. Open hypothesis: capacity may need adjustment for biased noise.

## Bad note

Changed decoder.py and added tests. Next: maybe optimize more.

The bad note repeats the diff and gives no rationale, evidence, or constraint.

## What belongs in state files instead

Use `implementation-notes.md` for in-progress deviations, `progress.md` for task status, `tests.json` for structured test results, `performance-log.md` for benchmark runs, and `qec-experiments.json` for simulation settings and outcomes. Use git notes at stable boundaries.
