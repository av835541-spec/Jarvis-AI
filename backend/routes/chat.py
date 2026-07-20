from flask import Blueprint, request, jsonify

chat = Blueprint("chat", __name__)

@chat.route("/chat", methods=["POST"])
def ai_chat():
    data = request.get_json()
    message = data.get("message", "")

    return jsonify({
        "reply": f"Jarvis AI received: {message}"
    })
