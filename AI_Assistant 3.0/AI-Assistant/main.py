import re
import os
os.environ['KMP_DUPLICATE_LIB_OK']='TRUE'
from record import record_voice
from camera import open_camera
from facebook import open_facebook_page
from alarm import open_alarm_app
from whatsapp import open_whatsapp_web
from audio_to_text import transcribe_audio_to_text
from word import open_word
from excel import open_excel
from calculator import open_calculator
from language import english_to_bengali,save_to_file
from chatgpt import open_chatgpt
from myinsta import open_myinsta_page
from linkedin import open_linkedin_page
from mylinkedin import open_mylinkedin_page
from my_assistant import assistant_wake_up


print("Recording started")
record_voice("my_voice.wav", duration=5)
print("Recording off")
transcribe=transcribe_audio_to_text("my_voice.wav")
transcribe=re.sub(r"[^a-zA-Z]+", "", transcribe).casefold()
print(transcribe)
if(transcribe.lower()=="opencamera"):
    open_camera()
elif(transcribe.lower()=="openfacebook"):
    open_facebook_page()
elif(transcribe.lower()=="openalarm"):
    open_alarm_app()
elif(transcribe.lower()=="openwhatsapp"):
    open_whatsapp_web()
elif(transcribe.lower()=="openwhatsapp"):
    open_chatgpt()
elif(transcribe.lower()=="openmicrosoftword"):
    open_word()
elif(transcribe.lower()=="openmicrosoftexcel"):
    open_excel() 
elif(transcribe.lower()=="openlinkedin"):
    open_linkedin_page() 
elif(transcribe.lower()=="openmylinkedinaccount"):
    open_mylinkedin_page() 
elif(transcribe.lower()=="openmyinstaaccount"):
    open_myinsta_page() 
elif(transcribe.lower()=="opencalculator"):
    open_calculator()   
elif(transcribe.lower()=="englishtobengali"):
    record_voice("my_voice.wav",duration=5)
    transcribe=transcribe_audio_to_text("my_voice.wav")
    bengali_translation=english_to_bengali(transcribe)
    print(bengali_translation)
    save_to_file(bengali_translation,"my_file.txt")

    