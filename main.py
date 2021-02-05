from subprocessFile import note
from calanderFile import get_date, authenticate_google, get_calendar_event
from voiceCommand import get_audio, speak
from functions import wish_me, user_name
from time import ctime
import wikipedia

wakeup = "Jarvis"
auth = authenticate_google()
print("Start......")

wish_me()
user_name()

result_found = 0
while True:
    print("Listening..")
    query = get_audio()
    print("You : ", query)
    if len(query) > 1:
        result_found = 0
        TIME_PHRASES = ["what time is it", "what is the time"]
        for phrase in TIME_PHRASES:
            if phrase in query:
                result_found = 1
                speak(ctime())

        CALENDAR_PHRASES = ["what do i have", "do i have plans", "am i busy"]
        for phrase in CALENDAR_PHRASES:
            if phrase in query:
                result_found = 1
                date = get_date(query)
                if date:
                    get_calendar_event(date, auth)
                else:
                    speak("I don't understand")

        NOTE_PHRASES = ["make a note", "write this down",
                      "type this", "create note"]
        for phrase in NOTE_PHRASES:
            if phrase in query:
                result_found = 1
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
            query = query[query.find("wikipedia")+10: ]
            query = query.replace("for", "").replace("about", "")
            try:
                results = wikipedia.summary(query, sentences = 3)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except:
                speak("No result found.")

        elif "bye" in query:
            speak("Good Bye, Sir")
            break

        else:
            if (result_found == 0):
                speak("I don't understand")

         