# Program must do the following:
# - Calculate a user's carbon footprint
# - Offer the user ways to reduce the carbon footprint
# - Offer gamification to help the user keep to their goals such as local and global leaderboards and achievements

# import all the modules required

# ask the user for input for the following areas:
# - monthly electric bill 
# - monthly gas bill
# - monthly oil bill
# - total yearly mileage on vehicle
# - number of flights taken in past year (4 hours or less)
# - number of flights taken in past year (4 hours or more)
# - does the user recycle newspaper?
# - does the user recycle aluminium and tin?
# - how many cryptocurrency gas fees?
# - how many nft gas fees?
# - Food waste?
# - Meat consumption?

# calculate the carbon footprint
# electric bill * 105
# gas bill * 105
# oil bill * 113
# total mileage in vehicle * .79
# number of flights (less than 4 hours) * 1100
# number of flights (more than 4 hours) * 4400
# add 184 if recycle newspaper = False
# add 166 if recycle aluminium / tin = False
# crypto gas fees * ___
# nft gas fees * ___
# food waste?
# Meat Consumption?

monthly_electric = float(input("What is your monthly electric bill?: "))

monthly_gas = float(input("What is your monthly gas bill?: "))

monthly_oil = float(input("What is your monthly oil bill?: "))

total_yearly_mileage = input("What is your total yearly mileage on your vehicle?: ")

number_of_flights_less = input("How many flights have you taken in the past year (4 hours or less): ")

number_of_flights_more = input("How many flights have you taken in the past year (4 hours or more): ")

recycle_newspaper = input("Do you recycle newspaper? (y/n): ")

recycle_aluminium = input("Do you recycle aluminium and tin? (y/n): ")

def electric():
  monthly_electric = monthly_electric * 105
  return monthly_electric

def gas(): 
  monthly_gas = monthly_gas * 105
  return monthly_gas

def oil(): 
  monthly_oil = monthly_oil * 113
  return monthly_oil

def yearly_mileage():
  total_yearly_mileage = total_yearly_mileage * 0.79
  return total_yearly_mileage


