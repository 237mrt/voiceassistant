import time
from datetime import date, datetime
import speech_recognition as sr
import serial
import platform
from ayarlar import port

today = time.strftime("%A")
_time = datetime.now().strftime("%H:%M")
r = sr.Recognizer()
sistem = platform.system()
nesil = platform.release()
islemci = platform.processor()
#ser = serial.Serial(port, 9600)
