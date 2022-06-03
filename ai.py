from datetime import datetime
from time import strftime
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

takecommand = True

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    time = datetime.now().strftime("%H:%M:%S")
    speak(time)

def date():
    year = datetime.now().year
    month = datetime.now().month
    date = datetime.now().day

    speak(date)
    speak(month)
    speak(year)

def greetme():
    speak("welkome sir! all programs will be loaded soon.")
    speak("the time right now is")
    time()
    speak("the date of today is")
    date()
    speak("where can i help u with sir!")




def goodbye():
    hour = datetime.now().hour
    if hour >=6 and hour<12:
        speak("have agood morning sir")
    elif hour >= 12 and hour<18:
        speak("have a good afternoon sir")
    elif hour >= 18 and hour<24:
        speak("have a good evening sir")
    else:
        speak("have a good night sir")


while takecommand == True:
    r = sr.Recognizer()
    Time = datetime.now().strftime("%H:%M")

    with sr.Microphone() as mic:
         print('listening...')
         
         audio_data = r.record(mic, duration=2)
         Tekst = r.recognize_google(audio_data)
         print("understood")
         print(Tekst)

    if Tekst == "stop program":
        exit()
    elif Tekst == "exit program":
        exit()
    
    if Tekst == "tell the time":
      speak(Time)
