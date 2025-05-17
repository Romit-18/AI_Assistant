# import webbrowser

# try:
#     # Attempt to open the URL in the default web browser
#     webbrowser.open("https://web.whatsapp.com/")
#     print("Webpage opened successfully.")
# except Exception as e:
#     # Handle any exceptions that occur
#     print(f"An error occurred: {e}")

import webbrowser

def open_whatsapp_web():
    try:
        # Attempt to open the URL in the default web browser
        webbrowser.open("https://web.whatsapp.com/")
        print("Webpage opened successfully.")
    except Exception as e:
        # Handle any exceptions that occur
        print(f"An error occurred: {e}")


