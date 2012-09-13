#!/usr/bin/env python
#
# This program is part of then "lenddb" Python CouchdB example
# It demonstrates how to synchronize design docs from the filesystem
#
# Synopsis
#   ./ldb-sync-ddocs.py
#


from couchdbkit import Database
from couchdbkit.loaders import FileSystemDocsLoader

from utils import get_credentials


def sync_ddocs(dburl):
    auth_filters = get_credentials()
    db = Database(dburl, filters=auth_filters)

    loader = FileSystemDocsLoader('_design')
    loader.sync(db, verbose=True)


if __name__ == '__main__':
    from settings import DB_URL
    sync_ddocs(DB_URL)
