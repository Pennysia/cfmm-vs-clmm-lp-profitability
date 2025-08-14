import pandas as pd, matplotlib.pyplot as plt
df = pd.read_csv('data/processed/fig02_falkenstein_ilfees.csv')
pairs = df['pair'].unique().tolist()
x = range(len(pairs)); w = 0.35
v2 = [df[(df.pair==p) & (df.variant=='v2')]['il_over_fees'].values[0] for p in pairs]
v3 = [df[(df.pair==p) & (df.variant=='v3')]['il_over_fees'].values[0] for p in pairs]
plt.figure(figsize=(9,5))
plt.bar([i-w/2 for i in x], v2, w, label='v2 (IL/Fees)')
plt.bar([i+w/2 for i in x], v3, w, label='v3 (IL/Fees)')
plt.xticks(list(x), pairs, rotation=20)
plt.ylabel('IL / Fees (lower is better)')
plt.title('Falkenstein (2025): IL/Fees — v2 vs v3 (30 bps unless noted)')
plt.legend(); plt.tight_layout()
plt.savefig('figures/fig02_falkenstein_ilfees.png', dpi=200)
