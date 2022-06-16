import time
from commands import JesuCommands
import speech_recognition as sr
from options import r


while True:
    
    with sr.Microphone() as source:
        print("Birşeyler söyle")
        audio = r.listen(source)

    voice = ""
    
    try:
        voice = r.recognize_google(audio, language="tr-TR")
        print(voice)
        command = JesuCommands(voice)
        command.commandFind()
        time.sleep(1)
    except sr.UnknownValueError:
        print("[Asistan] : Dediğinizi Anlayamadım")
    except sr.RequestError:
        print("[Asistan] : Sistem çalışmıyor")
    
    



