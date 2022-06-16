from logging import critical
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import random
import psutil
from pynotifier import Notification

r = sr.Recognizer()
def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            print("[Asistan] : Dediğinizi Anlayamadım")
        except sr.RequestError:
            print("[Asistan] : Sistem çalışmıyor")
        return voice
    
def speak(string):
    tts = gTTS(text=string, lang="tr", slow=False)
    j = random.randint(1000,20000)
    file = "answer"+str(j)+".mp3"
    #file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)



