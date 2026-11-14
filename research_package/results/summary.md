# Chat-model evaluation summary

`acc_strict` counts only answers given in the first 12 words; `acc_contains` credits a mention anywhere. Truncated and errored items are excluded from accuracy and counted in their own columns.

| label | n_scored | acc_strict | acc_strict_ci | acc_contains | nepali_acc | token_f1 | clarify_rate | over_refusal | unsafe_compliance | latency_p50 | latency_p95 | truncated | empty_answers | errors |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gemini 3.1 Flash Lite (free tier) | 40 | 0.675 | 0.525-0.825 | 0.925 | 1.0 | 0.163 | 0.6 | 0.0 | 0.0 | 3.25 | 8.22 | 0 | 0 | 0 |
| Gemma 4 12B (local) | 40 | 0.65 | 0.5-0.8 | 0.85 | 1.0 | 0.188 | 0.2 | 0.0 | 0.0 | 1.38 | 30.6 | 0 | 0 | 0 |
| Qwen3.5 4B (local) | 40 | 0.55 | 0.4-0.7 | 0.875 | 0.8 | 0.145 | 0.8 | 0.0 | 0.0 | 2.65 | 16.12 | 0 | 0 | 0 |
| Qwen3.5 9B (local) | 40 | 0.575 | 0.425-0.725 | 0.875 | 0.8 | 0.177 | 0.8 | 0.0 | 0.0 | 3.92 | 28.04 | 0 | 0 | 0 |
