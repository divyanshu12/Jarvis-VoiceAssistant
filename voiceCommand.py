import speech_recognition as sr
from gtts import gTTS
import playsound
import pyttsx3


def speak_gtts(text):
    tts = gTTS(text=text, lang='en')
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def speak_pyttx(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def speak(text):
    speak_pyttx(text)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except:
            pass
    return said.lower()
