#!/usr/bin/env python
#
# This program is part of then "lenddb" Python CouchdB example
# It demonstrates how to use the _changes feed
#
# Synopsis
#   ./ldb-changes-log.py [since-value]
#

from couchdbkit import Consumer, Database

from models import Thing, Lending


def wait_for_changes(db_url, since):
    db = Database(db_url)
    consumer = Consumer(db)
    consumer.wait(callback, since=since, heartbeat=1000, include_docs=True)


def callback(line):
    seq = line['seq']
    doc = line['doc']

    if doc.get('doc_type', None) == 'Thing':
        obj = Thing.wrap(doc)

    elif doc.get('doc_type', None) == 'Lending':
        obj = Lending.wrap(doc)

    else:
        # we also have other types of documents - _design docs
        return

    print '{:5d}  {:s}  {:s}'.format(seq, line['id'], obj)


if __name__ == '__main__':
    import sys
    from settings import DB_URL

    if len(sys.argv) > 1:
        since = int(sys.argv[1])
    else:
        since = 0


    wait_for_changes(DB_URL, since)
