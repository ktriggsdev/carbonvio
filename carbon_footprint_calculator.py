import streamlit as st
import pandas as pd
import hashlib
import sqlite3 

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

# Security
#passlib,hashlib,bcrypt,scrypt

def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management

conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data



def main():
    if "page" not in st.session_state:
        # initialize session state.
        st.session_state.update({
            "page": "home",

            "options": ["Home", "Login", "Signup", "Metric", "Imperial", "Yes", "No"],

            "text": "",
            "slider": 0,
            "number_input": 0,
            "checkbox": False,
            "selectbox": "Hello",
            "multiselect": ["Hello", "Everyone"],
        })

        page = st.sidebar.radio("Select your page", tuple(PAGES.keys()), format_func=str.capitalize)

        PAGES[page]()


def page_home():
    st.title("Carbonvio")

    menu = ["Home","Login","SignUp"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
	    st.subheader("Home")

    elif choice == "Login":
	    st.subheader("Login Section")

	    username = st.sidebar.text_input("User Name")
	    password = st.sidebar.text_input("Password",type='password')
	    if st.sidebar.checkbox("Login"):
		    # if password == '12345':
		    create_usertable()
		    hashed_pswd = make_hashes(password)

		    result = login_user(username,check_hashes(password,hashed_pswd))
		    if result:

			    st.success("Logged In as {}".format(username))

			    # user chooses either metric or imperial, the results differ for each option
                metric_imperial = st.session_state.selectbox('Are you Metric or Imperial(US) (Metric/Imperial): ', ['Metric', 'Imperial'])

                if metric_imperial == 'Metric':
                    st.subheader('Utility usage:')

                    # user is asked to input the values to calculate their footprint for metric
                    yearly_electric = st.session_state.number_input('How many KWh of electricity do you use per year?: ', 0, 100000)
                    yearly_electric = float(yearly_electric)

                    yearly_natural_gas = st.session_state.number_input('How many cubic meters of natural gas do you use per year?: ', 0, 100000)
                    yearly_natural_gas = float(yearly_natural_gas)

                    yearly_propane_gas = st.session_state.number_input('how many cubic meters of propane gas do you use per year?: ', 0, 100000)
                    yearly_propane_gas = float(yearly_propane_gas)

                    yearly_oil = st.session_state.number_input('how many litres of oil do you use per year for heating purposes?: ', 0, 100000)
                    yearly_oil = float(yearly_oil)

                    st.subheader('Transport:')
                    total_yearly_mileage = st.session_state.number_input('how many miles have you done in your vehicle this year?: ', 1, 100000)
                    total_yearly_mileage = float(total_yearly_mileage)
                    total_yearly_gallons = total_yearly_mileage / 25
                    total_yearly_gallons = float(total_yearly_gallons)

                    number_of_flights_less = st.session_state.number_input('How many flights have you taken this year' +
                                                                'that are 4 hours or less?: ', 0, 50)
                    number_of_flights_less = float(number_of_flights_less)

                    number_of_flights_more = st.session_state.number_input('How many flights have you taken this year' +
                                                                'that are 4 hours or more?: ', 0, 50)
                    number_of_flights_more = float(number_of_flights_more)

                    st.subheader('Recycling')
                    recycle_newspaper = st.session_state.selectbox('Do you recycle newspaper? (y/n): ', ['Yes', 'No'])

                    recycle_aluminium = st.session_state.selectbox('Do you recycle aluminium and tin? (y/n): ', ['Yes', 'No'])

                    trees = st.session_state.number_input("how many trees have you planted this year?: ", 0, 1000)
                    trees = float(trees)
                    carbon_offset = 46.2971   # the offset for each tree per year.

                    carbon_total = 0.0

                elif metric_imperial == 'Imperial':
                    st.subheader('Utility usage:')

                    # user is asked to input the values to calculate their footprint for imperial(US)
                    yearly_electric = st.session_state.number_input('How many Megajoules of electricity do you use per year?: ', 0, 100000)
                    yearly_electric = float(yearly_electric)

                    yearly_natural_gas = st.session_state.number_input('How many gallons of natural gas do you use per year?: ', 0, 100000)
                    yearly_natural_gas = float(yearly_natural_gas)

                    yearly_propane_gas = st.session_state.number_input('how many gallons of propane gas do you use per year?: ', 0, 100000)
                    yearly_propane_gas = float(yearly_propane_gas)

                    yearly_oil = st.session_state.number_input('how many gallons of oil do you use per year for heating purposes?: ', 0, 100000)
                    yearly_oil = float(yearly_oil)

                    st.subheader('Transport:')
                    total_yearly_mileage = st.session_state.number_input('how many miles have you done in your vehicle this year?: ', 1, 100000)
                    total_yearly_mileage = float(total_yearly_mileage)
                    total_yearly_gallons = total_yearly_mileage / 25
                    total_yearly_gallons = float(total_yearly_gallons)

                    number_of_flights_less = st.session_state.number_input('How many flights have you taken this year' +
                                                                ' that are 4 hours or less?: ', 0, 50)
                    number_of_flights_less = float(number_of_flights_less)

                    number_of_flights_more = st.session_state.number_input('How many flights have you taken this year' +
                                                                ' that are 4 hours or more?: ', 0, 50)
                    number_of_flights_more = float(number_of_flights_more)

                    st.subheader('Recycling')
                    recycle_newspaper = st.session_state.selectbox('Do you recycle newspaper? (y/n): ', ['Yes', 'No'])

                    recycle_aluminium = st.session_state.selectbox('Do you recycle aluminium and tin? (y/n): ', ['Yes', 'No'])

                    trees = st.session_state.number_input("how many trees have you planted this year?: ", 0, 1000)
                    trees = float(trees)
                    carbon_offset = 46.2971

                    carbon_total = 0.0


                # the brains of the program where the calculations are made.

                yearly_electric = yearly_electric * 0.994
                carbon_total = carbon_total + yearly_electric

                yearly_natural_gas = yearly_natural_gas * 11.7
                carbon_total = carbon_total + yearly_natural_gas

                yearly_propane_gas = yearly_propane_gas * 13
                carbon_total = carbon_total + yearly_propane_gas

                yearly_oil = yearly_oil * 19.6
                carbon_total = carbon_total + yearly_oil

                number_of_flights_less = number_of_flights_less * 1100
                carbon_total = carbon_total + number_of_flights_less

                number_of_flights_more = number_of_flights_more * 4400
                carbon_total = carbon_total + number_of_flights_more

                total_fuel_usage = total_yearly_mileage / total_yearly_gallons
                emission = total_fuel_usage * 19.6
                carbon_total = carbon_total + emission

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


                # yearly electric
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

                    with st.expander('You are using too much electricity! here are some ways to cut back on your usage:'):

                        for item in electricity_tips:
                            electricity_message = st.error(item)
                else:
                    with st.expander('Electricity: Good!'):
                        st.success('You are using the recommended amount of electricity, good job!')


                # gas
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
                    with st.expander('You are using too much gas! here are some ways to cut back on your usage:'):

                        for item in natural_gas_tips:
                            nat_gas_message = st.error(item)
                else:
                    with st.expander('Gas: Good!'):
                        st.success('You are using the recommended amount of gas, good job!')

                # oil
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

                    with st.expander('You are using too much oil! here are some ways to cut back on your usage:'):
                        for item in oil_tips:
                            oil_message = st.error(item)
                else:
                    with st.expander('Oil: Good!'):
                        st.success('You are using the recommended amount of oil, good job!')

                # mileage
                if total_yearly_mileage > 5920:
                    mileage_tips = [
                        'Consider eating and buying locally rather than travelling far',
                        'consider using an electric vehicle',
                        'do not travel far unless you need to',
                        'consider having localised holidays rather than ones far away'
                    ]

                    with st.expander('You have a higher mileage than average,' + 
                                        ' here are some ways to cut back on your mileage:'):
                        for item in mileage_tips:
                            mileage_message = st.error(item)
                else:
                    with st.expander('Mileage: Good!'):
                        st.success('You have an average or lower than average mileage, good job!')

                # flights (less than 4 hours)
                if number_of_flights_less > 6 * 1100:
                    flights_tips_less = [
                        'Consider flying abroad less for holidays',
                        'Consider whether it is better to fly for business trips, or take the bus, train or car'
                    ]

                    with st.expander('You have been on a higher number of flights (less than 4 hours) than' +
                                        ' the average here are some ways to cut back on your flights:'):
                        for item in flights_tips_less:
                            flights_less_message = st.error(item)
                else:
                    with st.expander('Flights (less than 4 hours): Good!'):
                        st.success('You have an average or lower than average number of flights (less than 4 hours)' +
                                    ', Good Job!')

                # flights (more than 4 hours)
                if number_of_flights_more > 2 * 4400:
                    flights_tips_more = [
                        'Consider flying abroad less for holidays',
                        'Consider whether it is better to fly for business trips, or take the bus, train or car',
                        'Consider flights that are less than 4 hours long'
                    ]
                    with st.expander('You have been on a higher number of flights (more than 4 hours) than' +
                                        ' the average here are some ways to cut back on your flights:'):

                        for item in flights_tips_more:
                            flights_more_message = st.error(item)
                else:
                    with st.expander('Flights (more than 4 hours): Good!'):
                        st.success('You have an average or lower than average number of flights (more than 4 hours)' +
                                    ', Good Job!')

                # recycling paper
                if recycle_newspaper == 'No':
                    recycle_paper_tips = [
                        'consider recycling newspaper',
                        'consider recycling paper',
                        'consider recycling cardboard'
                    ]
                    with st.expander('You do not recycle paper items such as cardboard, newspaper, paper, letters ' +
                                        'here are some ways to increase your recycling habits:'):

                        for item in recycle_paper_tips:
                            recycle_paper_message = st.error(item)
                else:
                    with st.expander('Recycling Paper: Good!'):
                        st.success('You recycle paper items such as newspaper, paper, letters, cardboard, ' +
                                    'good job!')

                # recycling aluminium and tin
                if recycle_aluminium == 'No':
                    recycle_aluminium_tips = [
                        'consider recycling tins',
                        'consider recycling any items that contain aluminium',
                        'consider recycling foil'
                    ]
                    with st.expander('You do not recycle aluminium or tin items such as tins, foil, ' +
                                        'products containing aluminium, ' +
                                        'here are some ways to increase your recycling habits:'):

                        for item in recycle_aluminium_tips:
                            recycle_aluminium_message = st.error(item)
                else:
                    with st.expander('Recycling Aluminium & Tin: Good!'):
                        st.success('You recycle aluminium and tin items such as tins, foil, ' +
                                    'products containing aluminium ' +
                                    'good job!')    

                # how many trees has the user planted?
                if carbon_offset < 138.8913:
                    carbon_offset_tips = [
                        'plant more trees or flowers',
                        'use sites like https://www.tree-nation.com to plant trees for free'
                    ]
                    with st.expander('You do not plant enough trees to offset your carbon emissions ' +
                                        'here are some ways to offset your carbon emissions:'):

                        for item in carbon_offset_tips:
                            carbon_offset_message = st.error(item)
                else:
                    with st.expander('carbon offset: Good!'):
                        st.success('You plant the average number of trees to offset your emissions ' +
                                    ' good job!')    

                # carbon footprint result is displayed
                st.subheader('Your Carbon Footprint:')
                carbon_footprint = st.text(f'Your Carbon Footprint is {carbon_total} tonnes of CO2')

                carbon_total_footprint = float(carbon_total)

                name_input = st.text_input('name')

                fields = [name_input, carbon_total_footprint]

                result = st.button("Submit")

                if result:

                    with open('leaderboard.csv', 'a', newline='') as f:  # Append & read mode

                        writer = csv.writer(f)
                        writer.writerow(fields)

                st.info(" #### Show contents of the CSV file :point_down:")
                st.dataframe(pd.read_csv("leaderboard.csv", names=["name", "carbon_total"]), height=300)

                    # Add a button to log out
                    if st.button('Log out'):
                        st.info('You have been successfuly logged out! Goodbye.')
                        # Clear the username and password inputs
                        sidebar.empty()
                        # Reload the page
                        st.experimental_rerun()

			        else:
			            st.warning("Incorrect Username/Password")

    elif choice == "SignUp":
		    st.subheader("Create New Account")
		    new_user = st.text_input("Username")
		    new_password = st.text_input("Password",type='password')

		    if st.button("Signup"):
			    create_usertable()
			    add_userdata(new_user,make_hashes(new_password))
			    st.success("You have successfully created a valid Account")
			    st.info("Go to Login Menu to login")
st.write(
    f"""
    Settings values
    ---------------
    - **Input**: {st.session_state.text}
    - **number_input**: {st.session_state.number_input}
    - **Slider**: `{st.session_state.slider}`
    - **Checkbox**: `{st.session_state.checkbox}`
    - **Radio**: {st.session_state.radio}
    - **Selectbox**: {st.session_state.selectbox}
    - **Multiselect**: {", ".join(st.session_state.multiselect)}
    """

)


def page_settings():
    st.header("Change settings")

    st.text_input("Input", key=persist("text"))
    st.slider("Slider", 0, 10, key=persist("slider"))
    st.checkbox("Checkbox", key=persist("checkbox"))
    st.radio("Radio", st.session_state["options"], key=persist("radio"))
    st.selectbox("Selectbox", st.session_state["options"], key=persist("selectbox"))
    st.multiselect("Multiselect", st.session_state["options"], key=persist("multiselect"))


PAGES = {
    "home": page_home,
    "settings": page_settings,


	

if __name__ == '__main__':
    load_widget_state()
	main()