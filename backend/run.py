from routes.app import app
from firebase_admin import credentials, firestore, initialize_app
from models.users import Users
from models.stores import Stores
from models.grocery_lists import Grocery_list
from connect import psycopg2


cred = credentials.Certificate('key.json')


default_app = initialize_app(cred)
db = firestore.client()



Users.users_ref = db.collection('users')
Stores.stores_ref = db.collection('stores')
Grocery_list._ref = db.collection('grocery_list')

if __name__ == "__main__":
    app.run()