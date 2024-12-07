import os
import requests
from config import openweathermap_api_key

def get_current_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={openweathermap_api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            return f"The current weather in {city} is {weather_description} with a temperature of {temperature}°C."
        else:
            return "Unable to fetch current weather. Please try again later."
    except Exception as e:
        print("An error occurred while fetching current weather:", e)
        return "Unable to fetch current weather. Please try again later."
