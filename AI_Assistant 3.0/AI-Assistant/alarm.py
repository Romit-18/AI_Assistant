import os

def open_alarm_app():
    try:
        os.system("start ms-clock:")
        
    except Exception as e:
        print(f"An error occurred: {e}")


