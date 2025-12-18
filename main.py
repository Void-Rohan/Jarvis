import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()


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
        webbrowser.open("https://instagram.com")
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
        musicLibrary.music(song)

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
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))
