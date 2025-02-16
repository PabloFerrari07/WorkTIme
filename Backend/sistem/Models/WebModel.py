from sistem import db
from datetime import datetime

class WebModel(db.Model):
    __tablename__ = 'webs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    dateCreated = db.Column(db.DateTime, default=datetime.now)
    category = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<Web {self.nombre}>'
    
def __init__(self, name, url, description, category, dateCreated):
        self.name = name
        self.url = url
        self.description = description
        self.category = category
        self.dateCreated = dateCreated