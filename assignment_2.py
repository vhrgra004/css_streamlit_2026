#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 09:59:31 2026

@author: gracevanheerden
"""

import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Diffuse Large B-cell Lymphoma Research")

# Collect basic information
name = "Ms. Grace van Heerden"
field = "Anatomical Pathology"
institution = "University of Cape Town"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

st.image(
    "https://upload.wikimedia.org/wikipedia/commons/d/de/Diffuse_large_B-cell_lymphoma_%28DLBCL%29%2C_high_mag.jpg",
    caption="Haematoxylin & Eosin Stain - DLBCL"
)

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Diffuse Large B-cell lymphoma Journal Articles", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Publication Year" in publications.columns:
        year_counts = publications["Publication Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Publication Year' column to visualize trends.")

# Dummy DLBCL metadata
dlbcl_data = pd.DataFrame({
    "Subtype": ["Not otherwise specified", "High-grade B-cell lymphoma"],
    "Frequency (%)": [90, 10],
    "Prognosis": ["Better", "Poor"],
})

coo_data = pd.DataFrame({
    "Cell-of-origin": ["GCB", "ABC"],
    "Frequency (%)": [55, 45],
    "Prognosis": ["Better", "Worse"],
})

high_grade = pd.DataFrame({
    "High-grade B-cell lymphoma": ["Double-hit", "Triple-hit"],
    "Translocation status": ["MYC and BCL2 rearranged", "MYC, BCL2 and BCL6 rearranged"],
    "Frequency (%)": [7, 2],
})

# Tabbed view for STEM data
st.subheader("DLBCL Metadata Viewer")
data_option = st.selectbox(
    "Choose a dataset to explore", 
    ["DLBCL subtype", "Cell-of-origin", "High-grade B-cell lymphoma"]
)

if data_option == "DLBCL subtype":
    st.write("### DLBCL subtype metadata")
    st.dataframe(dlbcl_data)
    # Add widget to filter by Energy levels
    frequency_filter = st.slider("Frequency (%)", 0.0, 100.0, (0.0, 100.0))
    filtered_dlbcl = dlbcl_data [
        dlbcl_data["Frequency (%)"].between(frequency_filter[0], frequency_filter[1])
    ]
    st.write(f"Filtered Results for Frequency {frequency_filter}:")
    st.dataframe(filtered_dlbcl)

elif data_option == "Cell-of-origin":
    st.write("### Cell-of-origin")
    st.dataframe(coo_data)
    # Add widget to filter by Brightness
    frequency_filter = st.slider("Frequency (%)", 0.0, 100.0, (0.0, 100.0))
    filtered_frequency = coo_data[
        coo_data["Frequency (%)"].between(frequency_filter[0], frequency_filter[1])
    ]
    st.write(f"Filtered Results for Frequency {frequency_filter}:")
    st.dataframe(filtered_frequency)

elif data_option == "High-grade B-cell lymphoma":
    st.write("### High-grade B-cell lymphoma")
    st.dataframe(high_grade)
    # Add widgets to filter by frequency
    frequency_filter = st.slider("Filter by Frequency (%)", 0.0, 10.0, (0.0, 10.0))
    filtered_frequency = high_grade[
        high_grade["Frequency (%)"].between(frequency_filter[0], frequency_filter[1])
    ]
    st.write(f"Filtered Results for Frequency {frequency_filter}:")
    st.dataframe(filtered_frequency)


# Add a contact section
st.header("Contact Information")
email = "vhrgra004@myuct.ac.za"
st.write(f"You can reach {name} at {email}.")
