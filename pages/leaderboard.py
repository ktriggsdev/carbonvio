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

# Connect to the SQLite database
conn = sqlite3.connect('leaderboard.db')
c = conn.cursor()

__login__obj = __login__(auth_token = "courier_auth_token", 
company_name = "Carbonvio",
width = 200, height = 250, 
logout_button_name = 'Logout', hide_menu_bool = False, 
hide_footer_bool = False, 
lottie_url = 'https://assets9.lottiefiles.com/packages/lf20_yt24wfpb.json')

LOGGED_IN = __login__obj.build_login_ui()

if LOGGED_IN == True:

    # Execute the SELECT statement and fetch the data
    c.execute('SELECT * FROM leaderboard')
    data = c.fetchall()

    # Create a DataFrame from the fetched data
    df = pd.DataFrame(data, columns=["name", "carbon_total"])

    # Display the DataFrame using Streamlit
    st.dataframe(df)

    # Close the connection to the SQLite database
    conn.close()
