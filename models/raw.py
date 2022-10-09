import uuid
from datetime import datetime

import sqlalchemy as sa
from sqlalchemy import Boolean, Column, String, DateTime, Enum, Computed, Index
from sqlalchemy.dialects.postgresql import UUID, TSVECTOR

from migrator.base import DeclarativeBase

class TSVector(sa.types.TypeDecorator):
    impl = TSVECTOR

class Raw(DeclarativeBase):
    __tablename__ = "raw"

    id = Column(UUID, primary_key=True, default=lambda: str(uuid.uuid4()))
    text = Column(String, nullable=False)
    url = Column(String, nullable=False)
    processed = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime(timezone=True), nullable=False)
    
    __ts_vector__ = Column(TSVector(), Computed("to_tsvector('russian', text)", persisted=True))

    __table_args__ = (Index("ix_raw_text_ts_vector__", __ts_vector__, postgresql_using="gin"),)


