import speech_recognition as sr
from gtts import gTTS
import playsound
import pyttsx3


def speak_gtts(text):
    tts = gTTS(text=text, lang='en')
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

# 0 - Male voice
# 1 - Female voice
def speak_pyttx(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def speak(text):
    speak_pyttx(text)


def get_audio():
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        recog.pause_threshold = 1
        audio = recog.listen(source)
        text_listened = ""
        try:
            text_listened = recog.recognize_google(audio, language ='en-in')
            print(text_listened)
        except:
            pass
    return text_listened.lower()
