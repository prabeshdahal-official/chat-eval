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

**Archive → Subject Class**
Archive `cs` → Subject class **Artificial Intelligence (cs.AI)**
The account `prabeshdahal.krip` is registered to the `cs` group, so `cs` appears in the archive list. Pick `cs.AI` from the subject list.

**Cross-list (optional)**
cs.CL — the study is a language-model evaluation; cross-listing is honest, not strategic.

**Comments field (fits the 400-character box)**
21 pages, 18 tables, 4 figures. Code, 208 raw answers and the evaluation harness: https://github.com/prabeshdahal-official/chat-eval

**License (form option: "CC BY: Creative Commons Attribution")**
Click **CC BY**. It keeps the paper consistent with what the artifact already declares: MIT for the code, CC BY 4.0 for the measured outputs. The choice is irrevocable, so it is recorded here.

Why not the others:
- `CC BY-SA` — forces every reuse to carry the same licence, which blocks mixing the text into a differently licensed review.
- `CC BY-NC-SA` / `CC BY-NC-ND` — not open access under most funder rules (Plan S, BOAI), and NC blocks commercial reuse such as a publisher's collected volume.
- `arXiv perpetual, non-exclusive` — the paper stays readable but readers get no reuse rights; the weakest option for a study whose point is reuse.
- `CC Zero` — no attribution, so you lose the credit link back to your work.

**Processors**
**xelatex** (the scan selects it automatically). The paper loads `fontspec` and a local Devanagari font, so `pdflatex` would fail. TeX Live 2025 is fine.

**Font file**
`NotoSansDevanagari-Regular.ttf` sits at the **root of the upload, next to `main.tex`**, and is referenced as `\newfontfamily\devanagari{NotoSansDevanagari-Regular.ttf}` with no path option. arXiv's scanner does not read the `Path=` option, which is why an earlier upload reported the font as "missing from the source". If the scan still marks the file "Not used", keep the row anyway — a note is not an error, and deleting it breaks the build.

## Abstract (plain text, paste as is)

Problem. Many papers say that one chat model is better than another. A reader often cannot check the claim. The questions are private, the scoring is hidden, and the run cannot be repeated.

Protocol. We test four chat models on one fixed set of 52 questions: Qwen3.5 4B, Qwen3.5 9B and Gemma 4 12B, which run on a free Colab GPU, and Gemini 3.1 Flash Lite, which runs on a free API tier. We set temperature to 0, so chance does not change answers. That gives 208 logged answers. No answer was empty, cut off or lost.

Scoring. We score each answer two ways. Retrieval score (acc_contains) is 1 if the expected answer appears anywhere in the reply. Answer-first score (acc_strict) is 1 only if the answer appears in the first 12 words. The second score asks: did the model say it early, or bury it?

Results. Retrieval score was 0.85 to 0.925. Answer-first score was 0.55 to 0.675. All four knew most answers but often said them late. The 95% ranges overlapped, so we claim no winner.

Release. We publish all 208 raw answers as JSONL files and the harness in a public repository. Anyone can re-run the test or check any number.
