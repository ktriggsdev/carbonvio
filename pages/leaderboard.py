import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='Carbonvio',
    page_icon='img/carbonvio.ico',
    menu_items={
        'Report a bug': "https://github.com/ktriggsdev/carbonvio/issues",
        'About': "Carbonvio, A carbon footprint calculator with a difference."
    })
st.title('Carbon Emissions Leaderboard')

# Define a filename to store the user credentials
filename = 'credentials.csv'

# Load the dataframe from the file if it exists, or create a new one
try:
    df = pd.read_csv(filename)
except FileNotFoundError:
    df = pd.DataFrame({
        'username': ['admin'],
        'password': ['5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8']
    })

# Define a function to hash passwords
def hash_password(password):
    return hashlib.sha1(password.encode('utf-8')).hexdigest()

# Define a function to check if the username and password are valid
def check_credentials(username, password):
    password_hash = hash_password(password)
    return (username in df['username'].values) and (password_hash == df[df['username'] == username]['password'].iloc[0])

# Define a function to register a new account
def register_account(username, password):
    password_hash = hash_password(password)
    # Check if the username is already taken
    if username in df['username'].values:
        return False
    else:
        # Append the new credentials to the dataframe
        df.loc[len(df)] = [username, password_hash]
        # Save the dataframe to the file
        df.to_csv(filename, index=False)
        return True

# Create a title and a sidebar
st.title('Login System')
sidebar = st.sidebar

# Ask the user to choose between login or register in the sidebar
mode = sidebar.radio('Choose mode', ['Login', 'Register'])

# If the user chooses login, ask them to enter username and password in the sidebar
if mode == 'Login':
    username = sidebar.text_input('Username')
    password = sidebar.text_input('Password', type='password')

    # If the user clicks the login button, check the credentials and display a message
    if sidebar.button('Login'):
        if check_credentials(username, password):
            st.success('Welcome back {}'.format(username))

            st.dataframe(pd.read_csv("leaderboard.csv", names=["name", "carbon_total"]), height=300)

            # Add a button to log out
if st.button('Log out'):
                st.info('You have been successfuly logged out! Goodbye.')
                # Clear the username and password inputs
                sidebar.empty()
                # Reload the page
                st.experimental_rerun()
else:
            st.error('Sorry, that isnt a valid username or password. Please try again')

# If the user chooses register, ask them to enter a new username and password in the sidebar
if  mode == 'Register':
    new_username = sidebar.text_input('Create a username')
    new_password = sidebar.text_input('Create a new password', type='password')

    # If the user clicks the register button, register a new account and display a message
if sidebar.button('Register'):
        if register_account(new_username, new_password):
            st.success('Welcome to Carbonvio!. You can now login with your new credentials.')
        else:
            st.error('Sorry, that username is already taken. Please choose a different one.')
