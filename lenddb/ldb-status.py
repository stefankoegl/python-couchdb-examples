#!/usr/bin/env python

# This program is used to create a new empty database
#
# Synopsis
#   ./new-thing.py name [key1=val2 [key2=val2 [...]]]
#

from models import Thing


def get_status():
    header = '{:35s} {:15s} {:15s}'.format('Id', 'Owner', 'Status')
    print header
    print '=' * len(header)

    things = Thing.view('things/status',
            group_level = 2
        )

    for result in things:
        print '{:35s} {:15s} {:15s}'.format(result['key'][1], result['key'][0], result['value'])


if __name__ == '__main__':
    get_status()
