import matplotlib.pyplot as plt

pairs = ['ETH–USDC (CEX)', 'ETH–USDC (TWAP)', 'ETH–USDT (CEX)', 'ETH–USDT (TWAP)', 'PEPE–ETH']
v2 =  [0.55, 0.51, 0.51, 0.47, 0.74]
v3 =  [1.16, 1.11, 1.16, 1.11, 0.85]

x = range(len(pairs)); w = 0.35
plt.figure(figsize=(9,5))
plt.bar([i-w/2 for i in x], v2, w, label='v2 (IL/Fees)')
plt.bar([i+w/2 for i in x], v3, w, label='v3 (IL/Fees)')
plt.xticks(list(x), pairs, rotation=20)
plt.ylabel('IL / Fees (lower is better)')
plt.title('Falkenstein (2025): IL/Fees — v2 vs v3 (30 bps unless noted)')
plt.legend(); plt.tight_layout()
plt.savefig('figures/fig02_falkenstein_ilfees.png', dpi=200)
