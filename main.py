import streamlit as st
import requests

def get_current_temperature(open_weathe_api, latitude, longitude):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={open_weathe_api}&units=metric"

    response = requests.get(url)
    data = response.json()

    if "main" in data:
        temperature = data["main"]["temp"]
        return temperature
    else:
        return None

def geographic_coordinates(city_name):
    iran_provinces_coordinates = {
    "Tehran": {"latitude": 35.6892, "longitude": 51.3890},
    "Isfahan": {"latitude": 32.6546, "longitude": 51.6680},
    "Shiraz": {"latitude": 29.5918, "longitude": 52.5836},
    "Tabriz": {"latitude": 38.0800, "longitude": 46.2919},
    "Mashhad": {"latitude": 36.2605, "longitude": 59.6168},
    "Ahvaz": {"latitude": 31.3183, "longitude": 48.6706},
    "Kermanshah": {"latitude": 34.3142, "longitude": 47.0650},
    "Rasht": {"latitude": 37.2808, "longitude": 49.5832},
    "Kerman": {"latitude": 30.2839, "longitude": 57.0834},
    "Urmia": {"latitude": 37.5527, "longitude": 45.0760},
    "Yazd": {"latitude": 31.8974, "longitude": 54.3569},
    "Zahedan": {"latitude": 29.4963, "longitude": 60.8629},
    "Bandar Abbas": {"latitude": 27.1832, "longitude": 56.2666},
    "Sari": {"latitude": 36.5633, "longitude": 53.0601},
    "Qom": {"latitude": 34.6399, "longitude": 50.8759},
    "Arak": {"latitude": 34.0954, "longitude": 49.7013},
    "Hamadan": {"latitude": 34.7982, "longitude": 48.5146},
    "Sanandaj": {"latitude": 35.3099, "longitude": 46.9988},
    "Bushehr": {"latitude": 28.9234, "longitude": 50.8203},
    "Khorramabad": {"latitude": 33.4878, "longitude": 48.3550},
    "Ardabil": {"latitude": 38.2498, "longitude": 48.2933},
    "Qazvin": {"latitude": 36.2688, "longitude": 50.0041},
    "Birjand": {"latitude": 32.8644, "longitude": 59.2211},
    "Ilam": {"latitude": 33.6351, "longitude": 46.4227},
    "Gorgan": {"latitude": 36.8427, "longitude": 54.4438},
    "Zanjan": {"latitude": 36.6736, "longitude": 48.4787},
    "Shahrekord": {"latitude": 32.3256, "longitude": 50.8599},
    "Yasuj": {"latitude": 30.6684, "longitude": 51.5876},
    "Semnan": {"latitude": 35.5790, "longitude": 53.3491},
    "Kashan": {"latitude": 33.9850, "longitude": 51.4096}
    }

    coordinates = iran_provinces_coordinates[city_name]
    latitude = coordinates["latitude"]
    longitude = coordinates["longitude"]

    return latitude, longitude

iran_provinces_capitals = [
    "Tehran","Isfahan","Shiraz","Tabriz",
    "Mashhad","Ahvaz","Kermanshah","Rasht",
    "Kerman","Urmia","Yazd","Zahedan",
    "Bandar Abbas","Sari","Qom","Arak",
    "Hamadan","Sanandaj","Bushehr","Khorramabad",
    "Ardabil","Qazvin","Birjand","Ilam",
    "Gorgan","Zanjan","Shahrekord","Yasuj",
    "Semnan","Kashan"]

st.title("Simple Weather App")
st.write("This application allows you to get the current temperature of Iranian provinces using the OpenWeatherMap API.")

# راهنمای دریافت API
st.markdown("""
### How to Get Your OpenWeatherMap API Key:
1. Go to the [OpenWeatherMap website](https://home.openweathermap.org/users/sign_up) and sign up for a free account.
2. After signing up, go to your profile and find the section **API Keys**.
3. Copy the API key and paste it in the field below.
""")

open_weathe_api = st.text_input('Enter your API')
city_name = st.selectbox('Enter the desired city', iran_provinces_capitals)
unit = st.selectbox('Select the temperature measurement unit:',['centigrade', 'fahrenheit'])

if st.button('Get information'):
    latitude, longitude = geographic_coordinates(city_name)

    if 'centigrade' == unit:
        centigrade = get_current_temperature(open_weathe_api, latitude, longitude)
        st.write(f'The air temperature of {city_name} city is {centigrade} degrees {unit}')
    else:
        centigrade = get_current_temperature(open_weathe_api, latitude, longitude)
        fahrenheit = (centigrade * 9/5) + 32
        st.success(f'The air temperature of {city_name} city is {fahrenheit} degrees {unit}')
