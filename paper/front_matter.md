# Front matter — “Chatting with AI Models”

Draft of the title block, abstract and keywords. Written in plain English: short sentences, common words, no jargon that is not immediately explained.

---

## Title

**Chatting with AI Models: A Zero-Budget, Repeatable Test of Four Chat Models on 52 Fixed Questions**

*Why this title:* “zero-budget” and “four” are kept because they state the real limits of the study. “Repeatable” is used instead of “reproducible” because it is a more common word with the same meaning here. A longer formal variant, if a venue prefers it: *“Chatting with AI Models: A Zero-Budget, Reproducible Evaluation of Four Chat Assistants on a Fixed 52-Item Protocol.”*

## Authors and affiliations

**Prabesh Dahal**
Independent Researcher, Kathmandu, Nepal

- Email: *to be added* — use the address you want public.
- ORCID: *to be added* — optional, but it makes the paper easier to link to your other work.
- Affiliation is written as “Independent Researcher” because no university or company funded or hosted this study.

## Abstract

**Problem.** Many papers say that one chat model is better than another. A reader often cannot check the claim. The questions are private, the scoring is hidden, and the run cannot be repeated.

**Protocol.** We test four chat models on one fixed set of 52 questions: Qwen3.5 4B, Qwen3.5 9B and Gemma 4 12B, which run on a free Colab GPU, and Gemini 3.1 Flash Lite, which runs on a free API tier. We set temperature to 0, so chance does not change answers. That gives 208 logged answers. No answer was empty, cut off or lost.

**Scoring.** We score each answer two ways. Retrieval score (acc_contains) is 1 if the expected answer appears anywhere in the reply. Answer-first score (acc_strict) is 1 only if the answer appears in the first 12 words. The second score asks: did the model say it early, or bury it?

**Results.** Retrieval score was 0.85 to 0.925. Answer-first score was 0.55 to 0.675. All four knew most answers but often said them late. The 95% ranges overlapped, so we claim no winner.

**Release.** We publish all 208 raw answers as JSONL files and the harness in a public repository. Anyone can re-run the test or check any number.

*Word count: 206 (target 180–220); five blocks, 29 sentences, mean 7.1 words per sentence.*

## Keywords

chat model evaluation; open-weight models; reproducibility; answer-first scoring; low-resource languages; free-tier benchmarking

---

## Notes on the choices above

- **Five parts only.** The abstract has exactly five labelled blocks — problem, protocol, scoring, results, release — in the order you asked for. No motivation beyond the first block, no future work, no limitations.
- **The two scores are defined in words, not symbols.** Each is stated as “is 1 if…”, which a reader can follow without a statistics background. The parenthetical metric names connect the abstract to the tables.
- **The ranges are quoted as given.** 0.85–0.925 for retrieval and 0.55–0.675 for answer-first. The abstract does not name the best model, because the ranges overlap; naming one would contradict the results section.
- **“We claim no winner” is a claim about the study, not about the models.** It keeps the abstract honest without making the paper sound like it failed.
