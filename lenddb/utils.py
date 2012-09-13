#!/usr/bin/env python
#
# This program is part of then "lenddb" Python CouchdB example
# It demonstrates how to provide authentication information in requests
#

import getpass
from restkit import BasicAuth


def get_credentials():
    """ gets user credentials from stdin and returns a auth filter list """

    username = raw_input('Username: ')
    if not username:
        return []

    password = getpass.getpass('Password: ')
    return [BasicAuth(username, password)]


def doc_repr(self):
    """ procudes a repr for a Document with dynamic properties """

    return '{cls}({properties})'.format(
            cls        = self.__class__.__name__,
            properties = ', '.join(
                '{k}={v}'.format(k=key, v=repr(getattr(self, key)))
                for key in self.all_properties().keys()
            )
        )

