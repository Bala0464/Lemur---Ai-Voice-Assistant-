import subprocess
import tkinter
import json
import random
import operator
import datetime
import webbrowser
import os
import smtplib
import ctypes
import time
import shutil
import wolframalpha
import wikipedia
import pyjokes
import feedparser
import requests
import pyttsx3
import winshell
import re
import speech_recognition as sr
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
import win32com.client as wincl
from urllib.request import urlopen
from decouple import Event
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning balu!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon balu!")

    else:
        speak("Good Evening  balu!")

    speak("How was your day till now?")


def username():
    uname ='balu'
    speak("Welcome back ")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome back ".center(columns))
    print("#####################".center(columns))

    speak("How can i Help you, balu")
    assname="chinni"


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        speak("Unable to Recognize your voice.")
        return "None"
    return query


import os
import subprocess as sp


paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'discord': "C:\\Users\\ashut\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}
def open_camera(): 
    sp.run('start microsoft.windows.camera:', shell=True)

def open_notepad():
    os.startfile(paths['notepad'])


def open_discord():
    os.startfile(paths['discord'])

def open_cmd():
    os.system('start cmd')

def open_calculator():
    sp.Popen(paths['calculator'])

def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results

def play_on_youtube(video):
    kit.playonyt(video)

def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)

def send_email(receiver_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email["Subject"] = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(email,password)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False
  
def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']

def weather():
    api_key = "AAAAPPPPIIII_____KKKKEEEEYYYY"  # Enter the API key you got from the OpenWeatherMap website
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    speak("Which city weather do you want me to search balu ?")
    print("Which city weather do you want me to search balu ?")
    city_name = takeCommand().lower()
    complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name  # This is to complete the base_url, you can also do this manually to checkout other weather data available
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        z = x["weather"]
        weather_description = z[0]["description"]
        speak("Here's the ")
        speak(city_name)
        speak("weather report")
        print(" Temperature (in kelvin unit) is " + str(current_temperature) + "\n It would be  " + str(weather_description))
        speak(" Temperature (in kelvin unit) is " + str(current_temperature) + "\n It would be  " + str(weather_description))
    else:
        print(" City Not Found ")
        speak(" City Not Found ")
        
        
def add(num1, num2):
    return num1 + num2
 

def subtract(num1, num2):
    return num1 - num2
 

def multiply(num1, num2):
    return num1 * num2
 

def divide(num1, num2):
    return num1 / num2


if __name__ == '__main__':
    clear = lambda: os.system('cls')
    clear()
    wishMe()
    username()

    while True:

        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia")
            result = wikipedia.summary("google", sentences = 4)
            print(result)
            speak(result)

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open hackerrank' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("hackerrank.com")

        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            # music_dir = "G:\\Song"
            webbrowser.open("gaana.com")
            
        elif 'the time' in query:
            now = datetime.datetime.now()
            speak ("Current date and time : ")
            print (now.strftime("%Y-%m-%d %H:%M:%S"))
            speak (now.strftime("%Y-%m-%d %H:%M:%S"))

        elif 'open opera' in query:
            codePath = r"C:\\Users.exe"
            os.startfile(codePath)

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, balu")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query

        elif "change name" in query:
            speak("What would you like to call me, balu")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)


        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Balu.")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "calculate" in query:
            print("What is the first number balu")
            speak("What is the first number balu")
            number_1 = takeCommand().lower()
            print("What is the second number balu")
            speak("What is the secind number balu")
            number_2 = takeCommand().lower()
            speak("Please select operation -\n" \
                "1. Addition\n" \
                "2. Subtract\n" \
                "3. Multiply\n" \
                "4. Divide\n")
            speak("Please say the number to do the operation")
            select = int(takeCommand().lower())
            if select == 1:
                print(number_1, "+", number_2, "=",
                      add(number_1, number_2))
                speak(number_1, "+", number_2, "=",
                      add(number_1, number_2))
            elif select == 2:
                print(number_1, "-", number_2, "=",
                      subtract(number_1, number_2))
                speak(number_1, "-", number_2, "=",
                      subtract(number_1, number_2))
            elif select == 3:
                print(number_1, "*", number_2, "=",
                      multiply(number_1, number_2))
                speak(number_1, "*", number_2, "=",
                      multiply(number_1, number_2))
            elif select == 4:
                print(number_1, "/", number_2, "=",
                      divide(number_1, number_2))
                speak(number_1, "/", number_2, "=",
                      divide(number_1, number_2))
            else:
                print("Invalid input")
                speak("Invalid input")

        elif 'search' in query or 'play' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "who i am" in query:
            speak("If you talk then definitely your human.")

        elif "why you came to world" in query:
            speak("Thanks to Balu. further It's a secret")

        elif 'power point presentation' in query:
            speak("opening Power Point presentation")
            power = 'onmech'
            os.startfile(power)

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Balu")

        elif 'reason for you' in query:
            speak("I am on the balu's aim in the life ")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed successfully")

        elif 'open bluestack' in query:
            appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
            os.startfile(appli)

        elif 'news' in query:
            speak(f"I'm reading out the latest news headlines and printing it on the screen for u , balu")
            url = 'https://www.bbc.com/news'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            headlines = soup.find('body').find_all('h3')
            unwanted = ['BBC World News TV', 'BBC World Service Radio','News daily newsletter', 'Mobile app', 'Get in touch']
            for x in list(dict.fromkeys(headlines)):
                if x.text.strip() not in unwanted:
                    print(x.text.strip())
                    speak(x.text.strip())
                    
            speak(f"That's for today's news balu")


        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))
        elif "update assistant" in query:
            speak("After downloading file please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream=True)

            with open("Voice.py", "wb") as Pypdf:

                total_length = int(r.headers.get('content-length'))

                for ch in progress.bar(r.iter_content(chunk_size=2391975),
                                       expected_size=(total_length / 1024) + 1):
                    if ch:
                        Pypdf.write(ch)
        elif "jarvis" in query:

            wishMe()
            speak("Jarvis 1 point o in your service ")
            speak(assname)

        elif 'weather' in query:
            weather()

            
        elif "send message " in query:
            account_sid = 'Account Sid key'
            auth_token = 'Auth token'
            client = Client(account_sid, auth_token)
            message = client.messages \
                .create(
                body=takeCommand(),
                from_='Sender No',
                to='Receiver No'
            )
            print(message.sid)

        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "Good Morning" in query:
            speak("A warm" + query)
            speak("How are you balu")
            speak(assname)
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")
        elif "how are you" in query:
            speak("I'm fine, glad you me that")
        elif "i love you" in query:
            speak("It's hard to understand")
        elif "what is" in query or "who is" in query:

            # Use the same API key
            # that we have generated earlier
            client = wolframalpha.Client("API_ID")
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")
        elif 'open notepad' in query:
            open_notepad()

        elif 'open discord' in query:
            open_discord()

        elif 'open command prompt' in query or 'open cmd' in query:
            open_cmd()

        elif 'open camera' in query:
            open_camera()

        elif 'open calculator' in query:
            open_calculator()
        elif "send an email" in query:
            speak("On what email address do I send balu? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject balu?")
            subject = take_user_input().capitalize()
            speak("What is the message balu?")
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email balu.")
            else:
                speak("Something went wrong while I was sending the mail. Please check the error logs balu")

        elif 'joke' in query:
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(joke)

        elif "advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            print(advice)

        
        
    # elif "" in query:
    # Command go here
    # For adding more commands
