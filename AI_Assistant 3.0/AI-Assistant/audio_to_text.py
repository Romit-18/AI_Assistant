from faster_whisper import WhisperModel

def transcribe_audio_to_text(file_path: str, model_size: str = "small") -> str:
    """
    Transcribes an audio file into text using the Faster Whisper library.

    Parameters:
    - file_path (str): Path to the audio file to be transcribed.
    - model_size (str): The size of the Whisper model to use. Defaults to 'small'.

    Returns:
    - str: The transcribed text from the audio file.
    """
    # Load the Whisper model
    model = WhisperModel(model_size)
    
    # Transcribe the audio file
    segments, info = model.transcribe(file_path)
    
    # Combine all transcriptions into a single string
    transcription = " ".join(segment.text for segment in segments)
    
    return transcription
