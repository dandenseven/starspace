from firebase_admin import credentials, firestore, initialize_app
import datetime


class Stores:

    stores_ref = ""

    def __init__(self, store_name="", store_address="", store_hours="", store_items="", store_sale_items="", 
                 sales_promotions_start_date="", sales_promotions_end_date="", store_id=None):

        self.store_name = store_name      
        self.store_address = store_address
        self.store_hours = store_hours
        self.store_items = store_items
        self.store_sale_items = store_sale_items
        self.sales_promotions_start_date = sales_promotions_start_date
        self.sales_promotions_end_date = sales_promotions_end_date
        self.store_id = store_id
    

    def to_json(self):
        return{"store_name": self.store_name,
                "store_address=": self.store_address,
                "store_hours=": self.store_hours,
                "store_items": self.store_items,
                "store_sale_items": self.store_sale_items,
                "self.sales_promotions_start_date": self.sales_promotions_start_date,
                "self.sales_promotions_end_date": self.sales_promotions_end_date,
                "store_id": self.store_id
                }

        