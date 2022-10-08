import uuid

from sqlalchemy import Boolean, Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from migrator.base import DeclarativeBase
from models.jobs import Jobs

class Users(DeclarativeBase):
    __tablename__ = "users"

    id = Column(UUID, primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    job_id = Column(UUID, ForeignKey(Jobs.id, ondelete="CASCADE"), nullable=True)

