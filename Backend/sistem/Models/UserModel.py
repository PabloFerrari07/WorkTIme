from sistem import db
from sistem.Models.WebModel import WebModel
from sistem.Models.CurriculumModel import CurriculumModel

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),)
    password = db.Column(db.Text)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(80), unique=True, nullable=False)
    web = db.relationship('WebModel', backref='user', lazy=True)
    curriculum = db.relationship('CurriculumModel', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'