"""What the verbalizer's final sentence looks like in each model: for the same five random documents (claims_data.
example_docs), the end of the passage, then each model's final sentence and the true/false claims in it with Claude's
label and the deletion drop. The blind sheet (make_final_sentence_sheet.py) excludes these documents. Writes
fve_claims/audit/out/final_sentence_examples.md. Run from the repo root."""
import sys, json
sys.path.insert(0, "fve_claims/audit")
from claims_data import load, explanations, example_docs, sentence_spans

OUT, TAIL = "fve_claims/audit/out/final_sentence_examples.md", 300
P = {r["pilot_id"]: r for r in map(json.loads, open("data/redocred_pilot/pilot.jsonl"))}
data = {m: (load(m), explanations(m)) for m in ["7B", "27B"]}

L = ["# Final-sentence examples", "",
     f"Documents {example_docs()} (random, seed in claims_data.py). The activation is read at the last token of the passage.",
     "Drops are percentage points of FVE with each model's local denominator. Claims are atomic propositions; "
     "labels are Claude's.", ""]
for pid in example_docs():
    p = P[pid]["prefix_text"]
    L += [f"## Document {pid}: {P[pid]['title']}", "", f"**End of passage:** …{p[-TAIL:]}", ""]
    for m, (s, z) in data.items():
        last = sentence_spans(z[pid])[-1]["text"]
        c = s[(s.pilot_id == pid) & s.final_sentence].sort_values("claim_id")
        L += [f"**{m} final sentence:** {last}", "", "| claim | subtype | Claude | drop (pp) |", "|---|---|---|---|"]
        L += [f"| {r.proposition} | {r.subtype} | {r.truth} | {100 * r.deletion:.2f} |" for r in c.itertuples()]
        L += [""]
open(OUT, "w").write("\n".join(L))
print(f"wrote {OUT}: documents {example_docs()}")
