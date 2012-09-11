from datetime import datetime

from couchdbkit import Document, StringProperty, DateTimeProperty, Database
from settings import DB_URL

db = Database(DB_URL)


class Thing(Document):
    owner = StringProperty()
    name = StringProperty()

Thing.set_db(db)



class Lending(Document):
    thing = StringProperty()
    owner = StringProperty()
    to_user = StringProperty()
    lent = DateTimeProperty(default=datetime.now)
    returned = DateTimeProperty()

Lending.set_db(db)
