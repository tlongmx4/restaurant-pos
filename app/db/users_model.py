from sqlalchemy import Column, String
from app.db import base
import uuid
from uuid import UUID

class User(base):
    __tablename__ = 'users'
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    name = Column(String)

