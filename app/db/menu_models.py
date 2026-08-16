from sqlalchemy import Column, ForeignKey, Numeric, String, Text
from app.db.base import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Numeric, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String)
    price = Column(Numeric(precision=6, scale=2), nullable=False)