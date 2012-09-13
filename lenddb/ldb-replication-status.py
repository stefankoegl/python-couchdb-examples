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
    header = '{:>10s} {:35s} => {:35s} {:>5s} {:>6s}'.format('Id', 'Source',
            'Target', 'Docs', 'Prog.')
    print header
    print '=' * len(header)

    # /_active_tasks has information about all running tasks (indexers,
    # replication, etc). We use it to get progress info for active
    # replication tasks
    for task in server.active_tasks():
        if task.get('type', None) != 'replication':
            continue

        print '{:>10s} {:35s} => {:35s} {:5d} {:5d}%'.format(
                task.get('doc_id', ''),
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

        # all active (non-error) replication tasks have already been printed
        # above; we're only interested in those that failed
        if doc.get('_replication_state', None) != 'error':
            continue

        print '{:>10s} {:35s} => {:35s} {:>12s}'.format(
                result['id'],
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
