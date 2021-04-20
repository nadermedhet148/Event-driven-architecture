from config.db import db
from config.flask_app import app
from Controllers.UserController import UserController 
from listeners.OrderCreatedConsumer import orderCreatedConsumer 
from models.User import User
import threading
from GRPCServer import startServer


app.register_blueprint(UserController)




if __name__ == '__main__':
    t1 = threading.Thread(target=orderCreatedConsumer)
    t1.start()
    t2 = threading.Thread(target=app.run)
    t2.start()
    startServer()
    
