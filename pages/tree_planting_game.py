import streamlit as st
file = '../img/carbonvio.png'
st.image(file)

st.header('Download our educational game')

game = '../pages/game.txt'
st.download_button(game)
