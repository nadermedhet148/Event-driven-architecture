from .consumer import consumer
import json
import random
import string




def orderCreated(ctedh, method, properties, body):
    event = json.loads(str(body, 'utf-8'))
    print(event)

def orderCreatedConsumer():
    consumer(channel_name="events.order.created", callback=orderCreated)
