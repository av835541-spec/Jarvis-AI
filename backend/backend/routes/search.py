from flask import Blueprint, request, jsonify
from services.search import web_search

search = Blueprint("search", __name__)

@search.route("/search", methods=["POST"])
def search_api():
    data = request.get_json()
    query = data.get("query", "")

    return jsonify(web_search(query))
