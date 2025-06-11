import os
from connect import psycopg2
from flask import Flask, request
from bs4 import BeautifulSoup
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

conn = psycopg2.connect(
            host = "localhost",
            port = "5432",
            database = "db_grocery",
            user = os.environ.get("DB_USER"),
            password = os.environ.get("DB_PASS")
    )
       
cur = conn.cursor() 










    
if __name__ == "__main__":
    app.run(debug=True)
