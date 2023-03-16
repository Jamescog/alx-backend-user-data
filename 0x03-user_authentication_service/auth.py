#!/usr/bin/env python3
"""4. Hash password"""


from bcrypt import hashpw, gensalt
from db import DB, User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """returns a salted hash of the input password"""
    salt = gensalt()
    return hashpw(password.encode(), salt)


class Auth:
    """Auth class to interact with the authentication database"""

    def __init__(self) -> None:
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """takes email and password and return User object"""

        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed = _hash_password(password)
            user = self._db.add_user(email, hashed)

            return user
        raise ValueError("User {} already exists".format(email))
