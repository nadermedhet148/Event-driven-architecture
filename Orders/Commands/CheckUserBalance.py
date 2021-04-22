import json

class CheckUserBalance:

    def __init__(self,orderId,userId,price):
        self.orderId = orderId 
        self.userId = userId
        self.price = price

    def to_string(self):
        return  json.dumps({
            "orderId" : self.orderId,
            "userId" : self.userId,
            "price" : self.price,
        })

