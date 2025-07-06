from ai.mistral import improve_transcription


def correct_transcription(transcription: str) -> str:
    result = improve_transcription(transcription)
    return result
