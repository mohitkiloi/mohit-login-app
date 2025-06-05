import streamlit as st
import pandas as pd
import json
import os

st.set_page_config(page_title="Login Threat Dashboard", layout="wide")

st.title(" Login Anomaly Detection Dashboard")

# Load data
logs = pd.read_csv("logs.csv")
alert_file = "alert_report.csv"
metrics_file = "experiments/metrics_report.json"

if os.path.exists(alert_file):
    alerts = pd.read_csv(alert_file)
    st.subheader(" Recent Suspicious Logins")
    st.dataframe(alerts.tail(10))
else:
    st.warning("No suspicious logins detected yet.")

# Show model metrics
if os.path.exists(metrics_file):
    with open(metrics_file, "r") as f:
        metrics = json.load(f)
    st.subheader("Isolation Forest Metrics")
    st.json(metrics)
else:
    st.info("No metrics report found yet.")

# Show full logs
with st.expander(" All Login Logs"):
    st.dataframe(logs.tail(100))

# Show charts
st.subheader("Failed vs Successful Logins Over Time")
logs['timestamp'] = pd.to_datetime(logs['timestamp'])
logs['status_numeric'] = logs['status'].apply(lambda x: 0 if x == 'success' else 1)
line_data = logs.groupby(logs['timestamp'].dt.date)['status_numeric'].sum()
st.line_chart(line_data)

# Optional: GNN predictions
gnn_output_file = "gnn_predictions.csv"
if os.path.exists(gnn_output_file):
    gnn_df = pd.read_csv(gnn_output_file)
    st.subheader(" GNN Predicted Attack Types")
    st.dataframe(gnn_df.tail(10))
