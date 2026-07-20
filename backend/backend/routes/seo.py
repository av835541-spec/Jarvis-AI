from flask import Blueprint, request, jsonify
from services.seo import generate_seo

seo = Blueprint("seo", __name__)

@seo.route("/seo", methods=["POST"])
def seo_generator():
    data = request.get_json()
    title = data.get("title", "")

    return jsonify(generate_seo(title))
