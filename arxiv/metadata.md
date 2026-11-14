# arXiv submission metadata

Copy these values into the arXiv form. Nothing else is needed.

**Title**
Chatting with AI Models: A Zero-Budget, Repeatable Test of Four Chat Models on 52 Fixed Questions

**Authors**
Krip Prabesh

**Affiliation**
Independent Researcher, Kathmandu, Nepal

**Contact email**
krip.prabesh@gmail.com

**ORCID**
0009-0002-1716-0724

**Primary category**
cs.AI

**Cross-list (optional)**
cs.CL — the study is a language-model evaluation; cross-listing is honest, not strategic.

**Comments field (fits the 400-character box)**
21 pages, 18 tables, 4 figures. Code, 208 raw answers and the evaluation harness: https://github.com/prabeshdahal-official/chat-eval

**License**
CC BY 4.0 — the paper. The repository code stays MIT and the measured outputs stay CC BY 4.0.

**Processors**
Choose **xelatex**. The paper loads `fontspec` and a local Devanagari font; `pdflatex` will fail.

## Abstract (plain text, paste as is)

Problem. Many papers say that one chat model is better than another. A reader often cannot check the claim. The questions are private, the scoring is hidden, and the run cannot be repeated.

Protocol. We test four chat models on one fixed set of 52 questions: Qwen3.5 4B, Qwen3.5 9B and Gemma 4 12B, which run on a free Colab GPU, and Gemini 3.1 Flash Lite, which runs on a free API tier. We set temperature to 0, so chance does not change answers. That gives 208 logged answers. No answer was empty, cut off or lost.

Scoring. We score each answer two ways. Retrieval score (acc_contains) is 1 if the expected answer appears anywhere in the reply. Answer-first score (acc_strict) is 1 only if the answer appears in the first 12 words. The second score asks: did the model say it early, or bury it?

Results. Retrieval score was 0.85 to 0.925. Answer-first score was 0.55 to 0.675. All four knew most answers but often said them late. The 95% ranges overlapped, so we claim no winner.

Release. We publish all 208 raw answers as JSONL files and the harness in a public repository. Anyone can re-run the test or check any number.
