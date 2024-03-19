from logging import exception               #pip install exception
from time import struct_time
from bs4 import ResultSet
import pyttsx3                              #pip install pyttsx3, is a text-to-speech 
                                            #conversion library in Python
import speech_recognition as sr             # pip install speechRecognition
import datetime                             #it is already present 
import wikipedia                            #pip install wikipedia
import webbrowser                           #its already present
import os                                   #pip install os
import pandas as pd                         #pip insatll pandas
from matplotlib import pyplot as plt        #pip install matplotlib
import numpy as np                          #pip install numpy
import cv2                                  #pip install opencv-python 
                                            #this is for opening camera
import pywhatkit as kit   
from requests import get 
import smtplib
import config
import subprocess as sp



engine = pyttsx3.init('sapi5')                #we will use this to take voices
voices = engine.getProperty('voices')
print(voices[0].id)                          #this to get the vioce for our system 
engine.setProperty('voice', voices[0].id)     #change the id no. to get diffrent voices



def speak(audio):                             #this function is for speaking the audio 
    engine.say(audio)                         #we have given audio as an argument  
    engine.runAndWait()


def play_on_youtube(video):
    kit.playonyt(video)



def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)


def wishme():                                 #this will wish us acording to time
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(" good morning sir")
    elif hour>=12 and hour<18:
        speak(" good afternoon sir !")
    else:
        speak("good evening sir!")

    speak('''hello, i am jarvis version 3.1 speed one teraheads memory one zettabyte,
please tell how can i help you''')
    print('''hello, i am jarvis version 3.1 speed one teraheads memory one zettabyte,
please tell how can i help you''')


def hear():                                #it takes microphone input form the user and 
                                           #reutrns string output
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.Microphone() as sourse:
        print("listening...")
        r.pause_threshold = 0.5    # seconds of non-speaking audio before a phrase is 
                                   # considered complete, jab bhi ham bolenge and agar 
                                   # hamane gap liya 1 sec ka tho ye complete na kr de
        r.energy_threshold = 250   #it takes the sound in croud area , 
                                        #increse it if their is croud .. then we have to speak louad if we increse
                                        #threshod frequency
        r.dynamic_energy_ratio = 2 #dont know what changes this

        audio = r.listen(sourse)
        try:
            query = r.recognize_google(audio)
            print("user said:", end = " ")
            print(query)
        except Exception as e:
            print("i didn't get that...")
            speak(f"i didn't get that....")
            print("say that again please...")
            speak(f"say that again please... ")
            return "none"
        return query

        

if __name__ == "__main__":
    wishme()
    while True:
        query = hear().lower()
        if 'wikipedia' in query.lower():
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences =2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            #please provide path of folder wihch contains music of sound
            music_dir = "C:\\Users\\Vishu_96.k\\Music\\music_dir"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'play song' in query:
            #please provide path of folder wihch contains music of sound
            music_dir = "C:\\Users\\Vishu_96.k\\Music\\music_dir"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S:%p")
            speak(f"sir the time is {strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\Vishu_96.k\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'namaste' in query:
            speak(f"namste sir!")

        elif 'how are you' in query:
            speak(f"i am fine sir!")
                        
        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is  {ip}")

        elif 'open notepad' in query:
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)

        elif 'open camera' in query:
            sp.run('start microsoft.windows.camera:', shell=True)

        elif 'play on youtube' in query:
            play_on_youtube('https://www.youtube.com/watch?v=r0Hr4RumEzY')

        elif 'the date' in query:
            current_date = datetime.date.today()
            print(current_date)
            speak(current_date)

        elif "send whatsapp message" in query:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = hear().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")

        elif 'quit' in query:
            speak(f"ok sir, you can call me anytime! ")
            speak(f"just say wake up jarvis!")
            break

        elif 'you need a break' in query:
            speak(f"ok sir, you can call me anytime! ")
            speak(f"just say wake up jarvis!")
            break
        



        
        

        

                
        