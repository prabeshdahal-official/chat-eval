import pathlib
p = pathlib.Path("paper/tex/main.tex"); s = p.read_text(encoding="utf-8")

# 1. gap figure in 6.4, right after the gap table
old = r"""The gap is larger than the distance between any two models on the retrieval score."""
new = r"""\begin{figure}[htbp]
\centering
\includegraphics[width=0.86\linewidth]{gap.png}
\caption{The strict--lenient gap per model: answers the model knew but stated after the first 12 words.}
\label{fig:gap}
\end{figure}

The gap is larger than the distance between any two models on the retrieval score."""
assert old in s
s = s.replace(old, new, 1)

# 2. renumber the later figures
s = s.replace(r"\caption{Behaviour probe outcomes. All four models refused every harmful request and answered every harmless one.}",
              r"\caption{Behaviour probes as counts out of six per direction. Every bar reaches six, which is the result we wanted and the weakest evidence in the paper.}")
s = s.replace(r"\caption{Response time per model. The 95th percentile depends on answer length as well as on model speed.}",
              r"\caption{Response time per model. The 95th percentile depends on answer length as well as on model speed.}")
p.write_text(s, encoding="utf-8")
print("main.tex updated")
