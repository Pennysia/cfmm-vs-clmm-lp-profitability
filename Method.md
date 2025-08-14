# Methods

## Scope
- Focus: volatile (non-stablecoin) pairs; stable–stable pools are out of scope.
- Profit is measured as: **Profit = Fees − LVR − Gas**.

## Data & Sources
- Primary sources: 18 academic/empirical papers listed in `References.md` and `papers/manifest.csv`.
- For each source, we maintain a distilled note with paragraph/section/figure pointers in `evidence/`.

## Measurements
- **Fees:** as reported; fee tiers noted. Compounding aligned to source.
- **LVR / IL:** taken from studies or computed from reported tables/figures. We favor markout- or price–liquidity-based estimators over naive HODL deltas.
- **Gas / re-range:** included when studies report it; otherwise noted as a limitation.

## Figures & Repro
- `data/processed/` contains tidy CSVs used by the plotting scripts in `src/`.
- `src/figure*.py` produce PNGs in `figures/`. Run them with `python src/figureXX_*.py` or `make figures`.
- `data/registry.csv` maps each figure to its data, script, and source(s).

## Assumptions & Caveats
- When combining studies, we preserve their conventions (e.g., markout windows). Cross-study comparisons are qualitative unless stated.
- v3 “time in range” and gas for active rebalancing can materially affect net results; when not reported, we do not impute.
