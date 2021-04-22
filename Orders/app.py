from Config.db import db
from Config.flask_app import app
from Controllers.OrderController import OrderController 
import threading
from Messages.listeners.ProductAccpetOrderConsumer import productAccpetOrderConsumer
from Messages.listeners.ProductRejectOrderConsumer import productRejectOrderConsumer
from Messages.listeners.UserAccpetOrderConsumer import userAccpetOrderConsumer
from Messages.listeners.UserRejectOrderConsumer import userRejectOrderConsumer



app.register_blueprint(OrderController)



def runApp():
    app.run(port=5300,host="0.0.0.0")

if __name__ == '__main__':
    t1 = threading.Thread(target=productAccpetOrderConsumer)
    t1.start()
    t3 = threading.Thread(target=productRejectOrderConsumer)
    t3.start()
    t4 = threading.Thread(target=userAccpetOrderConsumer)
    t4.start()
    t5 = threading.Thread(target=userRejectOrderConsumer)
    t5.start()
    t2 = threading.Thread(target=runApp)
    t2.start()
    
