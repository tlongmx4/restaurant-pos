from sqlalchemy import Column, ForeignKey, Numeric, String
from app.db.base import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Numeric, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Numeric(precision=6, scale=2))