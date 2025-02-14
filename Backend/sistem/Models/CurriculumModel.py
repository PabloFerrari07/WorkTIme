from Backend import db
from datetime import datetime

class Curriculum(db.Model):
    __tablename__ = 'curriculum'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    dateCreated = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)
    
    # Relación con Usuario
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    usuario = db.relationship('Usuario', back_populates='curriculums')