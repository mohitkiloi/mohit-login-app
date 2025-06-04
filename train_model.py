import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import precision_score, recall_score, f1_score
import joblib
import json
import os

df = pd.read_csv("logs.csv")
features = []
labels = []

for _, row in df.iterrows():
    try:
        width, height = map(int, row['screen_resolution'].split("x"))
    except:
        width, height = 0, 0

    features.append([
        1 if row['status'] == 'failure' else 0,
        width,
        height,
        len(str(row['user_agent'])),
        len(str(row['location']))
    ])
    labels.append(1 if row.get("attack_type", "normal") != "normal" else 0)

model = IsolationForest(contamination=0.15, random_state=42)
model.fit(features)
joblib.dump(model, "model.joblib")

preds = model.predict(features)
preds = [1 if p == -1 else 0 for p in preds]

precision = precision_score(labels, preds)
recall = recall_score(labels, preds)
f1 = f1_score(labels, preds)

metrics = {
    "model": "IsolationForest",
    "accuracy": round((sum([1 for i in range(len(preds)) if preds[i] == labels[i]]) / len(preds)), 4),
    "precision": round(precision, 4),
    "recall": round(recall, 4),
    "f1_score": round(f1, 4),
    "anomaly_threshold": -0.15
}

# Save metrics
os.makedirs("experiments", exist_ok=True)
with open("experiments/metrics_report.json", "w") as f:
    json.dump(metrics, f, indent=4)

# Print for Jenkins
print("\n📊 Model Metrics:")
for k, v in metrics.items():
    print(f"{k}: {v}")
