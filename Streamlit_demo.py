import streamlit as st
import pandas as pd
import plotly.express as plt

st.title("NASA Exoplanet Survey")
st.link_button("Dataset Source", "https://exoplanetarchive.ipac.caltech.edu/docs/intro.html")

exoplanet_csv = (".//Sources//Exoplanets.csv")

# Loading df and converting disc_year to dt
exo_df = pd.read_csv(exoplanet_csv, skiprows=96, header=0)
exo_df['disc_year'] = pd.to_datetime(exo_df['disc_year'])

check_table = st.checkbox("See source table")
if check_table:
    st.dataframe(exo_df)

col1,col2 = st.columns(2)

with col1:
    disc_year_group = exo_df.groupby(exo_df['disc_year'].dt.to_period('Y')).size().reset_index(name='count')
    disc_year_group['disc_year'] = disc_year_group['disc_year'].dt.to_timestamp()
    disc_year_plt = plt.line(disc_year_group, x="disc_year", y="count")
    disc_year_plt.show()