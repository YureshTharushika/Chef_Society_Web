
from datetime import datetime
from mongoengine import *

from flask_login import UserMixin


class User(Document, UserMixin):

    def __init__(self, user_json):
        self.user_json = user_json

    def get_id(self):
        object_id = self.user_json.get('_id')
        return str(object_id)

    def is_authenticated(self):
        return True    
    
    # username = StringField(unique=True, required=True)
    # email = EmailField(unique=True, required=True)
    # password = BinaryField(required=True)
    # date_created = DateTimeField(default=datetime.utcnow)
