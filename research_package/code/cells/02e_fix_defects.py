# Raised the token ceiling to 1024, fixed item M19 (comma -> "Dashain"),
# then pruned truncated records so --resume re-ran only the 27 affected items.
import json, pathlib
h = pathlib.Path("harness.py")
src = h.read_text(encoding="utf-8")
for old, new in [
    ("LOCAL_MAX_NEW = 2048 if THINK else 512", "LOCAL_MAX_NEW = 2048 if THINK else 1024"),
    ('"max_new": 512, "label"', '"max_new": 1024, "label"'),
    ('"List two Nepali festivals, separated by a comma, and nothing else.", ","),',
     '"List two Nepali festivals, separated by a comma, and nothing else.", "Dashain"),'),
]:
    if old in src:
        src = src.replace(old, new, 1)
h.write_text(src, encoding="utf-8")
dropped = 0
for f in sorted(pathlib.Path("runs").glob("*.jsonl")):
    keep = []
    for line in f.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        if rec.get("item_id") and (rec.get("truncated") or rec["item_id"] == "M19"):
            dropped += 1
            continue
        keep.append(line)
    f.write_text("
".join(keep) + "
", encoding="utf-8")
print("records queued for re-run:", dropped)
