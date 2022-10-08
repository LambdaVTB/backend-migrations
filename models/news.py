import uuid
from datetime import datetime

import sqlalchemy as sa
from sqlalchemy import Boolean, Column, String, DateTime, Enum, Computed, Index
from sqlalchemy.dialects.postgresql import UUID, TSVECTOR

from migrator.base import DeclarativeBase

class TSVector(sa.types.TypeDecorator):
    impl = TSVECTOR

class News(DeclarativeBase):
    __tablename__ = "news"

    id = Column(UUID, primary_key=True, default=lambda: str(uuid.uuid4()))
    summary = Column(String, nullable=True)
    raw_text = Column(String, nullable=False)
    processed = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    
    __ts_vector__ = Column(TSVector(), Computed("to_tsvector('russian', raw_text)", persisted=True))

    __table_args__ = (Index("ix_video_ts_vector__", __ts_vector__, postgresql_using="gin"),)


