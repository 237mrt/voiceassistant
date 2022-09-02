from distutils.cmd import Command
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

from message import spotifyMessage,closeLightMessage,openLightMessage,wikiMessage,exitMessage,songPlayMessage,uJokeMessage,whatTimeMessage,searchMessage,timeMessage,todayMessage,jokes,shutDownMessage,dayMessage
from options import today,_time,r,nesil,sistem,port,islemci,ser

class JesuCommands():
    
    def __init__(self,insound):
        self.sound = insound.lower()
        self.audioBlock = self.sound
        
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
       
    def playSongs(self):
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



    def openLight(self):
        self.speak('Işığı açıyorum')
        ser.write(b'H')
        self.speak("Işık başarıyla açıldı")

    def closeLight(self):
        self.speak('Işığı kapatıyorum')
        ser.write(b'H')
        self.speak("Işık başarıyla kapatıldı")


   


    # Command Create
    def shutDown(self):
        for kapan in shutDownMessage:
            if kapan in self.sound:
                self.exit()
                
    def today(self):
        for gün in dayMessage:
            if gün in self.sound:
                self.todays()

    def whatTime(self):
        for saat in whatTimeMessage:
            if saat in self.sound:
                self.times()
    
    def searchGoogle(self):
        for ara in searchMessage:
            if ara in self.sound:
                self.google()
    
    def uJokes(self):
        for saka in uJokeMessage:
            if saka in self.sound:
                self.jokes()
                
    def playSong(self):
        for sarki in songPlayMessage:
            if sarki in self.sound:
                self.playSongs()
    
    def wiki(self):
        for wiki in wikiMessage:
            if wiki in self.sound:
                self.wikipedia()
    
   
    
    def openLights(self):
        for isikac in openLightMessage:
            if isikac in self.sound:
                self.openLight()

    def closeLights(self):
        for isikkap in closeLightMessage:
            if isikkap in self.sound:
                self.closeLight()
       
        
        
    # Start Commands 
    def commandFind(self):
        self.shutDown() # Sistemi kapatır
        self.today()    # Hangi günde oldugumuzu söyler
        self.whatTime() # Saatin kaç olduğunu söyler
        self.searchGoogle() # Google da arama yapar
        self.uJokes() # Şaka yapar
        self.playSong() # İstediğiniz şarkıyı oynatır
        self.wiki # Wikipedia da arama yapar
        #self.openLights() # Au sisteminize bağlı ışıkları açar
        #self.closeLights() # Au sisteminize bağlı ışıkları kapar
        
            
       