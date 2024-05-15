#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Double, ForeignKey, Table
from sqlalchemy.orm import relationship


class TicketLine(Base):
    __tablename__ = 'ticket_line'
    ticket_id = Column(String(60), ForeignKey('tickets.id', ondelete='CASCADE',
                                              onupdate='CASCADE'),
                       primary_key=True)
    ticket_category_id = Column(String(60), ForeignKey('tickets_categories.id',
                                                       ondelete='CASCADE', onupdate='CASCADE'),
                                primary_key=True)
    user_id = Column(String(60), ForeignKey('users.id'))
    total_price = Column(Double)


class Ticket(BaseModel, Base):
    __tablename__ = 'tickets'
    concert_id = Column(String(128), ForeignKey('concerts.id'))
    price = Column(Double, nullable=False)
    tickets_categories = relationship(
        'TicketCategory', secondary='ticket_line', viewonly=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
