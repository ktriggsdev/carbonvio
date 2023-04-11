import streamlit as st
file = 'img/carbonvio.png'
st.image(file)

st.header('Download our educational game')

with open("pages/game.txt", "rb") as file:
    btn = st.download_button(
            label="Download Game",
            data=file,
            file_name="game.txt")
