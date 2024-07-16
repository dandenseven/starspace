import os
import os.path
from flask import Flask, json, request
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

@app.route("/api/login", methods=["POST"])
def login():

    



if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port="port")