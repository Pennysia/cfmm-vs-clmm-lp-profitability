import os
import pandas as pd, matplotlib.pyplot as plt

os.makedirs("data/processed", exist_ok=True)
os.makedirs("figures", exist_ok=True)
csv_path = "data/processed/fig02_falkenstein_ilfees.csv"

# Seed CSV if missing (numbers from the report)
if not os.path.exists(csv_path):
    df_init = pd.DataFrame([
        ["ETH–USDC (CEX)","v2",0.55],
        ["ETH–USDC (CEX)","v3",1.16],
        ["ETH–USDC (TWAP)","v2",0.51],
        ["ETH–USDC (TWAP)","v3",1.11],
        ["ETH–USDT (CEX)","v2",0.51],
        ["ETH–USDT (CEX)","v3",1.16],
        ["ETH–USDT (TWAP)","v2",0.47],
        ["ETH–USDT (TWAP)","v3",1.11],
        ["PEPE–ETH","v2",0.74],
        ["PEPE–ETH","v3",0.85],
    ], columns=["pair","variant","il_over_fees"])
    df_init.to_csv(csv_path, index=False)

df = pd.read_csv(csv_path)

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
