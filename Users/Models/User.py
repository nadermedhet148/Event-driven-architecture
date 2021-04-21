from Config.db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
    ordersCount = db.Column(db.Integer , default=0)
    balance = db.Column(db.Integer,default=0)


    def toDict(self):
        return {
            "userId": self.id,
            "name" : self.name,
            "ordersCount" : self.ordersCount,
            "balance" : self.balance,
            }