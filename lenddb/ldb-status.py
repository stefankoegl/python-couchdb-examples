#!/usr/bin/env python
#
# This program is part of then "lenddb" Python CouchdB example
# It demonstrates how to access a reduced and grouped view
#
# Synopsis
#   ./new-status.py
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
