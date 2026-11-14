# Provenance

Packaged: 2026-11-14 (rebuilt from the verified 12:59 package)
Python: 3.13.16
Platform: Linux-6.6.159+-x86_64-with-glibc2.39  (Google Colab, free T4 runtime)
Ollama: ollama version is 0.40.16
GPU: Tesla T4, 15360 MiB
harness.py sha256: 2b9d1eabd3255ff0d6d00d4138962a0c2abd40d9211bb1f05758c039ae4613cd
harness.py lines: 1068
Notebook: notebook/chat_eval_colab.ipynb (249200 bytes)

## Models evaluated
- qwen35-4b            qwen3.5:4b            local, Ollama
- qwen35-9b            qwen3.5:9b            local, Ollama
- gemma4-12b           gemma4:12b            local, Ollama
- gemini-flash-lite    gemini-3.1-flash-lite  hosted, free tier

## Protocol
52 records per model: 40 main items across 8 categories (factual, arithmetic,
reasoning, instruction, coherence, multiturn, underspecified, nepali) plus 12
safety probes (6 benign for over-refusal, 6 harmful for unsafe compliance).
Temperature 0, thinking disabled for the local models. Accuracy excludes
truncated and errored items. Intervals are bootstrap percentile intervals
resampled over items (n=40).

## Integrity
This harness is the one that produced results/*.jsonl. Verify before trusting
the summary table: `sha256sum code/harness.py` must equal the value above.
