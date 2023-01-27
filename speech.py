import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    print("Say something: ")
    audio = r.listen(source)

    text = r.recognize_google(audio)
    print("You said: {}".format(text))
