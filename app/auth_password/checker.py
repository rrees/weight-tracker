import os

_valid_usernames = os.environ["VALID_USERNAMES"].split(",")


def check_credentials(username, password):
    return username in _valid_usernames and password == os.environ["ADMIN_PASSWORD"]
