import streamlit as st
import datetime
import requests

'''
# How much will the ride cost?
'''
'''
## Let's find out
'''

date = st.date_input('Date input')
time = st.time_input('Time entry')
date_time = datetime.datetime.combine(date,time)

pickup_lon = st.number_input('Pick up longitutde')
pickpup_lat = st.number_input('Pick up latitude')
dropoff_lon = st.number_input('Drop off longitude')
dropoff_lat = st.number_input('Drop off latitude')
passengers = st.slider('Number of passengers', min_value = 1, max_value = 10)



url = 'https://taxifare-l74tpglpga-ew.a.run.app/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')
params = {'pickup_datetime' : date_time,
          'pickup_longitude' : pickup_lon,
          'pickup_latitude'  : pickpup_lat,
          'dropoff_longitude'  : dropoff_lon,
          'dropoff_latitude'  : dropoff_lat,
          'passenger_count'  : passengers
          }

response = requests.get(url, params = params).json()

fare = response['fare']

st.write('\n\n\n\n')
st.write(f'Here is the answer you are looking for $', round(fare,2))
