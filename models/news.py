import uuid
from datetime import datetime

import sqlalchemy as sa
from sqlalchemy import Boolean, Column, String, DateTime, Enum, Computed, Index, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, TSVECTOR

from migrator.base import DeclarativeBase
from models.raw import Raw
from enums.news_types import NewsTypes

class News(DeclarativeBase):
    __tablename__ = "news"

    id = Column(UUID, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False)
    news_type = Column(Enum(NewsTypes),nullable=False)
    source = Column(UUID, ForeignKey(Raw.id), nullable=True)
    

