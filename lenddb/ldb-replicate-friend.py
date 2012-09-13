#!/usr/bin/env python
#
# This program is part of then "lenddb" Python CouchdB example
# It demonstrates how to replicate from another database
#
# Synopsis
#   ./ldb-replicate-friend.py
#


from restkit import BasicAuth

from couchdbkit import Database
from couchdbkit.exceptions import ResourceNotFound


def replicate(db_url, friend_name, friend_db_url):
    cred = get_credentials()
    auth_filter = BasicAuth(*cred)
    db = Database(db_url, filters=[auth_filter])
    replicator_db = db.server['_replicator']

    # this describes the replication task
    replication_doc = {
        "source": friend_db_url,
        "target": db_url,
        "continuous": True,
        "filter": "things/from_friend",
        "query_params": {
            "friend": friend_name,
        }
    }

    # we try to delete an existing replication with the same Id
    # this would stop the replication
    try:
        del replicator_db[friend_name]
    except ResourceNotFound:
        pass

    # we store the replication task, which will automatically start it
    replicator_db[friend_name] = replication_doc


def get_credentials():
    import getpass
    username = raw_input('Username: ')
    password = getpass.getpass('Password: ')
    return username, password


if __name__ == '__main__':
    from settings import DB_URL
    import sys

    friend_name = sys.argv[1]
    friend_db_url = sys.argv[2]

    replicate(DB_URL, friend_name, friend_db_url)
