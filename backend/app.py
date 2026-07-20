from flask import Flask
from routes.chat import chat
from routes.youtube import youtube
from routes.seo import seo

app = Flask(__name__)

app.register_blueprint(chat)
app.register_blueprint(youtube)
app.register_blueprint(seo)

@app.route("/")
def home():
    return {
        "message": "Welcome to Jarvis AI",
        "version": "1.0.0",
        "status": "Running"
    }

if __name__ == "__main__":
    app.run(debug=True)
