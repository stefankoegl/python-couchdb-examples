#!/usr/bin/env python

# This program is used to create a new empty database
#
# Synopsis
#   ./new-thing.py name [key1=val2 [key2=val2 [...]]]
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
