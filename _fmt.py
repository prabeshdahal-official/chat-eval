import csv, pathlib
ROOT = pathlib.Path(".")
rows = list(csv.DictReader((ROOT/"research_package/results/results.csv").open(encoding="utf-8")))
by = {r["model"]: r for r in rows}
order = ["gemini-flash-lite","gemma4-12b","qwen35-4b","qwen35-9b"]
label = {"gemini-flash-lite":"Gemini 3.1 Flash Lite","gemma4-12b":"Gemma 4 12B",
         "qwen35-4b":"Qwen3.5 4B","qwen35-9b":"Qwen3.5 9B"}
T = ROOT/"paper/tex/tables"

def f3(v): return f"{float(v):.3f}"

acc = [r"\begin{table}[htbp]", r"\centering",
       r"\caption{Accuracy over the 40 scored items, with bootstrap 95\% ranges resampled over items.}",
       r"\label{tab:accuracy}", "{\\small", r"\begin{tabular}{@{}lrrrrrr@{}}", r"\toprule",
       r"Model & $n$ & \texttt{acc\_strict} & 95\% range & \texttt{acc\_contains} & 95\% range & Token F1 \\",
       r"\midrule"]
for k in order:
    r = by[k]
    lo, hi = r["acc_strict_ci"].split("-")
    lo2, hi2 = r["acc_contains_ci"].split("-")
    acc.append(f"{label[k]} & {r['n_scored']} & {f3(r['acc_strict'])} & [{f3(lo)}, {f3(hi)}] & "
               f"{f3(r['acc_contains'])} & [{f3(lo2)}, {f3(hi2)}] & {f3(r['token_f1'])} \\\\")
acc += [r"\bottomrule", r"\end{tabular}}", r"\end{table}"]
(T/"accuracy.tex").write_text("\n".join(acc)+"\n", encoding="utf-8")

gap = [r"\begin{table}[htbp]", r"\centering",
       r"\caption{Retrieval minus answer-first. The last column counts items the model got right but stated late.}",
       r"\label{tab:gap}", "{\\small", r"\begin{tabular}{@{}lrrrr@{}}", r"\toprule",
       r"Model & Retrieval & Answer-first & Gap & Right but late \\", r"\midrule"]
for k in order:
    r = by[k]
    g = float(r["acc_contains"]) - float(r["acc_strict"])
    gap.append(f"{label[k]} & {f3(r['acc_contains'])} & {f3(r['acc_strict'])} & {g:.3f} & {round(g*40)} of 40 \\\\")
gap += [r"\bottomrule", r"\end{tabular}}", r"\end{table}"]
(T/"gap.tex").write_text("\n".join(gap)+"\n", encoding="utf-8")

sp = [r"\begin{table}[htbp]", r"\centering",
      r"\caption{Response time in seconds and output throughput. A longer answer takes more seconds, so the two columns are not independent.}",
      r"\label{tab:speed}", "{\\small", r"\begin{tabular}{@{}lrrr@{}}", r"\toprule",
      r"Model & Median & 95th percentile & Output tokens/s \\", r"\midrule"]
for k in order:
    r = by[k]
    sp.append(f"{label[k]} & {float(r['latency_p50']):.2f} & {float(r['latency_p95']):.2f} & {float(r['tok_per_s']):.1f} \\\\")
sp += [r"\bottomrule", r"\end{tabular}}", r"\end{table}"]
(T/"speed.tex").write_text("\n".join(sp)+"\n", encoding="utf-8")
print("tables reformatted to 3 decimals")
