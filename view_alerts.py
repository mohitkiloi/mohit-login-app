import pandas as pd

df = pd.read_csv("alert_report.csv")

print("\n Suspicious Login Alerts:")
print(df[["timestamp", "email", "ip", "reason", "score"]].tail())
