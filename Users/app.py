from Config.db import db
from Config.flask_app import app
from Controllers.UserController import UserController 
from Messages.listeners.OrderCreatedConsumer import orderCreatedConsumer 
import threading
from GRPCServer import startServer


app.register_blueprint(UserController)




if __name__ == '__main__':
    t1 = threading.Thread(target=orderCreatedConsumer)
    t1.start()
    t2 = threading.Thread(target=app.run)
    t2.start()
    startServer()
    
