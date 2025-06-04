import joblib
import numpy as np
import os
import pandas as pd

# Load trained model
MODEL_PATH = "model.joblib"
model = joblib.load(MODEL_PATH) if os.path.exists(MODEL_PATH) else None

# Feature extraction
def preprocess(log_row):
    try:
        width, height = log_row["screen_resolution"].split("x")
        width = int(width)
        height = int(height)
    except:
        width, height = 0, 0

    features = [
        1 if log_row["status"] == "failure" else 0,
        width,
        height,
        len(str(log_row["user_agent"])),
        len(str(log_row["location"]))
    ]
    return np.array(features).reshape(1, -1)

# Predict single row
def detect_single_login(log_row):
    if model is None:
        return False, "Model not found", 0.0
    features = preprocess(log_row)
    score = model.decision_function(features)[0]
    prediction = model.predict(features)[0]  # -1 = anomaly
    is_suspicious = prediction == -1
    reason = "Anomaly score below threshold" if is_suspicious else "Normal login"
    return is_suspicious, reason, round(score, 4)

# Batch mode for Jenkins
if __name__ == "__main__":
    df = pd.read_csv("logs.csv")
    suspicious_logs = []

    for _, row in df.iterrows():
        suspicious, reason, score = detect_single_login(row)
        if suspicious:
            suspicious_logs.append({
                "timestamp": row["timestamp"],
                "email": row["email"],
                "ip": row["ip"],
                "reason": reason,
                "score": score
            })

    if suspicious_logs:
        df_alerts = pd.DataFrame(suspicious_logs)
        df_alerts.to_csv("alert_report.csv", index=False)
        print("\n Suspicious Logins Detected:")
        print(df_alerts.tail())
    else:
        # Create empty file with headers so Jenkins doesn't fail
        pd.DataFrame(columns=["timestamp", "email", "ip", "reason", "score"]).to_csv("alert_report.csv", index=False)
        print("No suspicious activity found.")
