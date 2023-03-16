#!/usr/bin/env python3
"""4. Hash password"""


from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    """returns a salted hash of the input password"""
    salt = gensalt()
    return hashpw(password.encode(), salt)
