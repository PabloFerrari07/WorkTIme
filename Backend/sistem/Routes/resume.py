from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from sistem import db
from sistem.Models.CurriculumModel import CurriculumModel

curriculum_bp = Blueprint("curriculum", __name__)  # 🔹 Blueprint para rutas relacionadas con CVs


@curriculum_bp.route("/curriculum/post", methods=["POST"])
@jwt_required()  # 🔐 Requiere autenticación con JWT

def post():
    user_id = get_jwt_identity()
    data = request.get_json()

    curriculum = CurriculumModel(
        name=data["name"],
        description=data["description"],
        archive=data["archive"],
        user_id=user_id
    )

    db.session.add(curriculum)

    db.session.commit()
    return jsonify({"message": "Curriculum data created successfully"}), 201


@curriculum_bp.route("/curriculums", methods=["GET"])
@jwt_required()
def get():
    user_id = get_jwt_identity()
    curriculums = CurriculumModel.query.filter_by(user_id=user_id).all()

    curriculums_list = [{"id": curriculum.id, "name": curriculum.name, "description": curriculum.description, "archive": curriculum.archive} for curriculum in curriculums]

    return jsonify(curriculums_list), 200


@curriculum_bp.route("/curriculum/put/<int:id>", methods=["PUT"])
@jwt_required()

def put(id):
    user_id = get_jwt_identity()
    curriculum = CurriculumModel.query.get(id)

    if not curriculum:
        return jsonify({"message": "Curriculum data not found"}), 404
    
    data = request.get_json()

    curriculum.name = data["name"]
    curriculum.description = data["description"]
    curriculum.archive = data["archive"]

    db.session.commit()
    return jsonify({"message": "Curriculum data updated successfully"}), 200

@curriculum_bp.route("/curriculum/delete/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    user_id = get_jwt_identity()
    curriculum = CurriculumModel.query.get(id)

    if not curriculum:
        return jsonify({"message": "Curriculum data not found"}), 404

    db.session.delete(curriculum)
    db.session.commit()
    return jsonify({"message": "Curriculum data deleted successfully"}), 200