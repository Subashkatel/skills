# Scientific source and model credibility

Use the applicable checks for source-derived laws, calibrated costs, or scientific
claims. Ordinary naming or layout changes do not require this entire review.

## Source fidelity

- Verify title, identifier, revision, and relevant page/section. Keep a short
  passage locator: extracted line numbers are specific to that extraction.
- Separate source observation, interpretation, modeling assumption, proposed
  design, and implemented behavior. A design report does not establish code behavior.
- Preserve quantity and conditions: one-way or round-trip, per-window or per-round,
  latency or throughput, maximum or percentile, units, clock, hardware generation,
  precision, code parameters, and workload.
- Label vendor projections, competitor estimates, aggregate peaks, independent
  measurements, and host-clock samples separately.
- State transferred assumptions. Pricing a decoder hop from a cache access is a
  surrogate model, not a measured QEC hop. Vary consequential proxies in sensitivity
  checks; do not omit uncertainty because a source supplies a precise number.
- A corpus search establishes only what was found in that corpus. Missing
  measurements do not prove physical impossibility or a universal zero-cost law.
- For figure-only evidence, inspect the rendered page. Text extraction can omit
  values, mix columns, or lose units.

## Simulation credibility

Start with intended use, the decision being supported, and acceptance criteria.
Distinguish verification of the implementation from validation of the model
against empirical evidence. Record input and development-data pedigree, the
validation domain, material assumptions, uncertainty, sensitivity, and exclusions.
Assess both the model and the particular result; separate epistemic uncertainty
from stochastic variability where the distinction affects the decision.

The local source is NASA-HDBK-7009B, implementation guidance for NASA-STD-7009B:
section 4.5.1 (provenance), section 4.7 (software/model validation), Appendix D
(credibility and robustness). The inspected file's cover is approved 2026-02-03
and some body headers still say DRAFT; preserve that edition detail when citing.
Use the handbook to select evidence proportional to intended use and consequence.
Completing these checks does not establish compliance with the NASA standard.

Keep evidence in the existing report or task record, with commands, data/version
identifiers, and limitations needed to reproduce the claim. An oracle derived
from the production calculation checks consistency, not independent correctness.
