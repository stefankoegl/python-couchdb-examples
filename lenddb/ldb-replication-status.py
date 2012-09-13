#!/usr/bin/env python
#
# This program is part of then "lenddb" Python CouchdB example
# It demonstrates how to access replication status
#
# Synopsis
#   ./ldb-replication-status.py
#


from restkit import BasicAuth

from couchdbkit import Database


def replication_status(db_url):
    cred = get_credentials()
    auth_filter = BasicAuth(*cred)
    db = Database(db_url, filters=[auth_filter])
    server = db.server

    # print a nice header
    header = '{:35s} => {:35s} {:5s} {:5s}%'.format('Source', 'Target',
            'Written', 'Progress')
    print header
    print '=' * len(header)

    # /_active_tasks has information about all running tasks (indexers,
    # replication, etc). We use it to get progress info for active
    # replication tasks
    for task in server.active_tasks():
        if task.get('type', None) != 'replication':
            continue

        print '{:35s} => {:35s} {:5d} {:5d}%'.format(
                task.get('source', ''),
                task.get('target', ''),
                task.get('docs_written', 0),
                task.get('progress', 0)
            )


    # For information about failed replications (eg filter does not exist
    # at the source, or the source does not exist at all), we have to look
    # into the documents in the /_replicator database
    replicator_db = server['_replicator']

    for result in replicator_db.view('_all_docs', include_docs=True):

        # we're not interested in design documents
        if result['id'].startswith('_design/'):
            continue

        doc = result['doc']
        if doc.get('_replication_state', None) != 'error':
            continue

        print '{:35s} => {:35s} {:>12s}'.format(
                doc.get('source', ''),
                doc.get('target', ''),
                doc.get('_replication_state', '')
            )



def get_credentials():
    import getpass
    username = raw_input('Username: ')
    password = getpass.getpass('Password: ')
    return username, password


if __name__ == '__main__':
    from settings import DB_URL

    replication_status(DB_URL)
