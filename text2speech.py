import pyttsx3

data = input("say something ... \n")

engine = pyttsx3.init()
engine.say(data)
engine.runAndWait()