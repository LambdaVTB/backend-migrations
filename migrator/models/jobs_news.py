import uuid

from sqlalchemy import Boolean, Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, TSVECTOR

from migrator.base import DeclarativeBase
from migrator.models.jobs import Jobs
from migrator.models.news import News

class JobsNews(DeclarativeBase):
    __tablename__ = "jobs_news"

    id = Column(UUID, primary_key=True, default=lambda: str(uuid.uuid4()))
    job_id = Column(UUID, ForeignKey(Jobs.id, ondelete="CASCADE"), nullable=False)
    news_id = Column(UUID, ForeignKey(News.id, ondelete="CASCADE"), nullable=False)

