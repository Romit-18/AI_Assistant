import sys
import io
# Import the Translator class from googletrans library
from googletrans import Translator

def english_to_bengali(text):
    # Create an instance of Translator
    translator = Translator()

    # Translate the text from English to Bengali
    translation = translator.translate(text, dest='bn')

    # Return the translated text
    return translation.text

def save_to_file(text, filename):
    # Save the text to a file
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

