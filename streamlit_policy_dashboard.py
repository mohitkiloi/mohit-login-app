import streamlit as st
import json
import pandas as pd
import os
import plotly.express as px

st.set_page_config(page_title="OPA Policy Compliance", layout="wide")

# Title
st.title("OPA Policy Dashboard – CI/CD Compliance Monitor")

# Load OPA result
opa_file = "policy_result.json"

with st.sidebar:
    st.markdown("## OPA Policy Result")
    if not os.path.exists(opa_file):
        st.warning("OPA result file not found. Run Jenkins first.")
    else:
        with open(opa_file) as f:
            data = json.load(f)

        decision = data["result"][0]["expressions"][0]["value"]
        if decision:
            st.success(" Build Allowed by OPA Policy")
        else:
            st.error(" Build Blocked by OPA Policy")

# Main Explanation
st.markdown("### Active Policy Rules")
st.markdown("""
```rego
package ci_cd.policy

default allow = false

allow {
  input.branch == "main"
  input.approved == true
  input.role == "admin"
}
""")