import pathlib
for f, old, new in [
    ("research_package/README.md", "(1041 lines)", "(1068 lines)"),
    ("paper/TOC.md", "single file, 1,041 lines", "single file, 1,068 lines"),
]:
    p = pathlib.Path(f); s = p.read_text(encoding="utf-8")
    assert old in s, f
    p.write_text(s.replace(old, new, 1), encoding="utf-8")
    print("fixed", f)
