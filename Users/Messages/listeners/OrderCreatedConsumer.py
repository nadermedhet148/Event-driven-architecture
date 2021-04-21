from .consumer import consumer
import json
import random
import string
from Events.income.OrderCreated import OrderCreatedEvent
from Models.User import User
from Config.db import db


def orderCreated(ctedh, method, properties, body):
    event = OrderCreatedEvent(str(body, 'utf-8'))
    user = User.query.get(event.userId)
    user.ordersCount =  user.ordersCount + 1
    user.balance = user.balance - event.totalPrice 
    db.session.add(user)
    db.session.commit()
    
    
def orderCreatedConsumer():
    consumer(channel_name="order_created", callback=orderCreated)