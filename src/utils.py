import os, re, csv, hashlib
from typing import List, Dict

IMG_REGEX = re.compile(r'!\[[^]]*\]\(([^)]+)\)')

def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1<<20), b""):
            h.update(chunk)
    return h.hexdigest()

def figure_paths_in_markdown(md_path: str) -> List[str]:
    with open(md_path, "r", encoding="utf-8") as f:
        txt = f.read()
    return IMG_REGEX.findall(txt)

def replace_paths_in_markdown(md_path: str, mapping: Dict[str,str]) -> int:
    with open(md_path, "r", encoding="utf-8") as f:
        txt = f.read()
    n = 0
    for old, new in mapping.items():
        if old in txt:
            txt = txt.replace(old, new); n += 1
    if n:
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(txt)
    return n

def read_registry(path="data/registry.csv"):
    rows=[]
    if not os.path.exists(path): return rows
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return rows
