#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(
            self,
            email: str,
            hashed_password: str) -> User:
        """ this will return the user object after it creates the user
            in the database

            Args:
                email - the email of the user
                hashed_password - the hashed_password of the user
            Returns:
                Newly created user object
        """

        user = User(email=email, hashed_password=hashed_password)
        self.__session.add(user)
        self.__session.commit()

        return user
