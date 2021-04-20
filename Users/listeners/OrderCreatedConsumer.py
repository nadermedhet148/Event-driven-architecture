from .consumer import consumer
import json
import random
import string
from Events.OrderCreated import OrderCreatedEvent



def orderCreated(ctedh, method, properties, body):
    event = OrderCreatedEvent(str(body, 'utf-8'))
    
def orderCreatedConsumer():
    consumer(channel_name="order_created", callback=orderCreated)
