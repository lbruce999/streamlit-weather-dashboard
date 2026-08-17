import requests
import streamlit as st


# -------------------------
# USER INPUT
# -------------------------

user = st.text_input("Enter City")


# -------------------------
# API CALL
# -------------------------

def get_input(user):
    if user == "":
        return None

    URL = f"https://wttr.in/{user}?format=j1"

    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()

        API_DATA = response.json()

        return API_DATA

    except requests.RequestException:
        return None


# -------------------------
# GET CURRENT CONDITIONS
# -------------------------

def current_conditions(api_data):
    conditions = api_data["current_condition"]

    for condition in conditions:
        return condition


# -------------------------
# GET LOCATION INFORMATION
# -------------------------

def get_nearest_area(api_data):
    areas = api_data["nearest_area"]

    for area in areas:
        return area


def get_city(nearest_area):
    area_names = nearest_area["areaName"]

    for city in area_names:
        return city["value"]


def get_region(nearest_area):
    regions = nearest_area["region"]

    for region in regions:
        return region["value"]


# -------------------------
# GET WEATHER DATA
# -------------------------

def get_temperature(current_condition):
    temperature = current_condition["temp_F"]

    return temperature


def get_weather_con(current_condition):
    weather_conditions = current_condition["weatherDesc"]

    for condition in weather_conditions:
        return condition["value"]


def get_humidity(current_condition):
    humidity = current_condition["humidity"]

    return humidity


def get_wind_speed(current_condition):
    wind_speed = current_condition["windspeedMiles"]

    return wind_speed


# -------------------------
# WEATHER MESSAGE
# -------------------------

def get_weather_message(temperature):
    num_temp = int(temperature)

    if num_temp >= 80:
        return "It's hot outside!"

    elif num_temp < 60:
        return "It's chilly outside!"

    else:
        return "It's a nice day!"


# -------------------------
# GET TODAY'S FORECAST
# -------------------------

def get_today_weather(api_data):
    weather = api_data["weather"]

    for day in weather:
        return day


def get_date(today_weather):
    date = today_weather["date"]

    return date


# -------------------------
# RUN APP
# -------------------------

api_data = get_input(user)


# Nothing has been entered yet
if user == "":
    st.info("Enter a city to load the weather.")


# User entered something, but API failed
elif api_data is None:
    st.error("Could not load weather data. Try another city.")


# API worked!
else:

    current_condition = current_conditions(api_data)

    nearest_area = get_nearest_area(api_data)

    today_weather = get_today_weather(api_data)


    # Extract values

    city = get_city(nearest_area)

    region = get_region(nearest_area)

    temperature = get_temperature(current_condition)

    condition = get_weather_con(current_condition)

    humidity = get_humidity(current_condition)

    wind_speed = get_wind_speed(current_condition)

    date = get_date(today_weather)


    # -------------------------
    # STREAMLIT UI
    # -------------------------

    weather_con = st.container(border=True)

    weather_con.title("Weather Dashboard")

    weather_con.header(f"{city}, {region}")

    weather_con.text(
        f"Temperature: {temperature}°F"
    )

    weather_con.text(
        f"Condition: {condition}"
    )

    weather_con.text(
        f"Humidity: {humidity}%"
    )

    weather_con.text(
        f"Wind Speed: {wind_speed} mph"
    )

    weather_con.text(
        f"Message: {get_weather_message(temperature)}"
    )

    weather_con.text(
        f"Today's Date: {date}"
    )