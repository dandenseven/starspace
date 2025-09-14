from firebase_admin import credentials, firestore, initialize_app
import datetime


class grocery_list():

    grocery_list_ref = ""

    def __init__(self, store_name="", store_items="", store_shopped_items="", store_missing_items="", store_shopping_list="",
                  store_id=None, user_id=None):
        
        self.store_name = store_name
        self.store_items = store_items
        self.store_shopped_items = store_shopped_items
        self.store_missing_items = store_missing_items
        self.store_shopping_list = store_shopping_list
        self.store_id = store_id
        self.user_id = user_id

    def to_json(self):
        return{"store_name": self.store_name,
            "store_items": self.store_items,
            "store_shopped_items": self.store_shopped_items,
            "store_missing_items": self.store_missing_items,
            "store_shopping_list": self.store_shopping_list,
            "store_id": self.store_id,
            "user_id": self.user_id
        }