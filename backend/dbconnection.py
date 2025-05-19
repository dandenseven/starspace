# import psycopg2
# # Connect to Postgres DB
# import os

# # Database connection parameters

# host = 'localhost'
# port = '5432'
# database = 'db_grocery'
# user = os.environ.get('DB_USER')
# password = os.environ.get('DB_PASS')

# #Connect to the database
# connection = psycopg2.connect(
#     host=host,
#     port=port,
#     database=database,
#     user=user,
    # password=password
)

# connection = psycopg2.connect(database="daneknight", 
#                 user= os.environ.get('DB_USER'),
#                 password= os.environ.get('DB_PASS'), 
#                 host="localhost", 
#                 port=5432)

# cursor = connection.cursor()


# cursor.close()
# connection.close()
# cursor.execute("SELECT * from portal.portal_users;")

# Fetch all rows from database
# record = cursor.fetchall()

# print("Data from Database:- ", record)

# import os
# import sys

# if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
#     print("Inside venv")
# else:
#     print("Not in venv")

# if 'VIRTUAL_ENV' in os.environ:
#     print("Inside venv")
# else:
#     print("Not in venv")