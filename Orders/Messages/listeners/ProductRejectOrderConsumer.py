from .consumer import consumer
from Services.OrderService import OrderService
import json

orderService = OrderService()

def productRejectOrder(ctedh, method, properties, body):
    payload = json.loads( str(body, 'utf-8'))
    orderService.handleProductRejectOrder(payload)

    
 
    
def productRejectOrderConsumer():
    consumer(channel_name="order/product_reject_order", callback=productRejectOrder)