from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('db.DevelopmentConfig')

db = SQLAlchemy(app)

# Crear el contexto de la aplicación antes de ejecutar db.create_all()
with app.app_context():
    db.create_all()
