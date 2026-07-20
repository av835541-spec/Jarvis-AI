from flask import Blueprint, request, jsonify
from services.ai_service import generate_reply
from services.memory import save_message

chat = Blueprint("chat", __name__)

@chat.route("/chat", methods=["POST"])
def ai_chat():
    data = request.get_json()
    message = data.get("message", "")

    save_message(message)

    reply = generate_reply(message)

    return jsonify({
        "reply": reply
    })
