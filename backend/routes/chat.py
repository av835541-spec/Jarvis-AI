from flask import Blueprint, request, jsonify
from services.ai_service import generate_reply

chat = Blueprint("chat", __name__)

@chat.route("/chat", methods=["POST"])
def ai_chat():
    data = request.get_json()
    message = data.get("message", "")

    reply = generate_reply(message)

    return jsonify({
        "reply": reply
    })
