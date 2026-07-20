from flask import Flask
from routes.chat import chat

app = Flask(__name__)

app.register_blueprint(chat)

@app.route("/")
def home():
    return {
        "message": "Welcome to Jarvis AI"
    }

if __name__ == "__main__":
    app.run(debug=True)
