import os

def open_calculator():
    try:
        # Attempt to run the calculator
        result = os.system("calc")
        if result != 0:
            print("An error occurred while trying to open Calculator.")
    except Exception as e:
        print(f"An exception occurred: {e}")


