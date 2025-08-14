import os, re, csv, hashlib, pathlib
papers_dir = pathlib.Path("papers")
out_path = papers_dir / "manifest.csv"
papers = sorted([p for p in papers_dir.iterdir() if p.suffix.lower()==".pdf"])

def sha256(fp):
    h = hashlib.sha256()
    with open(fp, "rb") as f:
        for chunk in iter(lambda: f.read(1<<20), b""):
            h.update(chunk)
    return h.hexdigest()

def guess_title(name: str) -> str:
    base = os.path.splitext(name)[0]
    base = base.replace('_', ' ')
    base = re.sub(r'\s+', ' ', base).strip()
    base = re.sub(r'\s+\.$', '', base)  # handle filenames ending with " .pdf"
    return base

def guess_year(name: str) -> str:
    m = re.search(r'(19|20)\d{2}', name)
    return m.group(0) if m else ""

papers_dir.mkdir(exist_ok=True)
with open(out_path, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["paper_id","title","filename","year","authors","venue","doi","url","sha256","bytes"])
    for i, p in enumerate(papers, 1):
        w.writerow([
            f"{i:02d}",
            guess_title(p.name),
            p.name,
            guess_year(p.name),
            "", "", "", "",
            sha256(p),
            p.stat().st_size
        ])
print(f"Wrote {out_path} with {len(papers)} rows.")
