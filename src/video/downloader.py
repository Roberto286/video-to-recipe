import yt_dlp
import os


def download_video(url, output_path="downloads"):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    ydl_opts = {
        "format": "best",
        "outtmpl": os.path.join(output_path, "%(title)s.%(ext)s"),
        "noplaylist": True,
        "quiet": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            return {"status": "success", "message": "Video downloaded successfully"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
