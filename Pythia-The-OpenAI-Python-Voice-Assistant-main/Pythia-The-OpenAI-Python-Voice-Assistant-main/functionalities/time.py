import requests
from datetime import datetime
from config import timezonedb_api_key

def format_time(raw_time):
    try:
        # Convert the raw time string to a datetime objects
        dt_object = datetime.strptime(raw_time, "%Y-%m-%d %H:%M:%S")

        # Format the datetime object into a spoken-friendly format
        formatted_time = dt_object.strftime("%I:%M %p")
        return formatted_time
    except Exception as e:
        print("An error occurred while formatting time:", e)
        return "Unknown"

def get_time(city):
    try:
        url = f"http://api.timezonedb.com/v2.1/get-time-zone?key={timezonedb_api_key}&format=json&by=zone&zone=Asia/{city}"
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            current_time = data['formatted']
            formatted_time = format_time(current_time)
            print("Formatted time:", formatted_time)  # Debugging print statement
            return f"The current time in {city} is {formatted_time}"
        else:
            return "Unable to fetch current time. Please try again later."
    except Exception as e:
        print("An error occurred while fetching current time:", e)
        return "Unable to fetch current time. Please try again later."
