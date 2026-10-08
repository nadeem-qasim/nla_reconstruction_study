"""Blind label check of the claims the headline rests on: final-sentence claims, 10 Claude-false + 5 Claude-true per model,
at most one claim per document, excluding the documents final_sentence_examples.py shows with labels and the claims in
the earlier spot-check. Each item shows the passage, the AV's final sentence with the claim highlighted, and the claim.
Writes the BLIND sheet and a separate KEY; score with score_final_sentence_sheet.py. Run from the repo root."""
import sys, csv, json, os, random
sys.path.insert(0, "fve_claims/audit")
from claims_data import load, explanations, example_docs, sentence_spans

BLIND, KEY = "fve_claims/audit/out/final_sentence_check_BLIND.md", "fve_claims/audit/out/final_sentence_check_KEY.csv"
SEED, QUOTA = 9, {("27B", "false"): 10, ("7B", "false"): 10, ("27B", "true"): 5, ("7B", "true"): 5}
P = {r["pilot_id"]: r for r in map(json.loads, open("data/redocred_pilot/pilot.jsonl"))}
done = {(k["model"], int(k["pilot_id"]), int(k["claim_id"])) for k in csv.DictReader(open("fve_claims/audit/out/claim_spotcheck_KEY.csv"))}
data = {m: (load(m), explanations(m)) for m in ["7B", "27B"]}

rng, pools = random.Random(SEED), {}
for (m, t) in QUOTA:
    s = data[m][0]
    c = s[s.final_sentence & (s.truth == t) & ~s.pilot_id.isin(example_docs())].sort_values(["pilot_id", "claim_id"])
    c = [r for r in c.itertuples() if (m, r.pilot_id, r.claim_id) not in done]
    rng.shuffle(c); pools[(m, t)] = c
picked, used = [], set()
while any(sum(p[0] == cell for p in picked) < q for cell, q in QUOTA.items()):
    for cell, q in QUOTA.items():   # round robin, so no cell gets first pick of the documents
        if sum(p[0] == cell for p in picked) >= q: continue
        r = next(r for r in pools[cell] if r.pilot_id not in used)
        picked.append((cell, r)); used.add(r.pilot_id)
rng.shuffle(picked)


def highlight(z, spans):
    """The explanation's last sentence with the claim's spans in bold; spans in earlier sentences are listed after it."""
    last = sentence_spans(z)[-1]; a, b = last["start"], last["end"]
    inside = sorted((x for x in spans if a <= x["start"] and x["end"] <= b), key=lambda x: x["start"])
    out, pos = [], a
    for x in inside:
        raw = z[x["start"]:x["end"]]; core = raw.strip(); lead = raw[:len(raw) - len(raw.lstrip())]
        out += [z[pos:x["start"]], lead + "**" + core + "**" + raw[len(lead) + len(core):]]; pos = x["end"]
    earlier = [x["text"] for x in spans if x not in inside]
    return "".join(out + [z[pos:b]]) + (f"  \n(also earlier in the explanation: \"{' … '.join(earlier)}\")" if earlier else "")


B = ["# Final-sentence label check — BLIND (label every item before opening the KEY)", "",
     "Judge each **Claim** against the **Passage** only. The activation is read at the passage's last token. The bold text is",
     "where the claim appears in the AV's final sentence. Write `human_label: true`, `false` or `unsure`:", "",
     "- true = stated in or entailed by the passage",
     "- false = contradicted by the passage, or a specific (name, number, date, place, quote) the passage does not contain.",
     "  After `false`, add `contradicted` or `absent`, e.g. `human_label: false absent`.",
     "- unsure = you can't decide; say why in `note:`.", "",
     "These are the definitions Claude's labels used (fve_claims/ANNOTATION_GUIDE.md, truth v2). Score with",
     "`uv run python fve_claims/audit/score_final_sentence_sheet.py`.", ""]
K = []
for i, ((m, t), r) in enumerate(picked, 1):
    iid = f"F{i:02d}"; z = data[m][1][r.pilot_id]
    B += [f"## {i}. {iid}", "", f"Model {m} · document {r.pilot_id}", "", f"**Passage:** {P[r.pilot_id]['prefix_text']}", "",
          f"**AV's final sentence:** {highlight(z, r.av_spans)}", "", f"**Claim:** {r.proposition}", "",
          "human_label: ", "note: ", ""]
    K.append({"item": iid, "model": m, "pilot_id": r.pilot_id, "claim_id": r.claim_id, "subtype": r.subtype,
              "truth": r.truth, "deletion_pp": round(100 * r.deletion, 3), "rationale": r.rationale})
if os.path.exists(BLIND) and "--force" not in sys.argv:
    sys.exit(f"{BLIND} exists and holds hand-entered labels; pass --force to overwrite it.")
open(BLIND, "w").write("\n".join(B))
with open(KEY, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(K[0])); w.writeheader(); w.writerows(K)
print(f"wrote {BLIND}: {len(K)} items from {len({k['pilot_id'] for k in K})} documents; KEY in {KEY} (do not open until done)")
