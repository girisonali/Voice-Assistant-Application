import pyttsx3

engine = pyttsx3.init()

text = "Hello! Welcome to Python"
engine.say(text)
engine.runAndWait()
