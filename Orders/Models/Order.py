from Config.db import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, unique=False, nullable=True)
    productId = db.Column(db.Integer, unique=False, nullable=True)
    totalPrice = db.Column(db.Integer, unique=False, nullable=True)
    totalQuantity = db.Column(db.Integer, unique=False, nullable=True)
    status = db.Column(db.String, unique=False, nullable=False)

    
    def toDict(self):
        return{
         "id" : self.id,
         "userId" : self.userId,
         "productId" : self.productId,
         "totalPrice" : self.totalPrice,
         "totalQuantity" : self.totalQuantity,
         "status" : self.status
        }