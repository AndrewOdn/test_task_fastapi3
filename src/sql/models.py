"""Database models"""
from sqlalchemy import Column, DateTime, Integer, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Statistic(Base):
    """statistic table model"""

    __tablename__ = "statistic"

    date = Column(DateTime, primary_key=True)
    views = Column(Integer)
    clicks = Column(Integer)
    cost = Column(Float)
