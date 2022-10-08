import uuid

from sqlalchemy import Boolean, Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, TSVECTOR

from migrator.base import DeclarativeBase
from models.jobs import Jobs
from models.users import Users

class UsersJobs(DeclarativeBase):
    __tablename__ = "users_jobs"

    id = Column(UUID, primary_key=True, default=lambda: str(uuid.uuid4()))
    users_id = Column(UUID, ForeignKey(Users.id, ondelete="CASCADE"), nullable=False)
    job_id = Column(UUID, ForeignKey(Jobs.id, ondelete="CASCADE"), nullable=False)
