import json

class CheckProductQuantity:

    def __init__(self,orderId,productId,quantity):
        self.orderId = orderId 
        self.productId = productId
        self.quantity = quantity

    def to_string(self):
        return  json.dumps({
            "orderId" : self.orderId,
            "productId" : self.productId,
            "quantity" : self.quantity,
        })

