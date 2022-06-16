import urllib.request
import json
from attr import s
from gtts import gTTS
import os
from playsound import playsound
import sys
from lxml import html
import random
import webbrowser
import pywhatkit
from ayarlar import port
import speech_recognition as sr

from message import exitMessage,openMessage,helloMessage,timeMessage,todayMessage,jokes
from options import today,_time,r,nesil,sistem,port,islemci

class JesuCommands():
    
    def __init__(self,insound):
        self.sound = insound.lower()
        self.audioBlock = self.sound
        self.commands = ["merhaba","kapan","görüşürüz","git","gün","saat","google","işletim sistemi","işlemci","şaka","şarkı","wikipedia","ışık aç","ışık kapat"]
        
    def record(ask=False):
        with sr.Microphone() as source:
            audio = r.listen(source)
            voice = ""
            try:
                voice = r.recognize_google(audio, language="tr-TR")
            except:
                pass
                
            return voice
        
    
        
    def speak(self,string):
        tts = gTTS(text=string, lang="tr", slow=False)
        j = random.randint(1000,20000)
        file = "answer"+str(j)+".mp3"
        #file = "answer.mp3"
        tts.save(file)
        playsound(file)
        os.remove(file)
        
    def welcome(self):
        self.speak("Selam")
    
    def exit(self):
        self.speak(exitMessage)
        sys.exit()
    
    def jokes(self):
        self.speak(jokes)
    
    def google(self):
        self.speak("Ne aramamı istersin?")
        search = self.record()
        url = "https://www.google.com/search?q={}".format(search)
        webbrowser.get().open(url)
        self.speak("{} içi Google'da bulabildiklerimi listeliyorum.".format(search))
    
    def todays(self):
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
        self.speak(todayMessage + j)
        
    def times(self):
        self.speak(timeMessage + _time)
    
    def isletimsistem(self):
        self.speak("Mevcut işletim sistemin" + sistem)
    
    def islemci(self):
        self.speak(nesil + "nesil" + islemci + "ye sahipsin.")  
       
    def playSong(self):
        self.speak("Hangi şarkıyı çalmamı istersin.")
        song = self.record()
        self.speak("{} şarkısını oynatıyorum".format(song))
        pywhatkit.playonyt(song)


    def wikipedia(self):
        self.speak("Kimi aramamı istiyorsun")
        why = self.record()
        self.speak(f"İşte {why} için wikipedia da bulduklarım.")
        url = "https://tr.wikipedia.org/wiki/{}".format(why)
        webbrowser.get().open(url)



    #def openLight(self):
    #    self.speak('Işığı açıyorum')
    #    ser.write(b'H')
    #    self.speak("Işık başarıyla açıldı")

    #def closeLight(self):
    #    self.speak('Işığı kapatıyorum')
    #    ser.write(b'H')
    #    self.speak("Işık başarıyla kapatıldı")





    def commandFind(self):
        for command in self.commands:
            if command in self.sound:
                self.commandStart(command)
            
    def commandStart(self,command):
        if command == "merhaba":
            self.welcome()
            
        elif command == "kapan" or command == "git" or command == "görüşürüz":
            self.exit()
            
        elif command == "gün":
            self.todays()
            
        elif command == "saat":
            self.times()
            
        elif command == "google":
            self.google()
            
        elif command == "işletim sistemi":
            self.isletimsistem()
        
        elif command == "işlemci":
            self.islemci()
            
        elif command == "şaka":
            self.jokes()
            
        elif command == "şarkı":
            self.playSong()
            
        elif command == "wikipedia":
            self.wikipedia()
            
        elif command == "ışık aç":
            self.openLight()
            
        elif command == "ışık kapat":
            self.closeLight()