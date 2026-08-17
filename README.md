# 🌤️ Streamlit Weather Dashboard

A simple interactive weather dashboard built with **Python**, **Streamlit**, and a live weather API.

Users can enter a city and receive current weather information including temperature, conditions, humidity, and wind speed.

## ✨ Features

- Search for weather by city
- Retrieve live weather data from an API
- Display current temperature in Fahrenheit
- Display current weather conditions
- Display humidity
- Display wind speed
- Generate a message based on the current temperature
- Handle empty input and failed API responses

## 🛠️ Built With

- **Python**
- **Streamlit**
- **Requests**
- **wttr.in Weather API**
- **JSON**

## 🔄 How It Works

The application follows a simple API data flow:

```text
User enters a city
        ↓
Streamlit captures the input
        ↓
Python sends an HTTP GET request
        ↓
Weather API returns JSON
        ↓
Python converts the response into a dictionary
        ↓
Functions extract the required weather data
        ↓
Streamlit displays the results
```

## 🧠 What I Practiced

I built this project while learning how data moves through a Python application.

Some of the concepts I practiced include:

- Creating and calling functions
- Function parameters
- Returning values from functions
- Passing returned values into other functions
- Working with dictionaries
- Navigating nested dictionaries and lists
- Sending HTTP GET requests
- Reading JSON API responses
- Extracting values from API data
- Converting strings into integers
- Using conditional logic
- Basic API error handling
- Connecting Python logic to a Streamlit interface

## 🚀 Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/lbruce999/streamlit-weather-dashboard.git
```

### 2. Enter the project directory

```bash
cd streamlit-weather-dashboard
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
streamlit run streamlit_app.py
```

Streamlit will start a local development server and open the dashboard in your browser.

## 📡 API

Weather information is retrieved from the **wttr.in** weather service.

The application sends a request based on the city entered by the user and receives a JSON response containing current weather information.

Example request:

```text
https://wttr.in/Youngstown?format=j1
```

The application then extracts the information it needs from the returned JSON instead of displaying the entire API response.

## 📂 Project Structure

```text
streamlit-weather-dashboard/
│
├── streamlit_app.py
├── requirements.txt
├── README.md
├── .gitignore
├── current_conditions.json
└── weather_data_test.ipynb
```

## 🔮 Future Improvements

Some features I would like to add as I continue developing the project:

- Multi-day weather forecasts
- Weather icons
- Celsius/Fahrenheit selection
- Improved invalid-city handling
- Better loading and API error states
- Additional weather information
- Streamlit Community Cloud deployment

## 📚 Project Purpose

This project was built as a hands-on exercise for learning Python application development and APIs.

Rather than only practicing functions individually, I wanted to understand how they work together inside an application:

**user input → function → API request → JSON → processing → returned values → UI**

That architecture will serve as the foundation for larger applications that consume APIs and work with external data.