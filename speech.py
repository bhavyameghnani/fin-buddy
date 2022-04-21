import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

engine=pyttsx3. init()
voices=engine.getProperty('voices')
engine.setProperty( 'voice',voices[1].id)
recognizer=sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print("Clearing background noises . .Please wait")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('Ask me anything. . ')
        recordedaudio=recognizer.listen(source)

    try:
        command=recognizer.recognize_google(recordedaudio)
        print("you said: ",text)
    except Exception as ex :
        print(ex)
    if 'time' in command:
        time=datetime.datetime. now().strftime ("%I:%M %p")
        print(time)
        engine.say(time)
        engine.runAndWait()

cmd()
