from werkzeug.security import generate_password_hash, check_password_hash
#from webapp.database import users

class User:
    def __init__(self, username, hash_password):
        self.username = username
        self.hash_password = hash_password

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False

    def get_id(self):
        return self.username
    
    def get_hash_password(self):
        return self.hash_password

