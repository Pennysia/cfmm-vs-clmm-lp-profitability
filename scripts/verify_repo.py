import csv, os, re, sys, glob, yaml

OK = True

def fail(msg):
    global OK
    print("FAIL:", msg); OK = False

# 1) manifest ↔ evidence (1-to-1)
manifest = list(csv.DictReader(open("papers/manifest.csv", newline="", encoding="utf-8")))
ids = {r["paper_id"] for r in manifest}
evidence = glob.glob("evidence/*.yaml")
id_from_name = lambda n: re.match(r"^(\d{2})_", os.path.basename(n)).group(1) if re.match(r"^(\d{2})_", os.path.basename(n)) else None
ids_seen = [id_from_name(p) for p in evidence]
if None in ids_seen:
    fail("Some evidence files don't begin with NN_…")
id_counts = {}
for i in ids_seen:
    id_counts[i] = id_counts.get(i, 0) + 1
dupes = [k for k,v in id_counts.items() if v>1]
missing = sorted(ids - set([i for i in ids_seen if i]))
if dupes:
    fail(f"Duplicate evidence IDs: {dupes}")
if missing:
    fail(f"Missing evidence for IDs: {missing}")

# 2) Report → figures exist
import re
md = open("Report.md", encoding="utf-8").read()
paths = re.findall(r'!\[[^]]*\]\(([^)]+)\)', md)
missing_figs = [p for p in paths if p.startswith("figures/") and not os.path.exists(p)]
if missing_figs:
    fail(f"Report references missing figures: {missing_figs}")

# 3) registry covers produced figures
reg = list(csv.DictReader(open("data/registry.csv", newline="", encoding="utf-8"))) if os.path.exists("data/registry.csv") else []
reg_outs = {r.get("outputs","") for r in reg}
produced = set(glob.glob("figures/*.png"))
not_in_reg = [p for p in produced if p not in reg_outs]
if not_in_reg:
    fail(f"Figures not listed in data/registry.csv: {not_in_reg}")

print("\nSUMMARY:")
print(f" - Manifest entries: {len(manifest)}")
print(f" - Evidence files  : {len([e for e in evidence if id_from_name(e)])}")
print(f" - Figures         : {len(produced)}")
print(f" - Report refs     : {len([p for p in paths if p.startswith('figures/')])}")

sys.exit(0 if OK else 1)
