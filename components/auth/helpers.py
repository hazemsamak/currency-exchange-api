__author__ = 'hsamak'

import hashlib
import os


def generate_hash_key():
    """
    @return: A hashkey for use to authenticate agains the API.
    """
    return hashlib.md5(os.urandom(32)).hexdigest()


print(generate_hash_key())
