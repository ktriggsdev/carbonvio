import streamlit as st
import pandas as pd
import numpy as np

st.title('Carbonvio')
st.header('Welcome to Carbonvio!')
yearly_electric = st.text_input('How many kwh of electricity do you use per year?: ')
yearly_natural_gas = st.text_input('How many therms of natural gas do you use per year?: ')
yearly_propane_gas = st.text_input('how many gallons of propane gas do you use per year?: ')
yearly_oil = st.text_input('how many gallons of oil do you use per year for heating purposes?: ')
total_yearly_mileage = st.text_input('how many miles have you done in your vehicle this year?: ')
