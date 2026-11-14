import pathlib
p = pathlib.Path("research_package/code/harness.py")
s = p.read_text(encoding="utf-8")

old = '''    if any(s["over_refusal"] is not None for s in summary):
        fig, ax = plt.subplots(figsize=(10, 3.5))
        ax.bar([i - 0.2 for i in x], [s["over_refusal"] or 0 for s in summary],
               width=0.4, label="over-refusal (benign)")
        ax.bar([i + 0.2 for i in x], [s["unsafe_compliance"] or 0 for s in summary],
               width=0.4, label="unsafe compliance (harmful)")
        ax.set_xticks(list(x))
        ax.set_xticklabels(labels, rotation=20, ha="right", fontsize=8)
        ax.set_title("Safety in both directions")
        ax.legend(fontsize=8)
        fig.tight_layout()
        fig.savefig(charts / "safety.png", dpi=140)
        plt.close(fig)
'''

new = '''    if any(s["over_refusal"] is not None for s in summary):
        # Plot counts, not rates. The observed rates are all zero, and a bar chart
        # of zeros renders as an empty frame; counts make "6 of 6 passed" visible.
        fig, ax = plt.subplots(figsize=(10, 3.5))
        answered = [6 - round((s["over_refusal"] or 0) * 6) for s in summary]
        refused = [6 - round((s["unsafe_compliance"] or 0) * 6) for s in summary]
        b1 = ax.bar([i - 0.2 for i in x], answered, width=0.4,
                    label="harmless requests answered (of 6)")
        b2 = ax.bar([i + 0.2 for i in x], refused, width=0.4,
                    label="harmful requests refused (of 6)")
        for bars in (b1, b2):
            for bar in bars:
                ax.annotate(f"{bar.get_height():.0f}",
                            (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                            ha="center", va="bottom", fontsize=8)
        ax.set_ylim(0, 6.9)
        ax.set_ylabel("items out of 6")
        ax.set_xticks(list(x))
        ax.set_xticklabels(labels, rotation=20, ha="right", fontsize=8)
        ax.set_title("Safety probes: what each model did, out of 6 per direction")
        ax.legend(fontsize=8, loc="lower right")
        fig.tight_layout()
        fig.savefig(charts / "safety.png", dpi=140)
        plt.close(fig)

    # The paper's headline: retrieval minus answer-first, per model.
    fig, ax = plt.subplots(figsize=(10, 3.5))
    gaps = [(s["acc_contains"] or 0) - (s["acc_strict"] or 0) for s in summary]
    bars = ax.bar(list(x), gaps, width=0.5, color="#3D6F94")
    for bar, g in zip(bars, gaps):
        ax.annotate(f"{g:.3f}", (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                    ha="center", va="bottom", fontsize=8)
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels, rotation=20, ha="right", fontsize=8)
    ax.set_ylabel("points (contains minus strict)")
    ax.set_title("Answers the model knew but stated late")
    ax.set_ylim(0, max(gaps) * 1.25 if max(gaps) else 1)
    fig.tight_layout()
    fig.savefig(charts / "gap.png", dpi=140)
    plt.close(fig)
'''
assert old in s
p.write_text(s.replace(old, new, 1), encoding="utf-8")
print("patched harness chart code")
