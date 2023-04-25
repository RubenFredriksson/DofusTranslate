import controller as c
import speech_recognition as sr
import tkinter as tk
import threading
from tkinter import messagebox

def listen(fromLanguage):

    # Convert the 'from' language into the correct format
    fromLanguage = c.languageToBCP47(fromLanguage)

    # Create a recognizer object
    r = sr.Recognizer()

    # Create a warning message to let the user know that their voice will be recorded after pressing OK
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Warning", "Your voice will be recorded after you press OK.")
    root.destroy()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        # Adjust ambient noise levels
        r.adjust_for_ambient_noise(source)

        # Record audio from the microphone
        audio = r.listen(source)

        # Use Google's speech recognition API to convert speech to text
        try:
            return r.recognize_google(audio, language=fromLanguage)
        except sr.UnknownValueError:
            return "Could not understand Audio."
        except sr.RequestError as e:
            return "Could not connect to Speech Recognition service"
        
def listenAsync(fromLanguage, callback):
    def run():
        text = listen(fromLanguage)
        callback(text)

    threading.Thread(target=run).start()