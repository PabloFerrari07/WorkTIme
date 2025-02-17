
from sistem.Models.WebModel import WebModel
from sistem import db
from flask import Flask, Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
web_bp = Blueprint("web", __name__)
#Metodo para CARGAR datos de la web
@web_bp.route("/web/post", methods=["POST"])
@jwt_required()  # 🔐 Requiere autenticación con JWT
def post():
    user_id = get_jwt_identity()  # Obtiene el ID del usuario autenticado

    data = request.get_json()  # Obtener los datos enviados en la petición
    web = WebModel(
        name=data["name"],
        url=data["url"],
        description=data["description"],
        category=data["category"],
        dateCreated=data["dateCreated"],
        user_id=user_id  # Asigna el ID del usuario autenticado
    )

    db.session.add(web)
    db.session.commit()
    
    return jsonify({"message": "Web data created successfully"}), 201


#Metodo para OBTENER datos de la web

@web_bp.route("/webs", methods=["GET"])
@jwt_required()
def get_webs():
    user_id = get_jwt_identity()
    webs = WebModel.query.filter_by(user_id=user_id).all()
    
    webs_list = [{"id": web.id, "name": web.name, "url": web.url, "description": web.description, "category": web.category, "dateCreated": web.dateCreated} for web in webs]

    return jsonify(webs_list), 200

#Metodo para ACTUALIZAR datos de la web

@web_bp.route("/web/put/<int:id>", methods=["PUT"])
@jwt_required()
def put(id):
    web = WebModel.query.get(id)

    user_id = get_jwt_identity()

    if not web:
        return jsonify({"message": "Web data not found"}), 404
    
    data = request.get_json()
    web.name = data["name"]
    web.url = data["url"]
    web.description = data["description"]
    web.category = data["category"]
    web.dateCreated = data["dateCreated"]
    
    db.session.commit()

    
    return jsonify({"message": "Web data updated successfully"}), 200

#Metodo para ELIMINAR datos de la web

@web_bp.route("/web/delete/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    user_id = get_jwt_identity()
    web = WebModel.query.get(id)
    
    if not web:
        return jsonify({"message": "Web data not found"}), 404
    
    db.session.delete(web)
    db.session.commit()

    return jsonify({"message": "Web data deleted successfully"}), 200