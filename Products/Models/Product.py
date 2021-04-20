from Config.db import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
    price = db.Column(db.Integer, unique=False, nullable=False)
    quantity = db.Column(db.Integer, unique=False, nullable=False)

    def toDict(self):
        return{
            "id" : self.id,
            "name" : self.name, 
            "price" : self.price,
            "quantity" : self.quantity,
        }