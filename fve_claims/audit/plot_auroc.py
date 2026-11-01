"""Plot saved claim scores; run from repository root: uv run python fve_claims/audit/plot_auroc.py."""
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import rankdata
from claims_data import load, auroc

OUT = Path("fve_claims/figures")
SEED, DRAWS = 0, 4000
COLORS = {"7B": "#2878B5", "27B": "#D47732"}


def auc(y, x):
    nt, nf = y.sum(), (~y).sum()
    if not nt or not nf:
        return np.nan
    return float((rankdata(x)[y].sum() - nt * (nt + 1) / 2) / (nt * nf))


results = {}
for model in COLORS:
    s = load(model).reset_index(drop=True)
    y = s.truth.eq("true").to_numpy()
    fs = s.final_sentence.to_numpy()
    scores = {c: s[c].to_numpy() for c in ("deletion", "paraphrase")}
    specs = {
        "All claims": ("deletion", np.ones(len(s), dtype=bool)),
        "Final explanation sentence": ("deletion", fs),
        "Elsewhere in explanation": ("deletion", ~fs),
        "Paraphrase": ("paraphrase", np.ones(len(s), dtype=bool)),
    }
    docs = np.sort(s.pilot_id.unique())
    rows = {d: np.flatnonzero(s.pilot_id.to_numpy() == d) for d in docs}
    rng = np.random.default_rng(SEED)
    boots = {k: [] for k in specs}
    for _ in range(DRAWS):
        ix = np.concatenate([rows[d] for d in rng.choice(docs, len(docs))])
        for k, (col, mask) in specs.items():
            selected = ix[mask[ix]]
            boots[k].append(auc(y[selected], scores[col][selected]))
    results[model] = {}
    for k, (col, mask) in specs.items():
        value = auc(y[mask], scores[col][mask])
        assert np.isclose(value, auroc(scores[col][mask & y], scores[col][mask & ~y]))
        samples = np.asarray(boots[k])
        lo, hi = np.nanpercentile(samples, [2.5, 97.5])
        results[model][k] = dict(auroc=value, ci95=[float(lo), float(hi)],
                                  n_true=int((mask & y).sum()), n_false=int((mask & ~y).sum()),
                                  valid_draws=int(np.isfinite(samples).sum()))

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                     "axes.spines.top": False, "axes.spines.right": False,
                     "axes.spines.left": False, "svg.fonttype": "none"})


def panel(ax, labels, keys):
    ax.axvline(.5, color="#82909C", ls=(0, (4, 4)), lw=1.3, zorder=0)
    for model, offset in [("7B", -.14), ("27B", .14)]:
        for j, key in enumerate(keys):
            r = results[model][key]
            v, (lo, hi) = r["auroc"], r["ci95"]
            yy = len(keys) - 1 - j + offset
            ax.errorbar(v, yy, xerr=[[v-lo], [hi-v]], fmt="o", color=COLORS[model],
                        capsize=4, markersize=7, elinewidth=2, label=model if j == 0 else None)
            ax.text(hi + .012, yy, f"{v:.3f}", va="center", color=COLORS[model], fontsize=10)
    ax.set_yticks(range(len(labels)), labels[::-1])
    ax.tick_params(axis="y", length=0, pad=12)
    ax.set_xlim(.35, .88)
    ax.set_xticks([.4, .5, .6, .7, .8])
    ax.set_ylim(-.6, len(labels)-.4)
    ax.set_xlabel("AUROC  ·  0.5 = chance")
    ax.grid(axis="x", alpha=.12)
    ax.legend(frameon=False, loc="upper right", ncol=2)


OUT.mkdir(exist_ok=True)
for name, labels, keys, title, subtitle, foot in [
    ("auroc_by_position", ["All claims", "Final explanation\nsentence", "Elsewhere in\nexplanation"],
     ["All claims", "Final explanation sentence", "Elsewhere in explanation"],
     "Claim discrimination by explanation position", "Deletion scores · true versus false claims",
     "Exploratory position subgroups; source locality and claim type are not controlled."),
    ("auroc_deletion_vs_paraphrase", ["Deletion", "Paraphrasing"], ["All claims", "Paraphrase"],
     "Deletion and paraphrase scores as truth signals", "All evaluated true/false claims · no fitted classifier",
     "Paraphrases edit whole sentences; this plot does not test their incremental value when combined with deletion."),
]:
    fig, ax = plt.subplots(figsize=(10.5, 5.5))
    fig.subplots_adjust(left=.25, right=.96, top=.77, bottom=.25)
    panel(ax, labels, keys)
    fig.text(.04, .94, title, fontsize=18, weight="bold", color="#20354A")
    fig.text(.04, .885, subtitle, fontsize=11, color="#536779")
    fig.text(.04, .12, "95% document-bootstrap intervals · 4,000 draws · 100 documents per model · AI-produced truth labels", fontsize=9, color="#536779")
    fig.text(.04, .065, foot, fontsize=8.5, color="#536779")
    for ext in ("png", "svg"):
        fig.savefig(OUT / f"{name}.{ext}", dpi=220, facecolor="white")
    plt.close(fig)

(OUT / "auroc_plot_data.json").write_text(json.dumps({"seed": SEED, "draws": DRAWS,
    "method": "Percentile bootstrap resampling all documents with replacement; claims weighted equally; larger drops predict true.",
    "results": results}, indent=2) + "\n")
print(json.dumps(results, indent=2))
