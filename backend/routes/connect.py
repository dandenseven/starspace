import os
import psycopg2
from config import load_config


# Function to pass in the connection configuration to PostgresSQL server
def connect(config):

    conn = psycopg2.connect(
            host = "localhost",
            port = "5432",
            database = "db_grocery",
            user = os.environ.get("DB_USER"),
            password = os.environ.get("DB_PASS")
    )

    try:
        # connecting to the PostgresSQL server
        with psycopg2.connect(**config) as conn:
                print("Connected to the PostgreSQl server.")
                return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


if __name__ == '__main__':
    config = load_config()
    connect(config)
    