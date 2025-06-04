import streamlit as st
import pandas as pd

st.title(" Suspicious Login Alert Dashboard")

try:
    alerts = pd.read_csv("alert_report.csv")
    st.metric("Total Alerts", len(alerts))

    if not alerts.empty:
        st.dataframe(alerts.sort_values(by="timestamp", ascending=False))
        ip_filter = st.selectbox("Filter by IP:", ["All"] + list(alerts['ip'].unique()))
        if ip_filter != "All":
            st.dataframe(alerts[alerts['ip'] == ip_filter])

except FileNotFoundError:
    st.warning("No alerts found. Run app and login to generate data.")
