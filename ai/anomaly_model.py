import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

df = pd.read_csv("data/processed_data.csv")

features = ["pressure", "position", "velocity"]
X = df[features]

model = IsolationForest(contamination=0.05, random_state=42)
df["anomaly"] = model.fit_predict(X)

joblib.dump(model, "models/anomaly_model.pkl")
df.to_csv("data/predictions.csv", index=False)

print("Anomaly detection complete. predictions.csv saved.")
