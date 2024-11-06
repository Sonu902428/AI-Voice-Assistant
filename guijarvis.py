import tkinter as tk
from tkinter import ttk
from threading import Thread
from PIL import Image, ImageTk
from jarvis import greetMe, takeCommand
from search import takeCommand, google_search,speak,wikipedia_search,youtube_search
import datetime
import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
# import pyaudio
import pyautogui

BG_COLOR = "#D2C6E2"
BUTTON_COLOR = "#F9F4F2"
BUTTON_FONT = ("Arial", 14, "bold")
BUTTON_FOREGROUND = "black"
HEADING_FONT = ("white", 24, "bold")
INSTRUCTION_FONT = ("Helvetica", 14)

stop_flag = False


class VoiceAssistantGUI:
    def __init__(self, master):
        self.master = master
        master.title("Voice Assistant")
        master.geometry("1920x1080")  # Set window size to 1920x1080
        master.configure(bg=BG_COLOR)

        # Load and set the background image
        background_image = Image.open("C://Users//dell//Pictures//flo-motion_5sec.gif")
        background_image = background_image.resize((1920, 1080), Image.LANCZOS)
        background_photo = ImageTk.PhotoImage(background_image)
        self.background_label = ttk.Label(master, image=background_photo)
        self.background_label.image = background_photo  # Keep reference to prevent garbage collection
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Heading
        heading_label = ttk.Label(master, text="Voice Assistant", font=HEADING_FONT, background=BG_COLOR)
        heading_label.pack(pady=20)

        # Create and place a button on the GUI
        self.button = ttk.Button(master, text="Start Voice Assistant", command=self.on_button_click,
                                 style="VoiceAssistant.TButton")
        self.button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Place the button at the center of the window

        # Style the button
        style = ttk.Style(master)
        style.configure("VoiceAssistant.TButton", font=BUTTON_FONT, background=BUTTON_COLOR,
                        foreground=BUTTON_FOREGROUND)
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    rate = engine.setProperty("rate", 150)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()
    def on_button_click(self):
        global stop_flag
        if not stop_flag:
            stop_flag = False
            Thread(target=self.start_voice_assistant).start()
        else:
            self.stop_voice_assistant()

    def start_voice_assistant(self):
        while True:
            query = takeCommand().lower()
            if "jarvis" in query:
                greetMe()
        # greetMe()  # Call the greetMe function from jaris_backend.py
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
                    print(temp)

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
    def stop_voice_assistant(self):
        global stop_flag
        speak("Stopping the Voice Assistant.")
        stop_flag = True

def main():
    root = tk.Tk()
    app = VoiceAssistantGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
