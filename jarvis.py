import datetime
import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
# import pyaudio
import pyautogui
import numpy as np

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate", 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 3)

    try:
        print("Understanding...")
        query = r.recognize_google(audio,language="en-in")
        print(f"you said: {query}\n")
    except Exception as e:
        print("say that again ")
        return "None"
    return query

def greetMe():
    hour = int(datetime.datetime.now().hour)
    print(datetime.datetime.now())
    if hour >= 0 and hour <= 12:
        speak("Good morning")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Goood Evening")
    speak("how can i  help you")

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "jarvis" in query:
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query or "bye" in query:
                    speak("bye, you can call me anytime.")
                    break

                elif "hello" in query:
                    speak("hello, how are you !")
                elif "i am fine" in query:
                    speak("that's great")
                elif "how are you" in query or "what about you" in query:
                    speak("i am, perfect")
                elif "thank you" in query:
                    speak("you are welcome")
                elif "google" in query:
                    from search import google_search
                    google_search(query)
                elif "youtube" in query:
                    from search import youtube_search
                    youtube_search(query)
                elif "wikipedia" in query:
                    from search import wikipedia_search
                    wikipedia_search(query)

                elif "temperature" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current{search} is {temp}")
                    print(temp)

                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")
                    print(strTime)

                elif "open" in query:
                    from Dictapp import openappweb

                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

                # elif "set an alarm" in query:
                #     print("input time example:- 10 and 10 and 10")
                #     speak("Set the time")
                #     a = input("Please tell the time :- ")
                #     alarm(a)
                #     speak("Done,sir")

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from keyboard import volumeup

                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown

                    speak("Turning volume down, sir")
                    volumedown()

                elif "remember that" in query:
                    rememberMessage = query.replace("remember that", "")
                    rememberMessage = query.replace("jarvis", "")
                    speak("You told me to remember that" + rememberMessage)
                    remember = open("Remember.txt", "a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt", "r")
                    speak("You told me to remember that" + remember.read())

            break

