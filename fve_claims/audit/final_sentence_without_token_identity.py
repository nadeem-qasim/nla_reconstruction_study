"""Compare final-verbalizer-sentence deletion drops before/after excluding token identity.

Uses the existing final_sentence tag and subtype labels; excludes final_token and
final_word from BOTH truth classes. Other local facts and syntax claims remain.
No model inference or relabeling. Means weight claims equally; confidence intervals
resample documents, preserving within-document dependence. Run from the repo root.
"""
import json
from pathlib import Path

import numpy as np

from claims_data import load

SEED, DRAWS = 0, 4000
EXCLUDED = {"final_token", "final_word"}
OUT = Path(__file__).resolve().parent / "out/final_sentence_without_token_identity.json"


def summarize(frame):
    sums = frame.groupby(["pilot_id", "truth"]).deletion.sum().unstack(fill_value=0)
    counts = frame.groupby(["pilot_id", "truth"]).size().unstack(fill_value=0)
    sums = sums.reindex(columns=["true", "false"], fill_value=0).to_numpy() * 100
    counts = counts.reindex(columns=["true", "false"], fill_value=0).to_numpy()
    rng = np.random.default_rng(SEED)
    indices = rng.integers(0, len(sums), size=(DRAWS, len(sums)))
    boot_counts = counts[indices].sum(axis=1)
    valid = (boot_counts > 0).all(axis=1)
    boots = sums[indices].sum(axis=1)[valid] / boot_counts[valid]
    means = sums.sum(axis=0) / counts.sum(axis=0)
    result = {"documents": int(len(sums)), "valid_bootstrap_draws": int(valid.sum())}
    for i, truth in enumerate(["true", "false"]):
        result[truth] = {
            "claims": int(counts[:, i].sum()),
            "documents": int((counts[:, i] > 0).sum()),
            "mean_drop_pp": float(means[i]),
            "ci95_pp": np.percentile(boots[:, i], [2.5, 97.5]).tolist(),
        }
    result["true_minus_false_pp"] = float(means[0] - means[1])
    result["gap_ci95_pp"] = np.percentile(boots[:, 0] - boots[:, 1], [2.5, 97.5]).tolist()
    return result


def main():
    output = {
        "filter": "final verbalizer sentence; exclude subtypes final_token and final_word from both truth classes",
        "scope": "Explicit token/word identity only; other claims about the source ending remain.",
        "score": "100 * (FVE_original - FVE_deleted), using each model's local denominator",
        "intervals": "95% percentile document-cluster bootstrap; equal claim weighting",
        "seed": SEED, "draws": DRAWS, "models": {},
    }
    for model in ["7B", "27B"]:
        data = load(model)
        assert not data.duplicated(["pilot_id", "claim_id"]).any()
        assert np.isfinite(data.deletion).all()
        final = data.loc[data.final_sentence].copy()
        excluded = final.subtype.isin(EXCLUDED)
        kept = final.loc[~excluded]
        assert len(kept) + int(excluded.sum()) == len(final)
        result = {
            "excluded_counts": {t: int((final.loc[excluded, "truth"] == t).sum()) for t in ["true", "false"]},
            "original": summarize(final), "without_token_identity": summarize(kept),
        }
        output["models"][model] = result
        for name in ["original", "without_token_identity"]:
            row = result[name]
            lo, hi = row["gap_ci95_pp"]
            print(f"{model} {name}: true {row['true']['mean_drop_pp']:.3f} pp "
                  f"(n={row['true']['claims']}), false {row['false']['mean_drop_pp']:.3f} pp "
                  f"(n={row['false']['claims']}); gap {row['true_minus_false_pp']:.3f} pp "
                  f"[95% CI {lo:.3f}, {hi:.3f}]")
        print(f"  excluded: {result['excluded_counts']}")
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(output, indent=2) + "\n")
    print(f"Saved {OUT}")


if __name__ == "__main__":
    main()
