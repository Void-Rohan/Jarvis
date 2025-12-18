import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import time
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "fd2a79114b1a4a0ebf16180d1b904016"


def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open insta" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open gmail" in c.lower():
        webbrowser.open("https://gmail.com")
    elif "open discord" in c.lower():
        webbrowser.open("https://discord.com")
    elif "open hianime" in c.lower():
        webbrowser.open("https://hianime.com")
    elif "open chatgpt" in c.lower():
        webbrowser.open("https://chatgpt.com")
    elif "open deepseek" in c.lower():
        webbrowser.open("https://chat.deepseek.com")
    elif "open chatgpt" in c.lower():
        webbrowser.open("https://chatgpt.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=bd&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()

            # Extract the articles
            articles = data.get('articles', [])

            # Print the headlines
            for article in articles:
                speak(article['title'])

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()
        # recognize speech using google
        print("Recognizing...")
        try:
            # Listen for the wakeup call "Jarvis"
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes")
                time.sleep(1)
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))
