from uuid import uuid4

from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Account(Base):
    __tablename__ = "account"

    id = Column(String(64), primary_key=True, unique=True, default=uuid4)
    username = Column(String(64))
    password = Column(String(64))
