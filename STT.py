import speech_recognition as sr
import json
from difflib import SequenceMatcher

def STT(filename):
    r = sr.Recognizer()

    file = sr.AudioFile(filename)
    with file as source:
        audio = r.record(source)
    output = r.recognize_google(audio)
    print(output)
    files = filename.split(".")
    target = files[0]
    target = target.replace("_", " ")
    target = target.lower()
    output = output.lower()
    if output in target:
        answer = {'Similarity': 100,
             'Spoken String': output}
    else:
        prob = SequenceMatcher(None, output, target).ratio() * 100
        answer = {'Similarity': prob,
                  'Spoken String': output}

    return json.dumps(answer)
