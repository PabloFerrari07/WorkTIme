# archivo init.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import os
app = Flask(__name__)
app.config.from_object('db.DevelopmentConfig')
app.config["JWT_SECRET_KEY"] = "super-secret"  # clave secreta para el token
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwtsecretkey")  # Necesario para JWT
# Inicializar JWTManager con la app
jwt = JWTManager(app)

db = SQLAlchemy(app)

# importar rutas
from sistem.Routes.Auth import auth_bp
app.register_blueprint(auth_bp)

from sistem.Routes.Web import web_bp
app.register_blueprint(web_bp)
# Crear el contexto de la aplicación antes de ejecutar db.create_all()
with app.app_context():
    db.create_all()
