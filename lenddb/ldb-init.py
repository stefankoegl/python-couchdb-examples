#!/usr/bin/env python

# This program is used to create a new empty database
#
# Synopsis
#   ./ldb-init.py
#


from restkit import BasicAuth

from couchdbkit import Database
from couchdbkit.exceptions import ResourceNotFound


def init_db(dburl):
    print 'Initializing', dburl

    print 'Authenticating'
    cred = get_credentials()
    auth_filter = BasicAuth(*cred)

    db = Database(dburl, filters=[auth_filter])
    server = db.server

    try:
        server.delete_db(db.dbname)
        print 'Deleting', db.dbname

    except ResourceNotFound:
        pass

    db = server.get_or_create_db(db.dbname)
    print 'Created', db.dbname


def get_credentials():
    import getpass
    username = raw_input('Username: ')
    password = getpass.getpass('Password: ')
    return username, password


if __name__ == '__main__':
    from settings import DB_URL
    init_db(DB_URL)
