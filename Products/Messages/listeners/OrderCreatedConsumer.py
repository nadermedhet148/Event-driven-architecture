from .consumer import consumer
import json
import random
import string
from Events.OrderCreated import OrderCreatedEvent
from Models.Product import Product
from Config.db import db
from Messages.publish import publish
from Commands.AccpetOrder import AccpetOrder
from Commands.RejectOrder import RejectOrder


def orderCreated(ctedh, method, properties, body):
    event = OrderCreatedEvent(str(body, 'utf-8'))
    product = Product.query.get(event.productId)
    product.quantity = product.quantity - event.quantity
    if(product.quantity > 0):
        db.session.add(product)
        db.session.commit()
        event = AccpetOrder(
        event.orderId,
        event.productId,
        event.quantity * product.price
        )
        publish(
            'order/product_accpet_order' ,
            event.to_string()
            )
    else:
        event = RejectOrder(
        event.orderId,
        event.productId,
        )
        publish(
            'order/product_reject_order' ,
            event.to_string()
            )
    
 
    
def orderCreatedConsumer():
    consumer(channel_name="product/order_created", callback=orderCreated)