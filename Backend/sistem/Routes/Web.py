
from sistem.Models.WebModel import WebModel
from sistem import db
from flask import Flask, Blueprint, jsonify, request

web_bp = Blueprint("web", __name__)

@web_bp.route("/web/post", methods=["POST"])

def post():
    data = request.get_json() # obtener datos de la web
    web = WebModel(
        name=data["name"],
        url=data["url"],
        description=data["description"],
        category=data["category"],
        dateCreated=data["dateCreated"]
    )

    db.session.add(web)
    db.session.commit()
    return jsonify({"message": "Data created"}), 200
