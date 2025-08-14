import pandas as pd, matplotlib.pyplot as plt
df = pd.read_csv('data/processed/fig03_aigner_dhaliwal_20pct.csv')
scenarios = ['down_20','up_20']; w = 0.22
x = range(len(scenarios))
def val(s, series): return df[(df.scenario==s) & (df.series==series)]['value_pct'].values[0]
plt.figure(figsize=(8,5))
plt.bar([i-w for i in x], [val(s,'v2') for s in scenarios], w, label='v2 (full range)')
plt.bar([i for i in x],    [val(s,'v3_50_150') for s in scenarios], w, label='v3 [50%,150%]')
plt.bar([i+w for i in x],  [val(s,'v3_75_125') for s in scenarios], w, label='v3 [75%,125%]')
plt.xticks(list(x), ['Down 20%','Up 20%'])
plt.ylabel('Impermanent Loss (%)')
plt.title('Aigner–Dhaliwal (2021): IL under ±20% Price Move')
plt.legend(); plt.tight_layout()
plt.savefig('figures/fig03_aigner_dhaliwal_20pct.png', dpi=200)
