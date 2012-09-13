from datetime import datetime

from couchdbkit import Document, StringProperty, DateTimeProperty, Database
from settings import DB_URL
from utils import doc_repr

db = Database(DB_URL)


class Thing(Document):
    owner = StringProperty(required=True)
    name = StringProperty(required=True)

    __repr__ = doc_repr

Thing.set_db(db)



class Lending(Document):
    thing = StringProperty(required=True)
    owner = StringProperty(required=True)
    to_user = StringProperty(required=True)
    lent = DateTimeProperty(default=datetime.now)
    returned = DateTimeProperty()

    __repr__ = doc_repr

Lending.set_db(db)
