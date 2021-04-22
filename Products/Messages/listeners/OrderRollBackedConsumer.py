from .consumer import consumer
import json
import random
import string
from Events.OrderRollBacked import OrderRollBackedEvent
from Models.Product import Product
from Config.db import db


def orderCreated(ctedh, method, properties, body):
    event = OrderRollBackedEvent(str(body, 'utf-8'))
    product = Product.query.get(event.productId)
    product.quantity = product.quantity + event.quantity
    db.session.add(product)
    db.session.commit()
    
def orderRollBackedConsumer():
    consumer(channel_name="product/roll_back_order", callback=orderCreated)