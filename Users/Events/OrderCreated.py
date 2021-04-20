import json

class OrderCreatedEvent:

    def __init__(self ,payloadString):
        payload = json.load(payloadString)
        self.orderId = payload.orderId
        self.userId = payload.userId
        self.productId = payload.productId
        self.totalPrice = payload.totalPrice
        self.quantity = payload.quantity

