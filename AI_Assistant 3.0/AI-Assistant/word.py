import os
def open_word():
    try:

        os.system("start winword")
        print("Microsoft Word Has been opened")
    except Exception as e:
        print(f"An error occured: {e}")


    