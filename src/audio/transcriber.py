import whisper

from ai.whisper import audio_to_text

model = whisper.load_model("medium")


def transcribe_audio(audio_path: str, output_path="files/transcriptions") -> str:
    """
    Transcribes audio from the given file path using Whisper model.

    Args:
        audio_path (str): Path to the audio file to be transcribed.

    Returns:
        str: Transcribed text from the audio.
    """
    result = audio_to_text(audio_path)
    return result
