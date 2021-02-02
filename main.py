from subprocessFile import note
from calanderFile import get_date, authenticate_google, get_calendar_event
from voiceCommand import get_audio, speak
from functions import wish_me, user_name
from time import ctime

wakeup = "Jarvis"
auth = authenticate_google()
print("Start......")

wish_me()
user_name()

while True:
    print("Listening..")
    query = get_audio()
    print("You : ", query)
    if query.count(wakeup.lower()) > 0:

        TIME_PHRASES = ["what time is it", "what is the time"]
        for phrase in TIME_PHRASES:
            if phrase in query:
                speak(ctime())

        CALENDAR_PHRASES = ["what do i have", "do i have plans", "am i busy"]
        for phrase in CALENDAR_PHRASES:
            if phrase in query:
                date = get_date(query)
                if date:
                    get_calendar_event(date, auth)
                else:
                    speak("I don't understand")

        NOTE_PHRASES = ["make a note", "write this down",
                      "type this", "create note"]
        for phrase in NOTE_PHRASES:
            if phrase in query:
                speak("What would you like me to write down? ")
                write_down = get_audio()
                note(write_down)
                speak("I've made a note of that.")

        if "help" in query:
            speak("I can help you with google events, making notes and current time")

        elif "good morning" in query:
            speak("Good Morning Sir")

        elif "how are you" in query:
            speak("I am fine")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        else:
            speak("I don't understand")

         