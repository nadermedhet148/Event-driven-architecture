import json

class AccpetOrder:

    def __init__(self,orderId,productId,price):
        self.orderId = orderId 
        self.productId = productId
        self.price = price

    def to_string(self):
        return  json.dumps({
            "orderId" : self.orderId,
            "productId" : self.productId,
            "price" : self.price
        })

