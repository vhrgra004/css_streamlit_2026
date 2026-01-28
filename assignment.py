#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 13:31:27 2026

@author: gracevanheerden
"""



import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(page_title="Researcher Profile", layout="wide")

# Sidebar Menu
st.sidebar.title("Data Options")
menu = st.sidebar.radio(
    "Go to:",
    ["DLBCL metadata", "Related publications", "Contact me"],
)

# Dummy DLBCL metadata
dlbcl_data = pd.DataFrame({
    "Subtype": ["Not otherwise specified", "High-grade B-cell lymphoma"],
    "Frequency (%)": [90, 10],
    "Prognosis": ["Better", "Poor"],
})

COO_data = pd.DataFrame({
    "Cell of origin": ["GCB", "ABC"],
    "Frequency (%)": [55, 45],
    "Prognosis": ["Better", "Worse"],,
})

high_grade = pd.DataFrame({
    "High-grade B-cell lymphoma": ["Double-hit", "Triple-hit"],
    "Translocation status": ["MYC and BCL2 rearranged", "MYC, BCL2 and BCL6 rearranged"],
    "Frequency (%)": [7, 2],
})

ipi_score = pd.DataFrame({
    "International prognostic index score": ["0-1", "2", "3", "4-5"],
    "Meaning": ["Low risk", "Low-intermediate risk", "high-intermediate risk", "high risk"],
})

# Sections based on menu selection
if menu == "Researcher Profile":
    st.title("Researcher Profile")
    st.sidebar.header("Profile Options")

    # Collect basic information
    name = "Ms. Grace van Heerden"
    field = "Anatomical Pathology"
    institution = "University of Cape Town"

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")
    
    st.image(
    "https://share.google/SUj6KvYMQR5yy4nTZ",
    caption="UCT Campus"
)

elif menu == "Publications":
    st.title("Publications")
    st.sidebar.header("Upload and Filter")

    # Upload publications file
    uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")
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

        # Publication trends
        if "Year" in publications.columns:
            st.subheader("Publication Trends")
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)
        else:
            st.write("The CSV does not have a 'Year' column to visualize trends.")

elif menu == "DLBCL metadata":
    st.title("STEM Data Explorer")
    st.sidebar.header("Data Selection")
    
    # Tabbed view for STEM data
    data_option = st.sidebar.selectbox(
        "Choose a dataset to explore", 
        ["DLBCL metadata", "Astronomy Observations", "Weather Data"]
    )

    if data_option == "DLBCL metadata":
        st.write("### DLBCL metadata")
        st.dataframe(dlbcl_metadata)
        # Add widget to filter by Energy levels
        frequency = st.slider("Filter by Frequency (%)", 0.0, 100.0, (0.0, 100.0))
        filtered_physics = dlbcl_metadata[
            dlbcl_metadata["Energy (MeV)"].between(frequency[0], frequency[1])
        ]
        st.write(f"Filtered Results for Frequency {frequency}:")
        st.dataframe(filtered_dlbcl)

    elif data_option == "Astronomy Observations":
        st.write("### Astronomy Observation Data")
        st.dataframe(astronomy_data)
        # Add widget to filter by Brightness
        brightness_filter = st.slider("Filter by Brightness (Magnitude)", -15.0, 5.0, (-15.0, 5.0))
        filtered_astronomy = astronomy_data[
            astronomy_data["Brightness (Magnitude)"].between(brightness_filter[0], brightness_filter[1])
        ]
        st.write(f"Filtered Results for Brightness Range {brightness_filter}:")
        st.dataframe(filtered_astronomy)

    elif data_option == "Weather Data":
        st.write("### Weather Data")
        st.dataframe(weather_data)
        # Add widgets to filter by temperature and humidity
        temp_filter = st.slider("Filter by Temperature (°C)", -10.0, 40.0, (-10.0, 40.0))
        humidity_filter = st.slider("Filter by Humidity (%)", 0, 100, (0, 100))
        filtered_weather = weather_data[
            weather_data["Temperature (°C)"].between(temp_filter[0], temp_filter[1]) &
            weather_data["Humidity (%)"].between(humidity_filter[0], humidity_filter[1])
        ]
        st.write(f"Filtered Results for Temperature {temp_filter} and Humidity {humidity_filter}:")
        st.dataframe(filtered_weather)
        
        

elif menu == "Contact":
    # Add a contact section
    st.header("Contact Information")
    email = "jane.doe@example.com"
    st.write(f"You can reach me at {email}.")
