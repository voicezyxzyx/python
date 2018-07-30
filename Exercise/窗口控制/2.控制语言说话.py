import win32com.client
import time
dehua = win32com.client.Dispatch("SAPI.SPVOICE")

while True:
    time.sleep(1)
    dehua.Speak("sunck is a good man")