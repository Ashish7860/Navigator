import requests
from functions.online_ops import find_my_ip, get_latest_news, get_random_advice, get_random_joke, get_trending_movies, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message
import pyttsx3
import speech_recognition as sr
from decouple import config
from datetime import datetime
from functions.os_ops import open_calculator, open_camera, open_cmd, open_notepad, open_word
from random import choice
from utils import opening_text
from pprint import pprint

USERNAME = config('USER')
BOTNAME = config('BOTNAME')


engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# Text to Speech Conversion
def speak(text):
    """Used to speak whatever text is passed to it from the utils file ( for our project) """

    engine.say(text)
    engine.runAndWait() # wait after speaking


# Greet the user
def greet_user():
    """Greets the user according to the time"""
    
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    speak(f"Hello {USERNAME} , I am {BOTNAME}. How may I assist you?")


# Takes Input from User
def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query :
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak(f"Good night {USERNAME}, take care!")
            else:
                speak(f"Have a good day {USERNAME}!")
            exit()
    except Exception:
        speak(f"Sorry {USERNAME}, I could not understand. Could you please say that again?")
        query = 'None'
    return query


if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()

        if 'open notepad' in query:
            open_notepad()


        elif 'open command prompt' in query or 'open cmd' in query:
            open_cmd()

        elif 'open camera' in query:
            open_camera()

        elif 'open calculator' in query:
            open_calculator()

        # to be checked
        elif 'my ip address' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen {USERNAME}.')
            print(f'Your IP Address is {ip_address}')

        elif 'wikipedia' in query:
            speak(f'What do you want to search on Wikipedia, {USERNAME}?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak(f"For your convenience, I am printing it on the screen {USERNAME}.")
            print(results)

        elif 'youtube' in query:
            speak(f'What do you want to play on Youtube, {USERNAME}?')
            video = take_user_input().lower()
            play_on_youtube(video)

        elif 'search on google' in query:
            speak(f'What do you want to search on Google, {USERNAME}?')
            query = take_user_input().lower()
            search_on_google(query)

        elif "send whatsapp message" in query:
            speak(f'On what number should I send the message {USERNAME} Please enter in the console: ')
            number = input("Enter the number: ")
            speak(f"What is the message {USERNAME}?")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            speak(f"I've sent the message {USERNAME}.")


        elif 'joke' in query:
            speak(f"Hope you like this one {USERNAME}")
            joke = get_random_joke()
            speak(joke)
            speak(f"For your convenience, I am printing it on the screen {USERNAME}.")
            pprint(joke)

        elif "advice" in query:
            speak(f"Here's an advice for you, {USERNAME}")
            advice = get_random_advice()
            speak(advice)
            speak(f"For your convenience, I am printing it on the screen {USERNAME}.")
            pprint(advice)


        

