import os
import sys
import uuid

def find_or_create_secret_key():
    """
    Look for secret_key.py and return the SECRET_KEY entry in it if the file exists.
    Otherwise, generate a new secret key, save it in secret_key.py, and return the key.
    """
    SECRET_KEY_DIR = os.path.dirname(__file__)
    SECRET_KEY_FILEPATH = os.path.join(SECRET_KEY_DIR, 'secret_key.py')
    sys.path.insert(1,SECRET_KEY_DIR)

    if os.path.isfile(SECRET_KEY_FILEPATH):
        from secret_key import SECRET_KEY
        return SECRET_KEY
    else:
        from django.utils.crypto import get_random_string
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&amp;*(-_=+)'
        new_key = get_random_string(50, chars)
        with open(SECRET_KEY_FILEPATH, 'w') as f:
            f.write("# Django secret key\n# Do NOT check this into version control.\n\nSECRET_KEY = '%s'\n" % new_key)
        from secret_key import SECRET_KEY
        return SECRET_KEY

def find_or_create_uuid():
    """
    Look for instance_uuid.py and return the UUID entry in it if the file exists.
    Otherwise, generate a new UUID, save it in instance_uuid.py, and return the UUID.
    """
    UUID_DIR = os.path.dirname(__file__)
    UUID_FILEPATH = os.path.join(UUID_DIR, 'instance_uuid.py')
    sys.path.insert(1, UUID_DIR)

    if os.path.isfile(UUID_FILEPATH):
        from instance_uuid import UUID
        return UUID
    else:
        with open(UUID_FILEPATH, 'w') as f:
            f.write("# Instance UUID\n\n\nUUID = '%s'\n" % uuid.uuid4())
        from instance_uuid import UUID
        return UUID
