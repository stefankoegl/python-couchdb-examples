#!/usr/bin/env python
#
# This program is part of then "lenddb" Python CouchdB example
# It demonstrates how to fetch an object by its _id
#
# Synopsis
#   ./ldb-get-thing.py <_id>
#

from models import Thing


def get_thing(thing_id):
    thing = Thing.get(thing_id)

    print '{key}: {val}'.format(key='_id', val=thing._id)
    print '{key}: {val}'.format(key='_rev', val=thing._rev)

    for key in thing.all_properties().keys():
        print '{key}: {val}'.format(key=key, val=getattr(thing, key))


if __name__ == '__main__':
    import sys
    get_thing(sys.argv[1])
