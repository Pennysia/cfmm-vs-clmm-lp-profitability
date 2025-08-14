#!/usr/bin/env python3
import csv, os, re, sys, glob, textwrap
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML not installed. Run: python -m pip install pyyaml", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "papers" / "manifest.csv"
EVID   = ROOT / "evidence"
OUT    = ROOT / "References.md"

def read_manifest():
    rows = []
    with PAPERS.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rows.append(r)
    return rows

def read_evidence():
    """Return dict by paper_id -> metadata from YAML (authors, year, title, result_type, supports_claim)."""
    out = {}
    for p in sorted(EVID.glob("*.yaml")):
        pid = p.name.split("_", 1)[0]
        try:
            y = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        except Exception:
            y = {}
        if not isinstance(y, dict): y = {}
        out[pid] = {
            "title": y.get("title", ""),
            "authors": y.get("authors", y.get("author", "")),
            "year": str(y.get("year", "")).strip(),
            "result_type": y.get("result_type", "").lower(),
            "supports_claim": str(y.get("supports_claim", "")).lower(),
        }
    return out

def guess_year(s):
    m = re.search(r'(19|20)\d{2}', s or "")
    return m.group(0) if m else ""

def norm_authors(a):
    if isinstance(a, list): return "; ".join(a)
    return str(a).strip()

def md_entry(title, filename, authors="", year=""):
    title = title.strip()
    if not title: title = filename
    if authors and year:
        head = f"**{authors} ({year}).** *{title}.*"
    elif authors:
        head = f"**{authors}.** *{title}.*"
    elif year:
        head = f"*{title}* ({year})."
    else:
        head = f"*{title}*."
    return f"- {head}  \n  (papers/{filename})"

def classify(row, ev):
    """Return 'core' if result_type in {v2_vs_v3, v2_vs_hodl} or supports_claim in {yes, mixed} (but not 'counter')."""
    rt = (ev.get("result_type") or "").lower()
    sc = (ev.get("supports_claim") or "").lower()
    if rt in {"v2_vs_v3", "v2_vs_hodl"}: return "core"
    if sc in {"yes", "mixed"} and rt != "counter": return "core"
    return "additional"

def generate():
    if not PAPERS.exists():
        print("papers/manifest.csv not found.", file=sys.stderr)
        sys.exit(1)

    manifest = read_manifest()
    evidence = read_evidence()

    core, addl = [], []
    for r in manifest:
        pid = r["paper_id"]
        fn  = r["filename"]
        # prefer evidence metadata; fall back to manifest, then filename heuristics
        ev  = evidence.get(pid, {})
        title = ev.get("title") or r.get("title") or os.path.splitext(fn)[0].replace("_"," ").strip()
        authors = norm_authors(ev.get("authors") or r.get("authors",""))
        year = ev.get("year") or r.get("year") or guess_year(title) or guess_year(fn)

        line = md_entry(title=title, filename=fn, authors=authors, year=year)
        (core if classify(r, ev) == "core" else addl).append(line)

    header = textwrap.dedent("""\
        # References

        This file is auto-generated from `papers/manifest.csv` and `evidence/*.yaml`.
        - Update **titles/authors/year** in the evidence YAMLs to improve entries.
        - Classification:
          - **Core**: `result_type` ∈ {`v2_vs_v3`, `v2_vs_hodl`} or `supports_claim` ∈ {`yes`, `mixed`} (and not `counter`)
          - **Additional**: everything else
        """)

    core_md = "## Core references used directly in the report\n\n" + ("\n".join(core) if core else "_(none yet)_")
    addl_md = "\n\n## Additional references present in `/papers`\n\n" + ("\n".join(addl) if addl else "_(none yet)_")

    OUT.write_text(header + "\n" + core_md + addl_md + "\n", encoding="utf-8")
    print(f"Wrote {OUT} — {len(core)} core, {len(addl)} additional, total {len(manifest)}.")

if __name__ == "__main__":
    generate()
