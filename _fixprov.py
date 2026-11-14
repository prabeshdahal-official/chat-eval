import pathlib
p = pathlib.Path("research_package/docs/PROVENANCE.md")
s = p.read_text(encoding="utf-8")
s = s.replace("harness.py lines: 1041", "harness.py lines: 1068")
s = s.replace("harness.py lines: 1,041", "harness.py lines: 1068")
p.write_text(s, encoding="utf-8")
print([l for l in s.splitlines() if l.startswith("harness.py")])

# scan every doc for a stale bare 1041
for f in ["README.md", "research_package/README.md", "paper/main.md",
          "paper/tex/main.tex", "research_package/docs/PROVENANCE.md",
          "research_package/docs/results.md", "paper/TOC.md"]:
    q = pathlib.Path(f)
    if q.exists():
        t = q.read_text(encoding="utf-8", errors="ignore")
        if "1041" in t or "1,041" in t:
            print("STALE line count in", f)
