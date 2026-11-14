# Results

Regenerated from `results/results.csv` when this package was built; the CSV is the
authoritative copy. `acc_strict` = expected answer within the first 12 words;
`acc_contains` = expected answer anywhere in the reply. Truncated and errored items
are excluded from accuracy and counted in their own columns.

| model | label | n_items | n_scored | errors | truncated | empty_answers | acc_contains | acc_contains_ci | acc_strict | acc_strict_ci | token_f1 | nepali_acc | over_refusal | unsafe_compliance | clarify_rate | latency_p50 | latency_p95 | ttft_p50 | tok_per_s | peak_vram_gb |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| gemini-flash-lite | Gemini 3.1 Flash Lite (free tier) | 52 | 40 | 0 | 0 | 0 | 0.925 | 0.85-1.0 | 0.675 | 0.525-0.825 | 0.163 | 1.0 | 0.0 | 0.0 | 0.6 | 3.25 | 8.22 | — | 45.97 | — |
| gemma4-12b | Gemma 4 12B (local) | 52 | 40 | 0 | 0 | 0 | 0.85 | 0.725-0.95 | 0.65 | 0.5-0.8 | 0.188 | 1.0 | 0.0 | 0.0 | 0.2 | 1.38 | 30.6 | 0.18 | 24.46 | 8.49 |
| qwen35-4b | Qwen3.5 4B (local) | 52 | 40 | 0 | 0 | 0 | 0.875 | 0.775-0.975 | 0.55 | 0.4-0.7 | 0.145 | 0.8 | 0.0 | 0.0 | 0.8 | 2.65 | 16.12 | 0.12 | 41.12 | 3.7 |
| qwen35-9b | Qwen3.5 9B (local) | 52 | 40 | 0 | 0 | 0 | 0.875 | 0.775-0.975 | 0.575 | 0.425-0.725 | 0.177 | 0.8 | 0.0 | 0.0 | 0.8 | 3.92 | 28.04 | 0.16 | 25.0 | 6.23 |
