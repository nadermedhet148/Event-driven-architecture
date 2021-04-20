from .consumer import consumer
import json
import random
import string




def orderCreated(ctedh, method, properties, body):
    event = json.loads(str(body, 'utf-8'))
    print(event , 'order_created' )

def orderCreatedConsumer():
    consumer(channel_name="order_created", callback=orderCreated)
