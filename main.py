import streamlit as st
import requests

# Enter your API key here
api_key = "fda50ce4546f34788056603c1eeacbf4"
base_url = "https://api.openweathermap.org/data/2.5/weather"

# Center-align the title
st.markdown("<h1 style='text-align:center;'>Weather App</h1>", unsafe_allow_html=True)

# User input for location (e.g., city or zip code) with placeholder text
location = st.text_input("", value="Ilford",
                         placeholder="Enter location (city or zip code)")

if location:
    # Make a request to the weather API
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()

        # Center-align text and increase font size
        st.markdown(f"<div style='text-align:center; font-size:30px;'>Weather in {location}:</div>",
                    unsafe_allow_html=True)
        st.markdown(
            f"<div style='text-align:center; font-size:30px;'>Temperature: {weather_data['main']['temp']}°C</div>",
            unsafe_allow_html=True)

        # Center-align the image with a higher resolution
        weather_icon = weather_data['weather'][0]['icon']
        st.markdown(
            f"<div style='text-align:center;'><img src='http://openweathermap.org/img/w/{weather_icon}.png' width='200'></div>",
            unsafe_allow_html=True)
    else:
        st.error(f"Error fetching weather data for {location}. Status code: {response.status_code}")
