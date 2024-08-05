import os
import os.path
from flask import Flask, json, request
from flask_cors import CORS
import sqlite3




app = Flask(__name__)
CORS(app)

# con = sqlite3.connnect("grocery.db")
# cur = con.cursor

@app.route("/api/login", methods=["POST"]) 




if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port="port")