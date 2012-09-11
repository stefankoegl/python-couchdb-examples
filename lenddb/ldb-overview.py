#!/usr/bin/env python

# This program is used to create a new empty database
#
# Synopsis
#   ./new-thing.py name [key1=val2 [key2=val2 [...]]]
#

from models import Thing


def list_things():
    header = '{:15s} {:8s}'.format('Owner', '# Things')
    print header
    print '=' * len(header)

    owners = Thing.view('things/by_owner_name',
            group_level  = 1
        )

    for owner_status in owners:
        owner = owner_status['key'][0]
        thing_count = owner_status['value']
        print '{:15s} {:8d}'.format(owner, thing_count)


if __name__ == '__main__':
    list_things()
