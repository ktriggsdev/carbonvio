import collections

import streamlit as st
import pandas as pd
import numpy as np

file = 'img/carbonvio.png'
st.image(file)

st.title('Welcome to Carbonvio!')
st.subheader('Utility usage:')
yearly_electric = st.number_input('How many KWh of electricity do you use per year?: ', 0, 100000)
yearly_electric = float(yearly_electric)
yearly_natural_gas = st.number_input('How many KWh of natural gas do you use per year?: ', 0, 100000)
yearly_natural_gas = float(yearly_natural_gas)
yearly_propane_gas = st.number_input('how many KWh of propane gas do you use per year?: ', 0, 100000)
yearly_propane_gas = float(yearly_propane_gas)
yearly_oil = st.number_input('how many litres of oil do you use per year for heating purposes?: ', 0, 100000)
yearly_oil = float(yearly_oil)
st.subheader('Transport:')
total_yearly_mileage = st.number_input('how many miles have you done in your vehicle this year?: ', 1, 100000)
total_yearly_mileage = float(total_yearly_mileage)
total_yearly_gallons = total_yearly_mileage / 25
total_yearly_gallons = float(total_yearly_gallons)
number_of_flights_less = st.number_input('How many flights have you taken this year that are 4 hours or less?: ', 0, 50)
number_of_flights_less = float(number_of_flights_less)
number_of_flights_more = st.number_input('How many flights have you taken this year that are 4 hours or more?: ', 0, 50)
number_of_flights_more = float(number_of_flights_more)
st.subheader('Recycling')
recycle_newspaper = st.selectbox('Do you recycle newspaper? (y/n): ', ['Yes', 'No'])
recycle_aluminium = st.selectbox('Do you recycle aluminium and tin? (y/n): ', ['Yes', 'No'])

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

if recycle_newspaper == "Yes":
    carbon_total = carbon_total + 0
elif recycle_newspaper == "No":
    carbon_total = carbon_total + 184

if recycle_aluminium == "Yes":
    carbon_total = carbon_total + 0
elif recycle_aluminium == "No":
    carbon_total = carbon_total + 166

carbon_offset = carbon_offset * trees
carbon_total = carbon_total - carbon_offset

st.subheader('Your Carbon Footprint:')
carbon_total = st.text(f'Your Carbon Footprint is {carbon_total} tonnes of CO2')


if yearly_electric > 2900:
    electricity_tips = [
        'Consider an energy audit',
        'unplug appliances you are not using such as toasters',
        'use dimmer switches',
        'Start Line Drying Laundry',
        'Keep Your Fridge and Freezer Full',
        'Install and Use Ceiling Fans to keep the cool air circulating',
        'Turn Off Your Stove',
        'Use LED Lighting',
        'Wash and Dry Dishes by Hand',
        'Turn Off Dishwasher Heat Dry',
        'Insulate Loft and rest of Home',
        'Insulate Electrical Outlets',
        'Install Storm Doors',
        'Plant trees around your home',
        'Lower Your Hot Water Heater Temperature',
        'Buy ENERGY STAR® Appliances',
        'lower temperature for washing machine to 30, 20 or even 15 if your machine supports that',
        'Do Only Full Laundry Loads',
        'Install a smart meter'
    ]

    electricity_bad = '<h3 style="font-family:monospace; color: #ef233c;">' \
                      'Tips to cut back on electricity usage:</h3>'
    st.markdown(electricity_bad, unsafe_allow_html=True)

    electricity_sub_bad = '<p style="font-family:monospace; color: #ef233c; font-size: 14px;">' \
                          'You are using too much electricity! here are some ways to cut back on your usage: </p>'
    st.markdown(electricity_sub_bad, unsafe_allow_html=True)

    for item in electricity_tips:
        electricity_message = st.code(item)
else:
    electricity_good = '<h3 style="font-family:monospace; color: #9ef01a;">' \
                         'Electricity: Good </h3>'
    st.markdown(electricity_good, unsafe_allow_html=True)

    electricity_sub_good = '<p style="font-family:monospace; color: #9ef01a; font-size: 14px;">' \
                           'You are using the recommended amount of electricity, good job!</p>'
    st.markdown(electricity_sub_good, unsafe_allow_html=True)


if yearly_natural_gas > 12000 or yearly_propane_gas > 12000:
    natural_gas_tips = [
        'Consider an energy audit',
        'Properly maintain heating systems',
        'check air vents and remove any blockages',
        'make your home air-tight'
        'keep all vents open',
        'keep windows and doors closed',
        'seal any cracks',
        'use good insulation',
        'insulate your water heater',
        'clean and replace air filters regularly',
        'lower your thermostat',
        'use a smart thermostat',
        'use a humidifier',
        'use a dehumidifier',
        'use a space heater',
        'wear extra layers such as a jumper',
        'turn down your water heater',
        'wash clothes in cold water',
        'hang your clothes',
        'use the dishwasher only when full',
        'do not use the fireplace',
        'install an attic tent',
        'use other heat sources',
        'use a timer',
        'install a heat pump',
        'use a drain water heat recovery system'
    ]

    nat_gas_bad = '<h3 style="font-family:monospace; color: #ef233c;">' \
                  'Tips to cut back on gas usage:</h3>'
    st.markdown(nat_gas_bad, unsafe_allow_html=True)

    nat_gas_sub_bad = '<p style="font-family:monospace; color: #ef233c; font-size: 14px;">' \
                      'You are using too much gas! here are some ways to cut back on your usage: </p>'
    st.markdown(nat_gas_sub_bad, unsafe_allow_html=True)

    for item in natural_gas_tips:
        nat_gas_message = st.code(item)
else:
    nat_gas_good = '<h3 style="font-family:monospace; color: #9ef01a;">' \
                         'Gas: Good </h3>'
    st.markdown(nat_gas_good, unsafe_allow_html=True)

    nat_gas_sub_good = '<p style="font-family:monospace; color: #9ef01a; font-size: 14px;">' \
                       'You are using the recommended amount of gas, good job!</p>'
    st.markdown(nat_gas_sub_good, unsafe_allow_html=True)


if yearly_oil > 2000:
    oil_tips = [
        'Consider an energy audit',
        'Cut back on/regulate air conditioning and heat.',
        'Eat and buy locally produced products',
        'Try going vegetarian even if it is just on a monday',
        'Do not buy bottled water',
        'Cut back on plastic products',
        'Recycle',
        'Roll down car windows instead of using A/C',
        'avoid standard candles, buy natural soy or beeswax candles.',
        'cut back on processed / canned foods',
        'eat organic if you cannot eat local',
        'do your research on soap products to make sure they do not contain too much oil'
    ]

    oil_bad = '<h3 style="font-family:monospace; color: #ef233c;">' \
              'Tips to cut back on oil usage:</h3>'
    st.markdown(oil_bad, unsafe_allow_html=True)

    oil_sub_bad = '<p style="font-family:monospace; color: #ef233c; font-size: 14px;">' \
                  'You are using too much oil! here are some ways to cut back on your usage: </p>'
    st.markdown(oil_sub_bad, unsafe_allow_html=True)

    for item in oil_tips:
        oil_message = st.code(item)
else:
    oil_good = '<h3 style="font-family:monospace; color: #9ef01a;">' \
                         'Oil: Good </h3>'
    st.markdown(oil_good, unsafe_allow_html=True)

    oil_sub_good = '<p style="font-family:monospace; color: #9ef01a; font-size: 14px;">' \
                   'You are using the recommended amount of oil, good job!</p>'
    st.markdown(oil_sub_good, unsafe_allow_html=True)

if total_yearly_mileage > 2000:
    mileage_tips = [
        'Consider eating and buying locally rather than travelling far',
        'consider using an electric vehicle',
        'do not travel far unless you need to',
        'consider having localised holidays rather than ones far away'
    ]

    mileage_bad = '<h3 style="font-family:monospace; color: #ef233c;">' \
                  'Tips to cut back on mileage:</h3>'
    st.markdown(mileage_bad, unsafe_allow_html=True)

    mileage_sub_bad = '<p style="font-family:monospace; color: #ef233c; font-size: 14px;">' \
                      'You have a higher mileage than average, here are some ways to cut back on your mileage: </p>'
    st.markdown(mileage_sub_bad, unsafe_allow_html=True)

    for item in mileage_tips:
        mileage_message = st.code(item)
else:
    mileage_good = '<h3 style="font-family:monospace; color: #9ef01a;">' \
                   'Mileage: Good </h3>'
    st.markdown(mileage_good, unsafe_allow_html=True)

    mileage_sub_good = '<p style="font-family:monospace; color: #9ef01a; font-size: 14px;">' \
                       'You have an average or lower than average mileage, good job!</p>'
    st.markdown(mileage_sub_good, unsafe_allow_html=True)

if number_of_flights_less > 5:
    flights_tips_less = [
        'Consider flying abroad less for holidays',
        'Consider whether it is better to fly for business trips, or take the bus, train or car'
    ]

    flights_less_bad = '<h3 style="font-family:monospace; color: #ef233c;">' \
                       'Tips to cut back on flights less than 4 hours:</h3>'
    st.markdown(flights_less_bad, unsafe_allow_html=True)

    flights_less_sub_bad = '<p style="font-family:monospace; color: #ef233c; font-size: 14px;">' \
                           'You have been on a higher number of flights ' \
                           '(less than 4 hours) than the average, ' \
                           'here are some ways to cut back on your mileage: </p>'
    st.markdown(flights_less_sub_bad, unsafe_allow_html=True)

    for item in flights_tips_less:
        flights_less_message = st.code(item)
else:
    flights_less_good = '<h3 style="font-family:monospace; color: #9ef01a;">' \
                        'Flights (less than 4 hours): Good </h3>'
    st.markdown(flights_less_good, unsafe_allow_html=True)

    flights_less_sub_good = '<p style="font-family:monospace; color: #9ef01a; font-size: 14px;">' \
                            'You have an average or lower than average number of flights (less than 4 hours), ' \
                            'good job!</p>'
    st.markdown(flights_less_sub_good, unsafe_allow_html=True)

if number_of_flights_more > 2:
    flights_tips_more = [
        'Consider flying abroad less for holidays',
        'Consider whether it is better to fly for business trips, or take the bus, train or car',
        'Consider flights that are less than 4 hours long'
    ]

    flights_more_bad = '<h3 style="font-family:monospace; color: #ef233c;">' \
                       'Tips to cut back on flights more than 4 hours:</h3>'
    st.markdown(flights_more_bad, unsafe_allow_html=True)

    flights_more_sub_bad = '<p style="font-family:monospace; color: #ef233c; font-size: 14px;">' \
                           'You have a have been on a higher number of flights ' \
                           '(more than 4 hours) than the average, ' \
                           'here are some ways to cut back on your mileage: </p>'
    st.markdown(flights_more_sub_bad, unsafe_allow_html=True)

    for item in flights_tips_more:
        flights_more_message = st.code(item)
else:
    flights_more_good = '<h3 style="font-family:monospace; color: #9ef01a;">' \
                        'Flights (more than 4 hours): Good </h3>'
    st.markdown(flights_more_good, unsafe_allow_html=True)

    flights_more_sub_good = '<p style="font-family:monospace; color: #9ef01a; font-size: 14px;">' \
                            'You have an average or lower than average number of flights (more than 4 hours), ' \
                            'good job!</p>'
    st.markdown(flights_more_sub_good, unsafe_allow_html=True)

if recycle_newspaper == 'No':
    recycle_paper_tips = [
        'consider recycling newspaper',
        'consider recycling paper',
        'consider recycling cardboard'
    ]

    recycle_paper_bad = '<h3 style="font-family:monospace; color: #ef233c;">' \
                        'Tips for recycling paper:</h3>'
    st.markdown(recycle_paper_bad, unsafe_allow_html=True)

    recycle_paper_sub_bad = '<p style="font-family:monospace; color: #ef233c; font-size: 14px;">' \
                            'You do not recycle paper items such as cardboard, newspaper, paper, letters' \
                            'here are some ways to increase your recycling habits: </p>'
    st.markdown(recycle_paper_sub_bad, unsafe_allow_html=True)

    for item in recycle_paper_tips:
        recycle_paper_message = st.code(item)
else:
    recycle_paper_good = '<h3 style="font-family:monospace; color: #9ef01a;">' \
                        'Recycling Paper: Good </h3>'
    st.markdown(recycle_paper_good, unsafe_allow_html=True)

    recycle_paper_sub_good = '<p style="font-family:monospace; color: #9ef01a; font-size: 14px;">' \
                             'You recycle paper items such as newspaper, paper, letters, cardboard, ' \
                             'good job!</p>'
    st.markdown(recycle_paper_sub_good, unsafe_allow_html=True)


if recycle_aluminium == 'No':
    recycle_aluminium_tips = [
        'consider recycling tins',
        'consider recycling any items that contain aluminium',
        'consider recycling foil'
    ]

    recycle_aluminium_bad = '<h3 style="font-family:monospace; color: #ef233c;">' \
                            'Tips for recycling aluminium and tin:</h3>'
    st.markdown(recycle_aluminium_bad, unsafe_allow_html=True)

    recycle_aluminium_sub_bad = '<p style="font-family:monospace; color: #ef233c; font-size: 14px;">' \
                                'You do not recycle aluminium or tin items such as tins, foil, ' \
                                'products containing aluminium' \
                                'here are some ways to increase your recycling habits: </p>'
    st.markdown(recycle_aluminium_sub_bad, unsafe_allow_html=True)

    for item in recycle_aluminium_tips:
        recycle_aluminium_message = st.code(item)
else:
    recycle_aluminium_good = '<h3 style="font-family:monospace; color: #9ef01a;">' \
                             'Recycling Aluminium: Good </h3>'
    st.markdown(recycle_aluminium_good, unsafe_allow_html=True)

    recycle_aluminium_sub_good = '<p style="font-family:monospace; color: #9ef01a; font-size: 14px;">' \
                                 'You recycle aluminium and tin items such as tins, foil, ' \
                                 'products containing aluminium ' \
                                 'good job!</p>'
    st.markdown(recycle_aluminium_sub_good, unsafe_allow_html=True)

if carbon_offset < 138.8913:
    carbon_offset_tips = [
        'plant more trees or flowers'
    ]

    carbon_offset_bad = '<h3 style="font-family:monospace; color: #ef233c;">' \
                        'Tips for carbon offsetting:</h3>'
    st.markdown(carbon_offset_bad, unsafe_allow_html=True)

    carbon_offset_sub_bad = '<p style="font-family:monospace; color: #ef233c; font-size: 14px;">' \
                            'You do not plant enough trees to offset your carbon emissions' \
                            'here are some ways to offset your carbon emissions: </p>'
    st.markdown(carbon_offset_sub_bad, unsafe_allow_html=True)

    for item in carbon_offset_tips:
        carbon_offset_message = st.code(item)
else:
    carbon_offset_good = '<h3 style="font-family:monospace; color: #9ef01a;">' \
                             'carbon offset: Good </h3>'
    st.markdown(carbon_offset_good, unsafe_allow_html=True)

    carbon_offset_sub_good = '<p style="font-family:monospace; color: #9ef01a; font-size: 14px;">' \
                             'You plant the average number of trees to offset your emissions' \
                             ' good job!</p>'
    st.markdown(carbon_offset_sub_good, unsafe_allow_html=True)

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
