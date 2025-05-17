import webbrowser

def open_mylinkedin_page():
    try:
        # Atmpt to open the URL in the default web browser
        webbrowser.open("https://www.linkedin.com/in/romit-pal-3001a4217/")
        print("Webpage opened successfully.")
    except Exception as e:
        # Handle any exceptions that occur
        print(f"An error occurred: {e}")
