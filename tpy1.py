import pyttsx3
import speech_recognition as sr
import time
import datetime
import keyboard
from SartComands import openComands, search, messenger, notepad
from StopComands import whatTime
from TalkComands import firstWord, lastWords, Talk
from NotesComand import readPlans, wrightNewPlan, writing
from weather import  weather

# voice building
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

hours = int(datetime.datetime.now().hour)                         #часы
minutes = int(datetime.datetime.now().minute)                     #минуты
seconds = int(datetime.datetime.now().second)                     #секунды


# functions
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        q = r.recognize_google(audio, language='en-in')
        print(f"User said: {q}\n")
    except Exception as e:
        print(e)
        # speak("Say that again please...")
        return "None"
    return q


# def keyboardy():
#     key1 = keyboard.read_key()
#     if key1 == 'esc':
#         speak('waiting, press key "f1" to start')
#         return 0
#     else:
#         return 1


def workOpen(command):
    if 'search' in command:
        searchTxt = takeCommand().lower()
        search(searchTxt)
    if 'open' or 'play' in command:
        openComands(command)
    if 'weather' in command:
        speak(weather())



def workStop(command):
    if 'sleep' in command:
        time.sleep(whatTime(command))
        speak('Привет')
    elif 'goodbye' in command:
        speak(lastWords(hours))
        exit()


def workNote(command):
    if 'read ' in command:
        speak(readPlans())
    if 'show' in command:
        notepad()
    if 'write' in command:
        if 'note' in command:
            speak('dictate your note')
            txt = takeCommand().lower()
            wrightNewPlan(txt)
        if 'message' in command:
            messenger(command)
            speak('dictate your massage')
            while True:
                mes = takeCommand().lower()
                if 'thank you igor' in mes:
                    break
                else:
                    writing(mes)

# main program
speak(firstWord(hours))
speak(' Sir, I am Igor, your intelligent assistant')
while True:
   inputCommand = takeCommand().lower()
   workOpen(inputCommand)
   workStop(inputCommand)
   workNote(inputCommand)
   speak(Talk(inputCommand))
