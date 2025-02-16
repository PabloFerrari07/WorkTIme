from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('db.DevelopmentConfig')

db = SQLAlchemy(app)

#importar rutas
from sistem.Routes.Auth import auth_bp
app.register_blueprint(auth_bp)

# Crear el contexto de la aplicación antes de ejecutar db.create_all()
with app.app_context():
    db.create_all()
