import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=5)
    while True:
        print("talk")
        audio = r.listen(source)
        # recognize speech using Sphinx
        try:
            print("Sphinx thinks you said " + r.recognize_google(audio,  key="GOOGLE_SPEECH_RECOGNITION_API_KEY"))
        except:
            print("I can't understand you")