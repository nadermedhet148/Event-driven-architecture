from .consumer import consumer
import json
import random
import string
from Events.income.OrderCreated import OrderCreatedEvent
from Models.Product import Product
from Config.db import db


def orderCreated(ctedh, method, properties, body):
    event = OrderCreatedEvent(str(body, 'utf-8'))
    product = Product.query.get(event.productId)
    product.quantity = product.quantity - event.quantity 
    db.session.add(product)
    db.session.commit()
    
    
def orderCreatedConsumer():
    consumer(channel_name="order_created", callback=orderCreated)