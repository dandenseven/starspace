from firebase_admin import credentials, firestore, initialize_app
import datetime


class grocery_list():

    grocery_list_ref = ""

    def __init__(self, store_name="", store_item="", store_item_price="", store_shopped_item="", store_shopped_item_price="", 
                 store_missing_item="", store_missing_item_price="",store_shopping_list="",store_id=None, user_id=None):
        
        self.store_name = store_name
        self.store_item = store_item
        self.store_item_price = store_item_price
        self.store_shopped_item = store_shopped_item
        self.store_shopped_item_price =  store_shopped_item_price
        self.store_missing_item = store_missing_item
        self.store_missing_item_price = store_missing_item_price
        self.store_shopping_list = store_shopping_list
        self.store_id = store_id
        self.user_id = user_id

    def to_json(self):
        return{"store_name": self.store_name,
            "store_item": self.store_item,
            "store_item_price": self.store_item_price,
            "store_shopped_item": self.store_shopped_item,
            "store_shopped_item_price":self.store_shopped_item_price,
            "store_missing_item": self.store_missing_item,
            "store_missing_item_price":self.store_missing_item_price,
            "store_shopping_list": self.store_shopping_list,
            "store_id": self.store_id,
            "user_id": self.user_id
        }