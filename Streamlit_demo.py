import streamlit as st
import pandas as pd
import plotly.express as plt

st.set_page_config(
    page_title="NASA Exoplanet Survey",
    page_icon="🪐",
    layout="wide",
    initial_sidebar_state="auto"
)

col1,col2 = st.columns([.65,.35])

with col1:
    st.title("NASA Exoplanet Survey")
    st.link_button("Dataset source here", "https://exoplanetarchive.ipac.caltech.edu/docs/intro.html")
    st.markdown("###### All data in the Exoplanet Archive are vetted by a team of astronomers (team roster) and are linked back to the original literature reference.")

    exoplanet_csv = (".//Sources//Exoplanets.csv")

    # Loading df and converting disc_year to dt
    exo_df = pd.read_csv(exoplanet_csv, skiprows=96, header=0)
    
    # Tell pandas "put these years into DT format to use the year on graph below"
    exo_df['disc_year'] = pd.to_datetime(exo_df['disc_year'], format="%Y")

    check_table = st.checkbox("See source table")
    if check_table:
        st.dataframe(exo_df)

    # Create the grouped time df with a count col
    time_group_df = exo_df.groupby([exo_df['disc_year'].dt.year, "discoverymethod"]).size().reset_index(name="Count") # Reset index in this .size() case makes it into a count col

    disc_year_plt = plt.bar(time_group_df, x="disc_year", y="Count", title="Discoveries Over Time", color="discoverymethod", barmode="group",
                             labels={
                                 "disc_year": "Discovery Year", 
                                 "Count": "Discovery Count"
                                 },                        
                             )
    st.plotly_chart(disc_year_plt)

with col2:
    st.image(".//Sources//img//STScI-01G8H1K2BCNATEZSKVRN9Z69SR.png", width='content')