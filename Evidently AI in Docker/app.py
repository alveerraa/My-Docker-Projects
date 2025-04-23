import streamlit as st
import pandas as pd
from evidently.report import Report
from evidently.metrics import DataDriftTable

st.set_page_config(page_title="Evidently AI - Data Drift", layout="centered")

st.title("📊 Evidently AI - Data Drift Report")

# Simulated data for demonstration
ref_data = pd.DataFrame({"feature": [1, 2, 3, 4, 5]})
curr_data = pd.DataFrame({"feature": [1, 2, 6, 7, 8]})

with st.spinner("Generating report..."):
    report = Report(metrics=[DataDriftTable()])
    report.run(reference_data=ref_data, current_data=curr_data)

# Display results
st.subheader("Raw JSON Output")
st.json(report.as_dict())

# (Optional) Show DataFrames
with st.expander("Show Reference Data"):
    st.dataframe(ref_data)

with st.expander("Show Current Data"):
    st.dataframe(curr_data)

st.success("Report generated successfully!")


