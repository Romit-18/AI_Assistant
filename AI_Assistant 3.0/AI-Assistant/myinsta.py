import webbrowser

def open_myinsta_page():
    try:
        # Atmpt to open the URL in the default web browser
        webbrowser.open("https://www.instagram.com/grow_teen/")
        print("Webpage opened successfully.")
    except Exception as e:
        # Handle any exceptions that occur
        print(f"An error occurred: {e}")
