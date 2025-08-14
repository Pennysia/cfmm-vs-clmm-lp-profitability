Here’s a clean, ready-to-paste **README.md** for your repo.

---

# cfmm-vs-clmm-lp-profitability

> **Evidence-based analysis of Uniswap LP profitability on non-stablecoin pairs: methods, figures, and citations comparing v2 (CFMM) and v3 (CLMM).**

[![License: MIT](https://img.shields.io/badge/Code%20License-MIT-informational.svg)](#license) [![Docs: CC BY 4.0](https://img.shields.io/badge/Docs-CC%20BY%204.0-lightgrey.svg)](#license)

## TL;DR

Across the sources we analyze, **Uniswap v2 (CFMM) generally delivers higher *net* LP returns than Uniswap v3 (CLMM) for volatile (non-stablecoin) pairs**, despite v3’s higher fee intensity. The difference is driven by adverse selection / LVR** and time spent out-of-range on v3; stable-stable pools are out of scope.

---

## Contents

* **Report.md** – full write-up with figures and citations
* **Method.md** – data sources, assumptions, and how each figure/table was built
* **References.md** – bibliography (mirrors the in-report references)
* **Disclaimer.md** – research & limitations notice
* **papers/** – source PDFs (+ `manifest.csv`)
* **evidence/** – per-paper distilled notes with paragraph/section pinpoints
* **data/** – `raw/` inputs (if any) and `processed/` tidy CSVs used for figures
* **figures/** – generated PNGs
* **src/** – scripts to build tables/figures (reproducible)
* **.github/workflows/** – CI: build figures on push
* **LICENSE** (code) & **LICENSE-DOCS** (text/figures)

A more detailed tree is in the repo’s root **README** comments or can be regenerated with `tree -a -L 2`.

---

## Quickstart

```bash
# Create and enter a virtual environment (Python 3.10+)
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Build figures (outputs to ./figures)
make figures
```

**Figures produced** (filenames may vary slightly depending on your `src/` scripts):

* `figures/fig01_woelders_eth_usdc.png`
* `figures/fig02_falkenstein_ilfees.png`
* `figures/fig03_aigner_dhaliwal_20pct.png`
* `figures/fig04_break_even_stable_risky.png`
* `figures/fig05_break_even_vs_rho.png`

Then open **Report.md** (links point to these images).

---

## Reproducibility & Data Provenance

* **Papers** live in `papers/` with a **`manifest.csv`** capturing: `paper_id,title,authors,year,venue,doi/url,checksum`.
* **Evidence notes**: each paper has a YAML in `evidence/` with only the facts used in the report and **section/paragraph/figure** pointers.
* **Processed CSVs** used for figures (if any) live in `data/processed/` and are referenced by the scripts in `src/`.
* **Figure registry**: `data/registry.csv` maps `figure_id → sources + method + script`.

> **Important:** Large PDFs/PNGs should use **Git LFS**. This repo includes a `.gitattributes` that tracks `papers/*.pdf` and `figures/*.png`.

---

## Method (short version)

* **Profit definition:** `Profit = Fees − LVR − Gas`.
* **Scope:** volatile (non-stablecoin) pairs; stable-stable pools are excluded from the claim.
* **Comparisons:** direct v2 vs v3 head-to-head where available (e.g., ETH–USD), plus structural/empirical studies for mechanism evidence.
* **Figures:** built from tables/values reported in the sources or from closed-form thresholds (for CPMM break-even).

Full details live in **Method.md**.

---

## How to Cite

Please cite the repository (and any release/DOI you mint) as:

> *cfmm-vs-clmm-lp-profitability: Evidence-based analysis of Uniswap LP profitability on non-stablecoin pairs* (year of latest update).
> Available at: [https://github.com/your-org/cfmm-vs-clmm-lp-profitability](https://github.com/your-org/cfmm-vs-clmm-lp-profitability)

There’s also a **CITATION.cff** so GitHub can generate a citation snippet automatically.

---

## Contributing

Issues and PRs that:

* correct citations/paragraph pointers,
* improve figure reproducibility,
* or add vetted, **non-duplicative** sources

are welcome. Please keep tone neutral and avoid investment advice. For larger additions, open an issue first to align on scope.

---

## License

* **Code** (in `src/`, build scripts): **MIT** – see `LICENSE`
* **Text, figures, and other content** (e.g., `Report.md`, `Method.md`, `References.md`, `figures/`): **CC BY 4.0** – see `LICENSE-DOCS`
* **Third-party papers** remain under their original copyrights (see `papers/manifest.csv`).

---

## Disclaimer

This is **research content**. It is **not** investment advice. Results depend on assumptions (e.g., fee tiers, markouts, gas/re-range policies). See **Disclaimer.md** and **Method.md** for details and limitations.



## Maintainers / Contact

* Name – email or handle
* Organization (optional)

---

### Handy commands

```bash
# Build all figures
make figures

# Clean generated outputs
make clean

# (Optional) Check your Python env
python -V && pip -V
```

If you want, I can also generate stub files for `papers/manifest.csv`, `data/registry.csv`, and `evidence/*.yaml` with your current 17 sources so the repo is runnable end-to-end on first clone.
