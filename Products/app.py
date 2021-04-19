from config.db import db
from config.flask_app import app
# from flask_migrate import Migrate
from Controllers.ProductController import ProductController 
import threading
from GRPCServer import startServer

# migrate = Migrate(app, db)

app.register_blueprint(ProductController)




def runApp():
    app.run(port=5100)

if __name__ == '__main__':

    t2 = threading.Thread(target=runApp)
    t2.start()
    startServer()
    
