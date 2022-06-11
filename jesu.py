from cProfile import run
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import date, datetime
import random
from random import choice
from pydub import AudioSegment
import webbrowser

r = sr.Recognizer()
today = time.strftime("%A")
_time = datetime.now().strftime("%H:%M")
today.capitalize()
exitMessage = ["Görüşürüz", "Kendine iyi bak", "Elveda", "Kapandım"]
exitMessage = random.choice(exitMessage)
helloMessage = ["Selam", "Hoşgeldin", "Merhaba", "Sanada Merhaba"]
helloMessage = random.choice(helloMessage)
timeMessage = ["Saat şuan", "Saati söylüyorum", "Saat", "Hemen bakıyorum saat"]
timeMessage = random.choice(timeMessage)
todayMessage = ["Bugün günlerden", "Bugün", "Günlerden"]
todayMessage = random.choice(todayMessage)

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
    
    if "kapan" in voice or "görüşürüz" in voice or "baybay" in voice:
        speak(exitMessage)
        exit()

    if "gün" in voice or "hangi gündeyiz" in voice or "bugün ne" in voice:
        if today == "Monday":
            print("Pazartesi")
            t = "Pazartesi"
        elif today == "Tuesday":
            print("Salı")
            t = "Salı"
        elif today == "Wednesday":
            print("Çarşamba")
            t = "Çarşamba"
        elif today == "Thursday":
            print("Perşembe")
            t = "Perşembe"
        elif today == "Friday":
            print("Cuma")
            t = "Cuma"
        elif today == "Saturday":
            print("Cumartesi")
            t = "Cumartesi"
        elif today == "Sunday":
            print("Pazar")
            t = "Pazar"

        speak(todayMessage + t)
    if "saat" in voice or "saat kaç" in voice or "saati söylermisin" in voice or "saati söyle" in voice:
        speak(timeMessage + _time)
      
    if "araştır" in voice or "google da ara":
        speak("Ne aramamı istersin?")
        search = record()
        url = "https://www.google.com/search?q={}".format(search)
        webbrowser.get().open(url)
        speak("{} içi Google'da bulabildiklerimi listeliyorum.".format(search))
    
    
def speak(string):
    tts = gTTS(text=string, lang="tr", slow=False)
    j = random.randint(1,100)
    file = "answer"+str(j)+".mp3"
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


speak("Selam Kullanıcı")

while True:
    wake = record()
    if wake != '':
        wake = wake.lower()
        print(wake.capitalize())
        test(wake)