import matplotlib.pyplot as plt

metrics = ['Total Return', 'Fee Yield', 'Adverse Selection / IL']
v2 = [0.01150, 0.01745, -0.00719]
v3 = [0.00087, 0.02325, -0.04131]

x = range(len(metrics)); w = 0.35
plt.figure(figsize=(8,5))
plt.bar([i-w/2 for i in x], v2, w, label='v2')
plt.bar([i+w/2 for i in x], v3, w, label='v3')
plt.xticks(list(x), metrics, rotation=15)
plt.ylabel('Value (unitless)')
plt.title('Woelders (2022): ETH–USDC Decomposition (2021-05-06→2022-06-01)')
plt.legend(); plt.tight_layout()
plt.savefig('figures/fig01_woelders_eth_usdc.png', dpi=200)
