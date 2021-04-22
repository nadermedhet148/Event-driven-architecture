from .consumer import consumer
from Services.OrderService import OrderService
import json

orderService = OrderService()

def userRejectOrder(ctedh, method, properties, body):
    payload = json.loads( str(body, 'utf-8'))
    orderService.handleUserRejectOrder(payload)

    
 
    
def userRejectOrderConsumer():
    consumer(channel_name="order/user_reject_order", callback=userRejectOrder)