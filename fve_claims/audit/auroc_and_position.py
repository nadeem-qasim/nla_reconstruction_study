"""Per-claim AUROC of the deletion and paraphrase drops (true vs false) with document-cluster
bootstrap CIs, and the deletion drop split by whether the claim touches the verbalizer's final
sentence. Re-derives findings 1 and 2 of the README from the scored CSVs and the claim labels.
Claims and the final-sentence tag come from claims_data.py. Run from the repo root."""

import sys
sys.path.insert(0, "fve_claims/audit")
import numpy as np, pandas as pd
from claims_data import load, auroc

SEED, DRAWS = 0, 4000

for name in ["7B", "27B"]:
    s = load(name)
    docs = np.sort(s.pilot_id.unique()); by_doc = {d: g for d, g in s.groupby("pilot_id")}
    print(f"\n=== {name} ===  n={len(s)}  ({(s.truth=='true').sum()} true / {(s.truth=='false').sum()} false)")
    for col in ["deletion", "paraphrase"]:
        f = lambda d: auroc(d[d.truth=="true"][col].values, d[d.truth=="false"][col].values)
        rng = np.random.default_rng(SEED)
        boots = np.array([f(pd.concat([by_doc[d] for d in rng.choice(docs, len(docs))])) for _ in range(DRAWS)])
        boots = boots[~np.isnan(boots)]
        lo, hi = np.percentile(boots, [2.5, 97.5])
        print(f"  AUROC({col:10s}) = {f(s):.4f}   document-bootstrap 95% CI [{lo:.3f}, {hi:.3f}]   "
              f"P(boot<=0.5) = {(boots<=0.5).mean():.3f}")
    # final-sentence split
    print("  --- deletion drop pp by position ---")
    for fs_flag, lab in [(True, "final sentence"), (False, "elsewhere")]:
        g = s[s.final_sentence == fs_flag]
        t, fa = g[g.truth=="true"].deletion*100, g[g.truth=="false"].deletion*100
        rng = np.random.default_rng(SEED)
        gd = np.sort(g.pilot_id.unique()); gby = {d: gg for d, gg in g.groupby("pilot_id")}
        dboot = []
        for _ in range(DRAWS):
            b = pd.concat([gby[d] for d in rng.choice(gd, len(gd))])
            bt, bf = b[b.truth=="true"].deletion, b[b.truth=="false"].deletion
            if len(bt) and len(bf): dboot.append((bt.mean()-bf.mean())*100)
        lo, hi = np.percentile(dboot, [2.5, 97.5])
        print(f"    {lab:15s} n={len(g):4d}  true {t.mean():7.3f} (n={len(t)})  false {fa.mean():7.3f} (n={len(fa)})  "
              f"diff {t.mean()-fa.mean():7.3f} pp  CI [{lo:.2f}, {hi:.2f}]")
