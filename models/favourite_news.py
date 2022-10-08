import uuid

from sqlalchemy import Boolean, Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, TSVECTOR

from migrator.base import DeclarativeBase
from models.news import News
from models.users import Users

class FavouriteNews(DeclarativeBase):
    __tablename__ = "favourite_news"

    id = Column(UUID, primary_key=True, default=lambda: str(uuid.uuid4()))
    news_id = Column(UUID, ForeignKey(News.id, ondelete="CASCADE"), nullable=False)
    user_id = Column(UUID, ForeignKey(Users.id, ondelete="CASCADE"), nullable=False)

