import os
from psycopg2 import config, connect
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

cred = connect(config)





    
if __name__ == "__main__":
    app.run(threaded=True, ost='0.0.0.0', port="port")