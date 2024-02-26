import speech_recognition as sr

data=sr.Recognizer()
print("listening")

with sr.Microphone() as source:
    audio=sr.listen(source)
    query=sr.recognize_google(audio,language='eng-in')
    print(query)