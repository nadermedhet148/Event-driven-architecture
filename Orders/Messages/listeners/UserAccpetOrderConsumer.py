from .consumer import consumer
from Services.OrderService import OrderService
import json

orderService = OrderService()

def userAccpetOrder(ctedh, method, properties, body):
    payload = json.loads( str(body, 'utf-8'))
    print('aaaaaaa')
    orderService.handleUserAccpetOrder(payload)
    
 
    
def userAccpetOrderConsumer():
    consumer(channel_name="order/user_accpet_order", callback=userAccpetOrder)