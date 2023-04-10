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

yearly_electric = float(input("What is your yearly electric bill? (KWh): "))

yearly_natural_gas = float(input("What is your yearly natural gas bill? (therms): "))

yearly_propane_gas = float(input("What is your yearly propane gas bill? (gallons): "))

yearly_oil = float(input("What is your yearly oil bill? (gallons): "))

total_yearly_mileage = float(input("What is your total yearly mileage on your vehicle? (m): "))

total_yearly_gallons = total_yearly_mileage / 25

number_of_flights_less = float(input("How many flights have you taken in the past year (4 hours or less): "))

number_of_flights_more = float(input("How many flights have you taken in the past year (4 hours or more): "))

recycle_newspaper = input("Do you recycle newspaper? (y/n): ")
recycle_newspaper = recycle_newspaper.lower()

recycle_aluminium = input("Do you recycle aluminium and tin? (y/n): ")
recycle_aluminium = recycle_aluminium.lower()

trees = float(input("how many trees have you planted this year?: "))

carbon_offset = 46.2971

carbon_total = 0.0


def electric(yearly_electric):
    global carbon_total
    yearly_electric = yearly_electric * 0.994
    carbon_total = carbon_total + yearly_electric
    return carbon_total


def gas(yearly_natural_gas):
    global carbon_total
    yearly_natural_gas = yearly_natural_gas * 11.7
    carbon_total = carbon_total + yearly_natural_gas
    return carbon_total


def propane(yearly_propane_gas):
    global carbon_total
    yearly_propane_gas = yearly_propane_gas * 13
    carbon_total = carbon_total + yearly_propane_gas
    return carbon_total


def oil(yearly_oil):
    global carbon_total
    yearly_oil = yearly_oil * 19.6
    carbon_total = carbon_total + yearly_oil
    return carbon_total


def yearly_mileage(total_yearly_gallons, total_yearly_mileage):
    global carbon_total
    total_fuel_usage = total_yearly_mileage / total_yearly_gallons
    emission = total_fuel_usage * 19.6
    carbon_total = carbon_total + emission
    return carbon_total


def flights_less(number_of_flights_less):
    global carbon_total
    number_of_flights_less = number_of_flights_less * 1100
    carbon_total = carbon_total + number_of_flights_less
    return carbon_total


def flights_more(number_of_flights_more):
    global carbon_total
    number_of_flights_more = number_of_flights_more * 4400
    carbon_total = carbon_total + number_of_flights_more
    return carbon_total


def recycle_paper(recycle_newspaper):
    global carbon_total
    if recycle_newspaper == "y":
        carbon_total = carbon_total + 0
    elif recycle_newspaper == "n":
        carbon_total = carbon_total + 184
    return carbon_total


def recycle_alu_tin(recycle_aluminium):
    global carbon_total
    if recycle_aluminium == "y":
        carbon_total = carbon_total + 0
    elif recycle_aluminium == "n":
        carbon_total = carbon_total + 166
    return carbon_total


def trees_count(trees):
    global carbon_offset
    global carbon_total
    carbon_offset = carbon_offset * trees
    carbon_total = carbon_total - carbon_offset
    return carbon_total


def total(carbon_total):
    print("Your carbon total is:")
    print(carbon_total)
    # utility_bills = monthly_electric + monthly_gas + monthly_oil
    # fuel = total_yearly_mileage
    # flights = number_of_flights_less + number_of_flights_more
    # recycle = recycle_newspaper, recycle_aluminium
    # offset = carbon_offset
    # carbon_total = utility_bills + fuel + flights + recycle


electric(yearly_electric)


gas(yearly_natural_gas)


propane(yearly_propane_gas)


oil(yearly_oil)


yearly_mileage(total_yearly_mileage, total_yearly_gallons)


flights_less(number_of_flights_less)


flights_more(number_of_flights_more)


recycle_paper(recycle_newspaper)


recycle_alu_tin(recycle_aluminium)


trees_count(trees)


total(carbon_total)
