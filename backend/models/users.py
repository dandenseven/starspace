from firebase_admin import credentials, firestore, initialize_app
import datetime


class Users:

    users_ref=""

    def __init__(self, username="", email="", first_name="", last_name="", last_login="",user_id=None):

        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.last_login = last_login
        self.user_id =user_id

    def to_json(self):
        return {"username": self.username,
                "email": self.email,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "last_login": datetime.datetime(self.last_login).timestamp
                }
    

    def insert(self):
        self.users_ref.document().set(self.to_json())

    def logout(self):
        self.users_ref.document().update(self.to_json())

    def update(self):
        self.users_ref.document(self.user_id).update(self.to_json())

    def delete(self):
        self.users_ref.document(self.user_id).delete(self.to_json())

    @classmethod
    def users_for_user(cls, user_id):
        return cls.users_ref.document(user_id).get()

    @classmethod
    def login(cls, email, password):
        return cls.users_ref.where("email", "==", email).where("password", "==",
                                                               password).get()


if __name__ == "__main__":
    pass