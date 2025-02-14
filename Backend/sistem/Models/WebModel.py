from Backend import db
from datetime import datetime
class Web(db.Model):
    __tablename__ = 'web'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    descripcion =db.Column(db.String)
    dateCreate = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    # Relación con Usuario
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    usuario = db.relationship('Usuario', back_populates='webs')