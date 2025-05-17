import speech_recognition as sr
import pyttsx3
from fuzzywuzzy import fuzz
recognizer = sr.Recognizer()
engine=pyttsx3.init()

def assistant_wake_up():
    with sr.Microphone() as source:
        print("Listening for 'hey rio'...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print(f"Heard: {text}")
            ratio=fuzz.ratio ("hey rio",text.lower())
            print(f"ratio is:{ratio}")
            if ratio>61:
                print("Wake word detected!")
                text="Hi I am Rio"
                engine.say(text)
                engine.runAndWait()
                return True
            
            else:
                print("Wake word not detected.")
                return False
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the audio. Please try again.")
        except sr.RequestError as e:
            print(f"Could not request results; check your internet connection: {e}")

while True:
    if assistant_wake_up():
        break
