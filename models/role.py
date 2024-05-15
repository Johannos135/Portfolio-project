from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Role(BaseModel, Base):
  __tablename__ = 'roles'
  name = Column(String(20), unique=True, nullable=False)
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)