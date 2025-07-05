from flask import Flask, request, jsonify
from flask_cors import CORS

from src.video.downloader import download_video

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
    download_video(recipe_url)
    return jsonify({"message": "Url received", "url": recipe_url}), 200


if __name__ == "__main__":
    CORS(app)  # Enable CORS for all routes
    app.run(port="8000")
