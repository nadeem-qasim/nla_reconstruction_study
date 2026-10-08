"""Shared loaders for the audit scripts: per-claim deletion and paraphrase scores joined to the claim labels, with the
final-sentence tag. The 7B tag comes from 07_tag_final_sentence.py; the 27B tag is computed here the same way (a claim is
final-sentence when its last av_span sits in the explanation's last sentence). Import from scripts run at the repo root."""
import sys, glob, json, random
sys.path.insert(0, "fve_claims")
import numpy as np, pandas as pd
from atomic import sentence_spans

AV = {"7B": ["fve_claims/01_av_7b.jsonl"],
      "27B": ["fve_claims/01_av_27b_25.jsonl", "fve_claims/01_av_27b_25_50.jsonl", "fve_claims/01_av_27b_50_100.jsonl"]}
LABELS = {"7B": "fve_claims/tasks/02_atoms_7b_doc*.jsonl", "27B": "fve_claims/tasks/02_atoms_27b_doc*.jsonl"}
SETTINGS_D_LOCAL = {"7B": "fve_claims/04_b0_25_settings.json", "27B": "fve_claims/04_06_27b_full_settings.json"}
D_RELEASED_7B = 0.7335
EXAMPLE_SEED, N_EXAMPLE_DOCS = 2026, 5   # documents shown with labels by final_sentence_examples.py


def labels(pattern, extra=()):
    recs = {}
    for f in sorted(glob.glob(pattern)):
        for l in open(f):
            r = json.loads(l); recs[(r["pilot_id"], r["claim_id"])] = r
    df = pd.DataFrame(recs.values())
    keep = ["pilot_id", "claim_id", "truth", "type", "subtype", "proposition", "rationale", "av_spans"] + list(extra)
    return df[[c for c in keep if c in df.columns]]


def explanations(model):
    """pilot_id -> the explanation text the claims' av_spans index into."""
    out = {}
    for f in AV[model]:
        for l in open(f):
            g = json.loads(l)
            out[g["pilot_id"]] = g["explanation"] if g["parse_ok"] else g["raw_generation"]
    return out


def load(model):
    """True/false claims with columns z, dl, hv (FVE of the explanation, the deletion and the heavy paraphrase, local
    denominator), deletion and paraphrase (drops as fractions), final_sentence and del_chars (deleted characters)."""
    if model == "27B":
        s = pd.read_csv("fve_claims/04_06_scores_27b_full.csv").merge(labels(LABELS["27B"]), on=["pilot_id", "claim_id"])
        s = s.assign(z=s.fve_z, dl=s.fve_del, hv=s.fve_heavy)
    else:
        s = pd.concat([pd.read_csv(f) for f in sorted(glob.glob("fve_claims/04_scores_7b_b*.csv"))])
        s = s.merge(pd.read_csv("fve_claims/06_scores_7b_paraphrase.csv")[["pilot_id", "claim_id", "fve_heavy_local"]],
                    on=["pilot_id", "claim_id"])
        s = s.merge(labels(LABELS["7B"], extra=["final_sentence"]), on=["pilot_id", "claim_id"])
        s = s.assign(z=s.fve_z_local, dl=s.fve_del_local, hv=s.fve_heavy_local)
    s = s[s.truth.isin(["true", "false"])].copy()
    if "final_sentence" not in s.columns:
        ns = {p: len(sentence_spans(z)) for p, z in explanations(model).items()}
        s["final_sentence"] = [max(x["sentence_id"] for x in sp) == ns[p] - 1 for p, sp in zip(s.pilot_id, s.av_spans)]
    s["deletion"] = s.z - s.dl
    s["paraphrase"] = s.z - s.hv
    s["del_chars"] = [sum(len(x["text"]) for x in sp) for sp in s.av_spans]
    return s


def auroc(pos, neg):
    """Mann-Whitney AUROC with ties at 0.5."""
    if len(pos) == 0 or len(neg) == 0: return np.nan
    r = pd.Series(np.concatenate([pos, neg])).rank().values
    return (r[:len(pos)].sum() - len(pos) * (len(pos) + 1) / 2) / (len(pos) * len(neg))


def d_local(model):
    return json.load(open(SETTINGS_D_LOCAL[model]))["D_local"]


def example_docs():
    """The documents final_sentence_examples.py prints with Claude's labels; the blind sheet excludes them."""
    return sorted(random.Random(EXAMPLE_SEED).sample(range(100), N_EXAMPLE_DOCS))
