import os
from connect import psycopg2
from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


app = Flask(__name__)
CORS(app)

# default_app = firebase_admin.initialize_app()
# cred = credentials.RefreshToken('path/to/refreshToken.json')
# default_app = firebase_admin.initialize_app(cred)
cred = credentials.Certificate(os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"))

firebase_admin.initialize_app(cred)
db = firestore.client

# Python cursor connection to PostgresSQL
conn = psycopg2.connect(
            host = "localhost",
            port = "5432",
            database = "db_grocery",
            user = os.environ.get("DB_USER"),
            password = os.environ.get("DB_PASS")
    )
       
cur = conn.cursor()


Users.users_ref = db.collection('users')
# Vehicle.vehicle_ref = db.collection('vehicle')
# Trip.trip_ref = db.collection('trip')


@app.route("/api/login", methods=["POST"])
def login():

    try:

        email = request.json.get("email")
        password = request.json.get("password")
        user_account = Users.login(email, password)
        print(user_account[1].to_dict())

        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"








    
if __name__ == "__main__":
    app.run(debug=True)
