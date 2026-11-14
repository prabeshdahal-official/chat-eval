# Archived runs/ and runs_pilot/ after settings changed, then printed
# per-file record/truncation counts. Renamed only; nothing deleted.
import json, pathlib, time
for d in ("runs", "runs_pilot"):
    p = pathlib.Path(d)
    if not p.exists():
        continue
    for f in sorted(p.glob("*.jsonl")):
        recs = [json.loads(l) for l in f.read_text(encoding="utf-8").splitlines() if l.strip()]
        recs = [r for r in recs if r.get("item_id")]
        print(f.stem, len(recs), sum(1 for r in recs if r.get("truncated")))
    p.rename(f"{d}_old_{time.strftime('%H%M')}")
