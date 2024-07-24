import datetime
from models.grocery import Grocery




class Users:

    users_acct = ""

    def __init__(self, username="", email="", phone_number="", first_name="", last_name="",
                last_login="", user_id=""):
        
        self.username = username
        self.email = email
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.last_login = last_login
        self.user_id = user_id


    def to_json(self):
        return {"username": self.username,
                "email": self.email,
                "phone_number": self.phone_number,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "last_login": datetime.datetime().timestamp()
                }