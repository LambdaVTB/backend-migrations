
import uuid

from sqlalchemy import Boolean, Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, TSVECTOR

from migrator.base import DeclarativeBase
from models.news import News
from models.tags import Tags

class TagsNews(DeclarativeBase):
    __tablename__ = "tags_news"

    id = Column(UUID, primary_key=True, default=lambda: str(uuid.uuid4()))
    news_id = Column(UUID, ForeignKey(News.id, ondelete="CASCADE"), nullable=False)
    tag_id = Column(UUID, ForeignKey(Tags.id, ondelete="CASCADE"), nullable=False)

