import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests

engine = pyttsx3.init()
r = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        
        try:
            sentence = r.recognize_google(audio, language='en-in')
            print(f"You said: {sentence}\n")
        except sr.UnknownValueError:
            speak("What")
            return "What"
        except Exception as e:
            speak("Sorry, my services are currently down. Try again later")
            return "None"
        return sentence
    
def create_note():
  speak("What should I write in the note?")
  note_text = listen()
  filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
  with open(filename, "w") as f:
    f.write(note_text)
  speak("Note saved.")
  
# create a function to read the saved notes too
# need to search by date or title
# advanced would be searching for it based on what was said in note
def read_note():
    speak("When was the note?")
    date = listen()
    filename = date + ".txt"
    with open(filename, "r") as f:
        speak(f)
    speak("That is the end.")
    
def main():
    speak("Hello, my name is AIVA. Your Artificial Intelligence Voice Assistant. How can I help you?")
    while True:
        command = listen().lower()
        if "bye" in command or "stop" in command:
            speak('Ok bye!')
            break
        if 'wikipedia' in command:
            statement = command.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in command:
            webbrowser.open_new_tab("https://wwww.youtube.com")
            speak("youtube is open now")
            time.sleep(5)
        elif "open google" in command:
            webbrowser.open_new_tab("https://wwww.google.com")
            speak("Google is open now")
            time.sleep(5)
        elif "search" in command:
            statement = command.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
        elif "play" in command:
            statement = command.replace("play", "")
            webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={statement}")
            time.sleep(5)
        time.sleep(3)
        