from subprocessFile import note
from calanderFile import get_date, authenticate_google, get_calendar_event
from voiceCommand import get_audio, speak
from time import ctime

wakeup = "Jarvis"
auth = authenticate_google()
print("Start......")

while True:
    print("Listening..")
    text = get_audio()
    print("You : ", text)
    if text.count(wakeup.lower()) > 0:

        TIME_PHRASES = ["what time is it", "what is the time"]
        for phrase in TIME_PHRASES:
            if phrase in text:
                speak(ctime())

        CALENDAR_PHRASES = ["what do i have", "do i have plans", "am i busy"]
        for phrase in CALENDAR_PHRASES:
            if phrase in text:
                date = get_date(text)
                if date:
                    get_calendar_event(date, auth)
                else:
                    speak("I don't understand")

        NOTE_PHRASES = ["make a note", "write this down",
                      "type this", "create note"]
        for phrase in NOTE_PHRASES:
            if phrase in text:
                speak("What would you like me to write down? ")
                write_down = get_audio()
                note(write_down)
                speak("I've made a note of that.")

        if "help" in text:
            speak("I can help you with google events, making notes and current time")

        elif "good morning" in text:
            speak("Good Morning Sir")

        elif "how are you" in text:
            speak("I am fine")

        else:
            speak("I don't understand")

         