from cProfile import run
from email.quoprimime import quote
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import date, datetime
import random
from pydub import AudioSegment
import webbrowser
import platform
import requests
from googletrans import Translator
import serial
from message import exitMessage,openMessage,helloMessage,timeMessage,todayMessage,jokes
from ayarlar import port

# Options
ser = serial.Serial(port, 9600)

r = sr.Recognizer()
today = time.strftime("%A")
_time = datetime.now().strftime("%H:%M")
today.capitalize()

# Options End

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

def response(voice):
    if "merhaba" in voice:
        speak(helloMessage)
    
    elif "kapan" in voice or "görüşürüz" in voice or "baybay" in voice:
        speak(exitMessage)
        exit()

    elif "gün" in voice or "hangi gündeyiz" in voice or "bugün ne" in voice:
        if today == "Monday":
            print("Pazartesi")
            j = "Pazartesi"
        elif today == "Tuesday":
            print("Salı")
            j = "Salı"
        elif today == "Wednesday":
            print("Çarşamba")
            j = "Çarşamba"
        elif today == "Thursday":
            print("Perşembe")
            j = "Perşembe"
        elif today == "Friday":
            print("Cuma")
            j = "Cuma"
        elif today == "Saturday":
            print("Cumartesi")
            j = "Cumartesi"
        elif today == "Sunday":
            print("Pazar")
            j = "Pazar"
        speak(todayMessage + j)
        
    elif "saat" in voice or "saat kaç" in voice or "saati söylermisin" in voice or "saati söyle" in voice:
        speak(timeMessage + _time)
      
    elif "araştır" in voice or "google da ara" in voice:
        speak("Ne aramamı istersin?")
        search = record()
        url = "https://www.google.com/search?q={}".format(search)
        webbrowser.get().open(url)
        speak("{} içi Google'da bulabildiklerimi listeliyorum.".format(search))
    
    elif "işletim sistemi" in voice:
        sistem = platform.system()
        speak("Mevcut işletim sistemin" + sistem)
        
    elif "işlemci" in voice:
        islemci = platform.processor()
        nesil = platform.release()
        speak(nesil + "nesil" + islemci + "ye sahipsin.") 
    
    elif "şaka" in voice or "şaka yap" in voice or "güldür" in voice:
        speak(jokes) 
    
    elif "ışığı aç" in voice or "ışıkları aç" in voice or "ışıklar" in voice:
        speak('Işığı açıyorum')
        ser.write(b'H')
        speak("Işık başarıyla açıldı")
    
    elif "ışığı kapat" in voice:
        speak("Işığı kapatıyorum")
        ser.write(b'L')
        speak("Işığı kapattım")
    
def speak(string):
    tts = gTTS(text=string, lang="tr", slow=False)
    j = random.randint(1000,20000)
    file = "answer"+str(j)+".mp3"
    #file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

def test(wake):
    if "jesus" in wake or "hey jesus" in wake or "hey" in wake:
        speak("Dinliyorum")
        wake = record()
        if wake != '':
            voice = wake.lower()
            print(wake.capitalize())
            response(voice)

speak(openMessage)

while True:
    wake = record()
    if wake != '':
        wake = wake.lower()
        print(wake.capitalize())
        test(wake)
        