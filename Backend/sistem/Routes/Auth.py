from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from sistem.Models.UserModel import UserModel
from sistem import db
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__)

#registrar usuario

@auth_bp.route("/register", methods=["POST"])
def register():
    if request.method == "POST":
        data = request.get_json() #obtener datos del usuario
        hashed_password = generate_password_hash(data["password"], method="pbkdf2:sha256")

        new_user = UserModel(
            username=data["name"],
            email=data["email"],
            phone=data["phone"],
            password=hashed_password
        )
        db.session.add(new_user) #agregar usuario a la base de datos
        db.session.commit() #guardar cambios
        return jsonify({"message": "User created successfully"}), 200 #respuesta exitosa
    
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json() #obtener datos del usuario
    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"message": "Email and password are required"}), 400
    
    #buscar usuario en la base de datos
    user = UserModel.query.filter_by(email=data["email"]).first()
    if not user or not check_password_hash(user.password, data["password"]):
        return jsonify({"message": "Invalid credentials"}), 401
    
    #generar token

    access_token = create_access_token(identity=user.id)

    return jsonify({"access_token": access_token}), 200


