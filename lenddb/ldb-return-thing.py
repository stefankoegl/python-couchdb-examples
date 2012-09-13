#!/usr/bin/env python
#
# This program is part of then "lenddb" Python CouchdB example
# It demonstrates how to update documents
#
# Synopsis
#   ./ldb-return-thing.py <lend_id>
#

from datetime import datetime

from models import Lending


def return_thing(username, lend_id):

    lending = Lending.get(lend_id)
    lending.returned = datetime.now()
    lending.save()

    print lending, 'saved with _id', lending._id


if __name__ == '__main__':
    import sys
    from settings import USERNAME

    lend_id = sys.argv[1]

    return_thing(USERNAME, lend_id)
