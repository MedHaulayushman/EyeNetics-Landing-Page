import pyttsx3

def say(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
text=input("ENTER THE TEXT YOU WANT ME TO SAY:")
say(text)