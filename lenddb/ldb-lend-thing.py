#!/usr/bin/env python
#
# This program is part of then "lenddb" Python CouchdB example
# It demonstrates how to create new documents
#
# Synopsis
#   ./ldb-lend-thing.py <thing_id> <to_username>
#

from datetime import datetime

from couchdbkit import Database
from couchdbkit.exceptions import ResourceNotFound

from models import Thing, Lending


def lend_thing(username, thing_id, to_user):

    try:
        thing = Thing.get(thing_id)
    except ResourceNotFound:
        print 'Thing not found'
        return

    lending = Lending(thing=thing_id, user=username, to_user=to_user)
    lending.save()

    print lending, 'saved with _id', lending._id


if __name__ == '__main__':
    import sys
    from settings import USERNAME

    thing_id, to_user = sys.argv[1:]

    lend_thing(USERNAME, thing_id, to_user)
