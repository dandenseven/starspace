import psycopg2
# Connect to Postgres DB


connection = psycopg2.connect(database="daneknight", 
                user="username", 
                password="pass", 
                host="hostname", 
                port=5432)

cursor = connection.cursor()

cursor.execute("SELECT * from portal.portal_users;")

# Fetch all rows from database
record = cursor.fetchall()

print("Data from Database:- ", record)

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