from couchdbkit import Document, StringProperty, Database
from settings import DB_URL

class Thing(Document):
    owner = StringProperty()
    name = StringProperty()


db = Database(DB_URL)
Thing.set_db(db)
