import numpy as np, pandas as pd, matplotlib.pyplot as plt
rhos = np.linspace(-0.5, 0.95, 200)
sigmas = [0.4, 0.8, 1.2]  # 40%, 80%, 120%
rows=[]
plt.figure(figsize=(8,5))
for s in sigmas:
    apy = np.exp((s**2 * (1 - rhos)) / 4.0) - 1.0
    rows += [{'rho':float(r), 'sigma_annual':s, 'apy_min':float(a)} for r,a in zip(rhos, apy)]
    plt.plot(rhos, apy, label=f'σ={s:.1f}')
pd.DataFrame(rows).to_csv('data/processed/fig05_break_even_vs_rho.csv', index=False)
plt.xlabel('Correlation ρ')
plt.ylabel('Break-even Fee APY (minimum)')
plt.title('CPMM/v2 Break-even Threshold — Risky–Risky (σ_i=σ_j=σ)')
plt.legend(); plt.grid(True, linestyle='--', linewidth=0.5)
plt.tight_layout(); plt.savefig('figures/fig05_break_even_vs_rho.png', dpi=200)
