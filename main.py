from subprocessFile import note
from calanderFile import get_date, authenticate_google, get_calendar_event
from voiceCommand import get_audio, speak_gtts, speak_pyttx


wakeup = "Hey buddy"
service = authenticate_google()
print("Start......")

while True:
    print("Listening")
    text = get_audio()
    if text.count(wakeup) > 0:
        speak_pyttx("hi, how can i help you ?")
        text = get_audio()
        print("You : ", text)

        CALENDAR_STRS = ["what do i have", "do i have plans", "am i busy"]
        for phrase in CALENDAR_STRS:
            if phrase in text:
                date = get_date(text)
                if date:
                    get_calendar_event(date, service)
                else:
                    speak_pyttx("Please try again")

        NOTE_STRS = ["make a note", "write this down",
                      "type this", "create note"]
        for phrase in NOTE_STRS:
            if phrase in text:
                speak_pyttx("What would you like me to write down? ")
                write_down = get_audio()
                note(write_down)
                speak_pyttx("I've made a note of that.")
