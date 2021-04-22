from .consumer import consumer
from Services.OrderService import OrderService
import json

orderService = OrderService()

def productAccpetOrder(ctedh, method, properties, body):
    payload = json.loads( str(body, 'utf-8'))
    orderService.handleProductAccpetOrder(payload)
    
 
    
def productAccpetOrderConsumer():
    consumer(channel_name="order/product_accpet_order", callback=productAccpetOrder)