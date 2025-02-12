import streamlit as st
import pandas as pd

# Load data
data = {
    "Payer Type": [
        "Self-Pay", "State Funding", "BEWELL Funding", "Harris Center", "Medicaid & Medicare"
    ],
    "Locations": [
        "Fulton, Galleria, Grand Parkway",
        "Fulton",
        "Fulton, Galleria, Grand Parkway",
        "Fulton, Galleria, Grand Parkway",
        "Fulton"
    ],
    "Medications Available": [
        "Methadone, Suboxone, Buprenorphine, Vivitrol, Sublocade",
        "Methadone, Buprenorphine, Vivitrol",
        "Buprenorphine, Vivitrol",
        "Methadone, Buprenorphine, Vivitrol",
        "Methadone, Buprenorphine"
    ]
}

df = pd.DataFrame(data)

# Streamlit UI
st.title("Texas Clinic Healthcare Dashboard")

# Filters
payer_filter = st.selectbox("Select Payer Type", ["All"] + list(df["Payer Type"].unique()))
location_filter = st.selectbox("Select Location", ["All"] + list(set(
    ", ".join(df["Locations"]).split(", "))))
medication_filter = st.selectbox("Select Medication", ["All"] + list(set(
    ", ".join(df["Medications Available"]).split(", "))))

# Filtering logic
filtered_df = df.copy()
if payer_filter != "All":
    filtered_df = filtered_df[filtered_df["Payer Type"] == payer_filter]
if location_filter != "All":
    filtered_df = filtered_df[filtered_df["Locations"].str.contains(location_filter, case=False)]
if medication_filter != "All":
    filtered_df = filtered_df[filtered_df["Medications Available"].str.contains(medication_filter, case=False)]

# Display results
st.write("### Filtered Results:")
st.dataframe(filtered_df)

# Summary
st.write("### Summary Information")
st.write("- Use the dropdown filters to narrow down your search.")
st.write("- This dashboard helps staff quickly find payer types, medications, and clinic locations.")
