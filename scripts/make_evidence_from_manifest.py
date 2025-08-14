import csv, os, pathlib, yaml, re

def slug(s: str) -> str:
    s = s.lower()
    s = re.sub(r'[^a-z0-9]+', '_', s).strip('_')
    return s[:80]

pathlib.Path("evidence").mkdir(exist_ok=True)

with open("papers/manifest.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        pid = row["paper_id"]
        title = row["title"] or row["filename"]
        fname = row["filename"]
        year = row.get("year","")
        out = f"evidence/{pid}_{slug(title)}.yaml"
        stub = {
            "paper_id": pid,
            "filename": fname,
            "title": title,
            "year": year,
            "citation": "",                # fill later
            "result_type": "tbd",          # v2_vs_v3 | v2_vs_hodl | v3_context | counter
            "supports_claim": "tbd",       # yes | no | mixed
            "claims": [],                  # add paragraph/section pointers you used
            "caveats": []
        }
        with open(out, "w") as o:
            yaml.dump(stub, o, sort_keys=False, allow_unicode=True)
        print("wrote", out)
