import json

class OrderCreatedEvent:

    def __init__(self ,payloadString):
        payload = json.loads(payloadString)
        print(payload)
        self.orderId   = payload['orderId'] 
        self.productId = payload['productId']
        self.quantity  = payload['quantity']

