import speech_recognition as sr
import json

def STT(filename):
    r = sr.Recognizer()

    file = sr.AudioFile(filename)
    with file as source:
        audio = r.record(source)
    output = r.recognize_google(audio)
    print(output)
    return json.dumps(output)
