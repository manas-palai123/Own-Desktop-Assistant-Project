# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 11:21:08 2020

@author: user
"""
import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import os
import webbrowser
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


    

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1

        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def wishme():
    hour=int(datetime.datetime.now().hour)
    if(hour>0 and hour<12):
        speak("Good Morning Manas")
    elif(hour>12 and hour<17):
        speak("Good Afternoon Manas")
    elif(hour>=17 and hour<=21):
        speak("Good Evening Manas")
    else:
        speak("Good night Manas")
    speak("Please tell me how can i help you")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('manas.palai2005@gmail.com', 'manas@#@12345')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishme()
    
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            try:

                speak("Searching Wikipedia...")
                query=query.replace("wikipedia","")
                results=wikipedia.summary(query,sentences=2)
                speak("According to wikipedia")
                print(results) 
                speak(results)
            except Exception as e:
                #print(e)
                speak("Sorry my friend i can not find similar kind of page")
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'play music' in query:
            music_dir = 'C:\\Users\\user\\Music\\Playlists'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))   
        elif 'who are you' in query:
            speak("I am your Love. Myself Appy")
        elif 'who is god according to you' in query:
            speak("God is the creator and Mr. manas is my creator. So he is my God")
        elif 'to whom you love the most' in query:
            speak("I love both of you. But Seenu is So cute")
        elif 'what you need from me' in query:
            speak("I want nothing from you. Just i need your love only")
        elif("will you marry me") in query:
            speak("Yes I wan to marry you. But you know I am a machine. I can be your good friend ")
        elif ("where are you") in query:
            speak("I am in a Loop")
        elif 'how are you' in query:
            speak("I am fine. Tell me about you")
        elif 'i am also fine' in query:
            speak("ok then")
        elif "what is your father's name" in query:
            speak("Mr Manas Palai is my father")
        elif "who is sinu" in query:
            speak("Seenu is queen of her world.She is the most cutest girl in her dream")
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "manas.palai2005@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")
        elif 'stop' in query:
            speak("OK Manas Have a good day")
            break 
            
    
    
    
    
    
    
    