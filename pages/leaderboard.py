import streamlit as st
import pandas as pd
from streamlit_login_auth_ui.widgets import __login__

st.set_page_config(
    page_title='Carbonvio',
    page_icon='img/carbonvio.ico',
    menu_items={
        'Report a bug': "https://github.com/ktriggsdev/carbonvio/issues",
        'About': "Carbonvio, A carbon footprint calculator with a difference."
    })
st.title('Carbon Emissions Leaderboard')

__login__obj = __login__(auth_token = "courier_auth_token", 
company_name = "Carbonvio",
width = 200, height = 250, 
logout_button_name = 'Logout', hide_menu_bool = False, 
hide_footer_bool = False, 
lottie_url = 'https://assets9.lottiefiles.com/packages/lf20_yt24wfpb.json')

LOGGED_IN = __login__obj.build_login_ui()

if LOGGED_IN == True:

    st.dataframe(pd.read_csv("leaderboard.csv", names=["name", "carbon_total"]), height=300)
