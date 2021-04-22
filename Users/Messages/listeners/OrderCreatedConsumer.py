from .consumer import consumer
import json
import random
import string
from Events.income.OrderCreated import OrderCreatedEvent
from Models.User import User
from Config.db import db
from Commands.AccpetOrder import AccpetOrder
from Commands.RejectOrder import RejectOrder
from Messages.publish import publish



def orderCreated(ctedh, method, properties, body):
    event = OrderCreatedEvent(str(body, 'utf-8'))
    user = User.query.get(event.userId)
    user.ordersCount =  user.ordersCount + 1
    user.balance = user.balance - event.totalPrice 
    if(user.balance > 0):
        db.session.add(user)
        db.session.commit()
        event = AccpetOrder(event.orderId,event.userId)
        publish('order/user_accpet_order',event.to_string())
    else:
        event = RejectOrder(event.orderId,event.userId)
        publish('order/user_reject_order' ,event.to_string())
    
    
def orderCreatedConsumer():
    consumer(channel_name="user/order_created", callback=orderCreated)