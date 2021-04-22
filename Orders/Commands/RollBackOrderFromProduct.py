import json

class RollBackOrderFromProduct:

    def __init__(self,orderId,productId):
        self.orderId = orderId 
        self.productId = productId

    def to_string(self):
        return  json.dumps({
            "orderId" : self.orderId,
            "productId" : self.productId
        })

