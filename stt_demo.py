#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
 
import speech_recognition as sr
#import os
 
# Record Audio
r = sr.Recognizer()
mic=sr.Microphone()

with mic  as source:
    print("Say something!")
    audio = r.listen(source)
 
# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("You said: " + r.recognize_google(audio))
    #text = r.recognize_google(audio)
    #os.system(text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
