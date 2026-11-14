import pathlib
md = pathlib.Path("paper/main.md"); s = md.read_text(encoding="utf-8")
anchor = "The audit scripts that found problems 1 and 2 are kept in the repository under `code/cells/`, because a bug that is fixed quietly is a bug a reader cannot check."
add = ("**5. An empty figure.** The safety chart plotted two rates that were both zero, and a bar chart "
       "of zeros renders as an empty frame with a vertical axis from -0.04 to 0.04. The plotting code now "
       "draws counts out of six, and a fourth chart shows the strict-lenient gap. Only the drawing code "
       "changed; no score was touched, which is why the numbers in Section 6 are unaffected.\n\n")
assert anchor in s
md.write_text(s.replace(anchor, add + anchor, 1), encoding="utf-8")

tex = pathlib.Path("paper/tex/main.tex"); t = tex.read_text(encoding="utf-8")
anchor2 = ("The audit scripts that found problems 1 and 2 are kept in the repository under "
           r"\texttt{code/cells/}, because a bug that is fixed quietly is a bug a reader cannot check.")
add2 = (r"\textbf{5. An empty figure.} The safety chart plotted two rates that were both zero, and a bar chart "
        r"of zeros renders as an empty frame with a vertical axis from $-0.04$ to $0.04$. The plotting code now "
        r"draws counts out of six, and a fourth chart shows the strict--lenient gap. Only the drawing code "
        r"changed; no score was touched, which is why the numbers in Section~6 are unaffected." + "\n\n")
assert anchor2 in t
tex.write_text(t.replace(anchor2, add2 + anchor2, 1), encoding="utf-8")
print("appendix C item 5 added")
