# cfmm-vs-clmm-lp-profitability

> **Evidence-based analysis of Uniswap LP profitability on non-stablecoin pairs: methods, figures, and citations comparing v2 (CFMM) and v3 (CLMM).**

[![Code: MIT](https://img.shields.io/badge/Code-MIT-informational)](#license) [![Docs: CC BY 4.0](https://img.shields.io/badge/Docs-CC%20BY%204.0-lightgrey)](#license)

## TL;DR

Across **18 sources**, **Uniswap v2 (CFMM) generally delivers higher net LP returns than Uniswap v3 (CLMM)** on **volatile (non-stablecoin)** pairs—despite v3’s higher fee intensity. Drivers: **adverse selection / LVR** and **time out-of-range** on v3. Stable-stable pools are **out of scope** for the main claim.

---

## Contents

* **Report.md** – full write-up with figures and section/paragraph pointers
* **Method.md** – data sources, assumptions, metrics, and how figures are built
* **References.md** – auto-generated bibliography (from `papers/manifest.csv` + `evidence/*.yaml`)
* **Disclaimer.md** – research & limitations notice
* **papers/** – source PDFs + `manifest.csv` (IDs, titles, checksums)
* **evidence/** – one YAML per paper with the exact lines/sections we used
* **data/** – `raw/` verbatim extractions (optional) and `processed/` tidy CSVs for plots
* **figures/** – generated PNGs used by the report
* **src/** – reproducible scripts to build figures and validate links
* **.github/workflows/** – CI to rebuild figures on push
* **LICENSE** (code) & **LICENSE-DOCS** (text/figures)

---

## Quickstart

```bash
# Create and activate a virtual environment (Python 3.10+)
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate

# Install deps
pip install -r requirements.txt
pip install pyyaml              # used by reference/evidence generators

# Build figures → ./figures
make figures

# Normalize/verify figure links inside Report.md
python src/build_report.py

# Auto-generate References.md from manifest + evidence
make refs
```

**Figures produced:**

* `figures/fig01_woelders_eth_usdc.png`
* `figures/fig02_falkenstein_ilfees.png`
* `figures/fig03_aigner_dhaliwal_20pct.png`
* `figures/fig04_break_even_stable_risky.png`
* `figures/fig05_break_even_vs_rho.png`

Open **Report.md** and verify images render.

---

## Reproducibility & Data Provenance

* **papers/manifest.csv** records `paper_id,title,filename,year,authors,venue,doi,url,sha256,bytes`.
  Generate/update via: `python scripts/make_manifest.py`.
* **evidence/** has one **YAML per paper** with:

  * `result_type` (`v2_vs_v3`, `v2_vs_hodl`, `v3_context`, `counter`)
  * `supports_claim` (`yes`, `no`, `mixed`)
  * `claims` with **precise section/paragraph/figure** pointers (what we actually used).
* **data/processed/** contains tidy CSVs used by the plotting scripts in **src/**.

  * `data/registry.csv` maps `figure_id → script, inputs, outputs, sources`.
* **data/raw/** (optional) stores **verbatim** numeric tables extracted from PDFs.

> Large binaries (PDFs/PNGs): use **Git LFS**. `.gitattributes` tracks `papers/*.pdf` and `figures/*.png`.

---

## Method (short version)

* **Profit** = `Fees − LVR − Gas`.
* **Scope**: volatile (non-stablecoin) pairs; stable-stable is out of scope for the main claim.
* **Comparisons**: prioritize direct v2 vs v3 ETH–USD matchups; complement with mechanism papers and cross-sectional v3 studies.
* **Figures**: built from reported tables or from closed-form CPMM thresholds (for v2 break-even).

See **Method.md** for details and caveats.

---

## Auto-generated References

**References.md** is built from `papers/manifest.csv` and enriched by metadata in `evidence/*.yaml`.

* Generate/update:

  ```bash
  python scripts/generate_references.py
  # or
  make refs
  ```
* Classification:

  * **Core**: `result_type ∈ {v2_vs_v3, v2_vs_hodl}` or `supports_claim ∈ {yes, mixed}` (and not `counter`).
  * **Additional**: everything else present in `/papers`.

---

## Health Checks

* **Normalize image paths & validate report links**

  ```bash
  python src/build_report.py
  ```

  Ensures `Report.md` uses `figures/*.png` and that each referenced figure exists.

* **Verify manifest ↔ evidence ↔ figures**

  ```bash
  python scripts/verify_repo.py
  ```

  Fails if: missing/duplicate evidence IDs, missing figures, or registry mismatch.

* **CI on push**
  `.github/workflows/build.yml` installs deps and runs the five `src/figure*.py` scripts to rebuild images.

---

## Repository Tree (key parts)

```
cfmm-vs-clmm-lp-profitability/
├─ Report.md
├─ Method.md
├─ References.md
├─ Disclaimer.md
├─ README.md
├─ LICENSE
├─ LICENSE-DOCS
├─ CITATION.cff
├─ CHANGELOG.md
├─ requirements.txt
├─ Makefile
├─ .github/workflows/build.yml
├─ papers/
│  ├─ manifest.csv
│  └─ *.pdf
├─ evidence/
│  └─ NN_<slug>.yaml
├─ data/
│  ├─ registry.csv
│  ├─ raw/        # optional: verbatim tables (keep .keep if empty)
│  └─ processed/  # tidy CSVs used in plots
├─ figures/
│  └─ fig01..05_*.png
└─ src/
   ├─ figure01_woelders.py
   ├─ figure02_falkenstein.py
   ├─ figure03_aigner_dhaliwal.py
   ├─ figure04_break_even_stable_risky.py
   ├─ figure05_break_even_vs_rho.py
   ├─ utils.py
   └─ build_report.py
```

---

## Contributing

PRs that:

* correct citations/paragraph pins,
* improve reproducibility (data → figure), or
* add **non-duplicative** sources with clear scope/metrics

are welcome. Keep tone neutral; avoid investment advice. For major additions, open an issue first.

---

## How to Cite

> **cfmm-vs-clmm-lp-profitability** (year of latest update). Evidence-based analysis of Uniswap LP profitability on non-stablecoin pairs: methods, figures, and citations comparing v2 (CFMM) and v3 (CLMM). GitHub repository.

There’s a **CITATION.cff** so GitHub can render a citation snippet automatically.

---

## License

* **Code** (`src/`, scripts): **MIT** – see `LICENSE`.
* **Text/figures** (`Report.md`, `Method.md`, `References.md`, `figures/`): **CC BY 4.0** – see `LICENSE-DOCS`.
* **Third-party papers** in `papers/` remain under their original copyrights.

---

## Disclaimer

This is **research content**, not investment advice. Results depend on assumptions (fee tiers, markouts, gas/re-range policy). See **Disclaimer.md** and **Method.md** for limitations.
