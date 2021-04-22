import json

class AccpetOrder:

    def __init__(self,orderId,userId):
        self.orderId = orderId 
        self.userId = userId

    def to_string(self):
        return  json.dumps({
            "orderId" : self.orderId,
            "userId" : self.userId,
        })

