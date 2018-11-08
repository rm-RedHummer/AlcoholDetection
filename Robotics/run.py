import speech_recognition as sr
import serial
import pyttsx3

engine = pyttsx3.init()
arduino = serial.Serial('COM7', 9600)
r = sr.Recognizer()
while True:
	print("Type 1 for text to speech and type 2 for speech recognition")
	engine.say("Type 1 for text to speech and type 2 for speech recognition")
	engine.runAndWait()
	choice = input()
	if choice == "1":
		engine.say("Enter what you want to hear")
		engine.runAndWait()
		print("Enter what you want to hear")
		text = input()
		engine.say(text)
		engine.runAndWait()
	elif choice == "2":
		with sr.Microphone() as source:
			engine.say("Say lights on to turn on LED and lights of to turn off LED")
			engine.runAndWait()
			while True:
				audio = r.listen(source)
				try:
					voice = r.recognize_google(audio)
					if voice == "lights on":
						print ("The LED is on")
						arduino.write(b'H')
						engine.say("The light is on")
						engine.runAndWait()
					elif voice == "lights off":
						print ("The LED is off")
						arduino.write(b'L')
						engine.say("The light is off")
						engine.runAndWait()
					elif voice == "exit":
						break
					else:
						print ("Please try again")
				except:
					print("I can't understand")
	elif choice == "exit":
		break
	else:
		print("Please try again")