#!/usr/bin/env python3
"""4. Hash password"""


from bcrypt import hashpw, gensalt, checkpw
from db import DB, User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """returns a salted hash of the input password"""
    salt = gensalt()
    return hashpw(password.encode(), salt)


def _generate_uuid() -> str:
    """generate and return uuid"""
    return str(uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """Check email and password"""
        try:
            user = self._db.find_user_by(email=email)
            hashed = user.hashed_password
            return checkpw(password.encode(), hashed)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """returns session id as string"""
        try:
            user = self._db.find_user_by(email=email)
            uuid = _generate_uuid()
            self._db.update_user(user.id, session_id=uuid)
            return uuid
        except NoResultFound:
            return None
