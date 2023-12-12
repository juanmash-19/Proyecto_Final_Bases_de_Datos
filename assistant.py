#en el archivo assistant.py hay esto:
import speech_recognition as sr
import pygame
from gtts import gTTS
import os

def speak(message):
    tts = gTTS(text=message, lang="es", slow=False)
    filename = os.path.join(os.path.dirname(__file__), "voice.mp3")
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.quit()
    os.remove(filename)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        beep()
        audio = r.listen(source, timeout=20)
        said = ""

        try:
            # recognize_bing()
            # recognize_google_cloud()
            # recognize_ibm()
            said = r.recognize_google(audio, language='es-ES')
        except Exception as e:
            print("Exception: "+ str(e))
    return said

def beep():
    filename = os.path.join(os.path.dirname(__file__), "beep.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.quit()