import os
def open_excel():
    try:

        os.system("start excel")
        print("Microsoft Excel Has been opened")
    except Exception as e:
        print(f"An error occured: {e}")
