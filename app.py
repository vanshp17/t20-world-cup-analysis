import streamlit as st
import pandas as pd
import pickle

pipe = pickle.load(open('t20_pipe.pkl','rb'))

#url = 'https://th.bing.com/th/id/OIP.egpQvkrgWbjF3QBtlatTDQAAAA?rs=1&pid=ImgDetMain.jpeg'

# Function to load local CSS file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load CSS
local_css("style.css")

# top 10 teams
teams = [
    'Australia',
    'India',
    'Bangladesh',
    'South Africa',
    'West Indies',
    'Afghanistan',
    'New Zealand',
    'Sri Lanka',
     'England',
    'Pakistan'
]

cities = ['Colombo',
         'Mirpur',
         'Johannesburg',
         'Dubai',
         'Auckland',
         'Cape Town',
         'London',
         'Pallekele',
         'Barbados',
         'Melbourne',
         'Durban',
         'St Lucia',
         'Sydney',
         'Wellington',
         'Lauderhill',
         'Hamilton',
         'Centurion',
         'Manchester',
         'Abu Dhabi',
         'Mumbai',
         'Nottingham',
         'Southampton',
         'Mount Maunganui',
         'Chittagong',
         'Kolkata',
         'Lahore',
         'Delhi',
         'Nagpur',
         'Chandigarh',
         'Adelaide',
         'Bangalore',
         'St Kitts',
         'Cardiff',
         'Christchurch',
         'Trinidad']

st.title('Welcome to T20 World Cup Analysis')

col1,col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select batting team ', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select bowling team ', sorted(teams))

city = st.selectbox('Select City ',sorted(cities))

col3,col4,col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score')
with col4:
    overs = st.number_input('Overs Done (works for over>5)')
with col5:
    wickets = st.number_input('Wickets Out')


last_five_overs_runs = st.number_input('Runs scored in last 5 overs')

if st.button('Predict Score'):
    balls_left = 120 - overs*6
    wickets_left = 10 - wickets
    crr = current_score/overs

    input_df = pd.DataFrame(
        {'batting_team' : [batting_team],
         'bowling_team': [bowling_team],
         'city': [city],
         'current_score':[current_score],
         'balls_left':[balls_left],
         'wickets_left':[wickets_left],
         'crr':[crr],
        'last_five_overs_runs':[last_five_overs_runs]}
    )

    result = pipe.predict(input_df)

    st.header('Predicted Score ' +str(int(result[0])))
