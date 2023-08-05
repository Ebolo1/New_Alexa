# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 15:42:44 2023
procedure
1. Importing speech_recognition, pyttsx3, pywhatkit, datetime, and wikipedia modules.
2. Creating a listener object from the speech_recognition module.
3. Creating a command variable to hold the voice command given by the user.
4. Creating a talk() function to convert the text to speech.
5. Creating a take_command() function to take voice commands from the user.
6. Creating a run_alexa() function to run the alexa code.
7. Creating a while loop to run the alexa code continuously.
@author: Ing.Ebolo Hsmiley
"""
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys 

"set microphone to accept sound"
my_mic = sr.Microphone(device_index=1)

"to recognize input from the microphone"
listener = sr.Recognizer()

"initialising my engine for Spectra to talk to me"
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with my_mic as source:
            print('listening....')
            'reduce noise inteference'
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            'prints the out put only if the word java is said in the command'
            if 'java' in command:
                command = command.replace('java', '')
                print(command)
    except:
        pass
    return command


def run_spectra():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        print(talk('playing' + song))
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        print(time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        date = datetime.date()
        talk(date)
        print(date)
    elif 'Hi' in command:
        talk('Hi, My is Java your virtual assistant, how can I help you today?')
    elif 'What is you name' in command:
        talk('My name is JAVA and what is yours')  
    elif 'who are you' in command:
        talk('I am Alexa your personal assistant. I am programmed to perform little task like opening youtube, google chrome and gmail etcetra ')
    elif 'are you single' in command:
        talk('I am in a virtual assistant, I can''t be in a relatonship')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'bye' in command:
        talk('Good bye see you soon')
        sys.exit()
    else:
        talk('Please say the command again.')

while True:
    run_spectra()
    