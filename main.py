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
recycle_newspaper = recycle_newspaper.lower()

recycle_aluminium = input("Do you recycle aluminium and tin? (y/n): ")
recycle_aluminium = recycle_aluminium.lower()

trees = float(input("how many trees have you planted this year?: "))

carbon_total = 0


def electric(monthly_electric, carbon_total):
    monthly_electric = monthly_electric * 105
    carbon_total = carbon_total + monthly_electric
    return monthly_electric, carbon_total


def gas(monthly_gas, carbon_total):
    monthly_gas = monthly_gas * 105
    carbon_total = carbon_total + monthly_gas
    return monthly_gas, carbon_total


def oil(monthly_oil, carbon_total):
    monthly_oil = monthly_oil * 113
    carbon_total = carbon_total + monthly_oil
    return monthly_oil, carbon_total


def yearly_mileage(total_yearly_mileage, carbon_total):
    total_yearly_mileage = total_yearly_mileage * 0.79
    carbon_total = carbon_total + total_yearly_mileage
    return total_yearly_mileage, carbon_total


def flights_less(number_of_flights_less, carbon_total):
    number_of_flights_less = number_of_flights_less * 1100
    carbon_total = carbon_total + number_of_flights_less
    return number_of_flights_less, carbon_total


def flights_more(number_of_flights_more, carbon_total):
    number_of_flights_more = number_of_flights_more * 4400
    carbon_total = carbon_total + number_of_flights_more
    return number_of_flights_more, carbon_total


def recycle_paper(recycle_newspaper, carbon_total):
    if recycle_newspaper == "y":
        recycle_newspaper = True
        carbon_total = carbon_total + 0
    elif recycle_newspaper == "n":
        recycle_newspaper = False
        carbon_total = carbon_total + 184
    return recycle_newspaper, carbon_total


def recycle_alu_tin(recycle_aluminium, carbon_total):
    if recycle_aluminium == "y":
        recycle_aluminium = True
        carbon_total = carbon_total + 0
    elif recycle_aluminium == "n":
        recycle_aluminium = False
        carbon_total = carbon_total + 166
    return recycle_aluminium, carbon_total


def trees_count(trees, carbon_total):
    carbon_offset = 46.2971
    carbon_offset = carbon_offset * trees
    carbon_total = carbon_total - carbon_offset
    return carbon_offset, carbon_total
