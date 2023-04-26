import streamlit as st
import pandas as pd
import hashlib
import chardet

file = 'img/carbonvio.png'

# sets the configuration of the app on streamlit
st.set_page_config(
    page_title='Carbonvio', 
    page_icon='img/carbonvio.ico',
    menu_items={
        'Report a bug': "https://github.com/ktriggsdev/carbonvio/issues",
        'About': "Carbonvio, A carbon footprint calculator with a difference."
    })
st.image(file)

# sets a title for the page
st.title('Welcome to Carbonvio!')


# If the user chooses login, ask them to enter username and password in the sidebar
#if mode == 'Login':
st.sidebar = sidebar

username = sidebar.text_input('username')
password = sidebar.text_input('password', type='password')
st.write("test 2")

detected_encoding = chardet.detect(password)['encoding']
decoded_string = password.decode(detected_encoding)
st.write(decoded_string)