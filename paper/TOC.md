# Paper structure — “Chatting with AI Models”

A publication-ready table of contents for the measurement study behind this repository.

**Working title:** *Chatting with AI Models: A Zero-Budget, Reproducible Evaluation of Four Chat Assistants on a Fixed 52-Item Protocol*

**Form:** short measurement paper / benchmark note. Primary category `cs.AI` — the category the endorsement covers. Target 8–10 pages including references.
**Claim discipline:** the study reports a null result on ranking. Any section that would imply a winner contradicts §6.3 and must be rewritten.

**Status:** title, author block, abstract and keywords are in `front_matter.md`. The full draft, including all 11 sections and Appendices A–E, is in `main.md`.

---

## Front matter

- **Title** — as above; keep “zero-budget” and “four” in the title, they are the honest scope.
- **Authors and affiliations** — single author, independent researcher.
- **Abstract** — 180–220 words, five moves only: the problem (claims that cannot be re-run), the protocol (4 models, 52 items, 208 answers, temperature 0), the two scoring definitions, the result (retrieval 0.85–0.925 vs answer-first 0.55–0.675, intervals overlapping), the release (raw JSONL + harness, public repository).
- **Keywords** — chat model evaluation; open-weight models; reproducibility; answer-first scoring; low-resource languages; free-tier benchmarking.

---

## 1. Introduction

- **1.1 Motivation** — public model comparisons are usually unfalsifiable: prompts private, scoring invisible, run not repeatable.
- **1.2 The zero-budget constraint as a design input** — what changes when the ceiling is \$0: free Colab T4 for open-weight models, free API tier for one hosted model. Constraint stated as method, not apology.
- **1.3 Contributions** — four bullets: (i) a 52-item protocol with a published expected answer per item; (ii) strict vs lenient accuracy as separate measures; (iii) 208 logged answers released raw; (iv) a single-file harness that reproduces the run.
- **1.4 What this paper does not claim** — one short paragraph. No ranking, no frontier-model claims, no general quality statement.

## 2. Related Work

Position against five threads, one paragraph each. Every citation must be located and verified before it enters the bibliography — do not cite from memory.

- **2.1 Static multiple-choice benchmarks** — the MMLU-style tradition and why exact-match on fixed options differs from free-text chat scoring.
- **2.2 Open-ended and pairwise chat evaluation** — judge-based and arena-style ranking; what they buy (scale, human preference) and what they cost (judge bias, cost, non-determinism).
- **2.3 Evaluation in low-resource languages** — Nepali specifically: how little is published, why five items is a probe and not a claim.
- **2.4 Reproducibility and artifact release** — the lineage of “submit the harness, not the number”.
- **2.5 Verbosity and directness** — prior observations that models bury answers; this paper turns that observation into a second metric.

## 3. Methodology

- **3.1 Research questions** — RQ1 correctness at fixed prompts; RQ2 does answer-first formatting differ more than correctness; RQ3 does scale help within one family (4B vs 9B); RQ4 do local and hosted models differ in clarification and safety behaviour.
- **3.2 Study design** — one fixed prompt set, four models, one run each, temperature 0, no prompt tuning per model.
- **3.3 Unit of analysis** — the **prompt**, not the API call. State n = 40 per model for accuracy; 5 for clarification; 5 for Nepali; 6 per direction for safety.
- **3.4 Threats to validity, stated up front** — small n, single run, one annotator, free-tier drift. Forward-reference §8 so the reader knows these are acknowledged, not hidden.

## 4. Evaluation Protocol

- **4.1 Prompt set construction** — the 52 items and their categories (factual 6, arithmetic 6, reasoning 6, instruction 6, coherence 3, multi-turn 3, underspecified 5, Nepali 5, benign safety 6, harmful safety 6). Include one worked example item verbatim.
- **4.2 Scoring: strict vs lenient** — define both precisely. `acc_contains` = expected answer anywhere; `acc_strict` = within the first 12 words. Justify the 12-word window and show one reply that passes lenient and fails strict.
- **4.3 Expected-answer policy** — single canonical string or a list of accepted variants; Devanagari normalisation (anusvara/candrabindu, digits); how the M19 defect (expected answer reduced to a bare comma by normalisation) was found and fixed.
- **4.4 Behavioural probes** — clarification on underspecified prompts; over-refusal on 6 benign prompts; unsafe compliance on 6 harmful prompts. Define each rate and its denominator explicitly.
- **4.5 Statistical treatment** — bootstrap percentile intervals over items, 2,000 resamples, 95%. State that intervals are the comparison device and that no significance test is claimed because no comparison is claimed.
- **4.6 Failure handling** — truncated and empty replies excluded from accuracy and reported in their own columns; transport failures never scored as wrong answers.

## 5. Models and Setup

- **5.1 Model slate** — Qwen3.5 4B, Qwen3.5 9B, Gemma 4 12B via Ollama; Gemini 3.1 Flash Lite on the free tier. One table: registry key, route, model ID, parameters where known, VRAM, quantisation.
- **5.2 Generation settings** — temperature 0, 4096 context, output budget (default, then 1,024 for the seven rerun items — stated as a deviation), thinking disabled for local models and why that is the fair comparison.
- **5.3 Hardware and runtime** — Colab free Tesla T4, 15,360 MiB; Python 3.13.16; Ollama 0.40.16; wall-clock date of the run.
- **5.4 Harness implementation** — single file, 1,041 lines, `requests` only, JSONL checkpointing, resume-safe by item ID.

## 6. Results

- **6.1 Data completeness** — 52 records per model, 52 unique item IDs, 0 errors, 0 truncated, 0 empty; 208 answers total. This subsection exists so §6.2 can be trusted.
- **6.2 Accuracy** — the main table: `acc_strict` with 95% CI, `acc_contains` with 95% CI, per model. State the observed ordering and immediately state that intervals overlap.
- **6.3 The strict–lenient gap** — the paper's most defensible finding. Report the gap per model (0.25–0.30) and interpret it as a verbosity/formatting effect, not an intelligence difference.
- **6.4 Scale within one family** — Qwen 4B vs 9B: 0.550 vs 0.575 strict, 0.875 vs 0.875 lenient, CIs nearly identical. Treat the null as a result, not a failure.
- **6.5 Behavioural probes** — clarification 3/5, 1/5, 4/5, 4/5; Nepali 5/5, 5/5, 4/5, 4/5; over-refusal 0/6 and unsafe compliance 0/6 for all four. Flag the denominators in the table caption.
- **6.6 Latency and throughput** — p50/p95 plus tokens per second; note that p95 mixes model speed with answer length.

## 7. Analysis and Discussion

- **7.1 Why correctness saturates but directness does not** — the 40 items were built to be answerable; formatting is where models actually diverge.
- **7.2 Does model size buy directness?** — no measurable effect at 4B vs 9B on this set; discuss capacity, instruction tuning, and the possibility that 40 items cannot resolve a 2.5-point difference.
- **7.3 Local vs hosted** — the hosted model had the widest tolerance for short answers; the local models clarified far more often (4/5 vs 1/5 for Gemma). Offer a hypothesis, label it a hypothesis.
- **7.4 What a practitioner should take away** — three sentences, no new data.
- **7.5 A note on the null result** — why publishing it is useful: it bounds what a 40-item protocol can detect.

## 8. Limitations

Numbered, each with its consequence for interpretation.

1. 40 scored items → one item ≈ 2.5 points; the third/fourth-place gap is smaller than that.
2. One run per model, one condition → no within-model variance estimate.
3. Fully overlapping intervals → no supported ranking.
4. Subgroup sizes (Nepali 5, clarification 5, safety 6 per direction) → descriptive only.
5. Free-tier and open-weight models only → no frontier-model claims.
6. Latency not normalised by answer length.
7. Mixed output budgets (seven items at 1,024 tokens) → affects length-sensitive metrics.
8. Thinking disabled → not each model's best configuration.
9. Single author wrote the expected answers → no inter-annotator agreement.
10. `token_f1` penalises length by construction.
11. No multiple-comparison correction, because no comparison is claimed.

## 9. Ethical Considerations

- **9.1 Harmful-prompt probes** — six harmful items were sent to four models; describe the categories at a level that does not reproduce harmful content, and state that no outputs are published verbatim in the appendix.
- **9.2 Safety conclusions are bounded** — 6 probes per direction cannot support a safety claim; over-refusal and unsafe-compliance are reported as counts, not rates.
- **9.3 Language representation** — Nepali items were written by one non-expert-annotated author; treat as a probe, avoid implying coverage of Nepali NLP.
- **9.4 Cost and access** — the study is only possible on free tiers; note who that includes and excludes, and that free tiers can change without notice.
- **9.5 Data and licensing** — model outputs are released as JSONL; state the licence split (MIT for code, CC BY 4.0 for measured outputs).

## 10. Reproducibility and Artifact

- **10.1 What is released** — harness, 208 raw answers, summary table, charts, environment record, manifest.
- **10.2 How to re-run** — four commands: mock dry run, 6-item pilot, full local run, report rebuild. Give them verbatim.
- **10.3 Integrity checks** — SHA-256 of the harness and of every artifact file; one verification snippet the reader can paste.
- **10.4 What a re-run will and will not reproduce** — the structure yes, the exact decimals no (model IDs rotate, free tiers rate-limit).
- **10.5 Artifact location** — public repository URL and the tagged release holding the archived snapshot.

## 11. Conclusion

Four short paragraphs, no new claims: the protocol, the two findings that survive (retrieval ≫ answer-first; scale produced no measurable gain at this n), the release, and the single most valuable next step (grow the item set to 150–200).

## References

Populate only with sources actually opened and verified. Suggested search targets, to be resolved before writing the bibliography:

| Thread | What to locate |
|---|---|
| Static benchmarks | The original MMLU paper and one critique of multiple-choice saturation |
| Chat/arena evaluation | One pairwise-preference or arena paper; one LLM-as-judge paper plus one judge-bias critique |
| Reproducibility | One paper or policy statement on artifact review and re-runnable evaluation |
| Verbosity/directness | One study on response length or answer position effects |
| Nepali / low-resource NLP | One Nepali or Devanagari NLP resource paper, if a suitable one exists |
| Tooling | Ollama and the Gemini API documentation, cited as software/documentation |

## Appendices

- **Appendix A — Full prompt set.** All 52 items: ID, category, prompt, expected answer(s), scoring rule.
- **Appendix B — Per-item outcome matrix.** 4 models × 40 items, strict and lenient, so a reader can see which items separate the models and which every model passed.
- **Appendix C — Failure and rerun log.** The thinking-mode truncation (47 of 50 Qwen items empty on the first run), the stale-resume episode, the M19 defect, and the seven items rerun at 1,024 tokens.
- **Appendix D — Environment and provenance.** Python, OS, GPU, Ollama version, model IDs, harness hash, manifest summary.
- **Appendix E — Reproduction transcript.** The exact commands and the observed summary output, trimmed to the lines that matter.

---

## Tables and figures

| ID | Content | Source in repository |
|---|---|---|
| Table 1 | Model slate and generation settings | harness registry, `docs/PROVENANCE.md` |
| Table 2 | The 52 items by category | §5 of `README.md`, harness prompt list |
| Table 3 | Main accuracy results with 95% CIs | `results/results.csv` |
| Table 4 | Behavioural probes with denominators | `results/results.csv`, `summary.md` |
| Table 5 | Latency and throughput | `results/results.csv` |
| Figure 1 | Accuracy by model, strict vs lenient | `results/charts/accuracy.png` |
| Figure 2 | Latency distribution | `results/charts/latency.png` |
| Figure 3 | Safety probe outcomes | `results/charts/safety.png` |
| Figure 4 | The strict–lenient gap (new, from the CSV) | derived |

## Length budget

| Section | Target |
|---|---|
| Abstract | 200 words |
| 1 Introduction | 700 |
| 2 Related work | 800 |
| 3–5 Method, protocol, setup | 1,500 |
| 6 Results | 900 |
| 7 Analysis | 700 |
| 8–10 Limitations, ethics, reproducibility | 900 |
| 11 Conclusion | 250 |
| Appendices | unlimited, but Table A and B do the work |

## Open items to resolve before submission

- [x] **Primary category: `cs.AI`.** Settled — it is the endorsed category, which removes a submission blocker. When filling in metadata, lead the abstract with the evaluation framing so a `cs.AI` reader sees immediately why a chat-model comparison belongs here rather than in `cs.CL`. If arXiv reclassifies the paper, that is a moderation decision, not a rejection; the artifact and the results stand either way.
- [x] **References verified.** Six sources, each opened on 14 November 2026: MMLU, HELM, MT-Bench/Chatbot Arena, the Nepali NLU benchmark, Ollama, and the Gemini API documentation. No citation was written from memory.
- [ ] Re-check the four model IDs against current Ollama and AI Studio listings, and record the date checked.
- [ ] Decide whether Figure 4 (the gap) is computed in the harness or in a short plotting script; if the latter, ship that script with the artifact.
- [ ] Confirm the repository URL and release tag render in the compiled PDF. *(URL is written in `main.md`; the tagged release does not exist yet.)*
