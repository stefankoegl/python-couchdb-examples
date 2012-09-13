#!/usr/bin/env python
#
# This program is part of then "lenddb" Python CouchdB example
# It demonstrates how to synchronize design docs from the filesystem
#
# Synopsis
#   ./ldb-sync-ddocs.py
#


from restkit import BasicAuth

from couchdbkit import Database
from couchdbkit.loaders import FileSystemDocsLoader


def sync_ddocs(dburl):
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
    sync_ddocs(DB_URL)
