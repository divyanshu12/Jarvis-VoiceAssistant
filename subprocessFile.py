import subprocess
import datetime


def note(text):
    date = datetime.datetime.now()
    file_name = "data/Note_"+str(date).replace(":", "-") + ".txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])
