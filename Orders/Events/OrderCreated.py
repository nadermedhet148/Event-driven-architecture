import json

class OrderCreated:

    def __init__(self , orderId , userId , productId , totalPrice , quantity):
        self.orderId = orderId 
        self.userId = userId
        self.productId = productId
        self.quantity = quantity

    def to_string(self):
        return  json.dumps({
            "orderId" : self.orderId,
            "userId" : self.userId,
            "productId" : self.productId,
            "totalPrice" : self.totalPrice,
            "quantity" : self.quantity,
        })

