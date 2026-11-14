# Denominator audit: counts what each metric is actually computed over.
import collections, json, pathlib
for f in sorted(pathlib.Path("runs").glob("*.jsonl")):
    recs = [json.loads(l) for l in f.read_text(encoding="utf-8").splitlines() if l.strip()]
    recs = [r for r in recs if r.get("item_id")]
    usable = [r for r in recs if not r.get("truncated") and not r.get("error")]
    print(f.stem, len(recs), dict(collections.Counter(r["category"] for r in recs if r.get("truncated"))))
    print("  benign", sum(1 for r in usable if r["scoring"] == "comply"),
          "harmful", sum(1 for r in usable if r["scoring"] == "refuse"),
          "clarify", sum(1 for r in usable if r["scoring"] == "clarify"))
