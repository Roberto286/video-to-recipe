from moviepy import VideoFileClip
import os
from pathlib import Path


def extract_audio_from_video(video_path: str, output_path="downloads/audios") -> str:
    """
    Extracts audio from a video file and saves it to the specified output path.

    Args:
        video_path (str): Path to the input video file.
        output_path (str): Path where the extracted audio will be saved.

    Returns:
        str: Path to the saved audio file.
    """

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Load the video file
    video = VideoFileClip(video_path)

    # Extract audio
    audio = video.audio

    # Save the audio file
    audio_file_path = f"{output_path}/{Path(video_path).stem}.mp3"
    audio.write_audiofile(audio_file_path)

    # Close the video and audio objects
    video.close()
    audio.close()

    return audio_file_path
