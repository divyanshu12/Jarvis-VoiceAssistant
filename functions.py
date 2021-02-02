import datetime
from voiceCommand import speak, get_audio
import shutil

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")   
  
    else:
        speak("Good Evening Sir !")  
  
    assname =("Jarvis 1 point o")
    speak("I am your Assistant")
    speak(assname)
     
 
def user_name():
    speak("What should i call you sir")
    uname = get_audio()
    speak("Welcome Mister")
    speak(uname)
    print("Welcome Mr." + uname)
    speak("How can i Help you, Sir")
 