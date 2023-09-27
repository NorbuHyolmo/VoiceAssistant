import openai
#install module 
import pyttsx3
import speech_recognition as sr
import os
import smtplib
import pywhatkit
import datetime
import pyautogui

#speech recognition from microsoft
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[1].id)

#changing the speech speed rate 
rate = engine.setProperty('rate', 180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    #it takes microphone input from the user and returns string output
    #recognizer function to recognize the audio 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        #pause_threshold extends the time of non-speaking phase
        #bolirako bela 1s jati pause huda boleko complete nahos bhanera time extend gareko
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising....")
        speak("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        print("Bujhena Dai")
        speak("bouzena dai")
        return "None"
    return query

def chatgpt():
    openai.api_key = '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'

    messages = [ {"role": "system", "content": 
                    "Please act like my personal assistant and address me as boss"} ]
    
    print("how may i help you today ?")
    speak("how may i help you today?")
    while True:
        message = takeCommand()
        if message:
            messages.append(
                {"role": "user", "content": message},
            )
            chat = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo", messages=messages
            )
        reply = chat.choices[0].message.content
        if "close" in message:
            speak("Closing the program now")
            quit()
        else:
            print(f"ChatGPT: {reply}")
            speak(reply)
            messages.append({"role": "assistant", "content": reply})


chatgpt()



