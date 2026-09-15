"""Render manuscript point estimates from data/results.json. Requires matplotlib."""
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "data/results.json").read_text())
colors = {
    "SFT": "#8db3ca",
    "SFT + Int.": "#e7c493",
    "SFT + RL": "#a4adbd",
    "Evo-RL": "#479a8f",
    "Evo-RL (R2)": "#10575d",
}
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 12,
    "text.color": "#182d34", "axes.labelcolor": "#53696f",
    "xtick.color": "#607078", "ytick.color": "#182d34",
    "svg.hashsalt": "evo-rl-policy-results",
})
fig, axes = plt.subplots(2, 2, figsize=(14, 9.2), gridspec_kw={"height_ratios": [1.7, 1]})
fig.subplots_adjust(left=.15, right=.96, top=.87, bottom=.12, hspace=.7, wspace=.52)
fig.text(.035, .965, "Policy improvement across tasks and rounds", fontsize=21, weight="bold")
fig.text(.035, .925, "PiperX insertion: 10 trials per method  |  SO-101 folding: 20 planned instances per stage", fontsize=12, color="#607078")

for i, (group, task) in enumerate([("PiperX insertion", "PiperX insertion"), ("SO-101 folding", "SO-101 folding")]):
    rows = [r for r in data["policy"] if r["group"] == group]
    for j, (metric, label) in enumerate([("sr", "Attempt success (%)"), ("tp", "Throughput (units/h)")]):
        ax = axes[i, j]
        values = [float(r[metric]) for r in rows]
        ax.barh(range(len(rows)), values, color=[colors[r["method"]] for r in rows], height=.62, zorder=3)
        ax.set_yticks(range(len(rows)), [r["method"] for r in rows])
        ax.invert_yaxis()
        ax.set_xlim(0, 115 if metric == "sr" else (105 if i else 82))
        ax.set_xticks([0, 25, 50, 75, 100] if metric == "sr" else ([0, 25, 50, 75, 100] if i else [0, 20, 40, 60, 80]))
        ax.set_title(f"{chr(65 + i * 2 + j)}   {task}", loc="left", pad=15, fontsize=13, weight="bold")
        ax.set_xlabel(label, labelpad=10)
        ax.xaxis.grid(True, color="#e4ebed", linewidth=.9, zorder=0)
        ax.tick_params(axis="both", length=0, pad=8)
        for spine in ax.spines.values():
            spine.set_visible(False)
        for y, (row, value) in enumerate(zip(rows, values)):
            ax.text(value + 1.8, y, row[metric], va="center", fontsize=12,
                    weight="bold" if row["method"].startswith("Evo-RL") else "normal")

fig.text(.035, .033, "Source: manuscript Table II, September 15, 2026. Point estimates; no confidence intervals supplied in this table.", fontsize=10, color="#607078")
out = ROOT / "dist/assets"
fig.savefig(out / "policy_results.svg", metadata={"Date": None, "Title": "Evo-RL policy comparison from manuscript Table II"})
fig.savefig(out / "policy_results.png", dpi=160, facecolor="white")
plt.close(fig)
