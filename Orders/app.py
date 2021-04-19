from config.db import db
from config.flask_app import app
# from flask_migrate import Migrate
from Controllers.OrderController import OrderController 
import threading

# migrate = Migrate(app, db)

app.register_blueprint(OrderController)



def runApp():
    app.run(port=5300,host="0.0.0.0")

if __name__ == '__main__':

    t2 = threading.Thread(target=runApp)
    t2.start()
    
