import numpy as np, matplotlib.pyplot as plt
sigmas = np.linspace(0.1, 1.5, 200)  # 10% to 150% annualized
apy = np.exp((sigmas**2)/8.0) - 1.0
plt.figure(figsize=(8,5))
plt.plot(sigmas, apy)
plt.xlabel('Annualized Volatility σ (risky asset)')
plt.ylabel('Break-even Fee APY (minimum)')
plt.title('CPMM/v2 Break-even Threshold — Stable–Risky (σ_j≈0)')
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tight_layout(); plt.savefig('figures/fig04_break_even_stable_risky.png', dpi=200)
