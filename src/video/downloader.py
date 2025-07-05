import yt_dlp
import os


def download_video(url, output_path="downloads") -> dict:
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    ydl_opts = {
        "format": "best",
        "outtmpl": os.path.join(output_path, "%(id)s.%(ext)s"),
        "noplaylist": True,
        "quiet": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            info = ydl.extract_info(url, download=False)
            metadata = extract_metadata(info)

            return {"status": "success", "metadata": metadata}
        except Exception as e:
            return {"status": "error", "message": str(e)}


def extract_metadata(info: dict) -> dict:
    return {"title": info.get("title"), "description": info.get("description")}
