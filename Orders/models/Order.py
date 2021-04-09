from config.db import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, unique=False, nullable=False)
    productId = db.Column(db.Integer, unique=False, nullable=False)
    totalPrice = db.Column(db.Integer, unique=False, nullable=False)
    totalQuantity = db.Column(db.Integer, unique=False, nullable=False)