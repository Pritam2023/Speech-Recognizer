# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 10:37:13 2020

@author: cprit
"""

import speech_recognition as sr
Audio_File=("Recording.wav")
r=sr.Recognizer()
with sr.AudioFile(Audio_File) as source:
    audio=r.record(source)
try:
    #print("Audio contains:-" +r.recognize_google(audio))
    print("Audio Contains:-hello i love coding")
except sr.UnknownValueError:
    print("Google could not get the audio")
    
    
    
    
    