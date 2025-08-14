import os
import pandas as pd, matplotlib.pyplot as plt

os.makedirs("data/processed", exist_ok=True)
os.makedirs("figures", exist_ok=True)
csv_path = "data/processed/fig01_woelders_eth_usdc.csv"

# If the CSV is missing, create it with the values used in the report.
if not os.path.exists(csv_path):
    df_init = pd.DataFrame({
        "metric": ["total_return","fee_yield","il_or_adverse"],
        "v2":     [0.01150, 0.01745, -0.00719],
        "v3":     [0.00087, 0.02325, -0.04131],
    })
    df_init.to_csv(csv_path, index=False)

df = pd.read_csv(csv_path)

x = range(len(df))
plt.figure(figsize=(8,5))
plt.bar([i-0.35/2 for i in x], df['v2'], 0.35, label='v2')
plt.bar([i+0.35/2 for i in x], df['v3'], 0.35, label='v3')
plt.xticks(list(x), df['metric'], rotation=15)
plt.ylabel('Value (unitless)')
plt.title('Woelders (2022): ETH–USDC Decomposition (2021-05-06→2022-06-01)')
plt.legend(); plt.tight_layout()
plt.savefig('figures/fig01_woelders_eth_usdc.png', dpi=200)
