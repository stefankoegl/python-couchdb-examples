#!/usr/bin/env python
#
# This program is part of then "lenddb" Python CouchdB example
# It demonstrates how to access a view
#
# Synopsis
#   ./new-list-things.py
#

from models import Thing


def list_things():
    header = '{:35s} {:15s} {:15s}'.format('Id', 'Owner', 'Name')
    print header
    print '=' * len(header)

    things = Thing.view('things/by_owner_name', include_docs=True, reduce=False)
    for thing in things:
        print '{:35s} {:15s} {:15s}'.format(thing._id, thing.owner, thing.name)


if __name__ == '__main__':
    list_things()
