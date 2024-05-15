#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, Double, Text
from sqlalchemy.orm import relationship


class Concert(BaseModel, Base):
    __tablename__ = 'concerts'
    artist = Column(String(50), nullable=False)
    venue = Column(String(128), nullable=False)
    date = Column(DateTime, nullable=False)
    gender = Column(Text, nullable=False)
    description = Column(Text)
    image_url = Column(Text)
    tickets = relationship('Ticket', backref='tickets')

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
