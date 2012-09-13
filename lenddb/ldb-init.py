#!/usr/bin/env python
#
# This program is part of then "lenddb" Python CouchdB example
# It demonstrates how to create a new empty database
#
# Synopsis
#   ./ldb-init.py
#


from couchdbkit import Database
from couchdbkit.exceptions import ResourceNotFound

from utils import get_credentials


def init_db(dburl):
    print 'Initializing', dburl

    print 'Authenticating'
    filters = get_credentials()

    db = Database(dburl, filters=filters)
    server = db.server

    try:
        server.delete_db(db.dbname)
        print 'Deleting', db.dbname

    except ResourceNotFound:
        pass

    db = server.get_or_create_db(db.dbname)
    print 'Created', db.dbname


if __name__ == '__main__':
    from settings import DB_URL
    init_db(DB_URL)
