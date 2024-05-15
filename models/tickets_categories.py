#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Text, Double


class TicketCategory(BaseModel, Base):
    __tablename__ = 'tickets_categories'
    name = Column(String(128))
    description = Column(Text)
    price_multiplier = Column(Double)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
