import uuid

from sqlalchemy import Boolean, Column, String
from sqlalchemy.dialects.postgresql import UUID

from migrator.base import DeclarativeBase


class Users(DeclarativeBase):
    __tablename__ = "users"

    id = Column(UUID, primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(String, nullable=False)

