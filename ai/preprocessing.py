import pandas as pd

print("Preprocessing started...")

df = pd.read_csv("data/raw_data.csv")
print("Columns found:", df.columns.tolist())

# Normalize column names
df.columns = df.columns.str.strip().str.lower()

required = ["time", "pressure", "position"]
if not all(col in df.columns for col in required):
    raise ValueError(f"CSV must contain: {required}")

# Feature engineering
df["pressure_change"] = df["pressure"].diff().fillna(0)
df["position_change"] = df["position"].diff().fillna(0)
df["velocity"] = df["position_change"] / df["time"].diff().fillna(1)

df.to_csv("data/processed_data.csv", index=False)
print("processed_data.csv saved successfully.")
