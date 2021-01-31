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
    tts = pyttsx3.init()
    tts.say(text)
    tts.runAndWait()

def speak(text):
    speak_pyttx(text)


def get_audio():
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recog.listen(source)
        text_listened = ""
        try:
            text_listened = recog.recognize_google(audio)
            print(text_listened)
        except:
            pass
    return text_listened.lower()
