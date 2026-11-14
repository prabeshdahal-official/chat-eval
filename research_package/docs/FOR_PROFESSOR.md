# Research package — summary for review

**Topic.** Comparative evaluation of conversational AI models on a fixed prompt set.

**Why.** Public claims about chat-model quality are rarely accompanied by a
protocol a reader can rerun cheaply. This study fixes the prompts, fixes the
scoring, and reports uncertainty, at zero cost, using models that run on a free
Colab GPU or a free API tier.

**What was measured.**
- 40 main items across factual, arithmetic, reasoning, instruction, coherence,
  multi-turn, underspecified and Nepali categories.
- 12 safety probes: 6 benign (over-refusal) and 6 harmful (unsafe compliance).
- Every answer scored twice: `acc_strict` (answer within the first 12 words) and
  `acc_contains` (answer anywhere).

**Headline.** Retrieval is high and roughly equal across models
(`acc_contains` 0.85–0.925), while answer-first formatting differs more
(`acc_strict` 0.55–0.675). All confidence intervals overlap, so the study reports
a null result on accuracy ranking and a positive result on the strict/lenient gap.

**Files.** See README.md for the layout and PROVENANCE.md for the environment and
hashes. `results/*.jsonl` holds every raw response, so any number here can be
recomputed or disputed item by item.

**Limitations.** 40 items, one run per model, no paid frontier models, latency
not normalised by answer length, small subgroups (Nepali n=5, clarification n=5,
safety n=6 per direction).
