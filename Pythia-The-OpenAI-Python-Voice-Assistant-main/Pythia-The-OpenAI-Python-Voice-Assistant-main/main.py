# main.py

import speech_recognition as sr
import os
from functionalities.open_website import open_website
from functionalities.open_music import open_music
from functionalities.open_apps import open_app
from functionalities.time import get_time
from functionalities.chat import chat, ai
from functionalities.weather import get_current_weather

def say(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language="en-in")
            print(f"User Said: {query}")
            return query
        except Exception as e:
            print("An error occurred while recognizing speech:", e)
            return "Some Error Occurred. Sorry, from Pythia"

if __name__ == '__main__':
    print('PyCharm')
    say("Hello I am Pythia A.I")
    chatStr = ""
    city = "Kathmandu"  # Replace with your city
    while True:
        print("Listening...")
        query = takeCommand()

        if "open" in query.lower():
            words = query.split()
            if len(words) > 1:
                action = words[0]
                parameter = words[1]
                if action == "open":
                    if parameter.lower() in ["facetime", "vlc", "safari"]:
                        say(open_app(parameter))
                    else:
                        say(open_website(parameter))
        elif "play music" in query.lower():
            # Call open_music function without any arguments
            say(open_music())
        elif "the time" in query.lower():
            # Retrieve current time using get_time function
            current_time = get_time(city)
            say(current_time)
        elif "current weather" in query.lower():
            current_weather = get_current_weather(city)
            say(current_weather)
        elif "Using artificial intelligence" in query:
            ai_response = ai(prompt=query)
            say(ai_response)
        else:
            chat_response = chat(query, chatStr)
            say(chat_response)
