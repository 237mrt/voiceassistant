import time
from datetime import date, datetime
import webbrowser
import platform
from googletrans import Translator
import serial
import pywhatkit
from message import exitMessage,openMessage,helloMessage,timeMessage,todayMessage,jokes
from ayarlar import port
from system import record,speak


# Options
#ser = serial.Serial(port, 9600)
today = time.strftime("%A")
_time = datetime.now().strftime("%H:%M")
today.capitalize()
# Options End

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
    
    elif "oynat" in voice or "çal" in voice or "şarkı çal" in voice:
        speak("Hangi şarkıyı çalmamı istersin.")
        song = record()
        speak("{} şarkısını oynatıyorum".format(song))
        pywhatkit.playonyt(song)
        
    elif "wikipedia" in voice:
        speak("Kimi aramamı istiyorsun")
        why = record()
        speak(f"İşte {why} için wikipedia da bulduklarım.")
        url = "https://tr.wikipedia.org/wiki/{}".format(why)
        webbrowser.get().open(url)
    #elif "ışığı aç" in voice or "ışıkları aç" in voice or "ışıklar" in voice:
    #    speak('Işığı açıyorum')
    #    ser.write(b'H')
    #    speak("Işık başarıyla açıldı")
    #
    #elif "ışığı kapat" in voice:
    #    speak("Işığı kapatıyorum")
    #    ser.write(b'L')
    #    speak("Işığı kapattım")

    
    
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


