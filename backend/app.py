import os
from config import load_config
from flask import Flask
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)





# def connect(config):

#     conn = psycopg2.connect(
#             host = "localhost",
#             port = "5432",
#             database = "db_grocery",
#             user = os.environ.get("DB_USER"),
#             password = os.environ.get("DB_PASS")
#     )

#     try:
#         # connecting to the PostgresSQL server
#         with psycopg2.connect(**config) as conn:
#                 print("Connected to the PostgreSQl server.")
#                 return conn
#     except (psycopg2.DatabaseError, Exception) as error:
#         print(error)


# if __name__ == '__main__':
#     config = load_config()
#     connect(config)
    
    