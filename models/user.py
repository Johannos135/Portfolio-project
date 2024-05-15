from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from hashlib import md5


class User(BaseModel, Base):
    __tablename__ = 'users'
    name = Column(String(128))
    email = Column(String(128), unique=True)
    phone_number = Column(String(20), nullable=False, unique=True)
    password = Column(String(20), nullable=False)
    role_id = Column(String(60), ForeignKey('roles.id'))
    role = relationship('Role')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        if name == 'password':
            value = md5((value).encode("utf8")).hexdigest()
        super().__setattr__(name, value)
