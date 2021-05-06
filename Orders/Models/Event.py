from Config.db import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, unique=False, nullable=True)
    orderId = db.Column(db.Integer, unique=False, nullable=True)
    payload = db.Column(db.String, unique=False, nullable=False)

    
