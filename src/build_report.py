import os, sys
from utils import figure_paths_in_markdown, replace_paths_in_markdown, read_registry

REPORT = "Report.md"

# 1) Normalize legacy image paths -> local figures/
MAPPING = {
    "sandbox:/mnt/data/chart_woelders_eth_usdc.png": "figures/fig01_woelders_eth_usdc.png",
    "sandbox:/mnt/data/chart_falkenstein_ilfees.png": "figures/fig02_falkenstein_ilfees.png",
    "sandbox:/mnt/data/chart_aigner_dhaliwal_20pct.png": "figures/fig03_aigner_dhaliwal_20pct.png",
    "sandbox:/mnt/data/chart_break_even_stable_risky.png": "figures/fig04_break_even_stable_risky.png",
    "sandbox:/mnt/data/chart_break_even_vs_rho_symmetric.png": "figures/fig05_break_even_vs_rho.png",
}

changed = replace_paths_in_markdown(REPORT, MAPPING)
print(f"[build_report] path replacements: {changed}")

# 2) Check that every referenced figure exists
paths = figure_paths_in_markdown(REPORT)
missing = [p for p in paths if p.startswith("figures/") and not os.path.exists(p)]
if missing:
    print("[build_report] MISSING figure files:")
    for m in missing: print(" -", m)
    sys.exit(1)

# 3) Registry consistency (optional)
reg = read_registry("data/registry.csv")
reg_outs = {r.get("outputs","") for r in reg}
missing_in_registry = [p for p in paths if p.startswith("figures/") and p not in reg_outs]
if missing_in_registry:
    print("[build_report] Figures referenced but not in data/registry.csv:")
    for p in missing_in_registry: print(" -", p)
else:
    print("[build_report] registry looks consistent.")

print("[build_report] OK.")
