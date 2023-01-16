import sys
from googlesearch import search
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import pyjokes
import pyaudio
import time
import requests, json
import math

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

# talk("I am smarter than humans")
def take_command():

    with sr.Microphone() as source:
        print("Listening...")
        engine.say('Hello, how may I help you?')
        engine.runAndWait()
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
        try:
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'bob' in command:
                command = command.replace('bob', '')
                print(command)
        except:
            print("Unable to understand audio")
    return command

def run_bob():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        dt = str(datetime.date.today())
        print(dt)
        talk("Today's date is " + dt)
    elif 'are you single' in command:
        talk("I'm in a relationship with WiFi")
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)
        print(joke)
    elif 'weather' in command:
        api_key = "b49fc337dde81490958f556094103567"
        base_url = " http://api.openweathermap.org/data/2.5/weather?"
        city_name = "guwahati"
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()

        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"] - 273.15
            val = "Temperature is " + str(math.trunc(current_temperature)) + " degree celsius"
            print(str(val))
            talk(val)
        else:
            talk("City Not Found")
    elif 'stop' in command:
        sys.exit()
    elif 'search the internet' or 'search the web' or 'search' or 'search google' in command:
        query = command.replace('search', '')
        for j in search(query, tld='com', num=10, stop=10, pause=1):
            print(j)
    else:
        talk("Unable to understand audio")

if __name__ == "__main__":
    run_bob()