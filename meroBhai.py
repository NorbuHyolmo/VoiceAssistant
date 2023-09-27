#install module 
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import pywhatkit
#for keyboard input on whatsapp
import time
import pyautogui
from pynput.keyboard import Key, Controller
keyboard = Controller()


#speech recognition from microsoft
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

#changing the speech speed rate 
rate = engine.setProperty('rate', 180)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Goodmorning Nurboo Dai!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Nurboo Dai!")
    else:
        speak("Good Evening Nurboo Dai!")
    
    speak("Bhunnus k guhrum hahzur co lagi Nurboo Dai")

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
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        print("Bujhena Dai")
        speak("bouzena dai")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("norbuhyolmo7@gmail.com","ywxkdjhshmcqxhcl")
    server.sendmail('norbuhyolmo7@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

    #logic for executing tasks based on query 
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)   

        # elif 'open youtube' in query:
        #     edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
        #     url = "https://youtube.com"
        #     webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
        #     webbrowser.get('edge').open(url)

        elif 'play' in query:
            command = takeCommand()
            song = command.replace("play", "")
            speak("playing" + song)
            pywhatkit.playonyt(song)

        elif 'open visual studio' in query:
            visual_path = "C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\Common7\\IDE\\devenv.exe"
            os.startfile(visual_path)

        elif 'open code' in query:
            code_path = "C:\\Users\\norbu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif 'what time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is currently {strTime}")

        elif 'spotify' in query:
            edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            #spotify_path = "C:\\Users\\norbu\\AppData\\Roaming\\Spotify\\Spotify.exe"
            #os.startfile(spotify_path)
            url = "https://open.spotify.com/playlist/5IUVTamItMAX4nrbwqlcz6?si=7ddd6a726bd54da4"
            webbrowser.register('spotify', None, webbrowser.BackgroundBrowser(edge_path))
            webbrowser.get('spotify').open(url)
            time.sleep(5)
            pyautogui.click()
            keyboard.press(Key.space)
            keyboard.release(Key.space)

        elif 'geet' in query:
            music_path = "D:\\music\\Songs"
            songs = os.listdir(music_path)
            speak("yaekai chin hi tuh dai")
            os.startfile(os.path.join(music_path, (random.choice(songs))))

        elif 'send email' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = input("Please Enter the Receiver's Email: ")
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("Sorry Nurboo dai, I am not able to send this email")

        elif 'mere bhai' in query:
            speak("suhbai theek cha mero dai")

    
        elif 'netflix' in query:
            edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            url = "https://www.netflix.com/browse"
            webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
            webbrowser.get('edge').open(url)

        elif 'send message' in query:   
            try:
                pywhatkit.sendwhatmsg_instantly(
                phone_no = "+977-9813983137", 
                message = takeCommand(),
                )
                time.sleep(10)
                pyautogui.click()
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                speak("Message Sent! ")
            except Exception as e:
                speak("Message send vaheena Dai")

        elif 'done for now' in query:
            speak("Hush Nurbo dai")
            quit()

        else:
            speak("out of my reach for now dai")
