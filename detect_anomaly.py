import pandas as pd
import joblib

df = pd.read_csv("logs.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
features = pd.get_dummies(df[["email", "role", "action", "status"]])

model = joblib.load("model.joblib")
df["anomaly"] = model.predict(features)
df["anomaly_label"] = df["anomaly"].apply(lambda x: "Anomaly" if x == -1 else "Normal")

df.to_csv("analyzed_logs.csv", index=False)
print("[INFO] Anomalies detected and saved in analyzed_logs.csv")
