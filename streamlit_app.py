import streamlit as st
import pandas as pd
import numpy as np

file = 'img/carbonvio.png'
st.image(file)

st.title('Carbonvio')
st.header('Welcome to Carbonvio!')
st.subheader('Utility usage:')
yearly_electric = st.number_input('How many kwh of electricity do you use per year?: ', 0, 100000)
yearly_electric = float(yearly_electric)
yearly_natural_gas = st.number_input('How many therms of natural gas do you use per year?: ', 0, 100000)
yearly_natural_gas = float(yearly_natural_gas)
yearly_propane_gas = st.number_input('how many gallons of propane gas do you use per year?: ', 0, 100000)
yearly_propane_gas = float(yearly_propane_gas)
yearly_oil = st.number_input('how many gallons of oil do you use per year for heating purposes?: ', 0, 100000)
yearly_oil = float(yearly_oil)
st.subheader('Transport:')
total_yearly_mileage = st.number_input('how many miles have you done in your vehicle this year?: ', 0, 100000)
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

yearly_electric = yearly_electric * 0.994
carbon_total = carbon_total + yearly_electric

yearly_natural_gas = yearly_natural_gas * 11.7
carbon_total = carbon_total + yearly_natural_gas

yearly_propane_gas = yearly_propane_gas * 13
carbon_total = carbon_total + yearly_propane_gas

yearly_oil = yearly_oil * 19.6
carbon_total = carbon_total + yearly_oil

total_fuel_usage = total_yearly_mileage / total_yearly_gallons
emission = total_fuel_usage * 19.6
carbon_total = carbon_total + emission

number_of_flights_less = number_of_flights_less * 1100
carbon_total = carbon_total + number_of_flights_less

number_of_flights_more = number_of_flights_more * 4400
carbon_total = carbon_total + number_of_flights_more

if recycle_newspaper == "y":
    carbon_total = carbon_total + 0
elif recycle_newspaper == "n":
    carbon_total = carbon_total + 184

if recycle_aluminium == "y":
    carbon_total = carbon_total + 0
elif recycle_aluminium == "n":
    carbon_total = carbon_total + 166

carbon_offset = carbon_offset * trees
carbon_total = carbon_total - carbon_offset

carbon_total = st.text(carbon_total)
# def electric(yearly_electric):
#     global carbon_total
#     yearly_electric = yearly_electric * 0.994
#     carbon_total = carbon_total + yearly_electric
#     return carbon_total
#
#
# def gas(yearly_natural_gas):
#     global carbon_total
#     yearly_natural_gas = yearly_natural_gas * 11.7
#     carbon_total = carbon_total + yearly_natural_gas
#     return carbon_total
#
#
# def propane(yearly_propane_gas):
#     global carbon_total
#     yearly_propane_gas = yearly_propane_gas * 13
#     carbon_total = carbon_total + yearly_propane_gas
#     return carbon_total
#
#
# def oil(yearly_oil):
#     global carbon_total
#     yearly_oil = yearly_oil * 19.6
#     carbon_total = carbon_total + yearly_oil
#     return carbon_total
#
#
# def yearly_mileage(total_yearly_gallons, total_yearly_mileage):
#     global carbon_total
#     total_fuel_usage = total_yearly_mileage / total_yearly_gallons
#     emission = total_fuel_usage * 19.6
#     carbon_total = carbon_total + emission
#     return carbon_total
#
#
# def flights_less(number_of_flights_less):
#     global carbon_total
#     number_of_flights_less = number_of_flights_less * 1100
#     carbon_total = carbon_total + number_of_flights_less
#     return carbon_total
#
#
# def flights_more(number_of_flights_more):
#     global carbon_total
#     number_of_flights_more = number_of_flights_more * 4400
#     carbon_total = carbon_total + number_of_flights_more
#     return carbon_total
#
#
# def recycle_paper(recycle_newspaper):
#     global carbon_total
#     if recycle_newspaper == "y":
#         carbon_total = carbon_total + 0
#     elif recycle_newspaper == "n":
#         carbon_total = carbon_total + 184
#     return carbon_total
#
#
# def recycle_alu_tin(recycle_aluminium):
#     global carbon_total
#     if recycle_aluminium == "y":
#         carbon_total = carbon_total + 0
#     elif recycle_aluminium == "n":
#         carbon_total = carbon_total + 166
#     return carbon_total
#
#
# def trees_count(trees):
#     global carbon_total
#     global carbon_offset
#     carbon_offset = carbon_offset * trees
#     carbon_total = carbon_total - carbon_offset
#     return carbon_total
#
#
#
#
#
# electric(yearly_electric)
#
#
# gas(yearly_natural_gas)
#
#
# propane(yearly_propane_gas)
#
#
# oil(yearly_oil)
#
#
# yearly_mileage(total_yearly_mileage, total_yearly_gallons)
#
#
# flights_less(number_of_flights_less)
#
#
# flights_more(number_of_flights_more)
#
#
# recycle_paper(recycle_newspaper)
#
#
# recycle_alu_tin(recycle_aluminium)
#
#
# trees_count(trees)
#
#
# carbon_total = st.text(carbon_total)
