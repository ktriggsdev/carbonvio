import streamlit as st
import pandas as pd
import numpy as np

st.title('Carbonvio')
st.header('Welcome to Carbonvio!')
st.subheader('Utility usage:')
yearly_electric = st.text_input('How many kwh of electricity do you use per year?: ')
yearly_electric = str(yearly_electric)
yearly_natural_gas = st.text_input('How many therms of natural gas do you use per year?: ')
yearly_natural_gas = str(yearly_natural_gas)
yearly_propane_gas = st.text_input('how many gallons of propane gas do you use per year?: ')
yearly_propane_gas = str(yearly_propane_gas)
yearly_oil = st.text_input('how many gallons of oil do you use per year for heating purposes?: ')
yearly_oil = str(yearly_oil)
st.subheader('Transport:')
total_yearly_mileage = st.number_input('how many miles have you done in your vehicle this year?: ', 100, 100000)
total_yearly_mileage = float(total_yearly_mileage)
total_yearly_gallons = total_yearly_mileage / 25
total_yearly_gallons = float(total_yearly_gallons)
number_of_flights_less = st.number_input('How many flights have you taken this year that are 4 hours or less?: ', 0, 50)
number_of_flights_less = float(number_of_flights_less)
number_of_flights_more = st.number_input('How many flights have you taken this year that are 4 hours or more?: ', 0, 50)
number_of_flights_more = float(number_of_flights_more)
st.subheader('Recycling')
recycle_newspaper = st.selectbox('Do you recycle newspaper? (y/n): ', ['Yes', 'No'])
recycle_newspaper = recycle_newspaper.lower()
recycle_aluminium = st.selectbox('Do you recycle aluminium and tin? (y/n): ', ['Yes', 'No'])
recycle_aluminium = recycle_aluminium.lower()

trees = st.number_input("how many trees have you planted this year?: ", 0, 1000)
trees = float(trees)

carbon_offset = 46.2971

carbon_total = 0.0
