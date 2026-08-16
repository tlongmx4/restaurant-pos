from sqlalchemy import Column, String
from app.db.base import Base
import uuid
from uuid import UUID

class User(Base):
    __tablename__ = 'users'
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    name = Column(String)

