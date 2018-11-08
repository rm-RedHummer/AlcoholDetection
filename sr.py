import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    while True:
        print("talk")
    	audio = r.listen(source)
    	# recognize speech using Sphinx
    	try:
    	    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    	except:
    		print("I can't hear you")
