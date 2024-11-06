import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 8)
    try:
        print("understanding...")
        query = r.recognize_google(audio, language="en-in")
        print(f"you said {query}\n")
    except Exception as e:
        print("say that again")
        return "none"
    return query

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def google_search(query):
    if "google" in query:
        import wikipedia
        query = query.replace("google", "")
        query = query.replace("google search", "")
        query = query.replace("jarvis", "")
        speak("this is I found on google")

    try:
        pywhatkit.search(query)
        result = wikipedia.summary(query, 1)
        speak(result)
    except:
        speak("not speakable output available")

def youtube_search(query):
    if "youtube" in query:
        query = query.replace("youtube", "")
        query = query.replace("youtube search", "")
        query = query.replace("jarvis", "")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("done")

# def wikipedia_search(query):
#     if "wikipedia" in query:
#         query = query.replace("wikipedia", "")
#         query = query.replace("wikipedia", "")
#         query = query.replace("jarvis", "")
#         # import wikipedia
#         result = wikipedia.summary(query, 2)
#         speak("According to wikipedia...")
#         print(result)
#         speak(result)

def wikipedia_search(query):
    if "wikipedia" in query:
        query = query.replace("wikipedia", "")
        query = query.replace("jarvis", "")
        try:
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia...")
            print(result)
            speak(result)
        except wikipedia.exceptions.DisambiguationError as e:
            options = e.options
            speak(f"The term '{query}' is ambiguous. It may refer to:")
            for option in options:
                speak(option)
            speak("Please provide a more specific query.")
        except wikipedia.exceptions.PageError as e:
            speak("Wikipedia page error. The requested page does not exist.")
        except wikipedia.exceptions.HTTPTimeoutError as e:
            speak("Wikipedia HTTP timeout error. Please check your internet connection.")
        except Exception as e:
            speak("An error occurred while fetching information from Wikipedia.")
            print(e)

