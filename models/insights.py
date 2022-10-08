
import uuid

from sqlalchemy import Boolean, Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID, TSVECTOR

from migrations.migrator.base import DeclarativeBase

class Insights(DeclarativeBase):
    __tablename__ = "insights"

    id = Column(UUID, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False)

