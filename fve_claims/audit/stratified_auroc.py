"""Where the deletion score separates true from false claims, and whether that survives the obvious confounds.
Per model: deletion AUROC (true vs false) pooled, in the verbalizer's final sentence and elsewhere, and stratified by
position; in the final sentence, the AUROC within deleted-length tertiles, within claim subtype and within both
(pair-weighted, i.e. only true/false pairs that share a stratum); how often a document's true claims cost more than its
false ones; medians next to means; how concentrated the large drops are; and the subtype x truth cells. CIs resample
whole documents (SEED and DRAWS as in auroc_and_position.py, so the pooled interval matches it). Drops are in
percentage points of FVE with the local denominator, which differs between the models; AUROC does not depend on it.
Writes fve_claims/audit/out/stratified_auroc.txt. Run from the repo root."""
import sys
sys.path.insert(0, "fve_claims/audit")
import numpy as np, pandas as pd
from scipy.stats import rankdata, binomtest
from claims_data import load, d_local, D_RELEASED_7B

SEED, DRAWS, OUT = 0, 4000, "fve_claims/audit/out/stratified_auroc.txt"
lines = []
def say(s=""):
    print(s); lines.append(s)


def au(y, x):
    """AUROC of score x for y (True = true claim); ties at 0.5. Same value as claims_data.auroc."""
    nt = int(y.sum()); nf = len(y) - nt
    if nt == 0 or nf == 0: return np.nan
    return (rankdata(x)[y].sum() - nt * (nt + 1) / 2) / (nt * nf)


def strat(y, x, g):
    """Pair-weighted mean of within-stratum AUROCs = AUROC over the true/false pairs that share a stratum."""
    num = den = 0.0
    for k in np.unique(g):
        m = g == k; nt = int(y[m].sum()); nf = int(m.sum()) - nt
        if nt and nf: num += au(y[m], x[m]) * nt * nf; den += nt * nf
    return num / den if den else np.nan


def pp(v): return f"{100 * np.median(v):6.2f} / {100 * np.mean(v):6.2f}"


for model in ["7B", "27B"]:
    s = load(model).reset_index(drop=True)
    y, x, fs = (s.truth == "true").values, s.deletion.values, s.final_sentence.values
    sub = s.subtype.astype(str).values
    tert = np.full(len(s), -1)
    tert[fs] = pd.qcut(s.del_chars[fs], 3, labels=False, duplicates="drop").values
    both = np.array([f"{a}|{b}" for a, b in zip(sub, tert)])
    metrics = {
        "pooled": lambda i: au(y[i], x[i]),
        "final sentence": lambda i: au(y[i][fs[i]], x[i][fs[i]]),
        "elsewhere": lambda i: au(y[i][~fs[i]], x[i][~fs[i]]),
        "position-stratified": lambda i: strat(y[i], x[i], fs[i]),
        "final, same length tertile": lambda i: strat(y[i][fs[i]], x[i][fs[i]], tert[i][fs[i]]),
        "final, same subtype": lambda i: strat(y[i][fs[i]], x[i][fs[i]], sub[i][fs[i]]),
        "final, same subtype + tertile": lambda i: strat(y[i][fs[i]], x[i][fs[i]], both[i][fs[i]]),
    }
    docs = np.sort(s.pilot_id.unique()); rows = {d: np.flatnonzero(s.pilot_id.values == d) for d in docs}
    rng = np.random.default_rng(SEED); boots = {k: [] for k in metrics}
    for _ in range(DRAWS):
        i = np.concatenate([rows[d] for d in rng.choice(docs, len(docs))])
        for k, f in metrics.items(): boots[k].append(f(i))
    allrows = np.arange(len(s))

    note = f"FVE denominator D_local {d_local(model):.4f}" + (f" (released {D_RELEASED_7B})" if model == "7B" else " (none released)")
    say(f"=== {model} ===  n={len(s)} ({y.sum()} true / {(~y).sum()} false); {note}")
    say(f"share of claims in the final sentence: true {fs[y].mean():.3f}, false {fs[~y].mean():.3f}")
    say("deletion AUROC, true vs false (document-bootstrap 95% CI):")
    for k, f in metrics.items():
        n = len(s) if k in ("pooled", "position-stratified") else int((fs if k.startswith("final") else ~fs).sum())
        b = np.array(boots[k]); b = b[~np.isnan(b)]; lo, hi = np.percentile(b, [2.5, 97.5])
        say(f"  {k:31s} n={n:4d}  {f(allrows):.3f} [{lo:.3f}, {hi:.3f}]")
    g = s[fs]
    say(f"  deleted length alone, final sentence  {au(y[fs], s.del_chars.values[fs]):.3f}   "
        f"(median deleted chars: true {g[g.truth == 'true'].del_chars.median():.0f}, false {g[g.truth == 'false'].del_chars.median():.0f})")
    wins = [h[h.truth == "true"].deletion.mean() > h[h.truth == "false"].deletion.mean()
            for _, h in g.groupby("pilot_id") if h.truth.nunique() == 2]
    say(f"final sentence, within documents: true-claim mean > false-claim mean in {sum(wins)} of {len(wins)} documents "
        f"(two-sided binomial p = {binomtest(sum(wins), len(wins)).pvalue:.2g})")
    say("deletion drop, pp (median / mean):")
    for lab, m in [("final sentence", fs), ("elsewhere", ~fs)]:
        say(f"  {lab:15s} true {pp(x[m & y])} (n={int((m & y).sum())})   false {pp(x[m & ~y])} (n={int((m & ~y).sum())})")
    top = np.sort(x[fs & y])[::-1]
    say(f"  the 10 largest final-sentence true drops carry {100 * top[:10].sum() / top.sum():.0f}% of the summed true drop")
    say("final sentence, subtype x truth (n, median pp, mean pp):")
    cells = g.assign(pp=g.deletion * 100).groupby(["subtype", "truth"]).pp.agg(["size", "median", "mean"]).round(2)
    for ln in cells.to_string().splitlines(): say("  " + ln)
    say()

open(OUT, "w").write("\n".join(lines) + "\n")
print(f"wrote {OUT}")
