import yt_dlp
import os


def download_video(url, output_path="downloads/videos") -> dict:
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
            info = ydl.extract_info(url, download=True)
            metadata = extract_metadata(info)
            # Get the output file path
            filename = ydl.prepare_filename(info)
            return {"status": "success", "metadata": metadata, "filepath": filename}
        except Exception as e:
            return {"status": "error", "message": str(e)}


def extract_metadata(info: dict) -> dict:
    return {"title": info.get("title"), "description": info.get("description")}
