import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

df = pd.read_csv("logs.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
features = pd.get_dummies(df[["email", "role", "action", "status"]])

model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
model.fit(features)

joblib.dump(model, "model.joblib")
print("✅ Model trained and saved to model.joblib")
