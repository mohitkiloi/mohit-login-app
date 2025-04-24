import pandas as pd

df = pd.read_csv('analyzed_logs.csv')
anomalies = df[df['anomaly_label'] == 'Anomaly']

# Create alert report
alert_df = anomalies[['email', 'timestamp', 'role', 'status']]
alert_df.to_csv('alert_report.csv', index=False)
print(f"[ALERT] Total anomalies found: {len(anomalies)}. Report saved to alert_report.csv.")
