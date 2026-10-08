"""Score the filled final-sentence BLIND sheet against the KEY: agreement overall, by model and by Claude's label; for the
Claude-false claims, how many you confirm and an exact one-sided 95% upper bound on the share Claude got wrong; whether
your false labels rest on absence or contradiction; then every disagreement. Run from the repo root."""
import csv, re
from scipy.stats import beta

BLIND, KEY = "fve_claims/audit/out/final_sentence_check_BLIND.md", "fve_claims/audit/out/final_sentence_check_KEY.csv"
labels, why, cur = {}, {}, None
for line in open(BLIND):
    if m := re.match(r"^## \d+\. (F\d+)", line):
        cur = m.group(1)
    if (m := re.match(r"^\s*human_label:\s*[*_`\s]*(\w+)(.*)", line)) and cur:  # tolerate **bold**, _italic_, `code`
        labels[cur] = m.group(1).lower()
        why[cur] = next((w for w in ("absent", "contradicted") if w in m.group(2).lower()), "")
rows = list(csv.DictReader(open(KEY)))
key = [k for k in rows if k["item"] in labels]
print(f"labels parsed: {len(key)} of {len(rows)} items; unsure: {sum(labels[k['item']] == 'unsure' for k in key)}")
dec = [k for k in key if labels[k["item"]] in ("true", "false")]
agree = lambda g: f"{sum(labels[k['item']] == k['truth'] for k in g)}/{len(g)}"
print(f"agreement (decided items): {agree(dec)}")
for name, g in [("27B", [k for k in dec if k["model"] == "27B"]), ("7B", [k for k in dec if k["model"] == "7B"]),
                ("Claude true", [k for k in dec if k["truth"] == "true"]), ("Claude false", [k for k in dec if k["truth"] == "false"])]:
    print(f"  {name:12s}: agree {agree(g)}")
cf = [k for k in dec if k["truth"] == "false"]
if cf:
    wrong = sum(labels[k["item"]] != "false" for k in cf)
    print(f"Claude-false claims you also call false: {len(cf) - wrong}/{len(cf)}; share Claude got wrong {wrong}/{len(cf)}, "
          f"one-sided 95% upper bound {beta.ppf(0.95, wrong + 1, len(cf) - wrong):.2f}")
hf = [k for k in dec if labels[k["item"]] == "false"]
print(f"your false labels: absent {sum(why[k['item']] == 'absent' for k in hf)}, contradicted "
      f"{sum(why[k['item']] == 'contradicted' for k in hf)}, unspecified {sum(why[k['item']] == '' for k in hf)}")
for k in key:
    if labels[k["item"]] != k["truth"]:
        print(f"  DISAGREE {k['item']} {k['model']} doc {k['pilot_id']} claim {k['claim_id']} ({k['subtype']}) "
              f"drop {float(k['deletion_pp']):.2f} pp: you {(labels[k['item']] + ' ' + why[k['item']]).strip()}, Claude {k['truth']}")
