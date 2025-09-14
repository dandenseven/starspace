from firebase_admin import credentials, firestore, initialize_app
import datetime


class Users:

    users_ref=""

    def __init__(self, username="", email="", first_name="", last_name="", user_id=None):

        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.user_id =user_id

    def to_json(self):
        return {"username": self.username,
                "email": self.email,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "user_id": self.user_id
                }