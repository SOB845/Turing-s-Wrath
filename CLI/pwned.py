# Orginal code written by Mike Pound and contributors
# Github: https://github.com/mikepound/pwned-search/blob/master/pwned.py

import hashlib
import sys

try:
    import requests
except ModuleNotFoundError:
    print("###  pip install requests  ###")
    raise


def lookup_pwned_api(pwd):

    """Returns hash and number of times password was seen in pwned database.
    Args:
        pwd: password to check
    Returns:
        A (sha1, count) tuple where sha1 is SHA-1 hash of pwd and count is number
        of times the password was seen in the pwned database.  count equal zero
        indicates that password has not been found.
    Raises:
        RuntimeError: if there was an error trying to fetch data from pwned
            database.
        UnicodeError: if there was an error UTF_encoding the password.
    """

    sha1pwd = hashlib.sha1(pwd.encode('utf-8')).hexdigest()
    head, tail = sha1pwd[:5], sha1pwd[5:]
    url = 'https://api.pwnedpasswords.com/range/' + head
    res = requests.get(url)
    if not res.ok:
        raise RuntimeError('Error fetching "{}": {}'.format(
            url, res.status_code))
    hashes = (line.split(':') for line in res.text.splitlines())
    count = next((int(count) for t, count in hashes if t == tail), 0)

    if count > 0:
        foundmsg = "This Password was found with {} occurrences. It's not safe at all!"
        print(foundmsg.format(count))

    else:
        print("Password is safe to use.")


    return sha1pwd, count
