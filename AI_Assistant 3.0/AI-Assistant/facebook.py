import webbrowser

def open_facebook_page():
    try:
        # Attempt to open the URL in the default web browser
        webbrowser.open("https://web.facebook.com/")
        print("Webpage opened successfully.")
    except Exception as e:
        # Handle any exceptions that occur
        print(f"An error occurred: {e}")
    
    
