#!/usr/bin/env python
#
# This program is part of then "lenddb" Python CouchdB example
# It demonstrates how to replicate from another database
#
# Synopsis
#   ./ldb-replicate-friend.py
#


from couchdbkit import Database
from couchdbkit.exceptions import ResourceNotFound

from utils import get_credentials


def replicate(db_url, username, friend_name, friend_db_url):
    auth_filters = get_credentials()
    db = Database(db_url, filters=auth_filters)
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
    replication_id = '{src}-{target}'.format(src=friend_name, target=username)
    replicator_db[replication_id] = replication_doc


if __name__ == '__main__':
    from settings import DB_URL, USERNAME
    import sys

    friend_name = sys.argv[1]
    friend_db_url = sys.argv[2]

    replicate(DB_URL, USERNAME, friend_name, friend_db_url)
