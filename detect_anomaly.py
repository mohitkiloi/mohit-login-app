import joblib
import numpy as np
import os

# Load trained Isolation Forest model
MODEL_PATH = "model.joblib"
model = joblib.load(MODEL_PATH) if os.path.exists(MODEL_PATH) else None

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
        len(log_row["user_agent"]),
        len(log_row["location"])
    ]
    return np.array(features).reshape(1, -1)

def detect_single_login(log_row):
    if model is None:
        return False, "Model not found", 0.0

    features = preprocess(log_row)
    score = model.decision_function(features)[0]
    prediction = model.predict(features)[0]  # -1 = anomaly

    is_suspicious = prediction == -1
    reason = "Anomaly score below threshold" if is_suspicious else "Normal login"

    return is_suspicious, reason, round(score, 4)

# Batch mode (Jenkins-friendly)
if __name__ == "__main__":
    import pandas as pd

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
        print("\n Suspicious Logins Detected:")
        print(pd.DataFrame(suspicious_logs).tail())
    else:
        print(" No suspicious activity found.")
