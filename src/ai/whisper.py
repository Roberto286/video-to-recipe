import whisper

model = whisper.load_model("medium")


def audio_to_text(audio_path: str) -> str:
    """
    Transcribes audio from the given file path using Whisper model.

    Args:
        audio_path (str): Path to the audio file to be transcribed.

    Returns:
        str: Transcribed text from the audio.
    """
    result = model.transcribe(audio_path)
    return result["text"]
