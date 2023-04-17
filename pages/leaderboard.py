import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='Carbonvio',
    page_icon='img/carbonvio.ico',
    menu_items={
        'Report a bug': "https://github.com/ktriggsdev/carbonvio/issues",
        'About': "Carbonvio, A carbon footprint calculator with a difference."
    })
st.title('Carbon Emissions Leaderboard')

# Read the carbon_total data into a Pandas DataFrame
df = pd.read_csv("leaderboard.csv")

# Create a leaderboard table
st.table(df.sort_values("carbon_total", ascending=False))