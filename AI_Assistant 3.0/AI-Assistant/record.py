import sounddevice as sd
from scipy.io.wavfile import write

def record_voice(filename="my_voice.wav", duration=5, samplerate=44100):
    """
    Records audio from the microphone and saves it as a WAV file.
    
    :param filename: Name of the output file (default: "output.wav").
    :param duration: Duration of the recording in seconds (default: 5 seconds).
    :param samplerate: Sampling rate in Hz (default: 44100 Hz).
    """
    try:
        print(f"Recording for {duration} seconds...")
        # Record audio
        audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2, dtype='int16')
        sd.wait()  # Wait for the recording to finish
        print("Recording complete. Saving the file...")
        
        # Save the audio data to a WAV file
        write(filename, samplerate, audio_data)
        print(f"Audio saved as {filename}.")
    except Exception as e:
        print(f"An error occurred: {e}")



