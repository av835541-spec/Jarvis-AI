from flask import Blueprint, jsonify

youtube = Blueprint("youtube", __name__)

@youtube.route("/youtube/status", methods=["GET"])
def status():
    return jsonify({
        "service": "YouTube Manager",
        "status": "Running"
    })
