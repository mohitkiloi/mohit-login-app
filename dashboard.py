import streamlit as st
import pandas as pd

st.set_page_config(page_title="Anomaly Detection Dashboard", layout="wide")

# Load data
df = pd.read_csv('analyzed_logs.csv')

# Title
st.title(" Anomaly Detection in Login Logs")

# Metrics
total = len(df)
anomalies = len(df[df['anomaly_label'] == 'Anomaly'])
normal = total - anomalies

st.metric("Total Logs", total)
st.metric("Anomalies Detected", anomalies)
st.metric("Normal Entries", normal)

# Filters
with st.sidebar:
    st.header("Filters")
    role_filter = st.multiselect("Select Roles", options=df['role'].unique(), default=list(df['role'].unique()))
    status_filter = st.multiselect("Login Status", options=df['status'].unique(), default=list(df['status'].unique()))
    anomaly_filter = st.selectbox("Anomaly Filter", options=["All", "Normal", "Anomaly"])

# Apply filters
filtered_df = df[df['role'].isin(role_filter) & df['status'].isin(status_filter)]
if anomaly_filter != "All":
    filtered_df = filtered_df[filtered_df['anomaly_label'] == anomaly_filter]

# Show table
st.dataframe(filtered_df)

# Chart
st.bar_chart(filtered_df['anomaly_label'].value_counts())
