import matplotlib.pyplot as plt

scenarios = ['Down 20%', 'Up 20%']
v2   = [-0.56, -0.46]
v3_a = [-2.34, -1.91]  # [50%,150%]
v3_b = [-4.75, -3.80]  # [75%,125%]

x = range(len(scenarios)); w = 0.22
plt.figure(figsize=(8,5))
plt.bar([i-w for i in x], v2,   w, label='v2 (full range)')
plt.bar(list(x),            v3_a, w, label='v3 [50%,150%]')
plt.bar([i+w for i in x],  v3_b, w, label='v3 [75%,125%]')
plt.xticks(list(x), scenarios)
plt.ylabel('Impermanent Loss (%)')
plt.title('Aigner–Dhaliwal (2021): IL under ±20% Price Move')
plt.legend(); plt.tight_layout()
plt.savefig('figures/fig03_aigner_dhaliwal_20pct.png', dpi=200)
