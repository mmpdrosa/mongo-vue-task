# routes.py
from bson import ObjectId
from flask import Blueprint, jsonify, request

from .models import Video, mongo

api = Blueprint("api", __name__)


@api.route("/videos", methods=["GET"])
def get_videos():
    videos = mongo.db.videos.find()
    results = []
    for video in videos:
        results.append(
            {
                "id": str(video["_id"]),
                "name": video["name"],
                "url": video["url"],
                "theme": video["theme"],
                "thumbs_up": video["thumbs_up"],
                "thumbs_down": video["thumbs_down"],
            }
        )
    return jsonify(results)


@api.route("/videos", methods=["POST"])
def add_video():
    data = request.get_json()
    new_video = Video(name=data["name"], url=data["url"], theme=data["theme"])
    mongo.db.videos.insert_one(new_video.json())
    return jsonify({"message": "Video added successfully"})


@api.route("/videos/<string:video_id>/thumbs-up", methods=["PUT"])
def thumbs_up(video_id):
    try:
        video_id = ObjectId(video_id)
        mongo.db.videos.update_one({"_id": video_id}, {"$inc": {"thumbs_up": 1}})
        return jsonify({"message": "Thumbs up added successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@api.route("/videos/<string:video_id>/thumbs-down", methods=["PUT"])
def thumbs_down(video_id):
    try:
        video_id = ObjectId(video_id)
        mongo.db.videos.update_one({"_id": video_id}, {"$inc": {"thumbs_down": 1}})
        return jsonify({"message": "Thumbs down added successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@api.route("/themes", methods=["GET"])
def get_themes():
    themes = mongo.db.videos.distinct("theme")
    theme_scores = {}

    for theme in themes:
        videos = mongo.db.videos.find({"theme": theme})
        score = sum(video["thumbs_up"] - (video["thumbs_down"] / 2) for video in videos)
        theme_scores[theme] = score

    # Sort themes by score in descending order
    sorted_themes = sorted(theme_scores.items(), key=lambda x: x[1], reverse=True)

    return jsonify({"themes": sorted_themes})
