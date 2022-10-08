import uuid

from sqlalchemy import Boolean, Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, TSVECTOR

from migrator.base import DeclarativeBase
from models.jobs import Jobs
from models.tags import Tags

class TagsJobs(DeclarativeBase):
    __tablename__ = "tags_jobs"

    id = Column(UUID, primary_key=True, default=lambda: str(uuid.uuid4()))
    job_id = Column(UUID, ForeignKey(Jobs.id, ondelete="CASCADE"), nullable=False)
    tag_id = Column(UUID, ForeignKey(Tags.id, ondelete="CASCADE"), nullable=False)

