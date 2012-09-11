#!/usr/bin/env python

# This program is used to create a new empty database
#
# Synopsis
#   ./ldb-init.py
#


from restkit import BasicAuth

from couchdbkit import Database
from couchdbkit.loaders import FileSystemDocsLoader


def init_db(dburl):
    cred = get_credentials()
    auth_filter = BasicAuth(*cred)
    db = Database(dburl, filters=[auth_filter])

    loader = FileSystemDocsLoader('_design')
    loader.sync(db, verbose=True)


def get_credentials():
    import getpass
    username = raw_input('Username: ')
    password = getpass.getpass('Password: ')
    return username, password


if __name__ == '__main__':
    from settings import DB_URL
    init_db(DB_URL)
