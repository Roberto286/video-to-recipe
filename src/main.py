from flask import Flask, request, jsonify
from flask_cors import CORS

from video.downloader import download_video
from video.processor import extract_audio_from_video

app = Flask(__name__)


@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"message": "pong"}), 200


@app.route("/recipe", methods=["POST"])
def recipe():
    data = request.get_json()
    recipe_url = data.get("url")
    if not recipe_url:
        return jsonify({"error": "URL is required"}), 400
    info = download_video(recipe_url)
    metadata, filepath = info["metadata"], info["filepath"]
    title, description = metadata["title"], metadata["description"]
    extract_audio_from_video(filepath)
    return jsonify(
        {
            "message": "Url received",
            "title": title,
            "description": description,
            "filepath": filepath,
        }
    ), 200


if __name__ == "__main__":
    CORS(app)  # Enable CORS for all routes
    app.run(port="8000")
