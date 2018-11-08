import pyttsx

print("Please enter what you want to hear")
engine = pyttsx.init()
engine.say("The quick brown fox jumped over the lazy dog.")
engine.runAndWait()
