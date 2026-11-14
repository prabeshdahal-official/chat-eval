# Chat-model evaluation — research package

Prepared 14 November 2026. Four chat models, 40 scored items plus 12 safety probes, zero API spend.

## Contents

```
code/harness.py        the harness that produced these results (1041 lines)
code/cells/*.py        the repair cells, kept as scripts for the audit trail
results/*.jsonl        one record per (model, item): raw response, score, timing
results/results.csv    one row per model (authoritative summary table)
results/summary.md     the same table in markdown
results/charts/*.png   accuracy, latency and safety figures
notebook/*.ipynb       the Colab notebook, including executed outputs
docs/RESULTS.md        every CSV column as a markdown table
docs/PROVENANCE.md     environment, model IDs, protocol, harness sha256
docs/FOR_PROFESSOR.md  one-page cover note
MANIFEST.json          sha256 + size for every file above
```

## Reproducing the run

`harness.py` is shipped as a file, so no cell has to regenerate it. A fresh Colab
runtime needs three things before the notebook's evaluation cells will work:

1. Upload `code/harness.py` to `/content/harness.py` (or clone it from wherever
   you host this package). The notebook's patch cells 2b/2c/2e assume it is there
   and will fail on a blank runtime.
2. Install Ollama and pull the three local models (notebook cell 1 does both).
3. Put `GOOGLE_API_KEY` in Colab Secrets for the Gemini route.

Then:

```bash
python harness.py --models qwen35-4b qwen35-9b gemma4-12b --out runs
python harness.py --models gemini-flash-lite --out runs
python harness.py --report --out runs
```

## Verify the package

```python
import hashlib, json, pathlib
man = json.loads(pathlib.Path("MANIFEST.json").read_text())
for e in man["files"]:
    p = pathlib.Path(e["path"])
    assert p.exists(), e["path"]
    assert hashlib.sha256(p.read_bytes()).hexdigest() == e["sha256"], e["path"]
print("all", len(man["files"]), "files verified")
```

## Scope

Four free or locally-runnable models, one run each, 40 items. This is a measurement
study, not a leaderboard: the 95% intervals overlap across all four models, so no
ranking is claimed. Subgroups are small (Nepali n=5, clarification n=5, safety n=6
per direction).
