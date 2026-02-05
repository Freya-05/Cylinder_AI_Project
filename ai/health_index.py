import pandas as pd

df = pd.read_csv("data/predictions.csv")

# Health index: 1 = healthy, 0 = anomaly
df["health_index"] = df["anomaly"].apply(lambda x: 1 if x == 1 else 0)

# Rolling average health score
df["health_score"] = df["health_index"].rolling(window=20).mean().fillna(1)

df.to_csv("data/health_results.csv", index=False)
print("Health index calculation complete.")
